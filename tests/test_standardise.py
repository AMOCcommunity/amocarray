"""Tests for amocatlas.standardise module.

Tests the standardization pipeline including metadata application,
variable renaming, and dataset enrichment.
"""

import pytest
import xarray as xr
import pandas as pd

from amocatlas import standardise, readers
from amocatlas.logger import disable_logging

# Disable logging for cleaner test output
disable_logging()


class TestStandardizeData:
    """Integration tests for data standardization."""

    @pytest.mark.slow
    def test_standardise_data_rapid(self):
        """Test end-to-end standardization of RAPID data."""
        # Load raw RAPID data
        raw_datasets = readers.load_dataset("rapid")
        raw_dataset = raw_datasets[0]  # Transport file

        # Standardize the data
        standardized = standardise.standardise_data(
            raw_dataset, file_name="moc_transports.nc"
        )

        # Should have AMOCatlas metadata
        assert "processing_datasource" in standardized.attrs
        assert standardized.attrs["processing_datasource"] == "rapid26n"

        # Should have applied variable mapping
        assert "applied_variable_mapping" in standardized.attrs
        mapping = standardized.attrs["applied_variable_mapping"]
        assert isinstance(mapping, dict)
        assert len(mapping) > 0

        # Should have standardized variable names
        std_vars = list(standardized.data_vars)

        # MOC variable should be present and standardized
        assert "MOC" in std_vars

        # Time coordinate should be standardized
        assert "TIME" in standardized.coords

        # Should have processing metadata
        assert "date_modified" in standardized.attrs  # Changed from processing_date
        assert "processing_software" in standardized.attrs
        assert "processing_version" in standardized.attrs

        # Should preserve data values while changing names
        assert standardized.sizes["TIME"] == raw_dataset.sizes["time"]

    def test_standardise_data_with_real_metadata(self):
        """Test that read.rapid() produces properly standardized data."""
        # Test that the new read API produces standardized data
        from amocatlas import read

        result = (
            read.rapid()
        )  # Loads single moc_transports.nc file (1.11MB) - already standardized

        # Should have basic standardization applied
        assert "processing_datasource" in result.attrs
        assert "processing_software" in result.attrs
        assert result.attrs["processing_datasource"] == "rapid26n"

        # Should have standardized variable names
        assert "MOC" in result.data_vars
        assert "TIME" in result.coords


class TestMetadataFunctions:
    """Unit tests for metadata handling functions."""

    def test_reorder_metadata(self):
        """Test metadata reordering according to GLOBAL_ATTR_ORDER."""
        # Create metadata in wrong order
        metadata = {
            "comment": "A comment",
            "title": "Test Title",
            "Conventions": "CF-1.8",  # Case-sensitive
            "description": "Test description",
            "featureType": "timeSeries",  # Case-sensitive
            "random_attr": "Some value",
        }

        result = standardise.reorder_metadata(metadata)
        result_keys = list(result.keys())

        # Should preserve case-sensitive attributes exactly
        assert "Conventions" in result_keys
        assert "featureType" in result_keys

        # Should follow GLOBAL_ATTR_ORDER for known attributes
        title_idx = result_keys.index("title")
        desc_idx = result_keys.index("description")
        assert title_idx < desc_idx  # Title comes before description

        # Unknown attributes should be at the end
        assert result_keys.index("random_attr") > desc_idx

    def test_get_amocatlas_version(self):
        """Test version detection."""
        version = standardise.get_dynamic_version()

        # Should return a reasonable version string
        assert isinstance(version, str), f"Version should be string, got {type(version)}: {repr(version)}"
        assert len(version) > 0, f"Version should not be empty, got: {repr(version)}"

        # Should be in some recognizable format (digits OR hex chars for git commits)
        has_digits = any(char.isdigit() for char in version)
        has_hex_chars = any(char in 'abcdef' for char in version.lower())
        assert has_digits or has_hex_chars, f"Version should contain digits or hex characters, got: {repr(version)}"

    def test_standardize_time_coordinate(self):
        """Test TIME coordinate standardization."""
        # Create test dataset with time coordinate
        ds = xr.Dataset(
            {"data": (["TIME"], [1, 2, 3])},
            coords={"time": pd.date_range("2020-01-01", periods=3)},
        )

        result = standardise.standardize_time_coordinate(ds)

        # Should have TIME coordinate
        assert "TIME" in result.coords

        # Should have standard attributes
        time_attrs = result["TIME"].attrs
        assert "standard_name" in time_attrs
        assert time_attrs["standard_name"] == "time"

    def test_clean_metadata(self):
        """Test metadata cleaning functionality."""
        # Test the clean_metadata function that exists
        metadata = {
            "Title": "Test Title",
            "TITLE": "Duplicate title",  # Duplicate should be resolved
            "creator_name": "Test Author",
            "principal_investigator": "Test PI",  # Should be consolidated with creator_name
            "Institution": "Test Institution",
            "Acknowledgement": "Test Acknowledgement",
        }

        result = standardise.clean_metadata(metadata)

        # Should return a cleaned dictionary
        assert isinstance(result, dict)
        assert len(result) > 0

        # Should consolidate contributor fields: creator_name should be removed and contributor_name added
        assert "creator_name" not in result  # Original field should be removed
        assert (
            "contributor_name" in result
        )  # Should be consolidated into standard contributor field

        # Should normalize acknowledgement spelling
        assert "acknowledgment" in result  # American spelling

        # Should resolve title duplicates (keeping one)
        title_count = sum(1 for k in result.keys() if k.lower().startswith("title"))
        assert title_count == 1  # Should have only one title field after deduplication


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    @pytest.mark.slow
    def test_standardise_data_edge_case(self):
        """Test standardization edge case with real rapid data."""
        # Use real rapid data since empty dataset needs metadata files
        from amocatlas import read

        rapid_data = read.rapid(raw=True)  # Raw data

        result = standardise.standardise_data(rapid_data, file_name="moc_transports.nc")

        # Should still have basic standardization
        assert "processing_datasource" in result.attrs
        assert isinstance(result, xr.Dataset)

    def test_reorder_metadata_empty(self):
        """Test metadata reordering with empty metadata."""
        result = standardise.reorder_metadata({})
        assert result == {}

    def test_reorder_metadata_case_sensitivity(self):
        """Test that case-sensitive attributes are preserved exactly."""
        metadata = {
            "conventions": "wrong case",  # lowercase
            "Conventions": "CF-1.8",  # correct case
            "featuretype": "wrong case",  # lowercase
            "featureType": "timeSeries",  # correct case
        }

        result = standardise.reorder_metadata(metadata)

        # Should preserve exact case for case-sensitive attributes
        assert result["Conventions"] == "CF-1.8"
        assert result["featureType"] == "timeSeries"

        # Should also preserve the lowercase versions (different attributes)
        assert result["conventions"] == "wrong case"
        assert result["featuretype"] == "wrong case"

    def test_version_fallback(self):
        """Test version detection fallback mechanisms."""
        # This tests that version detection doesn't crash
        # and provides some fallback even in edge cases

        from unittest import mock
        import subprocess

        with mock.patch("subprocess.run") as mock_run:
            # Mock git failure with the proper exception type that the function catches
            mock_run.side_effect = subprocess.SubprocessError("Git not found")

            version = standardise.get_dynamic_version()

            # Should still return something reasonable
            assert isinstance(version, str)
            assert len(version) > 0
