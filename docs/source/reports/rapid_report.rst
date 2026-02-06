RAPID Dataset Report
====================

Generated: 2026-02-06

This report covers all available RAPID datasets.

moc_transports.nc
-----------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: RAPID-AMOC 26°N array
- **Institution**: Unknown
- **Description**: RAPID 26N transport estimates dataset
- **DOI**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Source File**: moc_transports.nc
- **Data Product**: RAPID layer transport time series
- **Time Coverage**: 1080864000.0 to 1711497600.0
- **Record Length**: 14,599 observations (630633600.0 years)
- **Sampling Frequency**: 1036800.0H

**Citation:**

    Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: http://doi.org/10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 9
- **Total Coordinates**: 1
- **Dataset Size**: 1.11 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-----------------------------------------+------------------------------------+----------+------------+------------+-----------+
| Coordinate | Standardized Name | Description                             | Units                              | Size     | Min Value  | Max Value  | Missing % |
+============+===================+=========================================+====================================+==========+============+============+===========+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (14599,) | 2004-04-02 | 2024-03-27 | 0.0%      |
+------------+-------------------+-----------------------------------------+------------------------------------+----------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                            | Units | Size     | Min Value | Max Value | Missing % |
+===================+===================+========================================================================+=======+==========+===========+===========+===========+
| t_therm10         | t_therm10         | **Transport**: Thermocline recirculation 0-800m                        | Sv    | (14599,) | -28.85    | -7.63     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_aiw10           | t_aiw10           | **Transport**: Intermediate water 800-1100m                            | Sv    | (14599,) | -2.17     | 2.82      | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_ud10            | t_ud10            | **Transport**: upper NADW 1100-3000m                                   | Sv    | (14599,) | -22.20    | -0.38     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_ld10            | t_ld10            | **Transport**: lower NADW 3000-5000m                                   | Sv    | (14599,) | -14.41    | 7.14      | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_bw10            | t_bw10            | **Transport**: AABW > 5000m                                            | Sv    | (14599,) | -0.60     | 3.46      | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_gs10            | t_gs10            | **Florida Straits Transport**: Florida Current from cable measurements | Sv    | (14599,) | 21.01     | 39.65     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_ek10            | t_ek10            | **Ekman Transport**: Ekman transport from wind stress                  | Sv    | (14599,) | -13.00    | 18.29     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| t_umo10           | t_umo10           | **Transport**: Upper Mid-Ocean transport                               | Sv    | (14599,) | -28.24    | -6.65     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+
| moc_mar_hc10      | moc_mar_hc10      | **overturning transport**: MOC strength                                | Sv    | (14599,) | -4.35     | 32.34     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+----------+-----------+-----------+-----------+


Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/moc_transports_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for MOC_TRANSPORTS dataset.

Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: RAPID MOC timeseries
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 1080864000.0
- **Time Coverage End**: 1711497600.0
- **Program**: RAPID
- **Project**: RAPID-AMOC 26°N array
- **Contributor Name**: Ben Moat, Ben Moat
- **Contributor Email**: ben.moat@noc.ac.uk, ben.moat@noc.ac.uk
- **Contributor Id**: , 
- **Contributor Role**: creator, PI
- **Contributing Institutions**: National Oceanography Centre, UK
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Web Link**: https://rapid.ac.uk/rapidmoc
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Date Created**: 17-Sep-2024
- **Featuretype**: timeSeries
- **Description**: RAPID 26N transport estimates dataset
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **License**: CC-BY 4.0
- **Conventions**: CF-1.8, ACDD-1.3
- **Version**: 2024.1a
- **Data Product**: RAPID layer transport time series
- **Variable Mapping**: {'time': 'TIME'}
- **Source File**: moc_transports.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/moc_transports.nc
- **Amocatlas Datasource**: rapid26n
- **Summary**: RAPID 26N transport estimates dataset
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Time Coverage End**: 2024-03-27
- **Program**: RAPID
- **Institution**: 
- **License**: CC-BY 4.0
- **Amocatlas Datasource**: rapid26n
- **Citation**: Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Source File**: moc_transports.nc
- **Platform Type**: 
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Description**: RAPID 26N transport estimates dataset
- **Time Coverage Start**: 2004-04-01
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **Creator Email**: 
- **Creator Name**: 
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/moc_transports.nc
- **Project**: RAPID-AMOC 26°N array
- **Data Product**: RAPID layer transport time series
- **Weblink**: 
- **Conventions**: CF-1.8, ACDD-1.3
- **Variable Mapping**: {'time': 'TIME'}
- **Featuretype**: timeSeries

Dataset Overview
^^^^^^^^^^^^^^^^

- **Source File**: moc_vertical.nc
- **Error**: Could not generate full analysis - cannot access local variable 'pd' where it is not associated with a value

Dataset Overview
^^^^^^^^^^^^^^^^

- **Source File**: ts_gridded.nc
- **Error**: Could not generate full analysis - cannot access local variable 'pd' where it is not associated with a value

Dataset Overview
^^^^^^^^^^^^^^^^

- **Source File**: 2d_gridded.nc
- **Error**: Could not generate full analysis - cannot access local variable 'pd' where it is not associated with a value

Dataset Overview
^^^^^^^^^^^^^^^^

- **Source File**: meridional_transports.nc
- **Error**: Could not generate full analysis - cannot access local variable 'pd' where it is not associated with a value
