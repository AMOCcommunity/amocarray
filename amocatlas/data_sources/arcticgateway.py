"""Arctic Gateway transport data reader for AMOCatlas.

This module provides functions to read and process data from the Arctic Gateway
transport dataset, which includes measurements from key Arctic Ocean gateways:
Fram Strait, Davis Strait, Bering Strait, and Barents Sea Opening.

The data is provided as a zip archive containing multiple NetCDF files for
each gateway, with full-depth velocity adjustments applied.

Key functions:
- read_arcticgateway(): Main data loading interface for Arctic Gateway transport data

Data source: Pan-Arctic Gateway transports since 2004
Project: Norwegian Polar Institute Arctic gateway transport monitoring
"""

from pathlib import Path
from typing import Union
import zipfile
import xarray as xr

from amocatlas import logger, utilities
from amocatlas.utilities import apply_defaults
from amocatlas.reader_utils import ReaderUtils

log = logger.log  # ✅ use the global logger

# Datasource identifier for automatic standardization
DATASOURCE_ID = "arcticgateway"

# Default source and file list
ARCTIC_DEFAULT_SOURCE = "https://next.api.npolar.no/dataset/80b69907-f303-457e-ae41-45d8e2c0787c/attachment/1c52a414-2b76-46d9-b79c-bbf915be35eb/_blob"
ARCTIC_DEFAULT_FILES = ["Adjusted_fulldepth_v0.zip"]
ARCTIC_TRANSPORT_FILES = ["Adjusted_fulldepth_v0.zip"]
ARCTIC_ZIP_CONTENTS = {
    "Adjusted_fulldepth_v0.zip": {
        "Adjusted_fulldepth/BarentsSeaOpening_adjusted_v_fulldepth.nc",
        "Adjusted_fulldepth/BeringStrait_adjusted_v_fulldepth.nc",
        "Adjusted_fulldepth/DavisStrait_adjusted_v_fulldepth.nc",
        "Adjusted_fulldepth/FramStrait_adjusted_v_fulldepth.nc",
    }
}

# Mapping of filenames to download URLs
ARCTIC_FILE_URLS = {
    "Adjusted_fulldepth_v0.zip": (
        "https://next.api.npolar.no/dataset/80b69907-f303-457e-ae41-45d8e2c0787c/attachment/1c52a414-2b76-46d9-b79c-bbf915be35eb/_blob"
    ),
}

# Global metadata for ARCTIC
ARCTIC_METADATA = {
    "comment": "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas",
}

# File-specific metadata placeholder
ARCTIC_FILE_METADATA = {
    "BarentsSeaOpening_adjusted_v_fulldepth.nc": {
        "data_product": "Gateway transport Barents Sea Opening",
        "project": "Pan-Arctic Gateway transports since 2004",
    },
    "BeringStrait_adjusted_v_fulldepth.nc": {
        "data_product": "Gateway transport Bering Strait",
        "project": "Pan-Arctic Gateway transports since 2004",
    },
    "DavisStrait_adjusted_v_fulldepth.nc": {
        "data_product": "Gateway transport Davis Strait",
        "project": "Pan-Arctic Gateway transports since 2004",
    },
    "FramStrait_adjusted_v_fulldepth.nc": {
        "data_product": "Gateway transport Fram Strait",
        "project": "Pan-Arctic Gateway transports since 2004",
    },
}


@apply_defaults(None, ARCTIC_DEFAULT_FILES)
def read_arcticgateway(
    source: str,
    file_list: str | list[str],
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
    track_added_attrs: bool = False,) -> list[xr.Dataset]:
    """Load the ARCTIC Gateway transport dataset from a URL or local file path into xarray Datasets.

    Parameters
    ----------
    source : str, optional
        URL or local path to the NetCDF file(s).
        Defaults to the ARCTIC data repository URL.
    file_list : str or list of str, optional
        Filename or list of filenames to process.
        Defaults to ARCTIC_DEFAULT_FILES.
    transport_only : bool, optional
        If True, restrict to transport files only.
    data_dir : str, Path or None, optional
        Optional local data directory.
    redownload : bool, optional
        If True, force redownload of the data.

    Returns
    -------
    list of xr.Dataset
        List of loaded xarray datasets with basic inline and file-specific metadata.

    Raises
    ------
    ValueError
        If the source is neither a valid URL nor a directory path.
    FileNotFoundError
        If the file cannot be downloaded or does not exist locally.

    """
    log.info("Starting to read ARCTIC Gateway dataset")

    if file_list is None:
        file_list = ARCTIC_DEFAULT_FILES
    if transport_only:
        file_list = ARCTIC_TRANSPORT_FILES
    if isinstance(file_list, str):
        file_list = [file_list]

    local_data_dir = ReaderUtils.setup_data_directory(data_dir)

    # Print information about files being loaded
    ReaderUtils.print_loading_info(file_list, DATASOURCE_ID, ARCTIC_FILE_METADATA)

    datasets = []

    for file in file_list:
        download_url = ARCTIC_FILE_URLS.get(file)
        if not download_url:
            log.error("No download URL found for file: %s", file)
            raise ValueError(f"No download URL found for file: {file}")

        file_path = utilities.resolve_file_path(
            file_name=file,
            source=source,
            download_url=download_url,
            local_data_dir=local_data_dir,
            redownload=redownload,
        )

        # If the file is a zip, extract all contents
        file_path = Path(file_path)
        if file_path.suffix == ".zip":
            contents = ARCTIC_ZIP_CONTENTS.get(file)
            if not contents:
                raise ValueError(
                    f"No internal file mapping provided for zip file: {file}"
                )

            with zipfile.ZipFile(file_path, "r") as zip_ref:
                for member in contents:
                    target_path = local_data_dir / member
                    if redownload or not target_path.exists():
                        log.info("Extracting %s from %s", member, file)
                        zip_ref.extract(member, path=local_data_dir)

            # Look specifically for the .nc file to open
            nc_files = [f for f in contents if f.endswith(".nc")]
            if not nc_files:
                raise FileNotFoundError(
                    f"No NetCDF (.nc) file listed in zip contents for {file}"
                )

            for nc_file in nc_files:
                nc_path = local_data_dir / nc_file
                if not nc_path.exists():
                    raise FileNotFoundError(
                        f"Expected NetCDF file not found: {nc_path}"
                    )

                # Use ReaderUtils for consistent dataset loading
                ds = ReaderUtils.safe_load_dataset(nc_path)

                # Use ReaderUtils for consistent metadata attachment
                file_metadata = ARCTIC_FILE_METADATA.get(nc_file, {})
                ds = ReaderUtils.attach_standard_metadata(
                    ds,
                    nc_file,
                    nc_path,
                    ARCTIC_METADATA,
                    file_metadata,
                    datasource_id=DATASOURCE_ID,
                )

                datasets.append(ds)
        else:
            log.warning(
                "Non-zip ARCTIC Gateway files are not currently supported: %s", file
            )

    # Use ReaderUtils for validation
    ReaderUtils.validate_datasets_loaded(datasets, file_list)
    # Handle track_added_attrs parameter

    if track_added_attrs:

        added_attrs_per_dataset = [[] for _ in datasets]

        return datasets, added_attrs_per_dataset

    else:

        return datasets
