---
api-endpoint: https://historical-forecast-api.open-meteo.com/v1/forecast
date: 2024-12-16
description: Access accurate and comprehensive historical weather data with Open-Meteo's
  API. Explore global weather trends, analyze climate change, and optimize forecasts
  using reanalysis models and high-resolution weather data. Visit our documentation
  for detailed variables and parameters.
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Historical Forecast API
url: https://open-meteo.com/en/docs/historical-forecast-api
---

[Weather Forecast API](https://open-meteo.com/en/docs). The data is continuously archived and updated daily. For more information read the

[announcement blog article](https://openmeteo.substack.com/p/introducing-the-historical-forecast).

## API Response

The sample code automatically applies all the parameters selected above. It includes caching and the conversion to Pandas DataFrames.
The use of DataFrames is entirely optional. You can find further details and examples in the [Python API client](https://pypi.org/project/openmeteo-requests/) documentation.

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
url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
params = {
"latitude": 52.52,
"longitude": 13.41,
"start_date": "2024-12-16",
"end_date": "2024-12-29",
"hourly": "temperature_2m"
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

The weather data precisely aligns with the weather forecast API, created by continuously integrating weather forecast model data. Each update from the weather models' initial hours is compiled into a seamless time series. This extensive dataset is ideal for training machine learning models and combining them with forecast data to generate optimized predictions.

Weather models are initialized using data from weather stations, satellites, radar, airplanes, soundings, and buoys. With high update frequencies of 1, 3, or 6 hours, the resulting time series is nearly as accurate as direct measurements and offers global coverage. In regions like North America and Central Europe, the difference from local weather stations is minimal. However, for precise values such as precipitation, local measurements are preferable when available.

The Historical Forecast API archives comprehensive data, including atmospheric pressure levels, from all accessible weather forecast models. Depending on the model and public archive availability, data is available starting from 2021 or 2022.

The default Best Match option selects the most suitable high-resolution weather models for any global location, though users can also manually specify the weather model. Open-Meteo utilizes the following weather forecast models:

| National Weather Provider | Weather Model | Region | Spatial Resolution | Temporal Resolution | Update Frequency | Available Since |
|---|---|---|---|---|---|---|
| Deutscher Wetterdienst (DWD) | ICON | Global | 0.1° (~11 km) | 1-Hourly | Every 6 hours | 2022-11-24 |
| ICON-EU | Europe | 0.0625° (~7 km) | 1-Hourly | Every 3 hours | 2022-11-24 | |
| ICON-D2 | Central Europe | 0.02° (~2 km) | 1-Hourly | Every 3 hours | 2022-11-24 | |
| NOAA NCEP | GFS | Global | 0.11° (~13 km) | 1-Hourly | Every 6 hours | 2021-03-23 |
| GFS Pressure Variables | Global | 0.25° (~25 km) | 1-Hourly | Every 6 hours | 2021-03-23 | |
| HRRR | U.S. Conus | 3 km | 1-Hourly | Every hour | 2018-01-01 | |
| NBM | U.S. Conus | 3 km | 1-Hourly | Every hour | 2024-10-08 | |
| GFS GraphCast | Global | 0.25° (~25 km) | 6-Hourly | Every 6 hours | 2024-02-05 | |
| Météo-France | ARPEGE World | Global | 0.25° (~25 km) | 1-Hourly | Every 6 hours | 2024-01-02 |
| ARPEGE Europe | Europe | 0.1° (~11 km) | 1-Hourly | Every 6 hours | 2022-11-13 | |
| AROME France | Global | 0.025° (~2.5 km) | 1-Hourly | Every 3 hours | 2024-01-02 | |
| AROME France HD | Global | 0.01° (~1.5 km) | 1-Hourly | Every 3 hours | 2022-11-13 | |
| ECMWF | IFS 0.4° | Global | 0.4° (~44 km) | 3-Hourly | Every 6 hours | 2022-11-07 |
| IFS 0.25° | Global | 0.25° (~25 km) | 3-Hourly | Every 6 hours | 2024-02-03 | |
| AIFS 0.25° | Global | 0.25° (~25 km) | 6-Hourly | Every 6 hours | 2024-03-13 | |
| UK Met Office | UKMO Global | Global | 0.09° (~10 km) | Hourly | Every 6 hours | 2022-03-01 |
| UKMO UKV | UK and Ireland | 2 km | Hourly | Every hour | 2022-03-01 | |
| JMA | GSM | Global | 0.5° (~55 km) | 6-Hourly | Every 6 hours | 2016-01-01 |
| MSM | Japan | 0.05° (~5 km) | 1-Hourly | Every 3 hours | 2016-01-01 | |
| MET Norway | MET Nordic | Norway, Denmark, Sweden, Finland | 1 km | 1-Hourly | Every hour | 2022-11-15 |
| Canadian Weather Service | GEM Global | Global | 0.15° (~15 km) | 3-Hourly | Every 12 hours | 2022-11-23 |
| GEM Regional | North America, North Pole | 10 km | 1-Hourly | Every 6 hours | 2022-11-23 | |
| HRDPS Continental | Canada, Nothern US | 2.5 km | 1-Hourly | Every 6 hours | 2023-03-03 | |
| China Meteorological Administration (CMA) | GFS GRAPES | Global | 0.125° (~15 km) | 3-hourly | Every 6 hours | 2023-12-31 |
| Australian Bureau of Meteorology (BOM) | ACCESS-G | Global | 0.15° (~15 km) | 1-Hourly | Every 6 hours | 2024-01-18 |
| COSMO 2I & 5M AM ARPAE ARPAP Italy | COSMO 5M | Europe | 5 km | 1-Hourly | Every 12 hours | 2024-02-01 |
| COSMO 2I | Italy | 2.2 km | 1-Hourly | Every 12 hours | 2024-02-01 | |
| COSMO 2I RUC | Italy | 2.2 km | 1-Hourly | Every 3 hours | 2024-02-01 | |
| DMI | HARMONIE AROME DINI | Central & Northern Europe | 2 km | 1-Hourly | Every 3 hours | 2024-07-01 |
| KNMI | HARMONIE AROME Netherlands | Netherlands, Belgium | 2 km | 1-Hourly | Every hour | 2024-07-01 |
| HARMONIE AROME Europe | Central & Northern Europe up to Iceland | 5.5 km | 1-Hourly | Every hour | 2024-07-01 |

## Which Historical Weather Data to Use?

Open-Meteo provides various datasets for historical weather data: the Historical Weather API and the Historical Forecast API. For novice users expecting a single, definitive source of weather data, this can be confusing. In reality, only a small fraction of the Earth's surface is covered by weather stations with accurate and consistent measurements. To address this gap, numerical weather models are used to approximate past global weather.

This dataset is based on reanalysis weather models, particularly ERA5. It offers data from 1940 onwards with reasonable consistency throughout the time series, making it ideal for analyzing weather trends and climate change. The focus here is on consistency rather than pinpoint accuracy, with a spatial resolution ranging from 9 to 25 kilometers.[Historical Weather API:](https://open-meteo.com/en/docs/historical-weather-api)This dataset is constructed by continuously assembling weather forecasts, concatenating the first hours of each model update. Initialized with actual measurements, it closely mirrors local measurements but provides global coverage. However, it only includes data from the past 2-5 years and lacks long-term consistency due to evolving weather models and better initialization data over time.[Historical Forecast API:](https://open-meteo.com/en/docs/historical-forecast-api): Similar to the Historical Forecast API, this dataset archives high-resolution weather models but includes data with a lead time offset of 1, 2, 3, 4, or more days. This makes it ideal for analyzing forecast performance several days into the future. Due to the vast amount of data, only common weather variables are stored, with data processing beginning in early 2024.[Previous Runs API](https://open-meteo.com/en/docs/previous-runs-api)

#### Choosing the Right Dataset:

- For analyzing weather trends or climate change over decades, use the Historical Weather API with reanalysis data from 1940 onwards.
- For higher accuracy over the past few years, the Historical Forecast API with high-resolution forecasts is more suitable.
- To optimize weather forecasts using machine learning, it's essential to use data from the same high-resolution weather models, available through both the Historical Forecast API and the Previous Runs API.

## API Parameter

As the API is identical to the Forecast API, please refer to the Weather Forecast API documentation for all available variables and parameters. The only notable difference is the API host "historical-forecast-api.open-meteo.com" as historical data is moved to a different set of servers with access to a large storage system.