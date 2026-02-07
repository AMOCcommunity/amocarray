ARCTICGATEWAY Dataset Report
============================

*Generated: 2026-02-07*

This report covers all available ARCTICGATEWAY datasets.

----

Adjusted_fulldepth/FramStrait_adjusted_v_fulldepth.nc
-----------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **DOI**: https://doi.org/10.21334/npolar.2025.80b69907
- **Source File**: Adjusted_fulldepth/FramStrait_adjusted_v_fulldepth.nc
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Fram Strait
- **Time Coverage**: 2004-10-15 to 2022-05-15
- **Record Length**: 212 observations (17.6 years)
- **Sampling Frequency**: monthly

**Citation:**

    Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, R., Lee, C., Lenetsky, J., & Woodgate, R. (2025). Pan-Arctic Gateway transports since 2004 [Dataset]. Norwegian Polar Institute. https://doi.org/10.21334/NPOLAR.2025.80B69907

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 3
- **Total Coordinates**: 4
- **Dataset Size**: 755.07 MB

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
   * - *depth* → **DEPTH**
     - **Depth**:  Depth below surface of the water
     - meters
     - (665,)
     - 0.00
     - 2656.00
     - 0.0%
   * - *lat* → **LATITUDE**
     - **Latitude**: Latitude north (WGS84)
     - degrees_north
     - ()
     - 78.83
     - 78.83
     - 0.0%
   * - *lon* → **LONGITUDE**
     - **Longitude**: Longitude east (WGS84)
     - degrees_east
     - (234,)
     - -20.55
     - 11.87
     - 0.0%
   * - *time* → **TIME**
     - Time
     - datetime64[ns]
     - (212,)
     - 2004-10-15
     - 2022-05-15
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
   * - **CT**
     - **Cons. Temperature**: Conservative Temperature (TEOS-10)
     - degrees_Celsius
     - (212, 665, 234)
     - -2.74
     - 7.34
     - 5.7%
   * - **SA**
     - **Abs. Salinity**: Absolute Salinity (TEOS-10)
     - g kg-1
     - (212, 665, 234)
     - 27.84
     - 35.67
     - 5.7%
   * - *v* → **VCUR**
     - **V Velocity**: Northward Velocity component
     - m s-1
     - (212, 665, 234)
     - -0.49
     - 0.43
     - 5.7%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Pan-Arctic Gateway transports since 2004
- **Summary**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Program**: Pan-Arctic Gateway transports since 2004
- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Source**: Mooring and CTD data
- **License**: CC-BY-4.0
- **Acknowledgment**: The mooring data from the Arctic Gateways are provided by the Norwegian Polar Institute (Tromsø, Norway), the Alfred Wegener Institute (Bremerhaven, Germany), the Institute for Marine Research (Bergen, Norway) and the Applied Physics Laboratory, Univ. of Washington (Seattle, USA).
- **Doi**: https://doi.org/10.21334/npolar.2025.80b69907
- **Weblink**: https://doi.org/10.21334/NPOLAR.2025.80B69907
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Fram Strait
- **Time Coverage Start**: 2004-10-15
- **Time Coverage End**: 2022-05-15
- **Creator Institution**: Norwegian Polar Institute (NPI)
- **Contributor Name**: Norwegian Polar Institute (NPI), Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, Lee, C., Lenetsky, J., & Woodgate, R
- **Contributor Role**: 
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Contributor Email**: , , , , , , , , , , , , , , , 
- **Contributor Id**: www.npolar.no, , , , , , , , , , , , , , , 
- **Contributing Institutions**: Norwegian Polar Institute, Norwegian Polar Institute (NPI)
- **Contributing Institutions Vocabulary**: , 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Publisher Type**: institution
- **Conventions**: , OceanSITES-1.5
- **featureType**: timeSeries
- **featureType_vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: Adjusted_fulldepth/FramStrait_adjusted_v_fulldepth.nc
- **Source Path\***: ~/AMOCatlas/data/Adjusted_fulldepth/FramStrait_adjusted_v_fulldepth.nc
- **Date Created**: 2025-10-31T23:55:53Z
- **Date Modified**: 2026-02-07T21:43:25Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Processing Datasource\***: arcticgateway
- **Product Version**: v0
- **Applied Variable Mapping**: {'time': 'TIME', 'depth': 'DEPTH', 'lon': 'LONGITUDE', 'lat': 'LATITUDE', 'v': 'VCUR', 'TIME': 'TIME', 'DEPTH': 'DEPTH'}
- **Gateway**: FramStrait
- **Adjustments**: v is adjusted by a constant monthly value obtained from the inverse model, for all grid cells in a segment
- **Depth Limit**: None
- **Segments Format**: Python dictionary converted to a string. The slices can be applied in xarray coordinate selection
- **Segments**: {'EGS': {'long_name': 'East Greenland Shelf', 'lon_slice': slice(None, -10.6, None)}, 'EGC': {'long_name': 'East Greenland Current', 'lon_slice': slice(-10.6, -0.6, None)}, 'CFS': {'long_name': 'Central Fram Strait', 'lon_slice': slice(-0.6, 5.1, None)}, 'WSC': {'long_name': 'West Spitsbergen Current', 'lon_slice': slice(5.1, 8.805, None)}, 'WSS': {'long_name': 'West Spitsbergen Shelf', 'lon_slice': slice(8.805, None, None)}}
- **Project Website**: https://epoc-eu.org
- **Data Set Language**: eng
- **Data Assembly Center**: NO/NPI
- **Creator Type**: institution

----

Adjusted_fulldepth/DavisStrait_adjusted_v_fulldepth.nc
------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **DOI**: https://doi.org/10.21334/npolar.2025.80b69907
- **Source File**: Adjusted_fulldepth/DavisStrait_adjusted_v_fulldepth.nc
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Davis Strait
- **Time Coverage**: 2004-10-15 to 2022-05-15
- **Record Length**: 212 observations (17.6 years)
- **Sampling Frequency**: monthly

**Citation:**

    Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, R., Lee, C., Lenetsky, J., & Woodgate, R. (2025). Pan-Arctic Gateway transports since 2004 [Dataset]. Norwegian Polar Institute. https://doi.org/10.21334/NPOLAR.2025.80B69907

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 3
- **Total Coordinates**: 4
- **Dataset Size**: 159.52 MB

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
   * - *depth* → **DEPTH**
     - **Depth**:  Depth below surface of the water
     - meters
     - (263,)
     - 0.00
     - 1048.00
     - 0.0%
   * - *lat* → **LATITUDE**
     - **Latitude**: Latitude north (WGS84)
     - degrees_north
     - (125,)
     - 66.67
     - 67.32
     - 0.0%
   * - *lon* → **LONGITUDE**
     - **Longitude**: Longitude east (WGS84)
     - degrees_east
     - (125,)
     - -61.26
     - -53.87
     - 0.0%
   * - *time* → **TIME**
     - Time
     - datetime64[ns]
     - (212,)
     - 2004-10-15
     - 2022-05-15
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
   * - **CT**
     - **Cons. Temperature**: Conservative Temperature (TEOS-10)
     - degrees_Celsius
     - (212, 263, 125)
     - -1.75
     - 6.74
     - 0.4%
   * - **SA**
     - **Abs. Salinity**: Absolute Salinity (TEOS-10)
     - g kg-1
     - (212, 263, 125)
     - 30.12
     - 35.25
     - 0.4%
   * - *v* → **VCUR**
     - **V Velocity**: Northward Velocity component
     - m s-1
     - (212, 263, 125)
     - -0.44
     - 0.19
     - 0.4%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Pan-Arctic Gateway transports since 2004
- **Summary**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Program**: Pan-Arctic Gateway transports since 2004
- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Source**: Mooring and CTD data
- **License**: CC-BY-4.0
- **Acknowledgment**: The mooring data from the Arctic Gateways are provided by the Norwegian Polar Institute (Tromsø, Norway), the Alfred Wegener Institute (Bremerhaven, Germany), the Institute for Marine Research (Bergen, Norway) and the Applied Physics Laboratory, Univ. of Washington (Seattle, USA).
- **Doi**: https://doi.org/10.21334/npolar.2025.80b69907
- **Weblink**: https://doi.org/10.21334/NPOLAR.2025.80B69907
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Davis Strait
- **Time Coverage Start**: 2004-10-15
- **Time Coverage End**: 2022-05-15
- **Creator Institution**: Norwegian Polar Institute (NPI)
- **Contributor Name**: Norwegian Polar Institute (NPI), Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, Lee, C., Lenetsky, J., & Woodgate, R
- **Contributor Role**: 
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Contributor Email**: , , , , , , , , , , , , , , , 
- **Contributor Id**: www.npolar.no, , , , , , , , , , , , , , , 
- **Contributing Institutions**: Norwegian Polar Institute, Norwegian Polar Institute (NPI)
- **Contributing Institutions Vocabulary**: , 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Publisher Type**: institution
- **Conventions**: , OceanSITES-1.5
- **featureType**: timeSeries
- **featureType_vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: Adjusted_fulldepth/DavisStrait_adjusted_v_fulldepth.nc
- **Source Path\***: ~/AMOCatlas/data/Adjusted_fulldepth/DavisStrait_adjusted_v_fulldepth.nc
- **Date Created**: 2025-10-31T23:55:53Z
- **Date Modified**: 2026-02-07T21:43:25Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Processing Datasource\***: arcticgateway
- **Product Version**: v0
- **Applied Variable Mapping**: {'time': 'TIME', 'depth': 'DEPTH', 'lon': 'LONGITUDE', 'lat': 'LATITUDE', 'v': 'VCUR', 'TIME': 'TIME', 'DEPTH': 'DEPTH'}
- **Gateway**: DavisStrait
- **Adjustments**: v is adjusted by a constant monthly value obtained from the inverse model, for all grid cells in a segment
- **Depth Limit**: None
- **Segments Format**: Python dictionary converted to a string. The slices can be applied in xarray coordinate selection
- **Segments**: {'WDS': {'long_name': 'Western Davis Strait', 'lon_slice': slice(None, -57.6, None)}, 'EDS': {'long_name': 'Eastern Davis Strait', 'lon_slice': slice(-57.6, None, None)}}
- **Project Website**: https://epoc-eu.org
- **Data Set Language**: eng
- **Data Assembly Center**: NO/NPI
- **Creator Type**: institution

----

Adjusted_fulldepth/BeringStrait_adjusted_v_fulldepth.nc
-------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **DOI**: https://doi.org/10.21334/npolar.2025.80b69907
- **Source File**: Adjusted_fulldepth/BeringStrait_adjusted_v_fulldepth.nc
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Bering Strait
- **Time Coverage**: 2004-10-15 to 2022-05-15
- **Record Length**: 212 observations (17.6 years)
- **Sampling Frequency**: monthly

**Citation:**

    Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, R., Lee, C., Lenetsky, J., & Woodgate, R. (2025). Pan-Arctic Gateway transports since 2004 [Dataset]. Norwegian Polar Institute. https://doi.org/10.21334/NPOLAR.2025.80B69907

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 3
- **Total Coordinates**: 4
- **Dataset Size**: 2.56 MB

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
   * - *depth* → **DEPTH**
     - **Depth**:  Depth below surface of the water
     - meters
     - (16,)
     - 0.00
     - 60.00
     - 0.0%
   * - *lat* → **LATITUDE**
     - **Latitude**: Latitude north (WGS84)
     - degrees_north
     - (33,)
     - 65.69
     - 66.01
     - 0.0%
   * - *lon* → **LONGITUDE**
     - **Longitude**: Longitude east (WGS84)
     - degrees_east
     - (33,)
     - -169.67
     - -168.11
     - 0.0%
   * - *time* → **TIME**
     - Time
     - datetime64[ns]
     - (212,)
     - 2004-10-15
     - 2022-05-15
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
   * - **CT**
     - No description available
     - degrees_Celsius
     - (212, 16, 33)
     - -1.83
     - 5.44
     - 6.2%
   * - **SA**
     - No description available
     - g kg-1
     - (212, 16, 33)
     - 31.17
     - 33.56
     - 6.2%
   * - *v* → **VCUR**
     - velocity normal to gateway
     - m s-1
     - (212, 16, 33)
     - -0.08
     - 0.37
     - 6.2%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Pan-Arctic Gateway transports since 2004
- **Summary**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Program**: Pan-Arctic Gateway transports since 2004
- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Source**: Mooring and CTD data
- **License**: CC-BY-4.0
- **Acknowledgment**: The mooring data from the Arctic Gateways are provided by the Norwegian Polar Institute (Tromsø, Norway), the Alfred Wegener Institute (Bremerhaven, Germany), the Institute for Marine Research (Bergen, Norway) and the Applied Physics Laboratory, Univ. of Washington (Seattle, USA).
- **Doi**: https://doi.org/10.21334/npolar.2025.80b69907
- **Weblink**: https://doi.org/10.21334/NPOLAR.2025.80B69907
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Bering Strait
- **Time Coverage Start**: 2004-10-15
- **Time Coverage End**: 2022-05-15
- **Creator Institution**: Norwegian Polar Institute (NPI)
- **Contributor Name**: Norwegian Polar Institute (NPI), Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, Lee, C., Lenetsky, J., & Woodgate, R
- **Contributor Role**: 
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Contributor Email**: , , , , , , , , , , , , , , , 
- **Contributor Id**: www.npolar.no, , , , , , , , , , , , , , , 
- **Contributing Institutions**: Norwegian Polar Institute, Norwegian Polar Institute (NPI)
- **Contributing Institutions Vocabulary**: , 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Publisher Type**: institution
- **Conventions**: , OceanSITES-1.5
- **featureType**: timeSeries
- **featureType_vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: Adjusted_fulldepth/BeringStrait_adjusted_v_fulldepth.nc
- **Source Path\***: ~/AMOCatlas/data/Adjusted_fulldepth/BeringStrait_adjusted_v_fulldepth.nc
- **Date Created**: 2025-10-31T23:55:53Z
- **Date Modified**: 2026-02-07T21:43:25Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Processing Datasource\***: arcticgateway
- **Product Version**: v0
- **Applied Variable Mapping**: {'time': 'TIME', 'depth': 'DEPTH', 'lon': 'LONGITUDE', 'lat': 'LATITUDE', 'v': 'VCUR', 'TIME': 'TIME', 'DEPTH': 'DEPTH'}
- **Gateway**: BeringStrait
- **Adjustments**: v is adjusted by a constant monthly value obtained from the inverse model, for all grid cells in a segment
- **Depth Limit**: None
- **Segments Format**: Python dictionary converted to a string. The slices can be applied in xarray coordinate selection
- **Segments**: {'BS': {'long_name': 'Bering Strait', 'lon_slice': slice(None, None, None)}}
- **Project Website**: https://epoc-eu.org
- **Data Set Language**: eng
- **Data Assembly Center**: NO/NPI
- **Creator Type**: institution

----

Adjusted_fulldepth/BarentsSeaOpening_adjusted_v_fulldepth.nc
------------------------------------------------------------


Dataset Overview
^^^^^^^^^^^^^^^^

- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **DOI**: https://doi.org/10.21334/npolar.2025.80b69907
- **Source File**: Adjusted_fulldepth/BarentsSeaOpening_adjusted_v_fulldepth.nc
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Barents Sea Opening
- **Time Coverage**: 2004-10-15 to 2022-05-15
- **Record Length**: 212 observations (17.6 years)
- **Sampling Frequency**: monthly

**Citation:**

    Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, R., Lee, C., Lenetsky, J., & Woodgate, R. (2025). Pan-Arctic Gateway transports since 2004 [Dataset]. Norwegian Polar Institute. https://doi.org/10.21334/NPOLAR.2025.80B69907

Dataset Statistics
^^^^^^^^^^^^^^^^^^

- **Total Variables**: 3
- **Total Coordinates**: 4
- **Dataset Size**: 181.15 MB

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
   * - *depth* → **DEPTH**
     - **Depth**:  Depth below surface of the water
     - meters
     - (122,)
     - 0.00
     - 484.00
     - 0.0%
   * - *lat* → **LATITUDE**
     - **Latitude**: Latitude north (WGS84)
     - degrees_north
     - (306,)
     - 69.48
     - 77.70
     - 0.0%
   * - *lon* → **LONGITUDE**
     - **Longitude**: Longitude east (WGS84)
     - degrees_east
     - (306,)
     - 18.35
     - 20.31
     - 0.0%
   * - *time* → **TIME**
     - **Time**: Time in datetime format
     - datetime64[ns]
     - (212,)
     - 2004-10-15
     - 2022-05-15
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
   * - **CT**
     - **Cons. Temperature**: Conservative Temperature (TEOS-10)
     - degrees_Celsius
     - (212, 122, 306)
     - -2.40
     - 12.68
     - 45.1%
   * - **SA**
     - **Abs. Salinity**: Absolute Salinity (TEOS-10)
     - g kg-1
     - (212, 122, 306)
     - 33.41
     - 35.41
     - 45.1%
   * - *v* → **VCUR**
     - **V Velocity**: Northward Velocity component
     - m s-1
     - (212, 122, 306)
     - -0.10
     - 0.16
     - 45.1%


Metadata (edits applied noted)
^^^^^^^^^^^^^^^^^

The following metadata provides comprehensive information about this dataset:

- **Title**: Pan-Arctic Gateway transports since 2004
- **Summary**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Description**: Input data and adjusted data derived with an inverse model of ocean velocity, temperature and salinity obtained from ocean moorings and hydrography from the four main Arctic Gateways Fram Strait, Barents Sea Opening, Bering Strait and Davis Strait
- **Program**: Pan-Arctic Gateway transports since 2004
- **Project**: Explaining and predicting the ocean conveyor belt, The Fram Strait Arctic Outflow Observatory
- **Source**: Mooring and CTD data
- **License**: CC-BY-4.0
- **Acknowledgment**: The mooring data from the Arctic Gateways are provided by the Norwegian Polar Institute (Tromsø, Norway), the Alfred Wegener Institute (Bremerhaven, Germany), the Institute for Marine Research (Bergen, Norway) and the Applied Physics Laboratory, Univ. of Washington (Seattle, USA).
- **Doi**: https://doi.org/10.21334/npolar.2025.80b69907
- **Weblink**: https://doi.org/10.21334/NPOLAR.2025.80B69907
- **Data Product**: Pan-Arctic Gateway transports since 2004 - Barents Sea Opening
- **Time Coverage Start**: 2004-10-15
- **Time Coverage End**: 2022-05-15
- **Creator Institution**: Norwegian Polar Institute (NPI)
- **Contributor Name**: Norwegian Polar Institute (NPI), Fredriksen, H., de Steur, L., von Appen, W., Ingvaldsen, R., McPherson, Lee, C., Lenetsky, J., & Woodgate, R
- **Contributor Role**: 
- **Contributor Role Vocabulary**: http://vocab.nerc.ac.uk/search_nvs/W08/
- **Contributor Email**: , , , , , , , , , , , , , , , 
- **Contributor Id**: www.npolar.no, , , , , , , , , , , , , , , 
- **Contributing Institutions**: Norwegian Polar Institute, Norwegian Polar Institute (NPI)
- **Contributing Institutions Vocabulary**: , 
- **Contributing Institutions Role**: 
- **Contributing Institutions Role Vocabulary**: 
- **Publisher Type**: institution
- **Conventions**: , OceanSITES-1.5
- **featureType**: timeSeries
- **featureType_vocabulary**: https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types
- **Source File\***: Adjusted_fulldepth/BarentsSeaOpening_adjusted_v_fulldepth.nc
- **Source Path\***: ~/AMOCatlas/data/Adjusted_fulldepth/BarentsSeaOpening_adjusted_v_fulldepth.nc
- **Date Created**: 2025-10-31T23:55:53Z
- **Date Modified**: 2026-02-07T21:43:25Z
- **Processing Software**: http://github.com/AMOCcommunity/amocatlas
- **Processing Version**: v0.2.0
- **Processing Datasource\***: arcticgateway
- **Product Version**: v0
- **Applied Variable Mapping**: {'time': 'TIME', 'depth': 'DEPTH', 'lon': 'LONGITUDE', 'lat': 'LATITUDE', 'v': 'VCUR', 'TIME': 'TIME', 'DEPTH': 'DEPTH'}
- **Gateway**: BarentsSeaOpening
- **Adjustments**: v is adjusted by a constant monthly value obtained from the inverse model, for all grid cells in a segment
- **Depth Limit**: None
- **Segments Format**: Python dictionary converted to a string. The slices can be applied in xarray coordinate selection
- **Segments**: {'BSOsouth': {'long_name': 'South of Bear Island', 'lat_slice': slice(74.45, None, None)}, 'BSOnorth': {'long_name': 'North of Bear Island', 'lat_slice': slice(None, 74.45, None)}}
- **Project Website**: https://epoc-eu.org
- **Data Set Language**: eng
- **Data Assembly Center**: NO/NPI
- **Creator Type**: institution
