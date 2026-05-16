"""Tests for the SF2021 (Sanchez-Franks 2021) data reader.

These mirror the style used in other reader tests (see `test_noac47n.py`).
"""

import tempfile
from pathlib import Path

import pytest

from amocatlas.data_sources import sf2021
from amocatlas.logger import disable_logging

# Keep tests quiet
disable_logging()


class TestSF2021:
    """Basic tests for the `sf2021` reader module."""

    def test_module_constants_defined(self):
        assert hasattr(sf2021, "DATASOURCE_ID")
        assert hasattr(sf2021, "SF2021_DEFAULT_FILES")
        assert hasattr(sf2021, "SF2021_TRANSPORT_FILES")
        assert hasattr(sf2021, "SF2021_DEFAULT_SOURCE")
        assert hasattr(sf2021, "SF2021_METADATA")
        assert hasattr(sf2021, "SF2021_FILE_METADATA")

    def test_default_files_and_transport_files(self):
        files = sf2021.SF2021_DEFAULT_FILES
        transports = sf2021.SF2021_TRANSPORT_FILES
        assert isinstance(files, list)
        assert isinstance(transports, list)
        assert len(files) > 0
        assert len(transports) > 0
        # Expect the standard altimetry filename to be present
        assert "altimetry_moc_transport_1993_2020_18mos_smoothed.nc" in files

    def test_source_and_metadata_structure(self):
        source = sf2021.SF2021_DEFAULT_SOURCE
        assert isinstance(source, str)
        assert source.startswith("http")

        metadata = sf2021.SF2021_METADATA
        assert isinstance(metadata, dict)
        for key in ("project", "weblink", "comment"):
            assert key in metadata

    def test_read_function_exists(self):
        assert hasattr(sf2021, "read_sf2021")
        assert callable(sf2021.read_sf2021)
        assert sf2021.read_sf2021.__doc__ is not None

    def test_read_sf2021_raises_on_missing_local_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            with pytest.raises(FileNotFoundError, match="Local file not found"):
                sf2021.read_sf2021(
                    source=tmp_dir, file_list=["nonexistent_file.nc"], data_dir=tmp_dir
                )

    def test_read_returns_dataset_and_tracks_attrs(self, monkeypatch, tmp_path):
        import xarray as xr
        import pandas as pd

        # Minimal Dataset to be returned. Use an explicit DateOffset for
        # yearly frequency to remain compatible with newer pandas versions.
        time_index = pd.date_range("1993-01-01", periods=2, freq=pd.DateOffset(years=1))
        ds = xr.Dataset({"transport": ("TIME", [1.0, 2.0])}, coords={"TIME": time_index})

        fake_path = tmp_path / "altimetry_moc_transport_1993_2020_18mos_smoothed.nc"
        fake_path.write_text("fake")

        monkeypatch.setattr(
            "amocatlas.utilities.resolve_file_path",
            lambda file_name, source, download_url, local_data_dir, redownload=False: fake_path,
        )

        monkeypatch.setattr(
            "amocatlas.data_sources.sf2021.ReaderUtils.safe_load_dataset",
            lambda p: ds,
        )

        def fake_attach(ds_in, file, file_path, global_meta, yaml_file_meta, file_meta, ds_id, track_added_attrs=False):
            if track_added_attrs:
                return ds_in, {"added": ["source_file"]}
            return ds_in

        monkeypatch.setattr(
            "amocatlas.data_sources.sf2021.ReaderUtils.attach_metadata_with_tracking",
            fake_attach,
        )

        datasets, added = sf2021.read_sf2021(source=None, file_list=None, track_added_attrs=True, data_dir=tmp_path)

        assert isinstance(datasets, list)
        assert len(datasets) == 1
        assert isinstance(datasets[0], xr.Dataset)
        assert "TIME" in datasets[0].coords
        assert isinstance(added, list)
        assert isinstance(added[0], dict)
