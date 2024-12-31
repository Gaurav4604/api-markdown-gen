---
api-endpoint: https://flood-api.open-meteo.com/v1/flood
date: 2024-01-01
description: Access ensemble flood forecasts estimating the volume of water discharged
  by rivers worldwide. Get invaluable information for predicting flood events and
  taking proactive measures for flood preparedness. Ensure safety and minimize the
  impact of floods with our reliable flood data.
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Global Flood API
url: https://open-meteo.com/en/docs/flood-api
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
url = "https://flood-api.open-meteo.com/v1/flood"
params = {
"latitude": 59.91,
"longitude": 10.75,
"daily": "river_discharge"
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
daily_river_discharge = daily.Variables(0).ValuesAsNumpy()
daily_data = {"date": pd.date_range(
start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = daily.Interval()),
inclusive = "left"
)}
daily_data["river_discharge"] = daily_river_discharge
daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)
```


## Data Source

This API uses reanalysis and forecast data from the [Global Flood Awareness System (GloFAS)](https://www.globalfloods.eu). Per default, GloFAS version 4 with seamless data from 1984 until 7 months of forecast is
used.

Please note: Due to the 5 km resolution the closest river might not be selected correctly. Varying coordiantes by 0.1° can help to get a more representable discharge rate. The GloFAS website provides additional maps to help understand how rivers are covered in this dataset.

| Weather Model | Region | Spatial Resolution | Temporal Resolution | Data Length | Update frequency |
|---|---|---|---|---|---|
|

[GloFAS v4 Forecast](https://cds.climate.copernicus.eu/datasets/cems-glofas-forecast?tab=overview)

[GloFAS v4 Seasonal Forecast](https://ewds.climate.copernicus.eu/datasets/cems-glofas-seasonal?tab=overview)

[GloFAS v3 Reanalysis](https://ewds.climate.copernicus.eu/datasets/cems-glofas-historical?tab=overview)

[GloFAS v3 Forecast](https://ewds.climate.copernicus.eu/datasets/cems-glofas-forecast?tab=overview)

[GloFAS v3 Seasonal Forecast](https://ewds.climate.copernicus.eu/datasets/cems-glofas-seasonal?tab=overview)

## API Documentation

The API endpoint /v1/flood accepts a geographical coordinate and returns river discharge data from the largest river in a 5 km area for the given coordinates. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | ||
| daily | String array | No | A list of weather variables which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. | |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0! |
| past_days | Integer | No | 0 | If past_days is set, past data can be returned. |
| forecast_days | Integer (0-210) | No | 92 | Per default, only 92 days are returned. Up to 210 days of forecast are possible. |
| start_date end_date | String (yyyy-mm-dd) | No | The time interval to get data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). Data are available from 1984-01-01 until 7 month forecast. | |
| ensemble | Boolean | No | If True all forecast ensemble members will be returned | |
| cell_selection | String | No | nearest | Set a preference how grid-cells are selected. The default land finds a
suitable grid-cell on land with
|

[pricing](https://open-meteo.com/en/pricing)for more information.### Daily Parameter Definition

The parameter &daily= accepts the following values:

| Variable | Unit | Description |
|---|---|---|
| river_discharge | m³/s | Daily river discharge rate in m³/s |
| river_discharge_mean river_discharge_median river_discharge_max river_discharge_min river_discharge_p25 river_discharge_p75 | m³/s | Statistical analysis from ensemble members for river discharge rate in m³/s. Only available for forecasts and not for consolidated historical data. |

### JSON Return Object

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
| daily | Object | |
| daily_units | Object | For each selected weather variable, the unit will be listed here. |

### Errors

` ````
"error": true,
"reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"
```