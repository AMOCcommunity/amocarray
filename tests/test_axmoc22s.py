"""Tests for AXMOC 22.5°S data reader.

Simple, targeted tests focusing on module structure and constants.
Tests the basic functionality without complex data loading mocks.
"""

from amocatlas.data_sources import axmoc22s
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestAXMOC22S:
    """Test basic AXMOC 22.5°S module functionality."""

    def test_module_constants_defined(self):
        """Test that all required module constants exist."""
        assert hasattr(axmoc22s, "DATASOURCE_ID")
        assert hasattr(axmoc22s, "AXMOC22S_DEFAULT_FILES")
        assert hasattr(axmoc22s, "AXMOC22S_TRANSPORT_FILES")
        assert hasattr(axmoc22s, "AXMOC22S_DEFAULT_SOURCE")
        assert hasattr(axmoc22s, "AXMOC22S_METADATA")
        assert hasattr(axmoc22s, "AXMOC22S_FILE_METADATA")

        # Check values are sensible
        assert axmoc22s.DATASOURCE_ID == "axmoc22s"
        assert isinstance(axmoc22s.AXMOC22S_DEFAULT_FILES, list)
        assert isinstance(axmoc22s.AXMOC22S_TRANSPORT_FILES, list)
        assert isinstance(axmoc22s.AXMOC22S_DEFAULT_SOURCE, str)
        assert axmoc22s.AXMOC22S_DEFAULT_SOURCE.startswith("https://")
        assert isinstance(axmoc22s.AXMOC22S_METADATA, dict)
        assert isinstance(axmoc22s.AXMOC22S_FILE_METADATA, dict)

    def test_default_files_configuration(self):
        """Test default files configuration is reasonable."""
        files = axmoc22s.AXMOC22S_DEFAULT_FILES
        assert len(files) > 0
        assert "AXMOC_22S_timeseries_2007_2023.nc" in files

        transport_files = axmoc22s.AXMOC22S_TRANSPORT_FILES
        assert len(transport_files) > 0
        assert "AXMOC_22S_timeseries_2007_2023.nc" in transport_files

        # Files should be NetCDF format
        for file in files:
            assert file.endswith(".nc")

    def test_metadata_structure(self):
        """Test metadata structure is reasonable."""
        metadata = axmoc22s.AXMOC22S_METADATA
        assert isinstance(metadata, dict)

        # Check for expected keys
        expected_keys = ["project", "weblink", "comment"]
        for key in expected_keys:
            assert key in metadata, f"Expected metadata key '{key}' not found"

        # Check values are non-empty strings
        for _key, value in metadata.items():
            assert isinstance(value, str)
            assert len(value) > 0

    def test_file_metadata_structure(self):
        """Test file metadata structure is reasonable."""
        file_metadata = axmoc22s.AXMOC22S_FILE_METADATA
        assert isinstance(file_metadata, dict)
        assert "AXMOC_22S_timeseries_2007_2023.nc" in file_metadata

        for _filename, metadata in file_metadata.items():
            assert isinstance(metadata, dict)
            assert "data_product" in metadata
            assert isinstance(metadata["data_product"], str)
            assert len(metadata["data_product"]) > 0

    def test_function_exists_and_callable(self):
        """Test that main function exists and is callable."""
        assert hasattr(axmoc22s, "read_axmoc22s")
        assert callable(axmoc22s.read_axmoc22s)

        # Check function has documentation
        func = axmoc22s.read_axmoc22s
        assert func.__doc__ is not None
        assert "AXMOC22S" in func.__doc__ or "transport" in func.__doc__

    def test_module_docstring_informative(self):
        """Test that module has informative docstring."""
        assert axmoc22s.__doc__ is not None
        assert "22.5" in axmoc22s.__doc__
        assert "AMOC" in axmoc22s.__doc__
        assert "transport" in axmoc22s.__doc__

    def test_module_imports_successfully(self):
        """Test that the module imports without errors."""
        # This test passes if the module loaded successfully
        assert axmoc22s is not None
