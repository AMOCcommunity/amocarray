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
    read_osnap_2025,
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


def _return_single_or_list(datasets: List[xr.Dataset], all_files: bool) -> Union[xr.Dataset, List[xr.Dataset]]:
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


def _create_array_function(reader_func, array_name: str, supports_version: bool = False):
    """Create a uniform API function for an array reader.
    
    This factory function eliminates repetition by generating the standard
    interface for each array reader automatically.
    
    Parameters
    ----------
    reader_func : callable
        The underlying reader function (e.g., read_rapid)
    array_name : str
        Name of the array (for documentation)
    supports_version : bool, optional
        Whether this reader supports the version parameter
        
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
        data_dir: Union[str, Path, None] = None,
        redownload: bool = False,
        version: str = None,
    ) -> Union[xr.Dataset, List[xr.Dataset]]:
        # Build kwargs for the underlying reader
        kwargs = {
            'source': source,
            'file_list': file_list, 
            'transport_only': transport_only,
            'data_dir': data_dir,
            'redownload': redownload,
        }
        
        # Only pass version if the reader supports it
        if supports_version and version is not None:
            kwargs['version'] = version
        
        datasets = reader_func(**kwargs)
        return _return_single_or_list(datasets, all_files)
    
    # Add proper docstring
    array_function.__doc__ = f"""Load {array_name} array data.
    
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
    data_dir : str, Path, or None, optional
        Local directory for data storage.
    redownload : bool, optional
        Force redownload of data. Default: False.
    version : str, optional
        Dataset version{' (used for version selection)' if supports_version else ' (ignored for this array)'}. Default: None.
        
    Returns
    -------
    xr.Dataset or list of xr.Dataset
        Single dataset (default) or list of datasets if all_files=True.
    """
    
    return array_function


# Create all array functions using the factory pattern
rapid = _create_array_function(read_rapid, "RAPID 26°N")
move = _create_array_function(read_move, "MOVE 16°N") 
osnap = _create_array_function(read_osnap, "OSNAP", supports_version=True)
samba = _create_array_function(read_samba, "SAMBA 34.5°S")
arcticgateway = _create_array_function(read_arcticgateway, "Arctic Gateway")
fw2015 = _create_array_function(read_fw2015, "Frajka-Williams 2015")
mocha = _create_array_function(read_mocha, "MOCHA")
array_41n = _create_array_function(read_41n, "41°N")
dso = _create_array_function(read_dso, "Denmark Strait Overflow")
array_47n = _create_array_function(read_47n, "47°N")
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
    "array_41n",
    "dso", 
    "array_47n",
    "fbc",
]