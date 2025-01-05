
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

# Marine Weather API

Hourly wave forecasts at 5 km resolution

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
 1 day3 days5 days7 days (default)8 days10 days14 days16 days Forecast days 0 (default)12351 week2 weeks1 month2 months3 months Past days
## Hourly Marine Variables

 Wave Height  Wave Direction  Wave Period   Wind Wave Height  Wind Wave Direction  Wind Wave Period  Wind Wave Peak Period   Swell Wave Height  Swell Wave Direction  Swell Wave Period  Swell Wave Peak Period   Ocean Current Velocity  Ocean Current Direction

Note: Ocean currents consider Eulerian, Waves and Tides at 0.08° (~8 km) resolution. This is not suitable for small scale currents and does not replace your nautical almanac.

## Additional Variables And Options

## Wave Models

## Daily Marine Variables

 Wave Height Max  Wave Direction Dominant  Wave Period Max   Wind Wave Height Max  Wind Wave Direction Dominant  Wind Wave Period Max  Wind Wave Peak Period Max   Swell Wave Height Max  Swell Wave Direction Dominant  Swell Wave Period Max  Swell Wave Peak Period Max
## Current Conditions

 Wave Height  Wave Direction  Wave Period   Wind Wave Height  Wind Wave Direction  Wind Wave Period  Wind Wave Peak Period   Swell Wave Height  Swell Wave Direction  Swell Wave Period  Swell Wave Peak Period   Ocean Current Velocity  Ocean Current Direction
## Settings

MetricImperial Length Unit Km/hm/sMphKnots Velocity Unit ISO 8601 (e.g. 2022-12-31)Unix timestamp Timeformat

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
  Loading...  [Download XLSX](https://marine-api.open-meteo.com/v1/marine?latitude=54.544587&longitude=10.227487&hourly=wave_height&format=xlsx) [Download CSV](https://marine-api.open-meteo.com/v1/marine?latitude=54.544587&longitude=10.227487&hourly=wave_height&format=csv) API URL ([Open in new tab](https://marine-api.open-meteo.com/v1/marine?latitude=54.544587&longitude=10.227487&hourly=wave_height) or copy this
URL into your application).

## Data Sources

The Marine API combines wave models from different sources.

You can find the update timings in the [model updates documentation](/en/docs/model-updates).
| Data Set | Region |  | Spatial Resolution | Temporal Resolution | Data Availability | Update frequency |
| --- | --- | --- | --- | --- | --- | --- |
| [MeteoFrance MFWAM](https://data.marine.copernicus.eu/product/GLOBAL_ANALYSISFORECAST_WAV_001_027/description) | Global | [Map](https://data.marine.copernicus.eu/viewer/expert?view=viewer&crs=epsg%3A4326&z=0¢er=-23.399717243797422%2C42.59188729714914&zoom=10.52284658362573&layers=W3sib3BhY2l0eSI6MSwiaWQiOiJ0ZW1wMSIsImxheWVySWQiOiJHTE9CQUxfQU5BTFlTSVNGT1JFQ0FTVF9XQVZfMDAxXzAyNy9jbWVtc19tb2RfZ2xvX3dhdl9hbmZjXzAuMDgzZGVnX1BUM0gtaV8yMDIzMTEvVkhNMCIsInpJbmRleCI6MCwiaXNFeHBsb3JpbmciOnRydWUsImxvZ1NjYWxlIjpmYWxzZX1d&basemap=dark "Visualize as map") | 0.08° (~8 km) | 3-Hourly | October 2021 with 10 day forecast | Every 12 hours |
| [MeteoFrance SMOC Currents](https://data.marine.copernicus.eu/product/GLOBAL_ANALYSISFORECAST_PHY_001_024/services) | Global | [Map](https://data.marine.copernicus.eu/viewer/expert?view=viewer&crs=epsg%3A4326&z=-0.49402499198913574¢er=-12.433872193277338%2C42.88370285999325&zoom=11.872305323411199&layers=W3sib3BhY2l0eSI6MSwiaWQiOiJ0ZW1wMSIsImxheWVySWQiOiJHTE9CQUxfQU5BTFlTSVNGT1JFQ0FTVF9QSFlfMDAxXzAyNC9jbWVtc19tb2RfZ2xvX3BoeV9hbmZjX21lcmdlZC11dl9QVDFILWlfMjAyMjExL3VvIiwiekluZGV4IjowLCJpc0V4cGxvcmluZyI6dHJ1ZSwibG9nU2NhbGUiOmZhbHNlfV0%3D&basemap=dark "Visualize as map") | 0.08° (~8 km) | Hourly | January 2022 with 10 day forecast | Every 24 hours |
| [ECMWF WAM](https://www.ecmwf.int/en/elibrary/79883-wave-model) | Global |  | 0.25° (~25 km) | 3-Hourly | March 2024 with 10 day forecast | Every 6 hours |
| [NCEP GFS Wave](https://polar.ncep.noaa.gov/waves/index.php) | Global |  | 0.25° (~25 km) | Hourly | June 2024 with 16 day forecast | Every 6 hours |
| [NCEP GFS Wave](https://polar.ncep.noaa.gov/waves/index.php) | Latitude 52.5°N - 15°S |  | 0.16° (~16 km) | Hourly | October 2024 with 16 day forecast | Every 6 hours |
| [DWD GWAM](https://www.dwd.de/EN/specialusers/shipping/seegangsvorhersagesystem_en.html) | Europe |  | 0.05° (~5 km) | Hourly | August 2022 with 8 day forecast | Twice daily |
| [DWD EWAM](https://www.dwd.de/EN/specialusers/shipping/seegangsvorhersagesystem_en.html) | Global |  | 0.25° (~25 km) | Hourly | August 2022 with 4 day forecast | Twice daily |
| [ERA5-Ocean](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | Global |  | 0.5° (~50 km) | Hourly | 1940 to present | Daily with 5 days delay |

## API Documentation

The API endpoint /v1/marine accepts a geographical coordinate, a list of marine variables
and responds with a JSON hourly marine weather forecast for 7 days. Time always starts at 0:00 today.
All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitude, longitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. |
| hourly | String array | No |  | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |
| daily | String array | No |  | A list of daily weather variable aggregations which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used. If daily weather variables are specified, parameter timezone is required. |
| current | String array | No |  | A list of variables to get current conditions. |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc\_offset\_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified. |
| past\_days | Integer (0-92) | No | 0 | If past\_days is set, yesterday or the day before yesterday data are also returned. |
| forecast\_days | Integer (0-8) | No | 5 | Per default, 7 days are returned. Up to 8 days of forecast are possible. |
| forecast\_hourspast\_hours | Integer (>0) | No |  | Similar to forecast\_days, the number of timesteps of hourly data can controlled. Instead of using the current day as a reference, the current hour is used. |
| start\_dateend\_date | String (yyyy-mm-dd) | No |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). |
| start\_hourend\_hour | String (yyyy-mm-ddThh:mm) | No |  | The time interval to get weather data for hourly data. Time must be specified as an ISO8601 date (e.g. 2022-06-30T12:00). |
| length\_unit | String | No | metric | Options metric and imperial |
| cell\_selection | String | No | sea | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given
as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
from the preceding hour as an average or sum.

| Variable | Valid time | Unit | Description |
| --- | --- | --- | --- |
| wave\_heightwind\_wave\_heightswell\_wave\_height | Instant | Meter | Wave height of significant mean, wind and swell waves. Wave directions are always reported as the direction the waves come from. 0° = From north towards south; 90° = From east |
| wave\_directionwind\_wave\_directionswell\_wave\_direction | Instant | ° | Mean direction of mean, wind and swell waves |
| wave\_periodwind\_wave\_periodswell\_wave\_period | Instant | Seconds | Period between mean, wind and swell waves. |
| wind\_wave\_peak\_periodswell\_wave\_peak\_period | Instant | Seconds | Peak period between wind and swell waves. |
| ocean\_current\_velocity | Instant | km/h (mph, m/s, knots) | Velocity of ocean current considering Eulerian, Waves and Tides. |
| ocean\_current\_direction | Instant | ° | Direction following the flow of the current. E.g. where the current is heading towards. 0° = Going north; 90° = Towards east. |

### Daily Parameter Definition

Aggregations are a simple 24 hour aggregation from hourly values. The parameter &daily= accepts the following values:

| Variable | Unit | Description |
| --- | --- | --- |
| wave\_height\_maxwind\_wave\_height\_maxswell\_wave\_height\_max | Meter | Maximum wave height on a given day for mean, wind and swell waves |
| wave\_direction\_dominantwind\_wave\_direction\_dominantswell\_wave\_direction\_dominant | ° | Dominant wave direction of mean, wind and swell waves |
| wave\_period\_maxwind\_wave\_period\_maxswell\_wave\_period\_max | Seconds | Maximum wave period of mean, wind and swell |
| wind\_wave\_peak\_period\_maxswell\_wave\_peak\_period\_max | Seconds | Maximum peak period between wind and swell waves. |

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
    "wave_height": [1, 1.7, 1.7, 1.5, 1.5, 1.8, 2.0, 1.9, 1.3, ...]
  },
  "hourly_units": {
    "wave_height": "m"
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
| daily | Object | For each selected daily weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps. |
| daily\_units | Object | For each selected daily weather variable, the unit will be listed here. |

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error": true,
  "reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"

```
## Citation & Acknowledgement

Generated using ICON Wave forecast from the [German Weather Service DWD](https://www.dwd.de/EN/service/copyright/copyright_node.html).

All users of Open-Meteo data must provide a clear attribution to DWD as well as a reference to
Open-Meteo.

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

