---
api-endpoint: https://historical-forecast-api.open-meteo.com/v1/forecast
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Previous Model Runs API
url: https://open-meteo.com/en/docs/previous-runs-api
---

[Open-Meteo blog post](https://openmeteo.substack.com/p/weather-forecasts-from-previous-model-runs).

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
url = "https://previous-runs-api.open-meteo.com/v1/forecast"
params = {
"latitude": 52.52,
"longitude": 13.41,
"hourly": ["temperature_2m", "temperature_2m_previous_day1", "temperature_2m_previous_day2", "temperature_2m_previous_day3", "temperature_2m_previous_day4", "temperature_2m_previous_day5"],
"past_days": 7
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
hourly_temperature_2m_previous_day1 = hourly.Variables(1).ValuesAsNumpy()
hourly_temperature_2m_previous_day2 = hourly.Variables(2).ValuesAsNumpy()
hourly_temperature_2m_previous_day3 = hourly.Variables(3).ValuesAsNumpy()
hourly_temperature_2m_previous_day4 = hourly.Variables(4).ValuesAsNumpy()
hourly_temperature_2m_previous_day5 = hourly.Variables(5).ValuesAsNumpy()
hourly_data = {"date": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["temperature_2m_previous_day1"] = hourly_temperature_2m_previous_day1
hourly_data["temperature_2m_previous_day2"] = hourly_temperature_2m_previous_day2
hourly_data["temperature_2m_previous_day3"] = hourly_temperature_2m_previous_day3
hourly_data["temperature_2m_previous_day4"] = hourly_temperature_2m_previous_day4
hourly_data["temperature_2m_previous_day5"] = hourly_temperature_2m_previous_day5
hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
```


## API Documentation

Weather models constantly churn out updates, each predicting the future at different lead times. Think of Day 0 as latest forecast close to measurements, Day 1 as a glimpse 24 hours back, and Day 2 as a 48-hour rewind. Each day further back forecasts longer into the future and, typically, increases volatility. Data jumps become wilder past Day 6 or 7, highlighting the inherent challenge of long-term forecasting.

This data serves multiple purposes, including answering questions such as "what did yesterday's forecast predict for today?" or by comparing past forecasts with real-time observations, we can assess a forecast's accuracy and volatility. When combined with machine learning techniques, models can be trained specifically to enhance forecasts for the next 2 or 3 days.

The frequency of model updates varies, ranging from hourly to every six hours. For local models with shorter prediction horizons (2-5 days), we naturally have access to a shorter "time machine" of past predictions (2-5 days).

**Weather Models Sources:** The Previous Runs API uses the same models as available in the general weather forecast API. Please refer to the [Forecast API documentation](https://open-meteo.com/en/docs) for a list of all weather models and weather variables.

**Data Availability:** Data is generally available from January 2024 onwards. Exceptions are GFS temperature on 2 metre, which is available from March 2021 and JMA GSM + MSM models which are available from 2018. More data from previous runs can be reconstructed on request (depending on data availability from official sources).