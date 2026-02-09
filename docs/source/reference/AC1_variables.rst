Variables
=================

Temperature
~~~~~~~~~~~

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - sea_water_conservative_temperature
     - CT
     - degree_C
     - Conservative temperature
   * - sea_water_temperature
     - TEMP
     - degree_C
     - Sea water temperature
   * - sea_water_potential_temperature
     - POTEMP
     - degree_C
     - Sea water potential temperature

Salinity
~~~~~~~~~~~

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - sea_water_absolute_salinity
     - SA
     - g kg-1
     - Absolute salinity (g/kg)
   * - sea_water_practical_salinity
     - PSAL
     - 1
     - Practical salinity

Pressure
~~~~~~~~~~~

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - sea_water_pressure
     - PRES
     - dbar
     - Pressure
   * - sea_water_pressure_at_sea_floor
     - OBP
     - dbar
     - Pressure at sea floor

Density
~~~~~~~~~~~

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - sea_water_sigma_theta
     - SIGMA0
     - kg m-3
     - Density anomaly to 1000 kg m-3, surface reference
   * - sea_water_sigma_theta
     - SIGMA2
     - kg m-3
     - Density anomaly to 1000 kg m-3, 2000 dbar reference
   * - sea_water_neutral_density
     - GAMMA
     - kg m-3
     - Neutral density estimate


Velocity
~~~~~~~~~~~

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - eastward_sea_water_velocity
     - UCUR
     - m s-1
     - Eastward sea water velocity
   * - northward_sea_water_velocity
     - VCUR
     - m s-1
     - Northward sea water velocity
   * - baroclinic_northward_sea_water_velocity
     - VCUR
     - m s-1
     - Baroclinic (layered) meridional velocity
   * - barotropic_northward_sea_water_velocity
     - VCUR
     - m s-1
     - Depth-averaged (barotropic) meridional velocity

Transport
~~~~~~~~~~~

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - northward_ocean_freshwater_transport
     - MFT
     - Sverdrup
     - Total northward freshwater transport
   * - northward_ocean_freshwater_transport_due_to_gyre
     - MFT_GYRE
     - Sverdrup
     - Gyre component of freshwater transport
   * - northward_ocean_freshwater_transport_due_to_overturning
     - MFT_OT
     - Sverdrup
     - Overturning component of freshwater transport
   * - northward_ocean_heat_transport
     - MHT
     - PW
     - Total northward heat transport
   * - ocean_volume_transport_across_line
     - TRANS
     - Sverdrup
     - Volume transport across a defined line or section
   * - ocean_meridional_overturning_streamfunction
     - MOC, MOC_SIGMA0, MOC_SIGMA2, MOC_Z
     - Sverdrup
     - General overturning streamfunction

Uncertainty Variables
~~~~~~~~~~~~~~~~~~~~

**Convention**: All uncertainty variables follow the pattern ``{VARIABLE}_ERR``

.. list-table:: Uncertainty Variables (Examples)
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``MOC_ERR``
     - Uncertainty in MOC
     - Sverdrup
     - ocean_meridional_overturning_transport
     - Standard error/uncertainty in MOC estimate
   * - ``MOC_SIGMA0_ERR``
     - Uncertainty in MOC (σ₀)
     - Sverdrup
     - ocean_meridional_overturning_streamfunction
     - Uncertainty in σ₀-referenced MOC
   * - ``MHT_ERR``
     - Uncertainty in heat transport
     - PW
     - northward_ocean_heat_transport
     - Standard error in heat transport estimate
   * - ``MFT_ERR``
     - Uncertainty in freshwater transport
     - Sverdrup
     - northward_ocean_freshwater_transport
     - Standard error in freshwater transport estimate
   * - ``TRANS_EKMAN_ERR``
     - Uncertainty in Ekman transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Standard error in Ekman transport estimate

**Rules for Uncertainty Variables**:

- Same units as parent variable
- Same standard_name as parent variable where appropriate  
- long_name: "Uncertainty in {parent_long_name}"
- Include method of uncertainty calculation in description

Variable Metadata Requirements
-----------------------------

Variable Attributes
~~~~~~~~~~~~~~~~~~

Every variable in AC1.0 format should include the following attributes:

**standard_name** (string):
   - Use CF-1.8 standard name vocabulary where available
   - For AMOC-specific variables, document extensions clearly
   - Use closest CF standard name with clarification in description

**long_name** (string):
   - Human-readable name for the variable
   - Use sentence case (capitalize first word only)
   - Be descriptive but concise (< 60 characters recommended)

**units** (string):
   - UDUNITS-2 compliant unit specification
   - Use AMOCatlas preferred units (see Unit Standards)
   - Coordinate variables: use appropriate CF units

**description** (string, optional but recommended):
   - Extended description providing additional context
   - Include methodology, reference levels, coordinate systems
   - Clarify any deviations from standard definitions

**coordinates** (string, for data variables):
   - Space-separated list of coordinate variables
   - Standard format: "TIME DEPTH LATITUDE LONGITUDE"

Optional Attributes
~~~~~~~~~~~~~~~~~~

**valid_range** (numeric array):
   - [minimum, maximum] physically meaningful values
   - Use for data validation and quality control

**_FillValue** (numeric):
   - Value used for missing data
   - Should be outside valid_range

**comment** (string):
   - Additional notes about the variable
   - Methodology details, known issues, etc.

**source** (string):
   - Original data source or instrument
   - Useful for multi-source composite products

**processing_notes** (string):
   - Details about data processing applied
   - Quality control procedures, filtering, etc.

**reference_pressure** (numeric):
  - For density variables, specify reference pressure in dbar
  - Important for interpreting potential density coordinates

Vocabulary Standards
-------------------

CF Standard Name Vocabulary
~~~~~~~~~~~~~~~~~~~~~~~~~~

CF Standard Name Table v84
   - URL: https://cfconventions.org/Data/cf-standard-names/current/
   - Use for all geophysical variables where applicable
   - Document extensions in AMOCatlas vocabulary supplement


Quality Control Flags
~~~~~~~~~~~~~~~~~~~~~~~~~~

Following OceanSITES-1.5 QC flag conventions:

.. list-table:: Quality Control Flags
   :header-rows: 1
   :widths: 10 20 70

   * - Flag
     - Meaning
     - Description
   * - 0
     - No QC performed
     - No quality control has been performed
   * - 1
     - Good data
     - Passed documented required QC tests
   * - 2
     - Not evaluated
     - Used for data when no QC test could be performed
   * - 3
     - Questionable
     - Questionable data (may require user evaluation)
   * - 4
     - Bad data
     - Bad data that should not be used
   * - 7
     - Nominal value
     - Nominal value (e.g., from climatology)
   * - 8
     - Interpolated
     - Missing values filled by interpolation
   * - 9
     - Missing data
     - Used as _FillValue for missing data
