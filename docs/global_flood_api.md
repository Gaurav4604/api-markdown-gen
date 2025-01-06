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

# Global Flood API

Simulated river discharge at 5 km resolution from 1984 up to 7 months forecast

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

## Location and Time

- Location:
- Coordinates
- List
  Latitude Longitude America/AnchorageAmerica/Los_AngelesAmerica/DenverAmerica/ChicagoAmerica/New_YorkAmerica/Sao_PauloNot set (GMT+0)GMT+0Automatically detect time zoneEurope/LondonEurope/BerlinEurope/MoscowAfrica/CairoAsia/BangkokAsia/SingaporeAsia/TokyoAustralia/SydneyPacific/Auckland Timezone Search

- Time:
- Forecast Length
- Time Interval
  1 day7 days2 weeks1 month3 months (default)6 months Forecast days 0 (default)12351 week2 weeks1 month2 months3 months Past days

## Daily Weather Variables

River Discharge River Discharge Mean River Discharge Median River Discharge Maximum River Discharge Minimum River Discharge 25th Percentile River Discharge 75th Percentile All 50 Ensemble Members

Note: Statistical and ensemble forecasts are only available for forecasts.

## Flood Models

## Settings

ISO 8601 (e.g. 2022-12-31)Unix timestamp Timeformat

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
  Loading... [Download XLSX](https://flood-api.open-meteo.com/v1/flood?latitude=59.91&longitude=10.75&daily=river_discharge&format=xlsx) [Download CSV](https://flood-api.open-meteo.com/v1/flood?latitude=59.91&longitude=10.75&daily=river_discharge&format=csv) API URL ([Open in new tab](https://flood-api.open-meteo.com/v1/flood?latitude=59.91&longitude=10.75&daily=river_discharge) or copy this
  URL into your application).

## Data Source

This API uses reanalysis and forecast data from the [Global Flood Awareness System (GloFAS)](https://www.globalfloods.eu). Per default, GloFAS version 4 with seamless data from 1984 until 7 months of forecast is
used.

Please note: Due to the 5 km resolution the closest river might not be selected correctly.
Varying coordiantes by 0.1° can help to get a more representable discharge rate. The GloFAS
website provides additional maps to help understand how rivers are covered in this dataset.

| Weather Model                                                                                                | Region | Spatial Resolution | Temporal Resolution | Data Length       | Update frequency |
| ------------------------------------------------------------------------------------------------------------ | ------ | ------------------ | ------------------- | ----------------- | ---------------- |
| [GloFAS v4 Reanalysis](https://cds.climate.copernicus.eu/datasets/cems-glofas-historical?tab=overview)       | Global | 0.05° (~5 km)      | Daily               | 1984 - July 2022  | -                |
| [GloFAS v4 Forecast](https://cds.climate.copernicus.eu/datasets/cems-glofas-forecast?tab=overview)           | Global | 0.05° (~5 km)      | Daily               | 30 days forecast  | Daily            |
| [GloFAS v4 Seasonal Forecast](https://ewds.climate.copernicus.eu/datasets/cems-glofas-seasonal?tab=overview) | Global | 0.05° (~5 km)      | Daily               | 7 months forecast | Monthly          |
| [GloFAS v3 Reanalysis](https://ewds.climate.copernicus.eu/datasets/cems-glofas-historical?tab=overview)      | Global | 0.1° (~11 km)      | Daily               | 1984 - July 2022  | -                |
| [GloFAS v3 Forecast](https://ewds.climate.copernicus.eu/datasets/cems-glofas-forecast?tab=overview)          | Global | 0.1° (~11 km)      | Daily               | 30 days forecast  | Daily            |
| [GloFAS v3 Seasonal Forecast](https://ewds.climate.copernicus.eu/datasets/cems-glofas-seasonal?tab=overview) | Global | 0.1° (~11 km)      | Daily               | 7 months forecast | Monthly          |

## API Documentation

The API endpoint /v1/flood accepts a geographical coordinate and returns river discharge
data from the largest river in a 5 km area for the given coordinates. All URL parameters are listed
below:

| Parameter           | Format              | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | ------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| latitude, longitude | Floating point      | Yes      |         | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location_id.                                                                                                                 |
| daily               | String array        | No       |         | A list of weather variables which should be returned. Values can be comma separated, or multiple &daily= parameter in the URL can be used.                                                                                                                                                                                                                                                          |
| timeformat          | String              | No       | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all time is then in GMT+0!                                                                                                                                                                                                                                                             |
| past_days           | Integer             | No       | 0       | If past_days is set, past data can be returned.                                                                                                                                                                                                                                                                                                                                                     |
| forecast_days       | Integer (0-210)     | No       | 92      | Per default, only 92 days are returned. Up to 210 days of forecast are possible.                                                                                                                                                                                                                                                                                                                    |
| start_dateend_date  | String (yyyy-mm-dd) | No       |         | The time interval to get data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). Data are available from 1984-01-01 until 7 month forecast.                                                                                                                                                                                                                                             |
| ensemble            | Boolean             | No       |         | If True all forecast ensemble members will be returned                                                                                                                                                                                                                                                                                                                                              |
| cell_selection      | String              | No       | nearest | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey              | String              | No       |         | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information.                                                                                                                                                            |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### Daily Parameter Definition

The parameter &daily= accepts the following values:

| Variable                                                                                                                         | Unit | Description                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| river_discharge                                                                                                                  | m³/s | Daily river discharge rate in m³/s                                                                                                                  |
| river_discharge_mean, river_discharge_median, river_discharge_max, river_discharge_min, river_discharge_p25, river_discharge_p75 | m³/s | Statistical analysis from ensemble members for river discharge rate in m³/s. Only available for forecasts and not for consolidated historical data. |

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

| Parameter           | Format         | Description                                                                                                                                                          |
| ------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| latitude, longitude | Floating point | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be a few kilometers away from the requested coordinate. |
| generationtime_ms   | Floating point | Generation time of the weather forecast in milliseconds. This is mainly used for performance monitoring and improvements.                                            |
| daily               | Object         | For each selected weather variable, data will be returned as a floating point array. Additionally a time array will be returned with ISO8601 timestamps.             |
| daily_units         | Object         | For each selected weather variable, the unit will be listed here.                                                                                                    |

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error": true,
  "reason": "Cannot initialize WeatherVariable from invalid String value tempeture_2m for key hourly"

```

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
