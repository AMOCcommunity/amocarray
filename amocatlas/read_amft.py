from pathlib import Path
from typing import Union

import xarray as xr
import datetime

# Import the modules used
from amocatlas import logger, utilities
from amocatlas.logger import log_error, log_info, log_warning
from amocatlas.utilities import apply_defaults

log = logger.log  # Use the global logger

# Default list of AMFT (Atlantic meridional freshwater transport) data files
AMFT_DEFAULT_FILES = [
    "atl_mft_2000_extend_gpcp_oaflux.nc"
]
AMFT_TRANSPORT_FILES = ["atl_mft_2000_extend_gpcp_oaflux.nc"]
AMFT_DEFAULT_SOURCE = "https://zenodo.org/records/12790901/files/"

AMFT_METADATA = {
    "project": "An observation-based estimate of the Atlantic meridional freshwater transport",
    "weblink": "https://zenodo.org/records/12790901",
    "comment": "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas",
    "acknowledgement": "This study was supported by the NationalNatural Science Foundation of China(Grant 42122046, 42076202, 42075036),National Key Scientific and TechnologicalInfrastructure project “Earth SystemScience Numerical Simulator Facility”(EarthLab) and the new CornerstoneScience Foundation through theXPLORER PRIZE. F. Li acknowledgesthe financial support from the NationalKey R&D Program of China (Grant2023YFF0805102). Gratitude is extendedto Elaine L. McDonagh, who graciouslyshared RAPID freshwater transport data.",
    "doi": "http://doi.org/10.1029/2024gl110021",
    "paper": "Zheng, H., Cheng, L., Li, F., Pan, Y., &Zhu, C. (2024). An observation-based estimate of Atlantic meridional freshwatertransport. Geophysical Research Letters,51, e2024GL110021. http://doi.org/10.1029/2024gl110021",
}

AMFT_FILE_METADATA = {
    "atl_mft_2000_extend_gpcp_oaflux.nc": {
        "data_product": "An observation-based estimate of the Atlantic meridional freshwater transport",
    }
}


@apply_defaults(AMFT_DEFAULT_SOURCE, AMFT_DEFAULT_FILES)
def read_amft(
    source: Union[str, Path, None],
    file_list: Union[str, list[str]],
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
) -> list[xr.Dataset]:
    """Load the AMFT transport datasets from a URL or local file path into xarray Datasets.

    Parameters
    ----------
    ----------                                                     
    source : str, optional
        Local path to the data directory (remote source is handled per-file).

    file_list : str or list of str, optional
        Filename or list of filenames to process.
        Defaults to AMFT_DEFAULT_FILES.  

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
    ------                                                          
    ValueError
        If no source is provided for a file and no default URL mapping is found.
    FileNotFoundError                                                   
        If the file cannot be downloaded or does not exist locally.

    """
    log.info("Starting to read AMFT dataset")  # Ensure file_list has a default
    if file_list is None:
        file_list = AMFT_DEFAULT_FILES
    if transport_only:
        file_list = AMFT_TRANSPORT_FILES
    if isinstance(file_list, str):
        file_list = [file_list]
    # Determine the local storage path
    local_data_dir = Path(data_dir) if data_dir else utilities.get_default_data_dir()
    local_data_dir.mkdir(parents=True, exist_ok=True)

    datasets = []

    for file in file_list:
        if not (file.lower().endswith(".nc")):
            log_warning("Skipping unsupported file type : %s", file)
            continue

        download_url = (
            f"{source.rstrip('/')}/{file}" if utilities._is_valid_url(source) else None
        )

        file_path = utilities.resolve_file_path(
            file_name=file,
            source=source,
            download_url=download_url,
            local_data_dir=local_data_dir,
            redownload=redownload,
        )

        # Open dataset

        if file.lower().endswith(".nc"):
            try:
                log.info("Opening AMFT dataset: %s", file_path)
                ds = xr.open_dataset(file_path)
            except Exception as e:
                log.error("Failed to open NetCDF file: %s: %s", file_path, e)
                raise FileNotFoundError(
                    f"Failed to open NetCDF file : {file_path}: {e}"
                )
            # Attach metadata
            file_metadata = AMFT_FILE_METADATA.get(file, {})
            log_info("Attaching metadata to AMFT dataset from file: %s", file)
            utilities.safe_update_attrs(
                ds,
                {
                    "source_file": file,
                    "source_path": str(file_path),
                    **AMFT_METADATA,
                    **file_metadata,
                },
            )
        else:
            raise ValueError(
                f"Failed to convert to xarray Dataset for {file}: {e}",
            )
        

        datasets.append(ds)

    if not datasets:
        log_error("No valid AMFT files in %s", file_list)
        raise FileNotFoundError(f"No valid data files found in {file_list}")

    log_info("Successfully loaded %d AMFT dataset(s)", len(datasets))
    return datasets