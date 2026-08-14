"""SCOTIA (Scotland-Canada) overturning closure tests.

Split into its own ``test_closure_<array>.py`` (one per array) so matching an array to its
registered closures stays a one-file lookup as the vocabulary is populated.

SCOTIA's diagnostics are computed in neutral-density space and close exactly on the
provider's float64 netCDF (residuals at float rounding, not a physical tolerance):

  MOC(t)      = max over gamma of PSI(t, gamma)            -> exact
  PSI(t,g)    = cumulative sum over gamma of TRANS(t, g)   -> exact
  sum_g TRANS = 0  (net section transport, mass-conserved) -> exact

The file is a download, so every case is ``slow`` and skips unless available locally
(env var ``SCOTIA_NC``, ``~/.amocatlas_data`` or ``/tmp``).
"""

import numpy as np
import pytest
import xarray as xr
from closure_utils import resolve_data

_SCOTIA_NC = "SCOTIA_overturning_diagnostics.nc"

# Float64 budgets: residual should sit at rounding, not a physical few-percent tolerance.
EXACT_TOL = 1e-9  # Sverdrup


def _load():
    path = resolve_data("SCOTIA_NC", _SCOTIA_NC)
    if path is None:
        pytest.skip(f"{_SCOTIA_NC} not available locally; set SCOTIA_NC to run")
    return xr.open_dataset(path)


@pytest.mark.slow
def test_moc_is_density_max_of_streamfunction():
    """MOC = maximum over neutral density of the overturning streamfunction."""
    ds = _load()
    resid = np.abs(ds["moc"].values - ds["psi"].max("gamma_n_bin").values)
    assert resid.max() < EXACT_TOL, f"max|MOC - max_g PSI| = {resid.max():.2e} Sv"


@pytest.mark.slow
def test_streamfunction_is_cumulative_transport():
    """PSI(gamma) = cumulative sum of the transport-by-class over neutral density."""
    ds = _load()
    resid = np.abs(ds["psi"].values - ds["transport"].cumsum("gamma_n_bin").values)
    assert resid.max() < EXACT_TOL, f"max|PSI - cumsum_g TRANS| = {resid.max():.2e} Sv"


@pytest.mark.slow
def test_net_section_transport_is_zero():
    """Transport summed over all density classes is the (near-zero) net section transport."""
    ds = _load()
    net = np.abs(ds["transport"].sum("gamma_n_bin").values)
    assert net.max() < EXACT_TOL, f"max|sum_g TRANS| = {net.max():.2e} Sv"
