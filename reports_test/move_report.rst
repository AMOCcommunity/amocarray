MOVE Dataset Report
===================

Generated: 2026-02-06

This report covers all available MOVE datasets.

OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Institution**: Unknown
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **DOI**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Source File**: OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Data Product**: MOVE transport time series
- **Time Coverage**: -9223372036854775808.0 to 1665705600.0
- **Record Length**: 4,164 observations (9223372038520481792.0 years)
- **Sampling Frequency**: 4147200.0H

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

+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-------------------------+---------------+-----------+
| Coordinate                | Standardized Name         | Description                             | Units                              | Size    | Min Value               | Max Value     | Missing % |
+===========================+===========================+=========================================+====================================+=========+=========================+===============+===========+
| TIME                      | TIME                      | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (4164,) | -9223372036854775808.00 | 1665705600.00 | 0.0%      |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-------------------------+---------------+-----------+
| location_center_latitude  | location_center_latitude  | No description available                | degrees_north                      | ()      | 16.04                   | 16.04         | 0.0%      |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-------------------------+---------------+-----------+
| location_center_longitude | location_center_longitude | No description available                | degrees_east                       | ()      | -57.56                  | -57.56        | 0.0%      |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-------------------------+---------------+-----------+
| location_center_vertical  | location_center_vertical  | No description available                | dbar                               | ()      | 2750.00                 | 2750.00       | 0.0%      |
+---------------------------+---------------------------+-----------------------------------------+------------------------------------+---------+-------------------------+---------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| Original Variable                   | Standardized Name                   | Description                                                                                            | Units         | Size    | Min Value | Max Value                                | Missing % |
+=====================================+=====================================+========================================================================================================+===============+=========+===========+==========================================+===========+
| TRANSPORT_TOTAL                     | TRANSPORT_TOTAL                     | Ocean volume transport across the MOVE line                                                            | Sverdrup      | (4164,) | -31.86    | 9969209968386869046778552952102584320.00 | 3.8%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| transport_component_internal        | transport_component_internal        | **Transport**: Internal component of ocean volume transport across the MOVE line                       | Sv            | (4164,) | -35.46    | 9969209968386869046778552952102584320.00 | 3.6%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| transport_component_internal_offset | transport_component_internal_offset | **Transport**: Offset to be added to internal component of ocean volume transport across the MOVE line | Sv            | (4164,) | 5.78      | 9969209968386869046778552952102584320.00 | 1.8%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| transport_component_boundary        | transport_component_boundary        | **Transport**: Boundary component of ocean volume transport across the MOVE line                       | Sv            | (4164,) | -10.98    | 9969209968386869046778552952102584320.00 | 1.2%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| location_geometry                   | location_geometry                   | No description available                                                                               | unknown       | ()      | 0.00      | 0.00                                     | 0.0%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| location_vertices_latitude          | location_vertices_latitude          | No description available                                                                               | degrees_north | (6,)    | 15.45     | 16.33                                    | 0.0%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| location_vertices_longitude         | location_vertices_longitude         | No description available                                                                               | degrees_east  | (6,)    | -60.72    | -51.51                                   | 0.0%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+
| location_vertices_vertical          | location_vertices_vertical          | No description available                                                                               | dbar          | (6,)    | 1200.00   | 4950.00                                  | 0.0%      |
+-------------------------------------+-------------------------------------+--------------------------------------------------------------------------------------------------------+---------------+---------+-----------+------------------------------------------+-----------+


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
- **Time Coverage Start**: -9223372036854775808.0
- **Time Coverage End**: 1665705600.0
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
- **Data Product**: MOVE transport time series
- **Summary**: MOVE transport estimates dataset from UCSD mooring project
- **Source File**: OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Amocatlas Datasource**: move16n
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Program**: MOVE
- **Weblink**: 
- **Time Coverage Start**: 2000-01-01
- **Reference**: 
- **Amocatlas Datasource**: move16n
- **Source File**: OS_MOVE_20000206-20221014_DPR_VOLUMETRANSPORT.nc
- **Data Product**: MOVE transport time series
- **Platform Type**: 
- **Time Coverage End**: 2018-06-30
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Contributor Url**: 

OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
--------------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Institution**: Unknown
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **DOI**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Source File**: OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
- **Time Coverage**: 946684800.0 to 1666310400.0
- **Record Length**: 8,330 observations (719625600.0 years)
- **Sampling Frequency**: 2073600.0H

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

+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| Coordinate | Standardized Name | Description                                                    | Units                              | Size    | Min Value    | Max Value     | Missing % |
+============+===================+================================================================+====================================+=========+==============+===============+===========+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z                        | seconds since 1970-01-01T00:00:00Z | (8330,) | 946684800.00 | 1666310400.00 | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| PRESSURE   | PRESSURE          | Sea water pressure due to sea water, i.e. air pressure removed | dbar                               | (38,)   | 1250.00      | 4950.00       | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| LATITUDE   | LATITUDE          | Nominal latitude of site                                       | degree_north                       | (2,)    | 16.33        | 16.34         | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| LONGITUDE  | LONGITUDE         | Nominal longitude of site                                      | degree_east                        | (2,)    | -60.61       | -60.51        | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| Original Variable             | Standardized Name             | Description                                                        | Units        | Size          | Min Value | Max Value | Missing % |
+===============================+===============================+====================================================================+==============+===============+===========+===========+===========+
| latitude_time_varying         | latitude_time_varying         | Latitude of site, including differences between deployments        | degree_north | (2, 8330)     | 16.33     | 16.36     | 1.1%      |
+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| longitude_time_varying        | longitude_time_varying        | Longitude of site, including differences between deployments       | degree_east  | (2, 8330)     | -60.61    | -60.49    | 1.1%      |
+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| instrument_depth_time_varying | instrument_depth_time_varying | Estimated instrument depths                                        | m            | (2, 8330, 8)  | 160.17    | 4970.03   | 1.2%      |
+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| platform_name                 | platform_name                 | Official OceanSITES platform names                                 | unknown      | (5, 2)        | N/A       | N/A       | 0.0%      |
+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| VELOCITY_U                    | VELOCITY_U                    | Seawater velocity in east-west direction, positive towards east    | m s-1        | (2, 8330, 38) | -0.31     | 0.41      | 1.2%      |
+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| VELOCITY_V                    | VELOCITY_V                    | Seawater velocity in north-south direction, positive towards north | m s-1        | (2, 8330, 38) | -0.56     | 0.35      | 1.2%      |
+-------------------------------+-------------------------------+--------------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+


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
- **Time Coverage Start**: 946684800.0
- **Time Coverage End**: 1666310400.0
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
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Program**: MOVE
- **Weblink**: 
- **Source File**: OS_MOVE_20000101-20221021_GRD_CURRENTS-AT-SITES-MOVE3-MOVE4.nc
- **Reference**: 
- **Amocatlas Datasource**: move16n
- **Platform Type**: 
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Contributor Url**: 

OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
--------------------------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Meridional Overturning Variability Experiment (MOVE)
- **Institution**: Unknown
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **DOI**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Source File**: OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
- **Time Coverage**: 946684800.0 to 1666051200.0
- **Record Length**: 4,164 observations (719366400.0 years)
- **Sampling Frequency**: 4147200.0H

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

+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| Coordinate | Standardized Name | Description                                                    | Units                              | Size    | Min Value    | Max Value     | Missing % |
+============+===================+================================================================+====================================+=========+==============+===============+===========+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z                        | seconds since 1970-01-01T00:00:00Z | (4164,) | 946684800.00 | 1666051200.00 | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| PRESSURE   | PRESSURE          | Sea water pressure due to sea water, i.e. air pressure removed | dbar                               | (99,)   | 50.00        | 4950.00       | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| LATITUDE   | LATITUDE          | Nominal latitude of site                                       | degree_north                       | (2,)    | 15.45        | 16.34         | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+
| LONGITUDE  | LONGITUDE         | Nominal longitude of site                                      | degree_east                        | (2,)    | -60.51       | -51.51        | 0.0%      |
+------------+-------------------+----------------------------------------------------------------+------------------------------------+---------+--------------+---------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| Original Variable             | Standardized Name             | Description                                                    | Units        | Size          | Min Value | Max Value | Missing % |
+===============================+===============================+================================================================+==============+===============+===========+===========+===========+
| latitude_time_varying         | latitude_time_varying         | Latitude of site, including differences between deployments    | degree_north | (2, 4164)     | 15.32     | 16.34     | 0.6%      |
+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| longitude_time_varying        | longitude_time_varying        | Longitude of site, including differences between deployments   | degree_east  | (2, 4164)     | -60.52    | -51.50    | 0.6%      |
+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| instrument_depth_time_varying | instrument_depth_time_varying | Estimated instrument depths                                    | m            | (2, 4164, 22) | 4.97      | 5312.91   | 0.6%      |
+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| platform_name                 | platform_name                 | Official OceanSITES platform name                              | unknown      | (5, 2)        | N/A       | N/A       | 0.0%      |
+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| TEMPERATURE                   | TEMPERATURE                   | Temperature of sea water on the ITS-90 scale                   | degree_C     | (2, 4164, 99) | 1.84      | 29.26     | 0.6%      |
+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+
| SALINITY                      | SALINITY                      | Salinity of sea water reported on the practical salinity scale | 1            | (2, 4164, 99) | 33.88     | 37.48     | 0.6%      |
+-------------------------------+-------------------------------+----------------------------------------------------------------+--------------+---------------+-----------+-----------+-----------+


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
- **Time Coverage Start**: 946684800.0
- **Time Coverage End**: 1666051200.0
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
- **Doi**: http://dx.doi.org/10.1016/j.dsr.2005.12.007 http://dx.doi.org/10.1029/2011GL049801
- **Program**: MOVE
- **Weblink**: 
- **Source File**: OS_MOVE_20000101-20221018_GRD_TEMPERATURE-SALINITY-AT-SITES-MOVE1-MOVE3.nc
- **Reference**: 
- **Amocatlas Datasource**: move16n
- **Platform Type**: 
- **Description**: MOVE transport estimates dataset from UCSD mooring project
- **Contributor Url**: 
