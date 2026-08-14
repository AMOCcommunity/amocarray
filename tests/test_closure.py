"""Decomposition / budget closure tests (amocvocab spec section 6.4 + Appendix A).

A registered ``exact`` decomposition makes a checkable promise: its component variables
sum to the total, per element, to within a tolerance. This is the one conformance test
no CF/attribute checker can do — it catches unit errors, sign errors, a missing term, and
a mislabelled component. Appendix A fixed the tolerance at 1e-9 relative (seven decades
below the mildest real error, safely above float32 storage noise).

Each relation is checked against the provider's SOURCE file using the provider's own
variable names (compare in source units; do not convert — Appendix A.1). The files are not
committed (they are large / zipped downloads), so every dataset is ``slow`` and skips
unless available locally via its env var or a cached copy under ``~/.amocatlas_data``.

Relations marked ``must_close=True`` are asserted to close; the MOCHA negatives assert the
check discriminates (Appendix A.3). Relations flagged "hypothesis" below are ones we expect
but have not yet verified against data — when the file is present they will confirm or refute.
"""

import os
from pathlib import Path

import numpy as np
import pytest

REL_TOL = 1e-9  # Appendix A.4


def _resolve(env, filename):
    candidates = [os.environ.get(env)] if os.environ.get(env) else []
    candidates += [
        Path.home() / ".amocatlas_data" / filename,
        Path("/tmp") / filename,
    ]
    for c in candidates:
        if c and Path(c).is_file():
            return Path(c)
    return None


# dataset -> (env var, source filename, [(label, parts, total, must_close)])
DATASETS = {
    "mocha": (
        "AMOCVOCAB_MOCHA_NC",
        "mocha_mht_data_ERA5_v2020.nc",
        [
            ("mocha_mo_subdivision", ["Q_int", "Q_wedge", "Q_eddy"], "Q_mo", True),
            ("mocha_fc_ekman_mo", ["Q_fc", "Q_ek", "Q_mo"], "Q_sum", True),
            ("mocha_ot_gyre", ["Q_ot", "Q_gyre"], "Q_sum", True),
            ("negative:drop_eddy", ["Q_int", "Q_wedge"], "Q_mo", False),
            ("negative:eddy_in_gyre", ["Q_ot", "Q_gyre", "Q_eddy"], "Q_sum", False),
        ],
    ),
    # MOVE: does the boundary/internal/offset decomposition sum to the total transport?
    # Hypothesis (Eleanor): they add, and the offset is inside the sum. Verify when cached.
    "move": (
        "AMOCVOCAB_MOVE_NC",
        "OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc",
        [
            (
                "move_boundary_internal_offset",
                [
                    "transport_component_boundary",
                    "transport_component_internal",
                    "transport_component_internal_offset",
                ],
                "TRANSPORT_TOTAL",
                True,
            ),
        ],
    ),
    # OSNAP: the streamfunction FIELDS add (east + west = total) at every density/time,
    # even though the MOC maxima do not (max is not additive). This is the additive level.
    "osnap_sf": (
        "AMOCVOCAB_OSNAP_SF_NC",
        "OSNAP_Streamfunction_201408_202207_2025.nc",
        [
            ("osnap_east_west_field", ["T_EAST", "T_WEST"], "T_ALL", True),
        ],
    ),
    # RAPID mass balance: Florida Current + Ekman + the five mid-ocean depth layers = 0
    # (section-integrated net transport ~ 0; the small mean is Bering-Strait throughflow).
    # All terms are the same 10-day low-pass ("10") products, so this closes to 0.11 Sv.
    #
    # NOTE (not tested): MOC = FC + Ekman + UMO does NOT close cleanly (spikes to ~2.8 Sv at
    # ~33 short windows) because `moc_mar_hc10` is low-pass filtered AFTER summing while the
    # components are filtered individually; filter-of-sum != sum-of-filters near data gaps.
    # It is a filter-ordering artifact, not a component error. See
    # .claude/rapid-moc-anomaly/ for the plots and the dated event list.
    "rapid": (
        "AMOCVOCAB_RAPID_MOCT_NC",
        "moc_transports.nc",
        [
            (
                "rapid_mass_balance",
                [
                    "t_gs10",
                    "t_ek10",
                    "t_therm10",
                    "t_aiw10",
                    "t_ud10",
                    "t_ld10",
                    "t_bw10",
                ],
                "0",  # sum-to-zero relation: checked with an absolute tolerance
                True,
            ),
        ],
    ),
}

# Absolute tolerance (Sv) for sum-to-zero relations, where a relative tolerance is degenerate.
ZERO_ABS_TOL = 0.2

# Flatten to (dataset, env, filename, label, parts, total, must_close) for parametrize.
_CASES = [
    (ds, env, fn, label, parts, total, must)
    for ds, (env, fn, closures) in DATASETS.items()
    for (label, parts, total, must) in closures
]


@pytest.mark.slow
@pytest.mark.parametrize(
    "dataset,env,filename,label,parts,total,must_close",
    _CASES,
    ids=[c[3] for c in _CASES],
)
def test_closure(dataset, env, filename, label, parts, total, must_close):
    """Component sums reproduce their total to within REL_TOL (spec section 6.4)."""
    path = _resolve(env, filename)
    if path is None:
        pytest.skip(f"{dataset}: {filename} not available (set {env}).")
    import xarray as xr

    ds = xr.open_dataset(path, decode_times=False)
    needed = parts if total == "0" else (*parts, total)
    missing = [v for v in needed if v not in ds.variables]
    if missing:
        pytest.skip(f"{label}: variables not in file: {missing}")

    def val(v):
        a = ds[v].values.astype("f8")
        # Some providers write the netCDF default fill (9.969e36) without declaring
        # _FillValue, so xarray can't mask it (e.g. MOVE). Guard: transports are << 1e30.
        a[np.abs(a) > 1e30] = np.nan
        return a

    lhs = sum(val(v) for v in parts)
    if total == "0":
        # Sum-to-zero relation: relative tolerance is degenerate, use absolute Sv.
        ok = np.isfinite(lhs)
        resid = float(np.max(np.abs(lhs[ok])))
        assert bool(resid < ZERO_ABS_TOL) == must_close, (
            f"{label}: max |sum| {resid:.3f} Sv"
        )
        return
    rhs = val(total)
    ok = np.isfinite(lhs) & np.isfinite(rhs)
    rel = float(np.max(np.abs(lhs - rhs)[ok]) / np.max(np.abs(rhs[ok])))
    # bool()/==, not `is`: numpy comparison never returns the Python singleton.
    assert bool(rel < REL_TOL) == must_close, f"{label}: relative residual {rel:.3e}"
