from pathlib import Path
from typing import Union

import xarray as xr
import datetime
import pandas as pd

# Import the modules used
from amocatlas import logger, utilities
from amocatlas.logger import log_error, log_info, log_warning
from amocatlas.utilities import apply_defaults

log = logger.log  # Use the global logger

# Default list of 47N data files
A47N_DEFAULT_FILES = [
    "NOAC_AMOC.tab",
]
A47N_TRANSPORT_FILES = ["NOAC_AMOC.tab"]
A47N_DEFAULT_SOURCE = "https://doi.pangaea.de/10.1594/PANGAEA.959558"
A47N_METADATA = {
    "project": "Basin-wide AMOC volume transport from the NOAC array at 47°N in the subpolar North Atlantic (1993-2018) ",
    "weblink": "https://doi.pangaea.de/10.1594/PANGAEA.959558",
    "comment": "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas",
}
# Mapping of filenames to download URLs
A47N_FILE_URLS = {
    "NOAC_AMOC.tab": (
        "https://doi.pangaea.de/10.1594/PANGAEA.959558?format=textfile"
    ),
}

A47N_FILE_METADATA = {
    "NOAC_AMOC.tab": {
        "data_product": "Basin-wide AMOC volume transport from the NOAC array at 47°N in the subpolar North Atlantic (1993-2018)",
    },
}


@apply_defaults(A47N_DEFAULT_SOURCE, A47N_DEFAULT_FILES)
def read_47n(
    ##    source: str,
    source: Union[str, Path, None],
    file_list: Union[str, list[str]],
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
) -> list[xr.Dataset]:
    """Load the 47N transport datasets from a URL or local file path into xarray Datasets.

    Parameters
    ----------                                                  
    source : str, optional
        Local path to the data directory (remote source is handled per-file).
    file_list : str or list of str, optional
        Filename or list of filenames to process.
        Defaults to 47N_DEFAULT_FILES.                            
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
        If no source is provided for a file and no default URL mapping is found.
    FileNotFoundError                                                   
    If the file cannot be downloaded or does not exist locally.

    """
    log.info("Starting to read 47N dataset")  # Ensure file_list has a default
    if file_list is None:
        file_list = A47N_DEFAULT_FILES
    if transport_only:
        file_list = A47N_TRANSPORT_FILES
    if isinstance(file_list, str):
        file_list = [file_list]
    # Determine the local storage path
    local_data_dir = Path(data_dir) if data_dir else utilities.get_default_data_dir()
    local_data_dir.mkdir(parents=True, exist_ok=True)

    datasets = []

    for file in file_list:
        if not (file.lower().endswith(".tab")):
            log_warning("Skipping unsupported file type : %s", file)
            continue

        download_url = A47N_FILE_URLS.get(file)
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

        # Open dataset

        if file.lower().endswith(".tab"):
            # file .tab
            try:
                df = pd.read_csv(
                file_path,
                sep="\t",
                skiprows=31,
                engine="python",
                encoding="utf-8"
            )
            except Exception as e:
                log_error("Failed to parse ASCII file: %s: %s", file_path, e)
                raise FileNotFoundError(f"Failed to parse ASCII file: {file_path}: {e}")
            # Time handling
            try:
                df.rename(columns={'Date/Time': 'TIME'}, inplace=True)

                # Convert TIME to datetime64
                df["TIME"] = pd.to_datetime(df["TIME"], errors="raise")

                ds = df.set_index("TIME").to_xarray()

            except Exception as e:
                log_error("Failed to process time coordinate in %s: %s", file_path, e)
                raise

            except Exception as e:
                log_error(
                    "Failed to convert DataFrame to xarray Dataset for %s: %s",
                    file,
                    e,
                )
                raise ValueError(
                    f"Failed to convert DataFrame to xarray Dataset for {file}: {e}",
                )
            # Attach metadata
            file_metadata = A47N_FILE_METADATA.get(file, {})
            log_info("Attaching metadata to 47N dataset from file: %s", file)
            utilities.safe_update_attrs(
                ds,
                {
                    "source_file": file,
                    "source_path": str(file_path),
                    **A47N_METADATA,
                    **file_metadata,
                },
            )

        datasets.append(ds)

    if not datasets:
        log_error("No valid 47N files in %s", file_list)
        raise FileNotFoundError(f"No valid data files found in {file_list}")

    log_info("Successfully loaded %d 47N dataset(s)", len(datasets))
    return datasets
