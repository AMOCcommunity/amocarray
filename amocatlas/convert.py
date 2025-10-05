"""AMOCatlas Data Format Conversion

This module provides functionality to convert standardised AMOCatlas data to the AC1 format
following OceanSITES conventions and AC1 specifications.
"""

import xarray as xr
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple

from amocatlas import logger

log = logger.log


# Contributor ORCID lookup table
# Maps (array_name, contributor_name) tuples to ORCID identifiers
CONTRIBUTOR_ORCID_LOOKUP = {
    ("RAPID", "Ben Moat"): "https://orcid.org/0000-0001-8676-7779",
    ("rapid", "Ben Moat"): "https://orcid.org/0000-0001-8676-7779",
    ("RAPID", "Ben I. Moat"): "https://orcid.org/0000-0001-8676-7779",
    ("rapid", "Ben I. Moat"): "https://orcid.org/0000-0001-8676-7779",
}


def enrich_contributor_ids(attrs: Dict, array_name: str = None) -> Dict:
    """Enrich contributor information by adding ORCID identifiers where available.

    Parameters
    ----------
    attrs : Dict
        Dataset attributes dictionary
    array_name : str, optional
        Array name (e.g., 'RAPID', 'OSNAP')

    Returns
    -------
    Dict
        Updated attributes with enriched contributor_id field

    """
    if "contributor_name" not in attrs or not array_name:
        return attrs

    # Parse contributor names (handle comma-separated lists)
    names = [name.strip() for name in attrs["contributor_name"].split(",")]

    # Look up ORCIDs for each contributor
    orcids = []
    for name in names:
        # Try exact match first
        lookup_key = (array_name, name)
        if lookup_key in CONTRIBUTOR_ORCID_LOOKUP:
            orcids.append(CONTRIBUTOR_ORCID_LOOKUP[lookup_key])
            logger.log_info(
                f"Found ORCID for {name} in {array_name}: {CONTRIBUTOR_ORCID_LOOKUP[lookup_key]}"
            )
        else:
            # No match found, use empty string as placeholder
            orcids.append("")
            logger.log_warning(
                f"No ORCID found for contributor '{name}' in array '{array_name}'"
            )

    # Update contributor_id field
    attrs["contributor_id"] = ", ".join(orcids)

    return attrs


def to_AC1(
    ds: xr.Dataset, array_name: str = None, start_date: str = None, end_date: str = None
) -> List[xr.Dataset]:
    """Convert standardised AMOCatlas dataset to AC1 format datasets.

    Parameters
    ----------
    ds : xr.Dataset
        Standardised dataset from amocatlas.standardise
    array_name : str, optional
        Array name (e.g., 'RAPID'). If None, will try to determine from dataset.
    start_date : str, optional
        Start date in YYYYMMDD format. If None, will derive from data.
    end_date : str, optional
        End date in YYYYMMDD format. If None, will derive from data.

    Returns
    -------
    List[xr.Dataset]
        List of AC1-compliant datasets ready for saving

    Notes
    -----
    Currently supports RAPID moc_transports.nc conversion to component transports format.
    User should save the returned datasets using amocatlas.writers.save_dataset() or similar.

    """
    # Determine array name
    if array_name is None:
        array_name = _determine_array_name(ds)

    # Determine date range
    if start_date is None or end_date is None:
        start_date, end_date = _determine_date_range(ds)

    log.info(f"Converting {array_name} data to AC1 format")
    log.info(f"Date range: {start_date} to {end_date}")

    converted_datasets = []

    # Convert based on source data type
    source_file = ds.attrs.get("source_file", "")

    if "moc_transports" in source_file or _is_component_transport_data(ds):
        ac1_dataset = _convert_component_transports(
            ds, array_name, start_date, end_date
        )
        converted_datasets.append(ac1_dataset)
        log.info("Created component transports dataset")
    else:
        raise ValueError(f"Unsupported source data type: {source_file}")

    return converted_datasets


def _determine_array_name(ds: xr.Dataset) -> str:
    """Determine array name from dataset attributes."""
    # Check common attribute names
    for attr in ["array", "platform", "site_code"]:
        if attr in ds.attrs:
            value = ds.attrs[attr].upper()
            if value in ["RAPID", "OSNAP", "MOVE", "SAMBA"]:
                return value

    # Check source file name
    source_file = ds.attrs.get("source_file", "")
    if "rapid" in source_file.lower():
        return "RAPID"
    elif "osnap" in source_file.lower():
        return "OSNAP"
    elif "move" in source_file.lower():
        return "MOVE"
    elif "samba" in source_file.lower():
        return "SAMBA"

    # Default fallback
    log.warning("Could not determine array name, defaulting to 'RAPID'")
    return "RAPID"


def _determine_date_range(ds: xr.Dataset) -> Tuple[str, str]:
    """Determine date range from dataset time coordinate."""
    time_coord = ds["TIME"]

    # Convert to pandas datetime for easier handling
    time_pd = time_coord.to_pandas()
    start_dt = time_pd.iloc[0]
    end_dt = time_pd.iloc[-1]

    start_date = start_dt.strftime("%Y%m%d")
    end_date = end_dt.strftime("%Y%m%d")

    return start_date, end_date


def _is_component_transport_data(ds: xr.Dataset) -> bool:
    """Check if dataset contains component transport data."""
    # Look for transport variables with specific naming patterns
    transport_vars = [
        var for var in ds.data_vars if "t_" in var or "transport" in var.lower()
    ]
    return len(transport_vars) >= 6  # RAPID has 8-9 transport components


def _convert_component_transports(
    ds: xr.Dataset, array_name: str, start_date: str, end_date: str
) -> xr.Dataset:
    """Convert dataset to AC1 component transports format."""
    log.info(f"Converting to component transports format for {array_name}")

    # Define RAPID transport variable mapping
    transport_mapping = {
        "t_gs10": {
            "name": "Florida Straits",
            "description": "Florida Straits transport",
        },
        "t_ek10": {"name": "Ekman", "description": "Ekman transport"},
        "t_umo10": {
            "name": "Upper Mid-Ocean",
            "description": "Upper Mid-Ocean transport",
        },
        "t_therm10": {
            "name": "Thermocline",
            "description": "Thermocline recirculation 0-800m",
        },
        "t_aiw10": {
            "name": "Intermediate Water",
            "description": "Intermediate water 800-1100m",
        },
        "t_ud10": {"name": "Upper NADW", "description": "Upper NADW 1100-3000m"},
        "t_ld10": {"name": "Lower NADW", "description": "Lower NADW 3000-5000m"},
        "t_bw10": {"name": "AABW", "description": "AABW >5000m"},
    }

    # Get available transport variables
    available_transports = {
        var: transport_mapping[var] for var in transport_mapping if var in ds.data_vars
    }

    if not available_transports:
        raise ValueError("No recognized transport variables found in dataset")

    n_components = len(available_transports)
    log.info(
        f"Found {n_components} transport components: {list(available_transports.keys())}"
    )

    # Create new dataset structure
    ac1_ds = xr.Dataset()

    # Copy time coordinate - validate units from standardise.py, assign axis based on standard_name
    time_data = ds["TIME"].values
    orig_attrs = ds["TIME"].attrs if ds["TIME"].attrs else {}

    # Validate that TIME has required units
    if "units" not in orig_attrs:
        raise ValueError(
            "TIME coordinate is missing units attribute. Units should be assigned in standardise.py"
        )

    # Create fresh attributes to avoid encoding conflicts
    time_attrs = orig_attrs.copy()

    # Ensure standard metadata attributes
    time_attrs.update(
        {
            "standard_name": "time",
            "long_name": "Time",
            "axis": "T",  # Required for CF compliance and AC1 format
        }
    )

    ac1_ds["TIME"] = xr.DataArray(time_data, dims=["TIME"], attrs=time_attrs)

    # Add LATITUDE coordinate (scalar for RAPID 26°N)
    ac1_ds["LATITUDE"] = xr.DataArray(
        [26.5],
        dims=["LATITUDE"],
        attrs={
            "standard_name": "latitude",
            "long_name": "Latitude",
            "units": "degree_north",
            "axis": "Y",
        },
    )

    # Create N_COMPONENT dimension and coordinate
    component_names = list(available_transports.keys())
    ac1_ds["N_COMPONENT"] = xr.DataArray(
        np.arange(n_components),
        dims=["N_COMPONENT"],
        attrs={
            "long_name": "Transport component index",
            "units": "1",
            "comment": "Index for transport components",
        },
    )

    # Create TRANSPORT variable (N_COMPONENT, TIME) - validate units from standardise.py
    transport_data_list = []
    expected_units = "sverdrup"

    # Validate that all transport variables have the expected units
    for var in component_names:
        current_units = ds[var].attrs.get("units")
        if current_units is None:
            raise ValueError(
                f"Variable {var} is missing units attribute. Units should be assigned in standardise.py"
            )

        # Check for acceptable transport units (should be standardized in standardise.py)
        acceptable_units = [
            "sverdrup",
            "Sv",
            "Sverdrup",
        ]  # Different acceptable formats
        if current_units not in acceptable_units:
            raise ValueError(
                f"Variable {var} has units '{current_units}' but expected one of {acceptable_units}. Units should be standardized in standardise.py"
            )

        # Convert to AC1 standard if needed (only unit format changes, not values)
        var_data = ds[var].values
        if current_units in ["Sv", "Sverdrup"]:
            final_units = "sverdrup"  # AC1 standard format
        else:
            final_units = current_units

        transport_data_list.append(var_data)

    transport_data = np.array(transport_data_list)
    ac1_ds["TRANSPORT"] = xr.DataArray(
        transport_data,
        dims=["N_COMPONENT", "TIME"],
        attrs={
            "standard_name": "ocean_volume_transport_across_line",
            "long_name": "Volume transport across section",
            "units": "sverdrup",
            "vocabulary": "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/",
            "coordinates": "TIME LATITUDE",
            "_FillValue": np.nan,
            "comment": "Positive values indicate northward transport",
        },
    )

    # Create MOC_TRANSPORT variable (TIME) - use the MOC index if available
    if "moc_mar_hc10" in ds.data_vars:
        # Validate units from standardise.py
        moc_data = ds["moc_mar_hc10"].values
        current_units = ds["moc_mar_hc10"].attrs.get("units")

        if current_units is None:
            raise ValueError(
                "Variable moc_mar_hc10 is missing units attribute. Units should be assigned in standardise.py"
            )

        if current_units not in acceptable_units:
            raise ValueError(
                f"Variable moc_mar_hc10 has units '{current_units}' but expected one of {acceptable_units}. Units should be standardized in standardise.py"
            )

        ac1_ds["MOC_TRANSPORT"] = xr.DataArray(
            moc_data,
            dims=["TIME"],
            attrs={
                "standard_name": "ocean_meridional_overturning_streamfunction",
                "long_name": "Atlantic Meridional Overturning Circulation transport",
                "units": "sverdrup",
                "vocabulary": "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0466/",
                "coordinates": "TIME LATITUDE",
                "_FillValue": np.nan,
                "comment": "Maximum overturning transport",
            },
        )

    # Create TRANSPORT_NAME variable (string data, dimensionless)
    transport_names = [available_transports[var]["name"] for var in component_names]
    ac1_ds["TRANSPORT_NAME"] = xr.DataArray(
        transport_names,
        dims=["N_COMPONENT"],
        attrs={
            "long_name": "Transport component names",
            "units": "1",
            "comment": "Short names for each transport component",
        },
    )

    # Create TRANSPORT_DESCRIPTION variable (string data, dimensionless)
    transport_descriptions = [
        available_transports[var]["description"] for var in component_names
    ]
    ac1_ds["TRANSPORT_DESCRIPTION"] = xr.DataArray(
        transport_descriptions,
        dims=["N_COMPONENT"],
        attrs={
            "long_name": "Transport component descriptions",
            "units": "1",
            "comment": "Detailed descriptions of each transport component",
        },
    )

    # Copy and update global attributes
    ac1_ds.attrs = _create_ac1_global_attributes(
        ds, array_name, start_date, end_date, "transports_T12H"
    )

    return ac1_ds


def _create_ac1_global_attributes(
    ds: xr.Dataset, array_name: str, start_date: str, end_date: str, content_type: str
) -> Dict:
    """Create AC1-compliant global attributes."""
    attrs = {}

    # Required OceanSITES/CF/ACDD attributes
    attrs["Conventions"] = "CF-1.8, OceanSITES-1.4, ACDD-1.3"
    attrs["format_version"] = "1.4"
    attrs["data_type"] = "OceanSITES time-series data"
    attrs["featureType"] = "timeSeries"
    attrs["data_mode"] = "D"  # Delayed mode

    # Title and summary
    attrs["title"] = (
        f"{array_name} Atlantic Meridional Overturning Circulation Transport Components"
    )
    attrs["summary"] = (
        f"Component transport time series from the {array_name} observing array measuring the Atlantic Meridional Overturning Circulation."
    )

    # Source and provenance
    attrs["source"] = f"{array_name} moored array observations"
    attrs["site_code"] = array_name
    attrs["array"] = array_name

    # Geographic bounds (RAPID 26°N for now)
    if array_name == "RAPID":
        attrs["geospatial_lat_min"] = 26.5
        attrs["geospatial_lat_max"] = 26.5
        attrs["geospatial_lon_min"] = -79.0  # Approximate western boundary
        attrs["geospatial_lon_max"] = -13.0  # Approximate eastern boundary
        # Missing mandatory OceanSITES attributes
        attrs["platform_code"] = "RAPID26N"  # Unique platform identifier
    else:
        # Add geographic bounds for other arrays as needed
        attrs["platform_code"] = f"{array_name.upper()}_ARRAY"

    # Time coverage
    attrs["time_coverage_start"] = f"{start_date}T000000"
    attrs["time_coverage_end"] = f"{end_date}T235959"

    # Copy contributor information from original dataset
    contributor_attrs = [
        "contributor_name",
        "contributor_email",
        "contributor_id",
        "contributor_role",
        "contributing_institutions",
        "contributing_institutions_vocabulary",
        "contributing_institutions_role",
        "contributing_institutions_role_vocabulary",
    ]

    for attr in contributor_attrs:
        if attr in ds.attrs:
            attrs[attr] = ds.attrs[attr]

    # Enrich contributor information with ORCID identifiers
    attrs = enrich_contributor_ids(attrs, array_name)

    # Set default contributor role vocabulary if not present
    if "contributor_role_vocabulary" not in attrs:
        attrs["contributor_role_vocabulary"] = (
            "https://vocab.nerc.ac.uk/collection/W08/current/"
        )

    # Source acknowledgement
    if "acknowledgement" in ds.attrs:
        attrs["source_acknowledgement"] = ds.attrs["acknowledgement"]
    elif array_name == "RAPID":
        attrs["source_acknowledgement"] = (
            "Data from the RAPID AMOC observing project funded by the UK Natural Environment Research Council"
        )

    # License and DOI
    if "license" in ds.attrs:
        attrs["license"] = ds.attrs["license"]
    if "doi" in ds.attrs:
        attrs["doi"] = ds.attrs["doi"]

    # Processing metadata
    attrs["date_created"] = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    attrs["processing_level"] = (
        "Data verified against model or other contextual information"
    )
    attrs["comment"] = (
        f'Converted to AC1 format from {ds.attrs.get("source_file", "original data")} using amocatlas.convert.to_AC1()'
    )

    # Additional mandatory OceanSITES attributes
    attrs["naming_authority"] = "AMOCatlas"
    attrs["id"] = f"OS_{array_name}_{start_date}-{end_date}_DPR_{content_type}"
    attrs["cdm_data_type"] = "TimeSeries"

    # Quality control attributes
    attrs["QC_indicator"] = "excellent"  # no known problems, all important QC done

    # Institution information (if not already present)
    if "institution" not in attrs:
        attrs["institution"] = "AMOCatlas Community"

    return attrs


# Additional utility functions for future expansion


def _validate_ac1_output(ds: xr.Dataset, file_type: str) -> bool:
    """Validate AC1 dataset before writing."""
    # This could use the compliance checker we built
    # For now, just basic checks

    required_coords = ["TIME"]
    for coord in required_coords:
        if coord not in ds.coords:
            raise ValueError(f"Missing required coordinate: {coord}")

    if file_type == "component_transports":
        required_vars = ["TRANSPORT", "TRANSPORT_NAME", "TRANSPORT_DESCRIPTION"]
        for var in required_vars:
            if var not in ds.data_vars:
                raise ValueError(f"Missing required variable: {var}")

    return True


def _get_ac1_filename(
    array_name: str, start_date: str, end_date: str, content_type: str, partx: str
) -> str:
    """Generate AC1-compliant filename."""
    return f"OS_{array_name}_{start_date}-{end_date}_{content_type}_{partx}.nc"
