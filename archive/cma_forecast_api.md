---
api-endpoint: https://api.open-meteo.com/v1/cma
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: CMA Forecast API
url: https://open-meteo.com/en/docs/cma-api
---

[Weather Forecast API](https://open-meteo.com/en/docs), which utilizes multiple local weather models for forecasts extending up to 16 days.

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
url = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 52.52,
"longitude": 13.41,
"hourly": "temperature_2m",
"models": "cma_grapes_global"
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
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_data = {"date": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
```


## Data Source

The API relies on the Global/Regional Assimilation and Prediction Enhanced System (GFS GRAPES), independently developed by the China Meteorological Administration (CMA). It provides data in 3-hour intervals, offering forecasts for up to 10 days. The model runs four times daily at 0:00, 6:00, 12:00, and 18:00 UTC.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Forecast Length | Update frequency |
|---|---|---|---|---|---|
|

## API Documentation

The API endpoint /v1/cma accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days. Time always starts at 0:00 today and contains 168 hours. If &forecast_days=16 is set, up to 10 days of forecast can be returned. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | ||
| elevation | Floating point | No | The elevation used for statistical downscaling. Per default, a
|

[time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.past_hours

end_date

end_hour

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| temperature_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative_humidity_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew_point_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent_temperature | Instant | °C (°F) | |
| pressure_msl surface_pressure | Instant | hPa | |
| cloud_cover | Instant | % | Total cloud cover as an area fraction |
| cloud_cover_low | Instant | % | Low level clouds and fog up to 3 km altitude |
| cloud_cover_mid | Instant | % | Mid level clouds from 3 to 8 km altitude |
| cloud_cover_high | Instant | % | High level clouds from 8 km altitude |
| wind_speed_10m wind_speed_30m wind_speed_50m wind_speed_70m wind_speed_100m wind_speed_120m wind_speed_140m wind_speed_160m wind_speed_180m wind_speed_200m | Instant | km/h (mph, m/s, knots) | Wind speed at 10, 30, 50, 70, 100, 120, 140, 160, 180 or 200 meters above ground. Wind speed on 10 meters is the standard level. |
| wind_direction_10m wind_direction_30m wind_direction_50m wind_direction_70m wind_direction_100m wind_direction_120m wind_direction_140m wind_direction_160m wind_direction_180m wind_direction_200m | Instant | ° | Wind direction at 10, 30, 50, 70, 100, 120, 140, 160, 180 or 200 meters above ground |
| wind_gusts_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave_radiation | Preceding hour mean | W/m² | |
| direct_radiation direct_normal_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the
normal plane (perpendicular to the sun). GRAPES does bot offers direct radiation
directly. It is approximated based on
|

[Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf)[FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm)ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.[Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy).[Wikipedia](https://en.wikipedia.org/wiki/Lifted_index).soil_temperature_10_to_40cm

soil_temperature_40_to_100cm

soil_temperature_100_to_200cm

soil_moisture_10_to_40cm

soil_moisture_40_to_100cm

soil_moisture_100_to_200cm

### Pressure Level Variables

| Level (hPa) | 1000 | 975 | 950 | 925 | 900 | 850 | 800 | 750 | 700 | 650 | 600 | 550 | 500 | 450 | 400 | 350 | 300 | 275 | 250 | 225 | 200 | 175 | 150 | 125 | 100 | 70 | 50 | 30 | 20 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Altitude | 110 m | 320 m | 500 m | 800 m | 1000 m | 1500 m | 1900 m | 2.5 km | 3 km | 3.6 km | 4.2 km | 4.9 km | 5.6 km | 6.3 km | 7.2 km | 8.1 km | 9.2 km | 9.7 km | 10.4 km | 11 km | 11.8 km | 12.6 km | 13.5 km | 14.6 km | 15.8 km | 17.7 km | 19.3 km | 22 km | 23 km | 26 km |

All pressure level have valid times of the indicated hour (instant).

| Variable | Unit | Description |
|---|---|---|
| weather_code | WMO code | The most severe weather condition on a given day |
| temperature_1000hPa temperature_975hPa, ... | °C (°F) | Air temperature at the specified pressure level. Air temperatures decrease linearly with pressure. |
| relative_humidity_1000hPa relative_humidity_975hPa, ... | % | Relative humidity at the specified pressure level. |
| dew_point_1000hPa dew_point_975hPa, ... | °C (°F) | Dew point temperature at the specified pressure level. |
| cloud_cover_1000hPa cloud_cover_975hPa, ... | % | Cloud cover at the specified pressure level. |
| wind_speed_1000hPa wind_speed_975hPa, ... | km/h (mph, m/s, knots) | Wind speed at the specified pressure level. |
| wind_direction_1000hPa wind_direction_975hPa, ... | ° | Wind direction at the specified pressure level. |
| geopotential_height_1000hPa geopotential_height_975hPa, ... | meter | Geopotential height at the specified pressure level. This can be used to get the correct altitude in meter above sea level of each pressure level. Be carefull not to mistake it with altitude above ground. |

### Daily Parameter Definition

| Variable | Unit | Description |
|---|---|---|
| temperature_2m_max temperature_2m_min | °C (°F) | Maximum and minimum daily air temperature at 2 meters above ground |
| apparent_temperature_max apparent_temperature_min | °C (°F) | Maximum and minimum daily apparent temperature |
| precipitation_sum | mm | Sum of daily precipitation (including rain, showers and snowfall) |
| snowfall_sum | cm | Sum of daily snowfall |
| precipitation_hours | hours | The number of hours with rain |
| sunrise sunset | iso8601 | Sun rise and set times |
| sunshine_duration | seconds | |
| daylight_duration | seconds | Number of seconds of daylight per day |
| wind_speed_10m_max wind_gusts_10m_max | km/h (mph, m/s, knots) | Maximum wind speed and gusts on a day |
| wind_direction_10m_dominant | ° | Dominant wind direction |
| shortwave_radiation_sum | MJ/m² | The sum of solar radiation on a given day in Megajoules |
| et0_fao_evapotranspiration | mm | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field |

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
"temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...]
},
"hourly_units": {
"temperature_2m": "°C"
}
```


| Parameter | Format | Description |
|---|---|---|
| latitude, longitude | Floating point | |
| elevation | Floating point | |
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