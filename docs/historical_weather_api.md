---
api-endpoint: https://archive-api.open-meteo.com/v1/archive
date: 2024-12-15
description: "Historical \U0001F324️ weather data from 1940 onwards with weather records
  dating back to 1940 and hourly resolution available for any location on earth. Retrieve
  decades worth of data in less than a second with our lightning-fast API. Dive deep
  into historical weather records, uncover trends, and gain valuable insights with
  ease."
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Historical Weather API
url: https://open-meteo.com/en/docs/historical-weather-api
---

[blog article](https://open.substack.com/pub/openmeteo/p/processing-90-tb-historical-weather).

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
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)
# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
"latitude": 52.52,
"longitude": 13.41,
"start_date": "2024-12-15",
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


## Data Sources

The Historical Weather API is based on reanalysis datasets and uses a combination of weather station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of past weather conditions. These datasets are able to fill in gaps by using mathematical models to estimate the values of various weather variables. As a result, reanalysis datasets are able to provide detailed historical weather information for locations that may not have had weather stations nearby, such as rural areas or the open ocean.

The models for historical weather data use a spatial resolution of 9 km to resolve fine details close to coasts or complex mountain terrain. In general, a higher spatial resolution means that the data is more detailed and represents the weather conditions more accurately at smaller scales.

The ECMWF IFS dataset has been meticulously assembled by Open-Meteo using simulation runs at 0z and 12z, employing the most up-to-date version of IFS. This dataset offers the utmost resolution and precision in depicting historical weather conditions.

However, when studying climate change over decades, it is advisable to exclusively utilize ERA5 or ERA5-Land. This choice ensures data consistency and prevents unintentional alterations that could arise from the adoption of different weather model upgrades.

You can access data dating back to 1940 with a delay of 2 days. If you're looking for weather
information from the previous day, our [Forecast API](https://open-meteo.com/en/docs)
offers the &past_days= feature for your convenience.

| Data Set | Region | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency |
|---|---|---|---|---|---|
|

[ERA5](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

[ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview)

[ERA5-Ensemble](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

[CERRA](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-single-levels?tab=overview)

[ECMWF IFS Assimilation Long-Window](https://confluence.ecmwf.int/display/FUG/Section+2.5+Model+Data+Assimilation%2C+4D-Var)

Different reanalysis models may include different sets of weather variables in their datasets. For example, the ERA5 model includes all weather variables, while the ERA5-Land model only includes surface variables such as temperature, humidity, soil temperature, and soil moisture. The CERRA model includes most weather variables, but does not include soil temperature and moisture. It is important to be aware of the specific variables that are included in a particular reanalysis model in order to understand the limitations and potential biases of the data.

## API Documentation

The API endpoint /v1/archive allows users to retrieve historical weather data for a specific location and time period. To use this endpoint, you can specify a geographical coordinate, a time interval, and a list of weather variables that they are interested in. The endpoint will then return the requested data in a format that can be easily accessed and used by applications or other software. This endpoint can be very useful for researchers and other users who need to access detailed historical weather data for specific locations and time periods.

All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude longitude | Floating point | Yes | ||
| elevation | Floating point | No | The elevation used for statistical downscaling. Per default, a
|

end_date

[time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)is supported If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.[similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.[pricing](https://open-meteo.com/en/pricing)for more information.### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given as an instantaneous value for the indicated hour. Some variables like precipitation are calculated from the preceding hour as and average or sum.

| Variable | Valid time | Unit | Description |
|---|---|---|---|
| temperature_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative_humidity_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew_point_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent_temperature | Instant | °C (°F) | |
| pressure_msl surface_pressure | Instant | hPa | |
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision. If precipitation data is summed up to monthly sums, there might be small inconsistencies with the total precipitation amount. |
| rain | Preceding hour sum | mm (inch) | Only liquid precipitation of the preceding hour including local showers and rain from large scale systems. |
| snowfall | Preceding hour sum | cm (inch) | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent |
| cloud_cover | Instant | % | Total cloud cover as an area fraction |
| cloud_cover_low | Instant | % | Low level clouds and fog up to 2 km altitude |
| cloud_cover_mid | Instant | % | Mid level clouds from 2 to 6 km altitude |
| cloud_cover_high | Instant | % | High level clouds from 6 km altitude |
| shortwave_radiation | Preceding hour mean | W/m² | |
| direct_radiation direct_normal_irradiance | Preceding hour mean | W/m² | |
| diffuse_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour |
| global_tilted_irradiance | Preceding hour mean | W/m² | |
| sunshine_duration | Preceding hour sum | Seconds | Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition. |
| wind_speed_10m wind_speed_100m | Instant | km/h (mph, m/s, knots) | Wind speed at 10 or 100 meters above ground. Wind speed on 10 meters is the standard level. |
| wind_direction_10m wind_direction_100m | Instant | ° | Wind direction at 10 or 100 meters above ground |
| wind_gusts_10m | Instant | km/h (mph, m/s, knots) | Gusts at 10 meters above ground of the indicated hour. Wind gusts in CERRA
are defined as the maximum wind gusts of the preceding hour. Please consult the
|

[FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm)ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.soil_temperature_7_to_28cm

soil_temperature_28_to_100cm

soil_temperature_100_to_255cm

soil_moisture_7_to_28cm

soil_moisture_28_to_100cm

soil_moisture_100_to_255cm

### Daily Parameter Definition

| Variable | Unit | Description |
|---|---|---|
| weather_code | WMO code | The most severe weather condition on a given day |
| temperature_2m_max temperature_2m_min | °C (°F) | Maximum and minimum daily air temperature at 2 meters above ground |
| apparent_temperature_max apparent_temperature_min | °C (°F) | Maximum and minimum daily apparent temperature |
| precipitation_sum | mm | Sum of daily precipitation (including rain, showers and snowfall) |
| rain_sum | mm | Sum of daily rain |
| snowfall_sum | cm | Sum of daily snowfall |
| precipitation_hours | hours | The number of hours with rain |
| sunrise sunset | iso8601 | Sun rise and set times |
| sunshine_duration | seconds | |
| daylight_duration | seconds | Number of seconds of daylight per day |
| wind_speed_10m_max wind_gusts_10m_max | km/h (mph, m/s, knots) | Maximum wind speed and gusts on a day |
| wind_direction_10m_dominant | ° | Dominant wind direction |
| shortwave_radiation_sum | MJ/m² | The sum of solar radiaion on a given day in Megajoules |
| et0_fao_evapotranspiration | mm | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field |

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
| elevation | Floating point | |
| generationtime_ms | Floating point | |
| utc_offset_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezone timezone_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| hourly | Object | |
| hourly_units | Object | For each selected weather variable, the unit will be listed here. |
| daily | Object | |
| daily_units | Object | For each selected daily weather variable, the unit will be listed here. |

### Errors

```
"error": true,
"reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"
```


## Citation & Acknowledgement

We encourage researchers in the field of meteorology and related disciplines to cite Open-Meteo and its sources in their work. Citing not only gives proper credit but also promotes transparency, reproducibility, and collaboration within the scientific community. Together, let's foster a culture of recognition and support for open-data initiatives like Open-Meteo, ensuring that future researchers can benefit from the valuable resources it provides.

Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. [https://doi.org/10.5281/ZENODO.7970649](https://doi.org/10.5281/ZENODO.7970649)

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J.,
Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D.,
Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set].
ECMWF. [https://doi.org/10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47)

Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF. [https://doi.org/10.24381/CDS.E2161BAC](https://doi.org/10.24381/CDS.E2161BAC)

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea
U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton
M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. (2021). CERRA
sub-daily regional reanalysis data for Europe on single levels from 1984 to present [Data
set]. ECMWF. [https://doi.org/10.24381/CDS.622A565A](https://doi.org/10.24381/CDS.622A565A)

Zippenfenig, Patrick. Open-Meteo.com Weather API., Zenodo, 2023, doi:10.5281/ZENODO.7970649.

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set]. ECMWF. https://doi.org/10.24381/cds.adbb2d47

Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF. https://doi.org/10.24381/CDS.E2161BAC

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. CERRA Sub-Daily Regional Reanalysis Data for Europe on Single Levels from 1984 to Present. ECMWF, 2021, doi:10.24381/CDS.622A565A.

Zippenfenig, P. (2023) Open-Meteo.com Weather API. Zenodo. doi: 10.5281/ZENODO.7970649.

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023) “ERA5 hourly data on single levels from 1940 to present.” ECMWF. doi: 10.24381/cds.adbb2d47.

Muñoz Sabater, J. (2019) “ERA5-Land hourly data from 2001 to present.” ECMWF. doi: 10.24381/CDS.E2161BAC.

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. (2021) “CERRA sub-daily regional reanalysis data for Europe on single levels from 1984 to present.” ECMWF. doi: 10.24381/CDS.622A565A.

```
@software{Zippenfenig_Open-Meteo,
author = {Zippenfenig, Patrick},
doi = {10.5281/zenodo.7970649},
license = {CC-BY-4.0},
title = {Open-Meteo.com Weather API},
year = {2023},
copyright = {Creative Commons Attribution 4.0 International},
url = {https://open-meteo.com/}
}
```


```
@misc{Hersbach_ERA5,
doi = {10.24381/cds.adbb2d47},
url = {https://cds.climate.copernicus.eu/doi/10.24381/cds.adbb2d47},
author = {Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N.},
title = {ERA5 hourly data on single levels from 1940 to present},
publisher = {ECMWF},
year = {2023}
}
```


```
@misc{Munoz_ERA5_LAND,
doi = {10.24381/CDS.E2161BAC},
url = {https://cds.climate.copernicus.eu/doi/10.24381/cds.e2161bac},
author = {Muñoz Sabater, J.},
title = {ERA5-Land hourly data from 2001 to present},
publisher = {ECMWF},
year = {2019}
}
```


```
@misc{Schimanke_CERRA,
doi = {10.24381/CDS.622A565A},
url = {https://cds.climate.copernicus.eu/doi/10.24381/cds.622a565a},
author = {Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q.},
title = {CERRA sub-daily regional reanalysis data for Europe on single levels from 1984 to present},
publisher = {ECMWF},
year = {2021}
}
```


Generated using Copernicus Climate Change Service information 2022.