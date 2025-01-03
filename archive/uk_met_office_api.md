---
api-endpoint: https://api.open-meteo.com/v1/forecast
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: UK Met Office API
url: https://open-meteo.com/en/docs/ukmo-api
---

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)license. Therefore, any derived products from this data should also be redistributed under the same or a compatible license. Typically, Open-Meteo provides data under

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en).

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
"latitude": 51.5085,
"longitude": -0.1257,
"hourly": "temperature_2m",
"models": "ukmo_seamless"
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

This API uses global UKMO Global 10 km weather forecasts and combines them with high-resolution
UKV 2 km model for the United Kingdom and Ireland. Information about UKMO weather models is
available [here](https://www.metoffice.gov.uk/services/data/external-data-channels). For UKMO Global, values are interpolated from 3-hourly to 1-hourly after 54 hours and from
6-hourly data after 144 hours.

Note: UKMO open-data has an additional delay of 4 hours. The forecast is therefore not as accurate as it could be.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Forecast Length | Update frequency |
|---|---|---|---|---|---|
| UKMO Global | Global | 0.09° (~10 km) | Hourly, 3-hourly after 54 hours, 6-hourly after 144 hours | 7 days | Every 6 hours |
| UKMO UKV | UK and Ireland | 2 km | Hourly | 2 days | Every hour |

## API Documentation

For a detailed list of all available weather variables please refer to the general [Weather Forecast API](https://open-meteo.com/en/docs). Only notable remarks are listed below

**Direct Solar Radiation:**UKMO provides direct solar radiation. Many other weather models only provide global solar radiation and direct solar radiation must be calculated user separation models.**Shortwave solar radiation:**The Global UKMO domain does not include solar shortwave radiation. Therefore diffuse and tilted radiation are not available as well.**Wind Forecasts at 100m and above:**Wind forecasts at different levels above ground are only available for the 2 km UKV model.**Cloud Cover (2m):**UKMO UKV 2 km provides cloud cover at 2 metre above ground which can be interpreted as fog. This is remarkable, because only very weather models are capable of modeling low level cloud cover and fog with a good degree of accuracy.