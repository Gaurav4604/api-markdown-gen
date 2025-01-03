---
api-endpoint: https://api.open-meteo.com/v1/ecmwf
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: ECMWF Weather Forecast API
url: https://open-meteo.com/en/docs/ecmwf-api
---

[generic weather forecast API](https://open-meteo.com/en/docs), which combines weather models up to 1 km resolution seamlessly.

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
"models": "ecmwf_ifs025"
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

This API uses [open-data ECMWF Integrated Forecast System IFS](https://www.ecmwf.int/en/forecasts/datasets/open-data). ECMWF IFS models run every 6 hours at 9 km resolution, but only 0.25° grid spacing (~25 km) is
available as open data with a limited number of weather variables at 3-hourly intervals.

AIFS is an artificial intelligence weather model from ECMWF yielding better results as GraphCast and other models. Unfortunately, only 6-hourly time-steps are available. You can find more information about AIFS [here](https://www.ecmwf.int/en/about/media-centre/aifs-blog). As soon as ECWMF includes additional data, they will be made available in this API.

For hourly and high-resolution data (up to 1 km) try our [forecast API](https://open-meteo.com/en/docs) which
combines multiple models.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Forecast Length | Update frequency |
|---|---|---|---|---|---|
|

[IFS](https://www.ecmwf.int/en/forecasts/datasets/open-data)

[AIFS](https://www.ecmwf.int/en/forecasts/datasets/open-data)

## API Documentation

The API endpoint /v1/ecmwf accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 10 days. Time always starts at 0:00 today. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | ||
| elevation | Floating point | No | The elevation used for statistical downscaling. Per default, a
|

end_date

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as and average or sum.

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour |
| snowfall | Preceding hour sum | cm (inch) | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent. Snowfall amount is not provided by ECMWF directly, instead it is approximated based on total precipitation and temperature |
| precipitation_type | Instantaneous | mm (inch) | 0 = No precipitation, 1 = Rain, 3 = Freezing rain (i.e. supercooled raindrops which freeze on contact with the ground and other surfaces), 5 = Snow, 6 = Wet snow (i.e. snow particles which are starting to melt), 7 = Mixture of rain and snow, 8 = Ice pellets, 12 = Freezing drizzle (i.e. supercooled drizzle which freezes on contact with the ground and other surfaces) |
| runoff | Preceding hour sum | mm (inch) | Execess rain that is not absorbed by the soil |
| weather_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. Weather code is calculated from cloud cover analysis, precipitation and snowfall. As ECMWF IFS has barely no information about atmospheric stability, estimation about thunderstorms is not possible. |
| cloud_cover | Instant | % | Total cloud cover as an area fraction. Calculated as a weighted function from low, mid and high level clouds. |
| cloud_cover_low | Instant | % | Low level clouds and fog up to 3 km altitude. In case of ECMWF IFS it is based on relative humidity on pressure levels 1000, 925 and 850 hPa. |
| cloud_cover_mid | Instant | % | Mid level clouds from 3 to 8 km altitude. In case of ECMWF IFS it is based on relative humidity on pressure levels 700 and 500 hPa. |
| cloud_cover_high | Instant | % | High level clouds from 8 km altitude. In case of ECMWF IFS it is based on relative humidity on pressure levels 300, 250 and 200 hPa. |
| pressure_msl surface_pressure | Instant | hPa | Atmospheric air pressure reduced to sea level (Mean sea level) and actual pressure at surface level |
| surface_temperature | Instant | °C (°F) | Temperature of the the surface. Depending on the type of surface (e.g. concrete) this temperature can be significantly higher then the 2 meter air temperature |
| soil_temperature_0_7cm soil_temperature_7_to_28cm soil_temperature_28_to_100cm soil_temperature_100_to_255cm | Instant | °C (°F) | Average temperature of different soil depths below ground. |
| soil_moisture_0_to_7cm soil_moisture_7_to_28cm soil_moisture_28_to_100cm soil_moisture_100_to_255cm | Instant | m³/m³ | Average soil water content as volumetric mixing ratio at 0-7, 7-28, 28-100 and 100-255 cm depths. |
| total_column_integrated_water_vapour | Instant | kg/m² | Total amount of water in the atmosphere. |
| temperature_2m temperature_1000hPa, ... | Instant | °C (°F) | Air temperature 2 meter above ground. Additional temperature in the atmopshere are given on different pressure levels. |
| temperature_2m_min temperature_2m_max | Preceding 3-hour | °C (°F) | Minimum and maximum temperature of the preceding 3 hours. |
| geopotential_height_1000hPa | Instant | meter | Geopotential height on different atmospheric pressure levels |
| wind_speed_10m wind_speed_1000hPa, ... | Instant | km/h (mph, m/s, knots) | Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level. Additional wind speeds are given on atmospheric pressure levels. |
| wind_direction_10m wind_direction_1000hPa, ... | Instant | ° | Wind direction at 10 meters above ground and different pressure levels. |
| wind_gusts_10m | Preceding 3-hour max | km/h (mph, m/s, knots) | Maximum 3 second wind at 10 m height above ground as a maximum of the preceding 3 hours |
| relative_humidity_1000hPa, ... | Instant | % | Relative humidity at atmospheric pressure levels. Unfortunately, 2 meter relative humidity is unavailable. |
| cloud_cover_1000hPa, ... | Instant | % | Cloud cover at the specified pressure level. Cloud cover is approximated based on
relative humidity using
|

direct_normal_irradiance

[Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf)[Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf)### JSON Return Object

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


## Weather variable documentation

### WMO Weather interpretation codes (WW)

| Code | Description |
|---|---|
| 0 | Clear sky |
| 1, 2, 3 | Mainly clear, partly cloudy, and overcast |
| 45, 48 | Fog and depositing rime fog |
| 51, 53, 55 | Drizzle: Light, moderate, and dense intensity |
| 56, 57 | Freezing Drizzle: Light and dense intensity |
| 61, 63, 65 | Rain: Slight, moderate and heavy intensity |
| 66, 67 | Freezing Rain: Light and heavy intensity |
| 71, 73, 75 | Snow fall: Slight, moderate, and heavy intensity |
| 77 * | Snow grains |
| 80, 81, 82 * | Rain showers: Slight, moderate, and violent |
| 85, 86 * | Snow showers slight and heavy |
| 95 * | Thunderstorm: Slight or moderate |
| 96, 99 * | Thunderstorm with slight and heavy hail |

(*) Showers and thunderstorm forecast not available with ECMWF IFS

This service is based on data and products of the European Centre for Medium-Range Weather Forecasts (ECMWF). Source www.ecmwf.int. ECMWF does not accept any liability whatsoever for any error or omission in the data, their availability, or for any loss or damage arising from their use.