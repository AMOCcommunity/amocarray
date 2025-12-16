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

# Default list of 41N data files
FBC_DEFAULT_FILES = [
    "FBC_overflow_transport.txt",
]
FBC_TRANSPORT_FILES = ["FBC_overflow_transport.txt"]
FBC_DEFAULT_SOURCE = "https://envofar.fo/var/ftp/Timeseries/"

FBC_METADATA = {
    "project": "Faroe Bank Channel overflow 1995-2015",
    "weblink": "https://envofar.fo/var/ftp/Timeseries/FBC_overflow_transport.txt",
    "comment": "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas",
}

FBC_FILE_METADATA = {
    "FBC_overflow_transport.txt": {
        "data_product": "Daily averaged kinematic FBC-overflow flux (transport) in Sv",
    },
}

@apply_defaults(FBC_DEFAULT_SOURCE, FBC_DEFAULT_FILES)
def read_fbc(
    ##    source: str,
    source: Union[str, Path, None],
    file_list: Union[str, list[str]],
    transport_only: bool = True,
    data_dir: Union[str, Path, None] = None,
    redownload: bool = False,
) -> list[xr.Dataset]:
    """Load the 41N transport datasets from a URL or local file path into xarray Datasets.

    Parameters
    ----------
    ----------                                                      
    source : str, optional
        Local path to the data directory (remote source is handled per-file).

    file_list : str or list of str, optional
        Filename or list of filenames to process.
        Defaults to FBC_DEFAULT_FILES. 
                 
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
    log.info("Starting to read FBC dataset")  # Ensure file_list has a default
    if file_list is None:
        file_list = FBC_DEFAULT_FILES
    if transport_only:
        file_list = FBC_TRANSPORT_FILES
    if isinstance(file_list, str):
        file_list = [file_list]
    # Determine the local storage path
    local_data_dir = Path(data_dir) if data_dir else utilities.get_default_data_dir()
    local_data_dir.mkdir(parents=True, exist_ok=True)

    datasets = []

    for file in file_list:
        if not (file.lower().endswith(".txt")):
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
        if file.lower().endswith(".txt"):
            # file.txt
            try:
                # column_names, _ = utilities.parse_ascii_header(
                #     file_path, comment_char="%"
                # )
                data_start = utilities.find_data_start(file_path)

                df = pd.read_csv(
                    file_path,
                    sep=r"\s+",
                    encoding="latin-1",
                    skiprows=data_start,
                    names=["Decimal year", "Month", "Day", "Flux"],
                )
            except Exception as e:
                log_error("Failed to parse ASCII file: %s: %s", file_path, e)
                raise FileNotFoundError(f"Failed to parse ASCII file: {file_path}: {e}")

            # Time handling
            try:
                df = df.apply(
                    lambda col: col.astype(str)
                    .str.replace(",", "", regex=False)
                    .astype(float)
                )
                # df['Decimal year'] = df['Decimal year'].astype(str).str.replace(',', '',regex=False).astype(float)
                df["TIME"] = df["Decimal year"].apply(
                    lambda x: datetime.datetime(int(x), 1, 1)
                    + datetime.timedelta(
                        days=(x - int(x))
                        * (
                            datetime.datetime(int(x) + 1, 1, 1)
                            - datetime.datetime(int(x), 1, 1)
                        ).days
                    )
                )
                df = df.drop(columns=["Decimal year"])
                ds = df.set_index("TIME").to_xarray()
            except Exception as e:
                log_error(
                    "Failed to convert DataFrame to xarray Fataset for %s: %s",
                    file,
                    e,
                )
                raise ValueError(
                    f"Failed to convert DataFrame to xarray Dataset for {file}: {e}",
                )

            # Attach metadata
            file_metadata = FBC_FILE_METADATA.get(file, {})
            log_info("Attaching metadata to 41N dataset from file: %s", file)
            utilities.safe_update_attrs(
                ds,
                {
                    "source_file": file,
                    "source_path": str(file_path),
                    **FBC_METADATA,
                    **file_metadata,
                },
            )

        datasets.append(ds)

    if not datasets:
        log_error("No valid FBC files in %s", file_list)
        raise FileNotFoundError(f"No valid data files found in {file_list}")

    log_info("Successfully loaded %d FBC dataset(s)", len(datasets))
    return datasets