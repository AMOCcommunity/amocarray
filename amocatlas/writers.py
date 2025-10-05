from numbers import Number
from pathlib import Path
from typing import Union

import numpy as np
import xarray as xr

from amocatlas import logger


def save_dataset(ds: xr.Dataset, output_file: str = "../test.nc") -> bool:
    """Attempts to save the dataset to a NetCDF file. If a TypeError occurs due to invalid attribute values,
    it converts the invalid attributes to strings and retries the save operation.

    Parameters
    ----------
    ds : xarray.Dataset
        The dataset to be saved.
    output_file : str, optional
        The path to the output NetCDF file. Defaults to '../test.nc'.

    Returns
    -------
    bool
        True if the dataset was saved successfully, False otherwise.

    Notes
    -----
    This function is based on a workaround for issues with saving datasets containing
    attributes of unsupported types. See: https://github.com/pydata/xarray/issues/3743

    """
    valid_types: tuple[Union[type, tuple], ...] = (
        str,
        int,
        float,
        np.float32,
        np.float64,
        np.int32,
        np.int64,
    )
    # More general
    valid_types = (str, Number, np.ndarray, np.number, list, tuple)

    # Make a copy to avoid modifying the original dataset
    ds_copy = ds.copy()

    # Sanitize attributes: replace None with empty string to avoid NetCDF issues
    for k, v in ds_copy.attrs.items():
        if v is None:
            ds_copy.attrs[k] = ""

    # Handle datetime coordinate encoding conflicts
    # For datetime variables, remove manual units to let xarray handle encoding properly
    conflicting_keys = ["units", "calendar"]
    for var_name, variable in ds_copy.variables.items():
        if variable.dtype == np.dtype("datetime64[ns]"):
            logger.log_info(
                f"Configuring datetime encoding for variable '{var_name}' - removing manual units"
            )

            # Remove conflicting attributes that may clash with encoding
            for key in conflicting_keys:
                if key in ds_copy[var_name].attrs:
                    del ds_copy[var_name].attrs[key]

            # Set proper datetime encoding
            if var_name not in ds_copy.encoding:
                ds_copy.encoding[var_name] = {}
            ds_copy.encoding[var_name].update(
                {"units": "seconds since 1970-01-01T00:00:00Z", "calendar": "gregorian"}
            )

    # Set up compression encoding for data variables
    encoding = {}
    for var in ds_copy.data_vars:
        encoding[var] = {"zlib": True, "complevel": 4}

    try:
        ds_copy.to_netcdf(output_file, format="NETCDF4_CLASSIC", encoding=encoding)
        return True
    except TypeError as e:
        print(e.__class__.__name__, e)
        for varname, variable in ds_copy.variables.items():
            for k, v in variable.attrs.items():
                if not isinstance(v, valid_types) or isinstance(v, bool):
                    print(
                        f"variable '{varname}': Converting attribute '{k}' with value '{v}' to string.",
                    )
                    variable.attrs[k] = str(v)
        try:
            ds_copy.to_netcdf(output_file, format="NETCDF4_CLASSIC", encoding=encoding)
            return True
        except Exception as e:
            print("Failed to save dataset:", e)
            datetime_vars = [
                var
                for var in ds_copy.variables
                if ds_copy[var].dtype == "datetime64[ns]"
            ]
            print("Variables with dtype datetime64[ns]:", datetime_vars)
            float_attrs = [
                attr for attr in ds_copy.attrs if isinstance(ds_copy.attrs[attr], float)
            ]
            print("Attributes with dtype float64:", float_attrs)
            return False


def save_AC1_dataset(ds: xr.Dataset, data_dir: Union[str, Path]) -> Path:
    """
    Save AC1 dataset to netCDF using the OceanSITES 'id' attribute.

    Parameters
    ----------
    ds : xarray.Dataset
        Dataset with AC1-compliant global attributes including 'id'.
    data_dir : str or pathlib.Path
        Directory to save the netCDF file.

    Returns
    -------
    Path
        Full path to the saved NetCDF file.

    Raises
    ------
    ValueError
        If 'id' global attribute is not found.
    """
    if "id" not in ds.attrs:
        raise ValueError(
            "Global attribute 'id' not found. Cannot determine output filename."
        )

    data_dir = Path(data_dir)
    filename = f"{ds.attrs['id']}.nc"
    filepath = data_dir / filename

    # Use the main save_dataset function which handles all the encoding issues
    success = save_dataset(ds, str(filepath))

    if not success:
        raise RuntimeError(f"Failed to save AC1 dataset to {filepath}")

    return filepath
