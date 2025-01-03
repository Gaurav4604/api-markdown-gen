---
api-endpoint: https://air-quality-api.open-meteo.com/v1/air-quality
date: 2024-01-01
description:
  Get accurate forecasts for gases, particulate matter (PM), and pollen
  with the Air Quality API. Access this powerful API for free for non-commercial use.
  Stay informed about air quality conditions and make informed decisions based on
  reliable data. Enhance your applications and services with real-time air quality
  information.
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Air Quality API
url: https://open-meteo.com/en/docs/air-quality-api
---

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
url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
"latitude": 52.52,
"longitude": 13.41,
"hourly": ["pm10", "pm2_5"]
}
responses = openmeteo.weather_api(url, params=params)
# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_pm10 = hourly.Variables(0).ValuesAsNumpy()
hourly_pm2_5 = hourly.Variables(1).ValuesAsNumpy()
hourly_data = {"date": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}
hourly_data["pm10"] = hourly_pm10
hourly_data["pm2_5"] = hourly_pm2_5
hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
```

## Data Sources

Forecast is based on the 11 kilometer CAMS European air quality forecast and the 40 kilometer CAMS global atmospheric composition forecasts. The European and global domain are not coupled and may show different forecasts.

| Data Set | Region | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency |
| -------- | ------ | ------------------ | ------------------- | ----------------- | ---------------- |

|

[CAMS European Air Quality Reanalysis](https://ads.atmosphere.copernicus.eu/datasets/cams-europe-air-quality-reanalyses?tab=overview)

[CAMS global atmospheric composition forecasts](https://ads.atmosphere.copernicus.eu/datasets/cams-global-atmospheric-composition-forecasts?tab=overview)

[CAMS Global Greenhouse Gas Forecast](https://ads.atmosphere.copernicus.eu/datasets/cams-global-greenhouse-gas-forecasts?tab=overview)

## API Documentation

The API endpoint /v1/air-quality accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly air quality forecast for 5 days. Time always starts at 0:00 today.

All URL parameters are listed below:

| Parameter           | Format         | Required | Default                                                                                                                                     | Description                                                                                                                                                                                                                                    |
| ------------------- | -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| latitude, longitude | Floating point | Yes      |                                                                                                                                             |                                                                                                                                                                                                                                                |
| hourly              | String array   | No       | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |                                                                                                                                                                                                                                                |
| current             | String array   | No       | A list of variables to get current conditions.                                                                                              |                                                                                                                                                                                                                                                |
| domains             | String         | No       | auto                                                                                                                                        | Automatically combine both domains auto or specifically select the European cams_europe or global domain cams_global.                                                                                                                          |
| timeformat          | String         | No       | iso8601                                                                                                                                     | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc_offset_seconds again to get the correct date. |
| timezone            | String         | No       | GMT                                                                                                                                         | If timezone is set, all timestamps are returned as local-time and data is                                                                                                                                                                      |

returned starting at 00:00 local-time. Any time zone name from the
|

past_hours

end_date

end_hour

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

| Variable                                                | Valid time | Unit          | Description                                                                 |
| ------------------------------------------------------- | ---------- | ------------- | --------------------------------------------------------------------------- |
| pm10 pm2_5                                              | Instant    | μg/m³         | Particulate matter with diameter smaller than 10 µm (PM10) and smaller than |
| 2.5 µm (PM2.5) close to surface (10 meter above ground) |
| carbon_monoxide nitrogen_dioxide sulphur_dioxide ozone  | Instant    | μg/m³         | Atmospheric gases close to surface (10 meter above ground)                  |
| carbon_dioxide                                          | Instant    | ppm           | CO2 close to surface (10 meter above ground)                                |
| ammonia                                                 | Instant    | μg/m³         | Ammonia concentration. Only available for Europe.                           |
| aerosol_optical_depth                                   | Instant    | Dimensionless | Aerosol optical depth at 550 nm of the entire atmosphere to indicate haze.  |
| methane                                                 | Instant    | μg/m³         | Methane close to surface (10 meter above ground)                            |
| dust                                                    | Instant    | μg/m³         | Saharan dust particles close to surface level (10 meter above ground).      |
| uv_index uv_index_clear_sky                             | Instant    | Index         | UV index considering clouds and clear sky. See                              |

|

birch_pollen

grass_pollen

mugwort_pollen

olive_pollen

ragweed_pollen

european_aqi_pm2_5

european_aqi_pm10

european_aqi_nitrogen_dioxide

european_aqi_ozone

european_aqi_sulphur_dioxide

us_aqi_pm2_5

us_aqi_pm10

us_aqi_nitrogen_dioxide

us_aqi_ozone

us_aqi_sulphur_dioxide

us_aqi_carbon_monoxide

### JSON Return Object

On success a JSON object will be returned.

` ````
"latitude": 52.52,
"longitude": 13.419,
"elevation": 44.812,
"generationtime_ms": 2.2119,
"utc_offset_seconds": 0,
"timezone": "Europe/Berlin",
"timezone_abbreviation": "CEST",
"hourly": {
"time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
"pm10": [1, 1.7, 1.7, 1.5, 1.5, 1.8, 2.0, 1.9, 1.3, ...]
},
"hourly_units": {
"pm10": "μg/m³"
},

`````


| Parameter | Format | Description |
|---|---|---|
| latitude, longitude | Floating point | |
| generationtime_ms | Floating point | |
| utc_offset_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezone timezone_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| hourly | Object | |
| hourly_units | Object | For each selected weather variable, the unit will be listed here. |

### Errors

` ````
"error": true,
"reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"
`````
