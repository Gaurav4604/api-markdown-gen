---
api-endpoint: https://api.open-meteo.com/v1/metno
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: MET Norway API
url: https://open-meteo.com/en/docs/metno-api
---

[generic Weather Forecast API](https://open-meteo.com/en/docs)transparently combines MET Nordic with other weather models to take advantage of hourly updates.

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
"latitude": 59.91,
"longitude": 10.75,
"hourly": "temperature_2m",
"models": "metno_seamless"
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

This API uses local weather models from the Norwegian Meteorological Institute. The [MET Nordic](https://github.com/metno/NWPdocs/wiki/MET-Nordic-dataset) dataset is derived from the 2.5 km MetCoOp ensemble model with ECMWF initialization. With post-processing
based on measurement & radar and with updates every hour, the short-term forecast performance skill
should be high.

Unfortunately, only 2.5 days of forecast are available. The Open-Meteo [weather forecast API](https://open-meteo.com/en/docs) automatically uses MET Nordic in combination with larger scale models to offer a 7 days forecast.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Forecast Length | Update frequency |
|---|---|---|---|---|---|
|

## API Documentation

The API endpoint /v1/metno accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 2.5 days. Time always starts at 0:00 today. Data is only available in the Scandinavian region. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | ||
| elevation | Floating point | No | The elevation used for statistical downscaling. Per default, a
|

[time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.past_hours

end_date

end_hour

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as and average or sum.

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour |
| pressure_msl surface_pressure | Instant | hPa | Atmospheric air pressure reduced to sea level (Mean sea level) and actual pressure at surface level |
| temperature_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative_humidity_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew_point_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent_temperature | Instant | °C (°F) | |
| cloud_cover | Instant | % | Total cloud cover as an area fraction |
| wind_speed_10m | Instant | km/h (mph, m/s, knots) | Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level.. |
| wind_direction_10m | Instant | ° | Wind direction at 10 meters above ground. |
| wind_gusts_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave_radiation | Preceding hour mean | W/m² | |
| direct_radiation direct_normal_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun) |
| diffuse_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour. MET Nordic does not offers
diffuse and direct radiation directly. It is approximated based on
|

[FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm)ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.### JSON Return Object

On success a JSON object will be returned.

` ````
"latitude": 52.52,
"longitude": 13.419,
"generationtime_ms": 2.2119,
"timezone": "Europe/Berlin",
"timezone_abbreviation": "CEST",
"hourly": {
"time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
"temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...]
},
"hourly_units": {
"temperature_2m": "°C"
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

### Errors

` ````
"error": true,
"reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"
```