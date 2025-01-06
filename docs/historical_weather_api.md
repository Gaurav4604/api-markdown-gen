[Open-Meteo](/)

- ***
- [Home](/ "Weather API")
- [Features](/en/features "API Features")
- [Pricing](/en/pricing "Pricing")
- [API Docs](/en/docs "Documentation")

- ***
- [GitHub](https://github.com/open-meteo/open-meteo)
- [Twitter](https://twitter.com/open_meteo)
- ***
- Toggle theme
  - Light
  - Dark
  - Auto

# Historical Weather API

Discover how weather has shaped our world from 1940 until now

Available APIs

- [Weather Forecast](/en/docs)
- [Historical Weather](/en/docs/historical-weather-api)
- [Ensemble Models](/en/docs/ensemble-api)
- [Climate Change](/en/docs/climate-api)
- [Marine Forecast](/en/docs/marine-weather-api)
- [Air Quality](/en/docs/air-quality-api)
- [Geocoding](/en/docs/geocoding-api)
- [Elevation](/en/docs/elevation-api)
- [Flood](/en/docs/flood-api)
  Now, with the addition of the 9-kilometer ECMWF IFS model, the historical weather API provides access to a staggering 90 terabytes of meteorological data! Read the [blog article](https://open.substack.com/pub/openmeteo/p/processing-90-tb-historical-weather).

## Location and Time

- Location:
- Coordinates
- List
  Latitude Longitude America/AnchorageAmerica/Los_AngelesAmerica/DenverAmerica/ChicagoAmerica/New_YorkAmerica/Sao_PauloNot set (GMT+0)GMT+0Automatically detect time zoneEurope/LondonEurope/BerlinEurope/MoscowAfrica/CairoAsia/BangkokAsia/SingaporeAsia/TokyoAustralia/SydneyPacific/Auckland Timezone Search Start Date End Date

You can access past weather data dating back to 1940. However, there is a 5-day delay in the
data. If you want information for the most recent days, you can use the [forecast API](/en/docs "Weather forecast API")
and adjust the Past Days setting.

Quick:
2000-2009 2010-2019 2020 2021 2022 2023 2024

## Hourly Weather Variables

Temperature (2 m) Relative Humidity (2 m) Dewpoint (2 m) Apparent Temperature Precipitation (rain + snow) Rain Snowfall Snow depth Weather code Sealevel Pressure Surface Pressure Cloud cover Total Cloud cover Low Cloud cover Mid Cloud cover High Reference Evapotranspiration (ET₀) Vapour Pressure Deficit Wind Speed (10 m) Wind Speed (100 m) Wind Direction (10 m) Wind Direction (100 m) Wind Gusts (10 m) Soil Temperature (0-7 cm) Soil Temperature (7-28 cm) Soil Temperature (28-100 cm) Soil Temperature (100-255 cm) Soil Moisture (0-7 cm) Soil Moisture (7-28 cm) Soil Moisture (28-100 cm) Soil Moisture (100-255 cm)

## Additional Variables And Options

## Solar Radiation Variables

## ERA5-Ensemble Spread Variables

## Reanalysis models

## Daily Weather Variables

Weather code Maximum Temperature (2 m) Minimum Temperature (2 m) Mean Temperature (2 m) Maximum Apparent Temperature (2 m) Minimum Apparent Temperature (2 m) Mean Apparent Temperature (2 m) Sunrise Sunset Daylight Duration Sunshine Duration Precipitation Sum Rain Sum Snowfall Sum Precipitation Hours Maximum Wind Speed (10 m) Maximum Wind Gusts (10 m) Dominant Wind Direction (10 m) Shortwave Radiation Sum Reference Evapotranspiration (ET₀)

## Settings

Celsius °CFahrenheit °F Temperature Unit Km/hm/sMphKnots Wind Speed Unit MillimeterInch Precipitation Unit ISO 8601 (e.g. 2022-12-31)Unix timestamp Timeformat

- Usage License:
- Non-Commercial
- Commercial
- Self-Hosted
  Only for **non-commercial use** and less than 10.000 daily API calls. See [Terms](/en/terms) for more details.

## API Response

- Preview:
- Chart And URL
- Python
- Typescript
- Swift
- Other
  Loading... [Download XLSX](https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-12-17&end_date=2024-12-31&hourly=temperature_2m&format=xlsx) [Download CSV](https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-12-17&end_date=2024-12-31&hourly=temperature_2m&format=csv) API URL ([Open in new tab](https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-12-17&end_date=2024-12-31&hourly=temperature_2m) or copy this
  URL into your application).

## Data Sources

The Historical Weather API is based on reanalysis datasets and uses a combination of weather
station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of
past weather conditions. These datasets are able to fill in gaps by using mathematical models
to estimate the values of various weather variables. As a result, reanalysis datasets are able
to provide detailed historical weather information for locations that may not have had weather
stations nearby, such as rural areas or the open ocean.

The models for historical weather data use a spatial resolution of 9 km to resolve fine details
close to coasts or complex mountain terrain. In general, a higher spatial resolution means that the data is
more detailed and represents the weather conditions more accurately at smaller scales.

The ECMWF IFS dataset has been meticulously assembled by Open-Meteo using simulation runs at 0z and 12z,
employing the most up-to-date version of IFS. This dataset offers the utmost resolution and precision
in depicting historical weather conditions.

However, when studying climate change over decades, it is advisable to exclusively utilize ERA5 or ERA5-Land.
This choice ensures data consistency and prevents unintentional alterations that could arise from the adoption
of different weather model upgrades.

You can access data dating back to 1940 with a delay of 2 days. If you're looking for weather
information from the previous day, our [Forecast API](/en/docs "Weather Forecast API documentation")
offers the &past_days= feature for your convenience.

You can find the update timings in the [model updates documentation](/en/docs/model-updates).
| Data Set | Region | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency |
| --- | --- | --- | --- | --- | --- |
| [ECMWF IFS](https://www.ecmwf.int/en/forecasts/documentation-and-support/changes-ecmwf-model) | Global | 9 km | Hourly | 2017 to present | Daily with 2 days delay |
| [ERA5](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | Global | 0.25° (~25 km) | Hourly | 1940 to present | Daily with 5 days delay |
| [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview) | Global | 0.1° (~11 km) | Hourly | 1950 to present | Daily with 5 days delay |
| [ERA5-Ensemble](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | Global | 0.5° (~55 km) | 3-Hourly | 1940 to present | Daily with 5 days delay |
| [CERRA](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-single-levels?tab=overview) | Europe | 5 km | Hourly | 1985 to June 2021 | - |
| [ECMWF IFS Assimilation Long-Window](https://confluence.ecmwf.int/display/FUG/Section%2B2.5%2BModel%2BData%2BAssimilation%2C%2B4D-Var) | Global | 9 km | 6-Hourly | 2024 to present | Daily with 2 days delay |

Different reanalysis models may include different sets of weather variables in their datasets. For
example, the ERA5 model includes all weather variables, while the ERA5-Land model only includes
surface variables such as temperature, humidity, soil temperature, and soil moisture. The CERRA
model includes most weather variables, but does not include soil temperature and moisture. It is
important to be aware of the specific variables that are included in a particular reanalysis model
in order to understand the limitations and potential biases of the data.

## API Documentation

The API endpoint /v1/archive allows users to retrieve historical weather data for a
specific location and time period. To use this endpoint, you can specify a geographical coordinate,
a time interval, and a list of weather variables that they are interested in. The endpoint will then
return the requested data in a format that can be easily accessed and used by applications or other
software. This endpoint can be very useful for researchers and other users who need to access detailed
historical weather data for specific locations and time periods.

All URL parameters are listed below:

| Parameter           | Format              | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------- | ------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| latitude, longitude | Floating point      | Yes      |         | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location_id.                                                                                                                                                                                            |
| elevation           | Floating point      | No       |         | The elevation used for statistical downscaling. Per default, a [90 meter digital elevation model is used](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated. |
| start_dateend_date  | String (yyyy-mm-dd) | Yes      |         | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-12-31).                                                                                                                                                                                                                                                                                                                                                                           |
| hourly              | String array        | No       |         | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used.                                                                                                                                                                                                                                                                                                                                    |
| daily               | String array        | No       |         | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required.                                                                                                                                                                                                                                         |
| temperature_unit    | String              | No       | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit.                                                                                                                                                                                                                                                                                                                                                                                                      |
| wind_speed_unit     | String              | No       | kmh     | Other wind speed speed units: ms, mph and kn                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| precipitation_unit  | String              | No       | mm      | Other precipitation amount units: inch                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| timeformat          | String              | No       | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date.                                                                                                                                                                                                                                   |
| timezone            | String              | No       | GMT     | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified.                                             |
| cell_selection      | String              | No       | land    | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell.                                                                            |
| apikey              | String              | No       |         | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information.                                                                                                                                                                                                                                       |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given
as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
from the preceding hour as and average or sum.

| Variable                                                                                                     | Valid time          | Unit                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------ | ------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| temperature_2m                                                                                               | Instant             | °C (°F)                | Air temperature at 2 meters above ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| relative_humidity_2m                                                                                         | Instant             | %                      | Relative humidity at 2 meters above ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| dew_point_2m                                                                                                 | Instant             | °C (°F)                | Dew point temperature at 2 meters above ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| apparent_temperature                                                                                         | Instant             | °C (°F)                | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation                                                                                                                                                                                                                                                                                                                                                                                                        |
| pressure_mslsurface_pressure                                                                                 | Instant             | hPa                    | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.                                                                                                                                                                                                                                                                                                                                   |
| precipitation                                                                                                | Preceding hour sum  | mm (inch)              | Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision. If precipitation data is summed up to monthly sums, there might be small inconsistencies with the total precipitation amount.                                                                                                                                                                                                                                                                                             |
| rain                                                                                                         | Preceding hour sum  | mm (inch)              | Only liquid precipitation of the preceding hour including local showers and rain from large scale systems.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| snowfall                                                                                                     | Preceding hour sum  | cm (inch)              | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent                                                                                                                                                                                                                                                                                                                                                                       |
| cloud_cover                                                                                                  | Instant             | %                      | Total cloud cover as an area fraction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| cloud_cover_low                                                                                              | Instant             | %                      | Low level clouds and fog up to 2 km altitude                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cloud_cover_mid                                                                                              | Instant             | %                      | Mid level clouds from 2 to 6 km altitude                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| cloud_cover_high                                                                                             | Instant             | %                      | High level clouds from 6 km altitude                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| shortwave_radiation                                                                                          | Preceding hour mean | W/m²                   | Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation                                                                                                                                                                                                                                                                                                                                                                                                                   |
| direct_radiationdirect_normal_irradiance                                                                     | Preceding hour mean | W/m²                   | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun)                                                                                                                                                                                                                                                                                                                                                                                                        |
| diffuse_radiation                                                                                            | Preceding hour mean | W/m²                   | Diffuse solar radiation as average of the preceding hour                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| global_tilted_irradiance                                                                                     | Preceding hour mean | W/m²                   | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west). If azimuth is set to "nan", the calculation assumes a horizontal tracker. If tilt is set to "nan", it is assumed that the panel has a vertical tracker. If both are set to "nan", a bi-axial tracker is assumed. |
| sunshine_duration                                                                                            | Preceding hour sum  | Seconds                | Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition.                                                                                                                                                                                                                                                                                                                                                                              |
| wind_speed_10mwind_speed_100m                                                                                | Instant             | km/h (mph, m/s, knots) | Wind speed at 10 or 100 meters above ground. Wind speed on 10 meters is the standard level.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| wind_direction_10mwind_direction_100m                                                                        | Instant             | °                      | Wind direction at 10 or 100 meters above ground                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| wind_gusts_10m                                                                                               | Instant             | km/h (mph, m/s, knots) | Gusts at 10 meters above ground of the indicated hour. Wind gusts in CERRA are defined as the maximum wind gusts of the preceding hour. Please consult the [ECMWF IFS documentation](https://www.ecmwf.int/en/elibrary/81271-ifs-documentation-cy47r3-part-iv-physical-processes) for more information on how wind gusts are parameterized in weather models.                                                                                                                                                                          |
| et0_fao_evapotranspiration                                                                                   | Preceding hour sum  | mm (inch)              | ET₀ Reference Evapotranspiration of a well watered grass field. Based on [FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm) ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.                                                                                                                                                                                             |
| weather_code                                                                                                 | Instant             | WMO code               | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. Weather code is calculated from cloud cover analysis, precipitation and snowfall. As barely no information about atmospheric stability is available, estimation about thunderstorms is not possible.                                                                                                                                                                                                                        |
| snow_depth                                                                                                   | Instant             | meters                 | Snow depth on the ground. Snow depth in ERA5-Land tends to be overestimated. As the spatial resolution for snow depth is limited, please use it with care.                                                                                                                                                                                                                                                                                                                                                                             |
| vapour_pressure_deficit                                                                                      | Instant             | kPa                    | Vapor Pressure Deificit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases                                                                                                                                                                                                                                                                                                                                                                           |
| soil_temperature_0_to_7cmsoil_temperature_7_to_28cmsoil_temperature_28_to_100cmsoil_temperature_100_to_255cm | Instant             | °C (°F)                | Average temperature of different soil levels below ground.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| soil_moisture_0_to_7cmsoil_moisture_7_to_28cmsoil_moisture_28_to_100cmsoil_moisture_100_to_255cm             | Instant             | m³/m³                  | Average soil water content as volumetric mixing ratio at 0-7, 7-28, 28-100 and 100-255 cm depths.                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Daily Parameter Definition

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

| Variable                                         | Unit                   | Description                                                                                                                                                                                                                                    |
| ------------------------------------------------ | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weather_code                                     | WMO code               | The most severe weather condition on a given day                                                                                                                                                                                               |
| temperature_2m_maxtemperature_2m_min             | °C (°F)                | Maximum and minimum daily air temperature at 2 meters above ground                                                                                                                                                                             |
| apparent_temperature_maxapparent_temperature_min | °C (°F)                | Maximum and minimum daily apparent temperature                                                                                                                                                                                                 |
| precipitation_sum                                | mm                     | Sum of daily precipitation (including rain, showers and snowfall)                                                                                                                                                                              |
| rain_sum                                         | mm                     | Sum of daily rain                                                                                                                                                                                                                              |
| snowfall_sum                                     | cm                     | Sum of daily snowfall                                                                                                                                                                                                                          |
| precipitation_hours                              | hours                  | The number of hours with rain                                                                                                                                                                                                                  |
| sunrisesunset                                    | iso8601                | Sun rise and set times                                                                                                                                                                                                                         |
| sunshine_duration                                | seconds                | The number of seconds of sunshine per day is determined by calculating direct normalized irradiance exceeding 120 W/m², following the WMO definition. Sunshine duration will consistently be less than daylight duration due to dawn and dusk. |
| daylight_duration                                | seconds                | Number of seconds of daylight per day                                                                                                                                                                                                          |
| wind_speed_10m_maxwind_gusts_10m_max             | km/h (mph, m/s, knots) | Maximum wind speed and gusts on a day                                                                                                                                                                                                          |
| wind_direction_10m_dominant                      | °                      | Dominant wind direction                                                                                                                                                                                                                        |
| shortwave_radiation_sum                          | MJ/m²                  | The sum of solar radiaion on a given day in Megajoules                                                                                                                                                                                         |
| et0_fao_evapotranspiration                       | mm                     | Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field                                                                                                                                                                    |

### JSON Return Object

On success a JSON object will be returned.

```

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

| Parameter                     | Format         | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| latitude, longitude           | Floating point | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometers away from the requested coordinate.                                                                                                                                                                                                                              |
| elevation                     | Floating point | The elevation from a 90 meter digital elevation model. This effects which grid-cell is selected (see parameter cell_selection). Statistical downscaling is used to adapt weather conditions for this elevation. This elevation can also be controlled with the query parameter elevation. If &elevation=nan is specified, all downscaling is disabled and the averge grid-cell elevation is used. |
| generationtime_ms             | Floating point | Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements.                                                                                                                                                                                                                                                                         |
| utc_offset_seconds            | Integer        | Applied timezone offset from the &timezone= parameter.                                                                                                                                                                                                                                                                                                                                            |
| timezonetimezone_abbreviation | String         | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST)                                                                                                                                                                                                                                                                                                                             |
| hourly                        | Object         | For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.                                                                                                                                                                                                                                          |
| hourly_units                  | Object         | For each selected weather variable, the unit will be listed here.                                                                                                                                                                                                                                                                                                                                 |
| daily                         | Object         | For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.                                                                                                                                                                                                                                    |
| daily_units                   | Object         | For each selected daily weather variable, the unit will be listed here.                                                                                                                                                                                                                                                                                                                           |

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error": true,
  "reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"

```

## Citation & Acknowledgement

We encourage researchers in the field of meteorology and related disciplines to cite Open-Meteo
and its sources in their work. Citing not only gives proper credit but also promotes transparency,
reproducibility, and collaboration within the scientific community. Together, let's foster a
culture of recognition and support for open-data initiatives like Open-Meteo, ensuring that future
researchers can benefit from the valuable resources it provides.

- APA
- MLA
- Harvard
- BibTeX

Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. [https://doi.org/10.5281/ZENODO.7970649](https://doi.org/10.5281/ZENODO.7970649 "zenodo publication")

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J.,
Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D.,
Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set].
ECMWF. [https://doi.org/10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47 "era5-land")

Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF. [https://doi.org/10.24381/CDS.E2161BAC](https://doi.org/10.24381/CDS.E2161BAC "era5-land")

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea
U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton
M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. (2021). CERRA
sub-daily regional reanalysis data for Europe on single levels from 1984 to present [Data
set]. ECMWF. [https://doi.org/10.24381/CDS.622A565A](https://doi.org/10.24381/CDS.622A565A "cerra")

Zippenfenig, Patrick. Open-Meteo.com Weather API., Zenodo, 2023, doi:10.5281/ZENODO.7970649.

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J.,
Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D.,
Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set].
ECMWF. https://doi.org/10.24381/cds.adbb2d47

Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF.
https://doi.org/10.24381/CDS.E2161BAC

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea
U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton
M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. CERRA Sub-Daily
Regional Reanalysis Data for Europe on Single Levels from 1984 to Present. ECMWF, 2021,
doi:10.24381/CDS.622A565A.

Zippenfenig, P. (2023) Open-Meteo.com Weather API. Zenodo. doi: 10.5281/ZENODO.7970649.

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J.,
Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D.,
Thépaut, J-N. (2023) “ERA5 hourly data on single levels from 1940 to present.” ECMWF. doi:
10.24381/cds.adbb2d47.

Muñoz Sabater, J. (2019) “ERA5-Land hourly data from 2001 to present.” ECMWF. doi:
10.24381/CDS.E2161BAC.

Schimanke S., Ridal M., Le Moigne P., Berggren L., Undén P., Randriamampianina R., Andrea
U., Bazile E., Bertelsen A., Brousseau P., Dahlgren P., Edvinsson L., El Said A., Glinton
M., Hopsch S., Isaksson L., Mladek R., Olsson E., Verrelle A., Wang Z.Q. (2021) “CERRA
sub-daily regional reanalysis data for Europe on single levels from 1984 to present.” ECMWF.
doi: 10.24381/CDS.622A565A.

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

Open-Meteo

- [Features](/en/features)
- [Pricing](/en/pricing)
- [About us & Contact](/en/about)
- [License](/en/license)
- [Terms & Privacy](/en/terms)

Weather APIs

- [Weather Forecast API](/en/docs)
- [Historical Weather API](/en/docs/historical-weather-api)
- [ECMWF API](/en/docs/ecmwf-api)
- [GFS & HRRR Forecast API](/en/docs/gfs-api)
- [Météo-France API](/en/docs/meteofrance-api)
- [DWD ICON API](/en/docs/dwd-api)
- [GEM API](/en/docs/gem-api)
- [JMA API](/en/docs/jma-api)
- [Met Norway API](/en/docs/metno-api)

Other APIs

- [Ensemble API](/en/docs/ensemble-api)
- [Climate Change API](/en/docs/climate-api)
- [Marine Weather API](/en/docs/marine-weather-api)
- [Air Quality API](/en/docs/air-quality-api)
- [Geocoding API](/en/docs/geocoding-api)
- [Elevation API](/en/docs/elevation-api)
- [Flood API](/en/docs/flood-api)

External

- [GitHub](https://github.com/open-meteo/open-meteo)
- [Blog](https://openmeteo.substack.com/archive?sort=new)
- [Twitter](https://twitter.com/open_meteo)
- [Mastodon](https://fosstodon.org/%40openmeteo)
- [Service status and uptime](https://status.open-meteo.com)
- [Model Updates Overview](/en/docs/model-updates)
  © 2022-2025 Copyright: Open-Meteo.com
