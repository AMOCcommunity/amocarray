"""AMOCatlas plotting functions for visualization and publication figures."""

import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import numpy as np
from pandas import DataFrame
from pandas.io.formats.style import Styler


# ------------------------------------------------------------------------------------
# Views of the ds or nc file
# ------------------------------------------------------------------------------------
def show_contents(
    data: str | xr.Dataset,
    content_type: str = "variables",
) -> Styler | pd.DataFrame:
    """Wrapper function to show contents of an xarray Dataset or a netCDF file.

    Parameters
    ----------
    data : str or xr.Dataset
        The input data, either a file path to a netCDF file or an xarray Dataset.
    content_type : str, optional
        The type of content to show, either 'variables' (or 'vars') or 'attributes' (or 'attrs').
        Default is 'variables'.

    Returns
    -------
    pandas.io.formats.style.Styler or pandas.DataFrame
        A styled DataFrame with details about the variables or attributes.

    Raises
    ------
    TypeError
        If the input data is not a file path (str) or an xarray Dataset.
    ValueError
        If the content_type is not 'variables' (or 'vars') or 'attributes' (or 'attrs').

    """
    if content_type in ["variables", "vars"]:
        if isinstance(data, (str, xr.Dataset)):
            return show_variables(data)
        else:
            raise TypeError("Input data must be a file path (str) or an xarray Dataset")
    elif content_type in ["attributes", "attrs"]:
        if isinstance(data, (str, xr.Dataset)):
            return show_attributes(data)
        else:
            raise TypeError(
                "Attributes can only be shown for netCDF files (str) or xarray Datasets",
            )
    else:
        raise ValueError(
            "content_type must be either 'variables' (or 'vars') or 'attributes' (or 'attrs')",
        )


def show_variables(data: str | xr.Dataset) -> Styler:
    """Processes an xarray Dataset or a netCDF file, extracts variable information,
    and returns a styled DataFrame with details about the variables.

    Parameters
    ----------
    data : str or xr.Dataset
        The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns
    -------
    pd.io.formats.style.Styler
        A styled DataFrame containing the following columns:
        - dims: The dimension of the variable (or "string" if it is a string type).
        - name: The name of the variable.
        - units: The units of the variable (if available).
        - comment: Any additional comments about the variable (if available).
        - standard_name: The standard name of the variable (if available).
        - dtype: The data type of the variable.

    Raises
    ------
    TypeError
        If the input data is not a file path (str) or an xarray Dataset.

    """
    from netCDF4 import Dataset
    from pandas import DataFrame

    if isinstance(data, str):
        print(f"information is based on file: {data}")
        dataset = Dataset(data)
        variables = dataset.variables
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        variables = data.variables
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(variables):
        var = variables[key]
        if isinstance(data, str):
            dims = var.dimensions[0] if len(var.dimensions) == 1 else "string"
            units = "" if not hasattr(var, "units") else var.units
            comment = "" if not hasattr(var, "comment") else var.comment
        else:
            dims = var.dims[0] if len(var.dims) == 1 else "string"
            units = var.attrs.get("units", "")
            comment = var.attrs.get("comment", "")

        info[i] = {
            "name": key,
            "dims": dims,
            "units": units,
            "comment": comment,
            "standard_name": var.attrs.get("standard_name", ""),
            "dtype": str(var.dtype) if isinstance(data, str) else str(var.data.dtype),
        }

    vars = DataFrame(info).T

    dim = vars.dims
    dim[dim.str.startswith("str")] = "string"
    vars["dims"] = dim

    vars = (
        vars.sort_values(["dims", "name"])
        .reset_index(drop=True)
        .loc[:, ["dims", "name", "units", "comment", "standard_name", "dtype"]]
        .set_index("name")
        .style
    )

    return vars


def show_attributes(data: str | xr.Dataset) -> pd.DataFrame:
    """Processes an xarray Dataset or a netCDF file, extracts attribute information,
    and returns a DataFrame with details about the attributes.

    Parameters
    ----------
    data : str or xr.Dataset
        The input data, either a file path to a netCDF file or an xarray Dataset.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the following columns:
        - Attribute: The name of the attribute.
        - Value: The value of the attribute.
        - DType: The data type of the attribute.

    Raises
    ------
    TypeError
        If the input data is not a file path (str) or an xarray Dataset.

    """
    from netCDF4 import Dataset
    from pandas import DataFrame

    if isinstance(data, str):
        print(f"information is based on file: {data}")
        rootgrp = Dataset(data, "r", format="NETCDF4")
        attributes = rootgrp.ncattrs()
        get_attr = lambda key: getattr(rootgrp, key)
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        attributes = data.attrs.keys()
        get_attr = lambda key: data.attrs[key]
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(attributes):
        dtype = type(get_attr(key)).__name__
        info[i] = {"Attribute": key, "Value": get_attr(key), "DType": dtype}

    attrs = DataFrame(info).T

    return attrs


def show_variables_by_dimension(
    data: str | xr.Dataset,
    dimension_name: str = "trajectory",
) -> Styler:
    """Extracts variable information from an xarray Dataset or a netCDF file and returns a styled DataFrame
    with details about the variables filtered by a specific dimension.

    Parameters
    ----------
    data : str or xr.Dataset
        The input data, either a file path to a netCDF file or an xarray Dataset.
    dimension_name : str, optional
        The name of the dimension to filter variables by, by default "trajectory".

    Returns
    -------
    pandas.io.formats.style.Styler
        A styled DataFrame containing the following columns:
        - dims: The dimension of the variable (or "string" if it is a string type).
        - name: The name of the variable.
        - units: The units of the variable (if available).
        - comment: Any additional comments about the variable (if available).

    Raises
    ------
    TypeError
        If the input data is not a file path (str) or an xarray Dataset.

    """
    if isinstance(data, str):
        print(f"information is based on file: {data}")
        dataset = xr.open_dataset(data)
        variables = dataset.variables
    elif isinstance(data, xr.Dataset):
        print("information is based on xarray Dataset")
        variables = data.variables
    else:
        raise TypeError("Input data must be a file path (str) or an xarray Dataset")

    info = {}
    for i, key in enumerate(variables):
        var = variables[key]
        if isinstance(data, str):
            dims = var.dimensions[0] if len(var.dimensions) == 1 else "string"
            units = "" if not hasattr(var, "units") else var.units
            comment = "" if not hasattr(var, "comment") else var.comment
        else:
            dims = var.dims[0] if len(var.dims) == 1 else "string"
            units = var.attrs.get("units", "")
            comment = var.attrs.get("comment", "")

        if dims == dimension_name:
            info[i] = {
                "name": key,
                "dims": dims,
                "units": units,
                "comment": comment,
            }

    vars = DataFrame(info).T

    dim = vars.dims
    dim[dim.str.startswith("str")] = "string"
    vars["dims"] = dim

    vars = (
        vars.sort_values(["dims", "name"])
        .reset_index(drop=True)
        .loc[:, ["dims", "name", "units", "comment"]]
        .set_index("name")
        .style
    )

    return vars


def monthly_resample(da: xr.DataArray) -> xr.DataArray:
    """Resample to monthly mean if data is not already monthly."""
    time_key = [c for c in da.coords if c.lower() == "time"]
    if not time_key:
        raise ValueError("No time coordinate found.")
    time_key = time_key[0]

    # Extract time values and check spacing
    time_values = da[time_key].values
    dt_days = np.nanmean(np.diff(time_values) / np.timedelta64(1, "D"))
    if 20 <= dt_days <= 40:
        return da  # Already monthly

    # Drop NaT timestamps
    mask_valid_time = ~np.isnat(time_values)
    da = da.isel({time_key: mask_valid_time})

    # Drop duplicate timestamps (keep first)
    _, unique_indices = np.unique(da[time_key].values, return_index=True)
    da = da.isel({time_key: np.sort(unique_indices)})

    # Ensure strictly increasing time
    da = da.sortby(time_key)

    # Now resample
    return da.resample({time_key: "1MS"}).mean()


def plot_amoc_timeseries(
    data,
    varnames=None,
    labels=None,
    colors=None,
    title="AMOC Time Series",
    ylabel=None,
    time_limits=None,
    ylim=None,
    figsize=(10, 3),
    resample_monthly=True,
    plot_raw=True,
):
    """Plot original and optionally monthly-averaged AMOC time series for one or more datasets.

    Parameters
    ----------
    data : list of xarray.Dataset or xarray.DataArray
        List of datasets or DataArrays to plot.
    varnames : list of str, optional
        List of variable names to extract from each dataset. Not needed if DataArrays are passed.
    labels : list of str, optional
        Labels for the legend.
    colors : list of str, optional
        Colors for monthly-averaged plots.
    title : str
        Title of the plot.
    ylabel : str, optional
        Label for the y-axis. If None, inferred from attributes.
    time_limits : tuple of str or pd.Timestamp, optional
        X-axis time limits (start, end).
    ylim : tuple of float, optional
        Y-axis limits (min, max).
    figsize : tuple
        Size of the figure.
    resample_monthly : bool
        If True, monthly averages are computed and plotted.
    plot_raw : bool
        If True, raw data is plotted.

    """
    if not isinstance(data, list):
        data = [data]

    if varnames is None:
        varnames = [None] * len(data)
    if labels is None:
        labels = [f"Dataset {i+1}" for i in range(len(data))]
    if colors is None:
        colors = ["red", "darkblue", "green", "purple", "orange"]

    fig, ax = plt.subplots(figsize=figsize)

    for i, item in enumerate(data):
        label = labels[i]
        color = colors[i % len(colors)]
        var = varnames[i]

        # Extract DataArray
        if isinstance(item, xr.Dataset):
            da = item[var]
        else:
            da = item

        # Get time coordinate (case sensitive)
        for coord in da.coords:
            if coord.lower() == "time":
                time_key = coord
                break
        else:
            raise ValueError("No time coordinate found in dataset.")

        # Plot original
        if plot_raw:
            ax.plot(
                da[time_key],
                da,
                color="grey",
                alpha=0.5,
                linewidth=0.5,
                label=f"{label} (raw)" if label else "Original",
            )

        # Plot monthly average if requested
        if resample_monthly:

            da_monthly = monthly_resample(da)

            ax.plot(
                da_monthly[time_key],
                da_monthly,
                color=color,
                linewidth=1.5,
                label=f"{label} Monthly Avg",
            )

        # Attempt to extract ylabel from metadata if not provided
        if ylabel is None and "standard_name" in da.attrs and "units" in da.attrs:
            ylabel = f"{da.attrs['standard_name']} [{da.attrs['units']}]"

    # Horizontal zero line
    ax.axhline(0, color="black", linestyle="--", linewidth=0.5)

    # Styling
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel(ylabel if ylabel else "Transport [Sv]")
    ax.legend(loc="best")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Limits
    if time_limits:
        ax.set_xlim(pd.Timestamp(time_limits[0]), pd.Timestamp(time_limits[1]))
    if ylim:
        ax.set_ylim(ylim)

    plt.tight_layout()
    return fig, ax


def plot_monthly_anomalies(**kwargs) -> tuple[plt.Figure, list[plt.Axes]]:
    """Plot the monthly anomalies for various datasets.
    Pass keyword arguments in the form: `label_name_data`, `label_name_label`.
    For example:
        osnap_data = standardOSNAP[0]["MOC_all"], osnap_label = "OSNAP"
        ...
    """
    color_cycle = [
        "blue",
        "red",
        "green",
        "purple",
        "orange",
        "darkblue",
        "darkred",
        "darkgreen",
    ]

    # Extract and sort data/labels by name to ensure consistent ordering
    names = ["dso", "osnap", "fortyone", "rapid", "fw2015", "move", "samba"]
    datasets = [monthly_resample(kwargs[f"{name}_data"]) for name in names]
    labels = [kwargs[f"{name}_label"] for name in names]

    fig, axes = plt.subplots(len(datasets), 1, figsize=(10, 16), sharex=True)

    for i, (data, label, color) in enumerate(zip(datasets, labels, color_cycle)):
        time = data["TIME"]
        axes[i].plot(time, data, color=color, label=label)
        axes[i].axhline(0, color="black", linestyle="--", linewidth=0.5)
        axes[i].set_title(label)
        axes[i].set_ylabel("Transport [Sv]")
        axes[i].legend()
        axes[i].grid(True, linestyle="--", alpha=0.5)

        # Dynamic ylim
        ymin = float(data.min()) - 1
        ymax = float(data.max()) + 1
        axes[i].set_ylim([ymin, ymax])

        # Style choices
        axes[i].spines["top"].set_visible(False)
        axes[i].spines["right"].set_visible(False)
        axes[i].set_xlim([pd.Timestamp("2000-01-01"), pd.Timestamp("2023-12-31")])
        axes[i].set_clip_on(False)

    axes[-1].set_xlabel("Time")
    plt.tight_layout()
    return fig, axes


# ------------------------------------------------------------------------------------
# PyGMT Publication Plotting Functions
# ------------------------------------------------------------------------------------

# Check for PyGMT availability
try:
    import pygmt

    HAS_PYGMT = True
except Exception:
    # Catch ImportError and any GMT library loading errors (GMTCLibNotFoundError, etc.)
    HAS_PYGMT = False


def _check_pygmt():
    """Check if PyGMT is available and raise informative error if not."""
    if not HAS_PYGMT:
        raise ImportError(
            "PyGMT is required for publication-quality plots. "
            "Install with: pip install pygmt\n"
            "Note: PyGMT requires GMT to be installed separately. "
            "See https://www.pygmt.org/latest/install.html for details."
        )


def _add_amocatlas_timestamp(fig):
    """Add standardized AMOCatlas timestamp to PyGMT figure.

    Parameters
    ----------
    fig : pygmt.Figure
        PyGMT figure to add timestamp to.

    """
    fig.timestamp(
        label="AMOCatlas", font="10p,Helvetica,gray30", timefmt="%Y-%m-%dT%H:%M"
    )


def plot_moc_timeseries_pygmt(
    df: pd.DataFrame, column: str = "moc", label: str = "MOC [Sv]"
):
    """Plot MOC time series using PyGMT with publication-quality styling.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with 'time_num' (decimal years) and data columns.
    column : str, default "moc"
        Name of the column to plot.
    label : str, default "MOC [Sv]"
        Y-axis label for the plot.

    Returns
    -------
    pygmt.Figure
        PyGMT figure object.

    Raises
    ------
    ImportError
        If PyGMT is not installed.

    """
    _check_pygmt()

    fig = pygmt.Figure()

    pygmt.config(
        FONT_ANNOT_PRIMARY="20p",  # tick labels
        FONT_LABEL="20p",  # axis labels
        FONT_TITLE="20p",  # title (if used)
        MAP_TICK_LENGTH_PRIMARY="6p",  # major ticks longer
        MAP_TICK_PEN_PRIMARY="1.2p",  # major ticks thicker
        MAP_LABEL_OFFSET="10p",  # spacing axis ↔ label
        MAP_TICK_LENGTH_SECONDARY="3p",  # minor ticks longer
        MAP_TICK_PEN_SECONDARY="0.8p",  # minor ticks thicker
        MAP_GRID_PEN="0.25p,gray70,10_5",  # fine dashed grid
    )

    # --- Define plotting region ---
    col_filtered = f"{column}_filtered"
    xmax = max(df["time_num"].max(), 2025)
    if col_filtered not in df.columns:
        df[col_filtered] = df[column]
    ymin = df[[column, col_filtered]].min().min()
    ymax = df[[column, col_filtered]].max().max()
    region = [df["time_num"].min(), xmax, ymin, ymax]

    # --- Basemap ---
    fig.basemap(
        region=region, projection="X25c/7c", frame=["xaf", f"yafg10f5+l{label}", "WS"]
    )

    # --- Plot original series ---
    fig.plot(x=df["time_num"], y=df[column], pen=".75p,red", label="Original")

    # --- Plot filtered: thick white background + black foreground ---
    fig.plot(x=df["time_num"], y=df[col_filtered], pen="3.5p,white")
    fig.plot(
        x=df["time_num"], y=df[col_filtered], pen="2.5p,black", label="Filtered (Tukey)"
    )

    # Add AMOCatlas timestamp
    _add_amocatlas_timestamp(fig)

    return fig


def plot_osnap_components_pygmt(df: pd.DataFrame):
    """Plot OSNAP MOC components with shaded error bands using PyGMT.

    Parameters
    ----------
    df : pandas.DataFrame
        Must contain:
        - time_num (decimal years)
        - MOC_ALL, MOC_EAST, MOC_WEST
        - MOC_EAST_ERR, MOC_WEST_ERR

    Returns
    -------
    pygmt.Figure
        PyGMT figure object.

    Raises
    ------
    ImportError
        If PyGMT is not installed.

    """
    _check_pygmt()

    fig = pygmt.Figure()

    # Styling
    pygmt.config(
        FONT_ANNOT_PRIMARY="20p",
        FONT_LABEL="20p",
        FONT_TITLE="20p",
        MAP_TICK_LENGTH_PRIMARY="6p",
        MAP_TICK_PEN_PRIMARY="1.2p",
        MAP_LABEL_OFFSET="10p",
        MAP_TICK_LENGTH_SECONDARY="3p",
        MAP_TICK_PEN_SECONDARY="0.8p",
        MAP_GRID_PEN="0.25p,gray70,10_5",
    )

    # Region
    xmax = max(df["time_num"].max(), 2022)
    ymin = df[["MOC_ALL", "MOC_EAST", "MOC_WEST"]].min().min() - 1
    ymax = df[["MOC_ALL", "MOC_EAST", "MOC_WEST"]].max().max() + 1
    ymin = min(ymin, -5)
    ymax = max(ymax, 30)
    region = [df["time_num"].min(), xmax, ymin, ymax]

    # Basemap
    fig.basemap(
        region=region, projection="X15c/7c", frame=["xaf", "yafg5f2+lMOC [Sv]", "WS"]
    )

    # --- Shaded error for EAST ---
    east_upper = df["MOC_EAST"] + df["MOC_EAST_ERR"]
    east_lower = df["MOC_EAST"] - df["MOC_EAST_ERR"]

    # Build filled polygon for EAST
    import numpy as np

    x_east = np.concatenate([df["time_num"], df["time_num"][::-1]])
    y_east = np.concatenate([east_upper, east_lower[::-1]])
    fig.plot(x=x_east, y=y_east, fill="orange", transparency=70, close=True)

    # --- Shaded error for WEST ---
    west_upper = df["MOC_WEST"] + df["MOC_WEST_ERR"]
    west_lower = df["MOC_WEST"] - df["MOC_WEST_ERR"]
    x_west = np.concatenate([df["time_num"], df["time_num"][::-1]])
    y_west = np.concatenate([west_upper, west_lower[::-1]])
    fig.plot(x=x_west, y=y_west, fill="blue", transparency=70, close=True)

    # --- Main curves ---
    fig.plot(x=df["time_num"], y=df["MOC_ALL"], pen="2.5p,black", label="Total")
    fig.plot(
        x=df["time_num"],
        y=df["MOC_EAST"],
        pen="2.5p,orange",
        label="East",
        transparency=20,
    )
    fig.plot(x=df["time_num"], y=df["MOC_WEST"], pen="2.5p,blue", label="West")

    # Legend
    fig.legend(position="JMR+jMR+o-1.5i/0i", box=True)

    # Add AMOCatlas timestamp
    _add_amocatlas_timestamp(fig)

    return fig


def plot_rapid_components_pygmt(df: pd.DataFrame):
    """Plot RAPID MOC and component transports using PyGMT.

    Parameters
    ----------
    df : pandas.DataFrame
        Must include:
        - 'time_num'
        - 'moc_mar_hc10' (total MOC)
        - 't_gs10' (Florida Current)
        - 't_ek10' (Ekman)
        - 't_umo10' (upper mid-ocean)

    Returns
    -------
    pygmt.Figure
        PyGMT figure object.

    Raises
    ------
    ImportError
        If PyGMT is not installed.

    """
    _check_pygmt()

    fig = pygmt.Figure()

    pygmt.config(
        FONT_ANNOT_PRIMARY="20p",
        FONT_LABEL="20p",
        FONT_TITLE="20p",
        MAP_TICK_LENGTH_PRIMARY="6p",
        MAP_TICK_PEN_PRIMARY="1.2p",
        MAP_LABEL_OFFSET="10p",
        MAP_TICK_LENGTH_SECONDARY="3p",
        MAP_TICK_PEN_SECONDARY="0.8p",
        MAP_GRID_PEN="0.25p,gray70,10_5",
    )

    # Set region based on full value range
    xmax = max(df["time_num"].max(), 2025)
    components = ["moc_mar_hc10", "t_gs10", "t_ek10", "t_umo10"]
    ymin = df[components].min().min() - 1
    ymax = df[components].max().max() + 1
    region = [df["time_num"].min(), xmax, ymin, ymax]

    # Basemap
    fig.basemap(
        region=region,
        projection="X25c/15c",
        frame=["xaf", "yafg5f2+lTransport [Sv]", "WS+tRAPID MOC Components"],
    )

    # Plot each component with custom colors
    fig.plot(x=df["time_num"], y=df["moc_mar_hc10"], pen="1.5p,red", label="MOC")
    fig.plot(x=df["time_num"], y=df["t_gs10"], pen="1.5p,blue", label="Florida Current")
    fig.plot(x=df["time_num"], y=df["t_ek10"], pen="1.5p,black", label="Ekman")
    fig.plot(
        x=df["time_num"], y=df["t_umo10"], pen="1.5p,magenta", label="Upper Mid-Ocean"
    )

    # Plot labels at end of time series with slight offset

    # Use the actual end date of the time series
    x_label = df["time_num"].max()

    y_labels = {
        "MOC": df["moc_mar_hc10"].mean(),
        "Florida Current": df["t_gs10"].mean(),
        "Ekman": df["t_ek10"].mean(),
        "Upper Mid-Ocean": df["t_umo10"].mean(),
    }
    colors = {
        "MOC": "red",
        "Florida Current": "blue",
        "Ekman": "black",
        "Upper Mid-Ocean": "magenta",
    }
    for label, y in y_labels.items():
        fig.text(
            x=x_label,
            y=y,
            text=label,
            font=f"18p,Helvetica,{colors[label]}",
            justify="LM",
            no_clip=True,
            offset="0.1i/0i",  # Offset 0.1 inches to the right
        )

    # Add AMOCatlas timestamp
    _add_amocatlas_timestamp(fig)

    return fig


def plot_all_moc_pygmt(osnap_df, rapid_df, move_df, samba_df, filtered: bool = False):
    """Plot all MOC time series (OSNAP, RAPID, MOVE, SAMBA) in a stacked PyGMT figure.

    Parameters
    ----------
    osnap_df : pandas.DataFrame
        OSNAP MOC data with 'time_num' and 'moc'/'moc_filtered'.
    rapid_df : pandas.DataFrame
        RAPID MOC data with 'time_num' and 'moc'/'moc_filtered'.
    move_df : pandas.DataFrame
        MOVE MOC data with 'time_num' and 'moc'/'moc_filtered'.
    samba_df : pandas.DataFrame
        SAMBA MOC data with 'time_num' and 'moc'/'moc_filtered'.
    filtered : bool, default False
        Whether to plot filtered data (True) or original data (False).

    Returns
    -------
    pygmt.Figure
        PyGMT figure object.

    Raises
    ------
    ImportError
        If PyGMT is not installed.

    """
    _check_pygmt()

    magenta1 = "231/41/138"
    red1 = "227/26/28"
    blue1 = "8/104/172"
    green1 = "35/139/69"

    # Select column based on filtered flag
    col = "moc_filtered" if filtered else "moc"

    # Prepare data and labels
    dfs = [
        (osnap_df, "MOC [Sv]", (5, 25), 5, "OSNAP", green1, "W"),
        (rapid_df, "MOC [Sv]", (5, 30), 6, "RAPID 26°N", red1, "E"),
        (move_df, "MOC [Sv]", (5, 30), 6, "MOVE 16°N", magenta1, "W"),
        (samba_df, "Anomaly [Sv]", (-10, 15), 6, "SAMBA 34.5°S", blue1, "ES"),
    ]

    # Find global x range
    xmin = min(min(df["time_num"].min() for df, _, _, _, _, _, _ in dfs), 2000)
    xmax = max(max(df["time_num"].max() for df, _, _, _, _, _, _ in dfs), 2025)

    # Create figure
    fig = pygmt.Figure()

    panel_width = 20  # cm
    pygmt.config(
        FONT_ANNOT_PRIMARY="20p",
        FONT_LABEL="20p",
        FONT_TITLE="20p",
        MAP_TICK_LENGTH_PRIMARY="6p",
        MAP_TICK_PEN_PRIMARY="1.2p",
        MAP_LABEL_OFFSET="10p",
        MAP_TICK_LENGTH_SECONDARY="3p",
        MAP_TICK_PEN_SECONDARY="0.8p",
        MAP_GRID_PEN="0.25p,gray70,10_5",
    )

    # Set locations for labels
    myxloc = [2000.2, 2000.2, 2000.2, 2000.2]
    myyloc = [15, 17, 17, 0]
    myyoff = [0, 0, 8.5, -3]

    for i, (
        df,
        label,
        (ymin, ymax),
        panel_height,
        txt_lbl,
        pen_col,
        frame_coord,
    ) in enumerate(dfs):
        region = [xmin, xmax, ymin, ymax]

        fig.basemap(
            region=region,
            projection=f"X{panel_width}c/{panel_height}c",
            frame=["xaf", f"yaff5+l{label}", frame_coord],
        )

        # Plot reference line and data
        fig.plot(x=[xmin, xmax], y=[myyloc[i], myyloc[i]], pen="1.5p,gray50,2_2")

        if filtered:
            fig.plot(x=df["time_num"], y=df[col], pen="3.5p,white", no_clip=(i == 3))
            fig.plot(x=df["time_num"], y=df[col], pen="2p," + pen_col, no_clip=(i == 3))
        else:
            fig.plot(
                x=df["time_num"], y=df[col], pen="1.5p," + pen_col, no_clip=(i == 3)
            )

        # Add text annotation
        fig.text(
            text=txt_lbl,
            x=myxloc[i],
            y=myyloc[i] + myyoff[i] + 0.5,
            font="18p,Helvetica",
            justify="LB",
        )

        # Shift down for next panel, except after last
        if i < len(dfs) - 1:
            if i < 2:
                fig.shift_origin(yshift=f"-{panel_height-1.5}c")
            else:
                fig.shift_origin(yshift=f"-{panel_height-1.2}c")

    # Add AMOCatlas timestamp
    _add_amocatlas_timestamp(fig)

    return fig


def plot_bryden2005_pygmt():
    """Plot Bryden et al. 2005 historical AMOC estimates using PyGMT.

    Creates a plot of the historical AMOC estimates from Bryden et al. (2005)
    showing the decline from 1957 to 2004. This provides historical context
    for modern observational time series.

    Returns
    -------
    pygmt.Figure
        PyGMT figure object.

    Raises
    ------
    ImportError
        If PyGMT is not installed.

    References
    ----------
    Bryden, H. L., Longworth, H. R., & Cunningham, S. A. (2005).
    Slowing of the Atlantic meridional overturning circulation at 25°N.
    Nature, 438(7068), 655-657.

    """
    _check_pygmt()

    import os
    import pandas as pd

    # Bryden 2005 data
    years = [1957, 1981, 1992, 1998, 2004]
    amoc_values = [22.9, 18.7, 19.4, 16.1, 14.8]
    xticks = [1957, 1970, 1981, 1992, 2004]
    xtick_labels = ["af", "af", "af", "af", "af"]

    # Write custom tick annotation file
    with open("custom_xticks.txt", "w") as f:
        for x, label in zip(xticks, xtick_labels):
            f.write(f"{x} {label}\n")

    # Create DataFrame
    data = pd.DataFrame({"Year": years, "AMOC": amoc_values})

    # Create figure
    fig = pygmt.Figure()

    pygmt.config(
        FONT_ANNOT_PRIMARY="18p",  # tick labels
        FONT_LABEL="18p",  # axis labels
        FONT_TITLE="18p",  # title (if used)
        MAP_TICK_LENGTH_PRIMARY="6p",  # major ticks longer
        MAP_TICK_PEN_PRIMARY="1.2p",  # major ticks thicker
        MAP_LABEL_OFFSET="10p",  # spacing axis ↔ label
        MAP_TICK_LENGTH_SECONDARY="3p",  # minor ticks longer
        MAP_TICK_PEN_SECONDARY="0.8p",  # minor ticks thicker
        MAP_GRID_PEN="0.25p,gray70,10_5",  # fine dashed grid
    )

    # Set region and frame
    fig.basemap(
        region=[1955, 2006, 13, 24],
        projection="X8c/6c",
        frame=["WS", "yaf+lMOC [Sv]", "xccustom_xticks.txt"],
    )

    # Plot red line
    fig.plot(x=data["Year"], y=data["AMOC"], pen="2p,red")

    # Plot red diamonds (with black edge)
    fig.plot(x=data["Year"], y=data["AMOC"], style="d0.3c", fill="red", pen="red")

    # Delete the custom tick file
    if os.path.exists("custom_xticks.txt"):
        os.remove("custom_xticks.txt")

    # Add AMOCatlas timestamp
    _add_amocatlas_timestamp(fig)

    return fig


def plot_all_moc_overlaid_pygmt(
    osnap_df: pd.DataFrame,
    rapid_df: pd.DataFrame,
    move_df: pd.DataFrame,
    samba_df: pd.DataFrame,
    filtered: bool = False,
):
    """Plot all MOC time series overlaid using separate coordinate systems.

    This creates overlaid plots with different y-ranges for MOC data vs SAMBA anomaly,
    similar to the original moc_tseries_pygmt notebook with shiftflag=False.

    Parameters
    ----------
    osnap_df : pandas.DataFrame
        OSNAP MOC data with 'time_num' and 'moc'/'moc_filtered'.
    rapid_df : pandas.DataFrame
        RAPID MOC data with 'time_num' and 'moc'/'moc_filtered'.
    move_df : pandas.DataFrame
        MOVE MOC data with 'time_num' and 'moc'/'moc_filtered'.
    samba_df : pandas.DataFrame
        SAMBA MOC data with 'time_num' and 'moc'/'moc_filtered'.
    filtered : bool, default False
        Whether to plot filtered data (True) or original data (False).

    Returns
    -------
    pygmt.Figure
        PyGMT figure object.

    Raises
    ------
    ImportError
        If PyGMT is not installed.

    """
    _check_pygmt()

    # Color scheme matching original
    magenta1 = "231/41/138"
    red1 = "227/26/28"
    blue1 = "8/104/172"
    green1 = "35/139/69"

    # Select column based on filtered flag
    col = "moc_filtered" if filtered else "moc"

    # Prepare data and labels - overlay mode (shiftflag=False)
    dfs = [
        (osnap_df, "MOC [Sv]", (10, 20), 6, "OSNAP", green1, "W"),
        (rapid_df, "MOC [Sv]", (10, 20), 6, "RAPID 26°N", red1, "W"),
        (move_df, "MOC [Sv]", (10, 20), 6, "MOVE 16°N", magenta1, "W"),
        (samba_df, "Anomaly [Sv]", (-5, 5), 6, "SAMBA 34.5°S", blue1, "ES"),
    ]

    # Find global x range
    xmin = min(min(df["time_num"].min() for df, _, _, _, _, _, _ in dfs), 2000)
    xmax = max(max(df["time_num"].max() for df, _, _, _, _, _, _ in dfs), 2025)

    # Create figure
    fig = pygmt.Figure()

    panel_width = 20  # cm
    pygmt.config(
        FONT_ANNOT_PRIMARY="20p",
        FONT_LABEL="20p",
        FONT_TITLE="20p",
        MAP_TICK_LENGTH_PRIMARY="6p",
        MAP_TICK_PEN_PRIMARY="1.2p",
        MAP_LABEL_OFFSET="10p",
        MAP_TICK_LENGTH_SECONDARY="3p",
        MAP_TICK_PEN_SECONDARY="0.8p",
        MAP_GRID_PEN="0.25p,gray70,10_5",
    )

    # Label positions for overlay mode
    myxloc = [2018.2, 2006.2, 2000.2, 2015.2]
    myyloc = [13.5, 19, 15, 0]
    myyoff = [0, 0, -3, -4]

    for i, (
        df,
        label,
        (ymin, ymax),
        panel_height,
        txt_lbl,
        pen_col,
        frame_coord,
    ) in enumerate(dfs):
        region = [xmin, xmax, ymin, ymax]

        fig.basemap(
            region=region,
            projection=f"X{panel_width}c/{panel_height}c",
            frame=["xaf", f"yaff2+l{label}", frame_coord],
        )

        # Add gray horizontal line at y=0
        fig.plot(x=[xmin, xmax], y=[0, 0], pen="1.5p,gray50,2_2")

        # Plot the time series with white background + colored foreground
        fig.plot(x=df["time_num"], y=df[col], pen="3.5p,white", no_clip=True)
        fig.plot(x=df["time_num"], y=df[col], pen="2p," + pen_col, no_clip=True)

        # Add text annotation
        fig.text(
            text=txt_lbl,
            x=myxloc[i],
            y=myyloc[i] + myyoff[i] + 0.5,
            font=f"18p,Helvetica,{pen_col}",
            justify="LB",
            no_clip=True,
        )

        # No shifting between panels in overlay mode
        if i < len(dfs) - 1:
            fig.shift_origin(yshift=0)

    # Add AMOCatlas timestamp
    _add_amocatlas_timestamp(fig)

    return fig
