CALAFAT2025 Dataset Report
==========================

Generated: 2026-02-07 15:48:45

----

Bayesian_estimates_Atlantic_MHT.nc
----------------------------------

Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data
- **Description**: MHT estimates dataset
- **Source File**: Bayesian_estimates_Atlantic_MHT.nc
- **Data Product**: MHT estimates at 12 latitudes across the Atlantic based on spatiotemporal Bayesian hierarchical model
- **Time Coverage**: 2004-02-14 to 2020-08-14
- **Record Length**: 67 observations (16.5 years)
- **Sampling Frequency**: 3-monthly

**Citation:**

    Calafat, F. M., Vallivattathillam, P., & Frajka-Williams, E. (2025). Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data [Data set]. Zenodo. https://doi.org/10.5281/zenodo.16640426

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 2
- **Total Coordinates**: 3
- **Dataset Size**: 47.03 MB

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
   * - **LATITUDE**
     - **Latitude**: Latitude north (WGS84)
     - degrees_north
     - (12,)
     - -35.00
     - 65.00
     - 0.0%
   * - **LAT_BOUNDS**
     - Latitude cell boundaries
     - degrees_north
     - (12, 2)
     - -40.00
     - 67.50
     - 0.0%
   * - **TIME**
     - Time
     - datetime64[ns]
     - (67,)
     - 2004-02-14
     - 2020-08-14
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
   * - *htc* → **HTC**
     - **Heat Transport Convergence**: Regions are ordered from north to south. That is, htc(:,:,1) corresponds to the northernmost region, which is bounded by latitude(1) and latitude(2)
     - PW
     - (11, 67, 4000)
     - -0.71
     - 0.60
     - 1.5%
   * - *mht* → **MHT**
     - These estimates have been computed by setting the transport at 65N equal to zero and then integrating the heat transport convergences southward. A time-mean value of 0.506 PW has been added to the transport at 60N based on estimates from the OSNAP project
     - PW
     - (12, 67, 4000)
     - -1.04
     - 1.92
     - 0.0%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Observation-based probabilistic estimates of Atlantic meridional heat transport
- **Summary**: MHT estimates dataset
- **Description**: MHT estimates dataset
- **Program**: Calafat2025
- **Project**: Estimates of Atlantic meridional heat transport from spatiotemporal fusion of Argo, altimetry and gravimetry data
- **License**: None
- **Acknowledgment**: This work has been carried out within the framework of the EPOC project funded by the European Union's Horizon Europe programme (grant agreement No 101059547), under call HORIZON-CL6-2021-CLIMATE01.
- **Weblink**: https://zenodo.org/records/16640426
- **Platform**: Argo floats, altimetry, gravimetry data
- **Platform Vocabulary**: https://vocab.nerc.ac.uk/collection/L06/
- **Data Product**: MHT estimates at 12 latitudes across the Atlantic based on spatiotemporal Bayesian hierarchical model
- **Time Coverage Start**: 2004-02-14
- **Time Coverage End**: 2020-08-14
- **Contributor Name**: Francisco Calafat, Parvathi Vallivattathillam, Eleanor Frajka-Williams
- **Contributor Role**: Owner, Data Scientist, PI
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Contributor Email**: , , 
- **Contributor Id**: , , 
- **Contributing Institutions**: National Oceanography Centre, UK / University of the Balearic Islands, Spain
- **Contributing Institutions Vocabulary**: 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Conventions**: CF-1.8, ACDD-1.3, OceanSITES-1.5
- **Featuretype**: timeSeries
- **Featuretype Vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: Bayesian_estimates_Atlantic_MHT.nc
- **Source Path\***: ~/AMOCatlas/data/Bayesian_estimates_Atlantic_MHT.nc
- **Date Modified**: 2026-02-07T14:48:45Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Applied Variable Mapping**: {'mht': 'MHT', 'htc': 'HTC', 'TIME': 'TIME', 'LATITUDE': 'LATITUDE', 'MHT': 'MHT', 'HTC': 'HTC'}
- **Creation Data**: 31-Jul-2025 15:14:49
- **Contact**: francisco.mcalafat@uib.eu
- **Comment On Temporal Resolution**: Estimates of heat transport are quarterly values (i.e., 3-month means: Jan-Feb-Mar, Apr-May-Jun, ...)
- **Processing Datasource\***: calafat2025
- **Convections**: CF-1.8, ACDD-1.3
