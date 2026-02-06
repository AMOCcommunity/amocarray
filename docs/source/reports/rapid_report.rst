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
- **Time Coverage**: 2004-04-02 to 2024-03-27
- **Record Length**: 14,599 observations (20.0 years)
- **Sampling Frequency**: 12H

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

+------------+-------------------+--------------+------------------------------------+-------+------------+------------+-----------+
| Coordinate | Standardized Name | Description  | Units                              | Size  | Min Value  | Max Value  | Missing % |
+============+===================+==============+====================================+=======+============+============+===========+
| TIME       | TIME              | time in days | seconds since 1970-01-01T00:00:00Z | 14599 | 2004-04-02 | 2024-03-27 | 0.0%      |
+------------+-------------------+--------------+------------------------------------+-------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                            | Units | Size  | Min Value | Max Value | Missing % |
+===================+===================+========================================================================+=======+=======+===========+===========+===========+
| t_therm10         | t_therm10         | **Transport**: Thermocline recirculation 0-800m                        | Sv    | 14599 | -28.85    | -7.63     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_aiw10           | t_aiw10           | **Transport**: Intermediate water 800-1100m                            | Sv    | 14599 | -2.17     | 2.82      | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_ud10            | t_ud10            | **Transport**: upper NADW 1100-3000m                                   | Sv    | 14599 | -22.20    | -0.38     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_ld10            | t_ld10            | **Transport**: lower NADW 3000-5000m                                   | Sv    | 14599 | -14.41    | 7.14      | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_bw10            | t_bw10            | **Transport**: AABW > 5000m                                            | Sv    | 14599 | -0.60     | 3.46      | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_gs10            | t_gs10            | **Florida Straits Transport**: Florida Current from cable measurements | Sv    | 14599 | 21.01     | 39.65     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_ek10            | t_ek10            | **Ekman Transport**: Ekman transport from wind stress                  | Sv    | 14599 | -13.00    | 18.29     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| t_umo10           | t_umo10           | **Transport**: Upper Mid-Ocean transport                               | Sv    | 14599 | -28.24    | -6.65     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+
| moc_mar_hc10      | moc_mar_hc10      | **overturning transport**: MOC strength                                | Sv    | 14599 | -4.35     | 32.34     | 0.1%      |
+-------------------+-------------------+------------------------------------------------------------------------+-------+-------+-----------+-----------+-----------+


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
- **Time Coverage Start**: 2004-04-02
- **Time Coverage End**: 2024-03-27
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

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/moc_transports.nc
- **Weblink**: 
- **Source File**: moc_transports.nc
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Featuretype**: timeSeries
- **Description**: RAPID 26N transport estimates dataset
- **Time Coverage Start**: 2004-04-01
- **Platform Type**: 
- **Amocatlas Datasource**: rapid26n
- **Project**: RAPID-AMOC 26°N array
- **Files**: {'moc_transports.nc': {'data_product': 'RAPID layer transport time series', 'variable_mapping': {'time': 'TIME'}, 'variables': {'t_therm10': {'long_name': 'Transport', 'description': 'Thermocline recirculation 0-800m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_aiw10': {'long_name': 'Transport', 'description': 'Intermediate water 800-1100m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ud10': {'long_name': 'Transport', 'description': 'upper NADW 1100-3000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ld10': {'long_name': 'Transport', 'description': 'lower NADW 3000-5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_bw10': {'long_name': 'Transport', 'description': 'AABW > 5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_gs10': {'long_name': 'Florida Straits Transport', 'description': 'Florida Current from cable measurements', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ek10': {'long_name': 'Ekman Transport', 'description': 'Ekman transport from wind stress', 'units': 'Sv', 'standard_name': 'Transport'}, 't_umo10': {'long_name': 'Transport', 'description': 'Upper Mid-Ocean transport', 'units': 'Sv', 'standard_name': 'Transport'}, 'moc_mar_hc10': {'long_name': 'overturning transport', 'description': 'MOC strength', 'units': 'Sv', 'standard_name': 'Transport'}}}, 'ts_gridded.nc': {'data_product': 'RAPID gridded temperature and salinity', 'source_file': 'ts_gridded.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/ts_gridded.nc', 'variable_mapping': {}, 'variables': {'TG_west': {'long_name': 'Temperature west 26.52N/76.74W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_west': {'long_name': 'Salinity west 26.52N/76.74W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_wb3': {'long_name': 'Temperature WB3 26.50N/76.50W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_wb3': {'long_name': 'Salinity WB3 26.50N/76.50W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_east': {'long_name': 'Temperature east 26.99N/16.23W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_east': {'long_name': 'Salinity east 26.99N/16.23W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_marwest': {'long_name': 'Temperature MAR west 24.52N/50.57W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_marwest': {'long_name': 'Salinity MAR west 24.52N/50.57W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_mareast': {'long_name': 'Temperature MAR east 24.52N/41.21W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_mareast': {'long_name': 'Salinity MAR east 24.52N/41.21W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}}}, 'moc_vertical.nc': {'data_product': 'RAPID vertical streamfunction time series', 'source_file': 'moc_vertical.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/moc_vertical.nc', 'variable_mapping': {}, 'variables': {'stream_function_mar': {'long_name': 'Meridional overturning', 'description': 'Streamfunction across the Atlantic at 26.5°N', 'units': 'Sv', 'standard_name': 'Transport'}}}, '2d_gridded.nc': {'data_product': 'RAPID 2D gridded data', 'source_file': '2d_gridded.nc', 'variable_mapping': {}, 'variables': {'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'area': {'long_name': 'Grid cell area', 'description': 'Area of each grid cell', 'units': 'm2'}, 'CT': {'long_name': 'Conservative temperature', 'description': 'Conservative temperature following TEOS-10 standard', 'units': 'degC', 'standard_name': 'sea_water_conservative_temperature'}, 'SA': {'long_name': 'Absolute salinity', 'description': 'Absolute salinity following TEOS-10 standard', 'units': 'g/kg', 'standard_name': 'sea_water_absolute_salinity'}, 'V_insitu': {'long_name': 'In-situ velocity', 'description': 'In-situ meridional velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_ekman': {'long_name': 'Ekman velocity', 'description': 'Ekman transport velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_net': {'long_name': 'Net velocity', 'description': 'Net meridional velocity (in-situ + Ekman)', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}}, 'coordinates': {'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'longitude': {'long_name': 'Longitude', 'description': 'Longitude coordinate', 'units': 'degrees_east', 'standard_name': 'longitude'}, 'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}}}, 'meridional_transports.nc': {'data_product': 'RAPID meridional transport data', 'source_file': 'meridional_transports.nc', 'variable_mapping': {}, 'variables': {'amoc_depth': {'long_name': 'AMOC strength in depth coordinates', 'description': 'Atlantic meridional overturning circulation strength in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma0': {'long_name': 'AMOC strength in sigma0 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma2': {'long_name': 'AMOC strength in sigma2 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'heat_trans': {'long_name': 'Meridional heat transport', 'description': 'Northward oceanic heat transport', 'units': 'PW', 'standard_name': 'northward_ocean_heat_transport'}, 'frwa_trans': {'long_name': 'Freshwater transport', 'description': 'Meridional freshwater transport', 'units': 'Sv'}, 'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'stream_depth': {'long_name': 'Streamfunction in depth coordinates', 'description': 'Meridional overturning streamfunction in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma0': {'long_name': 'Streamfunction in sigma0 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma2': {'long_name': 'Streamfunction in sigma2 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}}, 'coordinates': {'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}, 'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'sigma0': {'long_name': 'Potential density anomaly (sigma-theta)', 'description': 'Potential density anomaly referenced to surface (sigma-theta), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_theta'}, 'sigma2': {'long_name': 'Potential density anomaly (sigma-2)', 'description': 'Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_2'}}}}
- **Conventions**: CF-1.8, ACDD-1.3
- **Creator Email**: 
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **License**: CC-BY 4.0
- **Time Coverage End**: 2024-03-27
- **Data Product**: RAPID layer transport time series
- **Program**: RAPID
- **Creator Name**: 
- **Citation**: Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Variables**: {'t_therm10': {'long_name': 'Transport', 'description': 'Thermocline recirculation 0-800m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_aiw10': {'long_name': 'Transport', 'description': 'Intermediate water 800-1100m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ud10': {'long_name': 'Transport', 'description': 'upper NADW 1100-3000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ld10': {'long_name': 'Transport', 'description': 'lower NADW 3000-5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_bw10': {'long_name': 'Transport', 'description': 'AABW > 5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_gs10': {'long_name': 'Florida Straits Transport', 'description': 'Florida Current from cable measurements', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ek10': {'long_name': 'Ekman Transport', 'description': 'Ekman transport from wind stress', 'units': 'Sv', 'standard_name': 'Transport'}, 't_umo10': {'long_name': 'Transport', 'description': 'Upper Mid-Ocean transport', 'units': 'Sv', 'standard_name': 'Transport'}, 'moc_mar_hc10': {'long_name': 'overturning transport', 'description': 'MOC strength', 'units': 'Sv', 'standard_name': 'Transport'}}
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **Institution**: 
- **Variable Mapping**: {'time': 'TIME'}

moc_vertical.nc
---------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: RAPID-AMOC 26°N array
- **Institution**: Unknown
- **Description**: RAPID 26N transport estimates dataset
- **DOI**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Source File**: moc_vertical.nc
- **Data Product**: RAPID vertical streamfunction time series
- **Time Coverage**: 2004-04-02 to 2024-03-27
- **Record Length**: 14,599 observations (20.0 years)
- **Sampling Frequency**: 12H

**Citation:**

    Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: http://doi.org/10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 1
- **Total Coordinates**: 2
- **Dataset Size**: 34.31 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-------------+----------------+-------+------------+------------+-----------+
| Coordinate | Standardized Name | Description | Units          | Size  | Min Value  | Max Value  | Missing % |
+============+===================+=============+================+=======+============+============+===========+
| time       | time              | time        | datetime64[ns] | 14599 | 2004-04-02 | 2024-03-27 | 0.0%      |
+------------+-------------------+-------------+----------------+-------+------------+------------+-----------+
| depth      | depth             | depth       | m              | 307   | 0.00       | 5995.07    | 0.0%      |
+------------+-------------------+-------------+----------------+-------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+---------------------+---------------------+--------------------------------------------------------------------------+-------+---------+-----------+-----------+-----------+
| Original Variable   | Standardized Name   | Description                                                              | Units | Size    | Min Value | Max Value | Missing % |
+=====================+=====================+==========================================================================+=======+=========+===========+===========+===========+
| stream_function_mar | stream_function_mar | **Meridional overturning**: Streamfunction across the Atlantic at 26.5°N | Sv    | 4481893 | -17.34    | 37.79     | 0.0%      |
+---------------------+---------------------+--------------------------------------------------------------------------+-------+---------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: RAPID streamfunction
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 2004-04-02
- **Time Coverage End**: 2024-03-27
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
- **Data Product**: RAPID vertical streamfunction time series
- **Source File**: moc_vertical.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/moc_vertical.nc
- **Variable Mapping**: {}
- **Amocatlas Datasource**: rapid26n
- **Summary**: RAPID 26N transport estimates dataset
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/moc_vertical.nc
- **Weblink**: 
- **Source File**: moc_vertical.nc
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Featuretype**: timeSeries
- **Description**: RAPID 26N transport estimates dataset
- **Time Coverage Start**: 2004-04-01
- **Platform Type**: 
- **Amocatlas Datasource**: rapid26n
- **Project**: RAPID-AMOC 26°N array
- **Files**: {'moc_transports.nc': {'data_product': 'RAPID layer transport time series', 'variable_mapping': {'time': 'TIME'}, 'variables': {'t_therm10': {'long_name': 'Transport', 'description': 'Thermocline recirculation 0-800m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_aiw10': {'long_name': 'Transport', 'description': 'Intermediate water 800-1100m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ud10': {'long_name': 'Transport', 'description': 'upper NADW 1100-3000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ld10': {'long_name': 'Transport', 'description': 'lower NADW 3000-5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_bw10': {'long_name': 'Transport', 'description': 'AABW > 5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_gs10': {'long_name': 'Florida Straits Transport', 'description': 'Florida Current from cable measurements', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ek10': {'long_name': 'Ekman Transport', 'description': 'Ekman transport from wind stress', 'units': 'Sv', 'standard_name': 'Transport'}, 't_umo10': {'long_name': 'Transport', 'description': 'Upper Mid-Ocean transport', 'units': 'Sv', 'standard_name': 'Transport'}, 'moc_mar_hc10': {'long_name': 'overturning transport', 'description': 'MOC strength', 'units': 'Sv', 'standard_name': 'Transport'}}}, 'ts_gridded.nc': {'data_product': 'RAPID gridded temperature and salinity', 'source_file': 'ts_gridded.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/ts_gridded.nc', 'variable_mapping': {}, 'variables': {'TG_west': {'long_name': 'Temperature west 26.52N/76.74W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_west': {'long_name': 'Salinity west 26.52N/76.74W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_wb3': {'long_name': 'Temperature WB3 26.50N/76.50W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_wb3': {'long_name': 'Salinity WB3 26.50N/76.50W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_east': {'long_name': 'Temperature east 26.99N/16.23W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_east': {'long_name': 'Salinity east 26.99N/16.23W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_marwest': {'long_name': 'Temperature MAR west 24.52N/50.57W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_marwest': {'long_name': 'Salinity MAR west 24.52N/50.57W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_mareast': {'long_name': 'Temperature MAR east 24.52N/41.21W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_mareast': {'long_name': 'Salinity MAR east 24.52N/41.21W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}}}, 'moc_vertical.nc': {'data_product': 'RAPID vertical streamfunction time series', 'source_file': 'moc_vertical.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/moc_vertical.nc', 'variable_mapping': {}, 'variables': {'stream_function_mar': {'long_name': 'Meridional overturning', 'description': 'Streamfunction across the Atlantic at 26.5°N', 'units': 'Sv', 'standard_name': 'Transport'}}}, '2d_gridded.nc': {'data_product': 'RAPID 2D gridded data', 'source_file': '2d_gridded.nc', 'variable_mapping': {}, 'variables': {'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'area': {'long_name': 'Grid cell area', 'description': 'Area of each grid cell', 'units': 'm2'}, 'CT': {'long_name': 'Conservative temperature', 'description': 'Conservative temperature following TEOS-10 standard', 'units': 'degC', 'standard_name': 'sea_water_conservative_temperature'}, 'SA': {'long_name': 'Absolute salinity', 'description': 'Absolute salinity following TEOS-10 standard', 'units': 'g/kg', 'standard_name': 'sea_water_absolute_salinity'}, 'V_insitu': {'long_name': 'In-situ velocity', 'description': 'In-situ meridional velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_ekman': {'long_name': 'Ekman velocity', 'description': 'Ekman transport velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_net': {'long_name': 'Net velocity', 'description': 'Net meridional velocity (in-situ + Ekman)', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}}, 'coordinates': {'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'longitude': {'long_name': 'Longitude', 'description': 'Longitude coordinate', 'units': 'degrees_east', 'standard_name': 'longitude'}, 'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}}}, 'meridional_transports.nc': {'data_product': 'RAPID meridional transport data', 'source_file': 'meridional_transports.nc', 'variable_mapping': {}, 'variables': {'amoc_depth': {'long_name': 'AMOC strength in depth coordinates', 'description': 'Atlantic meridional overturning circulation strength in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma0': {'long_name': 'AMOC strength in sigma0 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma2': {'long_name': 'AMOC strength in sigma2 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'heat_trans': {'long_name': 'Meridional heat transport', 'description': 'Northward oceanic heat transport', 'units': 'PW', 'standard_name': 'northward_ocean_heat_transport'}, 'frwa_trans': {'long_name': 'Freshwater transport', 'description': 'Meridional freshwater transport', 'units': 'Sv'}, 'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'stream_depth': {'long_name': 'Streamfunction in depth coordinates', 'description': 'Meridional overturning streamfunction in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma0': {'long_name': 'Streamfunction in sigma0 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma2': {'long_name': 'Streamfunction in sigma2 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}}, 'coordinates': {'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}, 'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'sigma0': {'long_name': 'Potential density anomaly (sigma-theta)', 'description': 'Potential density anomaly referenced to surface (sigma-theta), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_theta'}, 'sigma2': {'long_name': 'Potential density anomaly (sigma-2)', 'description': 'Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_2'}}}}
- **Conventions**: CF-1.8, ACDD-1.3
- **Creator Email**: 
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **License**: CC-BY 4.0
- **Time Coverage End**: 2024-03-27
- **Data Product**: RAPID vertical streamfunction time series
- **Program**: RAPID
- **Creator Name**: 
- **Citation**: Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Variables**: {'stream_function_mar': {'long_name': 'Meridional overturning', 'description': 'Streamfunction across the Atlantic at 26.5°N', 'units': 'Sv', 'standard_name': 'Transport'}}
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **Institution**: 
- **Variable Mapping**: {}

ts_gridded.nc
-------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: RAPID-AMOC 26°N array
- **Institution**: Unknown
- **Description**: RAPID 26N transport estimates dataset
- **DOI**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Source File**: ts_gridded.nc
- **Data Product**: RAPID gridded temperature and salinity
- **Time Coverage**: 2004-04-02 to 2024-03-27
- **Record Length**: 14,599 observations (20.0 years)
- **Sampling Frequency**: 12H

**Citation:**

    Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: http://doi.org/10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 19
- **Total Coordinates**: 1
- **Dataset Size**: 485.29 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-------------+----------------+-------+------------+------------+-----------+
| Coordinate | Standardized Name | Description | Units          | Size  | Min Value  | Max Value  | Missing % |
+============+===================+=============+================+=======+============+============+===========+
| time       | time              | time        | datetime64[ns] | 14599 | 2004-04-02 | 2024-03-27 | 0.0%      |
+------------+-------------------+-------------+----------------+-------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                        | Units     | Size    | Min Value | Max Value | Missing % |
+===================+===================+====================================+===========+=========+===========+===========+===========+
| pressure          | pressure          | No description available           | dbar      | 242     | 0.00      | 4820.00   | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_west           | TG_west           | Temperature west 26.52N/76.74W     | degC      | 3532958 | 2.16      | 29.23     | 0.4%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_west           | SG_west           | Salinity west 26.52N/76.74W        | psu       | 3532958 | 34.87     | 37.11     | 0.4%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_wb3            | TG_wb3            | Temperature WB3 26.50N/76.50W      | degC      | 3532958 | 2.15      | 28.77     | 1.2%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_wb3            | SG_wb3            | Salinity WB3 26.50N/76.50W         | psu       | 3532958 | 34.87     | 37.06     | 1.2%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_east           | TG_east           | Temperature east 26.99N/16.23W     | degC      | 3532958 | 2.36      | 23.74     | 0.8%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_east           | SG_east           | Salinity east 26.99N/16.23W        | psu       | 3532958 | 34.89     | 36.96     | 0.8%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_marwest        | TG_marwest        | Temperature MAR west 24.52N/50.57W | degC      | 3532958 | 2.12      | 28.80     | 0.8%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_marwest        | SG_marwest        | Salinity MAR west 24.52N/50.57W    | psu       | 3532958 | 34.86     | 37.78     | 0.8%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_mareast        | TG_mareast        | Temperature MAR east 24.52N/41.21W | degC      | 3532958 | 2.36      | 3.29      | 50.4%     |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_mareast        | SG_mareast        | Salinity MAR east 24.52N/41.21W    | psu       | 3532958 | 34.88     | 34.98     | 50.4%     |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_west_flag      | TG_west_flag      | Temperature east data FLAG         | data flag | 3532958 | 0.00      | 1.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_west_flag      | SG_west_flag      | Salinity east data FLAG            | data flag | 3532958 | 0.00      | 1.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_east_flag      | TG_east_flag      | Temperature MAR west data FLAG     | data flag | 3532958 | 0.00      | 2.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_east_flag      | SG_east_flag      | Salinity MAR west data FLAG        | data flag | 3532958 | 0.00      | 2.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_marwest_flag   | TG_marwest_flag   | Temperature MAR east data FLAG     | data flag | 3532958 | 0.00      | 2.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_marwest_flag   | SG_marwest_flag   | Salinity MAR east data FLAG        | data flag | 3532958 | 0.00      | 2.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| TG_mareast_flag   | TG_mareast_flag   | Temperature MAR east data FLAG     | data flag | 3532958 | 0.00      | 2.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+
| SG_mareast_flag   | SG_mareast_flag   | Salinity MAR east data FLAG        | data flag | 3532958 | 0.00      | 2.00      | 0.0%      |
+-------------------+-------------------+------------------------------------+-----------+---------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: RAPID streamfunction
- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 2004-04-02
- **Time Coverage End**: 2024-03-27
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
- **Data Product**: RAPID gridded temperature and salinity
- **Source File**: ts_gridded.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/ts_gridded.nc
- **Variable Mapping**: {}
- **Amocatlas Datasource**: rapid26n
- **Summary**: RAPID 26N transport estimates dataset
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/ts_gridded.nc
- **Weblink**: 
- **Source File**: ts_gridded.nc
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Featuretype**: timeSeries
- **Description**: RAPID 26N transport estimates dataset
- **Time Coverage Start**: 2004-04-01
- **Platform Type**: 
- **Amocatlas Datasource**: rapid26n
- **Project**: RAPID-AMOC 26°N array
- **Files**: {'moc_transports.nc': {'data_product': 'RAPID layer transport time series', 'variable_mapping': {'time': 'TIME'}, 'variables': {'t_therm10': {'long_name': 'Transport', 'description': 'Thermocline recirculation 0-800m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_aiw10': {'long_name': 'Transport', 'description': 'Intermediate water 800-1100m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ud10': {'long_name': 'Transport', 'description': 'upper NADW 1100-3000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ld10': {'long_name': 'Transport', 'description': 'lower NADW 3000-5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_bw10': {'long_name': 'Transport', 'description': 'AABW > 5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_gs10': {'long_name': 'Florida Straits Transport', 'description': 'Florida Current from cable measurements', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ek10': {'long_name': 'Ekman Transport', 'description': 'Ekman transport from wind stress', 'units': 'Sv', 'standard_name': 'Transport'}, 't_umo10': {'long_name': 'Transport', 'description': 'Upper Mid-Ocean transport', 'units': 'Sv', 'standard_name': 'Transport'}, 'moc_mar_hc10': {'long_name': 'overturning transport', 'description': 'MOC strength', 'units': 'Sv', 'standard_name': 'Transport'}}}, 'ts_gridded.nc': {'data_product': 'RAPID gridded temperature and salinity', 'source_file': 'ts_gridded.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/ts_gridded.nc', 'variable_mapping': {}, 'variables': {'TG_west': {'long_name': 'Temperature west 26.52N/76.74W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_west': {'long_name': 'Salinity west 26.52N/76.74W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_wb3': {'long_name': 'Temperature WB3 26.50N/76.50W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_wb3': {'long_name': 'Salinity WB3 26.50N/76.50W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_east': {'long_name': 'Temperature east 26.99N/16.23W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_east': {'long_name': 'Salinity east 26.99N/16.23W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_marwest': {'long_name': 'Temperature MAR west 24.52N/50.57W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_marwest': {'long_name': 'Salinity MAR west 24.52N/50.57W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_mareast': {'long_name': 'Temperature MAR east 24.52N/41.21W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_mareast': {'long_name': 'Salinity MAR east 24.52N/41.21W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}}}, 'moc_vertical.nc': {'data_product': 'RAPID vertical streamfunction time series', 'source_file': 'moc_vertical.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/moc_vertical.nc', 'variable_mapping': {}, 'variables': {'stream_function_mar': {'long_name': 'Meridional overturning', 'description': 'Streamfunction across the Atlantic at 26.5°N', 'units': 'Sv', 'standard_name': 'Transport'}}}, '2d_gridded.nc': {'data_product': 'RAPID 2D gridded data', 'source_file': '2d_gridded.nc', 'variable_mapping': {}, 'variables': {'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'area': {'long_name': 'Grid cell area', 'description': 'Area of each grid cell', 'units': 'm2'}, 'CT': {'long_name': 'Conservative temperature', 'description': 'Conservative temperature following TEOS-10 standard', 'units': 'degC', 'standard_name': 'sea_water_conservative_temperature'}, 'SA': {'long_name': 'Absolute salinity', 'description': 'Absolute salinity following TEOS-10 standard', 'units': 'g/kg', 'standard_name': 'sea_water_absolute_salinity'}, 'V_insitu': {'long_name': 'In-situ velocity', 'description': 'In-situ meridional velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_ekman': {'long_name': 'Ekman velocity', 'description': 'Ekman transport velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_net': {'long_name': 'Net velocity', 'description': 'Net meridional velocity (in-situ + Ekman)', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}}, 'coordinates': {'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'longitude': {'long_name': 'Longitude', 'description': 'Longitude coordinate', 'units': 'degrees_east', 'standard_name': 'longitude'}, 'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}}}, 'meridional_transports.nc': {'data_product': 'RAPID meridional transport data', 'source_file': 'meridional_transports.nc', 'variable_mapping': {}, 'variables': {'amoc_depth': {'long_name': 'AMOC strength in depth coordinates', 'description': 'Atlantic meridional overturning circulation strength in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma0': {'long_name': 'AMOC strength in sigma0 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma2': {'long_name': 'AMOC strength in sigma2 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'heat_trans': {'long_name': 'Meridional heat transport', 'description': 'Northward oceanic heat transport', 'units': 'PW', 'standard_name': 'northward_ocean_heat_transport'}, 'frwa_trans': {'long_name': 'Freshwater transport', 'description': 'Meridional freshwater transport', 'units': 'Sv'}, 'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'stream_depth': {'long_name': 'Streamfunction in depth coordinates', 'description': 'Meridional overturning streamfunction in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma0': {'long_name': 'Streamfunction in sigma0 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma2': {'long_name': 'Streamfunction in sigma2 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}}, 'coordinates': {'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}, 'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'sigma0': {'long_name': 'Potential density anomaly (sigma-theta)', 'description': 'Potential density anomaly referenced to surface (sigma-theta), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_theta'}, 'sigma2': {'long_name': 'Potential density anomaly (sigma-2)', 'description': 'Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_2'}}}}
- **Conventions**: CF-1.8, ACDD-1.3
- **Creator Email**: 
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **License**: CC-BY 4.0
- **Time Coverage End**: 2024-03-27
- **Data Product**: RAPID gridded temperature and salinity
- **Program**: RAPID
- **Creator Name**: 
- **Citation**: Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Variables**: {'TG_west': {'long_name': 'Temperature west 26.52N/76.74W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_west': {'long_name': 'Salinity west 26.52N/76.74W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_wb3': {'long_name': 'Temperature WB3 26.50N/76.50W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_wb3': {'long_name': 'Salinity WB3 26.50N/76.50W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_east': {'long_name': 'Temperature east 26.99N/16.23W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_east': {'long_name': 'Salinity east 26.99N/16.23W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_marwest': {'long_name': 'Temperature MAR west 24.52N/50.57W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_marwest': {'long_name': 'Salinity MAR west 24.52N/50.57W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_mareast': {'long_name': 'Temperature MAR east 24.52N/41.21W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_mareast': {'long_name': 'Salinity MAR east 24.52N/41.21W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}}
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **Institution**: 
- **Variable Mapping**: {}

2d_gridded.nc
-------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: RAPID-AMOC 26°N array
- **Institution**: Unknown
- **Description**: RAPID 26N transport estimates dataset
- **DOI**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Source File**: 2d_gridded.nc
- **Data Product**: RAPID 2D gridded data
- **Time Coverage**: 2004-04-06 to 2024-03-22
- **Record Length**: 730 observations (20.0 years)
- **Sampling Frequency**: 240.0H

**Citation:**

    Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: http://doi.org/10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 7
- **Total Coordinates**: 3
- **Dataset Size**: 1737.79 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| Coordinate | Standardized Name | Description              | Units          | Size | Min Value  | Max Value  | Missing % |
+============+===================+==========================+================+======+============+============+===========+
| depth      | depth             | No description available | float64        | 307  | 0.00       | 5995.06    | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| longitude  | longitude         | No description available | float64        | 254  | -79.50     | -14.12     | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| time       | time              | No description available | datetime64[ns] | 730  | 2004-04-06 | 2024-03-22 | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| Original Variable | Standardized Name | Description                                                                       | Units | Size     | Min Value | Max Value  | Missing % |
+===================+===================+===================================================================================+=======+==========+===========+============+===========+
| pressure          | pressure          | **Sea water pressure**: Sea water pressure at depth                               | dbar  | 307      | 0.00      | 6120.00    | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| area              | area              | **Grid cell area**: Area of each grid cell                                        | m2    | 77978    | 0.00      | 1710169.15 | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| CT                | CT                | **Conservative temperature**: Conservative temperature following TEOS-10 standard | degC  | 56923940 | 1.49      | 31.43      | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| SA                | SA                | **Absolute salinity**: Absolute salinity following TEOS-10 standard               | g/kg  | 56923940 | 0.00      | 37.88      | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| V_insitu          | V_insitu          | **In-situ velocity**: In-situ meridional velocity component                       | m/s   | 56923940 | 0.00      | 37.13      | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| V_ekman           | V_ekman           | **Ekman velocity**: Ekman transport velocity component                            | m/s   | 56923940 | 0.00      | 37.13      | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+
| V_net             | V_net             | **Net velocity**: Net meridional velocity (in-situ + Ekman)                       | m/s   | 730      | 0.00      | 0.00       | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------+-------+----------+-----------+------------+-----------+


Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/2d_gridded_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for 2D_GRIDDED dataset.

Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 2004-04-06
- **Time Coverage End**: 2024-03-22
- **Program**: RAPID
- **Project**: RAPID-AMOC 26°N array
- **Contributor Name**: Ben Moat
- **Contributor Email**: ben.moat@noc.ac.uk
- **Contributor Id**: 
- **Contributor Role**: creator
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
- **Data Product**: RAPID 2D gridded data
- **Source File**: 2d_gridded.nc
- **Variable Mapping**: {}
- **Coordinates**: [Complex metadata structure - 3 items]
- **Dataset Version**: v2024-1a
- **Dataset Creation Date**: 26-Jan-2026 14:06:26
- **File Creation Date**: 2026-01-26
- **Note On Velocity**: Velocity is separated into 3 components: V_insitu = Velocity derived from in-situ measurements and geostrophic balance, V_ekman = Ekman velocity derived from ERA5 reanalysis. The total transport from V_insitu and V_ekman is required to have zero net meridional transport. V_net is a spatially uniform velocity representing the net meridional transport derived from salt and mass conservation (McDonagh et al 2015) and is excluded from the calculation of the streamfunction. Note that the sizes of grid cells are not all equal, and velocity should be multiplied by area to obtain the transport in each cell. Longitude is the centre of the cells, except for values 2 and 3 which are the locations of moorings WB1 and WB2 and correspond with the eastern edge of the cells
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/2d_gridded.nc
- **Amocatlas Datasource**: rapid26n
- **Summary**: RAPID 26N transport estimates dataset
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/2d_gridded.nc
- **Creation Date**: 
- **Weblink**: 
- **Coordinates**: {'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'longitude': {'long_name': 'Longitude', 'description': 'Longitude coordinate', 'units': 'degrees_east', 'standard_name': 'longitude'}, 'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}}
- **Version**: 2024.1a
- **Source File**: 2d_gridded.nc
- **Featuretype**: timeSeries
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Description**: RAPID 26N transport estimates dataset
- **Platform Type**: 
- **Amocatlas Datasource**: rapid26n
- **Project**: RAPID-AMOC 26°N array
- **Files**: {'moc_transports.nc': {'data_product': 'RAPID layer transport time series', 'variable_mapping': {'time': 'TIME'}, 'variables': {'t_therm10': {'long_name': 'Transport', 'description': 'Thermocline recirculation 0-800m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_aiw10': {'long_name': 'Transport', 'description': 'Intermediate water 800-1100m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ud10': {'long_name': 'Transport', 'description': 'upper NADW 1100-3000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ld10': {'long_name': 'Transport', 'description': 'lower NADW 3000-5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_bw10': {'long_name': 'Transport', 'description': 'AABW > 5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_gs10': {'long_name': 'Florida Straits Transport', 'description': 'Florida Current from cable measurements', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ek10': {'long_name': 'Ekman Transport', 'description': 'Ekman transport from wind stress', 'units': 'Sv', 'standard_name': 'Transport'}, 't_umo10': {'long_name': 'Transport', 'description': 'Upper Mid-Ocean transport', 'units': 'Sv', 'standard_name': 'Transport'}, 'moc_mar_hc10': {'long_name': 'overturning transport', 'description': 'MOC strength', 'units': 'Sv', 'standard_name': 'Transport'}}}, 'ts_gridded.nc': {'data_product': 'RAPID gridded temperature and salinity', 'source_file': 'ts_gridded.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/ts_gridded.nc', 'variable_mapping': {}, 'variables': {'TG_west': {'long_name': 'Temperature west 26.52N/76.74W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_west': {'long_name': 'Salinity west 26.52N/76.74W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_wb3': {'long_name': 'Temperature WB3 26.50N/76.50W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_wb3': {'long_name': 'Salinity WB3 26.50N/76.50W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_east': {'long_name': 'Temperature east 26.99N/16.23W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_east': {'long_name': 'Salinity east 26.99N/16.23W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_marwest': {'long_name': 'Temperature MAR west 24.52N/50.57W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_marwest': {'long_name': 'Salinity MAR west 24.52N/50.57W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_mareast': {'long_name': 'Temperature MAR east 24.52N/41.21W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_mareast': {'long_name': 'Salinity MAR east 24.52N/41.21W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}}}, 'moc_vertical.nc': {'data_product': 'RAPID vertical streamfunction time series', 'source_file': 'moc_vertical.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/moc_vertical.nc', 'variable_mapping': {}, 'variables': {'stream_function_mar': {'long_name': 'Meridional overturning', 'description': 'Streamfunction across the Atlantic at 26.5°N', 'units': 'Sv', 'standard_name': 'Transport'}}}, '2d_gridded.nc': {'data_product': 'RAPID 2D gridded data', 'source_file': '2d_gridded.nc', 'variable_mapping': {}, 'variables': {'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'area': {'long_name': 'Grid cell area', 'description': 'Area of each grid cell', 'units': 'm2'}, 'CT': {'long_name': 'Conservative temperature', 'description': 'Conservative temperature following TEOS-10 standard', 'units': 'degC', 'standard_name': 'sea_water_conservative_temperature'}, 'SA': {'long_name': 'Absolute salinity', 'description': 'Absolute salinity following TEOS-10 standard', 'units': 'g/kg', 'standard_name': 'sea_water_absolute_salinity'}, 'V_insitu': {'long_name': 'In-situ velocity', 'description': 'In-situ meridional velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_ekman': {'long_name': 'Ekman velocity', 'description': 'Ekman transport velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_net': {'long_name': 'Net velocity', 'description': 'Net meridional velocity (in-situ + Ekman)', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}}, 'coordinates': {'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'longitude': {'long_name': 'Longitude', 'description': 'Longitude coordinate', 'units': 'degrees_east', 'standard_name': 'longitude'}, 'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}}}, 'meridional_transports.nc': {'data_product': 'RAPID meridional transport data', 'source_file': 'meridional_transports.nc', 'variable_mapping': {}, 'variables': {'amoc_depth': {'long_name': 'AMOC strength in depth coordinates', 'description': 'Atlantic meridional overturning circulation strength in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma0': {'long_name': 'AMOC strength in sigma0 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma2': {'long_name': 'AMOC strength in sigma2 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'heat_trans': {'long_name': 'Meridional heat transport', 'description': 'Northward oceanic heat transport', 'units': 'PW', 'standard_name': 'northward_ocean_heat_transport'}, 'frwa_trans': {'long_name': 'Freshwater transport', 'description': 'Meridional freshwater transport', 'units': 'Sv'}, 'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'stream_depth': {'long_name': 'Streamfunction in depth coordinates', 'description': 'Meridional overturning streamfunction in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma0': {'long_name': 'Streamfunction in sigma0 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma2': {'long_name': 'Streamfunction in sigma2 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}}, 'coordinates': {'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}, 'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'sigma0': {'long_name': 'Potential density anomaly (sigma-theta)', 'description': 'Potential density anomaly referenced to surface (sigma-theta), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_theta'}, 'sigma2': {'long_name': 'Potential density anomaly (sigma-2)', 'description': 'Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_2'}}}}
- **Conventions**: CF-1.8, ACDD-1.3
- **Creator Email**: 
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **License**: CC-BY 4.0
- **Data Product**: RAPID 2D gridded data
- **Program**: RAPID
- **Creator Name**: 
- **Citation**: Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Variables**: {'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'area': {'long_name': 'Grid cell area', 'description': 'Area of each grid cell', 'units': 'm2'}, 'CT': {'long_name': 'Conservative temperature', 'description': 'Conservative temperature following TEOS-10 standard', 'units': 'degC', 'standard_name': 'sea_water_conservative_temperature'}, 'SA': {'long_name': 'Absolute salinity', 'description': 'Absolute salinity following TEOS-10 standard', 'units': 'g/kg', 'standard_name': 'sea_water_absolute_salinity'}, 'V_insitu': {'long_name': 'In-situ velocity', 'description': 'In-situ meridional velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_ekman': {'long_name': 'Ekman velocity', 'description': 'Ekman transport velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_net': {'long_name': 'Net velocity', 'description': 'Net meridional velocity (in-situ + Ekman)', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}}
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **Institution**: 
- **Variable Mapping**: {}

meridional_transports.nc
------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: RAPID-AMOC 26°N array
- **Institution**: Unknown
- **Description**: RAPID 26N transport estimates dataset
- **DOI**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Source File**: meridional_transports.nc
- **Data Product**: RAPID meridional transport data
- **Time Coverage**: 2004-04-06 to 2024-03-22
- **Record Length**: 730 observations (20.0 years)
- **Sampling Frequency**: 240.0H

**Citation:**

    Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: http://doi.org/10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 9
- **Total Coordinates**: 4
- **Dataset Size**: 9.22 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| Coordinate | Standardized Name | Description              | Units          | Size | Min Value  | Max Value  | Missing % |
+============+===================+==========================+================+======+============+============+===========+
| time       | time              | No description available | datetime64[ns] | 730  | 2004-04-06 | 2024-03-22 | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| depth      | depth             | No description available | float64        | 307  | 0.00       | 5995.06    | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| sigma0     | sigma0            | No description available | float64        | 631  | 1022.00    | 1028.00    | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+
| sigma2     | sigma2            | No description available | float64        | 708  | 1030.00    | 1037.15    | 0.0%      |
+------------+-------------------+--------------------------+----------------+------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                                                                                             | Units | Size   | Min Value | Max Value | Missing % |
+===================+===================+=========================================================================================================================================+=======+========+===========+===========+===========+
| amoc_depth        | amoc_depth        | **AMOC strength in depth coordinates**: Atlantic meridional overturning circulation strength in depth coordinates                       | Sv    | 730    | -0.45     | 27.68     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| amoc_sigma0       | amoc_sigma0       | **AMOC strength in sigma0 coordinates**: Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates | Sv    | 730    | 7.23      | 28.95     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| amoc_sigma2       | amoc_sigma2       | **AMOC strength in sigma2 coordinates**: Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates | Sv    | 730    | 7.09      | 29.23     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| heat_trans        | heat_trans        | **Meridional heat transport**: Northward oceanic heat transport                                                                         | PW    | 730    | -0.13     | 2.10      | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| frwa_trans        | frwa_trans        | **Freshwater transport**: Meridional freshwater transport                                                                               | Sv    | 730    | -1.98     | -0.48     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| pressure          | pressure          | **Sea water pressure**: Sea water pressure at depth                                                                                     | dbar  | 307    | 0.00      | 6120.00   | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| stream_depth      | stream_depth      | **Streamfunction in depth coordinates**: Meridional overturning streamfunction in depth coordinates                                     | Sv    | 224110 | -8.89     | 27.68     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| stream_sigma0     | stream_sigma0     | **Streamfunction in sigma0 coordinates**: Meridional overturning streamfunction in potential density (sigma0) coordinates               | Sv    | 460630 | -10.98    | 28.95     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| stream_sigma2     | stream_sigma2     | **Streamfunction in sigma2 coordinates**: Meridional overturning streamfunction in potential density (sigma2) coordinates               | Sv    | 516840 | -9.31     | 29.23     | 0.0%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+


Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/meridional_transports_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for MERIDIONAL_TRANSPORTS dataset.

Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Platform**: mooring
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 2004-04-06
- **Time Coverage End**: 2024-03-22
- **Program**: RAPID
- **Project**: RAPID-AMOC 26°N array
- **Contributor Name**: Ben Moat
- **Contributor Email**: ben.moat@noc.ac.uk
- **Contributor Id**: 
- **Contributor Role**: creator
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
- **Data Product**: RAPID meridional transport data
- **Source File**: meridional_transports.nc
- **Variable Mapping**: {}
- **Coordinates**: [Complex metadata structure - 4 items]
- **Dataset Version**: v2024-1a
- **Dataset Creation Date**: 26-Jan-2026 14:06:26
- **File Creation Date**: 2026-01-26
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/meridional_transports.nc
- **Amocatlas Datasource**: rapid26n
- **Summary**: RAPID 26N transport estimates dataset
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/meridional_transports.nc
- **Creation Date**: 
- **Weblink**: 
- **Coordinates**: {'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}, 'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'sigma0': {'long_name': 'Potential density anomaly (sigma-theta)', 'description': 'Potential density anomaly referenced to surface (sigma-theta), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_theta'}, 'sigma2': {'long_name': 'Potential density anomaly (sigma-2)', 'description': 'Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_2'}}
- **Version**: 2024.1a
- **Source File**: meridional_transports.nc
- **Featuretype**: timeSeries
- **Doi**: https://doi.org/10.5285/223b34a32dc5c945e0637086abc0f274
- **Description**: RAPID 26N transport estimates dataset
- **Platform Type**: 
- **Amocatlas Datasource**: rapid26n
- **Project**: RAPID-AMOC 26°N array
- **Files**: {'moc_transports.nc': {'data_product': 'RAPID layer transport time series', 'variable_mapping': {'time': 'TIME'}, 'variables': {'t_therm10': {'long_name': 'Transport', 'description': 'Thermocline recirculation 0-800m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_aiw10': {'long_name': 'Transport', 'description': 'Intermediate water 800-1100m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ud10': {'long_name': 'Transport', 'description': 'upper NADW 1100-3000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ld10': {'long_name': 'Transport', 'description': 'lower NADW 3000-5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_bw10': {'long_name': 'Transport', 'description': 'AABW > 5000m', 'units': 'Sv', 'standard_name': 'Transport'}, 't_gs10': {'long_name': 'Florida Straits Transport', 'description': 'Florida Current from cable measurements', 'units': 'Sv', 'standard_name': 'Transport'}, 't_ek10': {'long_name': 'Ekman Transport', 'description': 'Ekman transport from wind stress', 'units': 'Sv', 'standard_name': 'Transport'}, 't_umo10': {'long_name': 'Transport', 'description': 'Upper Mid-Ocean transport', 'units': 'Sv', 'standard_name': 'Transport'}, 'moc_mar_hc10': {'long_name': 'overturning transport', 'description': 'MOC strength', 'units': 'Sv', 'standard_name': 'Transport'}}}, 'ts_gridded.nc': {'data_product': 'RAPID gridded temperature and salinity', 'source_file': 'ts_gridded.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/ts_gridded.nc', 'variable_mapping': {}, 'variables': {'TG_west': {'long_name': 'Temperature west 26.52N/76.74W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_west': {'long_name': 'Salinity west 26.52N/76.74W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_wb3': {'long_name': 'Temperature WB3 26.50N/76.50W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_wb3': {'long_name': 'Salinity WB3 26.50N/76.50W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_east': {'long_name': 'Temperature east 26.99N/16.23W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_east': {'long_name': 'Salinity east 26.99N/16.23W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_marwest': {'long_name': 'Temperature MAR west 24.52N/50.57W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_marwest': {'long_name': 'Salinity MAR west 24.52N/50.57W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}, 'TG_mareast': {'long_name': 'Temperature MAR east 24.52N/41.21W', 'units': 'degC', 'standard_name': 'sea_water_temperature'}, 'SG_mareast': {'long_name': 'Salinity MAR east 24.52N/41.21W', 'units': 'psu', 'standard_name': 'sea_water_practical_salinity'}}}, 'moc_vertical.nc': {'data_product': 'RAPID vertical streamfunction time series', 'source_file': 'moc_vertical.nc', 'source_path': '/Users/eddifying/Cloudfree/gitlab-cloudfree/amocatlas/data/moc_vertical.nc', 'variable_mapping': {}, 'variables': {'stream_function_mar': {'long_name': 'Meridional overturning', 'description': 'Streamfunction across the Atlantic at 26.5°N', 'units': 'Sv', 'standard_name': 'Transport'}}}, '2d_gridded.nc': {'data_product': 'RAPID 2D gridded data', 'source_file': '2d_gridded.nc', 'variable_mapping': {}, 'variables': {'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'area': {'long_name': 'Grid cell area', 'description': 'Area of each grid cell', 'units': 'm2'}, 'CT': {'long_name': 'Conservative temperature', 'description': 'Conservative temperature following TEOS-10 standard', 'units': 'degC', 'standard_name': 'sea_water_conservative_temperature'}, 'SA': {'long_name': 'Absolute salinity', 'description': 'Absolute salinity following TEOS-10 standard', 'units': 'g/kg', 'standard_name': 'sea_water_absolute_salinity'}, 'V_insitu': {'long_name': 'In-situ velocity', 'description': 'In-situ meridional velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_ekman': {'long_name': 'Ekman velocity', 'description': 'Ekman transport velocity component', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}, 'V_net': {'long_name': 'Net velocity', 'description': 'Net meridional velocity (in-situ + Ekman)', 'units': 'm/s', 'standard_name': 'northward_sea_water_velocity'}}, 'coordinates': {'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'longitude': {'long_name': 'Longitude', 'description': 'Longitude coordinate', 'units': 'degrees_east', 'standard_name': 'longitude'}, 'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}}}, 'meridional_transports.nc': {'data_product': 'RAPID meridional transport data', 'source_file': 'meridional_transports.nc', 'variable_mapping': {}, 'variables': {'amoc_depth': {'long_name': 'AMOC strength in depth coordinates', 'description': 'Atlantic meridional overturning circulation strength in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma0': {'long_name': 'AMOC strength in sigma0 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma2': {'long_name': 'AMOC strength in sigma2 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'heat_trans': {'long_name': 'Meridional heat transport', 'description': 'Northward oceanic heat transport', 'units': 'PW', 'standard_name': 'northward_ocean_heat_transport'}, 'frwa_trans': {'long_name': 'Freshwater transport', 'description': 'Meridional freshwater transport', 'units': 'Sv'}, 'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'stream_depth': {'long_name': 'Streamfunction in depth coordinates', 'description': 'Meridional overturning streamfunction in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma0': {'long_name': 'Streamfunction in sigma0 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma2': {'long_name': 'Streamfunction in sigma2 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}}, 'coordinates': {'time': {'long_name': 'Time', 'description': 'Time coordinate', 'units': 'days since 1950-01-01 00:00:00', 'standard_name': 'time'}, 'depth': {'long_name': 'Depth', 'description': 'Depth below sea surface', 'units': 'm', 'standard_name': 'depth'}, 'sigma0': {'long_name': 'Potential density anomaly (sigma-theta)', 'description': 'Potential density anomaly referenced to surface (sigma-theta), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_theta'}, 'sigma2': {'long_name': 'Potential density anomaly (sigma-2)', 'description': 'Potential density anomaly referenced to 2000m (sigma-2), density anomaly to 1000 kg/m3', 'units': 'kg/m3', 'standard_name': 'sea_water_sigma_2'}}}}
- **Conventions**: CF-1.8, ACDD-1.3
- **Creator Email**: 
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **License**: CC-BY 4.0
- **Data Product**: RAPID meridional transport data
- **Program**: RAPID
- **Creator Name**: 
- **Citation**: Moat B.I.; Smeed D.A.; Rayner D.; Johns W.E.; Smith, R.; Volkov, D.; Elipot S.; Petit T.; Kajtar J.; Baringer M. O.; and Collins, J. (2026). Atlantic meridional overturning circulation observed by the RAPID-MOCHA-WBTS (RAPID-Meridional Overturning Circulation and Heatflux Array-Western Boundary Time Series) array at 26N from 2004 to 2024 (v2024.1a), British Oceanographic Data Centre - Natural Environment Research Council, UK. doi: 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Variables**: {'amoc_depth': {'long_name': 'AMOC strength in depth coordinates', 'description': 'Atlantic meridional overturning circulation strength in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma0': {'long_name': 'AMOC strength in sigma0 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'amoc_sigma2': {'long_name': 'AMOC strength in sigma2 coordinates', 'description': 'Atlantic meridional overturning circulation strength in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'heat_trans': {'long_name': 'Meridional heat transport', 'description': 'Northward oceanic heat transport', 'units': 'PW', 'standard_name': 'northward_ocean_heat_transport'}, 'frwa_trans': {'long_name': 'Freshwater transport', 'description': 'Meridional freshwater transport', 'units': 'Sv'}, 'pressure': {'long_name': 'Sea water pressure', 'description': 'Sea water pressure at depth', 'units': 'dbar', 'standard_name': 'sea_water_pressure'}, 'stream_depth': {'long_name': 'Streamfunction in depth coordinates', 'description': 'Meridional overturning streamfunction in depth coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma0': {'long_name': 'Streamfunction in sigma0 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma0) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}, 'stream_sigma2': {'long_name': 'Streamfunction in sigma2 coordinates', 'description': 'Meridional overturning streamfunction in potential density (sigma2) coordinates', 'units': 'Sv', 'standard_name': 'ocean_meridional_overturning_mass_streamfunction'}}
- **Acknowledgement**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council and data is freely available from www.rapid.ac.uk/
- **Institution**: 
- **Variable Mapping**: {}
