---
api-endpoint: https://marine-api.open-meteo.com/v1/marine
date: 2024-01-01
description: Marine Weather API with ocean wave forecasts. Free access for non-commercial
  use. Access detailed ocean wave forecasts generated by local and global models.
  Stay informed about wave conditions and make well-informed decisions for your marine
  activities. Enhance safety and optimize your maritime operations with accurate and
  reliable marine weather data.
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Marine Weather API
url: https://open-meteo.com/en/docs/marine-weather-api
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
url = "https://marine-api.open-meteo.com/v1/marine"
params = {
"latitude": 54.544587,
"longitude": 10.227487,
"hourly": "wave_height"
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
hourly_wave_height = hourly.Variables(0).ValuesAsNumpy()
hourly_data = {"date": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}
hourly_data["wave_height"] = hourly_wave_height
hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
```


## Data Sources

The Marine API combines wave models from different sources.

| Data Set | Region | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency | |
|---|---|---|---|---|---|---|
|

[Map](https://data.marine.copernicus.eu/viewer/expert?view=viewer&crs=epsg%3A4326&z=0¢er=-23.399717243797422%2C42.59188729714914&zoom=10.52284658362573&layers=W3sib3BhY2l0eSI6MSwiaWQiOiJ0ZW1wMSIsImxheWVySWQiOiJHTE9CQUxfQU5BTFlTSVNGT1JFQ0FTVF9XQVZfMDAxXzAyNy9jbWVtc19tb2RfZ2xvX3dhdl9hbmZjXzAuMDgzZGVnX1BUM0gtaV8yMDIzMTEvVkhNMCIsInpJbmRleCI6MCwiaXNFeHBsb3JpbmciOnRydWUsImxvZ1NjYWxlIjpmYWxzZX1d&basemap=dark)[MeteoFrance SMOC Currents](https://data.marine.copernicus.eu/product/GLOBAL_ANALYSISFORECAST_PHY_001_024/services)

[Map](https://data.marine.copernicus.eu/viewer/expert?view=viewer&crs=epsg%3A4326&z=-0.49402499198913574¢er=-12.433872193277338%2C42.88370285999325&zoom=11.872305323411199&layers=W3sib3BhY2l0eSI6MSwiaWQiOiJ0ZW1wMSIsImxheWVySWQiOiJHTE9CQUxfQU5BTFlTSVNGT1JFQ0FTVF9QSFlfMDAxXzAyNC9jbWVtc19tb2RfZ2xvX3BoeV9hbmZjX21lcmdlZC11dl9QVDFILWlfMjAyMjExL3VvIiwiekluZGV4IjowLCJpc0V4cGxvcmluZyI6dHJ1ZSwibG9nU2NhbGUiOmZhbHNlfV0%3D&basemap=dark)[ECMWF WAM](https://www.ecmwf.int/en/elibrary/79883-wave-model)

[NCEP GFS Wave](https://polar.ncep.noaa.gov/waves/index.php)

[NCEP GFS Wave](https://polar.ncep.noaa.gov/waves/index.php)

[DWD GWAM](https://www.dwd.de/EN/specialusers/shipping/seegangsvorhersagesystem_en.html)

[DWD EWAM](https://www.dwd.de/EN/specialusers/shipping/seegangsvorhersagesystem_en.html)

[ERA5-Ocean](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

## API Documentation

The API endpoint /v1/marine accepts a geographical coordinate, a list of marine variables and responds with a JSON hourly marine weather forecast for 7 days. Time always starts at 0:00 today. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | ||
| hourly | String array | No | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. | |
| daily | String array | No | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required. | |
| current | String array | No | A list of variables to get current conditions. | |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc_offset_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is
returned starting at 00:00 local-time. Any time zone name from the
|

past_hours

end_date

end_hour

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| wave_height wind_wave_height swell_wave_height | Instant | Meter | Wave height of significant mean, wind and swell waves. Wave directions are always reported as the direction the waves come from. 0° = From north towards south; 90° = From east |
| wave_direction wind_wave_direction swell_wave_direction | Instant | ° | Mean direction of mean, wind and swell waves |
| wave_period wind_wave_period swell_wave_period | Instant | Seconds | Period between mean, wind and swell waves. |
| wind_wave_peak_period swell_wave_peak_period | Instant | Seconds | Peak period between wind and swell waves. |
| ocean_current_velocity | Instant | km/h (mph, m/s, knots) | Velocity of ocean current considering Eulerian, Waves and Tides. |
| ocean_current_direction | Instant | ° | Direction following the flow of the current. E.g. where the current is heading towards. 0° = Going north; 90° = Towards east. |

### Daily Parameter Definition

| Variable | Unit | Description |
|---|---|---|
| wave_height_max wind_wave_height_max swell_wave_height_max | Meter | Maximum wave height on a given day for mean, wind and swell waves |
| wave_direction_dominant wind_wave_direction_dominant swell_wave_direction_dominant | ° | Dominant wave direction of mean, wind and swell waves |
| wave_period_max wind_wave_period_max swell_wave_period_max | Seconds | Maximum wave period of mean, wind and swell |
| wind_wave_peak_period_max swell_wave_peak_period_max | Seconds | Maximum peak period between wind and swell waves. |

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
"wave_height": [1, 1.7, 1.7, 1.5, 1.5, 1.8, 2.0, 1.9, 1.3, ...]
},
"hourly_units": {
"wave_height": "m"
},
```


| Parameter | Format | Description |
|---|---|---|
| latitude, longitude | Floating point | |
| generationtime_ms | Floating point | |
| utc_offset_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezone timezone_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| hourly | Object | |
| hourly_units | Object | For each selected weather variable, the unit will be listed here. |
| daily | Object | |
| daily_units | Object | For each selected daily weather variable, the unit will be listed here. |

### Errors

` ````
"error": true,
"reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"
```


## Citation & Acknowledgement

Generated using ICON Wave forecast from the [German Weather Service DWD](https://www.dwd.de/EN/service/copyright/copyright_node.html).

All users of Open-Meteo data must provide a clear attribution to DWD as well as a reference to Open-Meteo.