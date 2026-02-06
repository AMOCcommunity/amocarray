CALAFAT2025 Dataset Report
==========================

Generated: 2026-02-06 23:23:18

Bayesian_estimates_Atlantic_MHT.nc
----------------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data
- **Description**: MHT estimates dataset
- **Citation**: Calafat, F. M., Vallivattathillam, P., & Frajka-Williams, E. (2025). Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data [Data set]. Zenodo. https://doi.org/10.5281/zenodo.16640426
- **Acknowledgement**: Calafat et al. 2025, doi:10.5194/os-21-2743-2025
- **Source File**: Bayesian_estimates_Atlantic_MHT.nc
- **Data Product**: MHT estimates at 12 latitudes across the Atlantic based on spatiotemporal Bayesian hierarchical model
- **Time Coverage**: 2004-02-14 to 2020-08-14
- **Record Length**: 67 observations (16.5 years)
- **Sampling Frequency**: 3-monthly

**Citation:**

    Calafat, F. M., Vallivattathillam, P., & Frajka-Williams, E. (2025). Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data [Data set]. Zenodo. https://doi.org/10.5281/zenodo.16640426

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 3
- **Total Coordinates**: 1
- **Dataset Size**: 47.03 MB

Coordinate Information
^^^^^^^^^^^^^^^^^^^^^^

The following table shows information about the dataset coordinates:

+------------+-------------------+-----------------------------------------+------------------------------------+-------+------------+------------+
| Coordinate | Standardized Name | Description                             | Units                              | Size  | Min Value  | Max Value  |
+============+===================+=========================================+====================================+=======+============+============+
| TIME       | TIME              | Time elapsed since 1970-01-01T00:00:00Z | seconds since 1970-01-01T00:00:00Z | (67,) | 2004-02-14 | 2020-08-14 |
+------------+-------------------+-----------------------------------------+------------------------------------+-------+------------+------------+


Variable Mapping and Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the mapping from original variable names to standardized names,
along with key statistics for each variable.

+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+
| Original Variable | Standardized Name | Description                                                                                                                                                                                                                                                                                    | Units         | Size           | Min Value | Max Value | Missing % |
+===================+===================+================================================================================================================================================================================================================================================================================================+===============+================+===========+===========+===========+
| latitude          | LATITUDE          | **Latitude of zonal sections**: Latitude of zonal sections across which heat transport is computed                                                                                                                                                                                             | degrees_north | (12,)          | -35.00    | 65.00     | 0.0%      |
+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+
| mht               | MHT               | **Meridional Heat Transport**: These estimates have been computed by setting the transport at 65N equal to zero and then integrating the heat transport convergences southward. A time-mean value of 0.506 PW has been added to the transport at 60N based on estimates from the OSNAP project | PW            | (12, 67, 4000) | -1.04     | 1.92      | 0.0%      |
+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+
| htc               | HTC               | **Heat Transport Convergence**: Regions are ordered from north to south. That is, htc(:,:,1) corresponds to the northernmost region, which is bounded by latitude(1) and latitude(2)                                                                                                           | PW            | (11, 67, 4000) | -0.71     | 0.60      | 1.5%      |
+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+
| LATITUDE          | LATITUDE          | **Latitude of zonal sections**: Latitude of zonal sections across which heat transport is computed                                                                                                                                                                                             | degrees_north | (12,)          | -35.00    | 65.00     | 0.0%      |
+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+
| MHT               | MHT               | **Meridional Heat Transport**: These estimates have been computed by setting the transport at 65N equal to zero and then integrating the heat transport convergences southward. A time-mean value of 0.506 PW has been added to the transport at 60N based on estimates from the OSNAP project | PW            | (12, 67, 4000) | -1.04     | 1.92      | 0.0%      |
+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+
| HTC               | HTC               | **Heat Transport Convergence**: Regions are ordered from north to south. That is, htc(:,:,1) corresponds to the northernmost region, which is bounded by latitude(1) and latitude(2)                                                                                                           | PW            | (11, 67, 4000) | -0.71     | 0.60      | 1.5%      |
+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+----------------+-----------+-----------+-----------+


Complete Metadata
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Observation-based probabilistic estimates of Atlantic meridional heat transport
- **Platform**: Argo floats, altimetry, gravimetry data
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Time Coverage Start**: 2004-02-14
- **Time Coverage End**: 2020-08-14
- **Program**: Calafat2025
- **Project**: Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data
- **Contributor Name**: Francisco Calafat, Parvathi Vallivattathillam, Eleanor Frajka-Williams
- **Contributor Email**: , , 
- **Contributor Id**: , , 
- **Contributor Role**: Owner, Data Scientist, PI
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Contributing Institutions**: National Oceanography Centre, UK / University of the Balearic Islands, Spain
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Web Link**: https://zenodo.org/records/16640426
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
- **Featuretype**: timeSeries
- **Creation Data**: 31-Jul-2025 15:14:49
- **Contact**: francisco.mcalafat@uib.eu
- **Comment On Temporal Resolution**: Estimates of heat transport are quarterly values (i.e., 3-month means: Jan-Feb-Mar, Apr-May-Jun, ...)
- **Source File**: Bayesian_estimates_Atlantic_MHT.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/Bayesian_estimates_Atlantic_MHT.nc
- **Amocatlas Datasource**: calafat2025
- **Applied Variable Mapping**: {'latitude': 'LATITUDE', 'mht': 'MHT', 'htc': 'HTC', 'TIME': 'TIME', 'LATITUDE': 'LATITUDE', 'MHT': 'MHT', 'HTC': 'HTC'}
- **Description**: MHT estimates dataset
- **Acknowledgment**: This work has been carried out within the framework of the EPOC project funded by the European Union's Horizon Europe programme (grant agreement No 101059547), under call HORIZON-CL6-2021-CLIMATE01.
- **License**: None
- **Convections**: CF-1.8, ACDD-1.3
- **Summary**: MHT estimates dataset
- **Acknowledgement**: Calafat et al. 2025, doi:10.5194/os-21-2743-2025
- **Data Product**: MHT estimates at 12 latitudes across the Atlantic based on spatiotemporal Bayesian hierarchical model
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types

Metadata Processing Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added by AMOCatlas processing:**

- **Source File**: Bayesian_estimates_Atlantic_MHT.nc
- **Source Path**: /Users/eddifying/Cloudfree/github/AMOCatlas/data/Bayesian_estimates_Atlantic_MHT.nc
- **Amocatlas Datasource**: calafat2025
- **Comment**: Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas
