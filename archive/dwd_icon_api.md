---
api-endpoint: https://api.open-meteo.com/v1/dwd-icon
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: DWD ICON API
url: https://open-meteo.com/en/docs/dwd-api
---

[generic weather forecast API](https://open-meteo.com/en/docs)if no other high resolution weather models are available.

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
"models": "icon_seamless"
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

This API uses global DWD ICON weather forecast and combines them with high-resolution ICON
Europe and Central Europe forecasts. Information about DWD wearther models is available [here](https://www.dwd.de/EN/ourservices/nwp_forecast_data/nwp_forecast_data.html). For ICON Global and Europe, values are interpolated from 3-hourly to 1-hourly after 78 hours.
15-minutely data is only available for a small number of weather variables and only in Central
Europe.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Forecast Length | Update frequency |
|---|---|---|---|---|---|
| ICON Global | Global | 0.1° (~11 km) | Hourly, 3-hourly after 78 hours | 7.5 days | Every 6 hours |
| ICON Europe | Europe | 0.0625° (~7 km) | Hourly, 3-hourly after 78 hours | 5 days | Every 3 hours |
| ICON D2 | Central Europe | 0.02° (~2 km) | 15-Minutely | 2 days | Every 3 hours |

## API Documentation

The API endpoint /v1/dwd-icon accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days. Time always starts at 0:00 today and contains 168 hours. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location_id. | |
| elevation | Floating point | No | The elevation used for statistical downscaling. Per default, a
|

[time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.forecast_minutely_15

past_hours

past_minutely_15

end_date

end_hour

start_minutely_15

end_minutely_15

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.Additional optional URL parameters will be added. For API stability, no required parameters will be added in the future!

### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as an average or sum.

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| temperature_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative_humidity_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew_point_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent_temperature | Instant | °C (°F) | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation |
| pressure_msl surface_pressure | Instant | hPa | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation. |
| cloud_cover | Instant | % | Total cloud cover as an area fraction |
| cloud_cover_low | Instant | % | Low level clouds and fog up to 3 km altitude |
| cloud_cover_mid | Instant | % | Mid level clouds from 3 to 8 km altitude |
| cloud_cover_high | Instant | % | High level clouds from 8 km altitude |
| wind_speed_10m wind_speed_80m wind_speed_120m wind_speed_180m | Instant | km/h (mph, m/s, knots) | Wind speed at 10, 80, 120 or 180 meters above ground. Wind speed on 10 meters is the standard level. |
| wind_direction_10m wind_direction_80m wind_direction_120m wind_direction_180m | Instant | ° | Wind direction at 10, 80, 120 or 180 meters above ground |
| wind_gusts_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave_radiation | Preceding hour mean | W/m² | Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation |
| direct_radiation direct_normal_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun) |
| diffuse_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour |
| global_tilted_irradiance | Preceding hour mean | W/m² | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west). If azimuth is set to "nan", the calculation assumes a horizontal tracker. If tilt is set to "nan", it is assumed that the panel has a vertical tracker. If both are set to "nan", a bi-axial tracker is assumed. |
| sunshine_duration | Preceding hour sum | Seconds | Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition. |
| vapour_pressure_deficit | Instant | kPa | Vapor Pressure Deificit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases |
| lightning_potential | Instant | J/kg | The Lightning Potential Index after
|

[FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm)ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.soil_temperature_6cm

soil_temperature_18cm

soil_temperature_54cm

soil_moisture_1_to_3cm

soil_moisture_3_to_9cm

soil_moisture_9_to_27cm

soil_moisture_27_to_81cm

[Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy).### 15-Minutely Parameter Definition

The parameter &minutely_15= can be used to get 15-minutely data. This data is based on the ICON-D2 model which is only available in Central Europe. If 15-minutely data is requested for locations outside Central Europe, data is interpolated from 1-hourly to 15-minutely.

15-minutely data can be requested for other weather variables that are available for hourly data, but will use interpolation.

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| shortwave_radiation | Preceding 15 minutes mean | W/m² | Shortwave solar radiation as average of the preceding 15 minutes. This is equal to the total global horizontal irradiation |
| direct_radiation direct_normal_irradiance | Preceding 15 minutes mean | W/m² | Direct solar radiation as average of the preceding 15 minutes on the horizontal plane and the normal plane (perpendicular to the sun) |
| diffuse_radiation | Preceding 15 minutes mean | W/m² | Diffuse solar radiation as average of the preceding 15 minutes |
| global_tilted_irradiance | Preceding 15 minutes mean | W/m² | Total radiation received on a tilted pane as average of the 15 minutes. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west). If azimuth is set to "nan", the calculation assumes a horizontal tracker. If tilt is set to "nan", it is assumed that the panel has a vertical tracker. If both are set to "nan", a bi-axial tracker is assumed. |
| sunshine_duration | Preceding 15 minutes sum | Seconds | Number of seconds of sunshine of the preceding 15-minutes per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition. |
| lightning_potential | Instant | J/kg | The Lightning Potential Index after
|

[Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy).### Pressure Level Variables

Pressure level variables do not have fixed altitudes. Altitude varies with atmospheric pressure. 1000 hPa is roughly between 60 and 160 meters above sea level. Estimated altitudes are given below. Altitudes are in meters above sea level (not above ground). For precise altitudes, geopotential_height can be used.

| Level (hPa) | 1000 | 975 | 950 | 925 | 900 | 850 | 800 | 700 | 600 | 500 | 400 | 300 | 250 | 200 | 150 | 100 | 70 | 50 | 30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Altitude | 110 m | 320 m | 500 m | 800 m | 1000 m | 1500 m | 1900 m | 3 km | 4.2 km | 5.6 km | 7.2 km | 9.2 km | 10.4 km | 11.8 km | 13.5 km | 15.8 km | 17.7 km | 19.3 km | 22 km |

All pressure level have valid times of the indicated hour (instant).

| Variable | Unit | Description |
|---|---|---|
| temperature_1000hPa temperature_975hPa, ... | °C (°F) | Air temperature at the specified pressure level. Air temperatures decrease linearly with pressure. |
| relative_humidity_1000hPa relative_humidity_975hPa, ... | % | Relative humidity at the specified pressure level. |
| dew_point_1000hPa dew_point_975hPa, ... | °C (°F) | Dew point temperature at the specified pressure level. |
| cloud_cover_1000hPa cloud_cover_975hPa, ... | % | Cloud cover at the specified pressure level. Cloud cover is approximated based on
relative humidity using
|

wind_speed_975hPa, ...

wind_direction_975hPa, ...

geopotential_height_975hPa, ...

### Daily Parameter Definition

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

| Variable | Unit | Description |
|---|---|---|
| temperature_2m_max temperature_2m_min | °C (°F) | Maximum and minimum daily air temperature at 2 meters above ground |
| apparent_temperature_max apparent_temperature_min | °C (°F) | Maximum and minimum daily apparent temperature |
| precipitation_sum | mm | Sum of daily precipitation (including rain, showers and snowfall) |
| rain_sum | mm | Sum of daily rain |
| showers_sum | mm | Sum of daily showers |
| snowfall_sum | cm | Sum of daily snowfall |
| precipitation_hours | hours | The number of hours with rain |
| weather_code | WMO code | The most severe weather condition on a given day |
| sunrise sunset | iso8601 | Sun rise and set times |
| sunshine_duration | seconds | The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk. |
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
| latitude, longitude | Floating point | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometers away from the requested coordinate. |
| elevation | Floating point | The elevation from a 90 meter digital elevation model. This effects which grid-cell is selected (see parameter cell_selection). Statistical downscaling is used to adapt weather conditions for this elevation. This elevation can also be controlled with the query parameter elevation. If &elevation=nan is specified, all downscaling is disabled and the averge grid-cell elevation is used. |
| generationtime_ms | Floating point | Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements. |
| utc_offset_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezone timezone_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| hourly | Object | For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| hourly_units | Object | For each selected weather variable, the unit will be listed here. |
| daily | Object | For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| daily_units | Object | For each selected daily weather variable, the unit will be listed here. |

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error object is returned with a HTTP 400 status code.

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
| 77 | Snow grains |
| 80, 81, 82 | Rain showers: Slight, moderate, and violent |
| 85, 86 | Snow showers slight and heavy |
| 95 * | Thunderstorm: Slight or moderate |
| 96, 99 * | Thunderstorm with slight and heavy hail |

(*) Thunderstorm forecast with hail is only available in Central Europe