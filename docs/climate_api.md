---
api-endpoint: https://climate-api.open-meteo.com/v1/climate
date: 2024-01-01
description: Downscaled IPCC climate predictions specifically tailored to a 10 km
  resolution, going beyond the limitations of continental-scale data. Explore high-resolution
  IPCC climate models, downscale predictions, and access daily climate projections
  up to 2050. Analyze climate change trends with control data dating back to 1950.
  Stay informed and make data-driven decisions for a sustainable future.
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Climate API
url: https://open-meteo.com/en/docs/climate-api
---

[blog article](https://openmeteo.substack.com/p/climate-change-api)with more information about climate models and how data is downscaled to 10 km resolution.

## API Response

[Python API client](https://pypi.org/project/openmeteo-requests/) documentation.

#### Install

```
pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas
```


#### Usage

```
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)
# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://climate-api.open-meteo.com/v1/climate"
params = {
"latitude": 52.52,
"longitude": 13.41,
"start_date": "1950-01-01",
"end_date": "2050-12-31",
"models": ["CMCC_CM2_VHR4", "FGOALS_f3_H", "HiRAM_SIT_HR", "MRI_AGCM3_2_S", "EC_Earth3P_HR", "MPI_ESM1_2_XR", "NICAM16_8S"],
"daily": "temperature_2m_max"
}
responses = openmeteo.weather_api(url, params=params)
# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_data = {"date": pd.date_range(
start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = daily.Interval()),
inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)
```


## Data Sources

This API utilizes regional downscaled climate models with up to 20 kilometer resolution from
the [HighResMip working group](https://hrcm.ceda.ac.uk/research/cmip6-highresmip/), which are part of the IPCC CMIP6 project.

The API offers climate data at a regional, rather than continental, level by downsizing it to
a 10 km resolution. This allows for direct comparison of various climate models to identify
vulnerable regions to climate change impacts or assessing the impact of climate change on
specific sectors, such as agriculture or public health. The reference point used is ERA5-Land,
which is accessible through the [Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api).

With typical weather variables in daily resolution data from 1950 to 2050 data allows estimation of common climate parameters like the number of days with temperatures exceeding 30°C or duration and frequency of droughts. Furthermore, daily data enables running of models to predict crop yield, pest infestation, and water balance.

While the data from past and recent years is available, it should not be mistaken for actual measurements, as it serves the purpose of model validation rather than showing actual past weather.

Projections beyond 2050 are highly dependent on different emission scenarios. The high resolution climate models are as close to RCP8.5 as possible within CMIP6. While other models consider different emission scenarios, the variations in these scenarios are less noticeable until 2050. Projections until 2100 are not part of this API.

The climate models available in this API vary in their accuracy and level of uncertainty, and depending on the analysis, some models may be more suitable than others. It is not possible to provide a general recommendation on which model is better. It is recommended to run analyses with multiple models and evaluate their performance afterward.

| Climate Model | Origin | Run by | Resolution | Description |
|---|---|---|---|---|
|

[FGOALS_f3_H](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.CAS.FGOALS-f3-H)

[Model](https://link.springer.com/content/pdf/10.1007/s00376-022-2030-5.pdf)[HiRAM_SIT_HR](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.AS-RCEC.HiRAM-SIT-HR)

[MRI_AGCM3_2_S](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.MRI.MRI-AGCM3-2-S.highresSST-present)

[EC_Earth3P_HR](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.EC-Earth-Consortium.EC-Earth3P-HR)

[Model](https://gmd.copernicus.org/articles/13/3507/2020/)[MPI_ESM1_2_XR](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.MPI-M.MPI-ESM1-2-XR)

[Model](https://gmd.copernicus.org/articles/12/3241/2019/)[NICAM16_8S](https://www.wdc-climate.de/ui/cmip6?input=CMIP6.HighResMIP.MIROC.NICAM16-8S)

[Model](https://gmd.copernicus.org/articles/14/795/2021/)Some weather variables may not be available in all climate models. Notably, soil moisture is only available in MRI-AGCM3-2-S and EC_Earth3P_HR. Additionally, some models may not provide certain aggregations, such as maximum relative humidity. However, mean relative humidity is generally available. The table below outlines the weather variables that are available in each model:

| Model | Temperature | Relative Humidity | Wind | Precipitation | Snowfall, Solar Radiation & Clouds | Soil moisture |
|---|---|---|---|---|---|---|
| CMCC-CM2-VHR4 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| FGOALS-f3-H | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ |
| HiRAM-SIT-HR | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ |
| MRI-AGCM3-2-S | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| EC_Earth3P_HR | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| MPI_ESM1_2_XR | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| NICAM16_8S | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

## API Documentation

The API endpoint /v1/climate allows users to retrieve climate weather data from multiple climate models. To use this endpoint, you can specify a geographical coordinate, a time interval, and a list of weather variables that they are interested in. It is recommended to use the full time range of 1950 to 2050.

All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude longitude | Floating point | Yes | ||
| start_date end_date | String (yyyy-mm-dd) | Yes | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-12-31). Data is available from 1950-01-01 until 2050-01-01. | |
| models | String array | Yes | A list of climate models separated by comma. 7 climate models are available CMCC_CM2_VHR4, FGOALS_f3_H, HiRAM_SIT_HR MRI_AGCM3_2_S, EC_Earth3P_HR, MPI_ESM1_2_XR, and NICAM16_8S are supported. | |
| daily | String array | Yes | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. | |
| temperature_unit | String | No | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit. |
| wind_speed_unit | String | No | kmh | Other wind speed speed units: ms, mph and kn |
| precipitation_unit | String | No | mm | Other precipitation amount units: inch |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date. |
| disable_bias_correction | Bool | No | false | Setting disable_bias_correction to true disables statistical downscaling and bias correction onto ERA5-Land. By default, all data is corrected using linear bias correction, and coefficients have been calculated for each month over a 50-year time series. The climate change signal is not affected by linear bias correction. |
| cell_selection | String | No | land | Set a preference how grid-cells are selected. The default land finds a
suitable grid-cell on land with
|

[pricing](https://open-meteo.com/en/pricing)for more information.Additional optional URL parameters may be added. For API stability, no required parameters will be added in the future!

### Daily Parameter Definition

The climate data in this API is presented as daily aggregations. Multiple weather variables can be retrieved at once. The parameter &daily= accepts the following values as comma separated list:

| Variable | Unit | Description |
|---|---|---|
| temperature_2m_max temperature_2m_min temperature_2m_mean | °C (°F) | Maximum, minimum and mean daily air temperature at 2 meters above ground. Additionally,
temperature is downscaled using a 90-meter digital elevation model. Climate models are
not perfect, and they have inherent uncertainties and biases that can affect the
accuracy of their temperature predictions. However, the temperature anomaly over a long
period of time is a good indicator the future Earth's climate. The following paper
analyses the
|

relative_humidity_2m_min

relative_humidity_2m_mean

[extreme precipitation](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EF002196)and[droughts in CMIP6 models](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EF002150).wind_speed_10m_max

### JSON Return Object

On success a JSON object will be returned. Please note: the resulting JSON might be multiple mega bytes in size.

` ````
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
|---|---|---|
| latitude, longitude | Floating point | |
| generationtime_ms | Floating point | |
| utc_offset_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezone timezone_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| daily | Object | |
| daily_units | Object | For each selected daily weather variable, the unit will be listed here. |

### Errors

```
"error": true,
"reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"
```


## Citation & Acknowledgement

CMIP6 model data is licensed under a Creative Commons Attribution 4.0 International License ([CC BY 4.0](https://creativecommons.org/licenses/)). Consult
[https://pcmdi.llnl.gov/CMIP6/TermsOfUse](https://pcmdi.llnl.gov/CMIP6/TermsOfUse) for terms
of use governing CMIP6 output, including citation requirements and proper acknowledgment. The data
producers and data providers make no warranty, either express or implied, including, but not limited
to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from
the supply of the information (including any liability arising in negligence) are excluded to the fullest
extent permitted by law.

All users of Open-Meteo data must provide a clear attribution to the CMIP6 program as well as a reference to Open-Meteo.