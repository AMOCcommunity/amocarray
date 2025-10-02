.. This file is included under 'format_orig.rst' and should use '~~' or lower as the top header level.

.. _array-41n:

41°N Original Data Format
-------------------------

The 41°N array provides AMOC estimates derived from Argo float observations and satellite altimetry data,  
extending the observational record back to 2002.

 
hobbs_willis_amoc41N_tseries.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These files contain an estimate of the Atlantic Meridional Overturning Circulation (AMOC) volume and heat transports, 
computed using observations of temperature, salinity and subsurface velocity from the Argo array of profiling floats (DOI: 10.17882/42182#116315), 
and satellite-based observations of sea level from altimetry (DOI: 10.48670/moi-00148 and DOI: 10.48670/moi-00149).  
The estimates are computed using the techniques of Willis (2010) and Hobbs and Willis (2012). 
In addition, estimates of wind stress at the surface were estimated from European Center for Medium Range Weather Forecast, 
ERA5 analysis (DOI: 10.24381/cds.143582cf).

Note that in all files, although there are 12 time-steps per year, each time step represents a 3-month average, 
so the time series is over sampled.

The .txt file contains comma separated values of the time series, with 1 header line and the following columns, 
estimated as in Willis (2010) and Hobbs and Willis (2012): 

Column 1: Decimal year

Column 2: Ekman Volume Transport (Sverdrups)

Column 3: Northward Geostrophic Transport (Sverdrups)

Column 4: Meridional Overturning Volume Transport (Sverdrups)

Column 5: Meridional Overturning Heat Transport (PetaWatts)

.. list-table:: Variables
   :widths: 12 22 14 10 35
   :header-rows: 1

   * - Name
     - Dimensions
     - Shape
     - Units
     - Description
   * - ``TIME``
     - ``TIME``
     - (275,)
     - datetime
     - Time coordinate
   * - ``EKMAN``
     - ``TIME``
     - (275,)
     - Sv
     - Ekman volume transport
   * - ``V_GEOS``
     - ``TIME``
     - (275,)
     - Sv
     - Northward geostrophic transport
   * - ``MOT``
     - ``TIME``
     - (275,)
     - Sv
     - Meridional overturning volume transport
   * - ``MOHT``
     - ``TIME``
     - (275,)
     - PW
     - Meridional overturning heat transport

trans_Argo_ERA5.nc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file called “trans_Argo_ERA5.nc” contains an estimate of the geostrophic transport as a function of latitude, 
longitude, depth and time, for the upper 2000 m for latitudes near 41 N in the Atlantic Ocean, 
estimated as described in Willis (2010). 
Also included are Ekman Transport and Overturning Transport as functions of time and latitude for this region.


.. list-table:: Variables
   :widths: 12 22 14 10 35
   :header-rows: 1

   * - Name
     - Dimensions
     - Shape
     - Units
     - Description
   * - ``time``
     - ``time``
     - (276,)
     - YYYYMM
     - Time coordinate
   * - ``Vek``
     - ``time``, ``lat``
     - (276,4)
     - Sv
     - Ekman transport
   * - ``trans``
     - ``time``, ``lat``, ``lon``, ``depth``
     - (275,)
     - Sv
     - Observed geostrophic transport
   * - ``moc``
     - ``time``, ``lat``
     - (276,4)
     - Sv
     - Overturning transport, Willis (2010) method
 

 Q_ARGO_obs_dens_2000depth_ERA5.nc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file called “Q_ARGO_obs_dens_2000depth_ERA5.nc” contains estimates of heat transport for these regions
based on various assumptions about the temperature of the ocean at depths unmeasured by the Core Argo array
(depths below 2000m), estimated as described in Hobbs and Willis (2012).  
These assumptions are described in the variable “Hpar”.

.. list-table:: Variables
   :widths: 12 22 14 10 35
   :header-rows: 1

   * - Name
     - Dimensions
     - Shape
     - Units
     - Description
   * - ``time``
     - ``time``
     - (276,)
     - YYYYMM
     - Time coordinate
   * - ``Qnet``
     - ``time``, ``lat``, ``Hpar``
     - (276,4, 4)
     - PW
     - Net heat transport
   * - ``Qek``
     - ``time``, ``lat``
     - (276,4)
     - PW
     - Ekman heat transport
   * - ``Q``
     - ``time``, ``lat``, ``lon``, ``depth``
     - (276,4, 320, 201)
     - PW
     - Observed heat transport