"""Tests for FBC (Faroe Bank Channel) data reader.

Simple, targeted tests focusing on module structure and constants.
Tests the basic functionality without complex data loading mocks.
"""

from amocatlas.data_sources import fbc
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestFBC:
    """Test basic FBC module functionality."""

    def test_module_constants_defined(self):
        """Test that all required module constants exist."""
        assert hasattr(fbc, "DATASOURCE_ID")
        assert hasattr(fbc, "FBC_DEFAULT_FILES")
        assert hasattr(fbc, "FBC_TRANSPORT_FILES")

        # Check values are sensible
        assert fbc.DATASOURCE_ID == "fbc"
        assert isinstance(fbc.FBC_DEFAULT_FILES, list)
        assert isinstance(fbc.FBC_TRANSPORT_FILES, list)

    def test_default_files_configuration(self):
        """Test default files configuration is reasonable."""
        files = fbc.FBC_DEFAULT_FILES
        assert len(files) > 0
        assert "OS_GSR_FBC_D_1995_2024.nc" in files

        transport_files = fbc.FBC_TRANSPORT_FILES
        assert len(transport_files) > 0
        assert "OS_GSR_FBC_D_1995_2024.nc" in transport_files

        # Files should be text format for FBC data
        for file in files:
            assert file.endswith(".nc")

    def test_function_exists_and_callable(self):
        """Test that main function exists and is callable."""
        assert hasattr(fbc, "read_fbc")
        assert callable(fbc.read_fbc)

        # Check function has documentation
        func = fbc.read_fbc
        assert func.__doc__ is not None
        assert "Faroe Bank Channel" in func.__doc__ or "FBC" in func.__doc__

    def test_module_docstring_informative(self):
        """Test that module has informative docstring."""
        assert fbc.__doc__ is not None
        assert "Faroe Bank Channel" in fbc.__doc__
        assert "overflow" in fbc.__doc__
        assert "FBC" in fbc.__doc__

    def test_module_imports_successfully(self):
        """Test that the module imports without errors."""
        # This test passes if the module loaded successfully
        assert fbc is not None
        # Check required dependencies are accessible
        assert hasattr(fbc, "xr")  # xarray
