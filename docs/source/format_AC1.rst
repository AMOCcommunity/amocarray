AMOCatlas Format AC1
====================

This document defines the AC1 (AMOCatlas Comprehensive) standard data format with enhanced OceanSITES compliance. This format provides maximum interoperability between moored estimates of overturning transport from the RAPID, OSNAP, MOVE and SAMBA arrays while ensuring full compliance with international oceanographic data standards.

**Relationship to Other Format Documents:**

- :doc:`format_orig` - Documents native data formats from each array
- :doc:`format_conversion` - Describes conversion strategies from native to standardized formats  
- :doc:`format_oceanSITES` - Details OceanSITES compliance requirements
- :doc:`format_AC1` - Current standardized output format implementation
- **This document (format_AC1)** - AC1 format with full OceanSITES integration

.. contents:: Table of Contents
   :local:
   :depth: 3

1. Overview & Context
---------------------

The AC1 format incorporates comprehensive OceanSITES v1.4 compliance for enhanced discoverability and interoperability, while adding rich metadata and standardized naming conventions for global data exchange.

The AC1 format provides enhanced compliance with:

- **Full Standards Compliance**: Complete implementation of CF Conventions 1.8, OceanSITES 1.4, and ACDD 1.3
- **Enhanced Discoverability**: Rich metadata using controlled vocabularies for global data catalogs
- **Workflow Integration**: Compatible with existing AMOCatlas workflows
- **International Interoperability**: Full compliance with OceanSITES and GDAC requirements
- **Provenance Tracking**: Comprehensive attribution to original data providers
- **Extensibility**: Supports future variables and array additions

1.1 Relationship to Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AC1 format represents the comprehensive standardization level in the AMOCatlas hierarchy:

.. code-block:: text

   Native Formats → Internal standardised → AC1 Standard  
   (format_orig)       (format_Atlas)       (format_AC1)    

**Compliance Framework**: AC1 datasets are designed to meet:

- CF Conventions 1.8 compliance (validation tools to be implemented)
- OceanSITES 1.4 compatibility (with documented deviations as specified in :ref:`deviations-from-oceansites`)
- AMOCatlas-specific validation rules (see :mod:`amocatlas.compliance_checker`)
- ACDD-1.3 metadata structure

**Standards Integration**: The format integrates multiple international standards:

- **CF Conventions 1.8**: `Climate and Forecast metadata conventions <https://cfconventions.org/cf-conventions/cf-conventions.html>`_
- **OceanSITES 1.4**: `Ocean observing time series data format <https://ocean-uhh.github.io/oceanarray/oceanSITES_manual.html>`_
- **ACDD 1.3**: `Attribute Convention for Data Discovery <https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3>`_
- **NERC Vocabularies**: :doc:`Controlled vocabularies for oceanographic parameters <AC1_vocabularies>`

2. Key Design Decisions
-----------------------

The AC1 format incorporates several design decisions that enhance interoperability while maintaining scientific accuracy and usability.

.. _deviations-from-oceansites:

2.1 Deviations from OceanSITES Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AC1 implements OceanSITES 1.4 with the following deviations optimized for AMOC array data:

.. list-table:: Deviations from OceanSITES Standard
   :widths: 30 35 35
   :header-rows: 1

   * - Feature
     - OceanSITES Standard
     - AC1 Format
   * - **Date Format**
     - ``"YYYY-MM-DDThh:mm:ssZ"``
     - Compact ISO 8601: ``"YYYYmmddTHHMMss"``
   * - **Contributor Metadata**
     - ``creator_*``, ``principal_investigator_*``
     - ``contributor_*`` attributes (unified pattern)
   * - **Density Coordinates**
     - Depth/pressure coordinates only
     - ``SIGMA0`` coordinate allowed (array-specific)
   * - **Component Dimension**
     - Not specified
     - ``N_COMPONENT`` for transport decomposition
   * - **Coordinate Units**
     - ``degrees_north``, ``degrees_east``
     - ``degree_north``, ``degree_east`` (UDUNITS-2)
   * - **Transport Units**
     - ``Sv`` for transport
     - ``sverdrup`` (avoids confusion with sievert)

**Rationale for Deviations**:

- **Contributor Pattern**: Unified ``contributor_*`` approach simplifies metadata management while providing equivalent functionality
- **Sigma Coordinates**: Essential for density-based transport calculations in some arrays
- **Component Dimension**: Enables systematic representation of transport decompositions across arrays
- **Coordinate Units**: `UDUNITS-2 <https://docs.unidata.ucar.edu/udunits/current/#Database>`_ singular forms provide better tool compatibility than OceanSITES plural forms
- **Sverdrup Unit**: Full spelling prevents confusion with ``Sv`` (sievert radiation unit)

These deviations maintain full CF compliance and ISO 8601 compatibility while optimizing for AMOC-specific scientific requirements.

3. File Organisation & Naming
-----------------------------

3.1 File Naming Convention
~~~~~~~~~~~~~~~~~~~~~~~~

Files follow the OceanSITES naming pattern with AMOC-specific modifications:

**Basic Pattern**: ``OS_[PLATFORM]_[DEPLOYMENT]_[MODE]_[PARAMS].nc``

**Components**:

- ``OS`` = OceanSITES prefix (maintains compatibility)
- ``[PLATFORM]`` = Platform identifier (e.g., "RAPID", "OSNAP") 
- ``[DEPLOYMENT]`` = Deployment code (e.g., "20040401-20230211" for date range)
- ``[MODE]`` = Data mode: R (real-time), P (provisional), D (delayed-mode)
- ``[PARAMS]`` = Parameter identifier (e.g., "transports_T12H", "sections_T1M")

**Examples**:

- ``OS_RAPID_20040401-20230211_D_transports_T12H.nc`` - Delayed-mode transport data
- ``OS_OSNAP_20140801-20200601_D_sections_T1M.nc`` - Delayed-mode section data

**Reference**: See OceanSITES file naming in "4.1.1 Deployment Data files Naming Convention".




4. Global Attributes
--------------------

Following OceanSITES 1.4, ACDD 1.3, and CF 1.8 requirements for comprehensive metadata.

.. note::
   **Requirement Status**: **M** = Mandatory, *HD* = Highly Desired, *S* = Suggested

4.1 Discovery and Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Discovery and Identification Attributes
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Vocabulary
     - RS
   * - ``site_code``
     - "RAPID"
     - OceanSITES site identifier
     - OceanSITES Registry
     - **M**
   * - ``array``
     - "RAPID"
     - Array grouping identifier
     - Custom AMOCatlas
     - **M**
   * - ``data_mode``
     - "D"
     - Data mode: R=real-time, P=provisional, D=delayed
     - OceanSITES Standard
     - **M**
   * - ``title``
     - "RAPID-MOCHA Transport Time Series"
     - Human-readable dataset title
     - Free text
     - *HD*
   * - ``theme``
     - "Transport Moored Arrays"
     - OceanSITES theme classification
     - OceanSITES Themes
     - *S*
   * - ``naming_authority``
     - "AMOCatlas"
     - Authority providing the dataset ID
     - Reverse DNS recommended
     - *S*
   * - ``id``
     - "OS_RAPID_20040402-20240327_DPR_transports_T12H"
     - Unique dataset identifier (filename without .nc)
     - OceanSITES Pattern
     - **M**
   * - ``summary``
     - "Oceanographic mooring data from the RAPID array at 26°N..."
     - Extended description for discovery (≤100 words)
     - Free text
     - *S*
   * - ``source``
     - "subsurface mooring"
     - Platform type from controlled vocabulary
     - SeaVoX L06
     - *HD*
   * - ``keywords``
     - "EARTH SCIENCE > Oceans > Ocean Circulation"
     - Discovery keywords (comma-separated)
     - GCMD preferred
     - *S*
   * - ``keywords_vocabulary``
     - "GCMD Science Keywords"
     - Vocabulary source for keywords
     - Standards reference
     - *S*
   * - ``comment``
     - "Preliminary version; subject to revision"
     - Miscellaneous information
     - Free text
     - *S*

4.2 Provenance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consolidates OceanSITES creator_* and principal_investigator_* fields into unified contributor_* attributes supporting multiple contributors following OG1 patterns.

.. list-table:: Contributor and Attribution Attributes
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Vocabulary
     - RS
   * - ``contributor_name``
     - "Dr. Jane Doe, Dr. John Smith"
     - Names of dataset contributors (comma-separated)
     - Free text
     - **M**
   * - ``contributor_email``
     - "jane.doe@example.org, john.smith@noc.ac.uk"
     - Email addresses (aligned with names)
     - Email format
     - **M**
   * - ``contributor_id``
     - "https://orcid.org/0000-0002-1825-0097, ..."
     - Persistent IDs (ORCID preferred)
     - ORCID/ISNI URLs
     - *HD*
   * - ``contributor_role``
     - "principalInvestigator, creator"
     - Roles (aligned with names)
     - NERC W08
     - **M**
   * - ``contributor_role_vocabulary``
     - "https://vocab.nerc.ac.uk/collection/W08/current/"
     - Vocabulary for contributor roles
     - Standards reference
     - **M**
   * - ``contributing_institutions``
     - "University of Hamburg, National Oceanography Centre"
     - Institutional contributors
     - Free text
     - **M**
   * - ``contributing_institutions_vocabulary``
     - "https://ror.org/"
     - Institutional identifier vocabulary
     - ROR/EDMO preferred
     - *HD*
   * - ``contributing_institutions_role``
     - "operator, dataProvider"
     - Institutional roles
     - NERC W08
     - **M**
   * - ``contributing_institutions_role_vocabulary``
     - "https://vocab.nerc.ac.uk/collection/W08/current/"
     - Vocabulary for institutional roles
     - Standards reference
     - **M**


**Standard Contributor Roles:** ``Data scientist``, ``Manufacturer``, ``PI``, ``Technical Coordinator``, ``Operator``, ``Owner``

Provenance and Data History


.. list-table:: Provenance and Source Attribution
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Format
     - RS
   * - ``source_acknowledgement``
     - "RAPID data collected and made freely available by the RAPID program..."
     - Attribution to original data providers (semicolon-separated)
     - Free text
     - **M**
   * - ``source_doi``
     - "https://doi.org/10.35090/gatech/70342; https://doi.org/10.1029/2018GL077408"
     - DOIs of source datasets (semicolon-separated)
     - DOI URLs
     - **M**
   * - ``amocatlas_version``
     - "0.3.0"
     - Version of amocatlas used for processing
     - Semantic version
     - **M**
   * - ``web_link``
     - "https://www.rapid.ac.uk/; https://www.o-snap.org/"
     - Links to project websites (semicolon-separated)
     - URLs
     - *S*
   * - ``start_date``
     - "2004-04-02T00:00:00Z"
     - Overall dataset start time
     - ISO 8601
     - **M**
   * - ``generated_doi``
     - "https://doi.org/10.xxxx/amocatlas-ac-proposed-2025"
     - DOI assigned to converted dataset (if available)
     - DOI URL
     - *S*




4.3 Geospatial and Temporal Coverage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Geospatial and Temporal Attributes
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Format
     - RS
   * - ``geospatial_lat_min``
     - 26.0
     - Southernmost latitude
     - Decimal degrees
     - **M**
   * - ``geospatial_lat_max``
     - 26.5
     - Northernmost latitude
     - Decimal degrees
     - **M**
   * - ``geospatial_lat_units``
     - "degrees_north"
     - Latitude units
     - UDUNITS-2
     - *S*
   * - ``geospatial_lon_min``
     - -80.0
     - Westernmost longitude
     - Decimal degrees
     - **M**
   * - ``geospatial_lon_max``
     - -13.0
     - Easternmost longitude
     - Decimal degrees
     - **M**
   * - ``geospatial_lon_units``
     - "degrees_east"
     - Longitude units
     - UDUNITS-2
     - *S*
   * - ``geospatial_vertical_min``
     - 0.0
     - Minimum depth/height
     - Meters
     - **M**
   * - ``geospatial_vertical_max``
     - 5000.0
     - Maximum depth/height
     - Meters
     - **M**
   * - ``geospatial_vertical_positive``
     - "down"
     - Vertical direction convention
     - "up" or "down"
     - *S*
   * - ``geospatial_vertical_units``
     - "m"
     - Vertical coordinate units
     - UDUNITS-2
     - *S*
   * - ``time_coverage_start``
     - "2004-04-02T00:00:00Z"
     - Dataset start time
     - ISO 8601
     - **M**
   * - ``time_coverage_end``
     - "2024-03-27T23:59:59Z"
     - Dataset end time
     - ISO 8601
     - **M**
   * - ``time_coverage_duration``
     - "P19Y11M25D"
     - Dataset duration
     - ISO 8601 Duration
     - *S*
   * - ``time_coverage_resolution``
     - "PT12H"
     - Temporal resolution
     - ISO 8601 Duration
     - *S*
   * - ``sea_area``
     - "North Atlantic Ocean"
     - Geographical coverage
     - SeaVoX C19
     - *S*


Time Format Rationale: The compact YYYYmmddTHHMMss format reduces attribute string length while maintaining human readability and ISO 8601 compatibility.

File dates: The file dates, date_created and date_modified, are our interpretation of the file dates as defined by ACDD. Date_created is the time stamp on the file, date_modified may be used to represent the ‘version date’ of the geophysical data in the file. The date_created may change when e.g. metadata is added or the file format is updated, and the optional date_modified MAY be earlier.

Geospatial extents: (geospatial_lat_min, max, and lon_min, max) are preferred to be stored as strings for use in the GDAC software, however numeric fields are acceptable. This information is linked to the site information, and may not be specific to the platform deployment.

4.4 Publication and Licensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Publication and Licensing Attributes
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Format
     - RS
   * - ``publisher_name``
     - "AMOCatlas Development Team"
     - Data publisher name
     - Free text
     - *S*
   * - ``publisher_url``
     - "https://github.com/AMOCcommunity/amocatlas"
     - Publisher web address
     - URL
     - *S*
   * - ``references``
     - "http://www.oceansites.org, https://doi.org/10.1029/2018GL077408"
     - Relevant publications and resources (semicolon-separated)
     - URLs/DOIs
     - *S*
   * - ``license``
     - "CC-BY-4.0"
     - Data license
     - License identifier
     - *S*
   * - ``citation``
     - "These data were collected and made freely available by the OceanSITES program..."
     - Recommended citation text
     - Free text
     - *S*
   * - ``acknowledgement``
     - "Principal funding provided by Horizon Europe EPOC project..."
     - Funding and support acknowledgements
     - Free text
     - *S*


4.5 Technical and Processing Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Technical and Processing Attributes
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Format
     - RS
   * - ``featureType``
     - "timeSeries"
     - CF discrete sampling geometry type
     - CF Standard
     - **M**
   * - ``data_type``
     - "OceanSITES time-series data"
     - OceanSITES data type classification
     - OceanSITES Standard
     - **M**
   * - ``format_version``
     - "1.4"
     - OceanSITES format version
     - Version string
     - **M**
   * - ``Conventions``
     - "CF-1.8, OceanSITES-1.4, ACDD-1.3"
     - Metadata conventions followed
     - Standards list
     - *S*
   * - ``platform_code``
     - "RAPID26N"
     - Unique platform identifier
     - Free text
     - **M**
   * - ``QC_indicator``
     - "excellent"
     - Overall quality assessment
     - OceanSITES QC levels
     - *S*
   * - ``processing_level``
     - "Data verified against model or other contextual information"
     - Processing level description
     - OceanSITES levels
     - *S*
   * - ``date_created``
     - "2025-01-15T10:30:00Z"
     - File creation timestamp
     - ISO 8601
     - **M**
   * - ``date_modified``
     - "2025-01-15T10:30:00Z"
     - Last modification timestamp
     - ISO 8601
     - *S*
   * - ``history``
     - "2025-01-15T10:30:00Z: Converted to AC1 using amocatlas v0.3.0"
     - Processing history log
     - Timestamped entries
     - *S*


5. Dimensions & Coordinates
---------------------------
Following CF conventions, dimensions are ordered as T, Z, Y, X with component dimensions leftmost:

.. list-table:: Dimension Ordering
   :widths: 20 30 50
   :header-rows: 1

   * - Category
     - Dimensions
     - Description
   * - **Component**
     - ``N_COMPONENT``
     - Transport components (optional)
   * - **Temporal**
     - ``TIME``
     - Time coordinate (unlimited)
   * - **Vertical**
     - ``DEPTH``, ``PRESSURE``
     - Vertical coordinates (optional)
   * - **Horizontal**
     - ``LATITUDE``, ``LONGITUDE``
     - Horizontal coordinates (optional)

.. warning::
   All datasets must include the ``TIME`` dimension. Other dimensions are optional depending on data type (timeSeries vs timeSeriesProfile).

   
.. list-table:: Coordinate Variables
   :widths: 15 20 50 5
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
     - RS
   * - ``TIME``
     - ``TIME``
     - **Data Type**: double (datetime64[ns])
       
       **Required Attributes**:

       - long_name = "Time"
       - standard_name = "time"
       - units = "seconds since 1970-01-01T00:00:00Z"
       - calendar = "gregorian"
       - axis = "T"
     - **M**
   * - ``LATITUDE``
     - scalar or ``LATITUDE``
     - **Data Type**: float32
       
       **Required Attributes**:

       - long_name = "Latitude"
       - standard_name = "latitude"
       - units = "degree_north"
       - valid_min = -90.0
       - valid_max = 90.0
       - axis = "Y"
     - *HD*
   * - ``LONGITUDE``
     - scalar or ``LONGITUDE``
     - **Data Type**: float32
       
       **Required Attributes**:

       - long_name = "Longitude"
       - standard_name = "longitude"
       - units = "degree_east"
       - valid_min = -180.0
       - valid_max = 180.0
       - axis = "X"
     - *HD*
   * - ``DEPTH``
     - ``DEPTH``
     - **Data Type**: float32
       
       **Required Attributes**:

       - long_name = "Depth below sea surface"
       - standard_name = "depth"
       - units = "m"
       - positive = "down"
       - valid_min = 0.0
       - axis = "Z"
     - *S*
   * - ``PRESSURE``
     - ``PRESSURE``
     - **Data Type**: float32
       
       **Required Attributes**:

       - long_name = "Sea water pressure"
       - standard_name = "sea_water_pressure"
       - units = "dbar"
       - positive = "down"
       - valid_min = 0.0
       - axis = "Z"
     - *S*
   * - ``SIGMA0``
     - ``SIGMA0``
     - **Data Type**: float32
       
       **Required Attributes**:

       - long_name = "Sea water sigma-theta"
       - standard_name = "sea_water_sigma_theta"
       - units = "kg m-3"
       - axis = "Z"
       - positive = "down"
     - *S*

6. Data Variables & QC
--------------------



6.1 Transport Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Transport Variables
   :widths: 30 60 10
   :header-rows: 1

   * - Variable Name
     - Variable Attributes
     - RS
   * - ``MOC_TRANSPORT``
       
       - **Data Type**: float32
       
       - **Dimensions**: ``TIME``
     - - long_name = "Maximum meridional overturning circulation transport"
       - standard_name = "ocean_volume_transport_across_line"
       - units = "sverdrup"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -50.0 (optional)
       - valid_max = 50.0 (optional)
     - *HD*
   * - ``TRANSPORT``
       
       - **Data Type**: float32

       - **Dimensions**: ``N_COMPONENT``, ``TIME``
     - - long_name = "Ocean volume transport components across line"
       - standard_name = "ocean_volume_transport_across_line"
       - units = "sverdrup"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
     - *HD*
   * - ``HEAT_TRANSPORT``
       
       - **Data Type**: float32

       - **Dimensions**: ``TIME``
     - - long_name = "Northward ocean heat transport"
       - standard_name = "northward_ocean_heat_transport"
       - units = "PW"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0483/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -5.0 (optional)
       - valid_max = 5.0 (optional)
     - *S*
   * - ``FRESHWATER_TRANSPORT``

       - **Data Type**: float32

       - **Dimensions**: ``TIME`` 
     - - long_name = "Northward ocean freshwater transport"
       - standard_name = "northward_ocean_freshwater_transport"
       - units = "sverdrup"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0507/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -5.0 (optional)
       - valid_max = 5.0 (optional)
     - *S*

6.2 Hydrographic Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. list-table:: Hydrographic Variables
   :widths: 30 60 10
   :header-rows: 1

   * - Variable Name
     - Variable Attributes
     - RS
   * - ``TEMP``
        - data type: float32
        - dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     -
        - long_name = "Sea water temperature"
        - standard_name = "sea_water_temperature"
        - units = "degree_Celsius"
        - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0335/"
        - valid_min = -2.0
        - valid_max = 40.0
        - _FillValue = NaNf
        - ancillary_variables = "TEMPERATURE_QC"
        - coordinates = "TIME, DEPTH, LATITUDE, LONGITUDE"
     - *HD*
   * - ``PSAL``
        - data type: float32
        - dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     -
        - long_name = "Sea water practical salinity"
        - standard_name = "sea_water_practical_salinity"
        - units = "1"
        - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/IADIHDIJ/"
        - valid_min = 0.0
        - valid_max = 50.0
        - _FillValue = NaNf
        - ancillary_variables = "SALINITY_QC"
        - coordinates = "TIME, DEPTH, LATITUDE, LONGITUDE"
     - *HD*
   * - ``UCUR``
        - data type: float32
        - dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     -
        - long_name = "Eastward sea water velocity"
        - standard_name = "eastward_sea_water_velocity"
        - units = "m s-1"
        - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0650/"
        - valid_min = -2.0
        - valid_max = 2.0
        - _FillValue = NaNf
        - ancillary_variables = "VELOCITY_EAST_QC"
        - coordinates = "TIME, DEPTH, LATITUDE, LONGITUDE"
     - *S*
   * - ``VCUR``
        - data type: float32
        - dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     -
        - long_name = "Northward sea water velocity"
        - standard_name = "northward_sea_water_velocity"
        - units = "m s-1"
        - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0494/"
        - valid_min = -2.0
        - valid_max = 2.0
        - _FillValue = NaNf
        - ancillary_variables = "VELOCITY_NORTH_QC"
        - coordinates = "TIME, DEPTH, LATITUDE, LONGITUDE"
     - *S*

6.3 Descriptive Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. list-table:: Descriptive Variables (Component Transport Arrays)
   :widths: 30 60 10
   :header-rows: 1

   * - Variable Name
     - Variable Attributes
     - RS
   * - ``TRANSPORT_NAME``
        - data type: |S64 (string)
        - dimensions: (``N_COMPONENT``)
     -
        - long_name = "Transport component names"
        - coordinates = "N_COMPONENT"
        - content = "Short descriptive names (e.g., Ekman, UMO, AMOC, Florida_Current)"
     - *HD*
   * - ``TRANSPORT_DESCRIPTION``
        - data type: |S256 (string)
        - dimensions: (``N_COMPONENT``)
     -
        - long_name = "Transport component descriptions"
        - coordinates = "N_COMPONENT"
        - content = "Detailed descriptions of transport components"
     - *S*

.. note::
   **Requirement Status**: **M** = Mandatory, *HD* = Highly Desired, *S* = Suggested


6.4 Variable-Level Quality Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For variables requiring quality control, implement OceanSITES QC conventions:

.. list-table:: Quality Control Variables
   :widths: 20 20 50 10
   :header-rows: 1

   * - QC Variable
     - Dimensions
     - Attributes and Values
     - RS
   * - ``<PARAM>_QC``
     - Same as parent variable
     - **Data Type**: byte
       
       **Required Attributes**:
       - long_name = "Quality flag for <parameter_name>"
       - flag_values = [0, 1, 2, 3, 4, 7, 8, 9]
       - flag_meanings = "unknown good_data probably_good_data potentially_correctable_bad_data bad_data nominal_value interpolated_value missing_value"
       - valid_min = 0
       - valid_max = 9
     - *S*
   * - ``<PARAM>_UNCERTAINTY``
     - Same as parent variable
     - **Data Type**: float32
       
       **Required Attributes**:
       - long_name = "Uncertainty estimate for <parameter_name>"
       - units = Same as parent variable
       - technique_title = "Description of uncertainty estimation method"
     - *S*




7. Conversion Tools and Implementation
-------------------------------------

7.1 Enhanced Conversion Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To produce AC1 compliant datasets from standardized inputs:

.. code-block:: python

   from amocatlas.convert import to_AC1
   
   # Convert with enhanced metadata
   ds_ac1 = to_AC1(
       ds_standardized,
       array_metadata_yaml="metadata/rapid_array.yml",
       validate=True,
       gdac_compliant=True
   )

7.2 Conversion Process
~~~~~~~~~~~~~~~~~~~~~

The conversion function performs these operations:

1. **Input Validation**: Verify standardized dataset structure
2. **Metadata Integration**: Load and apply array-specific YAML metadata
3. **Attribute Enhancement**: Add comprehensive global attributes following OceanSITES/ACDD standards
4. **Variable Standardization**: Ensure proper standard names, units, and vocabularies
5. **Quality Control**: Apply QC flags and uncertainty estimates where available
6. **File Naming**: Generate OceanSITES-compliant filename
7. **Compliance Validation**: Run CF Checker and OceanSITES validation
8. **Output Generation**: Write NetCDF4 file with optimal compression and chunking

7.3 Validation Tools
~~~~~~~~~~~~~~~~~~

All AC datasets must pass comprehensive validation:

.. list-table:: Validation Checks
   :widths: 30 70
   :header-rows: 1

   * - Validation Category
     - Requirements
   * - **File Naming**
     - Must match OceanSITES pattern: ``OS_[PSPANCode]_[StartEndCode]_[ContentType]_[PARTX].nc``
   * - **Global Attributes**
     - All mandatory (**M**) attributes must be present with valid values
   * - **Coordinate Variables**
     - TIME dimension required; appropriate axis attributes; valid units
   * - **Data Variables**
     - Valid standard_name attributes; UDUNITS-2 compliant units; appropriate _FillValue
   * - **CF Compliance**
     - Must pass CF Checker with zero errors
   * - **OceanSITES Compliance**
     - Must meet OceanSITES 1.4 requirements for GDAC submission
   * - **Vocabulary Compliance**
     - All controlled vocabulary references must resolve to valid terms

.. code-block:: python

   from amocatlas.validation import validate_AC_proposed
   
   # Comprehensive validation
   validation_result = validate_AC_proposed(
       "OS_RAPID_20040402-20240327_DPR_transports_T12H.nc",
       checks=["cf", "oceansites", "acdd", "amocatlas"]
   )
   
   if validation_result.is_valid:
       print("Dataset is fully compliant with AC1 format")
   else:
       print("Validation errors:", validation_result.errors)

8. Examples and Use Cases
------------------------

8.1 RAPID Transport Time Series Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``OS_RAPID_20040402-20240327_DPR_transports_T12H.nc``

.. code-block:: text

   netcdf OS_RAPID_20040402-20240327_DPR_transports_T12H {
   dimensions:
       TIME = UNLIMITED ; // (14600 currently)
       N_COMPONENT = 8 ;
       LATITUDE = 1 ;
       
   variables:
       double TIME(TIME) ;
           TIME:long_name = "Time" ;
           TIME:standard_name = "time" ;
           TIME:units = "seconds since 1970-01-01T00:00:00Z" ;
           TIME:calendar = "gregorian" ;
           TIME:axis = "T" ;
           
       float LATITUDE(LATITUDE) ;
           LATITUDE:long_name = "Latitude" ;
           LATITUDE:standard_name = "latitude" ;
           LATITUDE:units = "degrees_north" ;
           LATITUDE:valid_min = -90.0f ;
           LATITUDE:valid_max = 90.0f ;
           LATITUDE:axis = "Y" ;
           
       float MOC_TRANSPORT(TIME) ;
           MOC_TRANSPORT:long_name = "Maximum meridional overturning circulation transport" ;
           MOC_TRANSPORT:standard_name = "ocean_volume_transport_across_line" ;
           MOC_TRANSPORT:units = "sverdrup" ;
           MOC_TRANSPORT:coordinates = "TIME" ;
           MOC_TRANSPORT:_FillValue = NaNf ;
           MOC_TRANSPORT:vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/" ;
           
       float TRANSPORT(N_COMPONENT, TIME) ;
           TRANSPORT:long_name = "Ocean volume transport components across line" ;
           TRANSPORT:standard_name = "ocean_volume_transport_across_line" ;
           TRANSPORT:units = "sverdrup" ;
           TRANSPORT:coordinates = "TIME" ;
           TRANSPORT:_FillValue = NaNf ;
           
       string TRANSPORT_NAME(N_COMPONENT) ;
           TRANSPORT_NAME:long_name = "Transport component names" ;
           TRANSPORT_NAME:coordinates = "N_COMPONENT" ;
           
   // global attributes:
           :Conventions = "CF-1.8, OceanSITES-1.4, ACDD-1.3" ;
           :format_version = "1.4" ;
           :data_type = "OceanSITES time-series data" ;
           :featureType = "timeSeries" ;
           :data_mode = "D" ;
           :site_code = "RAPID" ;
           :array = "RAPID" ;
           :platform_code = "RAPID26N" ;
           :naming_authority = "AMOCatlas" ;
           :id = "OS_RAPID_20040402-20240327_DPR_transports_T12H" ;
           :title = "RAPID-MOCHA Transport Time Series at 26°N" ;
           :summary = "Meridional overturning circulation and component transports from the RAPID mooring array at 26°N in the Atlantic Ocean. Data processed to 12-hourly resolution with comprehensive quality control." ;
           :geospatial_lat_min = 26.0 ;
           :geospatial_lat_max = 26.5 ;
           :geospatial_lon_min = -80.0 ;
           :geospatial_lon_max = -13.0 ;
           :time_coverage_start = "2004-04-02T00:00:00Z" ;
           :time_coverage_end = "2024-03-27T23:59:59Z" ;
           :contributor_name = "Dr. David Smeed, Dr. Molly Baringer" ;
           :contributor_email = "david.smeed@noc.ac.uk, molly.baringer@noaa.gov" ;
           :contributor_role = "principalInvestigator, principalInvestigator" ;
           :source_acknowledgement = "RAPID data were collected and made freely available by the RAPID program and the national programs that contribute to it" ;
           :source_doi = "https://doi.org/10.5285/8cd7e7bb-9a20-05d8-e053-6c86abc012c2" ;
           :amocatlas_version = "0.3.0" ;
           :date_created = "2025-01-15T10:30:00Z" ;
           :history = "2025-01-15T10:30:00Z: Converted to AC1 using amocatlas v0.3.0" ;
   }


9. Reference Tables
-------------------

9.1 UDUNITS-2 Compliance
~~~~~~~~~~~~~~~~~~~~~~~~

All units must follow the `UDUNITS-2 standard <https://docs.unidata.ucar.edu/udunits/current/#Database>`_ for maximum compatibility and interoperability.

.. list-table:: Unit Specifications for AC1 Format
   :widths: 25 25 50
   :header-rows: 1

   * - Quantity
     - UDUNITS Format
     - Notes
   * - **Coordinates**
     - 
     - 
   * - Time
     - ``seconds since 1970-01-01T00:00:00Z``
     - ISO 8601 epoch reference (Unix timestamp)
   * - Latitude
     - ``degree_north``
     - UDUNITS-2 standard (singular form)
   * - Longitude
     - ``degree_east``
     - UDUNITS-2 standard (singular form)
   * - Depth
     - ``m``
     - Standard SI unit, positive downward
   * - Pressure
     - ``dbar``
     - Standard oceanographic unit (decibars)
   * - Density
     - ``kg m-3``
     - SI derived unit for sigma coordinates
   * - **Physical Variables**
     - 
     - 
   * - Temperature
     - ``degree_Celsius``
     - Preferred over ``degC`` (full spelling)
   * - Salinity
     - ``1``
     - Dimensionless (practical salinity scale)
   * - Velocity
     - ``m s-1``
     - SI derived unit (not ``m/s``)
   * - **Transport Variables**
     - 
     - 
   * - Ocean Volume Transport
     - ``sverdrup``
     - 1 sverdrup = 10^6 m³/s (avoid ``Sv`` confusion)
   * - Heat Transport
     - ``petawatt``
     - 1 PW = 10^15 W (preferred over ``W`` with scale factors)
   * - Freshwater Transport
     - ``sverdrup``
     - Same as volume transport

.. warning::
   Use lowercase ``sverdrup`` (not ``Sv``) to avoid confusion with the sievert radiation unit. UDUNITS-2 recognizes ``sverdrup`` as the standard oceanographic transport unit.

9.2 OceanSITES Reference table 1: data_type
~~~~~~~~~~~~~~~~~~~~~~~~

The data_type global attribute should have one of the valid values listed here.

.. list-table:: Data Type Values
   :widths: 100
   :header-rows: 1

   * - Data type
   * - OceanSITES profile data
   * - OceanSITES time-series data
   * - OceanSITES trajectory data

9.3 OceanSITES Reference table 2: QC_indicator
~~~~~~~~~~~~~~~~~~~~~~~~

The quality control flags indicate the data quality of the data values in a file. The byte codes in column 1 are used only in the <PARAM>_QC variables to describe the quality of each measurement, the strings in column 2 ('meaning') are used in the attribute <PARAM>:QC_indicator to describe the overall quality of the parameter.

When the numeric codes are used, the flag_values and flag_meanings attributes are required and should contain lists of the codes (comma-separated) and their meanings (space separated, replacing spaces within each meaning by '_').

.. list-table:: QC Flag Values
   :widths: 10 30 60
   :header-rows: 1

   * - Code
     - Meaning
     - Comment
   * - 0
     - unknown
     - No QC was performed
   * - 1
     - good data
     - All QC tests passed.
   * - 2
     - probably good data
     - 
   * - 3
     - potentially correctable bad data
     - These data are not to be used without scientific correction or re-calibration.
   * - 4
     - bad data
     - Data have failed one or more tests.
   * - 5
     - -
     - Not used
   * - 6
     - -
     - Not used.
   * - 7
     - nominal value
     - Data were not observed but reported. (e.g. instrument target depth.)
   * - 8
     - interpolated value
     - Missing data may be interpolated from neighboring data in space or time.
   * - 9
     - missing value
     - This is a fill value

.. _oceansites-processing-levels:

9.4 OceanSITES Reference table 3: Processing level
~~~~~~~~~~~~~~~~~~~~~~~~

This table describes the quality control and other processing procedures applied to all the measurements of a variable. The string values are used as an overall indicator (i.e. one summarizing all measurements) in the attributes of each variable in the processing_level attribute.

.. list-table:: Processing Level Values
   :widths: 100
   :header-rows: 1

   * - Processing Level
   * - Raw instrument data
   * - Instrument data that has been converted to geophysical values
   * - Post-recovery calibrations have been applied
   * - Data has been scaled using contextual information
   * - Known bad data has been replaced with null values
   * - Known bad data has been replaced with values based on surrounding data
   * - Ranges applied, bad data flagged
   * - Data interpolated
   * - Data manually reviewed
   * - Data verified against model or other contextual information
   * - Other QC process applied

9.5 OceanSITES Reference table 4: Data mode
~~~~~~~~~~~~~~~~~~~~~~~~

The values for the variables "<PARAM>_DM", the global attribute "data_mode", and variable attributes "<PARAM>:DM_indicator" are defined as follows:

.. list-table:: Data Mode Values
   :widths: 10 20 70
   :header-rows: 1

   * - Value
     - Meaning
     - Description
   * - R
     - Real-time data
     - Data coming from the (typically remote) platform through a communication channel without physical access to the instruments, disassembly or recovery of the platform. Example: for a mooring with a radio communication, this would be data obtained through the radio.
   * - P
     - Provisional data
     - Data obtained after instruments have been recovered or serviced; some calibrations or editing may have been done, but the data is not thought to be fully processed. Refer to the history attribute for more detailed information.
   * - D
     - Delayed-mode data
     - Data published after all calibrations and quality control procedures have been applied on the internally recorded or best available original data. This is the best possible version of processed data.
   * - M
     - Mixed
     - This value is only allowed in the global attribute "data_mode" or in attributes to variables in the form "<PARAM>:DM_indicator". It indicates that the file contains data in more than one of the above states. In this case, the variable(s) <PARAM>_DM specify which data is in which data mode.


9.6 OceanSITES Reference Table 6: Identifying data variables (subset)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: OceanSITES Variable Names (subset)
   :widths: 20 80
   :header-rows: 1

   * - Parameter
     - CF Standard name or suggested Long name
   * - CDIR
     - direction_of_sea_water_velocity
   * - CNDC
     - sea_water_electrical_conductivity
   * - CSPD
     - sea_water_speed
   * - DEPTH
     - depth
   * - DOX2
     - moles_of_oxygen_per_unit_mass_in_sea_water was dissolved_oxygen
   * - DOXY
     - mass_concentration_of_oxygen_in_sea_water was dissolved_oxygen
   * - DOXY_TEMP
     - temperature_of_sensor_for_oxygen_in_sea_water
   * - DYNHT
     - dynamic_height
   * - FLU2
     - fluorescence
   * - HCSP
     - sea_water_speed
   * - HEAT
     - heat_content
   * - ISO17
     - isotherm_depth
   * - PCO2
     - surface_partial_pressure_of_carbon_dioxide_in_air
   * - PRES
     - sea_water_pressure
   * - PSAL
     - sea_water_practical_salinity
   * - TEMP
     - sea_water_temperature
   * - UCUR
     - eastward_sea_water_velocity
   * - VCUR
     - northward_sea_water_velocity

10. Metadata Requirements and YAML Integration
---------------------------------------------

10.1 Array-Specific Metadata Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Metadata are provided as enhanced YAML files for each array, defining variable mappings, unit conversions, attributes, and contributor information.

**Enhanced YAML Structure (osnap_array.yml)**:

.. code-block:: yaml

   # Array identification
   array:
     name: "OSNAP"
     site_code: "OSNAP"
     platform_code: "OSNAP60N"
     sea_area: "North Atlantic Ocean"
     
   # Spatial coverage
   geospatial:
     lat_min: 59.0
     lat_max: 61.0
     lon_min: -45.0
     lon_max: -10.0
     vertical_min: 0.0
     vertical_max: 3000.0
     
   # Contributors
   contributors:
     - name: "Susan Lozier"
       email: "susan.lozier@duke.edu"
       orcid: "https://orcid.org/0000-0002-1234-5678"
       role: "PI"
       institution: "Duke University"
       institution_ror: "https://ror.org/00py81415"
       institution_role: "operator"
       
   # Variable definitions
   variables:
     temp:
       name: TEMPERATURE
       long_name: "Sea water temperature"
       standard_name: "sea_water_temperature"
       units: "degree_Celsius"
       vocabulary: "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0335/"
       valid_min: -2.0
       valid_max: 40.0
       
     sal:
       name: SALINITY
       long_name: "Sea water practical salinity"
       standard_name: "sea_water_practical_salinity"
       units: "1"
       vocabulary: "http://vocab.nerc.ac.uk/collection/P07/current/IADIHDIJ/"
       valid_min: 0.0
       valid_max: 50.0
       
     moc_transport:
       name: MOC_TRANSPORT
       long_name: "Atlantic meridional overturning circulation transport"
       standard_name: "ocean_volume_transport_across_line"
       units: "sverdrup"
       vocabulary: "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       
   # Provenance
   provenance:
     source_acknowledgement: "OSNAP data were collected and made freely available by the OSNAP project and all the national programs that contribute to it (www.o-snap.org)"
     source_doi: "https://doi.org/10.35090/gatech/70342"
     web_link: "https://www.o-snap.org/"
     
   # Processing
   processing:
     qc_indicator: "excellent"
     processing_level: "Data verified against model or other contextual information"


11. Future Development and Extensions
------------------------------------

11.1 Planned Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~

- **Multi-Array Integration**: Support for datasets combining multiple arrays
- **Real-Time Data Streams**: Extensions for operational oceanography
- **Machine-Readable Provenance**: Integration with Research Data Alliance metadata standards
- **Cloud-Optimized Formats**: Zarr and COG variants for cloud computing

11.2 Community Integration
~~~~~~~~~~~~~~~~~~~~~~~~~

AC1 format is designed for:

- **OceanSITES GDAC Submission**: Full compliance for global data archive
- **CMIP Integration**: Compatible with climate model evaluation workflows
- **ARGO Coordination**: Harmonized with autonomous profiling float data standards
- **Regional Programs**: Adaptable for other ocean observing arrays globally

12. Summary and Recommendations
-------------------------------

The AC1 format represents the next evolution of AMOCatlas data standardization, combining the proven AC1 implementation with comprehensive international standards compliance. Key benefits include:

**For Data Providers**:
- Simplified workflow for OceanSITES GDAC submission
- Enhanced discoverability through rich metadata
- Maintained compatibility with existing tools

**For Data Users**:
- Consistent interface across all AMOC arrays
- Full metadata for proper data citation and attribution
- Guaranteed interoperability with international tools and standards

**For the Community**:
- Foundation for global AMOC data integration
- Template for other observing array programs
- Future-ready architecture for emerging requirements

We recommend adopting AC1 format for all new AMOCatlas releases while maintaining AC1 support for existing workflows. The enhanced metadata and standards compliance provide immediate value for data discovery and long-term preservation while ensuring continued scientific productivity.

---

**Project Funding:**
AC1 format development is supported by the Horizon Europe project EPOC - Explaining and Predicting the Ocean Conveyor (Grant Agreement No. 101081012).

*Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.*