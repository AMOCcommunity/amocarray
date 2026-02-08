Coordinates 
========================

There is no single universal standard that mandates variable names in an ``xarray.Dataset`` or CF conventions.  Therefore, the standard_name and vocabulary are critically important for interoperability.


.. list-table::
   :widths: 40 10 15 35
   :header-rows: 1

   * - CF Standard Name
     - AC1 Name
     - Units
     - Description
   * - latitude
     - LATITUDE
     - degree_north
     - Latitude north (WGS84)
   * - longitude
     - LONGITUDE
     - degree_east
     - Longitude east (WGS84)
   * - time
     - TIME
     - datetime64[ns]
     - Time coordinate (CF-compliant)
   * - depth
     - DEPTH
     - m
     - Depth below sea surface, positive downwards
   * - sea_water_pressure
     - PRESSURE
     - dbar
     - Pressure coordinate (dbar)
   * - sea_water_sigma_theta
     - SIGMA0
     - kg m-3
     - Potential density anomaly coordinate (σ₀), reference pressure 0 dbar
   * - sea_water_sigma_theta
     - SIGMA2
     - kg m-3
     - Potential density anomaly coordinate (σ₂), reference pressure 2000 dbar
