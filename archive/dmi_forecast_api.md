---
api-endpoint: https://api.open-meteo.com/v1/dmi
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: DMI Forecast API
url: https://open-meteo.com/en/docs/dmi-api
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
url = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 52.52,
"longitude": 13.41,
"hourly": "temperature_2m",
"models": "dmi_seamless"
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

DMI provides weather forecasts from the HARMONIE AROME model with ECMWF IFS initialization. This
is a collaboration of multiple European national weather services under the name "United Weather
Centres-West" (UWC-West). Forecasts for Europe use 2 km resolution and provide a large range of
weather variables. All data is updated every 3 hours and provides forecast for up to 2.5 days.
After 2.5 days, Open-Meteo combines forecasts with the [ECMWF IFS 0.25° model](https://open-meteo.com/en/docs/ecmwf-api) to provide up to 10 days of forecast.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Forecast Length | Update frequency |
|---|---|---|---|---|---|
|

## API Documentation

For a detailed list of all available weather variables please refer to the general [Weather Forecast API](https://open-meteo.com/en/docs). Only notable remarks are listed below

**Direct Solar Radiation:**DMI provides direct solar radiation. Many other weather models only provide global solar radiation and direct solar radiation must be calculated user separation models.**Direct Normalized Irradiance (DNI):**Although DNI is available, it has not been integrated. Open-Meteo uses solar position algorithms which calculate DNI from direct radiation with (almost) the same results.**Wind Direction Correction:**Wind direction has been calculated from U/V wind component vectors. Special care has been taken to correct for the Lambert Conformal Conic projection. Without this correction, wind directions have an error of up to 15°.**Cloud Cover (2m):**DMI provides cloud cover at 2 metre abouve ground which can be interpreted as fog. This is remarkable, because only very weather models are capable of modeling low level cloud cover and fog with a good degree of accuracy.