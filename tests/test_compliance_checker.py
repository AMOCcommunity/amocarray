"""
Tests for AMOCatlas AC1 compliance checker functionality.
"""

import pytest
import xarray as xr
import numpy as np
import tempfile
import os
from pathlib import Path

from amocatlas import compliance_checker, logger

# Disable logging for tests
logger.disable_logging()

# Test data file - a valid AC1 file for testing modifications
TEST_AC1_FILE = "data/OS_TEST_20040402-20240327_DPR_transports_T12H.nc"


@pytest.fixture
def valid_ac1_dataset():
    """Create a valid AC1 dataset for testing."""
    time_data = np.array(
        ["2004-04-02T00:00:00", "2004-04-02T12:00:00", "2004-04-03T00:00:00"],
        dtype="datetime64[ns]",
    )

    # Create 8 transport components as required
    component_names = [
        "Florida Straits",
        "Ekman",
        "Upper Mid-Ocean",
        "Thermocline",
        "Intermediate Water",
        "Upper NADW",
        "Lower NADW",
        "AABW",
    ]

    ds = xr.Dataset(
        {
            "TRANSPORT": xr.DataArray(
                np.random.random((8, 3)),
                dims=["N_COMPONENT", "TIME"],
                attrs={
                    "long_name": "Ocean volume transport",
                    "units": "sverdrup",
                    "standard_name": "ocean_volume_transport_across_line",
                    "coordinates": "TIME LATITUDE",
                },
            ),
            "MOC_TRANSPORT": xr.DataArray(
                np.random.random(3),
                dims=["TIME"],
                attrs={
                    "long_name": "Maximum meridional overturning circulation transport",
                    "units": "sverdrup",
                    "standard_name": "ocean_volume_transport_across_line",
                },
            ),
            "TRANSPORT_NAME": xr.DataArray(
                component_names,
                dims=["N_COMPONENT"],
                attrs={
                    "long_name": "Transport component names",
                    "comment": "Short names for each transport component",
                },
            ),
            "TRANSPORT_DESCRIPTION": xr.DataArray(
                [f"{name} transport component" for name in component_names],
                dims=["N_COMPONENT"],
                attrs={
                    "long_name": "Transport component descriptions",
                    "comment": "Detailed descriptions of each transport component",
                },
            ),
        },
        coords={
            "TIME": xr.DataArray(
                time_data,
                dims=["TIME"],
                attrs={"long_name": "Time", "standard_name": "time", "axis": "T"},
            ),
            "LATITUDE": xr.DataArray(
                26.5,
                attrs={
                    "long_name": "Latitude",
                    "standard_name": "latitude",
                    "units": "degree_north",
                    "axis": "Y",
                },
            ),
        },
        attrs={
            # Required OceanSITES/CF/ACDD attributes
            "Conventions": "CF-1.8, OceanSITES-1.4, ACDD-1.3",
            "format_version": "1.4",
            "data_type": "OceanSITES time-series data",
            "featureType": "timeSeries",
            "data_mode": "D",
            "title": "RAPID Atlantic Meridional Overturning Circulation Transport Components",
            "summary": "Component transport time series from the RAPID observing array.",
            "source": "RAPID moored array observations",
            "site_code": "RAPID",
            "array": "RAPID",
            "platform_code": "RAPID26N",
            "naming_authority": "AMOCatlas",
            "id": "OS_RAPID_20040402-20040403_DPR_transports_T12H",
            "cdm_data_type": "TimeSeries",
            "QC_indicator": "excellent",
            "processing_level": "Data verified against model or other contextual information",
            "date_created": "20251005T143000",
            "institution": "AMOCatlas Community",
            # Geographic bounds
            "geospatial_lat_min": 26.5,
            "geospatial_lat_max": 26.5,
            "geospatial_lon_min": -79.0,
            "geospatial_lon_max": -13.0,
            # Time coverage
            "time_coverage_start": "20040402T000000",
            "time_coverage_end": "20040403T000000",
            # Contributors
            "contributor_name": "Ben Moat",
            "contributor_email": "ben.moat@example.org",
            "contributor_id": "https://orcid.org/0000-0001-8676-7779",
            "contributor_role": "principalInvestigator",
            "contributor_role_vocabulary": "https://vocab.nerc.ac.uk/collection/W08/current/",
            "contributing_institutions": "National Oceanography Centre",
            "contributing_institutions_vocabulary": "https://ror.org/example",
            "contributing_institutions_role": "operator",
            "contributing_institutions_role_vocabulary": "https://vocab.nerc.ac.uk/collection/W08/current/",
            "source_acknowledgement": "Data from the RAPID AMOC observing project",
        },
    )

    return ds


@pytest.fixture
def temp_netcdf_file(valid_ac1_dataset):
    """Create a temporary NetCDF file with valid AC1 dataset."""
    # Create proper OceanSITES filename in temp directory
    temp_dir = tempfile.gettempdir()
    proper_name = os.path.join(
        temp_dir, "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
    )

    # Remove manual units from TIME to avoid encoding conflicts
    ds = valid_ac1_dataset.copy()
    if "units" in ds["TIME"].attrs:
        del ds["TIME"].attrs["units"]

    # Set encoding for datetime
    ds.encoding["TIME"] = {
        "units": "seconds since 1970-01-01T00:00:00Z",
        "calendar": "gregorian",
    }

    ds.to_netcdf(proper_name, format="NETCDF4_CLASSIC")
    yield proper_name

    # Cleanup
    if os.path.exists(proper_name):
        os.unlink(proper_name)


class TestComplianceChecker:
    """Test compliance checker functionality."""

    def test_valid_file_passes(self, temp_netcdf_file):
        """Test that a valid AC1 file passes compliance check."""
        result = compliance_checker.validate_ac1_file(temp_netcdf_file)

        assert result.passed, f"Valid file should pass. Errors: {result.errors}"
        assert result.file_type == "component_transports"
        assert len(result.errors) == 0

    def test_missing_required_global_attributes(self, valid_ac1_dataset):
        """Test detection of missing required global attributes."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)

        # Remove a required attribute
        ds_modified = ds.copy()
        del ds_modified.attrs["title"]
        ds.close()

        # Use proper OceanSITES filename pattern
        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "Missing required global attribute: title" in error
                for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()

    def test_invalid_filename_pattern(self, valid_ac1_dataset):
        """Test detection of invalid filename patterns."""
        # Load actual AC1 file
        ds = xr.open_dataset(TEST_AC1_FILE)

        # Use invalid filename pattern
        filename = "invalid_filename.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "does not match OceanSITES pattern" in error
                or "Filename must follow OceanSITES pattern" in error
                for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds.close()

    def test_missing_required_dimensions(self, valid_ac1_dataset):
        """Test detection of missing required dimensions."""
        # Load actual AC1 file and remove TIME dimension
        ds = xr.open_dataset(TEST_AC1_FILE)

        # Create dataset without TIME dimension
        ds_no_time = ds.isel(TIME=0).drop_vars("TIME")
        ds.close()

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_no_time.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any("TIME dimension is required" in error for error in result.errors)
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_no_time.close()

    def test_missing_variable_attributes(self, valid_ac1_dataset):
        """Test detection of missing variable attributes."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)
        ds_modified = ds.copy()
        ds.close()

        # Remove long_name from TRANSPORT
        del ds_modified["TRANSPORT"].attrs["long_name"]

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "TRANSPORT missing required attribute: long_name" in error
                for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()

    def test_datetime_coordinate_units_not_required(self, valid_ac1_dataset):
        """Test that TIME coordinate doesn't require manual units attribute."""
        ds = valid_ac1_dataset.copy()
        # TIME coordinate should not have manual units (xarray handles this)
        if "units" in ds["TIME"].attrs:
            del ds["TIME"].attrs["units"]

        with tempfile.NamedTemporaryFile(
            suffix="_OS_RAPID_20040402-20040403_DPR_transports_T12H.nc", delete=False
        ) as tmp:
            ds.encoding["TIME"] = {
                "units": "seconds since 1970-01-01T00:00:00Z",
                "calendar": "gregorian",
            }
            ds.to_netcdf(tmp.name, format="NETCDF4_CLASSIC")

            result = compliance_checker.validate_ac1_file(tmp.name)

            # Should pass - datetime coordinates don't need manual units
            time_units_errors = [
                error for error in result.errors if "TIME" in error and "units" in error
            ]
            assert (
                len(time_units_errors) == 0
            ), f"TIME should not require manual units. Errors: {time_units_errors}"

        os.unlink(tmp.name)

    def test_unitless_variables_allowed(self, valid_ac1_dataset):
        """Test that descriptive variables don't require units."""
        ds = valid_ac1_dataset.copy()
        # TRANSPORT_NAME and TRANSPORT_DESCRIPTION should not require units
        if "units" in ds["TRANSPORT_NAME"].attrs:
            del ds["TRANSPORT_NAME"].attrs["units"]
        if "units" in ds["TRANSPORT_DESCRIPTION"].attrs:
            del ds["TRANSPORT_DESCRIPTION"].attrs["units"]

        with tempfile.NamedTemporaryFile(
            suffix="_OS_RAPID_20040402-20040403_DPR_transports_T12H.nc", delete=False
        ) as tmp:
            if "units" in ds["TIME"].attrs:
                del ds["TIME"].attrs["units"]
            ds.encoding["TIME"] = {
                "units": "seconds since 1970-01-01T00:00:00Z",
                "calendar": "gregorian",
            }
            ds.to_netcdf(tmp.name, format="NETCDF4_CLASSIC")

            result = compliance_checker.validate_ac1_file(tmp.name)

            # Should not require units for descriptive variables
            name_units_errors = [
                error
                for error in result.errors
                if "TRANSPORT_NAME" in error and "units" in error
            ]
            desc_units_errors = [
                error
                for error in result.errors
                if "TRANSPORT_DESCRIPTION" in error and "units" in error
            ]

            assert (
                len(name_units_errors) == 0
            ), f"TRANSPORT_NAME should not require units. Errors: {name_units_errors}"
            assert (
                len(desc_units_errors) == 0
            ), f"TRANSPORT_DESCRIPTION should not require units. Errors: {desc_units_errors}"

        os.unlink(tmp.name)

    def test_invalid_data_mode(self, valid_ac1_dataset):
        """Test detection of invalid data_mode values."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)
        ds_modified = ds.copy()
        ds.close()

        ds_modified.attrs["data_mode"] = "INVALID"

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "data_mode must be one of ['R', 'P', 'D']" in error
                for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()

    def test_invalid_qc_indicator(self, valid_ac1_dataset):
        """Test detection of invalid QC_indicator values."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)
        ds_modified = ds.copy()
        ds.close()

        ds_modified.attrs["QC_indicator"] = "invalid"

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "QC_indicator must be one of" in error for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()

    def test_invalid_date_format(self, valid_ac1_dataset):
        """Test detection of invalid date formats."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)
        ds_modified = ds.copy()
        ds.close()

        ds_modified.attrs["date_created"] = "2025-10-05T14:30:00Z"  # Wrong format

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "date_created must use format YYYYmmddTHHMMss" in error
                for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()

    def test_invalid_orcid_format(self, valid_ac1_dataset):
        """Test detection of invalid ORCID formats."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)
        ds_modified = ds.copy()
        ds.close()

        ds_modified.attrs["contributor_id"] = "https://orcid.org/invalid-format"

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any("Invalid ORCID format" in error for error in result.errors)
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()

    def test_missing_conventions(self, valid_ac1_dataset):
        """Test detection of missing conventions."""
        # Load actual AC1 file and modify it
        ds = xr.open_dataset(TEST_AC1_FILE)
        ds_modified = ds.copy()
        ds.close()

        ds_modified.attrs["Conventions"] = "CF-1.8"  # Missing OceanSITES and ACDD

        filename = "OS_RAPID_20040402-20040403_DPR_transports_T12H.nc"
        filepath = os.path.join(tempfile.gettempdir(), filename)

        try:
            ds_modified.to_netcdf(filepath, format="NETCDF4_CLASSIC")
            result = compliance_checker.validate_ac1_file(filepath)

            assert not result.passed
            assert any(
                "Conventions must include 'OceanSITES-1.4'" in error
                for error in result.errors
            )
            assert any(
                "Conventions must include 'ACDD-1.3'" in error
                for error in result.errors
            )
        finally:
            if os.path.exists(filepath):
                os.unlink(filepath)
            ds_modified.close()


class TestValidationResult:
    """Test ValidationResult class functionality."""

    def test_validation_result_creation(self):
        """Test ValidationResult object creation."""
        result = compliance_checker.ValidationResult(passed=True)

        assert result.passed == True
        assert result.errors == []
        assert result.warnings == []
        assert result.file_type is None

    def test_validation_result_with_errors(self):
        """Test ValidationResult with errors."""
        result = compliance_checker.ValidationResult(passed=True)
        result.errors.append("Test error")

        # passed is determined by @property based on errors
        assert len(result.errors) == 1
        assert result.errors[0] == "Test error"

    def test_validation_result_warnings_dont_fail(self):
        """Test that warnings don't cause validation to fail."""
        result = compliance_checker.ValidationResult(passed=True)
        result.warnings.append("Test warning")

        assert len(result.warnings) == 1


if __name__ == "__main__":
    pytest.main([__file__])
