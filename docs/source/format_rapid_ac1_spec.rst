RAPID Transport Data: OceanSITES/AC1 Specification
==================================================

This document provides the precise specification for converting RAPID array transport data from native format to OceanSITES/AC1 compatible format.

1. Overview
-----------

The RAPID array at 26°N produces multiple transport-related products that must be standardized for interoperability. This specification defines the exact structure, dimensions, variables, and attributes required for OceanSITES/AC1 compliance.

1.1 RAPID Native Products
~~~~~~~~~~~~~~~~~~~~~~~~~

The following RAPID products contain transport data:

.. list-table:: RAPID Transport Products
   :widths: 25 25 50
   :header-rows: 1

   * - Native File
     - Content Type
     - AC1 Target
   * - ``moc_transports.nc``
     - Component transports (12-hourly)
     - ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_transports_T12H.nc``
   * - ``meridional_transports.nc``
     - MOC, MHT, MFT (10-daily)
     - ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_transports_T10D.nc``
   * - ``moc_vertical.nc``
     - Streamfunction (12-hourly)
     - ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_streamfunction_T12H.nc``

1.2 Deviations from OceanSITES Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   The following choices differ from referenced standards and may need future revision based on community feedback.

.. list-table:: Format Deviations
   :widths: 30 35 35
   :header-rows: 1

   * - Attribute/Feature
     - OceanSITES Standard
     - AC1 Format
   * - ``time_coverage_start``
     - ``"YYYY-MM-DDThh:mm:ssZ"``
     - ``"YYYYmmddTHHMMss"``
   * - ``time_coverage_end``
     - ``"YYYY-MM-DDThh:mm:ssZ"``
     - ``"YYYYmmddTHHMMss"``
   * - ``SIGMA0`` coordinate
     - Depth/pressure coordinates only
     - Density coordinate dimension allowed
   * - Contributor attributes
     - ``creator_*``, ``principal_investigator_*``
     - ``contributor_*`` (following oceanarray pattern)

.. note::
   These deviations maintain ISO 8601 compatibility while reducing attribute string length and following established oceanarray patterns.

2. File Format Specifications
-----------------------------

2.1 Component Transports (12-hourly)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Target File**: ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_transports_T12H.nc``

**Source**: ``moc_transports.nc``

**Dimensions**:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Dimension
     - Specification
   * - ``TIME``
     - Unlimited, 12-hourly intervals
   * - ``N_COMPONENT``
     - 8 (number of transport components)

**Coordinate Variables**:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
   * - ``TIME``
     - ``TIME``
     - **Data Type**: double
       
       **Attributes**:
       
       - long_name = "Time"
       - standard_name = "time"
       - units = "seconds since 1970-01-01T00:00:00Z"
       - calendar = "gregorian"
       - axis = "T"
   * - ``LATITUDE``
     - scalar
     - **Data Type**: float32
       
       **Value**: 26.5
       
       **Attributes**:
       
       - long_name = "Latitude of RAPID array"
       - standard_name = "latitude"
       - units = "degree_north"
       - axis = "Y"
   * - ``LONGITUDE_BOUNDS``
     - (2,)
     - **Data Type**: float32
       
       **Values**: [-80.0, -13.0]
       
       **Attributes**:
       
       - long_name = "Longitude bounds of RAPID section"
       - standard_name = "longitude"
       - units = "degrees_east"

**Data Variables**:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
   * - ``TRANSPORT``
     - ``N_COMPONENT, TIME``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Ocean volume transport by component"
       - standard_name = "ocean_volume_transport_across_line"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - units = "sverdrup"
       - coordinates = "TIME LATITUDE"
       - _FillValue = NaNf
   * - ``TRANSPORT_NAME``
     - ``N_COMPONENT``
     - **Data Type**: string
       
       **Values**: ["ekman", "florida_straits", "upper_mid_ocean", "thermocline_recirculation", "intermediate_water", "upper_nadw", "lower_nadw", "aabw"]
       
       **Attributes**:
       
       - long_name = "Transport component names"
   * - ``TRANSPORT_DESCRIPTION``
     - ``N_COMPONENT``
     - **Data Type**: string
       
       **Values**: ["Ekman transport", "Florida Straits transport", "Upper Mid-Ocean transport", "Thermocline recirculation 0-800 m", "Intermediate water 800-1100 m", "Upper NADW 1100-3000 m", "Lower NADW 3000-5000 m", "AABW >5000 m"]
       
       **Attributes**:
       
       - long_name = "Transport component descriptions"
   * - ``MOC_TRANSPORT``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Meridional overturning circulation transport"
       - standard_name = "ocean_volume_transport_across_line"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - units = "sverdrup"
       - coordinates = "TIME LATITUDE"
       - _FillValue = NaNf
       - comment = "Total overturning transport (MOC index)"

**Variable Mapping**:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Native Variable
     - AC1 Mapping
   * - ``t_ek10``
     - ``TRANSPORT[0,:]`` (ekman)
   * - ``t_gs10``
     - ``TRANSPORT[1,:]`` (florida_straits)
   * - ``t_umo10``
     - ``TRANSPORT[2,:]`` (upper_mid_ocean)
   * - ``t_therm10``
     - ``TRANSPORT[3,:]`` (thermocline_recirculation)
   * - ``t_aiw10``
     - ``TRANSPORT[4,:]`` (intermediate_water)
   * - ``t_ud10``
     - ``TRANSPORT[5,:]`` (upper_nadw)
   * - ``t_ld10``
     - ``TRANSPORT[6,:]`` (lower_nadw)
   * - ``t_bw10``
     - ``TRANSPORT[7,:]`` (aabw)
   * - ``moc_mar_hc10``
     - ``MOC_TRANSPORT[:]``

2.2 MOC and Heat/Freshwater Transports (10-daily)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Target File**: ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_transports_T10D.nc``

**Source**: ``meridional_transports.nc``

**Dimensions**:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Dimension
     - Specification
   * - ``TIME``
     - Unlimited, 10-day intervals
   * - ``DEPTH``
     - 307 (depth levels)
   * - ``SIGMA0``
     - 631 (potential density anomaly levels)

.. warning::
   **[DEVIATION]** The ``SIGMA0`` coordinate dimension is a deviation from standard OceanSITES format, which typically uses depth/pressure coordinates. This dimension is required for density-coordinate streamfunction data from RAPID.

**Coordinate Variables**:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
   * - ``TIME``
     - ``TIME``
     - **Data Type**: double
       
       **Attributes**:
       
       - long_name = "Time"
       - standard_name = "time"
       - units = "seconds since 1970-01-01T00:00:00Z"
       - calendar = "gregorian"
       - axis = "T"
   * - ``LATITUDE``
     - scalar
     - **Data Type**: float32
       
       **Value**: 26.5
       
       **Attributes**:
       
       - long_name = "Latitude of RAPID array"
       - standard_name = "latitude"
       - units = "degree_north"
       - axis = "Y"
   * - ``DEPTH``
     - ``DEPTH``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Depth below sea surface"
       - standard_name = "depth"
       - units = "m"
       - positive = "down"
       - valid_min = 0.0
       - axis = "Z"
   * - ``PRESSURE``
     - ``DEPTH``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Sea water pressure"
       - standard_name = "sea_water_pressure"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0330/"
       - units = "dbar"
       - positive = "down"
       - valid_min = 0.0
   * - ``SIGMA0``
     - ``SIGMA0``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Potential density anomaly"
       - standard_name = "sea_water_sigma_theta"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0333/"
       - units = "kg m-3"
       - valid_min = 0.0
       - valid_max = 50.0

**Data Variables**:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
   * - ``MOC_TRANSPORT_DEPTH``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Maximum meridional overturning circulation transport from depth streamfunction"
       - standard_name = "ocean_volume_transport_across_line"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - units = "sverdrup"
       - coordinates = "TIME LATITUDE"
       - _FillValue = NaNf
       - comment = "Maximum value from depth-coordinate streamfunction"
   * - ``MOC_TRANSPORT_SIGMA``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Maximum meridional overturning circulation transport from density streamfunction"
       - standard_name = "ocean_volume_transport_across_line"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - units = "sverdrup"
       - coordinates = "TIME LATITUDE"
       - _FillValue = NaNf
       - comment = "Maximum value from density-coordinate streamfunction"
   * - ``HEAT_TRANSPORT``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Northward ocean heat transport"
       - standard_name = "northward_ocean_heat_transport"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0483/"
       - units = "petawatt"
       - coordinates = "TIME LATITUDE"
       - _FillValue = NaNf
   * - ``FRESHWATER_TRANSPORT``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Northward ocean freshwater transport"
       - standard_name = "northward_ocean_freshwater_transport"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0507/"
       - units = "sverdrup"
       - coordinates = "TIME LATITUDE"
       - _FillValue = NaNf
   * - ``STREAMFUNCTION_DEPTH``
     - ``TIME, DEPTH``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Meridional overturning streamfunction in depth coordinates"
       - standard_name = "ocean_meridional_overturning_streamfunction"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0466/"
       - units = "sverdrup"
       - coordinates = "TIME DEPTH LATITUDE"
       - _FillValue = NaNf
       - comment = "Overturning streamfunction in depth space"
   * - ``STREAMFUNCTION_SIGMA``
     - ``TIME, SIGMA0``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Meridional overturning streamfunction in density coordinates"
       - standard_name = "ocean_meridional_overturning_streamfunction"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0466/"
       - units = "sverdrup"
       - coordinates = "TIME SIGMA0 LATITUDE"
       - _FillValue = NaNf
       - comment = "Overturning streamfunction in density space"

**Variable Mapping**:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Native Variable
     - AC1 Mapping
   * - ``amoc_depth``
     - ``MOC_TRANSPORT_DEPTH``
   * - ``amoc_sigma``
     - ``MOC_TRANSPORT_SIGMA``
   * - ``heat_trans``
     - ``HEAT_TRANSPORT``
   * - ``frwa_trans``
     - ``FRESHWATER_TRANSPORT``
   * - ``stream_depth``
     - ``STREAMFUNCTION_DEPTH``
   * - ``stream_sigma``
     - ``STREAMFUNCTION_SIGMA``

2.3 Streamfunction (12-hour intervals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Target File**: ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_streamfunction_T12H.nc``

**Source**: ``moc_vertical.nc``

**Dimensions**:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Dimension
     - Specification
   * - ``TIME``
     - Unlimited, 12-hour intervals
   * - ``DEPTH``
     - 307 (depth levels)

**Coordinate Variables**:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
   * - ``TIME``
     - ``TIME``
     - **Data Type**: double
       
       **Attributes**:
       
       - long_name = "Time"
       - standard_name = "time"
       - units = "seconds since 1970-01-01T00:00:00Z"
       - calendar = "gregorian"
       - axis = "T"
   * - ``DEPTH``
     - ``DEPTH``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Depth below sea surface"
       - standard_name = "depth"
       - units = "m"
       - positive = "down"
       - valid_min = 0.0
       - axis = "Z"
   * - ``LATITUDE``
     - scalar
     - **Data Type**: float32
       
       **Value**: 26.5
       
       **Attributes**:
       
       - long_name = "Latitude of RAPID array"
       - standard_name = "latitude"
       - units = "degree_north"
       - axis = "Y"

**Data Variables**:

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
   * - ``STREAMFUNCTION``
     - ``TIME, DEPTH``
     - **Data Type**: float32
       
       **Attributes**:
       
       - long_name = "Meridional overturning streamfunction"
       - standard_name = "ocean_meridional_overturning_streamfunction"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0466/"
       - units = "sverdrup"
       - coordinates = "TIME DEPTH LATITUDE"
       - _FillValue = NaNf

**Variable Mapping**:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Native Variable
     - AC1 Mapping
   * - ``stream_function_mar``
     - ``STREAMFUNCTION`` (transposed from native (depth, time) to (TIME, DEPTH))

3. Global Attributes
-------------------

All RAPID AC1 files must include the following global attributes:

.. list-table:: Required Global Attributes
   :widths: 25 75
   :header-rows: 1

   * - Attribute
     - Specification
   * - ``Conventions``
     - "CF-1.8, OceanSITES-1.4, ACDD-1.3"
   * - ``format_version``
     - "1.4"
   * - ``data_type``
     - "OceanSITES time-series data"
   * - ``featureType``
     - "timeSeries"
   * - ``platform``
     - "subsurface mooring"
   * - ``site_code``
     - "RAPID"
   * - ``array``
     - "RAPID"
   * - ``data_mode``
     - "D"
   * - ``title``
     - "RAPID-MOCHA Ocean Transport Time Series at 26°N"
   * - ``summary``
     - "Meridional overturning circulation and transport components from the RAPID-MOCHA array at 26°N in the Atlantic Ocean."
   * - ``source``
     - "subsurface mooring"
   * - ``contributor_name``
     - "David Smeed, Ben Moat"
   * - ``contributor_role``
     - "Data scientist, Data scientist"
   * - ``contributor_role_vocabulary``
     - "https://vocab.nerc.ac.uk/collection/W08/current/"
   * - ``contributor_id``
     - "https://orcid.org/0000-0003-1740-1778, https://orcid.org/0000-0001-8676-7779"
   * - ``contributing_institutions``
     - "National Oceanography Centre (Southampton) (NOC), Atlantic Oceanographic and Meteorological Laboratory National Oceanic and Atmospheric Administration (NOAA AOML), Rosenstiel School of Marine and Atmospheric Science University of Miami (RSMAS)"
   * - ``contributing_institutions_vocabulary``
     - "https://edmo.seadatanet.org/report/17, https://edmo.seadatanet.org/report/1799, https://edmo.seadatanet.org/report/1382"
   * - ``contributing_institutions_role``
     - "Operator, Operator, Operator"
   * - ``contributing_institutions_role_vocabulary``
     - "https://vocab.nerc.ac.uk/collection/W08/current/"
   * - ``geospatial_lat_min``
     - 26.5
   * - ``geospatial_lat_max``
     - 26.5
   * - ``geospatial_lon_min``
     - -80.0
   * - ``geospatial_lon_max``
     - -13.0
   * - ``time_coverage_start``
     - "YYYYmmddTHHMMss" (e.g., "20040401T000000")
   * - ``time_coverage_end``
     - "YYYYmmddTHHMMss" (e.g., "20230211T235959")
   * - ``source_acknowledgement``
     - "Data from the RAPID AMOC observing project is funded by the Natural Environment Research Council, U.S. National Science Foundation (NSF) with support from NOAA. They are freely available from https://rapid.ac.uk/"
   * - ``references``
     - "https://www.rapid.ac.uk/, https://doi.org/10.5285/35784047-9b82-2160-e053-6c86abc0c91b"
   * - ``license``
     - "Data available free of charge. User assumes all risk for use of data."

.. warning::
   **Note on Deviations**: This specification includes deviations from OceanSITES standard (see section 1.2), particularly in time format (``YYYYmmddTHHMMss``) and contributor attributes (``contributor_*`` instead of ``creator_*`` and ``principal_investigator_*``). These choices follow oceanarray conventions and may need future revision based on community feedback.

.. note::
   **Source Data Version**: These specifications are based on RAPID dataset version v2024.1. Version information should be preserved in processing history or comments during conversion.

4. Validation Rules
------------------

4.1 Filename Validation
~~~~~~~~~~~~~~~~~~~~~~~

**OceanSITES Filename Convention**: ``OS_[PSPANCode]_[StartEndCode]_[ContentType]_[PARTX].nc``

**RAPID AC1 Filenames**:

.. list-table:: Expected Filenames
   :widths: 40 60
   :header-rows: 1

   * - File Type
     - Filename Pattern
   * - Component Transports (12-hour)
     - ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_transports_T12H.nc``
   * - MOC/Heat/Freshwater (10-day)
     - ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_transports_T10D.nc``
   * - Streamfunction (12-hour)
     - ``OS_RAPID_YYYYMMDD-YYYYMMDD_DPR_streamfunction_T12H.nc``

**Filename Components**:

- ``OS``: OceanSITES prefix (mandatory)
- ``RAPID``: Platform/array code (mandatory for RAPID data)
- ``YYYYMMDD-YYYYMMDD``: Start and end dates in compact format (mandatory)
- ``DPR``: Content type = Derived Product (mandatory for RAPID transports)
- ``PARTX``: Content descriptor with time resolution
  - ``transports_T12H``: 12-hour component transports
  - ``transports_T10D``: 10-day MOC/heat/freshwater transports  
  - ``streamfunction_T12H``: 12-hour streamfunction
- ``.nc``: NetCDF extension (mandatory)

**Validation Rules**:

- Filename must match exact pattern for intended file type
- Date range must be valid (start ≤ end)
- Date format must be ``YYYYMMDD`` (8 digits)
- File extension must be ``.nc``

4.2 Dimension Validation
~~~~~~~~~~~~~~~~~~~~~~~~

**Dimension Sizes**:

- ``TIME`` dimension must be unlimited
- ``N_COMPONENT`` must equal 8 for component transport files
- ``DEPTH`` must equal 307 for streamfunction and meridional transport files
- ``SIGMA0`` must equal 631 for meridional transport files

**Dimension Ordering** (T, Z, Y, X rule):

- Coordinate dimensions must follow CF convention: ``TIME``, ``DEPTH``/``PRESSURE``/``SIGMA0``, ``LATITUDE``, ``LONGITUDE``
- Component dimensions (``N_COMPONENT``) must be leftmost of spatiotemporal dimensions
- Valid examples: ``(N_COMPONENT, TIME)``, ``(TIME, DEPTH)``, ``(TIME, SIGMA0)``

4.3 Units Validation
~~~~~~~~~~~~~~~~~~~~

**Approved UDUNITS-2 Units** (must match exactly):

- Time: ``seconds since 1970-01-01T00:00:00Z``
- Latitude: ``degree_north`` (singular, not ``degrees_north``)
- Longitude: ``degree_east`` (singular, not ``degrees_east``)
- Depth: ``m``
- Pressure: ``dbar``
- Temperature: ``degree_Celsius``
- Salinity: ``1`` (dimensionless)
- Velocity: ``m s-1``
- Transport: ``sverdrup`` (not ``Sv``)
- Heat Transport: ``petawatt`` (not ``PW`` or ``watt``)
- Density: ``kg m-3``

4.4 Variable Validation
~~~~~~~~~~~~~~~~~~~~~~

**Required Attributes**:

- All coordinate variables must have ``axis`` attribute (T, Z, Y, or X)
- All variables must have ``long_name`` and ``standard_name`` where available
- All variables must include ``vocabulary`` attribute where specified in tables
- All data variables must have ``_FillValue`` matching variable data type
- All variables must have ``units`` attribute

**Vocabulary Validation**:

- Each variable with specified vocabulary must include exact URL from specification
- Vocabulary URLs must be accessible and valid NERC vocabulary references

**Data Value Validation**:

- **LATITUDE values**: Must be between -90 and 90 degrees
- **LONGITUDE values**: Must be between -180 and 360 degrees
- **DEPTH values**: Must be ≥0 if ``positive="down"``, or ≤0 if ``positive="up"``
- **PRESSURE values**: Must be ≥0 (pressure cannot be negative)
- **TIME values**: Must fall within date range specified in filename (``YYYYMMDD-YYYYMMDD``)
- **Transport/Streamfunction values**: Can be any sign (positive or negative flows are valid)
- **Temperature values**: Must be within ``valid_min`` and ``valid_max`` if specified
- **Salinity values**: Must be within ``valid_min`` and ``valid_max`` if specified

4.5 FeatureType Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Automatic FeatureType Assignment**:

- ``timeSeries``: Files with only ``TIME`` dimension (e.g., component transports)
- ``timeSeriesProfile``: Files with vertical coordinates (``DEPTH``, ``PRESSURE``, or ``SIGMA0``)

4.6 Global Attributes Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mandatory Attributes** (from AC1 format specification):

- ``Conventions`` = "CF-1.8, OceanSITES-1.4, ACDD-1.3"
- ``format_version`` = "1.4"
- ``data_type`` = "OceanSITES time-series data"
- ``featureType`` (auto-assigned based on dimensions)
- ``data_mode`` = "D"
- ``title``, ``summary``, ``source``
- ``geospatial_lat_min``, ``geospatial_lat_max``, ``geospatial_lon_min``, ``geospatial_lon_max``
- ``time_coverage_start``, ``time_coverage_end``

**RAPID-Specific Mandatory Attributes**:

- ``site_code`` = "RAPID"
- ``array`` = "RAPID"

**Contributor Information** (following oceanarray deviation):

- ``contributor_name``: Names of data contributors
- ``contributor_role``: Roles from NERC W08 vocabulary (e.g., "Data scientist", "Manufacturer")
- ``contributor_role_vocabulary`` = "https://vocab.nerc.ac.uk/collection/W08/current/"
- ``contributor_id``: ORCID URLs in format "https://orcid.org/0000-0000-0000-0000"

**Prohibited Attributes** (oceanarray deviation):

- ``creator_*`` attributes (not used)
- ``principal_investigator_*`` attributes (not used)

4.7 File-Specific Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Component Transports (T12H)**:

- Must contain ``N_COMPONENT`` dimension with size 8
- Must contain ``TRANSPORT`` variable with dimensions ``(N_COMPONENT, TIME)``
- Must contain ``MOC_TRANSPORT`` variable with dimension ``(TIME)``
- Must contain component name and description variables

**MOC/Heat/Freshwater Transports (T10D)**:

- Must contain ``DEPTH`` and ``SIGMA0`` dimensions with sizes 307 and 631
- Must contain streamfunction variables: ``STREAMFUNCTION_DEPTH``, ``STREAMFUNCTION_SIGMA``
- Must contain transport variables: ``MOC_TRANSPORT_DEPTH``, ``MOC_TRANSPORT_SIGMA``

**Streamfunction (T12H)**:

- Must contain ``DEPTH`` dimension with size 307
- Must contain ``STREAMFUNCTION`` variable with dimensions ``(TIME, DEPTH)``
- Must NOT contain ``SIGMA0`` dimension

4.8 Compliance Checklist
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Validation Checklist
   :widths: 50 50
   :header-rows: 1

   * - Check
     - Requirement
   * - **File Structure**
     - 
   * - NetCDF4 format
     - Must be valid NetCDF4 file
   * - Dimension ordering
     - T, Z, Y, X with components leftmost
   * - Unlimited TIME
     - TIME dimension must be unlimited
   * - **Variables**
     - 
   * - Required coordinates
     - TIME always present; others as specified
   * - Vocabulary URLs
     - All specified vocabularies present and valid
   * - Units compliance
     - Only approved UDUNITS-2 units
   * - Data types
     - float32 for data, double for TIME
   * - **Attributes**
     - 
   * - Mandatory globals
     - All required global attributes present
   * - Contributor format
     - ORCID as URLs, roles from W08 vocabulary
   * - FeatureType
     - timeSeries or timeSeriesProfile as appropriate
   * - **Standards**
     - 
   * - CF compliance
     - Must follow CF Conventions 1.8
   * - OceanSITES compliance
     - Must follow OceanSITES v1.4 (with noted deviations)
   * - AC1 compliance
     - Must follow AC1 format specification

5. Implementation Notes
----------------------

5.1 Unit Conversions
~~~~~~~~~~~~~~~~~~~~

- Native RAPID units "Sv" → AC1 "sverdrup"
- Native RAPID units "PW" → AC1 "petawatt"

5.2 Dimension Reordering
~~~~~~~~~~~~~~~~~~~~~~~

- Native streamfunction (depth, time) → AC1 (TIME, DEPTH)
- Follow CF convention T, Z, Y, X ordering

5.3 Quality Control
~~~~~~~~~~~~~~~~~~

- Preserve any existing quality flags from native data
- Add ``QC_indicator`` global attribute if quality assessment available

6. Compliance Verification
-------------------------

Each converted file must be validated using the AMOCatlas compliance checker, which verifies:

1. **File Structure**: NetCDF4 format, dimension ordering, unlimited TIME
2. **Variable Requirements**: Required coordinates, vocabularies, units, data types
3. **Attribute Compliance**: Mandatory global attributes, contributor information
4. **Format Standards**: CF Conventions 1.8, OceanSITES v1.4 (with deviations), AC1 specification
5. **File-Specific Rules**: Component dimensions, streamfunction variables, transport requirements

**Reference Implementation**: ``amocatlas.convert.rapid_to_ac1()``