"""Intuitive namespace API for AMOCatlas data readers.

This module provides a more user-friendly API for accessing AMOC array data
with discoverable function names and consistent return types. Each array gets
its own function with IDE autocompletion support.

Key improvements over readers.load_dataset():
- Single dataset returned by default (most common use case)
- all_files=True parameter for power users who need multiple files
- Array-specific parameters feel natural (e.g., version for OSNAP)
- IDE autocompletion works for array names

Examples
--------
Basic usage (single dataset):
    >>> from amocatlas import read
    >>> data = read.rapid()                    # Single transport dataset
    >>> osnap = read.osnap(version="2025")     # Latest OSNAP data
    >>> arctic = read.arcticgateway()          # Arctic gateway transports

Power user access (multiple datasets):
    >>> all_rapid = read.rapid(all_files=True)     # List of all RAPID files
    >>> all_osnap = read.osnap(all_files=True)      # List of all OSNAP files

Custom parameters:
    >>> rapid_custom = read.rapid(
    ...     source="https://my-mirror.com/rapid/",
    ...     transport_only=False,
    ...     redownload=True
    ... )

"""

from typing import Union, List
import xarray as xr
from pathlib import Path

# Import all the individual readers from the data_sources package
from .data_sources import (
    read_rapid,
    read_move,
    read_osnap,
    read_samba,
    read_fw2015,
    read_mocha,
    read_41n,
    read_dso,
    read_calafat2025,
    read_zheng2024,
    read_47n,
    read_fbc,
    read_arcticgateway,
)

# Import standardization functions
from . import standardise

# Mapping from datasource_id to standardization functions
STANDARDIZATION_MAP = {
    "rapid26n": standardise.standardise_rapid,
    "move16n": standardise.standardise_move,
    "osnap55n": standardise.standardise_osnap,
    "samba34s": standardise.standardise_samba,
    "arcticgateway": standardise.standardise_arcticgateway,
    "fw2015": standardise.standardise_fw2015,
    "mocha26n": standardise.standardise_mocha,
    "wh41n": standardise.standardise_41n,
    "dso": standardise.standardise_dso,
    "noac47n": standardise.standardise_47n,
    "fbc": standardise.standardise_fbc,
    "calafat2025": standardise.standardise_calafat2025,
    "zheng2024": standardise.standardise_zheng2024,
}


def _return_single_or_list(
    datasets: List[xr.Dataset], all_files: bool
) -> Union[xr.Dataset, List[xr.Dataset]]:
    """Helper function to return single dataset or list based on all_files parameter.

    Parameters
    ----------
    datasets : list of xr.Dataset
        List of loaded datasets.
    all_files : bool
        If True, return the list. If False, return single dataset.

    Returns
    -------
    xr.Dataset or list of xr.Dataset
        Single dataset if all_files=False, list if all_files=True.

    Raises
    ------
    ValueError
        If no datasets were loaded.

    """
    if not datasets:
        raise ValueError("No datasets were loaded")

    return datasets if all_files else datasets[0]


def _create_array_function(
    reader_func, array_name: str, supports_version: bool = False
):
    """Create a uniform API function for an array reader with optional standardization.

    This factory function eliminates repetition by generating the standard
    interface for each array reader automatically. By default, applies standardization
    for clean, analysis-ready data unless raw=True is specified.

    Parameters
    ----------
    reader_func : callable
        The underlying reader function (e.g., read_rapid)
    array_name : str
        Name of the array (for documentation)
    supports_version : bool, optional
        Whether this reader supports the version parameter
    standardize_func : callable, optional
        Standardization function to apply (e.g., standardise.standardise_rapid)

    Returns
    -------
    callable
        A function with uniform signature that wraps the reader

    """

    def array_function(
        source: Union[str, Path, None] = None,
        file_list: Union[str, List[str], None] = None,
        transport_only: bool = True,
        all_files: bool = False,
        raw: bool = False,
        data_dir: Union[str, Path, None] = None,
        redownload: bool = False,
        version: str = None,
        track_added_attrs: bool = False,
    ) -> Union[xr.Dataset, List[xr.Dataset], tuple]:
        # Build kwargs for the underlying reader
        # If all_files=True, automatically disable transport_only to get all files
        effective_transport_only = transport_only and not all_files

        kwargs = {
            "source": source,
            "file_list": file_list,
            "transport_only": effective_transport_only,
            "data_dir": data_dir,
            "redownload": redownload,
            "track_added_attrs": track_added_attrs,
        }

        # Only pass version if the reader supports it
        if supports_version and version is not None:
            kwargs["version"] = version

        # Load raw datasets
        reader_result = reader_func(**kwargs)
        
        # Handle the case where track_added_attrs=True returns a tuple
        if track_added_attrs:
            datasets, added_attrs_per_dataset = reader_result
        else:
            datasets = reader_result
            added_attrs_per_dataset = None

        # Apply standardization by default (unless raw=True)
        if not raw:
            try:
                # Apply standardization to each dataset based on its datasource_id
                standardized_datasets = []
                for i, ds in enumerate(datasets):
                    # Get datasource_id from dataset metadata
                    datasource_id = ds.attrs.get("amocatlas_datasource")

                    if datasource_id and datasource_id in STANDARDIZATION_MAP:
                        # Get file name for standardization (needed by standardize functions)
                        if isinstance(file_list, list) and i < len(file_list):
                            file_name = file_list[i]
                        elif isinstance(file_list, str):
                            file_name = file_list
                        else:
                            # Use source_file from metadata or default
                            file_name = ds.attrs.get(
                                "source_file", f"{array_name.lower()}_data.nc"
                            )

                        standardize_func = STANDARDIZATION_MAP[datasource_id]
                        standardized_ds = standardize_func(ds, file_name)
                        standardized_datasets.append(standardized_ds)
                    else:
                        # No standardization available, keep raw data
                        standardized_datasets.append(ds)

                datasets = standardized_datasets

            except Exception as e:
                # If standardization fails, log warning but continue with raw data
                import warnings

                warnings.warn(
                    f"Standardization failed for {array_name}: {e}. Returning raw data.",
                    UserWarning,
                    stacklevel=2,
                )

        # Return datasets and optionally added_attrs
        result = _return_single_or_list(datasets, all_files)
        
        if track_added_attrs:
            # Return tuple of (datasets, added_attrs) 
            if all_files:
                # If returning list of datasets, return list of metadata changes dicts
                return result, added_attrs_per_dataset
            else:
                # If returning single dataset, return single metadata changes dict
                return result, added_attrs_per_dataset[0] if added_attrs_per_dataset else {"added": [], "modified": []}
        else:
            return result

    # Add proper docstring
    array_function.__doc__ = f"""Load {array_name} array data.
    
    By default, returns standardized, analysis-ready data with consistent variable names,
    metadata, and units following oceanographic conventions. Use raw=True to get data
    in original format from the source files.
    
    Parameters
    ----------
    source : str, Path, or None, optional
        URL or local path to the data source.
    file_list : str, list of str, or None, optional
        Specific files to load. Defaults to transport files.
    transport_only : bool, optional
        If True, load only transport data. Default: True.
    all_files : bool, optional
        If True, return list of all datasets. If False, return single dataset. Default: False.
    raw : bool, optional
        If True, return data in original format without standardization. 
        If False (default), apply standardization for analysis-ready data.
    data_dir : str, Path, or None, optional
        Local directory for data storage.
    redownload : bool, optional
        Force redownload of data. Default: False.
    version : str, optional
        Dataset version{' (used for version selection)' if supports_version else ' (ignored for this array)'}. Default: None.
        
    Returns
    -------
    xr.Dataset or list of xr.Dataset
        Standardized dataset (default) or raw dataset if raw=True.
        Single dataset by default, or list of datasets if all_files=True.
        
    Notes
    -----
    Standardization includes:
    - Consistent variable names across arrays
    - Proper CF-compliant metadata and attributes  
    - Standardized units following oceanographic conventions
    - Additional quality control and formatting
    """

    return array_function


# Create all array functions using the factory pattern with automatic standardization
rapid = _create_array_function(read_rapid, "RAPID 26°N")
move = _create_array_function(read_move, "MOVE 16°N")
osnap = _create_array_function(read_osnap, "OSNAP", supports_version=True)
samba = _create_array_function(read_samba, "SAMBA 34.5°S")
arcticgateway = _create_array_function(read_arcticgateway, "Arctic Gateway")
fw2015 = _create_array_function(read_fw2015, "Frajka-Williams 2015")
mocha = _create_array_function(read_mocha, "MOCHA")
wh41n = _create_array_function(read_41n, "41°N")
dso = _create_array_function(read_dso, "Denmark Strait Overflow")
noac47n = _create_array_function(read_47n, "47°N")
fbc = _create_array_function(read_fbc, "Faroe Bank Channel")
calafat2025 = _create_array_function(read_calafat2025, "Calafat et al. 2025")
zheng2024 = _create_array_function(read_zheng2024, "Zheng et al. 2024")


# Define __all__ to control what's exported
__all__ = [
    "rapid",
    "move",
    "osnap",
    "samba",
    "arcticgateway",
    "fw2015",
    "mocha",
    "wh41n",
    "dso",
    "noac47n",
    "fbc",
    "calafat2025",
    "zheng2024",
]
