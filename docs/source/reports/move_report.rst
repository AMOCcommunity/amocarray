MOVE Dataset Report
===================

Generated: 2026-02-06 23:23:13

This report covers all available MOVE datasets.

OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Citation**: MOVE was funded by NOAA GOMO and led by U. Send and M. Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **Acknowledgement**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **DOI**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Source File**: OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Data Product**: MOVE transport time series (2000-2022)
- **Time Coverage**: -9223372036.9 to 1.7
- **Record Length**: 4,164 observations (292.3 years)
- **Sampling Frequency**: <1H

**Citation:**

    MOVE was funded by NOAA GOMO and led by U. Send and M. Lankhorst. MOVE data are made freely available through the international OceanSITES program.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 8
- **Total Coordinates**: 4
- **Dataset Size**: 0.16 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-----------+-----------+
| Coordinate                | Standardized Name         | Description                             | Units                              | Size    | Min Value | Max Value |
+===========================+===========================+=========================================+====================================+=========+===========+===========+
| TIME                      | TIME                      | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (4164,) | N/A       | N/A       |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-----------+-----------+
| location_center_latitude  | location_center_latitude  | No description available                | degrees_north                      | ()      | 16        | 16        |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-----------+-----------+
| location_center_longitude | location_center_longitude | No description available                | degrees_east                       | ()      | -57.6     | -57.6     |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-----------+-----------+
| location_center_vertical  | location_center_vertical  | No description available                | dbar                               | ()      | 2.75e+03  | 2.75e+03  |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-----------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------+----------+---------+-----------+------------------------------------------+-----------+
| Original Variable                   | Standardized Name   | Description                                                                                                            | Units    | Size    | Min Value | Max Value                                | Missing % |
+=====================================+=====================+========================================================================================================================+==========+=========+===========+==========================================+===========+
| TRANSPORT_TOTAL                     | MOC                 | Ocean volume transport across the MOVE line                                                                            | Sverdrup | (4164,) | -31.86    | 9969209968386869046778552952102584320.00 | 3.8%      |
+-------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------+----------+---------+-----------+------------------------------------------+-----------+
| transport_component_internal        | MOC_INTERNAL        | **Internal transport component**: Internal component of ocean volume transport across the MOVE line                    | Sverdrup | (4164,) | -35.46    | 9969209968386869046778552952102584320.00 | 3.6%      |
+-------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------+----------+---------+-----------+------------------------------------------+-----------+
| transport_component_internal_offset | MOC_INTERNAL_OFFSET | **Internal transport offset**: Offset to be added to internal component of ocean volume transport across the MOVE line | Sverdrup | (4164,) | 5.78      | 9969209968386869046778552952102584320.00 | 1.8%      |
+-------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------+----------+---------+-----------+------------------------------------------+-----------+
| transport_component_boundary        | MOC_BOUNDARY        | **Boundary transport component**: Boundary component of ocean volume transport across the MOVE line                    | Sverdrup | (4164,) | -10.98    | 9969209968386869046778552952102584320.00 | 1.2%      |
+-------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------+----------+---------+-----------+------------------------------------------+-----------+


Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT dataset.

Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Ocean Volume Transport across the MOVE Line at 16 N
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: -9223372036.9
- **Time Coverage End**: 1.7
- **Program**: MOVE
- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Contributor Name**: Uwe Send, Matthias Lankhorst, Matthias Lankhorst
- **Contributor Email**: , , 
- **Contributor Id**: _, http://orcid.org/0000-0002-4166-4044, http://orcid.org/0000-0002-4166-4044
- **Contributor Role**: Principal Investigator, Creator
- **Contributing Institutions**: Scripps Institution of Oceanography
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Web Link**: https://mooring.ucsd.edu/move/
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Date Created**: 2019-01-30T18:13:16Z
- **Featuretype**: timeSeries
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Acknowledgement**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **License**: Data freely available. User assumes all risk for use of data. Please give due credit to the authors, project, and funding sources when using these data, e.g. by including the 'citation' text provided here.
- **References**: Uwe Send, Matthias Lankhorst, Torsten Kanzow: Observation of decadal change in the Atlantic Meridional Overturning Circulation using 10 years of continuous transport data. Geophysical Research Letters, Vol. 38, L24606, 2011. doi: 10.1029/2011GL049801.
- **Conventions**: CF-1.7, ACDD-1.3
- **Source**: Derived using the following files: OceanSITES file OS_MOVE_MULTISITE_GRIDDED_TS.nc, created 2019-01-30T18:11:12Z OceanSITES file OS_MOVE_MULTISITE_GRIDDED_V.nc, created 2019-01-17T00:40:57Z
- **Data Product**: MOVE transport time series (2000-2022)
- **Variable Mapping**: {'TRANSPORT_TOTAL': 'MOC', 'transport_component_internal': 'MOC_INTERNAL', 'transport_component_internal_offset': 'MOC_INTERNAL_OFFSET', 'transport_component_boundary': 'MOC_BOUNDARY'}
- **Summary**: MOVE transport estimates dataset from UCSD mooring project
- **Source File**: OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Amocatlas Datasource**: move16n
- **Applied Variable Mapping**: {'TRANSPORT_TOTAL': 'MOC', 'transport_component_internal': 'MOC_INTERNAL', 'transport_component_internal_offset': 'MOC_INTERNAL_OFFSET', 'transport_component_boundary': 'MOC_BOUNDARY'}
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Contributor Url**: 
- **Program**: MOVE
- **Data Product**: MOVE transport time series (2000-2022)
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Platform Type**: 
- **Time Coverage End**: 2018-06-30
- **Amocatlas Datasource**: move16n
- **Variable Mapping**: {'TRANSPORT_TOTAL': 'MOC', 'transport_component_internal': 'MOC_INTERNAL', 'transport_component_internal_offset': 'MOC_INTERNAL_OFFSET', 'transport_component_boundary': 'MOC_BOUNDARY'}
- **Reference**: 
- **Weblink**: 
- **Time Coverage Start**: 2000-01-01
- **Source File**: OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc

OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
--------------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Citation**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **Acknowledgement**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **DOI**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Source File**: OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
- **Time Coverage**: 0.9 to 1.7
- **Record Length**: 8,330 observations (0.7 years)
- **Sampling Frequency**: <1H

**Citation:**

    Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 6
- **Total Coordinates**: 4
- **Dataset Size**: 10.99 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| Coordinate | Standardized Name | Description                                                    | Units                              | Size    | Min Value  | Max Value  |
+============+===================+================================================================+====================================+=========+============+============+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z                        | seconds since 1970-01-01T00:00:00Z | (8330,) | 1970-01-01 | 1970-01-01 |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| PRESSURE   | PRESSURE          | Sea water pressure due to sea water, i.e. air pressure removed | dbar                               | (38,)   | 1.25e+03   | 4.95e+03   |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| LATITUDE   | LATITUDE          | Latitude north (WGS84)                                         | degrees_north                      | (2,)    | 16.3       | 16.3       |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| LONGITUDE  | LONGITUDE         | longitude east (WGS84)                                         | degrees_east                       | (2,)    | -60.6      | -60.5      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+--------------------------------------------------------------------+-------+---------------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                        | Units | Size          | Min Value | Max Value | Missing % |
+===================+===================+====================================================================+=======+===============+===========+===========+===========+
| VELOCITY_V        | VELOCITY_V        | Seawater velocity in north-south direction, positive towards north | m s-1 | (2, 8330, 38) | -0.56     | 0.35      | 1.2%      |
+-------------------+-------------------+--------------------------------------------------------------------+-------+---------------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Gridded Velocity Data from the MOVE Moorings
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Id**: OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4
- **Naming Authority**: OceanSITES
- **Geospatial Lat Min**: 16.330833435058594
- **Geospatial Lat Max**: 16.362333333333336
- **Geospatial Lon Min**: -60.61249923706055
- **Geospatial Lon Max**: -60.494327545166016
- **Geospatial Vertical Min**: 1250.0
- **Geospatial Vertical Max**: 4950.0
- **Time Coverage Start**: 0.9
- **Time Coverage End**: 1.7
- **Program**: MOVE
- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Contributor Name**: Uwe Send, Matthias Lankhorst, Matthias Lankhorst
- **Contributor Email**: , , 
- **Contributor Id**: _, http://orcid.org/0000-0002-4166-4044, http://orcid.org/0000-0002-4166-4044
- **Contributor Role**: Principal Investigator, Creator
- **Contributing Institutions**: Scripps Institution of Oceanography
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Web Link**: https://mooring.ucsd.edu/move/
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Date Created**: 2019-01-30T18:13:16Z
- **Featuretype**: timeSeries
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Acknowledgement**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **License**: Data freely available. User assumes all risk for use of data. Please give due credit to the authors, project, and funding sources when using these data, e.g. by including the 'citation' text provided here.
- **References**: Uwe Send, Matthias Lankhorst, Torsten Kanzow: Observation of decadal change in the Atlantic Meridional Overturning Circulation using 10 years of continuous transport data. Geophysical Research Letters, Vol. 38, L24606, 2011. doi: 10.1029/2011GL049801.
- **Conventions**: CF-1.7, ACDD-1.3
- **Source**: Derived using the following files: OceanSITES file OS_MOVE_MULTISITE_GRIDDED_TS.nc, created 2019-01-30T18:11:12Z OceanSITES file OS_MOVE_MULTISITE_GRIDDED_V.nc, created 2019-01-17T00:40:57Z
- **Summary**: MOVE transport estimates dataset from UCSD mooring project
- **Data Type**: OceanSITES time-series data
- **Format Version**: 1.5
- **Update Interval**: void
- **Qc Indicator**: excellent
- **Area**: Tropical Atlantic Ocean
- **Geospatial Vertical Positive**: down
- **Geospatial Vertical Units**: dbar
- **Source File**: OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
- **Amocatlas Datasource**: move16n
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Contributor Url**: 
- **Program**: MOVE
- **Amocatlas Datasource**: move16n
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Platform Type**: 
- **Reference**: 
- **Weblink**: 
- **Source File**: OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc

OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
--------------------------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Citation**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **Acknowledgement**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **DOI**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Source File**: OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
- **Time Coverage**: 0.9 to 1.7
- **Record Length**: 4,164 observations (0.7 years)
- **Sampling Frequency**: <1H

**Citation:**

    Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 6
- **Total Coordinates**: 4
- **Dataset Size**: 14.14 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| Coordinate | Standardized Name | Description                                                    | Units                              | Size    | Min Value  | Max Value  |
+============+===================+================================================================+====================================+=========+============+============+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z                        | seconds since 1970-01-01T00:00:00Z | (4164,) | 1970-01-01 | 1970-01-01 |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| PRESSURE   | PRESSURE          | Sea water pressure due to sea water, i.e. air pressure removed | dbar                               | (99,)   | 50         | 4.95e+03   |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| LATITUDE   | LATITUDE          | Latitude north (WGS84)                                         | degrees_north                      | (2,)    | 15.4       | 16.3       |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+
| LONGITUDE  | LONGITUDE         | longitude east (WGS84)                                         | degrees_east                       | (2,)    | -60.5      | -51.5      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+------------+------------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+----------------------------------------------------------------+-------+---------------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                    | Units | Size          | Min Value | Max Value | Missing % |
+===================+===================+================================================================+=======+===============+===========+===========+===========+
| SALINITY          | SALINITY          | Salinity of sea water reported on the practical salinity scale | 1     | (2, 4164, 99) | 33.88     | 37.48     | 0.6%      |
+-------------------+-------------------+----------------------------------------------------------------+-------+---------------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Gridded Temperature and Salinity Data from the MOVE Moorings
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Id**: OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3
- **Naming Authority**: OceanSITES
- **Geospatial Lat Min**: 15.323833333333333
- **Geospatial Lat Max**: 16.34
- **Geospatial Lon Min**: -60.516666666666666
- **Geospatial Lon Max**: -51.5
- **Geospatial Vertical Min**: 50.0
- **Geospatial Vertical Max**: 4950.0
- **Time Coverage Start**: 0.9
- **Time Coverage End**: 1.7
- **Program**: MOVE
- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Contributor Name**: Uwe Send, Matthias Lankhorst, Matthias Lankhorst
- **Contributor Email**: , , 
- **Contributor Id**: _, http://orcid.org/0000-0002-4166-4044, http://orcid.org/0000-0002-4166-4044
- **Contributor Role**: Principal Investigator, Creator
- **Contributing Institutions**: Scripps Institution of Oceanography
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Web Link**: https://mooring.ucsd.edu/move/
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Date Created**: 2019-01-30T18:13:16Z
- **Featuretype**: timeSeries
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Acknowledgement**: Collection of MOVE data was funded by NOAA Research, and carried out by principal investigators Uwe Send and Matthias Lankhorst. MOVE data are made freely available through the international OceanSITES program.
- **License**: Data freely available. User assumes all risk for use of data. Please give due credit to the authors, project, and funding sources when using these data, e.g. by including the 'citation' text provided here.
- **References**: Uwe Send, Matthias Lankhorst, Torsten Kanzow: Observation of decadal change in the Atlantic Meridional Overturning Circulation using 10 years of continuous transport data. Geophysical Research Letters, Vol. 38, L24606, 2011. doi: 10.1029/2011GL049801.
- **Conventions**: CF-1.7, ACDD-1.3
- **Source**: Derived using the following files: OceanSITES file OS_MOVE_MULTISITE_GRIDDED_TS.nc, created 2019-01-30T18:11:12Z OceanSITES file OS_MOVE_MULTISITE_GRIDDED_V.nc, created 2019-01-17T00:40:57Z
- **Summary**: MOVE transport estimates dataset from UCSD mooring project
- **Data Type**: OceanSITES time-series data
- **Format Version**: 1.5
- **Update Interval**: void
- **Qc Indicator**: excellent
- **Area**: Tropical Atlantic Ocean
- **Geospatial Vertical Positive**: down
- **Geospatial Vertical Units**: dbar
- **Source File**: OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
- **Amocatlas Datasource**: move16n
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Contributor Url**: 
- **Program**: MOVE
- **Amocatlas Datasource**: move16n
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Platform Type**: 
- **Reference**: 
- **Weblink**: 
- **Source File**: OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
