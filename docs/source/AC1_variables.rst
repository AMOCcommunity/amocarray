Variable Names
===============

There is no single universal standard that mandates variable names in an ``xarray.Dataset`` or CF conventions.  Therefore, the standard_name and vocabulary are critically important for interoperability.



**CMIP6 Variable Mapping by Category**

.. warning::
   The CMIP6 variable names in these tables require verification and may not be accurate. Please consult the official CMIP6 documentation for correct variable mappings.

This table maps CF standard names to CMIP6 variable names, organized by category.
These short names are typically used in CMIP6 NetCDF output and should be matched to your xarray variables
via the `standard_name` attribute.

Temperature
-----------

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - CMIP6 Name
     - Description
   * - sea_water_conservative_temperature
     - CT
     - 
     - Conservative temperature
   * - sea_water_temperature
     - TEMP
     - 
     - Sea water temperature
   * - sea_water_potential_temperature
     - POTEMP
     - thetao
     - Sea water potential temperature

Salinity
--------

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - CMIP6 Name
     - Description
   * - sea_water_absolute_salinity
     - SA
     - 
     - Absolute salinity (g/kg)
   * - sea_water_practical_salinity
     - PSAL
     - so
     - Practical salinity

Pressure
--------

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - CMIP6 Name
     - Description
   * - sea_water_pressure
     - PRES
     - pso
     - Pressure
   * - sea_water_pressure_at_sea_floor
     - OBP
     - 
     - Pressure at sea floor

Density
-------

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - CMIP6 Name
     - Description
   * - sea_water_sigma_theta
     - 
     - sigma0
     - Density anomaly to 1000, surface reference
   * - sea_water_potential_density
     - 
     - 
     - Same as sigma-theta
   * - sea_water_neutral_density
     - 
     - gamma_n
     - Neutral density estimate
   * - ocean_sigma_coordinate
     - 
     - —
     - Vertical coordinate metadata

Velocity
--------

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - CMIP6 Name
     - Description
   * - eastward_sea_water_velocity
     - UCUR
     - 
     - Eastward sea water velocity
   * - northward_sea_water_velocity
     - VCUR
     - 
     - Northward sea water velocity
   * - baroclinic_northward_sea_water_velocity
     - VCUR
     - votemper
     - Baroclinic (layered) meridional velocity
   * - barotropic_northward_sea_water_velocity
     - VCUR
     - vbar
     - Depth-averaged (barotropic) meridional velocity

Transport
---------

.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - CMIP6 Name
     - Description
   * - northward_ocean_freshwater_transport
     - MFT
     - fwt_north
     - Total freshwater transport
   * - northward_ocean_freshwater_transport_due_to_gyre
     - MFT_GYRE
     - fwt_north_gyre
     - Gyre component of freshwater transport
   * - northward_ocean_freshwater_transport_due_to_overturning
     - MFT_OT
     - fwt_north_ovt
     - Overturning component of freshwater transport
   * - northward_ocean_heat_tranpsport
     - MHT
     - fht_north
     - Total northward heat transport
   * - ocean_volume_transport_across_line
     - TRANSPORT
     - vol_transport
     - Volume transport across a defined line or section
   * - ocean_meridional_overturning_mass_streamfunction
     - MOC_MASS
     - moc
     - Overturning streamfunction (mass)
   * - ocean_meridional_overturning_streamfunction
     - MOC
     - mosf
     - General overturning streamfunction
   * - ocean_meridional_overturning_streamfunction
     - MOC_SIG
     - 
     - Overturning streamfunction in density space (sigma coordinate)
