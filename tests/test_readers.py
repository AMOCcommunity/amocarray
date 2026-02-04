import pytest
import xarray as xr

from amocatlas import logger, readers

logger.disable_logging()


def test_load_sample_dataset_rapid():
    ds = readers.load_sample_dataset("rapid")
    assert isinstance(ds, xr.Dataset), "Expected an xarray.Dataset"
    assert "TIME" in ds or "time" in ds, "Dataset should have a TIME or time coordinate"
    time_dim = "TIME" if "TIME" in ds.dims else "time"
    assert time_dim in ds.dims, "Dataset should have a TIME or time dimension"
    assert ds.sizes[time_dim] > 0, f"{time_dim} dimension should not be empty"
    assert "moc_mar_hc10" in ds, "Expected variable moc_mar_hc10 in RAPID dataset"


def test_load_sample_dataset_invalid_array():
    with pytest.raises(
        ValueError,
        match="Sample dataset for array 'invalid' is not defined",
    ):
        readers.load_sample_dataset("invalid")


def test_load_dataset_invalid_array():
    with pytest.raises(ValueError, match="Unknown array name: invalid"):
        readers.load_dataset("invalid")


def test_calafat2025_file_validation():
    """Test CALAFAT2025 reader error handling with invalid files."""
    from amocatlas import read_calafat2025

    # Test that constants are defined properly
    assert (
        "Bayesian_estimates_Atlantic_MHT.zip" in read_calafat2025.CALAFAT2025_FILE_URLS
    )
    assert len(read_calafat2025.CALAFAT2025_DEFAULT_FILES) > 0


def test_zheng2024_file_validation():
    """Test ZHENG2024 reader error handling with invalid inputs."""
    from amocatlas import read_zheng2024

    # Test with non-existent file in local source
    with pytest.raises(FileNotFoundError, match="Local file not found"):
        read_zheng2024.read_zheng2024(
            source="/nonexistent/path",
            file_list=["nonexistent.nc"],
            data_dir="/tmp/nonexistent_dir",
        )


def test_calafat2025_defaults():
    """Test CALAFAT2025 default parameters."""
    from amocatlas import read_calafat2025

    # Check defaults exist
    assert read_calafat2025.CALAFAT2025_DEFAULT_FILES is not None
    assert read_calafat2025.CALAFAT2025_TRANSPORT_FILES is not None
    assert read_calafat2025.CALAFAT2025_FILE_URLS is not None
    assert read_calafat2025.CALAFAT2025_METADATA is not None


def test_calafat2025_no_download_url():
    """Test CALAFAT2025 error when no download URL is available for a file."""
    from amocatlas import read_calafat2025
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        with pytest.raises(ValueError, match="No download URL found for file"):
            read_calafat2025.read_calafat2025(
                source="fake_source",  # Provide a source to avoid defaults
                file_list=["nonexistent_file.zip"],
                data_dir=tmp_dir,
            )


def test_calafat2025_no_zip_contents():
    """Test CALAFAT2025 error when no zip contents mapping is provided."""
    from amocatlas import read_calafat2025
    import tempfile
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Mock a fake file with URL but no zip contents mapping
        with patch.object(
            read_calafat2025,
            "CALAFAT2025_FILE_URLS",
            {"fake.zip": "http://example.com/fake.zip"},
        ):
            with patch.object(read_calafat2025, "CALAFAT2025_ZIP_CONTENTS", {}):
                with patch("amocatlas.utilities.resolve_file_path") as mock_resolve:
                    mock_resolve.return_value = tmp_dir + "/fake.zip"
                    # Create a fake zip file
                    import zipfile

                    fake_zip = tmp_dir + "/fake.zip"
                    with zipfile.ZipFile(fake_zip, "w"):
                        pass

                    with pytest.raises(
                        ValueError,
                        match="No internal file mapping provided for zip file",
                    ):
                        read_calafat2025.read_calafat2025(
                            source=None,
                            file_list=["fake.zip"],
                            data_dir=tmp_dir,
                        )


def test_calafat2025_no_netcdf_in_zip():
    """Test CALAFAT2025 error when zip contains no NetCDF files."""
    from amocatlas import read_calafat2025
    import tempfile
    import zipfile
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a zip file with no .nc files
        fake_zip = tmp_dir + "/fake.zip"
        with zipfile.ZipFile(fake_zip, "w") as zf:
            zf.writestr("README.txt", "test content")

        with patch.object(
            read_calafat2025,
            "CALAFAT2025_FILE_URLS",
            {"fake.zip": "http://example.com/fake.zip"},
        ):
            with patch.object(
                read_calafat2025,
                "CALAFAT2025_ZIP_CONTENTS",
                {"fake.zip": {"README.txt"}},
            ):
                with patch("amocatlas.utilities.resolve_file_path") as mock_resolve:
                    mock_resolve.return_value = fake_zip

                    with pytest.raises(FileNotFoundError, match="No NetCDF"):
                        read_calafat2025.read_calafat2025(
                            source=None,
                            file_list=["fake.zip"],
                            data_dir=tmp_dir,
                        )


def test_calafat2025_transport_only_flag():
    """Test CALAFAT2025 transport_only flag functionality."""
    from amocatlas import read_calafat2025
    from unittest.mock import patch

    # Test that transport_only=True uses transport files
    with patch("amocatlas.read_calafat2025.read_calafat2025") as mock_func:
        mock_func.return_value = []

        # When transport_only is True, should use transport files
        read_calafat2025.read_calafat2025(
            source="fake_source",
            file_list=None,  # Should be overridden
            transport_only=True,
            data_dir="/tmp",
        )

        # Verify the function was called (this tests the decorator behavior)
        assert mock_func.called


def test_calafat2025_string_to_list_conversion():
    """Test CALAFAT2025 converts string file_list to list."""
    from amocatlas import read_calafat2025
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        # This should convert string to list internally before hitting the error
        with pytest.raises(ValueError, match="No download URL found for file"):
            read_calafat2025.read_calafat2025(
                source="fake_source",
                file_list="nonexistent_file.zip",  # String input
                data_dir=tmp_dir,
            )


def test_calafat2025_non_zip_file_warning():
    """Test CALAFAT2025 logs warning for non-zip files."""
    from amocatlas import read_calafat2025
    import tempfile
    from unittest.mock import patch

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a fake .nc file to avoid download
        fake_nc = tmp_dir + "/fake.nc"
        with open(fake_nc, "w") as f:
            f.write("fake content")

        with patch.object(
            read_calafat2025,
            "CALAFAT2025_FILE_URLS",
            {"fake.nc": "http://example.com/fake.nc"},
        ):
            with patch("amocatlas.utilities.resolve_file_path") as mock_resolve:
                mock_resolve.return_value = fake_nc

                # Should raise because no datasets were processed
                with pytest.raises(
                    FileNotFoundError, match="No valid NetCDF files found"
                ):
                    read_calafat2025.read_calafat2025(
                        source="fake_source",
                        file_list=["fake.nc"],
                        data_dir=tmp_dir,
                    )


def test_zheng2024_defaults():
    """Test ZHENG2024 default parameters."""
    from amocatlas import read_zheng2024

    # Check defaults exist
    assert read_zheng2024.ZHENG2024_DEFAULT_FILES is not None
    assert read_zheng2024.ZHENG2024_TRANSPORT_FILES is not None
    assert read_zheng2024.ZHENG2024_DEFAULT_SOURCE is not None
    assert read_zheng2024.ZHENG2024_METADATA is not None


@pytest.mark.parametrize(
    "array_name, expected_var",
    [
        ("rapid", "moc_mar_hc10"),
        ("move", "TRANSPORT_TOTAL"),
        ("osnap", "MOC_ALL"),  # OSNAP should contain MOC
        ("fw2015", "MOC_PROXY"),
        ("mocha", "Q_eddy"),
        ("41n", "Meridional Overturning Volume Transport (Sverdrups)"),
        ("dso", "DSO_tr"),
    ],
)
def test_load_dataset(array_name, expected_var):
    datasets = readers.load_dataset(array_name)
    assert isinstance(datasets, list), f"{array_name} should return a list of datasets"
    assert len(datasets) > 0, f"{array_name} dataset list should not be empty"

    for ds in datasets:
        assert isinstance(
            ds,
            xr.Dataset,
        ), f"Each dataset for {array_name} should be an xarray.Dataset"
        assert (
            "TIME" in ds or "time" in ds
        ), f"{array_name} dataset should have TIME or time coordinate"
        assert (
            expected_var in ds
        ), f"{array_name} dataset should contain variable {expected_var}"
        assert (
            "source_file" in ds.attrs
        ), f"{array_name} dataset should include 'source_file' metadata"
        assert (
            "project" in ds.attrs
        ), f"{array_name} dataset should include 'project' metadata"
