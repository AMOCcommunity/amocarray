AMOCatlas AC-0.1 Manual
==========================

This document defines the AC (AMOC Community) standard data format which is an OceanSITES variant with small deviations.  This format provides interoperability between moored estimates of overturning transport from the RAPID, OSNAP, MOVE and SAMBA arrays and other data products which product ocean transports while ensuring compliance with international oceanographic data standards.  Note the deviations below (:ref:`deviations-from-oceansites`).

**Related Documentation:**

- :doc:`AC1_format` - AC-0.1 format specification (overview)
- :doc:`AC1_variables` - Variable naming conventions and standards  
- :doc:`AC1_units` - Unit definitions and conversions
- :doc:`variables` - Auto-generated variable mapping tables

This document provides the detailed implementation guide for AC-0.1, while the above documents provide quick references.

.. contents:: Table of Contents
   :local:
   :depth: 3

1. Overview & Context
---------------------

The AC-0.1 format incorporates OceanSITES-1.4 while specifying additional metadata (vocabularies) and standardised naming conventions.

The AC-0.1 format provides compliance with:

- **Standards Compliance**: Implements CF Conventions 1.8, OceanSITES-1.4, and ACDD 1.3
- **Discoverability**: Rich metadata using controlled vocabularies 
- **Workflow Integration**: Compatible with existing AMOCatlas workflows
- **International Interoperability**: Compliance with OceanSITES  
- **Provenance Tracking**: Comprehensive attribution to original data providers
- **Extensibility**: Supports future variables and array additions

1.1 Relationship to Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AC-0.1 format represents the standardization level in the AMOCatlas hierarchy:

.. code-block:: text

   Native Formats → Internal standardised → AC-0.1 Standard  
   (original)          (atlas internal)     (format_AC-0.1)    

**Compliance Framework**: AC-0.1 datasets are designed to meet:

- CF Conventions 1.8 compliance (validation tools available)
- OceanSITES-1.4 compatibility (with documented deviations as specified in :ref:`deviations-from-oceansites`)
- AMOCatlas-specific validation rules (see :mod:`amocatlas.compliance_checker`)
- ACDD-1.3 metadata structure

**Standards Integration**: The format integrates multiple international standards:

- **CF Conventions 1.8**: `Climate and Forecast metadata conventions <https://cfconventions.org/cf-conventions/cf-conventions.html>`_
- **OceanSITES-1.4**: `Ocean observing time series data format <https://ocean-uhh.github.io/oceanarray/oceanSITES_manual.html>`_
- **ACDD 1.3**: `Attribute Convention for Data Discovery <https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3>`_
- **NERC Vocabularies**: `Controlled vocabularies for oceanographic parameters <https://vocab.nerc.ac.uk/>`_

2. Key Design Decisions
-----------------------

The AC-0.1 format incorporates several design decisions that enhance interoperability while maintaining scientific accuracy and usability.

.. _deviations-from-oceansites:

2.1 Deviations from OceanSITES Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AC-0.1 implements OceanSITES-1.4 with the following deviations optimized for AMOC array data:

.. list-table:: Deviations from OceanSITES Standard
   :widths: 30 35 35
   :header-rows: 1

   * - Feature
     - OceanSITES Standard
     - AC-0.1 Format
   * - **Contributor Metadata**
     - ``creator_*``, ``principal_investigator_*``
     - ``contributor_*`` attributes (unified pattern)
   * - **Density Coordinates**
     - Depth/pressure coordinates only
     - ``SIGMA0``, ``SIGMA2`` coordinates allowed (array-specific)
   * - **Component Dimension**
     - Not specified
     - ``N_COMPONENT`` for transport decomposition
   * - **Coordinate Units**
     - ``degrees_north``, ``degrees_east``
     - ``degree_north``, ``degree_east`` (UDUNITS-2, CF-1.8 compliant)
   * - **Transport Units**
     - ``Sv`` for transport
     - ``Sverdrup`` (avoids confusion with sievert)

**Rationale for Deviations**:

- **Contributor Pattern**: Unified ``contributor_*`` approach simplifies metadata management while providing equivalent functionality
- **Sigma Coordinates**: Essential for density-based transport calculations in some arrays
- **Component Dimension**: Enables systematic representation of transport decompositions across arrays (*not yet implemented*)
- **Coordinate Units**: `UDUNITS-2 <https://docs.unidata.ucar.edu/udunits/current/#Database>`_ singular forms provide better tool compatibility than OceanSITES plural forms, also compliant with CF-1.8
- **Sverdrup Unit**: Full spelling prevents confusion with ``Sv`` (sievert radiation unit)

These deviations maintain CF compliance and ISO 8601 compatibility while optimizing for AMOC-specific scientific requirements.

3. File Organisation & Naming
-----------------------------

3.1 File Naming Convention
~~~~~~~~~~~~~~~~~~~~~~~~

Files follow the OceanSITES naming pattern with AMOC-specific modifications:

**Basic Pattern**: ``OS_[PLATFORM_CODE]_[DEPLOYMENT]_[MODE]_[PARAMS].nc``

**Components**:

- ``OS`` = OceanSITES prefix (maintains compatibility)
- ``[PLATFORM_CODE]`` = Platform identifier derived from ``processing_datasource`` (e.g., "RAPID26N", "OSNAP55N", "MOVE16N") 
- ``[DEPLOYMENT]`` = Deployment code (e.g., "20040401-20230211" for date range)
- ``[MODE]`` = Data mode: R (real-time), P (provisional), D (delayed-mode)
- ``[PARAMS]`` = Parameter identifier (e.g., "transports_T12H", "sections_T1M")

**Examples**:

- ``OS_RAPID26N_20040401-20230211_D_transports_T12H.nc`` - Delayed-mode transport data
- ``OS_OSNAP55N_20140801-20200601_D_sections_T1M.nc`` - Delayed-mode section data
- ``OS_MOVE16N_20040201-20181201_D_transports_T12H.nc`` - Delayed-mode transport data

**Reference**: See OceanSITES file naming in "4.1.1 Deployment Data files Naming Convention" of the OceanSITES manual (https://ocean-uhh.github.io/oceanarray/oceanSITES_manual.html#data-files).




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
   * - ``platform_code``
     - "RAPID26N"
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
     - "io.github.amoccommunity"
     - Authority providing the dataset ID
     - Reverse DNS recommended
     - *S*
   * - ``id``
     - "OS_RAPID26N_20040402-20240327_DPR_transports_T12H"
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
     - "Jane Doe, John Smith"
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
     - "originator, principalInvestigator"
     - Roles (aligned with names)
     - NERC G04
     - **M**
   * - ``contributor_role_vocabulary``
     - "https://vocab.nerc.ac.uk/collection/G04/current/"
     - Vocabulary for contributor roles
     - Standards reference
     - **M**
   * - ``contributing_institutions``
     - "University of Hamburg (IfM), National Oceanography Centre (Southampton)"
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
     - "https://vocab.nerc.ac.uk/collection/W08/current/" or "https://vocab.nerc.ac.uk/collection/G04/current/"
     - Vocabulary for institutional roles
     - Standards reference
     - **M**


**Standard Contributor Roles (NERC G04):** ``originator``, ``principalInvestigator``, ``author``, ``coAuthor``, ``contributor``, ``publisher``, ``custodian``, ``owner``, ``pointOfContact``



.. list-table:: Provenance and Source Attribution
   :widths: 20 25 40 10 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - Format
     - RS
   * - ``acknowledgment``
     - "RAPID data collected and made freely available by the RAPID program..."
     - Attribution to original data providers (comma-separated)
     - Free text
     - **M**
   * - ``doi``
     - "https://doi.org/10.35090/gatech/70342, https://doi.org/10.1029/2018GL077408"
     - DOIs of source datasets (comma-separated)
     - DOI URLs
     - **M**
   * - ``processing_version``
     - "0.2.0"
     - Version of processing software used
     - Semantic version
     - **M**
   * - ``weblink``
     - "https://www.rapid.ac.uk/, https://www.o-snap.org/"
     - Links to project websites (comma-separated)
     - URLs
     - *S*
   * - ``start_date``
     - "2004-04-02T00:00:00Z"
     - Overall dataset start time
     - ISO 8601
     - **M**





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
     - "degree_north"
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
     - "degree_east"
     - Longitude units
     - UDUNITS-2
     - *S*
   * - ``geospatial_vertical_min``
     - 0.0
     - Minimum depth/height
     - meters
     - **M**
   * - ``geospatial_vertical_max``
     - 5000.0
     - Maximum depth/height
     - meters
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
    - `SeaVoX C19 <https://vocab.nerc.ac.uk/collection/C19/current/>`_
     - *S*


Time Format Rationale: The compact YYYY-mm-ddTHH:MM:ssZ format reduces attribute string length while maintaining human readability and ISO 8601 compatibility.

File dates: The file dates, date_created and date_modified, are our interpretation of the file dates as defined by ACDD. Date_created is the time stamp on the original dataset, date_modified may be used when e.g. metadata is added or the file format is updated.

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
    * - ``references``
     - "http://www.oceansites.org, https://doi.org/10.1029/2018GL077408"
     - Relevant publications and resources (comma-separated)
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
   * - ``acknowledgment``
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
     - "timeSeries" or "timeSeriesProfile"
     - CF discrete sampling geometry type
     - CF Standard
     - **M**
   * - ``data_type``
     - "OceanSITES time-series data"
     - OceanSITES data type classification
     - OceanSITES Standard
     - **M**
   * - ``format_version``
     - "AC-0.1"
     - AMOCatlas format version
     - Version string
     - **M**
   * - ``Conventions``
     - "CF-1.8, OceanSITES-1.4, ACDD-1.3"
     - Metadata conventions followed
     - Standards list
     - *S*
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
     - ``DEPTH``, ``PRESSURE``, ``SIGMA0``, ``SIGMA2``
     - Vertical coordinates (optional)
   * - **Horizontal**
     - ``LATITUDE``, ``LONGITUDE``, ``LATITUDE_BOUNDS``, ``LONGITUDE_BOUNDS``
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
       
       **Attributes**:

       - long_name = "Time"
       - standard_name = "time"
       - units = "seconds since 1970-01-01T00:00:00Z" (datetime64[ns])
       - calendar = "gregorian"
       - axis = "T"
     - **M**
   * - ``LATITUDE``
     - scalar or ``LATITUDE``
     - **Data Type**: float32
       
       **Attributes**:

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
       
       **Attributes**:

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
       
       **Attributes**:

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
       
       **Attributes**:

       - long_name = "Pressure"
       - standard_name = "sea_water_pressure"
       - units = "dbar"
       - positive = "down"
       - valid_min = 0.0
       - axis = "Z"
     - *S*
   * - ``SIGMA0``
     - ``SIGMA0``
     - **Data Type**: float32
       
       **Attributes**:

       - long_name = "sigma0"
       - standard_name = "sea_water_sigma_theta"
       - units = "kg m-3"
       - axis = "Z"
       - reference_pressure = 0.0 
     - *S*
   * - ``SIGMA2``
     - ``SIGMA2``
     - **Data Type**: float32
      
       **Attributes**:

       - long_name = "sigma2"
       - standard_name = "sea_water_sigma2"
       - units = "kg m-3"
       - axis = "Z"
       - reference_pressure = 2000.0 
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
   * - ``MOC``
       
       - **Data Type**: float32
       
       - **Dimensions**: ``TIME``
     - - long_name = "MOC_z" 
       - standard_name = "ocean_meridional_overturning_streamfunction"
       - units = "Sverdrup"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0466/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -50.0 (optional)
       - valid_max = 50.0 (optional)
     - *HD*
   * - ``MOC_SIGMA0`` or ``MOC_SIGMA2``
       
       - **Data Type**: float32
       
       - **Dimensions**: ``TIME``
     - - long_name =  "MOC_sigma0" or "MOC_sigma2" (depending on vertical coordinate used)
       - standard_name = "ocean_meridional_overturning_streamfunction"
       - units = "Sverdrup"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0466/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, SIGMA0" or "SIGMA2" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -50.0 (optional)
       - valid_max = 50.0 (optional)
     - *HD*
   * - ``TRANS_*``
       
       - **Data Type**: float32

       - **Dimensions**: ``N_COMPONENT``, ``TIME``
     - - long_name = "Transport"
       - standard_name = "ocean_volume_transport_across_line"
       - units = "Sverdrup"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
     - *HD*
   * - ``MHT``
       
       - **Data Type**: float32

       - **Dimensions**: ``TIME``
     - - long_name = "MHT"
       - standard_name = "northward_ocean_heat_transport"
       - units = "PW"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0483/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -5.0 (optional)
       - valid_max = 5.0 (optional)
     - *S*
   * - ``MHT_GYRE``

       - **Data Type**: float32

       - **Dimensions**: ``TIME``
     - - long_name = "MHT_gyre"
       - standard_name = "northward_ocean_heat_transport_due_to_gyre"
       - units = "PW"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0486/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -5.0 (optional)
       - valid_max = 5.0 (optional)
     - *S*
   * - ``MHT_OT``

       - **Data Type**: float32

       - **Dimensions**: ``TIME``
     - - long_name = "MHT_ot"
       - standard_name = "northward_ocean_heat_transport_due_to_overturning"
       - units = "PW"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0487/"
       - coordinates = "TIME, LONGITUDE, LATITUDE, DEPTH" (required if variable does not have 4 coordinates in its definition)
       - _FillValue = NaNf
       - valid_min = -5.0 (optional)
       - valid_max = 5.0 (optional)
     - *S*
   * - ``MFT``

       - **Data Type**: float32

       - **Dimensions**: ``TIME`` 
     - - long_name = "MFT"
       - standard_name = "northward_ocean_freshwater_transport"
       - units = "Sverdrup"
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
        - units = "degree_C"
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
   * - ``POTEMP``
     - data type: float32
       
       dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     - **Attributes**:
       
       - long_name = "theta"
       - standard_name = "sea_water_potential_temperature"
       - units = "degree_C"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0329/"
       - valid_min = -2.0
       - valid_max = 40.0
       - _FillValue = NaNf
       - ancillary_variables = "POTEMP_QC"
       - coordinates = "TIME, DEPTH, LATITUDE, LONGITUDE"
     - *HD*
   * - ``CT``
     - data type: float32
       
       dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     - **Attributes**:
       
       - long_name = "CT"
       - standard_name = "sea_water_conservative_temperature"
       - units = "degree_C"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/IFEDAFIE/"
       - valid_min = -2.0
       - valid_max = 40.0
       - _FillValue = NaNf
       - ancillary_variables = "CT_QC"
       - coordinates = "TIME, DEPTH, LATITUDE, LONGITUDE"
     - *HD*
   * - ``SA``
     - data type: float32
       
       dimensions: (``TIME``, ``DEPTH``, ``LATITUDE``, ``LONGITUDE``)
     - **Attributes**:
       
       - long_name = "SA"
       - standard_name = "sea_water_absolute_salinity"
       - units = "g kg-1"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/JIBGDIEJ/"
       - valid_min = 0.0
       - valid_max = 50.0
       - _FillValue = NaNf
       - ancillary_variables = "SA_QC"
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
       
       **Attributes**:
       
       - long_name = "Quality flag for <parameter_name>"
       - flag_values = [0, 1, 2, 3, 4, 7, 8, 9]
       - flag_meanings = "unknown good_data probably_good_data potentially_correctable_bad_data bad_data nominal_value interpolated_value missing_value"
       - valid_min = 0
       - valid_max = 9
     - *S*
   * - ``<PARAM>_UNCERTAINTY``
     - Same as parent variable
     - **Data Type**: float32
       
       **Attributes**:
       
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
     - ``degree_C``
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
   :widths: 20 50 20
   :header-rows: 1

   * - Parameter
     - CF Standard name or suggested Long name
     - AC1 Variable Name
   * - CDIR
     - direction_of_sea_water_velocity
     - CDIR
   * - CNDC
     - sea_water_electrical_conductivity
     - CNDC
   * - CSPD
     - sea_water_speed
     - CSPD
   * - DEPTH
     - depth
     - DEPTH
   * - DOX2
     - moles_of_oxygen_per_unit_mass_in_sea_water was dissolved_oxygen
     - DOX2
   * - DOXY
     - mass_concentration_of_oxygen_in_sea_water was dissolved_oxygen
     - DOXY
   * - DOXY_TEMP
     - temperature_of_sensor_for_oxygen_in_sea_water
     - DOXY_TEMP
   * - DYNHT
     - dynamic_height
     - DYNHT
   * - FLU2
     - fluorescence
     - FLU2
   * - HCSP
     - sea_water_speed
     - HCSP
   * - HEAT
     - heat_content
     - HEAT
   * - ISO17
     - isotherm_depth
     - ISO17
   * - PCO2
     - surface_partial_pressure_of_carbon_dioxide_in_air
     - PCO2
   * - PRES
     - sea_water_pressure
     - PRESSURE
   * - PSAL
     - sea_water_practical_salinity
     - PSAL
   * - TEMP
     - sea_water_temperature
     - TEMP
   * - UCUR
     - eastward_sea_water_velocity
     - UCUR
   * - VCUR
     - northward_sea_water_velocity
     - VCUR

11. Future Development and Extensions
------------------------------------

- **Multi-Array Integration**: Support for datasets combining multiple arrays
- **Real-Time Data Streams**: Extensions for operational oceanography
- **Machine-Readable Provenance**: Integration with Research Data Alliance metadata standards
- **Cloud-Optimized Formats**: Zarr and COG variants for cloud computing


---

**Project Funding:**
AC1 format development is supported by the Horizon Europe project EPOC - Explaining and Predicting the Ocean Conveyor (Grant Agreement No. 101081012).

*Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.*