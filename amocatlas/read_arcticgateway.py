from pathlib import Path
from typing import Union
import zipfile
import xarray as xr

from amocatlas import logger, utilities
from amocatlas.utilities import apply_defaults

log = logger.log  # ✅ use the global logger

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
) -> list[xr.Dataset]:
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

    # Determine the local storage path
    local_data_dir = Path(data_dir) if data_dir else utilities.get_default_data_dir()
    local_data_dir.mkdir(parents=True, exist_ok=True)

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

                log.info("Opening ARCTIC Gateway dataset: %s", nc_path)
                try:
                    ds = xr.open_dataset(nc_path)
                except Exception as e:
                    log.error("Failed to open NetCDF file: %s: %s", nc_path, e)
                    raise FileNotFoundError(
                        f"Failed to open NetCDF file: {nc_path}: {e}"
                    )

                metadata = ARCTIC_FILE_METADATA.get(nc_file, {})
                utilities.safe_update_attrs(
                    ds,
                    {
                        "source_file": nc_file,
                        "source_path": str(nc_path),
                        **ARCTIC_METADATA,
                        **metadata,
                    },
                )

                datasets.append(ds)
        else:
            log.warning(
                "Non-zip ARCTIC Gateway files are not currently supported: %s", file
            )

    if not datasets:
        log.error("No valid NetCDF files found in %s", file_list)
        raise FileNotFoundError(f"No valid NetCDF files found in {file_list}")

    log.info("Successfully loaded %d ARCTIC Gateway dataset(s)", len(datasets))
    return datasets
