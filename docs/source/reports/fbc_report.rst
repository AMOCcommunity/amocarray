FBC Dataset Report
==================

*Generated: 2026-02-08*

----

FBC_overflow_transport.txt
--------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: B. Hansen et al.: A stable Faroe Bank Channel overflow
- **Description**: FBC Overflow transport time series
- **Source File**: FBC_overflow_transport.txt
- **Data Product**: Daily averaged kinematic FBC-overflow flux (transport) in Sv
- **Time Coverage**: 1995-11-13 to 2023-05-19
- **Record Length**: 9,497 observations (27.5 years)
- **Sampling Frequency**: daily

**Citation:**

    Hansen, B., Húsgarð Larsen, K. M., Hátún, H., and Østerhus, S.: A stable Faroe Bank Channel overflow 1995–2015, Ocean Sci., 12, 1205–1220, https://doi.org/10.5194/os-12-1205-2016, 2016.

**Acknowledgement:**

    Funding for the in situ Faroe Bank Channel measurements is from the Environmental Research Programme of the Nordic Council of Ministers (NMR) 1993–1998, from national Nordic research councils, from the Danish DANCEA programme, and from the European Framework Programs, lately under grant agreement no. GA212643 (THOR) and under grant agreement no. 308299 (NACLIM).

Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/FBC_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for FBC dataset.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 1
- **Total Coordinates**: 1
- **Dataset Size**: 0.14 MB

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
   * - **TIME**
     - Time
     - datetime64[ns]
     - (9497,)
     - 1995-11-13
     - 2023-05-19
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
   * - *Flux* → **TRANS_FBC**
     - **FBC Overflow**: FBC Overflow transport time series
     - Sverdrup
     - (9497,)
     - 0.50
     - 4.86
     - 0.0%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Summary**: FBC Overflow transport time series
- **Description\***: FBC Overflow transport time series
- **Program\***: FBC
- **Project\***: B. Hansen et al.: A stable Faroe Bank Channel overflow
- **License\***: None
- **Acknowledgment\***: Funding for the in situ Faroe Bank Channel measurements is from the Environmental Research Programme of the Nordic Council of Ministers (NMR) 1993–1998, from national Nordic research councils, from the Danish DANCEA programme, and from the European Framework Programs, lately under grant agreement no. GA212643 (THOR) and under grant agreement no. 308299 (NACLIM).
- **Weblink\***: https://envofar.fo/data/index.php?dir=Timeseries&sort=N&order=A
- **Data Product\***: Daily averaged kinematic FBC-overflow flux (transport) in Sv
- **Time Coverage Start\***: 1995-11-13
- **Time Coverage End\***: 2023-05-19
- **Contributing Institutions\***: Faroe Marine Research Institute (FAMRI)
- **Contributing Institutions Vocabulary**: https://edmo.seadatanet.org/report/3084
- **Contributing Institutions Role**: 
- **Conventions**: CF-1.8, ACDD-1.3, OceanSITES-1.5
- **featureType\***: timeSeries
- **featureType_vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: FBC_overflow_transport.txt
- **Source Path\***: ~/AMOCatlas/data/FBC_overflow_transport.txt
- **Source Url\***: https://envofar.fo/var/ftp/Timeseries/FBC_overflow_transport.txt
- **Date Modified**: 2026-02-08T13:38:59Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Processing Datasource\***: fbc
- **Variable Mapping\***: {'Flux': 'TRANS_FBC'}
- **Original Variable Metadata\***: [Complex metadata structure - 3 items]
- **Applied Variable Mapping**: {'Flux': 'TRANS_FBC'}
- **Variables To Remove\***: Day, Month
