"""Tests for LEBRAS 35°N data reader.

Simple, targeted tests focusing on module structure and constants.
Tests the basic functionality without complex data loading mocks.
"""

from amocatlas.data_sources import lebras35n
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestLEBRAS35N:
    """Test basic LEBRAS 35°N module functionality."""

    def test_module_constants_defined(self):
        """Test that all required module constants exist."""
        assert hasattr(lebras35n, "DATASOURCE_ID")
        assert hasattr(lebras35n, "LEBRAS35N_DEFAULT_FILES")
        assert hasattr(lebras35n, "LEBRAS35N_TRANSPORT_FILES")
        assert hasattr(lebras35n, "LEBRAS35N_DEFAULT_SOURCE")
        assert hasattr(lebras35n, "LEBRAS35N_METADATA")
        assert hasattr(lebras35n, "LEBRAS35N_FILE_METADATA")

        # Check values are sensible
        assert lebras35n.DATASOURCE_ID == "lebras35n"
        assert isinstance(lebras35n.LEBRAS35N_DEFAULT_FILES, list)
        assert isinstance(lebras35n.LEBRAS35N_TRANSPORT_FILES, list)
        assert isinstance(lebras35n.LEBRAS35N_DEFAULT_SOURCE, str)
        assert lebras35n.LEBRAS35N_DEFAULT_SOURCE.startswith("https://")
        assert isinstance(lebras35n.LEBRAS35N_METADATA, dict)
        assert isinstance(lebras35n.LEBRAS35N_FILE_METADATA, dict)

    def test_default_files_configuration(self):
        """Test default files configuration is reasonable."""
        files = lebras35n.LEBRAS35N_DEFAULT_FILES
        assert len(files) > 0
        assert "AMOC35N.nc" in files
        assert "AMOC35N_gridded_velocities.nc" in files

        transport_files = lebras35n.LEBRAS35N_TRANSPORT_FILES
        assert len(transport_files) > 0
        assert "AMOC35N.nc" in transport_files
        assert "AMOC35N_gridded_velocities.nc" not in transport_files

        # Files should be NetCDF format
        for file in files:
            assert file.endswith(".nc")

    def test_metadata_structure(self):
        """Test metadata structure is reasonable."""
        metadata = lebras35n.LEBRAS35N_METADATA
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
        file_metadata = lebras35n.LEBRAS35N_FILE_METADATA
        assert isinstance(file_metadata, dict)
        assert "AMOC35N.nc" in file_metadata
        assert "AMOC35N_gridded_velocities.nc" in file_metadata

        for _filename, metadata in file_metadata.items():
            assert isinstance(metadata, dict)
            assert "data_product" in metadata
            assert isinstance(metadata["data_product"], str)
            assert len(metadata["data_product"]) > 0

    def test_function_exists_and_callable(self):
        """Test that main function exists and is callable."""
        assert hasattr(lebras35n, "read_lebras35n")
        assert callable(lebras35n.read_lebras35n)

        # Check function has documentation
        func = lebras35n.read_lebras35n
        assert func.__doc__ is not None
        assert "LEBRAS35N" in func.__doc__ or "transport" in func.__doc__

    def test_module_docstring_informative(self):
        """Test that module has informative docstring."""
        assert lebras35n.__doc__ is not None
        assert "35" in lebras35n.__doc__
        assert "AMOC" in lebras35n.__doc__
        assert "transport" in lebras35n.__doc__

    def test_module_imports_successfully(self):
        """Test that the module imports without errors."""
        # This test passes if the module loaded successfully
        assert lebras35n is not None
