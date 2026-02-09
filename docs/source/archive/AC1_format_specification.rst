AMOCatlas Format (A0.1)
======================================

.. note::
   This specification defines the **AMOCatlas Format v0.1 (AC0.1)**, a standardized data format for Atlantic Meridional Overturning Circulation (AMOC) observational datasets. AC1.0 is based on OceanSITES-1.5 with specific extensions and modifications for AMOC monitoring requirements.

Overview
--------

The AMOCatlas Format v0.1 (ACC0.1) provides a standardized framework for organizing, documenting, and distributing AMOC observational data. It builds upon established oceanographic data standards while addressing the specific needs of AMOC research and monitoring.

**Base Standards**:

- **CF-1.8**: Climate and Forecast Metadata Conventions
- **OceanSITES-1.5**: Ocean sustained interdisciplinary time series
- **ACDD-1.3**: Attribute Convention for Data Discovery

Format Identification
---------------------

Datasets following AC1.0 format are identified by the following global attributes:

.. code-block:: none

   Conventions = "CF-1.8, ACDD-1.3, OceanSITES-1.5"
   format_version = "AC1.0" 
   standard_name_vocabulary = "CF Standard Name Table v84"

Key Features of AC1.0
---------------------

Coordinate System Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Coordinate Names** (UPPERCASE):
  - **TIME**: Temporal coordinate. Since we use xarray, this is in datetime64[ns].
  - **DEPTH**: Depth below sea surface (positive downward)
  - **LATITUDE**: Geographic latitude (degrees_north)
  - **LONGITUDE**: Geographic longitude (degrees_east)
  - **PRESSURE**: Pressure coordinate (dbar)
  - **SIGMA0**: Potential density anomaly coordinate (σ₀), with reference pressure of 0 dbar
  - **SIGMA2**: Potential density anomaly coordinate (σ₂), with reference pressure of 2000 dbar

**Rationale**: Ensures consistent coordinate identification across all AMOC datasets regardless of source format (lat, latitude, pres, sigmatheta).

Variable Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Transport Variables** (TRANS prefix):
  - Pattern: ``TRANS_{component}`` or ``TRANS_{depth1}_{depth2}``
  - Examples: ``TRANS_EKMAN``, ``TRANS_FC``, ``TRANS_0_800``
  - Units: ``Sverdrup`` (full spelling to avoid confusion with sievert)

**Overturning Variables**:
For the MOC, the variable of "MOC" implies the overturning in depth coordinates, while "MOC_SIGMA0" or "MOC_SIGMA2" indicates depth coordinates.  For "MOC" in depth coordinates, the longname will be "MOC_Z".
  - ``MOC_Z``: Overturning in depth coordinates
  - ``MOC_SIGMA0``: Overturning in σ₀ density coordinates
  - ``MOC_SIGMA2``: Overturning in σ₂ density coordinates  
  - ``MOC``: Default overturning in depth coordinates
  
**Uncertainty Variables** (_ERR suffix):
  - Pattern: ``{VARIABLE}_ERR``
  - Examples: ``MOC_SIGMA0_ERR``, ``MHT_ERR``, ``MFT_WEST_ERR``
  - Units: Always identical to parent variable

**Heat/Freshwater Transport**:
  - ``MHT``: Meridional heat transport (units: ``PW``)
  - ``MFT``: Meridional freshwater transport (units: ``Sverdrup``)
  - Regional qualifiers: ``_EAST``, ``_WEST``, ``_GYRE``, ``_OT``

Note - the regional qualifiers may be updated in a later version to combine the data into a single variable with an additional "REGION" coordinate, but for now they are separate variables to match the original datasets.


Metadata Requirements
~~~~~~~~~~~~~~~~~~~~

**Required Variable Attributes**:
  - ``standard_name``: From CF-1.8 vocabulary where available
  - ``long_name``: Human-readable description
  - ``units``: UDUNITS-2 compliant units, defaulting to CF standard units apart from the exceptions above (Sverdrup, PW, degree_C, etc.)
  - ``description``: Extended description (optional but recommended)

**Required Global Attributes** (selection):
  - ``title``, ``summary``, ``source``
  - ``array``, ``id``, 
  - ``contributor_name``, ``contributor_email``, ``contributor_role``, 
  - ``format_version``, ``date_created``

Deviations from OceanSITES-1.5
------------------------------

AC1.0 modifies OceanSITES-1.5 in the following ways:

.. list-table:: Key Deviations from OceanSITES-1.5
   :header-rows: 1
   :widths: 25 35 40

   * - Aspect
     - OceanSITES-1.5/CF-1.8
     - AC1.0 Modification
   * - Transport Units
     - ``m3 s-1`` (CF standard)
     - ``Sverdrup`` (full spelling)
   * - Heat Transport Units
     - Variable (W, TW, etc.)
     - ``PW`` (petawatts)
   * - Variable Prefixes
     - Variable
     - ``TRANS_`` for transport, ``MOC_`` for overturning
   * - Standard Name Extensions
     - OceanSITES vocabulary only
     - CF-1.8 + AMOC-specific extensions


Format Validation
-----------------

AC1.0 compliance can be validated using the AMOCatlas compliance checker:

.. code-block:: python

   from amocatlas.compliance_checker import validate_ac1_format
   
   # Validate a dataset
   results = validate_ac1_format(dataset)
   
   # Check for AC1.0 compliance
   if results.is_compliant:
       print("Dataset is AC1.0 compliant")
   else:
       print("Compliance issues found:")
       for issue in results.issues:
           print(f"  - {issue}")

Version History
---------------

**AC1.0** (2026-02-08):

- Initial specification
- Based on OceanSITES-1.5 with AMOC-specific extensions
- Establishes variable naming conventions and unit standards
- Defines coordinate system requirements
- Implements uncertainty variable convention

References
----------

- **CF Conventions**: https://cfconventions.org/
- **OceanSITES**: http://www.oceansites.org/docs/oceansites_data_format_reference_manual.pdf
- **ACDD**: https://wiki.esipfed.org/ACDD
- **UDUNITS-2**: https://docs.unidata.ucar.edu/udunits/current/
- **CF Standard Names**: https://cfconventions.org/Data/cf-standard-names/current/
