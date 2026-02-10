"""Tests for calafat2025 data reader.

Simple, targeted tests focusing on module structure and constants.
Tests the basic functionality without complex data loading mocks.
"""

from amocatlas.data_sources import calafat2025
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestCalafat2025:
    """Test basic calafat2025 module functionality."""

    def test_module_constants_defined(self):
        """Test that all required module constants exist."""
        assert hasattr(calafat2025, "DATASOURCE_ID")
        assert hasattr(calafat2025, "CALAFAT2025_DEFAULT_SOURCE")
        assert hasattr(calafat2025, "CALAFAT2025_DEFAULT_FILES")
        assert hasattr(calafat2025, "CALAFAT2025_ZIP_CONTENTS")
        assert hasattr(calafat2025, "CALAFAT2025_FILE_URLS")

        # Check values
        assert calafat2025.DATASOURCE_ID == "calafat2025"
        assert isinstance(calafat2025.CALAFAT2025_DEFAULT_SOURCE, str)
        assert calafat2025.CALAFAT2025_DEFAULT_SOURCE.startswith("https://")

    def test_zip_contents_configuration(self):
        """Test ZIP contents configuration is properly structured."""
        contents = calafat2025.CALAFAT2025_ZIP_CONTENTS
        assert isinstance(contents, dict)
        assert "Bayesian_estimates_Atlantic_MHT.zip" in contents

        # Check expected files in zip
        files = contents["Bayesian_estimates_Atlantic_MHT.zip"]
        assert "Bayesian_estimates_Atlantic_MHT.nc" in files
        assert "README.txt" in files

        # Check file extensions make sense
        nc_files = [f for f in files if f.endswith(".nc")]
        assert len(nc_files) >= 1, "Expected at least one .nc file"

    def test_file_urls_configuration(self):
        """Test file URLs configuration."""
        file_urls = calafat2025.CALAFAT2025_FILE_URLS
        assert isinstance(file_urls, dict)
        assert "Bayesian_estimates_Atlantic_MHT.zip" in file_urls

        # Check URL format
        for _filename, url in file_urls.items():
            assert isinstance(url, str)
            assert url.startswith("https://")
            assert "zenodo" in url.lower()

    def test_default_files_configuration(self):
        """Test default files configuration."""
        files = calafat2025.CALAFAT2025_DEFAULT_FILES
        assert isinstance(files, list)
        assert len(files) > 0
        assert "Bayesian_estimates_Atlantic_MHT.zip" in files

        transport_files = calafat2025.CALAFAT2025_TRANSPORT_FILES
        assert isinstance(transport_files, list)
        assert len(transport_files) > 0

    def test_function_exists_and_callable(self):
        """Test that main function exists and is callable."""
        assert hasattr(calafat2025, "read_calafat2025")
        assert callable(calafat2025.read_calafat2025)

        # Check function has documentation
        func = calafat2025.read_calafat2025
        assert func.__doc__ is not None
        assert "CALAFAT2025" in func.__doc__ or "transport" in func.__doc__

    def test_module_docstring_informative(self):
        """Test that module has informative docstring."""
        assert calafat2025.__doc__ is not None
        assert "Calafat" in calafat2025.__doc__
        assert "2025" in calafat2025.__doc__
        assert "MHT" in calafat2025.__doc__ or "heat" in calafat2025.__doc__

    def test_module_imports_successfully(self):
        """Test that the module imports without errors."""
        # This test passes if the module loaded successfully
        assert calafat2025 is not None
