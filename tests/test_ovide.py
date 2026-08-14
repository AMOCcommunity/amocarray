"""Tests for the OVIDE reader (SEANOE 10.17882/46445).

The fast tests check registration and metadata validity without network. The integration
test downloads the file and verifies the two-index merge onto a single TIME axis.
"""

import numpy as np
import pytest

from amocatlas import read
from amocatlas.utilities import validate_array_yaml


def test_ovide_registered():
    assert "ovide" in read.__all__
    assert callable(read.ovide)


def test_ovide_metadata_valid():
    # Raises on failure; passes silently otherwise.
    validate_array_yaml("ovide")


@pytest.mark.slow
def test_ovide_merges_two_indices_onto_one_time():
    """read.ovide() returns one dataset on a single 1993-2015 TIME axis.

    The file has MOC_index_AVISO (1993-2015) and MOC_index_ISAS/err (2002-2015) on separate
    monthly axes that coincide; the reader reindexes the ISAS series onto the AVISO axis
    (NaN before 2002), so all three share one TIME.
    """
    ds = read.ovide()
    if isinstance(ds, list):
        ds = ds[0]

    assert set(ds.dims) == {"TIME"}
    assert ds.sizes["TIME"] == 276
    assert {"MOC_SIGMA1", "MOC_SIGMA1_PROXY", "MOC_SIGMA1_ERR"} <= set(ds.data_vars)

    # The proxy spans the full record; the ISAS index/error start in 2002 -> NaN before.
    assert np.isfinite(ds["MOC_SIGMA1_PROXY"].values).sum() == 276
    assert np.isfinite(ds["MOC_SIGMA1"].values).sum() == 168
    assert np.isfinite(ds["MOC_SIGMA1_ERR"].values).sum() == 168

    assert str(ds["TIME"].values[0])[:7] == "1993-01"
    assert str(ds["TIME"].values[-1])[:7] == "2015-12"

    # MOC is the sigma1-space overturning maximum; the uncertainty carries no standard_name.
    assert (
        ds["MOC_SIGMA1"].attrs["standard_name"]
        == "ocean_meridional_overturning_streamfunction"
    )
    assert ds["MOC_SIGMA1"].attrs["cell_methods"] == "SIGMA1: maximum"
    assert ds["MOC_SIGMA1_ERR"].attrs.get("standard_name") in (None, "")
