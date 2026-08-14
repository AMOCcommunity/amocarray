"""Tests for the SCOTIA reader (Fox et al. 2026, SAMS THREDDS).

The fast tests check registration and metadata validity without network. The integration
test downloads the diagnostics file and verifies the neutral-density coordinate, variable
naming and CF-case attributes after standardisation.
"""

import numpy as np
import pytest

from amocatlas import read
from amocatlas.utilities import validate_array_yaml


def test_scotia_registered():
    assert "scotia" in read.__all__
    assert callable(read.scotia)


def test_scotia_metadata_valid():
    # Raises on failure; passes silently otherwise.
    validate_array_yaml("scotia")


@pytest.mark.slow
def test_scotia_neutral_density_diagnostics():
    """read.scotia() returns overturning diagnostics on a neutral-density coordinate.

    The single diagnostics file carries the overturning streamfunction and transport-by-class
    on a neutral-density (gamma-n) axis, plus scalar time series (MOC, gamma at the MOC,
    heat/freshwater/density fluxes).
    """
    ds = read.scotia()
    if isinstance(ds, list):
        ds = ds[0]

    assert set(ds.dims) == {"TIME", "GAMMA"}
    assert ds.sizes["TIME"] == 246
    assert ds.sizes["GAMMA"] == 2000
    assert {
        "MOC_GAMMA",
        "PSI_GAMMA",
        "TRANS_GAMMA",
        "MHT",
        "MFT",
        "DENSITY_FLUX",
        "GAMMA_MOC",
    } <= set(ds.data_vars)

    assert str(ds["TIME"].values[0])[:7] == "2004-01"
    assert str(ds["TIME"].values[-1])[:7] == "2024-06"

    # The bin-bound arrays are dropped in v1; only the bin centres are served.
    assert "gamma_n_lower" not in ds.variables
    assert "gamma_n_upper" not in ds.variables

    # Neutral-density coordinate carries the CF standard_name.
    assert ds["GAMMA"].attrs["standard_name"] == "sea_water_neutral_density"
    assert ds["GAMMA"].attrs["units"] == "kg m-3"

    # Streamfunction quantities: overturning streamfunction; MOC is its density-space maximum.
    assert (
        ds["MOC_GAMMA"].attrs["standard_name"]
        == "ocean_meridional_overturning_streamfunction"
    )
    assert ds["MOC_GAMMA"].attrs["cell_methods"] == "GAMMA: maximum"
    assert ds["MOC_GAMMA"].dims == ("TIME",)
    assert ds["PSI_GAMMA"].dims == ("TIME", "GAMMA")
    assert ds["TRANS_GAMMA"].dims == ("TIME", "GAMMA")

    # Heat transport is CF (PW convertible to W); freshwater transport is not (Sverdrup vs
    # CF kg s-1) so it carries no standard_name; transport-by-class has no CF name either.
    assert ds["MHT"].attrs["standard_name"] == "northward_ocean_heat_transport"
    assert ds["MFT"].attrs.get("standard_name") in (None, "")
    assert ds["TRANS_GAMMA"].attrs.get("standard_name") in (None, "")

    # Neutral density at the overturning maximum is itself a neutral density.
    assert ds["GAMMA_MOC"].attrs["standard_name"] == "sea_water_neutral_density"

    assert np.isfinite(ds["MOC_GAMMA"].values).all()
