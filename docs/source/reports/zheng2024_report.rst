ZHENG2024 Dataset Report
========================

Generated: 2026-02-06 23:23:18

atl_mft_2000_extend_gpcp_oaflux.nc
----------------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: An observation based estimate of the Atlantic meridional freshwater transport
- **Description**: An observation based estimate of the Atlantic meridional freshwater transport
- **Citation**: Zheng, H. (2024). An observation-based estimate of the Atlantic meridional freshwater transport [Data set]. Zenodo. https://doi.org/10.5281/zenodo.12790901
- **Acknowledgement**: Zheng et al. (2024), http://doi.org/10.1029/2024gl110021
- **Source File**: atl_mft_2000_extend_gpcp_oaflux.nc
- **Data Product**: An observation based estimate of the Atlantic meridional freshwater transport
- **Time Coverage**: 2004-04-30 to 2020-12-31
- **Record Length**: 201 observations (16.7 years)
- **Sampling Frequency**: monthly

**Citation:**

    Zheng, H. (2024). An observation-based estimate of the Atlantic meridional freshwater transport [Data set]. Zenodo. https://doi.org/10.5281/zenodo.12790901

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 1
- **Total Coordinates**: 2
- **Dataset Size**: 0.16 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-----------------------------------------+------------------------------------+--------+------------+------------+
| Coordinate | Standardized Name | Description                             | Units                              | Size   | Min Value  | Max Value  |
+============+===================+=========================================+====================================+========+============+============+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (201,) | 2004-04-30 | 2020-12-31 |
+------------+-------------------+-----------------------------------------+------------------------------------+--------+------------+------------+
| lat        | LATITUDE          | Latitude north (WGS84)                  | degrees_north                      | (101,) | -34.5      | 65.5       |
+------------+-------------------+-----------------------------------------+------------------------------------+--------+------------+------------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+------------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                                                                                                                                                                                                                                                                                                                       | Units | Size       | Min Value | Max Value | Missing % |
+===================+===================+===================================================================================================================================================================================================================================================================================================================================================================+=======+============+===========+===========+===========+
| mft               | MFT               | **Meridional Freshwater Transport**: An Observation-Based Estimate of Atlantic Meridional Freshwater Transport. AMFT given by RAPID array at 26.5°N was integrated southward and northward in combination with ocean freshwater content (calculated by salinity) and surface freshwater flux, with the residual of the freshwater budget equation being the AMFT. | Sv    | (201, 101) | -0.98     | 0.92      | 0.0%      |
+-------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+------------+-----------+-----------+-----------+
| MFT               | MFT               | **Meridional Freshwater Transport**: An Observation-Based Estimate of Atlantic Meridional Freshwater Transport. AMFT given by RAPID array at 26.5°N was integrated southward and northward in combination with ocean freshwater content (calculated by salinity) and surface freshwater flux, with the residual of the freshwater budget equation being the AMFT. | Sv    | (201, 101) | -0.98     | 0.92      | 0.0%      |
+-------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+------------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Platform**: Salinity observations used in this study are from the Institute of Atmospheric Physics (IAP). Argo floats, CTD salinity sensors, bottles, mooring, sourced from the World Ocean Database (WOD). Precipitation and evaporation observations are derived from the Global Precipitation Climatology Project (GPCP).
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 2004-04-30
- **Time Coverage End**: 2020-12-31
- **Program**: amft
- **Project**: An observation based estimate of the Atlantic meridional freshwater transport
- **Contributor Name**: Huayi Zheng, Lijing Cheng, Feili Li, Yuying Pan, Chenyu Zhu
- **Contributor Email**: , , , , 
- **Contributor Id**: , , , , 
- **Contributor Role**: 
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Web Link**: https://zenodo.org/records/12790901
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Featuretype**: timeSeries
- **Description**: An observation based estimate of the Atlantic meridional freshwater transport
- **Acknowledgement**: Zheng et al. (2024), http://doi.org/10.1029/2024gl110021
- **References**: Zheng, H., Cheng, L., Li, F., Pan, Y., & Zhu, C. (2024). An observation-based estimate of Atlantic meridional freshwater transport. Geophysical Research Letters, 51, e2024GL110021. https://doi.org/10.1029/2024GL110021
- **License**: None
- **Conventions**: CF-1.8, ACDD-1.3
- **Data Product**: An observation based estimate of the Atlantic meridional freshwater transport
- **Variable Mapping**: {'time': 'TIME', 'lat': 'LATITUDE', 'mft': 'MFT'}
- **Source File**: atl_mft_2000_extend_gpcp_oaflux.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/atl_mft_2000_extend_gpcp_oaflux.nc
- **Amocatlas Datasource**: zheng2024
- **Applied Variable Mapping**: {'time': 'TIME', 'lat': 'LATITUDE', 'mft': 'MFT', 'TIME': 'TIME', 'MFT': 'MFT'}
- **Summary**: An observation based estimate of the Atlantic meridional freshwater transport
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Conventions**: CF-1.8, ACDD-1.3
- **Description**: An observation based estimate of the Atlantic meridional freshwater transport
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Contributor Id**: , , , , 
- **Acknowledgement**: Zheng et al. (2024), http://doi.org/10.1029/2024gl110021
- **Program**: amft
- **Data Product**: An observation based estimate of the Atlantic meridional freshwater transport
- **Time Coverage End**: 2020-12-31
- **Platform Type**: 
- **Amocatlas Datasource**: zheng2024
- **Time Coverage Start**: 2004-04-30
- **Citation**: Zheng, H. (2024). An observation-based estimate of the Atlantic meridional freshwater transport [Data set]. Zenodo. https://doi.org/10.5281/zenodo.12790901
- **Source File**: atl_mft_2000_extend_gpcp_oaflux.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/atl_mft_2000_extend_gpcp_oaflux.nc
- **License**: None
- **References**: Zheng, H., Cheng, L., Li, F., Pan, Y., & Zhu, C. (2024). An observation-based estimate of Atlantic meridional freshwater transport. Geophysical Research Letters, 51, e2024GL110021. https://doi.org/10.1029/2024GL110021
- **Project**: An observation based estimate of the Atlantic meridional freshwater transport
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Source Url**: 
- **Variable Mapping**: {'time': 'TIME', 'lat': 'LATITUDE', 'mft': 'MFT'}
- **Featuretype**: timeSeries
- **Contributor Name**: Huayi Zheng, Lijing Cheng, Feili Li, Yuying Pan, Chenyu Zhu
- **Weblink**: 
- **Contributor Role**: 
