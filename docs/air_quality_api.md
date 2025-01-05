
 [Open-Meteo](/)

* ---
* [Home](/ "Weather API")
* [Features](/en/features "API Features")
* [Pricing](/en/pricing "Pricing")
* [API Docs](/en/docs "Documentation")

* ---
* [GitHub](https://github.com/open-meteo/open-meteo)
* [Twitter](https://twitter.com/open_meteo)
* ---
* Toggle theme
  + Light
  + Dark
  + Auto

# Air Quality API

Pollutants and pollen forecast in 11 km resolution

 Available APIs

* [Weather Forecast](/en/docs)
* [Historical Weather](/en/docs/historical-weather-api)
* [Ensemble Models](/en/docs/ensemble-api)
* [Climate Change](/en/docs/climate-api)
* [Marine Forecast](/en/docs/marine-weather-api)
* [Air Quality](/en/docs/air-quality-api)
* [Geocoding](/en/docs/geocoding-api)
* [Elevation](/en/docs/elevation-api)
* [Flood](/en/docs/flood-api)

## Location and Time

* Location:
* Coordinates
* List
  Latitude   Longitude  America/AnchorageAmerica/Los\_AngelesAmerica/DenverAmerica/ChicagoAmerica/New\_YorkAmerica/Sao\_PauloNot set (GMT+0)GMT+0Automatically detect time zoneEurope/LondonEurope/BerlinEurope/MoscowAfrica/CairoAsia/BangkokAsia/SingaporeAsia/TokyoAustralia/SydneyPacific/Auckland Timezone   Search

* Time:
* Forecast Length
* Time Interval
 1 day3 days5 days (default)7 days Forecast days 0 (default)12351 week2 weeks1 month2 months3 months Past days
## Hourly Air Quality Variables

 Particulate Matter PM10  Particulate Matter PM2.5  Carbon Monoxide CO  Carbon Dioxide CO2  Nitrogen Dioxide NO2  Sulphur Dioxide SO2  Ozone O3   Aerosol Optical Depth  Dust  UV Index  UV Index Clear Sky  Ammonia NH3 (\*)  Methane CH4   Alder Pollen (\*)  Birch Pollen (\*)  Grass Pollen (\*)  Mugwort Pollen (\*)  Olive Pollen (\*)  Ragweed Pollen (\*)   \* Only available in Europe during pollen season with 4 days forecast
## European Air Quality Index

## United States Air Quality Index

## Additional Variables and Options

## Current Conditions

 European AQI  United States AQI  Particulate Matter PM10  Particulate Matter PM2.5  Carbon Monoxide CO  Nitrogen Dioxide NO2  Sulphur Dioxide SO2  Ozone O3   Aerosol Optical Depth  Dust  UV Index  UV Index Clear Sky  Ammonia NH3 (\*)   Alder Pollen (\*)  Birch Pollen (\*)  Grass Pollen (\*)  Mugwort Pollen (\*)  Olive Pollen (\*)  Ragweed Pollen (\*)
## Settings

Global + EuropeanGlobal (40 km)European (11 km) Domain ISO 8601 (e.g. 2022-12-31)Unix timestamp Timeformat

* Usage License:
* Non-Commercial
* Commercial
* Self-Hosted
 Only for **non-commercial use** and less than 10.000 daily API calls. See [Terms](/en/terms) for more details.
## API Response

* Preview:
* Chart And URL
* Python
* Typescript
* Swift
* Other
  Loading...  [Download XLSX](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5&format=xlsx) [Download CSV](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5&format=csv) API URL ([Open in new tab](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5) or copy this
URL into your application).

## Data Sources

Forecast is based on the 11 kilometer CAMS European air quality forecast
and the 40 kilometer
CAMS global atmospheric composition forecasts. The European and global domain are not coupled and may show different forecasts.

You can find the update timings in the [model updates documentation](/en/docs/model-updates).
| Data Set | Region | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency |
| --- | --- | --- | --- | --- | --- |
| [CAMS European Air Quality Forecast](https://ads.atmosphere.copernicus.eu/datasets/cams-europe-air-quality-forecasts?tab=overview) | Europe | 0.1° (~11 km) | 1-Hourly | October 2023 onwards | Every 24 hours, 4 days forecast |
| [CAMS European Air Quality Reanalysis](https://ads.atmosphere.copernicus.eu/datasets/cams-europe-air-quality-reanalyses?tab=overview) | Europe | 0.1° (~11 km) | Hourly | 2013 onwards | - |
| [CAMS global atmospheric composition forecasts](https://ads.atmosphere.copernicus.eu/datasets/cams-global-atmospheric-composition-forecasts?tab=overview) | Global | 0.25° (~25 km) | 3-Hourly | August 2022 onwards | Every 12 hours, 5 days forecast |
| [CAMS Global Greenhouse Gas Forecast](https://ads.atmosphere.copernicus.eu/datasets/cams-global-greenhouse-gas-forecasts?tab=overview) | Global | 0.1° (~11 km) | 3-Hourly | November 2024 onwards | Every 24 hours, 5 days forecast |

## API Documentation

The API endpoint /v1/air-quality accepts a geographical coordinate, a list of weather
variables and responds with a JSON hourly air quality forecast for 5 days. Time always starts at
0:00 today.

All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitude, longitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. |
| hourly | String array | No |  | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |
| current | String array | No |  | A list of variables to get current conditions. |
| domains | String | No | auto | Automatically combine both domains auto or specifically select the European cams\_europe or global domain cams\_global. |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc\_offset\_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified. |
| past\_days | Integer (0-92) | No | 0 | If past\_days is set, yesterday or the day before yesterday data are also returned. |
| forecast\_days | Integer (0-7) | No | 5 | Per default, 5 days are returned. Up to 7 days of forecast are possible. |
| forecast\_hourspast\_hours | Integer (>0) | No |  | Similar to forecast\_days, the number of timesteps of hourly data can controlled. Instead of using the current day as a reference, the current hour is used. |
| start\_dateend\_date | String (yyyy-mm-dd) | No |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). |
| start\_hourend\_hour | String (yyyy-mm-ddThh:mm) | No |  | The time interval to get weather data for hourly data. Time must be specified as an ISO8601 date (e.g. 2022-06-30T12:00). |
| cell\_selection | String | No | nearest | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given
as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
from the preceding hour as an average or sum.

| Variable | Valid time | Unit | Description |
| --- | --- | --- | --- |
| pm10pm2\_5 | Instant | μg/m³ | Particulate matter with diameter smaller than 10 µm (PM10) and smaller than 2.5 µm (PM2.5) close to surface (10 meter above ground) |
| carbon\_monoxidenitrogen\_dioxidesulphur\_dioxideozone | Instant | μg/m³ | Atmospheric gases close to surface (10 meter above ground) |
| carbon\_dioxide | Instant | ppm | CO2 close to surface (10 meter above ground) |
| ammonia | Instant | μg/m³ | Ammonia concentration. Only available for Europe. |
| aerosol\_optical\_depth | Instant | Dimensionless | Aerosol optical depth at 550 nm of the entire atmosphere to indicate haze. |
| methane | Instant | μg/m³ | Methane close to surface (10 meter above ground) |
| dust | Instant | μg/m³ | Saharan dust particles close to surface level (10 meter above ground). |
| uv\_indexuv\_index\_clear\_sky | Instant | Index | UV index considering clouds and clear sky. See [ECMWF UV Index recommendation](https://confluence.ecmwf.int/display/CUSF/CAMS%2Bglobal%2BUV%2Bindex) for more information |
| alder\_pollenbirch\_pollengrass\_pollenmugwort\_pollenolive\_pollenragweed\_pollen | Instant | Grains/m³ | Pollen for various plants. Only available in Europe as provided by CAMS European Air Quality forecast. |
| european\_aqieuropean\_aqi\_pm2\_5european\_aqi\_pm10european\_aqi\_nitrogen\_dioxideeuropean\_aqi\_ozoneeuropean\_aqi\_sulphur\_dioxide | Instant | European AQI | European Air Quality Index (AQI) calculated for different particulate matter and gases individually. The consolidated european\_aqi returns the maximum of all individual indices. Ranges from 0-20 (good), 20-40 (fair), 40-60 (moderate), 60-80 (poor), 80-100 (very poor) and exceeds 100 for extremely poor conditions. |
| us\_aqius\_aqi\_pm2\_5us\_aqi\_pm10us\_aqi\_nitrogen\_dioxideus\_aqi\_ozoneus\_aqi\_sulphur\_dioxideus\_aqi\_carbon\_monoxide | Instant | U.S. AQI | United States Air Quality Index (AQI) calculated for different particulate matter and gases individually. The consolidated us\_aqi returns the maximum of all individual indices. Ranges from 0-50 (good), 51-100 (moderate), 101-150 (unhealthy for sensitive groups), 151-200 (unhealthy), 201-300 (very unhealthy) and 301-500 (hazardous). |

### JSON Return Object

On success a JSON object will be returned.

```

  "latitude": 52.52,
  "longitude": 13.419,
  "elevation": 44.812,
  "generationtime_ms": 2.2119,
  "utc_offset_seconds": 0,
  "timezone": "Europe/Berlin",
  "timezone_abbreviation": "CEST",
  "hourly": {
    "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", ...],
    "pm10": [1, 1.7, 1.7, 1.5, 1.5, 1.8, 2.0, 1.9, 1.3, ...]
  },
  "hourly_units": {
    "pm10": "μg/m³"
  },

```

| Parameter | Format | Description |
| --- | --- | --- |
| latitude, longitude | Floating point | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometers away from the requested coordinate. |
| generationtime\_ms | Floating point | Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements. |
| utc\_offset\_seconds | Integer | Applied timezone offset from the &timezone= parameter. |
| timezonetimezone\_abbreviation | String | Timezone identifier (e.g. Europe/Berlin) and abbreviation (e.g. CEST) |
| hourly | Object | For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| hourly\_units | Object | For each selected weather variable, the unit will be listed here. |

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error": true,
  "reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"

```
## Citation & Acknowledgement

METEO FRANCE, Institut national de l'environnement industriel et des risques (Ineris), Aarhus
University, Norwegian Meteorological Institute (MET Norway), Jülich Institut für Energie- und
Klimaforschung (IEK), Institute of Environmental Protection – National Research Institute
(IEP-NRI), Koninklijk Nederlands Meteorologisch Instituut (KNMI), Nederlandse Organisatie voor
toegepast-natuurwetenschappelijk onderzoek (TNO), Swedish Meteorological and Hydrological
Institute (SMHI), Finnish Meteorological Institute (FMI), Italian National Agency for New
Technologies, Energy and Sustainable Economic Development (ENEA) and Barcelona Supercomputing
Center (BSC) (2022): CAMS European air quality forecasts, ENSEMBLE data. Copernicus Atmosphere
Monitoring Service (CAMS) Atmosphere Data Store (ADS). (Updated twice daily).

All users of Open-Meteo data must provide a clear attribution to [CAMS ENSEMBLE data provider](https://confluence.ecmwf.int/display/CKB/CAMS%2BRegional%3A%2BEuropean%2Bair%2Bquality%2Banalysis%2Band%2Bforecast%2Bdata%2Bdocumentation%5C#CAMSRegional:Europeanairqualityanalysisandforecastdatadocumentation-Howtoacknowledge,citeandrefertothedata) as well as a reference to Open-Meteo.

Open-Meteo

* [Features](/en/features)
* [Pricing](/en/pricing)
* [About us & Contact](/en/about)
* [License](/en/license)
* [Terms & Privacy](/en/terms)

Weather APIs

* [Weather Forecast API](/en/docs)
* [Historical Weather API](/en/docs/historical-weather-api)
* [ECMWF API](/en/docs/ecmwf-api)
* [GFS & HRRR Forecast API](/en/docs/gfs-api)
* [Météo-France API](/en/docs/meteofrance-api)
* [DWD ICON API](/en/docs/dwd-api)
* [GEM API](/en/docs/gem-api)
* [JMA API](/en/docs/jma-api)
* [Met Norway API](/en/docs/metno-api)

Other APIs

* [Ensemble API](/en/docs/ensemble-api)
* [Climate Change API](/en/docs/climate-api)
* [Marine Weather API](/en/docs/marine-weather-api)
* [Air Quality API](/en/docs/air-quality-api)
* [Geocoding API](/en/docs/geocoding-api)
* [Elevation API](/en/docs/elevation-api)
* [Flood API](/en/docs/flood-api)

External

* [GitHub](https://github.com/open-meteo/open-meteo)
* [Blog](https://openmeteo.substack.com/archive?sort=new)
* [Twitter](https://twitter.com/open_meteo)
* [Mastodon](https://fosstodon.org/%40openmeteo)
* [Service status and uptime](https://status.open-meteo.com)
* [Model Updates Overview](/en/docs/model-updates)
 © 2022-2025 Copyright: Open-Meteo.com

