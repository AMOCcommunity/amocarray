"""SAMBA (34.5S) decomposition closure tests — amocvocab spec section 6.4 + Appendix A.

Split into its own file (one ``test_closure_<array>.py`` per array) so that matching an
array to its registered closures stays a one-file lookup as the vocabulary is populated.

SAMBA's MOC-anomaly constituents come from a whitespace ``.asc`` rounded to 0.01 Sv and
contain sparse single-day glitch rows (~7% of rows spike by several Sv). Closure is
therefore checked on the MEDIAN absolute residual (robust to those glitches), not the max
used for the exact float64 netCDF budgets in ``test_closure.py``.

Two tiers are asserted (both checked against the provider source file, in source units —
Appendix A.1):
  exact       — components sum to the total within the provider's rounding step;
  approximate — components reconstruct the total within a stated physical tolerance (a real
                few-percent residual, not rounding).
The approximate bound is two-sided: the median must be below APPROX_TOL (it does close
roughly) AND at or above EXACT_TOL (it is genuinely approximate, not exact), so the tier
label stays meaningful. The file is a large download, so every case is ``slow`` and skips
unless the source is available locally. See ``.claude/samba-closure/`` for the plots.

Observed tiers (v2020 source, 1957 daily records):
  relative  = W_density + E_density   -> exact       (median 0.01 Sv)
  reference = W_botpres + E_botpres    -> approximate (median 0.15 Sv)
  total     = relative + reference + ekman -> approximate (median 0.31 Sv / 0.15 robust)
"""

import numpy as np
import pytest
from closure_utils import resolve_data

_SAMBA_ASC = "MOC_TotalAnomaly_and_constituents.asc"
_SAMBA_COLS = {  # 0-indexed data column in the .asc (cols 1-4 are Year/Month/Day/Hour)
    "total": 4,
    "relative": 5,
    "reference": 6,
    "ekman": 7,
    "w_density": 8,
    "e_density": 9,
    "w_botpres": 10,
    "e_botpres": 11,
}
SAMBA_EXACT_TOL = 0.02  # Sv — twice the provider's 0.01 Sv rounding step
SAMBA_APPROX_TOL = 0.5  # Sv — an "approximate" reconstruction of the total

_SAMBA_CASES = [
    (
        "samba_relative=Wdensity+Edensity",
        ["w_density", "e_density"],
        "relative",
        "exact",
    ),
    (
        "samba_reference=Wbotpres+Ebotpres",
        ["w_botpres", "e_botpres"],
        "reference",
        "approximate",
    ),
    (
        "samba_total=relative+reference+ekman",
        ["relative", "reference", "ekman"],
        "total",
        "approximate",
    ),
]


@pytest.mark.slow
@pytest.mark.parametrize(
    "label,parts,total,tier", _SAMBA_CASES, ids=[c[0] for c in _SAMBA_CASES]
)
def test_samba_closure(label, parts, total, tier):
    """SAMBA constituent sums reproduce their parent at the declared closure tier."""
    path = resolve_data("AMOCVOCAB_SAMBA_ASC", _SAMBA_ASC)
    if path is None:
        pytest.skip(f"samba: {_SAMBA_ASC} not available (set AMOCVOCAB_SAMBA_ASC).")

    rows = []
    with open(path) as fh:
        for line in fh:
            if line.startswith("%") or not line.strip():
                continue
            rows.append([float(x) for x in line.split()])
    d = np.array(rows)

    lhs = sum(d[:, _SAMBA_COLS[p]] for p in parts)
    rhs = d[:, _SAMBA_COLS[total]]
    resid = np.abs(lhs - rhs)
    resid = resid[np.isfinite(resid)]
    med = float(np.median(resid))

    if tier == "exact":
        assert med < SAMBA_EXACT_TOL, f"{label}: median |res| {med:.3f} Sv (want exact)"
    elif tier == "approximate":
        assert SAMBA_EXACT_TOL <= med < SAMBA_APPROX_TOL, (
            f"{label}: median |res| {med:.3f} Sv (want approximate, "
            f"[{SAMBA_EXACT_TOL}, {SAMBA_APPROX_TOL}) Sv)"
        )
    else:
        raise AssertionError(f"unknown closure tier {tier!r}")
