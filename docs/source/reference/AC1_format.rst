Overview (Draft)
======================================

.. note::
   This specification defines the **AMOCatlas Format v0.1 (AC-0.1)**, a standardized data format for Atlantic Meridional Overturning Circulation (AMOC) observational datasets. AC-0.1 is based on OceanSITES-1.5 with specific extensions and modifications for AMOC monitoring requirements.

The AMOCatlas Format v0.1 (AC-0.1) provides a standardized framework for organizing, documenting, and distributing AMOC observational data. It builds upon established oceanographic data standards while addressing the specific needs of AMOC research and monitoring.

**Base Standards**:

- **CF-1.8**: Climate and Forecast Metadata Conventions
- **OceanSITES-1.5**: Ocean sustained interdisciplinary time series
- **ACDD-1.3**: Attribute Convention for Data Discovery

**Documentation Structure**:

This format specification is supported by detailed reference documentation:

- :doc:`AC1_variables`: Comprehensive variable naming conventions and metadata standards
- :doc:`AC1_units`: UDUNITS-2 compliant unit definitions with AMOC-specific extensions
- :doc:`variables`: Auto-generated variable mapping tables from standardized datasets

Format Identification
---------------------

Datasets following AC-0.1 format are identified by the following global attributes:

.. code-block:: none

   Conventions = "CF-1.8, ACDD-1.3, OceanSITES-1.5"
   format_version = "AC-0.1" 
   standard_name_vocabulary = "CF Standard Name Table v84"

Key Features
------------

Coordinate System Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Coordinate Names** (UPPERCASE):
  - **TIME**: Temporal coordinate (datetime64[ns] in xarray)
  - **DEPTH**: Depth below sea surface (positive downward, units: m)
  - **LATITUDE**: Geographic latitude (units: degree_north)
  - **LONGITUDE**: Geographic longitude (units: degree_east)
  - **PRESSURE**: Pressure coordinate (units: dbar)
  - **SIGMA0**: Potential density anomaly coordinate (σ₀, reference_pressure: 0 dbar)
  - **SIGMA2**: Potential density anomaly coordinate (σ₂, reference_pressure: 2000 dbar)

**Rationale**: Ensures consistent coordinate identification across all AMOC datasets regardless of source format variations.

Variable Naming Framework
~~~~~~~~~~~~~~~~~~~~~~~~~

Variables use **UPPERCASE** naming with underscores for readability, following CF-1.8 standard names where available. Key patterns include:

**Transport Variables** (``TRANS_`` prefix):
  - Pattern: ``TRANS_{component}`` or ``TRANS_{depth1}_{depth2}``
  - Examples: ``TRANS_EKMAN``, ``TRANS_FC``, ``TRANS_0_800``
  - Units: ``Sverdrup`` (full spelling to avoid confusion with sievert)

**Overturning Variables** (``MOC_`` with coordinate specification):
  - ``MOC`` or ``MOC_Z``: Overturning in depth coordinates
  - ``MOC_SIGMA0``: Overturning in σ₀ density coordinates
  - ``MOC_SIGMA2``: Overturning in σ₂ density coordinates

**Heat/Freshwater Transport**:
  - ``MHT_*``: Meridional heat transport (units: ``PW``)
  - ``MFT_*``: Meridional freshwater transport (units: ``Sverdrup``)
  - Regional qualifiers: ``_EAST``, ``_WEST``, ``_GYRE``, ``_OT``

**Uncertainty Variables** (``_ERR`` suffix):
  - Pattern: ``{VARIABLE}_ERR``
  - Examples: ``MOC_SIGMA0_ERR``, ``MHT_ERR``, ``TRANS_EKMAN_ERR``
  - Units: Always identical to parent variable

For complete variable specifications, see :doc:`AC1_variables`.

Unit Standardization
~~~~~~~~~~~~~~~~~~~

**Preferred Units**:
  - Transport: ``Sverdrup`` (1×10⁶ m³/s)
  - Heat transport: ``PW`` (1×10¹⁵ W)
  - Temperature: ``degree_C``
  - Salinity: ``1`` (practical salinity, dimensionless)
  - Pressure: ``dbar``
  - Coordinates: ``degree_north``, ``degree_east``

**Rationale**:
  - ``Sverdrup`` reflects appropriate scales for AMOC and avoids Sv/sievert confusion
  - ``PW`` makes heat transport values more readable than base SI watts
  - CF-compliant coordinate units enable automatic identification

For complete unit specifications, see :doc:`AC1_units`.

Metadata Requirements
~~~~~~~~~~~~~~~~~~~~

**Required Variable Attributes**:
  - ``standard_name``: From CF-1.8 vocabulary where available
  - ``long_name``: Human-readable description
  - ``units``: UDUNITS-2 compliant units following AC-0.1 preferences
  - ``description``: Extended description (optional but recommended)

**Required Global Attributes**:
  - ``title``, ``summary``, ``source``
  - ``array``, ``id``
  - ``contributor_name``, ``contributor_email``, ``contributor_role``
  - ``format_version``, ``date_created``

Deviations from Standards
-------------------------

AC-0.1 intentionally modifies CF-1.8/OceanSITES-1.5 conventions in specific cases:

.. list-table:: Key Deviations from CF-1.8/OceanSITES-1.5
   :header-rows: 1
   :widths: 25 35 40

   * - Aspect
     - Standard Convention
     - AC-0.1 Modification
   * - Transport Units
     - ``m3 s-1`` (CF standard)
     - ``Sverdrup`` (readability, scale appropriateness)
   * - Heat Transport Units
     - Variable (W, TW, etc.)
     - ``PW`` (consistent scale)
   * - Variable Prefixes
     - Variable naming
     - ``TRANS_`` for transport, ``MOC_`` for overturning
   * - Coordinate Names
     - Variable (lat, latitude, etc.)
     - Standardized UPPERCASE (TIME, DEPTH, etc.)

These deviations are scientifically justified and documented for community review.

Standards Compliance
--------------------

**Format Identification**:
  - Global attribute: ``format_version = "AC-0.1"``
  - Conventions: ``"CF-1.8, ACDD-1.3, OceanSITES-1.5"``
  - Standard name vocabulary: ``"CF Standard Name Table v84"``

**Variable Compliance**:
  Every AC-0.1 variable includes:
  - CF-1.8 compliant ``standard_name`` where available
  - Human-readable ``long_name``
  - UDUNITS-2 compliant ``units``
  - Extended ``description`` with methodology details

Format Validation
-----------------

AC-0.1 compliance can be validated using the AMOCatlas compliance checker:

.. code-block:: python

   from amocatlas.compliance_checker import validate_ac1_format
   
   # Validate a dataset
   results = validate_ac1_format(dataset)
   
   # Check for AC-0.1 compliance
   if results.is_compliant:
       print("Dataset is AC-0.1 compliant")
   else:
       print("Compliance issues found:")
       for issue in results.issues:
           print(f"  - {issue}")

Version History
---------------

**AC-0.1** (2026-02-08):

- Initial format specification
- Based on OceanSITES-1.5 with AMOC-specific extensions
- Establishes variable naming conventions and unit standards
- Defines coordinate system requirements
- Implements uncertainty variable convention
- CF-1.8 compliance with documented deviations

References
----------

- **CF Conventions**: https://cfconventions.org/
- **OceanSITES**: http://www.oceansites.org/docs/oceansites_data_format_reference_manual.pdf
- **ACDD**: https://wiki.esipfed.org/ACDD
- **UDUNITS-2**: https://docs.unidata.ucar.edu/udunits/current/
- **CF Standard Names**: https://cfconventions.org/Data/cf-standard-names/current/