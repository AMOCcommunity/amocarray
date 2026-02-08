AMOCatlas Variables (AC1.0)
===================================

This document defines the comprehensive variable naming conventions, metadata requirements, and categorization standards for the AMOCatlas Format v1.0 (AC1.0).

.. note::
   These standards ensure consistent variable identification and metadata across all AMOC observational datasets. All variables must follow these conventions to achieve AC1.0 compliance.

Variable Categories
------------------

Coordinate Variables
~~~~~~~~~~~~~~~~~~~

Coordinate variables use **UPPERCASE** naming for consistency across all datasets.

.. list-table:: Coordinate Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``TIME``
     - Time
     - days since 1950-01-01
     - time
     - Temporal coordinate, CF-compliant datetime
   * - ``DEPTH``
     - Depth below sea surface
     - m
     - depth
     - Positive downward depth coordinate
   * - ``LATITUDE``
     - Latitude
     - degree_north
     - latitude
     - Geographic latitude coordinate, positive northward
   * - ``LONGITUDE``
     - Longitude
     - degree_east
     - longitude
     - Geographic longitude coordinate, positive eastward

Transport Variables
~~~~~~~~~~~~~~~~~~

Transport variables use the **TRANS_** prefix with descriptive suffixes.  These are used for components of the transbasin transport, such as the Ekman transport, Florida Current transport, and layer-specific transports.  They may be array-specific.

.. list-table:: Transport Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``TRANS_EKMAN``
     - Ekman transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Wind-driven Ekman transport component
   * - ``TRANS_FC``
     - Florida Current transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Volume transport through Florida Straits (26°N)
   * - ``TRANS_UMO``
     - Upper mid-ocean transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Geostrophic transport in upper mid-ocean (26°N)
   * - ``TRANS_0_800``
     - Transport 0-800m depth
     - Sverdrup
     - ocean_volume_transport_across_line
     - Volume transport in 0-800m depth layer (26°N)
   * - ``TRANS_800_1100``
     - Transport 800-1100m depth
     - Sverdrup
     - ocean_volume_transport_across_line
     - Volume transport in 800-1100m depth layer (26°N)
   * - ``TRANS_1100_3000``
     - Transport 1100-3000m depth
     - Sverdrup
     - ocean_volume_transport_across_line
     - Volume transport in 1100-3000m depth layer (26°N)
   * - ``TRANS_3000_5000``
     - Transport 3000-5000m depth
     - Sverdrup
     - ocean_volume_transport_across_line
     - Volume transport in 3000-5000m depth layer (26°N)
   * - ``TRANS_below_5000``
     - Transport below 5000m depth
     - Sverdrup
     - ocean_volume_transport_across_line
     - Volume transport below 5000m depth (26°N)
   * - ``TRANS_DSO``
     - Denmark Strait overflow transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Transport through Denmark Strait
   * - ``TRANS_FBC``
     - Faroe Bank Channel transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Transport through Faroe Bank Channel
   * - ``TRANS_GEO``
     - Geostrophic transport
     - Sverdrup
     - ocean_volume_transport_across_line
     - Geostrophic component of transport

Overturning Variables
~~~~~~~~~~~~~~~~~~~~

Overturning variables use **MOC** with coordinate system specification.

.. list-table:: Overturning Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``MOC``
     - Meridional overturning circulation
     - Sverdrup
     - ocean_meridional_overturning_transport
     - AMOC strength (coordinate in attributes)
   * - ``MOC_Z``
     - MOC in depth coordinates
     - Sverdrup
     - ocean_meridional_overturning_transport
     - Overturning streamfunction maximum in depth coordinates
   * - ``MOC_SIGMA0``
     - MOC in σ₀ density coordinates
     - Sverdrup
     - ocean_meridional_overturning_transport
     - Overturning streamfunction in potential density coordinates (26°N, OSNAP, 47°N)
   * - ``MOC_SIGMA2``
     - MOC in σ₂ density coordinates
     - Sverdrup
     - ocean_meridional_overturning_transport
     - Overturning streamfunction in σ₂ density coordinates (26°N)
   * - ``MOC_BOUNDARY``
     - Boundary MOC component
     - Sverdrup
     - ocean_volume_transport_across_line
     - Boundary component of overturning (16°N)
   * - ``MOC_INTERNAL``
     - Internal MOC component
     - Sverdrup
     - ocean_volume_transport_across_line
     - Internal (baroclinic) component of overturning (16°N)
   * - ``MOC_WEST_SIGMA0``
     - Western boundary MOC (σ₀)
     - Sverdrup
     - ocean_meridional_overturning_streamfunction
     - Western section MOC in σ₀ coordinates (OSNAP)
   * - ``MOC_EAST_SIGMA0``
     - Eastern boundary MOC (σ₀)
     - Sverdrup
     - ocean_meridional_overturning_streamfunction
     - Eastern section MOC in σ₀ coordinates (OSNAP)

Streamfunction Variables
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Streamfunction Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``STREAMFUNCTION_Z``
     - Overturning streamfunction (depth)
     - Sverdrup
     - ocean_meridional_overturning_streamfunction
     - Time-varying MOC streamfunction vs. depth
   * - ``STREAMFUNCTION_SIGMA0``
     - Overturning streamfunction (σ₀)
     - Sverdrup
     - ocean_meridional_overturning_streamfunction
     - Time-varying MOC streamfunction vs. σ₀ density
   * - ``STREAMFUNCTION_SIGMA2``
     - Overturning streamfunction (σ₂)
     - Sverdrup
     - ocean_meridional_overturning_streamfunction
     - Time-varying MOC streamfunction vs. σ₂ density

Heat Transport Variables
~~~~~~~~~~~~~~~~~~~~~~~

Heat transport variables use **MHT** prefix with regional qualifiers.

.. list-table:: Heat Transport Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``MHT``
     - Meridional heat transport
     - PW
     - northward_ocean_heat_transport
     - Total northward oceanic heat transport
   * - ``MHT_NET``
     - Net meridional heat transport
     - PW
     - northward_ocean_heat_transport
     - Net meridional heat transport
   * - ``MHT_EKMAN``
     - Ekman heat transport
     - PW
     - northward_ocean_heat_transport_component
     - Ekman component of heat transport
   * - ``MHT_FC``
     - Florida Current heat transport
     - PW
     - northward_ocean_heat_transport_component
     - Heat transport through Florida Straits (26°N)
   * - ``MHT_GYRE``
     - Gyre heat transport
     - PW
     - northward_ocean_heat_transport_due_to_gyre
     - Basinwide gyre heat transport component (26°N)
   * - ``MHT_OT``
     - Overturning heat transport
     - PW
     - northward_ocean_heat_transport_due_to_meridional_overturning
     - Overturning component of heat transport
   * - ``MHT_EAST``
     - Eastern section heat transport
     - PW
     - northward_ocean_heat_transport
     - Meridional heat transport across eastern section (OSNAP)
   * - ``MHT_WEST``
     - Western section heat transport
     - PW
     - northward_ocean_heat_transport
     - Meridional heat transport across western section (OSNAP)

Freshwater Transport Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Freshwater transport variables use **MFT** prefix.

.. list-table:: Freshwater Transport Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``MFT``
     - Meridional freshwater transport
     - Sverdrup
     - northward_ocean_freshwater_transport
     - Total meridional freshwater transport
   * - ``MFT_EAST``
     - Eastern section freshwater transport
     - Sverdrup
     - northward_ocean_freshwater_transport
     - Freshwater transport across eastern section (OSNAP)
   * - ``MFT_WEST``
     - Western section freshwater transport
     - Sverdrup
     - northward_ocean_freshwater_transport
     - Freshwater transport across western section (OSNAP)

Temperature and Salinity Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Temperature and Salinity Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``TEMP``
     - Sea water temperature
     - degree_C
     - sea_water_temperature
     - In-situ temperature
   * - ``POTEMP``
     - Potential temperature
     - degree_C
     - sea_water_potential_temperature
     - Potential temperature referenced to surface
   * - ``CT``
     - Conservative temperature
     - degree_C
     - sea_water_conservative_temperature
     - TEOS-10 conservative temperature
   * - ``PSAL``
     - Practical salinity
     - 1
     - sea_water_practical_salinity
     - Practical salinity following PSS-78
   * - ``SA``
     - Absolute salinity
     - g kg-1
     - sea_water_absolute_salinity
     - TEOS-10 absolute salinity

Density Variables
~~~~~~~~~~~~~~~~

.. list-table:: Density Variables
   :header-rows: 1
   :widths: 20 25 15 15 25

   * - Variable Name
     - Long Name
     - Units
     - Standard Name
     - Description
   * - ``SIGMA0``
     - Potential density anomaly (σ₀)
     - kg m-3
     - sea_water_sigma_theta
     - Potential density referenced to surface minus 1000 (OSNAP, 26°N)
   * - ``SIGMA2``
     - Potential density anomaly (σ₂)
     - kg m-3
     - sea_water_sigma_theta
     - Potential density referenced to 2000 dbar minus 1000 (26°N)



Flag variables use naming pattern: ``{VARIABLE}_FLAG``

Examples and Usage
-----------------

Example Variable Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Complete variable definition for MOC_SIGMA0
   MOC_SIGMA0 = {
       'data': moc_data,
       'attrs': {
           'standard_name': 'ocean_meridional_overturning_transport',
           'long_name': 'MOC_sigma0', # Used for plotting
           'units': 'Sverdrup',
           'description': 'Maximum of the Atlantic meridional overturning streamfunction in potential density coordinates referenced to the surface (σ₀ = σ(S,T,0) - 1000 kg/m³)',
           'coordinates': 'TIME LATITUDE',
           'valid_range': [-10.0, 50.0],
           'processing_notes': 'Calculated using temperature and salinity from moored instrumentation'
       }
   }


Change Management (not yet implemented)
--------------------------------------

**Version Control**:
   - All changes to variable standards must be documented
   - Backward compatibility maintained where possible
   - Breaking changes require major version increment

**Community Review**:
   - Proposed changes undergo community review process
   - Technical working group evaluates scientific justification
   - Implementation plan includes migration tools for existing data

**Documentation Updates**:
   - Standards documentation updated with each version
   - Examples provided for new variable types
   - Migration guides for version updates