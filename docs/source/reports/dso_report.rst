DSO Dataset Report
==================

Generated: 2026-02-06 23:23:18

DSO_transport_hourly_1996_2021.nc
---------------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Overflow time-series through Denmark Strait
- **Description**: Denmark Strait Overflow
- **Citation**: Jochumsen, K., Moritz, M., Nunes, N., Quadfasel, D., Larsen, K. M. H., Hansen, B., Valdimarsson, H., and Jonsson, S.: Revised transportestimates of the Denmark Strait overflow, Journal of Geophysical Research: Oceans, 122, doi:10.1002/2017JC012803, 2017.
- **Source File**: DSO_transport_hourly_1996_2021.nc
- **Data Product**: Overflow time-series through Denmark Strait
- **Time Coverage**: 830908800.0 to 2021-08-07
- **Record Length**: 221,514 observations (25.3 years)
- **Sampling Frequency**: <1H

**Citation:**

    Jochumsen, K., Moritz, M., Nunes, N., Quadfasel, D., Larsen, K. M. H., Hansen, B., Valdimarsson, H., and Jonsson, S.: Revised transportestimates of the Denmark Strait overflow, Journal of Geophysical Research: Oceans, 122, doi: http://doi.org/10.1002/2017JC012803, 2017.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 1
- **Total Coordinates**: 4
- **Dataset Size**: 2.54 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-----------------------------------------+------------------------------------+-----------+------------+------------+
| Coordinate | Standardized Name | Description                             | Units                              | Size      | Min Value  | Max Value  |
+============+===================+=========================================+====================================+===========+============+============+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (221514,) | 1996-05-01 | 2021-08-07 |
+------------+-------------------+-----------------------------------------+------------------------------------+-----------+------------+------------+
| LATITUDE   | LATITUDE          | Latitude north (WGS84)                  | degrees_north                      | (1,)      | 66         | 66         |
+------------+-------------------+-----------------------------------------+------------------------------------+-----------+------------+------------+
| LONGITUDE  | LONGITUDE         | longitude east (WGS84)                  | degrees_east                       | (1,)      | -27        | -27        |
+------------+-------------------+-----------------------------------------+------------------------------------+-----------+------------+------------+
| DEPTH      | DEPTH             | Depth below surface of the water        | meter                              | (1,)      | 630        | 630        |
+------------+-------------------+-----------------------------------------+------------------------------------+-----------+------------+------------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+------------------------------------------+--------+-------------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                              | Units  | Size        | Min Value | Max Value | Missing % |
+===================+===================+==========================================+========+=============+===========+===========+===========+
| DSO_tr            | TRANS_DSO         | Denmark Strait Overflow volume transport | m3 s-1 | (221514, 1) | -9.66     | 3.08      | 8.3%      |
+-------------------+-------------------+------------------------------------------+--------+-------------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Volume transport timeseries in the North Atlantic
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Id**: OS_2GSR_DSO_D
- **Naming Authority**: OceanSITES
- **Geospatial Lat Min**: 66
- **Geospatial Lat Max**: 66
- **Geospatial Lon Min**: -27
- **Geospatial Lon Max**: -27
- **Time Coverage Start**: 830908800.0
- **Time Coverage End**: 2021-08-07
- **Program**: DSO
- **Project**: Overflow time-series through Denmark Strait
- **Network**: GSR
- **Contributor Name**: Armin Koehl
- **Contributor Email**: armin.koehl@uni-hamburg.de
- **Contributor Id**: https://www.ifm.uni-hamburg.de/institute/staff/koehl.html
- **Contributor Role**: publisher
- **Web Link**: https://www.cen.uni-hamburg.de/en/icdc/data/ocean/denmark-strait-overflow.html
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Date Created**: 2021-12-06T19:37:07Z
- **Featuretype**: timeSeries
- **Description**: Denmark Strait Overflow
- **Acknowledgment**: The timeseries was generated by Institution of Oceanography Hamburg and Hafranns�knastofnun / Marine and Freshwater Research Institute (Reykjavik, Iceland). They were supported through funding from the NACLIM, EU-FP7, grant agr. n.308299, until 2016, and from RACE II (F�rderkennzeichen 03F0729B, until 2018), RACE-Synthese (F�rderkennzeichen 03F0825B, until 2020) German Federal Ministry for Education and Research (BMBF). Nordic WOCE, VEINS, MOEN (contract no. EVK2-CT-2002-00141), ASOF-W (contract no. EVK2-CT-2002-00149), NAClim (grant agr. nr. 308299) THOR (grant agr. nr. 212643), AtlantOS, Blue Action
- **Convections**: CF-1.8, ACDD-1.3
- **Data Product**: Overflow time-series through Denmark Strait
- **Acknowledgement**: None
- **Variable Mapping**: {'DSO_tr': 'TRANS_DSO'}
- **Site Code**: GSR
- **Platform Code**: DSO
- **Source**: subsurface moorings
- **Data Mode**: D
- **Data Type**: OceanSITES time series data
- **Format Version**: 1.3
- **Update Interval**: void
- **Summary**: Denmark Strait Overflow
- **Wmo Platfrom Code**: void
- **Array**: GSR
- **Keywords Vocabulary**: AGU Index Terms
- **Keywords**: OCEANOGRAPHY: PHYSICAL >Currents, OCEANOGRAPHY: GENERAL >North Atlantic oceanography, OCEANOGRAPHY: GENERAL >Time series experiments
- **Area**: North Atlantic Ocean
- **Geospatial Lat Units**: degrees_north
- **Geospatial Lon Units**: degrees_east
- **Geospatial Vertical Positive**: down
- **Geospatial Vertical Units**: meter
- **Time Coverage Duration**: P21Y4M17D
- **Time Coverage Resolution**: PT1H
- **Cdm Data Type**: Station
- **Conventions**: OceanSITES-1.3
- **Netcdf Version**: 3.5
- **References**: http://www.oceansites.org/tma/index.html
- **Data Assembly Center**: void
- **License**: void
- **Date Modified**: 2021-12-06T19:37:07Z
- **History**: 2021-12-06T19:37:07ZOceanSITES file with provisional transport data sent to DAC by Ursula Schauer
- **Processing Level**: Known bad data has been replaced with values based on surrounding data, Data interpolated, Data manually reviewed
- **Qc Indicator**: excellent
- **Instituion**: Institute of Oceanography (Hamburg) and the Marine Research Institute (Reykjavik, Iceland)
- **Source File**: DSO_transport_hourly_1996_2021.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/DSO_transport_hourly_1996_2021.nc
- **Amocatlas Datasource**: dso
- **Applied Variable Mapping**: {'DSO_tr': 'TRANS_DSO'}
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/DSO_transport_hourly_1996_2021.nc
- **Description**: Denmark Strait Overflow
- **Program**: DSO
- **Data Product**: Overflow time-series through Denmark Strait
- **Source Url**: 
- **Platform Type**: 
- **Featuretype**: timeSeries
- **Amocatlas Datasource**: dso
- **Variable Mapping**: {'DSO_tr': 'TRANS_DSO'}
- **Convections**: 
- **Weblink**: 
- **Source File**: DSO_transport_hourly_1996_2021.nc
- **Acknowledgment**: The timeseries was generated by Institution of Oceanography Hamburg and Hafranns�knastofnun / Marine and Freshwater Research Institute (Reykjavik, Iceland). They were supported through funding from the NACLIM, EU-FP7, grant agr. n.308299, until 2016, and from RACE II (F�rderkennzeichen 03F0729B, until 2018), RACE-Synthese (F�rderkennzeichen 03F0825B, until 2020) German Federal Ministry for Education and Research (BMBF). Nordic WOCE, VEINS, MOEN (contract no. EVK2-CT-2002-00141), ASOF-W (contract no. EVK2-CT-2002-00149), NAClim (grant agr. nr. 308299) THOR (grant agr. nr. 212643), AtlantOS, Blue Action
