ZHENG2024 Datasets
==================

*Generated: |today|*

----

atl_mft_2000_extend_gpcp_oaflux.nc
----------------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: An observation based estimate of the Atlantic meridional freshwater transport
- **Description**: An observation based estimate of the Atlantic meridional freshwater transport
- **Source File**: atl_mft_2000_extend_gpcp_oaflux.nc
- **Data Product**: An observation based estimate of the Atlantic meridional freshwater transport
- **Time Coverage**: 2004-04-30 to 2020-12-31
- **Record Length**: 201 observations (16.7 years)
- **Sampling Frequency**: monthly

**Citation:**

    Zheng, H. (2024). An observation-based estimate of the Atlantic meridional freshwater transport [Data set]. Zenodo. https://doi.org/10.5281/zenodo.12790901

Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/ZHENG2024_2d_gridded.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for ZHENG2024 dataset.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 1
- **Total Coordinates**: 2
- **Dataset Size**: 0.16 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates in the standardised version, including coordinate name remapping from the original, if any:

.. list-table::
   :widths: 14 14 14 14 14 14 14
   :header-rows: 1

   * - Coordinate
     - Description
     - Units
     - Size
     - Min Value
     - Max Value
     - Missing %
   * - *lat* → **LATITUDE**
     - **Latitude**: Latitude north (WGS84)
     - degree_north
     - (101,)
     - -34.50
     - 65.50
     - 0.0%
   * - *time* → **TIME**
     - **Time**: Time in datetime format
     - datetime64[ns]
     - (201,)
     - 2004-04-30
     - 2020-12-31
     - 0.0%


Variable Information
^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

.. list-table::
   :widths: 14 14 14 14 14 14 14
   :header-rows: 1

   * - Variable
     - Description
     - Units
     - Size
     - Min Value
     - Max Value
     - Missing %
   * - *mft* → **MFT**
     - **Freshwater**: An Observation-Based Estimate of Atlantic Meridional Freshwater Transport. AMFT given by RAPID array at 26.5°N was integrated southward and northward in combination with ocean freshwater content (calculated by salinity) and surface freshwater flux, with the residual of the freshwater budget equation being the AMFT.
     - Sverdrup
     - (201, 101)
     - -0.98
     - 0.92
     - 0.0%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Summary**: An observation based estimate of the Atlantic meridional freshwater transport
- **Description\***: An observation based estimate of the Atlantic meridional freshwater transport
- **Program\***: amft
- **Project\***: An observation based estimate of the Atlantic meridional freshwater transport
- **License\***: None
- **References\***: Zheng, H., Cheng, L., Li, F., Pan, Y., & Zhu, C. (2024). An observation-based estimate of Atlantic meridional freshwater transport. Geophysical Research Letters, 51, e2024GL110021. https://doi.org/10.1029/2024GL110021
- **Weblink\***: https://zenodo.org/records/12790901
- **Data Product\***: An observation based estimate of the Atlantic meridional freshwater transport
- **Time Coverage Start\***: 2004-04-30
- **Time Coverage End\***: 2020-12-31
- **Contributor Name\***: Huayi Zheng, Lijing Cheng, Feili Li, Yuying Pan, Chenyu Zhu
- **Contributor Role\***: contributor, , , , 
- **Contributor Role Vocabulary\***: https://vocab.nerc.ac.uk/collection/G04/current/
- **Contributor Email**: , , , , 
- **Contributor Id\***: https://orcid.org/0009-0004-5333-7595, https://orcid.org/0000-0002-9854-0392, https://orcid.org/0000-0002-3073-9813, https://orcid.org/0000-0001-7694-2625, https://orcid.org/0000-0002-9330-4294
- **Contributing Institutions**: 
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Conventions\***: CF-1.8, ACDD-1.3, OceanSITES-1.5
- **featureType\***: timeSeries
- **featureType_vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: atl_mft_2000_extend_gpcp_oaflux.nc
- **Source Path\***: ~/AMOCatlas/data/atl_mft_2000_extend_gpcp_oaflux.nc
- **Source Url\***: https://zenodo.org/records/12790901
- **Date Modified**: 2026-02-01T00:00:00Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Processing Datasource\***: zheng2024
- **Variable Mapping\***: {'time': 'TIME', 'lat': 'LATITUDE', 'mft': 'MFT'}
- **Original Variable Metadata\***: [Complex metadata structure - 3 items]
- **Applied Variable Mapping**: {'time': 'TIME', 'lat': 'LATITUDE', 'mft': 'MFT', 'TIME': 'TIME', 'MFT': 'MFT'}
- **Comment\***: Salinity observations used in this study are from the Institute of Atmospheric Physics (IAP). Argo floats, CTD salinity sensors, bottles, mooring, sourced from the World Ocean Database (WOD). Precipitation and evaporation observations are derived from the Global Precipitation Climatology Project (GPCP). (Note: date_modified has been set to a canonical value for documentation generation to avoid git churn)
