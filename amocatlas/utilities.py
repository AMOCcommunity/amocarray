"""Utility functions for AMOCatlas package.

This module provides shared utility functions including:
- File download and caching
- Data directory management
- URL and path validation
- Metadata loading and validation
- Decorator functions for default parameters
"""

from ftplib import FTP
from functools import wraps
from importlib import resources
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple, Union
from urllib.parse import urlparse
import re
import yaml

import pandas as pd
import requests
import xarray as xr

from amocatlas import logger
from amocatlas.logger import log_debug

log = logger.log


def get_project_root() -> Path:
    """Return the absolute path to the project root directory."""
    return Path(__file__).resolve().parent.parent


def get_default_data_dir() -> Path:
    """Get the default data directory path for AMOCatlas."""
    return Path(__file__).resolve().parent.parent / "data"


def apply_defaults(default_source: str, default_files: List[str]) -> Callable:
    """Decorator to apply default values for 'source' and 'file_list' parameters if they are None.

    Parameters
    ----------
    default_source : str
        Default source URL or path.
    default_files : list of str
        Default list of filenames.

    Returns
    -------
    Callable
        A wrapped function with defaults applied.

    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(
            source: Optional[str] = None,
            file_list: Optional[List[str]] = None,
            *args,
            **kwargs,
        ) -> Callable:
            if source is None:
                source = default_source
            if file_list is None:
                file_list = default_files
            return func(source=source, file_list=file_list, *args, **kwargs)

        return wrapper

    return decorator


def normalize_whitespace(attrs: dict) -> dict:
    """Replace non-breaking & other unusual whitespace in every string attr value
    with a normal ASCII space, and collapse runs of whitespace down to one space.
    """
    ws_pattern = re.compile(r"\s+")
    cleaned = {}
    for k, v in attrs.items():
        if isinstance(v, str):
            # 1) replace non-breaking spaces with normal spaces
            t = v.replace("\u00a0", " ")
            # 2) collapse any runs of whitespace (tabs, newlines, NBSP, etc.) to a single space
            t = ws_pattern.sub(" ", t).strip()
            cleaned[k] = t
        else:
            cleaned[k] = v
    return cleaned


def resolve_file_path(
    file_name: str,
    source: Union[str, Path, None],
    download_url: Optional[str],
    local_data_dir: Path,
    redownload: bool = False,
) -> Path:
    """Resolve the path to a data file, using local source, cache, or downloading if necessary.

    Parameters
    ----------
    file_name : str
        The name of the file to resolve.
    source : str or Path or None
        Optional local source directory.
    download_url : str or None
        URL to download the file if needed.
    local_data_dir : Path
        Directory where downloaded files are stored.
    redownload : bool, optional
        If True, force redownload even if cached file exists.

    Returns
    -------
    Path
        Path to the resolved file.

    """
    # Use local source if provided
    if source and not is_valid_url(source):
        source_path = Path(source)
        candidate_file = source_path / file_name
        if candidate_file.exists():
            log.info("Using local file: %s", candidate_file)
            return candidate_file
        else:
            log.error("Local file not found: %s", candidate_file)
            raise FileNotFoundError(f"Local file not found: {candidate_file}")

    # Use cached file if available and redownload is False
    cached_file = local_data_dir / file_name
    if cached_file.exists() and not redownload:
        log.info("Using cached file: %s", cached_file)
        return cached_file

    # Download if URL is provided
    if download_url:
        try:
            log.info("Downloading file from %s to %s", download_url, local_data_dir)
            return download_file(
                download_url, local_data_dir, redownload=redownload, filename=file_name
            )
        except (OSError, IOError, ConnectionError, TimeoutError) as e:
            log.exception("Failed to download %s", download_url)
            raise FileNotFoundError(f"Failed to download {download_url}: {e}") from e

    # If no options succeeded
    raise FileNotFoundError(
        f"File {file_name} could not be resolved from local source, cache, or remote URL.",
    )


def load_array_metadata(datasource_id: str) -> dict:
    """Load metadata YAML for a given data source.

    Parameters
    ----------
    datasource_id : str
        Datasource identifier (e.g., 'rapid26n', 'samba34s').

    Returns
    -------
    dict
        Dictionary containing the parsed YAML metadata.

    """
    try:
        with (
            resources.files("amocatlas.metadata")
            .joinpath(f"{datasource_id.lower()}.yml")
            .open("r") as f
        ):
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"No metadata file found for datasource: {datasource_id}"
        ) from e
    except Exception as e:
        raise RuntimeError(
            f"Error loading metadata for datasource {datasource_id}: {e}"
        ) from e


def safe_update_attrs(
    ds: xr.Dataset,
    new_attrs: Dict[str, str],
    overwrite: bool = False,
    verbose: bool = True,
) -> xr.Dataset:
    """Safely update attributes of an xarray Dataset without overwriting existing keys,
    unless explicitly allowed.

    Parameters
    ----------
    ds : xr.Dataset
        The xarray Dataset whose attributes will be updated.
    new_attrs : dict of str
        Dictionary of new attributes to add.
    overwrite : bool, optional
        If True, allow overwriting existing attributes. Defaults to False.
    verbose : bool, optional
        If True, emit a warning when skipping existing attributes. Defaults to True.

    Returns
    -------
    xr.Dataset
        The dataset with updated attributes.

    """
    for key, value in new_attrs.items():
        if key in ds.attrs:
            if not overwrite:
                if verbose:
                    log_debug(
                        f"Attribute '{key}' already exists in dataset attrs and will not be overwritten.",
                    )
                continue  # Skip assignment
        ds.attrs[key] = value

    return ds


# Validate the structure and required fields of an array-level metadata YAML.
REQUIRED_GLOBAL_FIELDS = [
    "project",
    "weblink",
    "time_coverage_start",
    "time_coverage_end",
]

REQUIRED_VARIABLE_FIELDS = [
    "units",
    "standard_name",
]


def validate_array_yaml(datasource_id: str, verbose: bool = True) -> bool:
    """Validate the structure and required fields of a datasource metadata YAML.

    Parameters
    ----------
    datasource_id : str
        The datasource identifier (e.g., 'rapid26n', 'samba34s').
    verbose : bool
        If True, print detailed validation messages.

    Returns
    -------
    bool
        True if validation passes, False otherwise.

    """
    try:
        meta = load_array_metadata(datasource_id)
    except (FileNotFoundError, yaml.YAMLError, KeyError) as e:
        if verbose:
            print(f"Failed to load metadata for datasource '{datasource_id}': {e}")
        return False

    success = True

    # Check required global metadata fields
    global_meta = meta.get("metadata", {})
    for field in REQUIRED_GLOBAL_FIELDS:
        if field not in global_meta:
            success = False
            if verbose:
                print(f"Missing required global metadata field: {field}")

    # Check each file's variable definitions
    for file_name, file_meta in meta.get("files", {}).items():
        variables = file_meta.get("variables", {})
        for var_name, var_attrs in variables.items():
            for field in REQUIRED_VARIABLE_FIELDS:
                if field not in var_attrs:
                    success = False
                    if verbose:
                        print(
                            f"Missing '{field}' for variable '{var_name}' in file '{file_name}'"
                        )

    if success and verbose:
        print(f"Validation passed for datasource '{datasource_id}'.")

    return success


def _validate_dims(ds: xr.Dataset) -> None:
    """Validate the dimensions of an xarray Dataset.

    This function checks if the first dimension of the dataset is named 'TIME' or 'time'.
    If not, it raises a ValueError.

    Parameters
    ----------
    ds : xr.Dataset
        The xarray Dataset to validate.

    Raises
    ------
    ValueError
        If the first dimension name is not 'TIME' or 'time'.

    """
    dim_name = list(ds.dims)[0]  # Should be 'N_MEASUREMENTS' for OG1
    if dim_name not in ["TIME", "time"]:
        raise ValueError(f"Dimension name '{dim_name}' is not 'TIME' or 'time'.")


def sanitize_variable_name(name: str) -> str:
    """Sanitize variable names to create valid Python identifiers.

    Replaces illegal Python identifier characters (spaces, parentheses, periods,
    hyphens, etc.) with underscores and collapses repeated underscores into single ones.

    Parameters
    ----------
    name : str
        The original variable name that may contain illegal characters

    Returns
    -------
    str
        A sanitized variable name that is a valid Python identifier

    Examples
    --------
    >>> sanitize_variable_name("Total MOC anomaly (relative to record-length average of 14.7 Sv)")
    'Total_MOC_anomaly__relative_to_record_length_average_of_14_7_Sv'
    >>> sanitize_variable_name("Upper-cell volume transport anomaly")
    'Upper_cell_volume_transport_anomaly'

    """
    # Replace any character that is not alphanumeric or underscore with underscore
    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", name)

    # Remove leading/trailing underscores
    sanitized = sanitized.strip("_")

    # Ensure it doesn't start with a number (prepend 'var_' if needed)
    if sanitized and sanitized[0].isdigit():
        sanitized = f"var_{sanitized}"

    # Handle edge case of empty string
    if not sanitized:
        sanitized = "unnamed_variable"

    return sanitized


def is_valid_url(url: str) -> bool:
    """Validate if a given string is a valid URL with supported schemes.

    Parameters
    ----------
    url : str
        The URL string to validate.

    Returns
    -------
    bool
        True if the URL is valid and uses a supported scheme ('http', 'https', 'ftp'),
        otherwise False.

    """
    try:
        result = urlparse(url)
        return all(
            [
                result.scheme in ("http", "https", "ftp"),
                result.netloc,
                result.path,  # Ensure there's a path, not necessarily its format
            ],
        )
    except (ValueError, TypeError, AttributeError):
        return False


def _is_valid_file(path: str) -> bool:
    """Check if the given path is a valid file and has a '.nc' extension.

    Parameters
    ----------
    path : str
        The file path to validate.

    Returns
    -------
    bool
        True if the path is a valid file and ends with '.nc', otherwise False.

    """
    return Path(path).is_file() and path.endswith(".nc")


def download_file(
    url: str,
    dest_folder: str,
    redownload: bool = False,
    filename: str = None,
) -> str:
    """Download a file from HTTP(S) or FTP to the specified destination folder.

    Parameters
    ----------
    url : str
        The URL of the file to download.
    dest_folder : str
        Local folder to save the downloaded file.
    redownload : bool, optional
        If True, force re-download of the file even if it exists.
    filename : str, optional
        Optional filename to save the file as. If not given, uses the name from the URL.

    Returns
    -------
    str
        The full path to the downloaded file.

    Raises
    ------
    ValueError
        If the URL scheme is unsupported.

    """
    dest_folder_path = Path(dest_folder)
    dest_folder_path.mkdir(parents=True, exist_ok=True)

    local_filename = dest_folder_path / (filename or Path(url).name)
    if local_filename.exists() and not redownload:
        # File exists and redownload not requested
        return str(local_filename)

    parsed_url = urlparse(url)

    if parsed_url.scheme in ("http", "https"):
        # HTTP(S) download
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

    elif parsed_url.scheme == "ftp":
        # FTP download
        with FTP(parsed_url.netloc) as ftp:
            ftp.login()  # anonymous login
            with open(local_filename, "wb") as f:
                ftp.retrbinary(f"RETR {parsed_url.path}", f.write)

    else:
        raise ValueError(f"Unsupported URL scheme in {url}")

    return str(local_filename)


def parse_ascii_header(
    file_path: str,
    comment_char: str = "%",
) -> Tuple[List[str], int]:
    """Parse the header of an ASCII file to extract column names and the number of header lines.

    Header lines are identified by the given comment character (default: '%').
    Columns are defined in lines like:
    '<comment_char> Column 1: <column_name>'.

    Parameters
    ----------
    file_path : str
        Path to the ASCII file.
    comment_char : str, optional
        Character used to identify header lines. Defaults to '%'.

    Returns
    -------
    tuple of (list of str, int)
        A tuple containing:
        - A list of column names extracted from the header.
        - The number of header lines to skip.

    """
    column_names: List[str] = []
    header_line_count: int = 0

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            header_line_count += 1
            if line.startswith(comment_char):
                if "Column" in line and ":" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        column_name = parts[1].strip()
                        column_names.append(column_name)
            else:
                # Stop when the first non-header line is found
                break

    return column_names, header_line_count


def read_ascii_file(file_path: str, comment_char: str = "#") -> pd.DataFrame:
    """Read an ASCII file into a pandas DataFrame, skipping lines starting with a specified comment character.

    Parameters
    ----------
    file_path : str
        Path to the ASCII file.
    comment_char : str, optional
        Character denoting comment lines. Defaults to '#'.

    Returns
    -------
    pd.DataFrame
        The loaded data as a pandas DataFrame.

    """
    return pd.read_csv(file_path, sep=r"\s+", comment=comment_char, on_bad_lines="skip")


def find_data_start(file_path: str) -> int:
    """Locate the first line of numerical data in a legacy ASCII file.

    This function scans an ASCII text file line by line and returns the
    zero-based line index of the first row that appears to contain data.
    A data row is identified as a non-empty line whose first non-whitespace
    character is a digit. This is useful for files with long, human-readable
    headers (titles, references, separators) preceding the actual data table.

    Parameters
    ----------
    file_path : str
        Path to the ASCII file to be scanned.

    Returns
    -------
    int
        Zero-based line index at which the numerical data table begins.

    Raises
    ------
    ValueError
        If no data-like lines are found in the file.

    """
    with open(file_path, encoding="latin-1") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if line and line[0].isdigit():
                return i
    raise ValueError("No data lines found")


# =============================================================================
# Unit Standardization System
# =============================================================================


def get_standard_unit_mappings() -> Dict[str, str]:
    """Get the comprehensive mapping of unit variations to standard units.

    Returns
    -------
    Dict[str, str]
        Dictionary mapping various unit forms to their standard equivalents.

    Notes
    -----
    This centralizes all unit standardization rules for consistency across
    the AMOCatlas package. Add new unit mappings here as needed.

    Examples
    --------
    >>> mappings = get_standard_unit_mappings()
    >>> print(mappings["Sv"])  # "Sverdrup"
    >>> print(mappings["deg C"])  # "degrees_celsius"

    """
    return {
        # Transport units
        "Sv": "Sverdrup",
        "sv": "Sverdrup",
        "Sverdrups": "Sverdrup",
        "1e6 m3 s-1": "Sverdrup",
        "1e6 m^3/s": "Sverdrup",
        # Temperature units
        "deg C": "degrees_Celsius",
        "degC": "degrees_Celsius",
        "°C": "degrees_Celsius",
        "celsius": "degrees_Celsius",
        "degrees C": "degrees_Celsius",
        "C": "degrees_Celsius",
        "deg_C": "degrees_Celsius",
        "degree_C": "degrees_Celsius",
        "degree_celsius": "degrees_Celsius",
        "degrees_celsius": "degrees_Celsius",
        "degrees Celsius": "degrees_Celsius",
        # Salinity units
        "psu": "PSU",  # Practical Salinity Units are dimensionless
        "PSU": "PSU",
        "pss": "PSU",  # Practical Salinity Scale
        "PSS": "PSU",
        "g/kg": "g kg-1",  # Convert to CF-compliant form
        "g kg^-1": "g kg-1",
        # Pressure units
        "decibar": "dbar",
        "db": "dbar",
        "mbar": "millibar",
        "mb": "millibar",
        "hPa": "hectopascal",
        # Distance/Length units
        "m": "meters",
        "meters": "meters",
        "metres": "meters",
        "km": "kilometers",
        "kilometers": "kilometers",
        "kilometres": "kilometers",
        # Time units
        "sec": "second",
        "seconds": "second",
        "s": "second",
        "min": "minute",
        "minutes": "minute",
        "hr": "hour",
        "hours": "hour",
        "h": "hour",
        "day": "day",
        "days": "day",
        "d": "day",
        # Speed/Velocity units
        "m/s": "m s-1",
        "m s^-1": "m s-1",
        "cm/s": "cm s-1",
        "cm s^-1": "cm s-1",
        "mm/s": "mm s-1",
        "mm s^-1": "mm s-1",
        # Angular units
        "deg": "degree",
        "degrees": "degree",
        "°": "degree",
        "rad": "radian",
        "radians": "radian",
        # Geographic units
        "deg N": "degrees_north",
        "deg_N": "degrees_north",
        "degree_N": "degrees_north",
        "degree_north": "degrees_north",
        "degN": "degrees_north",
        "°N": "degrees_north",
        "deg E": "degrees_east",
        "deg_E": "degrees_east",
        "degree_E": "degrees_east",
        "degree_east": "degrees_east",
        "degE": "degrees_east",
        "°E": "degrees_east",
        "deg W": "degrees_west",
        "deg_W": "degrees_west",
        "degree_W": "degrees_west",
        "degree_west": "degrees_west",
        "degW": "degrees_west",
        "°W": "degrees_west",
        "deg S": "degrees_south",
        "deg_S": "degrees_south",
        "degree_S": "degrees_south",
        "degree_south": "degrees_south",
        "degS": "degrees_south",
        "°S": "degrees_south",
        # Density units
        "kg/m3": "kg m-3",
        "kg m^-3": "kg m-3",
        "g/cm3": "g cm-3",
        "g cm^-3": "g cm-3",
        # Frequency units
        "Hz": "hertz",
        "hz": "hertz",
        "1/s": "s-1",
        "s^-1": "s-1",
        # Dimensionless units (explicitly unitless)
        "unitless": "1",
        "dimensionless": "1",
        # No units specified (placeholders)
        "": "",  # Empty string (placeholder for unspecified units)
        "n/a": "",
        "N/A": "",
        "none": "",
        "-": "",
    }


def standardize_dataset_units(
    ds: xr.Dataset, mapping: Optional[Dict[str, str]] = None, log_changes: bool = True
) -> xr.Dataset:
    """Standardize units throughout a dataset using comprehensive mapping rules.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize units for.
    mapping : Dict[str, str], optional
        Custom unit mapping. If None, uses get_standard_unit_mappings().
    log_changes : bool, optional
        Whether to log unit changes. Default is True.

    Returns
    -------
    xr.Dataset
        Dataset with standardized units.

    Notes
    -----
    This function applies unit standardization to all variables and coordinates
    in the dataset. It's designed to be the central unit standardization
    function for AMOCatlas, replacing the simpler standardize_units function.

    Examples
    --------
    >>> ds_std = standardize_dataset_units(ds)
    >>> # Check if Sv was converted to Sverdrup
    >>> print(ds_std['transport'].attrs['units'])  # "Sverdrup"

    """
    from .logger import log_info, log_debug

    if mapping is None:
        mapping = get_standard_unit_mappings()

    units_changed = 0

    # Process data variables
    for var_name in ds.data_vars:
        current_units = ds[var_name].attrs.get("units", "")
        if log_changes:
            log_debug(f"Variable {var_name}: current units = '{current_units}'")

        if current_units in mapping:
            new_units = mapping[current_units]
            ds[var_name].attrs["units"] = new_units
            if log_changes:
                log_info(
                    f"Standardized units for variable {var_name}: '{current_units}' → '{new_units}'"
                )
            units_changed += 1
        elif current_units == "":
            if log_changes:
                log_debug(f"Variable {var_name}: no units attribute found")
        else:
            if log_changes:
                log_debug(
                    f"Variable {var_name}: units '{current_units}' - no standardization needed"
                )

    # Process coordinate variables
    for coord_name in ds.coords:
        current_units = ds[coord_name].attrs.get("units", "")
        if log_changes:
            log_debug(f"Coordinate {coord_name}: current units = '{current_units}'")

        if current_units in mapping:
            new_units = mapping[current_units]
            ds[coord_name].attrs["units"] = new_units
            if log_changes:
                log_info(
                    f"Standardized units for coordinate {coord_name}: '{current_units}' → '{new_units}'"
                )
            units_changed += 1
        elif current_units == "":
            if log_changes:
                log_debug(f"Coordinate {coord_name}: no units attribute found")
        else:
            if log_changes:
                log_debug(
                    f"Coordinate {coord_name}: units '{current_units}' - no standardization needed"
                )

    # Final cleanup: Remove empty units attributes (unspecified units)
    empty_units_removed = 0

    # Remove empty units from data variables
    for var_name in ds.data_vars:
        if ds[var_name].attrs.get("units") == "":
            del ds[var_name].attrs["units"]
            empty_units_removed += 1
            if log_changes:
                log_debug(f"Removed empty units attribute from variable {var_name}")

    # Remove empty units from coordinates
    for coord_name in ds.coords:
        if ds[coord_name].attrs.get("units") == "":
            del ds[coord_name].attrs["units"]
            empty_units_removed += 1
            if log_changes:
                log_debug(f"Removed empty units attribute from coordinate {coord_name}")

    if log_changes:
        log_info(
            f"Unit standardization complete: {units_changed} variables/coordinates updated, "
            f"{empty_units_removed} empty units attributes removed"
        )

    return ds


def apply_unit_standardization_after_metadata(ds: xr.Dataset) -> xr.Dataset:
    """Apply unit standardization with high priority to override YAML metadata.

    This function is designed to be called after metadata enrichment to ensure
    that standardized units take precedence over any units specified in YAML
    metadata files.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset that may have had units overwritten by metadata processing.

    Returns
    -------
    xr.Dataset
        Dataset with units re-standardized.

    Notes
    -----
    This addresses the issue where YAML metadata files contain "Sv" units
    that override the standardized "Sverdrup" units. This function should
    be called as the final step in standardization.

    Examples
    --------
    >>> # In standardization pipeline
    >>> ds = apply_metadata_from_yaml(ds)  # This might set units: Sv
    >>> ds = apply_unit_standardization_after_metadata(ds)  # This fixes it

    """
    from .logger import log_info

    log_info("Applying final unit standardization to override any metadata conflicts")
    return standardize_dataset_units(ds, log_changes=True)


def mask_invalid_values(ds: xr.Dataset) -> xr.Dataset:
    """Mask values outside valid_min/valid_max ranges as NaN.

    Many netCDF files contain valid_min and valid_max attributes that define
    the valid range for variables. Values outside this range should be treated
    as missing data but are often not automatically masked by xarray.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to check for invalid values.

    Returns
    -------
    xr.Dataset
        Dataset with values outside valid ranges masked as NaN.

    Examples
    --------
    >>> # Variable has valid_min=-100, valid_max=100 but contains 9.97e+36
    >>> ds_clean = mask_invalid_values(ds)
    >>> # Now extreme values are masked as NaN

    """
    from .logger import log_info, log_debug

    variables_masked = 0
    total_values_masked = 0

    # Process all variables (data variables and coordinates)
    for var_name in ds.variables:
        var = ds[var_name]

        # Check if variable has valid range attributes
        valid_min = var.attrs.get("valid_min")
        valid_max = var.attrs.get("valid_max")

        if valid_min is not None or valid_max is not None:
            # Use xarray operations to preserve lazy evaluation
            invalid_mask = xr.zeros_like(var, dtype=bool)

            if valid_min is not None:
                invalid_mask = invalid_mask | (var < valid_min)

            if valid_max is not None:
                invalid_mask = invalid_mask | (var > valid_max)

            # Count invalid values (this will materialize the mask but not the full data)
            invalid_count = invalid_mask.sum().values

            if invalid_count > 0:
                log_info(
                    f"Masking {invalid_count} invalid values in '{var_name}' "
                    f"(valid range: {valid_min} to {valid_max})"
                )
                log_debug(
                    f"  Original min/max: {var.min().values:.2e} / {var.max().values:.2e}"
                )

                # Apply mask using xarray where operation to preserve lazy evaluation
                masked_var = var.where(~invalid_mask)

                # Update the variable data
                ds[var_name] = masked_var

                log_debug(
                    f"  Masked min/max: {masked_var.min().values:.2e} / {masked_var.max().values:.2e}"
                )

                variables_masked += 1
                total_values_masked += invalid_count
            else:
                log_debug(
                    f"Variable '{var_name}' has valid range but no invalid values"
                )

    if variables_masked > 0:
        log_info(
            f"Masked invalid values in {variables_masked} variables "
            f"({total_values_masked} total values)"
        )

    return ds
