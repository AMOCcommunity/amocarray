FW2015 Dataset Report
=====================

Generated: 2026-02-06 23:23:14

MOCproxy_for_figshare_v1.mat
----------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Unknown
- **Description**: Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements
- **Citation**: Frajka-Williams, E. (2015), Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements. Geophys. Res. Lett., 42, 3458–3464. doi: 10.1002/2015GL063220.
- **Acknowledgement**: Frajka-Williams, E. (2015), Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements. Geophys. Res. Lett., 42, 3458–3464. doi: 10.1002/2015GL063220.
- **Source File**: MOCproxy_for_figshare_v1.mat
- **Data Product**: a proxy for the meridional overturning circulation at 26N, using sea level anomaly and cable measurements
- **Time Coverage**: 727056000.0 to 2014-12-15
- **Record Length**: 264 observations (21.9 years)
- **Sampling Frequency**: monthly

**Citation:**

    Frajka-Williams, E. (2015), Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements. Geophys. Res. Lett., 42, 3458–3464. doi: http://doi.org/10.1002/2015GL063220.

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 11
- **Total Coordinates**: 1
- **Dataset Size**: 0.02 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-----------------------------------------+------------------------------------+--------+------------+------------+
| Coordinate | Standardized Name | Description                             | Units                              | Size   | Min Value  | Max Value  |
+============+===================+=========================================+====================================+========+============+============+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (264,) | 1993-01-15 | 2014-12-15 |
+------------+-------------------+-----------------------------------------+------------------------------------+--------+------------+------------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                                                                                                                                                                                                                                                                                                                                 | Units | Size   | Min Value | Max Value | Missing % |
+===================+===================+=============================================================================================================================================================================================================================================================================================================================================================================+=======+========+===========+===========+===========+
| mocproxy          | MOC_PROXY         | **Overturning transport proxy**: a proxy for the meridional overturning circulation at 26N, using sea level anomaly and cable measurements                                                                                                                                                                                                                                  | Sv    | (264,) | 13.21     | 20.54     | 10.2%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| umoproxy          | TRANS_UMO_PROXY   | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | -19.51    | -15.16    | 10.2%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| h1umo             | SSHA              | **Sea surface height anomaly near 28N, 70W**: sea level anomaly from a spatially-smoothed and temporally filtered version of the AVISO mapped absolute dynamic topography product and selected near 28N, 70W in the Atlantic, at the point with the highest anticorrelation between the upper mid-ocean transport measured by the RAPID-MOCHA project and sea level anomaly | cm    | (264,) | -3.17     | 6.12      | 10.2%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| gs                | TRANS_FC          | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | 30.19     | 34.61     | 3.8%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| umo               | TRANS_UMO         | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | -20.18    | -15.31    | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| ek                | TRANS_EKMAN       | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | 1.64      | 5.11      | 6.1%      |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| moc               | MOC               | **Overturning transport**: The meridional overturning circulation at 26N or, the volume of water moving northward in the top (roughly) 1100 m of the ocean which is equal-and-opposite-to the volume of water moving southward below this depth.                                                                                                                            | Sv    | (264,) | 12.98     | 19.95     | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| unadw             | TRANS_1100_3000   | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | -12.89    | -10.79    | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| lnadw             | TRANS_3000_5000   | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | -8.34     | -3.21     | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| ek_grid           | TRANS_EKMAN__GRID | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | 1.97      | 4.42      | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| gs_grid           | TRANS_FC_GRID     | No description available                                                                                                                                                                                                                                                                                                                                                    | 1     | (264,) | 30.61     | 32.13     | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+
| MOC               | MOC               | **Overturning transport**: The meridional overturning circulation at 26N or, the volume of water moving northward in the top (roughly) 1100 m of the ocean which is equal-and-opposite-to the volume of water moving southward below this depth.                                                                                                                            | Sv    | (264,) | 12.98     | 19.95     | 61.0%     |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+--------+-----------+-----------+-----------+


Dataset Visualization
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../_static/reports/FW2015_timeseries.png
   :alt: AMOC time series plot
   :align: center
   :scale: 80%

   Time series plot for FW2015 dataset.

Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Time Coverage Start**: 727056000.0
- **Time Coverage End**: 2014-12-15
- **Contributor Name**: 
- **Contributor Email**: 
- **Contributor Id**: https://figshare.com/articles/dataset/MOCproxy_for_figshare_v1_0_mat/1463479?file=3369779
- **Contributor Role**: 
- **Web Link**: https://figshare.com/articles/dataset/MOCproxy_for_figshare_v1_0_mat/1463479?file=3369779
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Featuretype**: timeSeries
- **Description**: Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements
- **License**: CC-BY 4.0
- **Conventions**: CF-1.8, ACDD-1.3
- **Data Product**: a proxy for the meridional overturning circulation at 26N, using sea level anomaly and cable measurements
- **Acknowledgement**: Frajka-Williams, E. (2015), Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements. Geophys. Res. Lett., 42, 3458–3464. doi: 10.1002/2015GL063220.
- **Variable Mapping**: [Complex metadata structure - 12 items]
- **Created**: Jun 2015, Eleanor Frajka-Williams
- **Url**: http://eleanorfrajka.com/moc-from-space/
- **Paper**: http://dx.doi.org/10.1002/2015GL063220
- **Version**: v1.0
- **Source File**: MOCproxy_for_figshare_v1.mat
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/MOCproxy_for_figshare_v1.mat
- **Amocatlas Datasource**: fw2015
- **Applied Variable Mapping**: [Complex metadata structure - 14 items]
- **Summary**: Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Conventions**: CF-1.8, ACDD-1.3
- **Description**: Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Acknowledgement**: Frajka-Williams, E. (2015), Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements. Geophys. Res. Lett., 42, 3458–3464. doi: 10.1002/2015GL063220.
- **Data Product**: a proxy for the meridional overturning circulation at 26N, using sea level anomaly and cable measurements
- **Time Coverage End**: 2014-12-15
- **Amocatlas Datasource**: fw2015
- **Time Coverage Start**: 1993-01-15
- **Citation**: Frajka-Williams, E. (2015), Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements. Geophys. Res. Lett., 42, 3458–3464. doi: 10.1002/2015GL063220.
- **Source File**: MOCproxy_for_figshare_v1.mat
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/MOCproxy_for_figshare_v1.mat
- **License**: CC-BY 4.0
- **Source Url**: 
- **Variable Mapping**: {'time': 'TIME', 'mocproxy': 'MOC_PROXY', 'umoproxy': 'TRANS_UMO_PROXY', 'h1umo': 'SSHA', 'gs': 'TRANS_FC', 'umo': 'TRANS_UMO', 'ek': 'TRANS_EKMAN', 'moc': 'MOC', 'unadw': 'TRANS_1100_3000', 'lnadw': 'TRANS_3000_5000', 'ek_grid': 'TRANS_EKMAN__GRID', 'gs_grid': 'TRANS_FC_GRID'}
- **Featuretype**: timeSeries
- **Weblink**: 
