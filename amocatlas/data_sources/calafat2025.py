"""Calafat et al. 2025 MHT data reader for AMOCatlas.

This module provides functions to read and process Atlantic Meridional Heat
Transport (MHT) data from Calafat et al. (2025). This dataset provides
observations and estimates of meridional heat transport across multiple
latitudes in the Atlantic Ocean.
"""

from pathlib import Path
from typing import Union
import zipfile
import xarray as xr

from amocatlas import logger, utilities
from amocatlas.logger import log_info
from amocatlas.utilities import apply_defaults
from amocatlas.reader_utils import ReaderUtils

log = logger.log  # ✅ use the global logger

# Datasource identifier for automatic standardization
DATASOURCE_ID = "calafat2025"

# Default source and file list
CALAFAT2025_DEFAULT_SOURCE = "https://zenodo.org/records/16640426/files/Bayesian_estimates_Atlantic_MHT.zip?download=1"
CALAFAT2025_DEFAULT_FILES = ["Bayesian_estimates_Atlantic_MHT.zip"]
CALAFAT2025_TRANSPORT_FILES = ["Bayesian_estimates_Atlantic_MHT.zip"]
CALAFAT2025_ZIP_CONTENTS = {
    "Bayesian_estimates_Atlantic_MHT.zip": {
        "Bayesian_estimates_Atlantic_MHT.nc",
        "README.txt",
    }
}

# Mapping of filenames to download URLs
CALAFAT2025_FILE_URLS = {
    "Bayesian_estimates_Atlantic_MHT.zip": (
        "https://zenodo.org/records/16640426/files/Bayesian_estimates_Atlantic_MHT.zip?download=1"
    ),
}

# Global metadata for MOCHA
CALAFAT2025_METADATA = {
    "comment": "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas",
}

# File-specific metadata placeholder
CALAFAT2025_FILE_METADATA = {
    "Bayesian_estimates_Atlantic_MHT.nc": {
        "data_product": "MHT estimates at 12 latitudes across the Atlantic based on spatiotemporal Bayesian hierarchical model",
        "project": "CALAFAT2025",
        # Add specific acknowledgments here if needed in future
    },
}


@apply_defaults(None, CALAFAT2025_DEFAULT_FILES)
def read_calafat2025(
    source: str,
    file_list: str | list[str],
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
    track_added_attrs: bool = False,) -> list[xr.Dataset]:
    """Load the CALAFAT2025 transport dataset from a URL or local file path into xarray Datasets.

    Parameters
    ----------
    source : str, optional
        URL or local path to the NetCDF file(s).
        Defaults to the CALAFAT2025 data repository URL.
    file_list : str or list of str, optional
        Filename or list of filenames to process.
        Defaults to CALAFAT2025_DEFAULT_FILES.
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
    log.info("Starting to read CALAFAT2025 dataset")


    # Load YAML metadata with fallback
    global_metadata, yaml_file_metadata = ReaderUtils.load_array_metadata_with_fallback(
        DATASOURCE_ID, CALAFAT2025_METADATA
    )

    if file_list is None:
        if transport_only:
            file_list = CALAFAT2025_TRANSPORT_FILES
        else:
            file_list = CALAFAT2025_DEFAULT_FILES
    if isinstance(file_list, str):
        file_list = [file_list]

    # Determine the local storage path
    local_data_dir = Path(data_dir) if data_dir else utilities.get_default_data_dir()
    local_data_dir.mkdir(parents=True, exist_ok=True)

    # Print information about files being loaded
    ReaderUtils.print_loading_info(file_list, DATASOURCE_ID, CALAFAT2025_FILE_METADATA)

    datasets = []

    added_attrs_per_dataset = [] if track_added_attrs else None
    for file in file_list:
        download_url = CALAFAT2025_FILE_URLS.get(file)
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
            contents = CALAFAT2025_ZIP_CONTENTS.get(file)
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
                
                # Fix Calafat time coordinate: convert decimal years to standard format
                if 'time' in ds.coords:
                    import pandas as pd
                    import numpy as np
                    
                    # Convert from 'time' to 'TIME' and from decimal years to seconds since 1970
                    decimal_years = ds['time'].values
                    log_info("Converting Calafat decimal years to standard TIME format")
                    
                    # Convert decimal years to datetime
                    datetime_values = []
                    for year in decimal_years:
                        # Split into year and fraction
                        year_int = int(year)
                        year_frac = year - year_int
                        
                        # Calculate days into the year
                        year_start = pd.Timestamp(f"{year_int}-01-01")
                        next_year = pd.Timestamp(f"{year_int + 1}-01-01")
                        days_in_year = (next_year - year_start).days
                        days_into_year = year_frac * days_in_year
                        
                        # Create the datetime
                        result_time = year_start + pd.Timedelta(days=days_into_year)
                        datetime_values.append(result_time)
                    
                    # Convert to seconds since 1970-01-01
                    epoch = pd.Timestamp('1970-01-01')
                    seconds_since_1970 = np.array([(dt - epoch).total_seconds() for dt in datetime_values])
                    
                    # Replace 'time' coordinate with 'TIME' 
                    ds = ds.rename({'time': 'TIME'})
                    ds = ds.assign_coords(TIME=seconds_since_1970)
                    
                    # Add proper TIME coordinate attributes
                    ds['TIME'].attrs.update({
                        "long_name": "Time elapsed since 1970-01-01T00:00:00Z",
                        "standard_name": "time",
                        "calendar": "gregorian", 
                        "units": "seconds since 1970-01-01T00:00:00Z",
                        "vocabulary": "http://vocab.nerc.ac.uk/collection/OG1/current/TIME/"
                    })

                # Use ReaderUtils for consistent metadata attachment
                file_metadata = CALAFAT2025_FILE_METADATA.get(nc_file, {})
                
                if track_added_attrs:
                    # Use tracking version to collect attribute changes
                    ds, attr_changes = ReaderUtils.attach_metadata_with_tracking(
                        ds,
                        nc_file,
                        nc_path,
                        CALAFAT2025_METADATA,
                        {},  # yaml metadata (CALAFAT2025 doesn't have separate YAML files)
                        file_metadata,
                        DATASOURCE_ID,
                        track_added_attrs=True
                    )
                    added_attrs_per_dataset.append(attr_changes)
                else:
                    # Standard metadata attachment without tracking
                    ds = ReaderUtils.attach_standard_metadata(
                        ds,
                        nc_file,
                        nc_path,
                        CALAFAT2025_METADATA,
                        file_metadata,
                        datasource_id=DATASOURCE_ID,
                    )

                datasets.append(ds)
        else:
            log.warning(
                "Non-zip CALAFAT2025 files are not currently supported: %s", file
            )

    if not datasets:
        log.error("No valid NetCDF files found in %s", file_list)
        raise FileNotFoundError(f"No valid NetCDF files found in {file_list}")

    log.info("Successfully loaded %d CALAFAT2025 dataset(s)", len(datasets))
    # Handle track_added_attrs parameter

    if track_added_attrs:
        return datasets, added_attrs_per_dataset
    else:
        return datasets
