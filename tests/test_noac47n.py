"""Tests for NOAC 47°N array data reader.

Simple, targeted tests focusing on module structure and constants.
Tests the basic functionality without complex data loading mocks.
"""

from amocatlas.data_sources import noac47n
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestNOAC47N:
    """Test basic NOAC 47°N module functionality."""

    def test_module_constants_defined(self):
        """Test that all required module constants exist."""
        assert hasattr(noac47n, "DATASOURCE_ID")
        assert hasattr(noac47n, "NOAC47N_DEFAULT_FILES")
        assert hasattr(noac47n, "NOAC47N_TRANSPORT_FILES")
        assert hasattr(noac47n, "A47N_DEFAULT_SOURCE")
        assert hasattr(noac47n, "A47N_METADATA")

        # Check values are sensible
        assert noac47n.DATASOURCE_ID == "noac47n"
        assert isinstance(noac47n.NOAC47N_DEFAULT_FILES, list)
        assert isinstance(noac47n.A47N_METADATA, dict)

    def test_default_files_configuration(self):
        """Test default files configuration is reasonable."""
        files = noac47n.NOAC47N_DEFAULT_FILES
        assert len(files) > 0
        assert "NOAC_AMOC.tab" in files

        transport_files = noac47n.NOAC47N_TRANSPORT_FILES
        assert len(transport_files) > 0
        assert "NOAC_AMOC.tab" in transport_files

        # Files should be tab format
        for file in files:
            assert file.endswith(".tab")

    def test_source_configuration(self):
        """Test data source configuration."""
        source = noac47n.A47N_DEFAULT_SOURCE
        assert isinstance(source, str)
        assert source.startswith("https://")
        assert "doi" in source or "pangaea" in source.lower()

    def test_metadata_structure(self):
        """Test metadata structure is reasonable."""
        metadata = noac47n.A47N_METADATA
        assert isinstance(metadata, dict)

        # Check for expected keys
        expected_keys = ["project", "weblink", "comment"]
        for key in expected_keys:
            assert key in metadata, f"Expected metadata key '{key}' not found"

        # Check values are non-empty strings
        for _key, value in metadata.items():
            assert isinstance(value, str)
            assert len(value) > 0

    def test_function_exists_and_callable(self):
        """Test that main function exists and is callable."""
        assert hasattr(noac47n, "read_47n")
        assert callable(noac47n.read_47n)

        # Check function has documentation
        func = noac47n.read_47n
        assert func.__doc__ is not None
        assert "47" in func.__doc__ or "NOAC" in func.__doc__

    def test_module_docstring_informative(self):
        """Test that module has informative docstring."""
        assert noac47n.__doc__ is not None
        assert "NOAC" in noac47n.__doc__
        assert "47°N" in noac47n.__doc__ or "47N" in noac47n.__doc__

    def test_module_imports_successfully(self):
        """Test that the module imports without errors."""
        # This test passes if the module loaded successfully
        assert noac47n is not None
        # Check required dependencies are accessible
        assert hasattr(noac47n, "xr")  # xarray
        assert hasattr(noac47n, "pd")  # pandas
