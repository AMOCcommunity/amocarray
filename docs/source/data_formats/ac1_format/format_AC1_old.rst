AMOCatlas Format AC1
====================

This document defines the AC1 standard data format produced by the ``amocatlas.convert.to_AC1()`` function. This format is designed to provide consistency between moored estimates of overturning transport, as from the RAPID, OSNAP, MOVE and SAMBA arrays.

**Relationship to Other Format Documents:**

- :doc:`format_orig` - Documents native data formats from each array
- :doc:`format_conversion` - Describes conversion strategies from native to standardized formats  
- :doc:`format_oceanSITES` - Details OceanSITES compliance requirements
- **This document (format_AC1)** - Specifies the final standardized output format

1. Overview
-----------

The AC1 format enhances interoperability for Atlantic Meridional Overturning Circulation (AMOC) mooring array datasets. It uses NetCDF4 format with ``xarray.Dataset`` objects and is derived from the OceanSITES data format v1.4, with enhanced vocabulary specifications for AMOC-specific variables.

1.1 Design Principles
~~~~~~~~~~~~~~~~~~~~~

The AC1 format follows these core principles:

- **Standards Compliance**: Built on CF Conventions 1.8, OceanSITES 1.4, and ACDD 1.3
- **Controlled Vocabularies**: Uses NERC vocabulary services where available
- **Provenance Tracking**: Maintains full attribution to original data providers
- **Extensibility**: Supports future variables and array additions

1.2 Format Hierarchy
~~~~~~~~~~~~~~~~~~~~

The AC1 format sits at the top of the AMOCatlas data processing hierarchy:

.. code-block:: text

   Native Formats → OceanSITES Compatible → AC1 Standard
   (format_orig)    (format_oceanSITES)     (format_AC1)

1.3 Compliance Framework
~~~~~~~~~~~~~~~~~~~~~~~~

All AC1 datasets must pass:

- CF Checker validation
- OceanSITES format compliance
- AMOCatlas-specific validation rules

1.4 Deviations from OceanSITES Standard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   The following choices differ from referenced standards and may need future revision based on community feedback.

The AC1 format follows oceanarray conventions and includes these deviations from OceanSITES:

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
   * - Contributor metadata
     - ``creator_*``, ``principal_investigator_*``
     - ``contributor_*`` attributes only
   * - Density coordinates
     - Depth/pressure coordinates only
     - ``SIGMA0`` coordinate allowed (array-specific)

.. note::
   These deviations maintain ISO 8601 compatibility while reducing attribute string length and following established oceanarray patterns.

2. File Specification
---------------------

2.1 Technical Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: File Format Requirements
   :widths: 25 75
   :header-rows: 1

   * - Property
     - Specification
   * - **File Format**
     - NetCDF4 Classic
   * - **Data Structure**
     - ``xarray.Dataset`` compatible
   * - **Conventions**
     - CF-1.8, OceanSITES-1.4, ACDD-1.3
   * - **Compression**
     - Level 6 deflate compression (default)
   * - **Chunking**
     - TIME dimension chunked for optimal access

2.2 Dimension Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~

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

3. Variable Specification
-------------------------

3.1 Coordinate Variables
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Coordinate Variables
   :widths: 15 20 55 10
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
       - units = "seconds since 1970-01-01T00:00:00Z"
       - calendar = "gregorian"
       - axis = "T"
     - **M**
   * - ``LATITUDE``
     - scalar or ``N_PROF``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Latitude"
       - standard_name = "latitude"
       - units = "degrees_north"
       - valid_min = -90.0
       - valid_max = 90.0
       - axis = "Y"
     - *HD*
   * - ``LONGITUDE``
     - scalar or ``N_PROF``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Longitude"
       - standard_name = "longitude"
       - units = "degrees_east"
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
       - long_name = "Sea water pressure"
       - standard_name = "sea_water_pressure"
       - units = "dbar"
       - positive = "down"
       - valid_min = 0.0
       - axis = "Z"
     - *S*

3.2 Transport Variables
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Transport Variables
   :widths: 15 20 55 10
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
     - RS
   * - ``MOC_TRANSPORT``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Maximum meridional overturning circulation transport"
       - standard_name = "ocean_volume_transport_across_line"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/W946809H/"
       - units = "sverdrup"
       - coordinates = "TIME"
       - _FillValue = NaNf
     - *HD*
   * - ``HEAT_TRANSPORT``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Northward ocean heat transport"
       - standard_name = "northward_ocean_heat_transport"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0483/"
       - units = "petawatt"
       - coordinates = "TIME"
       - _FillValue = NaNf
     - *S*
   * - ``FRESHWATER_TRANSPORT``
     - ``TIME``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Northward ocean freshwater transport"
       - standard_name = "northward_ocean_freshwater_transport"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0507/"
       - units = "sverdrup"
       - coordinates = "TIME"
       - _FillValue = NaNf
     - *S*

3.3 Hydrographic Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Hydrographic Variables
   :widths: 15 20 55 10
   :header-rows: 1

   * - Variable
     - Dimension
     - Attributes and Requirements
     - RS
   * - ``TEMPERATURE``
     - ``TIME, DEPTH, ...``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Sea water temperature"
       - standard_name = "sea_water_temperature"
       - vocabulary = "https://vocab.nerc.ac.uk/collection/P07/current/CFSN0335/"
       - units = "degree_Celsius"
       - coordinates = "TIME DEPTH LATITUDE LONGITUDE"
       - _FillValue = NaNf
       - valid_min = -2.0
       - valid_max = 40.0
     - *S*
   * - ``SALINITY``
     - ``TIME, DEPTH, ...``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Sea water practical salinity"
       - standard_name = "sea_water_practical_salinity"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/IADIHDIJ/"
       - units = "1"
       - coordinates = "TIME DEPTH LATITUDE LONGITUDE"
       - _FillValue = NaNf
       - valid_min = 0.0
       - valid_max = 50.0
     - *S*
   * - ``VELOCITY_MERIDIONAL``
     - ``TIME, DEPTH, ...``
     - **Data Type**: float32
       
       **Attributes**:
       - long_name = "Northward sea water velocity"
       - standard_name = "northward_sea_water_velocity"
       - vocabulary = "http://vocab.nerc.ac.uk/collection/P07/current/CFSN0494/"
       - units = "m s-1"
       - coordinates = "TIME DEPTH LATITUDE LONGITUDE"
       - _FillValue = NaNf
     - *S*

.. note::
   **Requirement Status**: **M** = Mandatory, *HD* = Highly Desired, *S* = Suggested

4. Units
--------

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
     - ISO 8601 epoch reference
   * - Latitude
     - ``degrees_north``
     - **[DEVIATION]** OceanSITES uses ``degrees_north`` (plural)
   * - Longitude
     - ``degrees_east``
     - **[DEVIATION]** OceanSITES uses ``degrees_east`` (plural)
   * - Depth
     - ``m``
     - Standard SI unit, positive downward
   * - Pressure
     - ``dbar``
     - Standard oceanographic unit (decibars)
   * - **Physical Variables**
     - 
     - 
   * - Temperature
     - ``degree_Celsius``
     - Preferred over ``degC``
   * - Salinity
     - ``1``
     - Dimensionless (practical salinity)
   * - Velocity
     - ``m s-1``
     - SI derived unit
   * - **Transport Variables**
     - 
     - 
   * - Ocean Volume Transport
     - ``sverdrup``
     - 1 sverdrup = 10^6 m³/s (avoid ``Sv`` to prevent confusion with sievert)
   * - Heat Transport
     - ``petawatt``
     - 1 PW = 10^15 W
   * - Freshwater Transport
     - ``sverdrup``
     - Same as volume transport

.. warning::
   Use lowercase ``sverdrup`` (not ``Sv``) to avoid confusion with the sievert radiation unit. UDUNITS-2 recognizes ``sverdrup`` as the standard oceanographic transport unit.

5. Global Attributes
--------------------

.. list-table:: Global Attributes
   :widths: 20 20 25 5
   :header-rows: 1

   * - Attribute
     - Example
     - Description
     - RS
   * - title
     - "RAPID-MOCHA Transport Time Series"
     - Descriptive dataset title
     - **M**
   * - platform
     - "moorings"
     - Type of platform
     - **M**
   * - platform_vocabulary
     - "https://vocab.nerc.ac.uk/collection/L06/current/"
     - Controlled vocab for platform types
     - **M**
   * - featureType
     - "timeSeries"
     - NetCDF featureType
     - **M**
   * - id
     - "RAPID_20231231_<orig>.nc"
     - Unique file identifier
     - **M**
   * - contributor_name
     - "Dr. Jane Doe"
     - Name of dataset PI
     - **M**
   * - contributor_email
     - "jane.doe@example.org"
     - Email of dataset PI
     - **M**
   * - contributor_id
     - "ORCID:0000-0002-1825-0097"
     - Identifier (e.g., ORCID)
     - HD
   * - contributor_role
     - "principalInvestigator"
     - Role using controlled vocab
     - **M**
   * - contributor_role_vocabulary
     - "http://vocab.nerc.ac.uk/search_nvs/W08/"
     - Role vocab reference
     - **M**
   * - contributing_institutions
     - "University of Hamburg"
     - Responsible org(s)
     - **M**
   * - contributing_institutions_vocabulary
     - "https://ror.org/012tb2g32"
     - Institutional ID vocab (e.g. ROR, EDMO)
     - HD
   * - contributing_institutions_role
     - "operator"
     - Role of institution
     - **M**
   * - contributing_institutions_role_vocabulary
     - "https://vocab.nerc.ac.uk/collection/W08/current/"
     - Vocabulary for institution roles
     - **M**
   * - source_acknowledgement
     - "...text..."
     - Attribution to original dataset providers
     - **M**
   * - source_doi
     - "https://doi.org/..."
     - Semicolon-separated DOIs of original datasets
     - **M**
   * - amocatlas_version
     - "0.2.1"
     - Version of amocatlas used
     - **M**
   * - web_link
     - "http://project.example.org"
     - Semicolon-separated URLs for more information
     - S
   * - start_date
     - "20230301T000000"
     - Overall dataset start time (UTC)
     - **M**
   * - date_created
     - "20240419T130000"
     - File creation time (UTC, zero-filled as needed)
     - **M**

5. Variable Attributes
----------------------

.. list-table:: Variable Attributes
   :widths: 20 60 5
   :header-rows: 1

   * - Attribute
     - Description
     - RS
   * - long_name
     - Descriptive name of the variable
     - **M**
   * - standard_name
     - CF-compliant standard name (if available)
     - **M**
   * - vocabulary
     - Controlled vocabulary identifier
     - HD
   * - _FillValue
     - Fill value, same dtype as variable
     - **M**
   * - units
     - Physical units (e.g., m/s, degree_Celsius)
     - **M**
   * - coordinates
     - Comma-separated coordinate list (e.g., "TIME, DEPTH")
     - **M**

6. Metadata Requirements
------------------------

Metadata are provided as YAML files for each array. These define variable mappings, unit conversions, and attributes to attach during standardisation.

Example YAML (osnap_array.yml):

.. code-block:: yaml

   variables:
     temp:
       name: TEMPERATURE
       units: degree_Celsius
       long_name: In situ temperature
       standard_name: sea_water_temperature

     sal:
       name: SALINITY
       units: g/kg
       long_name: Practical salinity
       standard_name: sea_water_practical_salinity

     uvel:
       name: U
       units: m/s
       long_name: Zonal velocity
       standard_name: eastward_sea_water_velocity

7. Validation Rules
-------------------

- All datasets must include the TIME coordinate.
- At least one of: TEMPERATURE, SALINITY, TRANSPORT, U, V must be present.
- Global attribute array_name must match one of: ["move", "rapid", "osnap", "samba"].
- File must pass CF-check where possible.

8. Examples
-----------

YAML input: see metadata/osnap_array.yml

Resulting NetCDF Header (excerpt):

.. code-block:: text

   dimensions:
       TIME = 384
       DEPTH = 4

   variables:
       float32 TEMPERATURE(TIME, DEPTH)
           long_name = "In situ temperature"
           standard_name = "sea_water_temperature"
           units = "degree_Celsius"
       ...

   global attributes:
       :title = "OSNAP Array Transport Data"
       :institution = "AWI / University of Hamburg"
       :array_name = "osnap"
       :Conventions = "CF-1.8"

9. Conversion Tool
------------------

To produce AC1-compliant datasets from raw standardised inputs, use:

.. code-block:: python

   from amocatlas.convert import to_AC1
   ds_ac1 = to_AC1(ds_std)

This function:

- Validates standardised input
- Adds metadata from YAML
- Ensures output complies with AC1 format

10. Notes
---------

- Format is extensible for future variables or conventions
- Please cite amocatlas and relevant data providers when using AC1-formatted datasets

11. Provenance and Attribution
------------------------------

To ensure transparency and appropriate credit to original data providers, the AC1 format includes structured global attributes for data provenance.

**Project Funding:**
AC1 format development is supported by the Horizon Europe project EPOC - Explaining and Predicting the Ocean Conveyor (Grant Agreement No. 101081012).

*Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.*

Required Provenance Fields:

.. list-table::
   :widths: 30 60
   :header-rows: 1

   * - Attribute
     - Purpose
   * - source
     - Semicolon-separated list of original dataset short names
   * - source_doi
     - Semicolon-separated list of DOIs for original data
   * - source_acknowledgement
     - Semicolon-separated list of attribution statements
   * - history
     - Auto-generated history log with timestamp and tool version
   * - amocatlas_version
     - Version of amocatlas used for conversion
   * - generated_doi
     - DOI assigned to the converted AC1 dataset (optional)

Example:

.. code-block:: text

   :source = "OSNAP; SAMBA"
   :source_doi = "https://doi.org/10.35090/gatech/70342; https://doi.org/10.1029/2018GL077408"
   :source_acknowledgement = "OSNAP data were collected and made freely available by the OSNAP project and all the national programs that contribute to it (www.o-snap.org); M. Kersalé et al., Highly variable upper and abyssal overturning cells in the South Atlantic. Sci. Adv. 6, eaba7573 (2020). DOI: 10.1126/sciadv.aba7573"
   :history = "2025-04-19T13:42Z: Converted to AC1 using amocatlas v0.2.1"
   :amocatlas_version = "0.2.1"
   :generated_doi = "https://doi.org/10.xxxx/amocatlas-ac1-2025"

YAML Integration (optional):

.. code-block:: yaml

   metadata:
     citation:
       doi: "https://doi.org/10.1029/2018GL077408"
       acknowledgement: >
         M. Kersalé et al., Highly variable upper and abyssal overturning cells in the South Atlantic.
         Sci. Adv. 6, eaba7573 (2020). DOI: 10.1126/sciadv.aba7573
