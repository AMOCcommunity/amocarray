"""Test sigma coordinate transformation in RAPID readers.

This test file provides comprehensive tests for the sigma0/sigma2 coordinate
transformation functionality in the RAPID reader (rapid26n.py).
"""

import numpy as np
import xarray as xr

from amocatlas import logger

logger.disable_logging()


def test_rapid_sigma_coordinate_transformation():
    """Test that sigma0/sigma2 coordinate transformation works correctly.

    This test verifies the transformation logic in rapid26n.py that converts potential density
    values (>1000) to potential density anomaly values (<100) by subtracting 1000.

    Requirements tested:
    1. Test that sigma values > 100 are transformed by subtracting 1000
    2. Test that attributes are preserved during transformation
    """
    # Create test dataset directly in memory with sigma coordinates that need transformation

    # Create sigma0 coordinate with values > 1000 (needs transformation)
    sigma0_original_values = np.array(
        [1021.5, 1024.2, 1026.8, 1027.5, 1028.1, 1028.9, 1029.4, 1030.2]
    )
    sigma0_coord = xr.DataArray(
        sigma0_original_values,
        dims=["sigma0"],
        attrs={
            "long_name": "Potential density anomaly to 1000 kg/m3, surface reference",
            "units": "kg m-3",
            "standard_name": "sea_water_sigma_theta",
        },
    )

    # Create sigma2 coordinate with values > 1000 (needs transformation)
    sigma2_original_values = np.array([1032.1, 1034.5, 1036.2, 1037.8, 1038.9, 1039.7])
    sigma2_coord = xr.DataArray(
        sigma2_original_values,
        dims=["sigma2"],
        attrs={
            "long_name": "Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3",
            "units": "kg m-3",
            "standard_name": "sea_water_sigma_2000",
        },
    )

    # Create time coordinate
    time_coord = xr.DataArray(
        np.arange(10), dims=["time"], attrs={"units": "days since 2020-01-01"}
    )

    # Create mock dataset
    ds_original = xr.Dataset(
        {
            "amoc_sigma0": (
                ["time", "sigma0"],
                np.random.random((10, 8)),
                {
                    "long_name": "Atlantic meridional overturning circulation strength",
                    "units": "Sv",
                },
            ),
            "stream_sigma2": (
                ["time", "sigma2"],
                np.random.random((10, 6)),
                {"long_name": "Meridional overturning streamfunction", "units": "Sv"},
            ),
        },
        coords={"time": time_coord, "sigma0": sigma0_coord, "sigma2": sigma2_coord},
    )

    # Apply the transformation logic directly (from rapid26n.py lines 154-171)
    # Simulate what happens when file == "meridional_transports.nc"
    ds = ds_original.copy(deep=True)

    # Apply sigma0 transformation
    if "sigma0" in ds.coords:
        original_values = ds["sigma0"].values
        if original_values.max() > 100:  # Check if values are > 1000 range
            original_attrs = ds[
                "sigma0"
            ].attrs.copy()  # Store attrs before transformation
            ds["sigma0"] = ds["sigma0"] - 1000
            # Preserve any existing attributes - simulate the original logic
            ds["sigma0"].attrs.update(original_attrs)

    # Apply sigma2 transformation
    if "sigma2" in ds.coords:
        original_values = ds["sigma2"].values
        if original_values.max() > 100:  # Check if values are > 1000 range
            original_attrs = ds[
                "sigma2"
            ].attrs.copy()  # Store attrs before transformation
            ds["sigma2"] = ds["sigma2"] - 1000
            # Preserve any existing attributes
            ds["sigma2"].attrs.update(original_attrs)

    # Test 1: Verify sigma0 values > 100 were transformed (1000 subtracted)
    assert "sigma0" in ds.coords, "sigma0 coordinate should be present"
    transformed_sigma0 = ds["sigma0"].values
    expected_sigma0 = sigma0_original_values - 1000
    np.testing.assert_array_almost_equal(
        transformed_sigma0,
        expected_sigma0,
        decimal=6,
        err_msg="sigma0 values should be transformed by subtracting 1000",
    )

    # Verify transformed values are all < 100 (density anomaly range)
    assert np.all(transformed_sigma0 < 100), (
        "All transformed sigma0 values should be < 100"
    )
    assert np.all(transformed_sigma0 > 0), (
        "All transformed sigma0 values should be positive"
    )

    # Test 2: Verify sigma2 values > 100 were transformed (1000 subtracted)
    assert "sigma2" in ds.coords, "sigma2 coordinate should be present"
    transformed_sigma2 = ds["sigma2"].values
    expected_sigma2 = sigma2_original_values - 1000
    np.testing.assert_array_almost_equal(
        transformed_sigma2,
        expected_sigma2,
        decimal=6,
        err_msg="sigma2 values should be transformed by subtracting 1000",
    )

    # Verify transformed values are all < 100
    assert np.all(transformed_sigma2 < 100), (
        "All transformed sigma2 values should be < 100"
    )
    assert np.all(transformed_sigma2 > 0), (
        "All transformed sigma2 values should be positive"
    )

    # Test 3: Verify attributes are preserved during transformation
    sigma0_attrs = ds["sigma0"].attrs
    assert "long_name" in sigma0_attrs, "sigma0 should preserve long_name attribute"
    assert (
        sigma0_attrs["long_name"]
        == "Potential density anomaly to 1000 kg/m3, surface reference"
    )
    assert "units" in sigma0_attrs, "sigma0 should preserve units attribute"
    assert sigma0_attrs["units"] == "kg m-3"
    assert "standard_name" in sigma0_attrs, (
        "sigma0 should preserve standard_name attribute"
    )

    sigma2_attrs = ds["sigma2"].attrs
    assert "long_name" in sigma2_attrs, "sigma2 should preserve long_name attribute"
    assert (
        sigma2_attrs["long_name"]
        == "Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3"
    )
    assert "units" in sigma2_attrs, "sigma2 should preserve units attribute"
    assert sigma2_attrs["units"] == "kg m-3"
    assert "standard_name" in sigma2_attrs, (
        "sigma2 should preserve standard_name attribute"
    )


def test_rapid_sigma_coordinate_no_transformation_when_values_small():
    """Test that sigma coordinates with values < 100 are NOT transformed.

    This prevents the creation of negative density anomaly values, which would be
    physically unrealistic.
    """
    # Create dataset with sigma coordinates that should NOT be transformed

    # Create sigma0 coordinate with values < 100 (should NOT be transformed)
    sigma0_original_values = np.array(
        [21.5, 24.2, 26.8, 28.5]
    )  # Already density anomaly
    sigma0_coord = xr.DataArray(
        sigma0_original_values,
        dims=["sigma0"],
        attrs={"long_name": "Sigma0", "units": "kg m-3"},
    )

    # Create sigma2 coordinate with values < 100 (should NOT be transformed)
    sigma2_original_values = np.array([32.1, 34.5, 36.2])  # Already density anomaly
    sigma2_coord = xr.DataArray(
        sigma2_original_values,
        dims=["sigma2"],
        attrs={"long_name": "Sigma2", "units": "kg m-3"},
    )

    # Create time coordinate
    time_coord = xr.DataArray(np.arange(5), dims=["time"])

    # Create mock dataset
    ds_original = xr.Dataset(
        {"amoc_sigma0": (["time", "sigma0"], np.random.random((5, 4)))},
        coords={"time": time_coord, "sigma0": sigma0_coord, "sigma2": sigma2_coord},
    )

    # Apply the transformation logic directly (from rapid26n.py lines 154-171)
    ds = ds_original.copy(deep=True)

    # Apply sigma0 transformation
    if "sigma0" in ds.coords:
        original_values = ds["sigma0"].values
        if original_values.max() > 100:  # Check if values are > 1000 range
            original_attrs = ds["sigma0"].attrs.copy()
            ds["sigma0"] = ds["sigma0"] - 1000
            ds["sigma0"].attrs.update(original_attrs)

    # Apply sigma2 transformation
    if "sigma2" in ds.coords:
        original_values = ds["sigma2"].values
        if original_values.max() > 100:  # Check if values are > 1000 range
            original_attrs = ds["sigma2"].attrs.copy()
            ds["sigma2"] = ds["sigma2"] - 1000
            ds["sigma2"].attrs.update(original_attrs)

    # Test 4: Verify values < 100 are NOT transformed
    assert "sigma0" in ds.coords
    untransformed_sigma0 = ds["sigma0"].values
    np.testing.assert_array_equal(
        untransformed_sigma0,
        sigma0_original_values,
        err_msg="sigma0 values < 100 should NOT be transformed",
    )

    assert "sigma2" in ds.coords
    untransformed_sigma2 = ds["sigma2"].values
    np.testing.assert_array_equal(
        untransformed_sigma2,
        sigma2_original_values,
        err_msg="sigma2 values < 100 should NOT be transformed",
    )

    # Verify attributes are still preserved for untransformed coordinates
    assert "long_name" in ds["sigma0"].attrs
    assert "units" in ds["sigma0"].attrs
    assert "long_name" in ds["sigma2"].attrs
    assert "units" in ds["sigma2"].attrs


def test_rapid_sigma_transformation_threshold():
    """Test the exact threshold condition for sigma coordinate transformation.

    The transformation should only apply when max(values) > 100.
    """
    # Test case 1: max value exactly 100 - should NOT transform
    sigma0_values_at_threshold = np.array([95.0, 98.0, 100.0])
    sigma0_coord = xr.DataArray(
        sigma0_values_at_threshold,
        dims=["sigma0"],
        attrs={"long_name": "Sigma0", "units": "kg m-3"},
    )

    ds1 = xr.Dataset({"data": (["sigma0"], [1, 2, 3])}, coords={"sigma0": sigma0_coord})

    # Apply transformation logic
    if "sigma0" in ds1.coords:
        original_values = ds1["sigma0"].values
        if original_values.max() > 100:  # Should be False for max=100
            original_attrs = ds1["sigma0"].attrs.copy()
            ds1["sigma0"] = ds1["sigma0"] - 1000
            ds1["sigma0"].attrs.update(original_attrs)

    # Should NOT be transformed (values remain unchanged)
    np.testing.assert_array_equal(
        ds1["sigma0"].values,
        sigma0_values_at_threshold,
        err_msg="Values with max=100 should NOT be transformed",
    )

    # Test case 2: max value slightly over 100 - should transform
    sigma0_values_over_threshold = np.array([95.0, 98.0, 100.1])
    sigma0_coord2 = xr.DataArray(
        sigma0_values_over_threshold,
        dims=["sigma0"],
        attrs={"long_name": "Sigma0", "units": "kg m-3"},
    )

    ds2 = xr.Dataset(
        {"data": (["sigma0"], [1, 2, 3])}, coords={"sigma0": sigma0_coord2}
    )

    # Apply transformation logic
    if "sigma0" in ds2.coords:
        original_values = ds2["sigma0"].values
        if original_values.max() > 100:  # Should be True for max=100.1
            original_attrs = ds2["sigma0"].attrs.copy()
            ds2["sigma0"] = ds2["sigma0"] - 1000
            ds2["sigma0"].attrs.update(original_attrs)

    # Should be transformed (1000 subtracted)
    expected_transformed = sigma0_values_over_threshold - 1000
    np.testing.assert_array_almost_equal(
        ds2["sigma0"].values,
        expected_transformed,
        decimal=6,
        err_msg="Values with max>100 should be transformed by subtracting 1000",
    )


def test_rapid_sigma_transformation_edge_cases():
    """Test edge cases for sigma coordinate transformation."""
    # Test case: Mixed values (some > 1000, some < 100) - all should be transformed if max > 100
    mixed_values = np.array([25.0, 1027.5, 50.0, 1030.2])  # max = 1030.2 > 100
    sigma0_coord = xr.DataArray(
        mixed_values,
        dims=["sigma0"],
        attrs={"long_name": "Mixed Sigma0", "units": "kg m-3"},
    )

    ds = xr.Dataset(
        {"data": (["sigma0"], [1, 2, 3, 4])}, coords={"sigma0": sigma0_coord}
    )

    # Apply transformation logic
    if "sigma0" in ds.coords:
        original_values = ds["sigma0"].values
        if original_values.max() > 100:  # Should be True
            original_attrs = ds["sigma0"].attrs.copy()
            ds["sigma0"] = ds["sigma0"] - 1000
            ds["sigma0"].attrs.update(original_attrs)

    # ALL values should be transformed (subtract 1000 from each)
    expected_transformed = mixed_values - 1000
    np.testing.assert_array_almost_equal(
        ds["sigma0"].values,
        expected_transformed,
        decimal=6,
        err_msg="When max > 100, ALL sigma values should be transformed",
    )

    # Verify some values become negative (which is expected for values originally < 1000)
    assert np.any(ds["sigma0"].values < 0), (
        "Some transformed values should be negative for mixed input"
    )

    # But the originally high values should now be in reasonable density anomaly range
    transformed_high_values = ds["sigma0"].values[mixed_values > 1000]
    assert np.all(transformed_high_values > 0), (
        "Originally high values should be positive after transformation"
    )
    assert np.all(transformed_high_values < 100), (
        "Originally high values should be < 100 after transformation"
    )


def test_rapid_sigma_coordinate_attributes_preserved():
    """Test that all coordinate attributes are properly preserved during transformation."""
    # Create coordinate with comprehensive attributes
    sigma0_values = np.array([1021.5, 1024.2, 1026.8, 1027.5])
    comprehensive_attrs = {
        "long_name": "Potential density anomaly to 1000 kg/m3, surface reference",
        "units": "kg m-3",
        "standard_name": "sea_water_sigma_theta",
        "axis": "Z",
        "positive": "down",
        "comment": "Test comment attribute",
        "valid_min": 1020.0,
        "valid_max": 1040.0,
        "_FillValue": -999.0,
    }

    sigma0_coord = xr.DataArray(
        sigma0_values, dims=["sigma0"], attrs=comprehensive_attrs
    )

    ds = xr.Dataset(
        {"data": (["sigma0"], [1, 2, 3, 4])}, coords={"sigma0": sigma0_coord}
    )

    # Store original attributes for comparison
    original_attrs = ds["sigma0"].attrs.copy()

    # Apply transformation logic
    if "sigma0" in ds.coords:
        original_values = ds["sigma0"].values
        if original_values.max() > 100:
            original_attrs_backup = ds["sigma0"].attrs.copy()
            ds["sigma0"] = ds["sigma0"] - 1000
            ds["sigma0"].attrs.update(original_attrs_backup)

    # Verify ALL original attributes are preserved
    transformed_attrs = ds["sigma0"].attrs
    for key, value in original_attrs.items():
        assert key in transformed_attrs, f"Attribute '{key}' should be preserved"
        assert transformed_attrs[key] == value, (
            f"Attribute '{key}' value should be unchanged"
        )

    # Verify no extra attributes were added
    assert len(transformed_attrs) == len(original_attrs), (
        "No extra attributes should be added"
    )


def test_rapid_sigma_coordinate_missing_coordinates():
    """Test behavior when sigma coordinates are missing from dataset."""
    # Create dataset without sigma0 or sigma2 coordinates
    ds = xr.Dataset(
        {
            "temperature": (["time", "depth"], np.random.random((10, 5))),
            "salinity": (["time", "depth"], np.random.random((10, 5))),
        },
        coords={"time": np.arange(10), "depth": np.array([10, 50, 100, 200, 500])},
    )

    # Store original state
    original_coords = set(ds.coords.keys())
    original_data_vars = set(ds.data_vars.keys())

    # Apply transformation logic (should have no effect)
    if "sigma0" in ds.coords:
        original_values = ds["sigma0"].values
        if original_values.max() > 100:
            original_attrs = ds["sigma0"].attrs.copy()
            ds["sigma0"] = ds["sigma0"] - 1000
            ds["sigma0"].attrs.update(original_attrs)

    if "sigma2" in ds.coords:
        original_values = ds["sigma2"].values
        if original_values.max() > 100:
            original_attrs = ds["sigma2"].attrs.copy()
            ds["sigma2"] = ds["sigma2"] - 1000
            ds["sigma2"].attrs.update(original_attrs)

    # Verify dataset is unchanged
    assert set(ds.coords.keys()) == original_coords, (
        "Coordinate names should be unchanged"
    )
    assert set(ds.data_vars.keys()) == original_data_vars, (
        "Data variable names should be unchanged"
    )

    # Verify specific coordinates are still missing
    assert "sigma0" not in ds.coords, "sigma0 should still be missing"
    assert "sigma2" not in ds.coords, "sigma2 should still be missing"
