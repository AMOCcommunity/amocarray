"""RAPID array data reader for AMOCatlas.

This module provides functions to read and process data from the RAPID
(Rapid Climate Change) observing array located at 26°N in the Atlantic.

"""

from pathlib import Path
from typing import Union

import xarray as xr

# Import the modules used
from amocatlas import logger, utilities
from amocatlas.logger import log_error, log_info, log_warning
from amocatlas.utilities import apply_defaults
from amocatlas.reader_utils import ReaderUtils

log = logger.log  # Use the global logger

# Default list of RAPID data files
RAPID_DEFAULT_SOURCE = "https://rapid.ac.uk/sites/default/files/rapid_data/"
RAPID_TRANSPORT_FILES = ["moc_transports.nc"]
RAPID_DEFAULT_FILES = [
    "moc_transports.nc",
    "moc_vertical.nc",
    "ts_gridded.nc",
    "2d_gridded.nc",
    "meridional_transports.nc",
]

# Inline metadata dictionary
RAPID_METADATA = {
    "description": "RAPID 26N transport estimates dataset",
    "project": "RAPID-AMOC 26°N array",
    "web_link": "https://rapid.ac.uk/rapidmoc",
    "note": "Dataset accessed and processed via xarray",
}

# File-specific metadata placeholder
RAPID_FILE_METADATA = {
    "moc_transports.nc": {
        "data_product": "RAPID layer transport time series",
    },
    "moc_vertical.nc": {
        "data_product": "RAPID vertical streamfunction time series",
    },
    "ts_gridded.nc": {
        "data_product": "RAPID gridded temperature and salinity",
    },
    "2d_gridded.nc": {
        "data_product": "RAPID 2D gridded temperature and salinity",
    },
    "meridional_transports.nc": {
        "data_product": "RAPID meridional transport time series",
    },
}
# https://rapid.ac.uk/sites/default/files/rapid_data/ts_gridded.nc
# https://rapid.ac.uk/sites/default/files/rapid_data/moc_vertical.nc
# https://rapid.ac.uk/sites/default/files/rapid_data/moc_transports.nc
# https://rapid.ac.uk/sites/default/files/rapid_data/2d_gridded.nc
# https://rapid.ac.uk/sites/default/files/rapid_data/meridional_transports.nc


@apply_defaults(RAPID_DEFAULT_SOURCE, RAPID_DEFAULT_FILES)
def read_rapid(
    source: Union[str, Path, None],
    file_list: Union[str, list[str]],
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
) -> list[xr.Dataset]:
    """Load the RAPID transport dataset from a URL or local file path into an xarray.Dataset.

    Parameters
    ----------
    source : str, optional
        URL or local path to the NetCDF file(s).
        Defaults to the RAPID data repository URL.
    file_list : str or list of str, optional
        Filename or list of filenames to process.
        If None, will attempt to list files in the source directory.
    transport_only : bool, optional
        If True, restrict to transport files only.
    data_dir : str, Path or None, optional
        Optional local data directory.
    redownload : bool, optional
        If True, force redownload of the data.

    Returns
    -------
    xr.Dataset
        The loaded xarray dataset with basic inline metadata.

    Raises
    ------
    ValueError
        If the source is neither a valid URL nor a directory path.
    FileNotFoundError
        If no valid NetCDF files are found in the provided file list.

    """
    log_info("Starting to read RAPID dataset")

    # Use ReaderUtils for common operations
    file_list = ReaderUtils.prepare_file_list(
        file_list, RAPID_DEFAULT_FILES, RAPID_TRANSPORT_FILES, transport_only
    )
    local_data_dir = ReaderUtils.setup_data_directory(data_dir)

    datasets = []
    netcdf_files = ReaderUtils.filter_netcdf_files(file_list)

    for file in netcdf_files:
        # RAPID-specific URL construction
        download_url = (
            f"{source.rstrip('/')}/{file}" if utilities.is_valid_url(source) else None
        )

        file_path = utilities.resolve_file_path(
            file_name=file,
            source=source,
            download_url=download_url,
            local_data_dir=local_data_dir,
            redownload=redownload,
        )

        # Use ReaderUtils for consistent dataset loading and metadata
        ds = ReaderUtils.safe_load_dataset(file_path)
        file_metadata = RAPID_FILE_METADATA.get(file, {})
        ds = ReaderUtils.attach_standard_metadata(
            ds, file, file_path, RAPID_METADATA, file_metadata
        )

        datasets.append(ds)

    # Use ReaderUtils for validation
    ReaderUtils.validate_datasets_loaded(datasets, file_list)

    return datasets
