"""Tests for arcticgateway data reader.

Simple, targeted tests focusing on module structure and constants.
Avoids complex mocking of the full data loading process.
"""

from amocatlas.data_sources import arcticgateway
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestArcticGateway:
    """Test basic arcticgateway module functionality."""

    def test_module_constants_defined(self):
        """Test that all required module constants exist."""
        assert hasattr(arcticgateway, "DATASOURCE_ID")
        assert hasattr(arcticgateway, "ARCTIC_DEFAULT_SOURCE")
        assert hasattr(arcticgateway, "ARCTIC_DEFAULT_FILES")
        assert hasattr(arcticgateway, "ARCTIC_ZIP_CONTENTS")

        # Check values
        assert arcticgateway.DATASOURCE_ID == "arcticgateway"
        assert isinstance(arcticgateway.ARCTIC_DEFAULT_SOURCE, str)
        assert arcticgateway.ARCTIC_DEFAULT_SOURCE.startswith("https://")

    def test_zip_contents_configuration(self):
        """Test ZIP contents configuration is properly structured."""
        contents = arcticgateway.ARCTIC_ZIP_CONTENTS
        assert isinstance(contents, dict)
        assert "Adjusted_fulldepth_v0.zip" in contents

        # Check that expected gateway files are listed
        files = contents["Adjusted_fulldepth_v0.zip"]
        expected_gateways = [
            "FramStrait",
            "DavisStrait",
            "BeringStrait",
            "BarentsSeaOpening",
        ]

        for gateway in expected_gateways:
            gateway_files = [f for f in files if gateway in f]
            assert len(gateway_files) == 1, f"Expected exactly one file for {gateway}"

        # Check file paths are reasonable
        for filepath in files:
            assert filepath.endswith(".nc")
            assert "Adjusted_fulldepth" in filepath

    def test_default_files_configuration(self):
        """Test default files configuration."""
        files = arcticgateway.ARCTIC_DEFAULT_FILES
        assert isinstance(files, list)
        assert len(files) > 0
        assert "Adjusted_fulldepth_v0.zip" in files

    def test_function_exists_and_callable(self):
        """Test that main function exists and is callable."""
        assert hasattr(arcticgateway, "read_arcticgateway")
        assert callable(arcticgateway.read_arcticgateway)

        # Check function has reasonable signature
        func = arcticgateway.read_arcticgateway
        assert func.__doc__ is not None
        assert "Load" in func.__doc__

    def test_module_imports_successfully(self):
        """Test that the module imports without errors."""
        # This test passes if the module loaded successfully
        assert arcticgateway is not None
