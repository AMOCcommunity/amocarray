FBC Dataset Report
==================

Generated: 2026-02-06 17:32:23

FBC_overflow_transport.txt
--------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: B. Hansen et al.: A stable Faroe Bank Channel overflow
- **Institution**: Unknown
- **Description**: FBC Overflow transport time series
- **Source File**: FBC_overflow_transport.txt
- **Data Product**: Daily averaged kinematic FBC-overflow flux (transport) in Sv
- **Time Coverage**: 816260112.0 to 1684483344.0
- **Record Length**: 9,497 observations (868223232.0 years)
- **Sampling Frequency**: 2270592.0H

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 3
- **Total Coordinates**: 1
- **Dataset Size**: 0.29 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-----------------------------------------+------------------------------------+---------+------------+------------+-----------+
| Coordinate | Standardized Name | Description                             | Units                              | Size    | Min Value  | Max Value  | Missing % |
+============+===================+=========================================+====================================+=========+============+============+===========+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (9497,) | 1995-11-13 | 2023-05-19 | 0.0%      |
+------------+-------------------+-----------------------------------------+------------------------------------+---------+------------+------------+-----------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+-------------------------------------------------------------------------------+-------+---------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                                   | Units | Size    | Min Value | Max Value | Missing % |
+===================+===================+===============================================================================+=======+=========+===========+===========+===========+
| Month             | Month             | Month                                                                         | None  | (9497,) | 1.00      | 12.00     | 0.0%      |
+-------------------+-------------------+-------------------------------------------------------------------------------+-------+---------+-----------+-----------+-----------+
| Day               | Day               | Day                                                                           | None  | (9497,) | 1.00      | 31.00     | 0.0%      |
+-------------------+-------------------+-------------------------------------------------------------------------------+-------+---------+-----------+-----------+-----------+
| TRANSPORT         | TRANSPORT         | **Faroe Bank Channel Overflow Transport**: FBC Overflow transport time series | Sv    | (9497,) | 0.50      | 4.86      | 0.0%      |
+-------------------+-------------------+-------------------------------------------------------------------------------+-------+---------+-----------+-----------+-----------+


Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/FBC_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for FBC dataset.

Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Time Coverage Start**: 816260112.0
- **Time Coverage End**: 1684483344.0
- **Program**: FBC
- **Project**: B. Hansen et al.: A stable Faroe Bank Channel overflow
- **Contributor Name**: 
- **Contributor Email**: 
- **Contributor Id**: https://envofar.fo/var/ftp/Timeseries/FBC_overflow_transport.txt
- **Contributor Role**: 
- **Web Link**: https://envofar.fo/data/index.php?dir=Timeseries&sort=N&order=A
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Featuretype**: timeSeries
- **Description**: FBC Overflow transport time series
- **Acknowledgment**: The authors wish to thank captains and crew on the RV Magnus Heinason as well as Regin Kristiansen for unfailing support during measurements at sea, and Ebba Mortensen for data processing. Funding for the in situ measurements has been obtained from the Environmental Research Programme of the Nordic Council of Ministers (NMR) 1993–1998, from national Nordic research councils, from the Danish DANCEA programme, and from the European Framework Programs, lately under grant agreement no. GA212643 (THOR) and under grant agreement no. 308299 (NACLIM). Analysis and preparation of this manuscript was mainly funded by the NACLIM project. We thank three anonymous referees for very constructive comments.
- **License**: None
- **Data Product**: Daily averaged kinematic FBC-overflow flux (transport) in Sv
- **Variable Mapping**: {'TIME': 'TIME', 'Month': 'Month', 'Day': 'Day', 'Flux': 'TRANSPORT'}
- **Source File**: FBC_overflow_transport.txt
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/FBC_overflow_transport.txt
- **Amocatlas Datasource**: fbc
- **Summary**: FBC Overflow transport time series
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

*No metadata modifications detected.*
