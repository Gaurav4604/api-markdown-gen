
 [Open-Meteo](/)

* ---
* [Home](/ "Weather API")
* [Features](/en/features "API Features")
* [Pricing](/en/pricing "Pricing")
* [API Docs](/en/docs "Documentation")

* ---
* [GitHub](https://github.com/open-meteo/open-meteo)
* [Twitter](https://twitter.com/open_meteo)
* ---
* Toggle theme
  + Light
  + Dark
  + Auto

# Climate API

Explore Climate Change on a Local Level with High-Resolution Climate Data

 Available APIs

* [Weather Forecast](/en/docs)
* [Historical Weather](/en/docs/historical-weather-api)
* [Ensemble Models](/en/docs/ensemble-api)
* [Climate Change](/en/docs/climate-api)
* [Marine Forecast](/en/docs/marine-weather-api)
* [Air Quality](/en/docs/air-quality-api)
* [Geocoding](/en/docs/geocoding-api)
* [Elevation](/en/docs/elevation-api)
* [Flood](/en/docs/flood-api)
  Read the [blog article](https://openmeteo.substack.com/p/climate-change-api) with more information
about climate models and how data is downscaled to 10 km resolution.
## Location and Time

* Location:
* Coordinates
* List
  Latitude   Longitude  America/AnchorageAmerica/Los\_AngelesAmerica/DenverAmerica/ChicagoAmerica/New\_YorkAmerica/Sao\_PauloNot set (GMT+0)GMT+0Automatically detect time zoneEurope/LondonEurope/BerlinEurope/MoscowAfrica/CairoAsia/BangkokAsia/SingaporeAsia/TokyoAustralia/SydneyPacific/Auckland Timezone   Search       Start Date  End Date

Quick:
1950-2050 2015-2050

## Daily Weather Variables

 Mean Temperature (2 m)  Maximum Temperature (2 m)  Minimum Temperature (2 m)  Mean Wind Speed (10 m)  Max Wind Speed (10 m)  Mean Cloud Cover  Shortwave Radiation Sum   Mean Relative Humidity (2 m)  Maximum Relative Humidity (2 m)  Minimum Relative Humidity (2 m)  Mean Dewpoint (2 m)  Minimum Dewpoint (2 m)  Maximum Dewpoint (2 m)   Precipitation Sum  Rain Sum  Snowfall Sum  Sealevel Pressure  Mean Soil Moisture (0-10 cm)  Reference Evapotranspiration (ET₀)
## Climate models 7 / 7

 CMCC\_CM2\_VHR4 (30 km)  FGOALS\_f3\_H (28 km)  HiRAM\_SIT\_HR (25 km)  MRI\_AGCM3\_2\_S (20 km)  EC\_Earth3P\_HR (29 km)  MPI\_ESM1\_2\_XR (51 km)  NICAM16\_8S (31 km)
## Settings

 Raw data. Disable statistical downscaling with ERA5-Land (10 km) Celsius °CFahrenheit °F Temperature Unit Km/hm/sMphKnots Wind Speed Unit MillimeterInch Precipitation Unit ISO 8601 (e.g. 2022-12-31)Unix timestamp Timeformat

* Usage License:
* Non-Commercial
* Commercial
* Self-Hosted
 Only for **non-commercial use** and less than 10.000 daily API calls. See [Terms](/en/terms) for more details.
## API Response

* Preview:
* Chart And URL
* Python
* Typescript
* Swift
* Other
  Loading...  [Download XLSX](https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=1950-01-01&end_date=2050-12-31&models=CMCC_CM2_VHR4,FGOALS_f3_H,HiRAM_SIT_HR,MRI_AGCM3_2_S,EC_Earth3P_HR,MPI_ESM1_2_XR,NICAM16_8S&daily=temperature_2m_max&format=xlsx) [Download CSV](https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=1950-01-01&end_date=2050-12-31&models=CMCC_CM2_VHR4,FGOALS_f3_H,HiRAM_SIT_HR,MRI_AGCM3_2_S,EC_Earth3P_HR,MPI_ESM1_2_XR,NICAM16_8S&daily=temperature_2m_max&format=csv) API URL ([Open in new tab](https://climate-api.open-meteo.com/v1/climate?latitude=52.52&longitude=13.41&start_date=1950-01-01&end_date=2050-12-31&models=CMCC_CM2_VHR4,FGOALS_f3_H,HiRAM_SIT_HR,MRI_AGCM3_2_S,EC_Earth3P_HR,MPI_ESM1_2_XR,NICAM16_8S&daily=temperature_2m_max) or copy this
URL into your application).

Note: This API call is equivalent to **1844.5** calls because of factors like long time intervals, the number of locations, variables, or models involved.

## Data Sources

This API utilizes regional downscaled climate models with up to 20 kilometer resolution from
the [HighResMip working group](https://hrcm.ceda.ac.uk/research/cmip6-highresmip/ "CMIP6 HighResMIP"), which are part of the IPCC CMIP6 project.

The API offers climate data at a regional, rather than continental, level by downsizing it to
a 10 km resolution. This allows for direct comparison of various climate models to identify
vulnerable regions to climate change impacts or assessing the impact of climate change on
specific sectors, such as agriculture or public health. The reference point used is ERA5-Land,
which is accessible through the [Historical Weather API](/en/docs/historical-weather-api "Historical Weather Information via API").

With typical weather variables in daily resolution data from 1950 to 2050 data allows
estimation of common climate parameters like the number of days with temperatures exceeding
30°C or duration and frequency of droughts. Furthermore, daily data enables running of models
to predict crop yield, pest infestation, and water balance.

While the data from past and recent years is available, it should not be mistaken for actual
measurements, as it serves the purpose of model validation rather than showing actual past
weather.

Projections beyond 2050 are highly dependent on different emission scenarios. The high
resolution climate models are as close to RCP8.5 as possible within CMIP6. While other models
consider different emission scenarios, the variations in these scenarios are less noticeable
until 2050. Projections until 2100 are not part of this API.

The climate models available in this API vary in their accuracy and level of uncertainty, and
depending on the analysis, some models may be more suitable than others. It is not possible to
provide a general recommendation on which model is better. It is recommended to run analyses
with multiple models and evaluate their performance afterward.

| Climate Model | Origin | Run by | Resolution | Description |
| --- | --- | --- | --- | --- |
| [CMCC-CM2-VHR4](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.CMCC.CMCC-CM2-VHR4) | Italy | Fondazione Centro Euro-Mediterraneo sui Cambiamenti Climatici, Lecce (CMCC) | 30 km |  |
| [FGOALS\_f3\_H](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.CAS.FGOALS-f3-H) | China | Chinese Academy of Sciences, Beijing (CAS) | 28 km | [Model](https://link.springer.com/content/pdf/10.1007/s00376-022-2030-5.pdf) |
| [HiRAM\_SIT\_HR](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.AS-RCEC.HiRAM-SIT-HR) | Taiwan | Research Center for Environmental Changes, Academia Sinica, Nankang, Taipei (AS-RCEC) | 25 km |  |
| [MRI\_AGCM3\_2\_S](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.MRI.MRI-AGCM3-2-S.highresSST-present) | Japan | Meteorological Research Institute, Tsukuba, Ibaraki (MRI) | 20 km |  |
| [EC\_Earth3P\_HR](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.EC-Earth-Consortium.EC-Earth3P-HR) | Europe | EC-Earth consortium, Rossby Center, Swedish Meteorological and Hydrological Institute/SMHI, Norrkoping, Sweden | 29 km | [Model](https://gmd.copernicus.org/articles/13/3507/2020/) |
| [MPI\_ESM1\_2\_XR](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.MPI-M.MPI-ESM1-2-XR) | Germany | Max Planck Institute for Meteorology, Hamburg 20146, Germany | 51 km | [Model](https://gmd.copernicus.org/articles/12/3241/2019/) |
| [NICAM16\_8S](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.MIROC.NICAM16-8S) | Japan | Japan Agency for Marine-Earth Science and Technology, Kanagawa 236-0001, Japan (MIROC) | 31 km | [Model](https://gmd.copernicus.org/articles/14/795/2021/) |

Some weather variables may not be available in all climate models. Notably, soil moisture is
only available in
MRI-AGCM3-2-S and EC\_Earth3P\_HR. Additionally, some models may not
provide certain aggregations, such as maximum relative humidity. However, mean relative humidity
is generally available. The table below outlines the weather variables that are available in
each model:

⚠️ = Only daily mean values available. No daily minima or maxima.
| Model | Temperature | RelativeHumidity | Wind | Precipitation | Snowfall,Solar Radiation &Clouds | Soil moisture |
| --- | --- | --- | --- | --- | --- | --- |
| CMCC-CM2-VHR4 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| FGOALS-f3-H | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ |
| HiRAM-SIT-HR | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ |
| MRI-AGCM3-2-S | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| EC\_Earth3P\_HR | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| MPI\_ESM1\_2\_XR | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| NICAM16\_8S | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

## API Documentation

The API endpoint /v1/climate allows users to retrieve climate weather data from multiple
climate models. To use this endpoint, you can specify a geographical coordinate, a time interval,
and a list of weather variables that they are interested in. It is recommended to use the full time
range of 1950 to 2050.

All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitudelongitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. |
| start\_dateend\_date | String (yyyy-mm-dd) | Yes |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-12-31). Data is available from 1950-01-01 until 2050-01-01. |
| models | String array | Yes |  | A list of climate models separated by comma. 7 climate models are available CMCC\_CM2\_VHR4, FGOALS\_f3\_H, HiRAM\_SIT\_HR MRI\_AGCM3\_2\_S, EC\_Earth3P\_HR, MPI\_ESM1\_2\_XR, and NICAM16\_8S are supported. |
| daily | String array | Yes |  | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. |
| temperature\_unit | String | No | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit. |
| wind\_speed\_unit | String | No | kmh | Other wind speed speed units: ms, mph and kn |
| precipitation\_unit | String | No | mm | Other precipitation amount units: inch |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0! For daily values with unix timestamp, please apply utc\_offset\_seconds again to get the correct date. |
| disable\_bias\_correction | Bool | No | false | Setting disable\_bias\_correction to true disables statistical downscaling and bias correction onto ERA5-Land. By default, all data is corrected using linear bias correction, and coefficients have been calculated for each month over a 50-year time series. The climate change signal is not affected by linear bias correction. |
| cell\_selection | String | No | land | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters may be added. For API stability, no required parameters will
be added in the future!

### Daily Parameter Definition

The climate data in this API is presented as daily aggregations. Multiple weather variables can
be retrieved at once. The parameter &daily= accepts the following values as comma separated
list:

| Variable | Unit | Description |
| --- | --- | --- |
| temperature\_2m\_maxtemperature\_2m\_mintemperature\_2m\_mean | °C (°F) | Maximum, minimum and mean daily air temperature at 2 meters above ground. Additionally, temperature is downscaled using a 90-meter digital elevation model. Climate models are not perfect, and they have inherent uncertainties and biases that can affect the accuracy of their temperature predictions. However, the temperature anomaly over a long period of time is a good indicator the future Earth's climate. The following paper analyses the [robustness of CMIP6 temperature predictions](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020EF001667). |
| cloud\_cover\_mean | % | Mean cloud cover on a given day. Cloud cover in climate models is generally represented through simplified parameterizations that estimate the cloud amount, height, and thickness based on atmospheric conditions such as temperature, humidity, and wind speed. These parameterizations have been shown to provide reasonable estimates of global cloud cover but they can have significant uncertainties and biases on regional and local scales. Systematic biases have been corrected using the weather reanalysis ERA5. |
| relative\_humidity\_2m\_maxrelative\_humidity\_2m\_minrelative\_humidity\_2m\_mean | % | Maximum, minimum and mean daily relative humidity at 2 meters above ground. While systematic biases in relative humidity have been removed through bias correction, caution should still be exercised when using relative humidity data as raw data shows larger differences between different climate models. |
| soil\_moisture\_0\_to\_10cm\_mean | m³/m³ | Daily mean soil moisture fraction within 0-10 cm. Soil moisture data is only available by MRI\_AGCM3\_2\_S and EC\_Earth3P\_HR. Due to the limited number of climate models that provide soil moisture data, it is not possible to make a general statement about their accuracy. As a result, it may be advisable to conduct your own water balance modeling. |
| precipitation\_sum | mm | Sum of daily precipitation (including rain, showers and snowfall). Climate models have been able to capture some of the large-scale patterns of precipitation and associated droughts and extreme precipitation events, particularly over longer time scales. However, there are still uncertainties associated with the representation of precipitation at smaller geographical scales including thunderstorm. Please compare different climate models for drought duration or extreme precipitation events. The following papers analyze [extreme precipitation](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EF002196) and [droughts in CMIP6 models](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EF002150). |
| rain\_sum | mm | Sum of daily liquid rain, excluding snow. |
| snowfall\_sum | cm | Sum of daily snowfall. Please note that snowfall data may have larger biases in complex terrain, as it is not adjusted for different terrain elevations. Use this data with caution to estimate how mountainous regions will be effected by reduced snowfall. |
| wind\_speed\_10m\_meanwind\_speed\_10m\_max | km/h (mph, m/s, knots) | Mean and maximum wind speed 10 meter above ground on a day. Simulations of winds and pressure systems in climate models are greatly influenced by the resolution used to model the terrain. Without bias correction, wind speed can vary significantly between different climate models, particularly in complex terrain. Although, data is bias corrected with ERA5, it might not accurately represent local conditions. |
| pressure\_msl\_mean | hPa | Daily mean air pressure reduced to mean sea level. |
| shortwave\_radiation\_sum | MJ/m² | The sum of solar radiation on a given day in Megajoules. Shortwave radiation predictions are impacted by aerosols and clouds present in the atmosphere. The future composition of gases in the atmosphere is a key area of study in climate modeling. As there are uncertainties associated with aerosols and clouds, it is important to take these into account when using shortwave radiation data. |

### JSON Return Object

On success a JSON object will be returned. Please note: the resulting JSON might be multiple
mega bytes in size.

```

  "latitude": 52.52,
  "longitude": 13.419,
  "generationtime_ms": 2.2119,
  "timezone": "Europe/Berlin",
  "timezone_abbreviation": "CEST",
  "daily": {
    "time": ["2022-07-01", "2022-07-01", "2022-07-01", ...],
    "temperature_2m_max": [13, 12.7, 12.7, 12.5, 12.5, 12.8, ...]
  },
  "daily_units": {
    "temperature_2m": "°C"
  },

```

| Parameter | Format | Description |
| --- | --- | --- |
| latitude, longitude | Floating point | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometers away from the requested coordinate. |
| generationtime\_ms | Floating point | Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements. |
| utc\_offset\_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezonetimezone\_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| daily | Object | For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| daily\_units | Object | For each selected daily weather variable, the unit will be listed here. |

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error": true,
  "reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"

```
## Citation & Acknowledgement

CMIP6 model data is licensed under a Creative Commons Attribution 4.0 International License ([CC BY 4.0](https://creativecommons.org/licenses/)). Consult
<https://pcmdi.llnl.gov/CMIP6/TermsOfUse> for terms
of use governing CMIP6 output, including citation requirements and proper acknowledgment. The data
producers and data providers make no warranty, either express or implied, including, but not limited
to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from
the supply of the information (including any liability arising in negligence) are excluded to the fullest
extent permitted by law.

All users of Open-Meteo data must provide a clear attribution to the CMIP6 program as well as a
reference to Open-Meteo.

Open-Meteo

* [Features](/en/features)
* [Pricing](/en/pricing)
* [About us & Contact](/en/about)
* [License](/en/license)
* [Terms & Privacy](/en/terms)

Weather APIs

* [Weather Forecast API](/en/docs)
* [Historical Weather API](/en/docs/historical-weather-api)
* [ECMWF API](/en/docs/ecmwf-api)
* [GFS & HRRR Forecast API](/en/docs/gfs-api)
* [Météo-France API](/en/docs/meteofrance-api)
* [DWD ICON API](/en/docs/dwd-api)
* [GEM API](/en/docs/gem-api)
* [JMA API](/en/docs/jma-api)
* [Met Norway API](/en/docs/metno-api)

Other APIs

* [Ensemble API](/en/docs/ensemble-api)
* [Climate Change API](/en/docs/climate-api)
* [Marine Weather API](/en/docs/marine-weather-api)
* [Air Quality API](/en/docs/air-quality-api)
* [Geocoding API](/en/docs/geocoding-api)
* [Elevation API](/en/docs/elevation-api)
* [Flood API](/en/docs/flood-api)

External

* [GitHub](https://github.com/open-meteo/open-meteo)
* [Blog](https://openmeteo.substack.com/archive?sort=new)
* [Twitter](https://twitter.com/open_meteo)
* [Mastodon](https://fosstodon.org/%40openmeteo)
* [Service status and uptime](https://status.open-meteo.com)
* [Model Updates Overview](/en/docs/model-updates)
 © 2022-2025 Copyright: Open-Meteo.com

