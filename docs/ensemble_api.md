---
api-endpoint: https://ensemble-api.open-meteo.com/v1/ensemble
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Ensemble API
url: https://open-meteo.com/en/docs/ensemble-api
---

[blog article](https://openmeteo.substack.com/p/ensemble-weather-forecast-api).

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
from openmeteo_sdk.Variable import Variable
from openmeteo_sdk.Aggregation import Aggregation
import requests_cache
import pandas as pd
from retry_requests import retry
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)
# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://ensemble-api.open-meteo.com/v1/ensemble"
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
# Process hourly data
hourly = response.Hourly()
hourly_variables = list(map(lambda i: hourly.Variables(i), range(0, hourly.VariablesLength())))
hourly_temperature_2m = filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, hourly_variables)
hourly_data = {"date": pd.date_range(
start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
freq = pd.Timedelta(seconds = hourly.Interval()),
inclusive = "left"
)}
# Process all members
for variable in hourly_temperature_2m:
member = variable.EnsembleMember()[f"temperature_2m_member{member}"] = variable.ValuesAsNumpy()
hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
```


## Data Source

Ensemble models are a type of weather forecasting technique that use multiple members or versions of a model to produce a range of possible outcomes for a given forecast. Each member is initialized with slightly different initial conditions and/or model parameters to account for uncertainties and variations in the atmosphere, resulting in a set of perturbed forecasts.

By combining the perturbed forecasts, the ensemble model generates a probability distribution of possible outcomes, indicating not only the most likely forecast but also the range of possible outcomes and their likelihoods. This probabilistic approach provides more comprehensive and accurate forecast guidance, especially for high-impact weather events where uncertainties are high.

Different national weather services calculate ensemble models, each with varying resolutions of weather variables and forecast time-range. For instance, the German weather service DWD's ICON model provides exceptionally high resolution for Europe but only forecasts up to 7 days. Meanwhile, the GFS model can forecast up to 35 days, albeit at a lower resolution of 50 km. The appropriate ensemble model to use would depend on the forecast horizon and region of interest.

[model updates documentation](https://open-meteo.com/en/docs/model-updates).

| National Weather Service | Weather Model | Region | Resolution | Members | Forecast Length | Update frequency |
|---|---|---|---|---|---|---|
| Deutscher Wetterdienst (DWD) | ICON-D2-EPS | Central Europe | 2 km, hourly | 20 | 2 days | Every 3 hours |
| ICON-EU-EPS | Europe | 13 km, hourly | 40 | 5 days | Every 6 hours | |
| ICON-EPS | Global | 26 km, hourly | 40 | 7.5 days | Every 12 hours | |
| NOAA | GFS Ensemble 0.25° | Global | 25 km, 3-hourly | 31 | 10 days | Every 6 hours |
| GFS Ensemble 0.5° | Global | 50 km, 3-hourly | 31 | 35 days | Every 6 hours | |
| ECMWF | IFS 0.4° | Global | 44 km, 3-hourly | 51 | 15 days | Every 6 hours |
| IFS 0.25° | Global | 25 km, 3-hourly | 51 | 15 days | Every 6 hours | |
| Canadian Weather Service | GEM | Global | 25 km, 3-hourly | 21 | 16 days (32 days every thursday) | Every 12 hours |
| Australian Bureau of Meteorology (BOM) | ACCESS-GE | Global | 40 km, 3-hourly | 18 | 10 days | Every 6 hours |

To ensure ease of use, all data is interpolated to a 1-hourly time-step resolution. As the forecast horizon extends further into the future, some ensemble models may reduce the time resolution to 6-hourly intervals.

## API Documentation

The API endpoint /v1/ensemble accepts a geographical coordinate, a list of weather variables and responds with a JSON hourly weather forecast for 7 days for each ensemble member. Time always starts at 0:00 today. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude, longitude | Floating point | Yes | ||
| models | String array | Yes | Select one or more ensemble weather models as comma-separated list | |
| elevation | Floating point | No | The elevation used for statistical downscaling. Per default, a
|

[time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.forecast_minutely_15

past_hours

past_minutely_15

end_date

end_hour

start_minutely_15

end_minutely_15

[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| temperature_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative_humidity_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew_point_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent_temperature | Instant | °C (°F) | |
| pressure_msl surface_pressure | Instant | hPa | |
| cloud_cover | Instant | % | Total cloud cover as an area fraction |
| wind_speed_10m wind_speed_80m wind_speed_120m | Instant | km/h (mph, m/s, knots) | Wind speed at 10, 80 or 120 meters above ground. Wind speed on 10 meters is the standard level. |
| wind_direction_10m wind_direction_80m wind_direction_120m | Instant | ° | Wind direction at 10, 80 or 120 meters above ground |
| wind_gusts_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave_radiation | Preceding hour mean | W/m² | |
| direct_radiation direct_normal_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the
normal plane (perpendicular to the sun). HRRR offers direct radiation directly. In GFS it
is approximated based on
|

[Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf)[FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm)ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.[Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy).soil_temperature_10_to_40cm

soil_temperature_40_to_100cm

soil_temperature_100_to_200cm

soil_moisture_10_to_40cm

soil_moisture_40_to_100cm

soil_moisture_100_to_200cm