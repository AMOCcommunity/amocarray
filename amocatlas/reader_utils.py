"""Shared utility functions for AMOCatlas readers.

This module provides common functionality used across different array readers
to eliminate code duplication while preserving the unique access patterns
of each data source (HTTP directories, per-file URLs, zip archives).

Key utilities:
- Dataset loading with consistent error handling
- Metadata attachment patterns
- File list preparation
- Data directory management
"""

from pathlib import Path
from typing import Dict, List, Union, Any
import xarray as xr

from amocatlas import logger, utilities
from amocatlas.logger import log_info, log_warning, log_error

log = logger.log

# Mapping from datasource IDs to display names for user-friendly output
DATASOURCE_DISPLAY_NAMES = {
    "rapid26n": "RAPID 26°N",
    "move16n": "MOVE 16°N",
    "osnap55n": "OSNAP",
    "samba34s": "SAMBA 34.5°S",
    "arcticgateway": "Arctic Gateway",
    "fw2015": "Frajka-Williams 2015",
    "mocha26n": "MOCHA 26°N",
    "wh41n": "Willis & Hobbs 41°N",
    "dso": "Denmark Strait Overflow",
    "noac47n": "NOAC 47°N",
    "fbc": "Faroe Bank Channel",
    "calafat2025": "Calafat et al. 2025",
    "zheng2024": "Zheng et al. 2024",
}


class ReaderUtils:
    """Shared utilities for AMOCatlas data readers."""

    @staticmethod
    def safe_load_dataset(file_path: Path, **kwargs) -> xr.Dataset:
        """Load an xarray Dataset with consistent error handling.

        Parameters
        ----------
        file_path : Path
            Path to the NetCDF file to load.
        **kwargs : dict
            Additional keyword arguments passed to xr.open_dataset.

        Returns
        -------
        xr.Dataset
            The loaded xarray Dataset.

        Raises
        ------
        FileNotFoundError
            If the file cannot be opened or read.

        """
        try:
            log_info("Opening dataset: %s", file_path)
            return xr.open_dataset(file_path, **kwargs)
        except (OSError, IOError, ValueError, KeyError) as e:
            log_error("Failed to open NetCDF file: %s: %s", file_path, e)
            raise FileNotFoundError(
                f"Failed to open NetCDF file: {file_path}: {e}"
            ) from e

    @staticmethod
    def attach_standard_metadata(
        ds: xr.Dataset,
        file_name: str,
        file_path: Path,
        global_metadata: Dict[str, Any],
        file_metadata: Dict[str, Any],
        datasource_id: str = None,
    ) -> xr.Dataset:
        """Attach standard metadata to a dataset with datasource identification.

        Parameters
        ----------
        ds : xr.Dataset
            The dataset to add metadata to.
        file_name : str
            Original filename.
        file_path : Path
            Full path to the loaded file.
        global_metadata : dict
            Global metadata for this array type.
        file_metadata : dict
            File-specific metadata.
        datasource_id : str, optional
            Unique identifier for the data source (e.g., 'rapid26n', 'samba34s').
            Used for automatic standardization function selection.

        Returns
        -------
        xr.Dataset
            Dataset with attached metadata including datasource identification.

        """
        log_info("Attaching metadata to dataset from file: %s", file_name)

        # Build metadata dictionary
        metadata = {
            "source_file": file_name,
            "source_path": str(file_path),
            **global_metadata,
            **file_metadata,
        }

        # Add datasource identification if provided
        if datasource_id:
            metadata["amocatlas_datasource"] = datasource_id

        utilities.safe_update_attrs(ds, metadata)
        return ds

    @staticmethod
    def prepare_file_list(
        file_list: Union[str, List[str], None],
        default_files: List[str],
        transport_files: List[str],
        transport_only: bool,
    ) -> List[str]:
        """Prepare the list of files to process.

        Parameters
        ----------
        file_list : str, list of str, or None
            User-provided file list.
        default_files : list of str
            Default files for this array.
        transport_files : list of str
            Transport-only files for this array.
        transport_only : bool
            Whether to restrict to transport files only.

        Returns
        -------
        list of str
            List of files to process.

        """
        if file_list is None:
            file_list = default_files
        if transport_only:
            file_list = transport_files
        if isinstance(file_list, str):
            file_list = [file_list]
        return file_list

    @staticmethod
    def setup_data_directory(data_dir: Union[str, Path, None]) -> Path:
        """Set up the local data directory.

        Parameters
        ----------
        data_dir : str, Path, or None
            User-provided data directory, or None for default.

        Returns
        -------
        Path
            Path to the local data directory.

        """
        local_data_dir = (
            Path(data_dir) if data_dir else utilities.get_default_data_dir()
        )
        local_data_dir.mkdir(parents=True, exist_ok=True)
        return local_data_dir

    @staticmethod
    def filter_netcdf_files(file_list: List[str]) -> List[str]:
        """Filter file list to only include NetCDF files.

        Parameters
        ----------
        file_list : list of str
            List of filenames to filter.

        Returns
        -------
        list of str
            Filtered list containing only .nc files.

        """
        netcdf_files = []
        for file in file_list:
            if file.lower().endswith(".nc"):
                netcdf_files.append(file)
            else:
                log_warning("Skipping non-NetCDF file: %s", file)
        return netcdf_files

    @staticmethod
    def print_loading_info(
        file_list: List[str],
        datasource_id: str,
        file_metadata: Dict[str, Dict[str, Any]],
    ) -> None:
        """Print informative output about files being loaded.

        Parameters
        ----------
        file_list : list of str
            List of files being loaded.
        datasource_id : str
            Datasource identifier (e.g., 'rapid26n', 'samba34s').
        file_metadata : dict
            Dictionary mapping filenames to their metadata dictionaries.

        """
        display_name = DATASOURCE_DISPLAY_NAMES.get(
            datasource_id, datasource_id.upper()
        )
        print(f"Loading {len(file_list)} {display_name} dataset(s):")
        for i, file in enumerate(file_list):
            description = file_metadata.get(file, {}).get(
                "data_product", "No description available"
            )
            print(f"  {i}. {file}: {description}")
        print()

    @staticmethod
    def validate_datasets_loaded(
        datasets: List[xr.Dataset], file_list: List[str]
    ) -> None:
        """Validate that datasets were successfully loaded.

        Parameters
        ----------
        datasets : list of xr.Dataset
            List of loaded datasets.
        file_list : list of str
            Original file list.

        Raises
        ------
        FileNotFoundError
            If no valid datasets were loaded.

        """
        if not datasets:
            log_error("No valid NetCDF files found in %s", file_list)
            raise FileNotFoundError(f"No valid NetCDF files found in {file_list}")

        log_info("Successfully loaded %d dataset(s)", len(datasets))
