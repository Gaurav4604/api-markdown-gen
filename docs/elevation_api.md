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

# Elevation API

90 meter resolution digital elevation model

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
  Get more information on how weather forecasts are improved with elevation models in our [blog article](https://openmeteo.substack.com/p/87a094f1-325d-497a-8a9d-4d16b794fd15).

## Select Coordinates or City

Latitude Longitude Search Locations ...

- Usage License:
- Non-Commercial
- Commercial
- Self-Hosted
  Only for **non-commercial use** and less than 10.000 daily API calls. See [Terms](/en/terms) for more details. Preview {"elevation":[38.0]} API URL ([Open in new tab](https://api.open-meteo.com/v1/elevation?latitude=52.52&longitude=13.41)) You can copy this API URL into your application

## API Documentation

The API endpoint /v1/elevation accepts one or multiple geographical coordinate and returns
the terrain elevation for those points.

Data is based on the [Copernicus DEM 2021 release GLO-90](https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model) with 90 meters resolution. The GLO-90 dataset is available worldwide with a free license.

All URL parameters are listed below:

| Parameter           | Format               | Required | Default | Description                                                                                                                                                                                                                                                           |
| ------------------- | -------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| latitude, longitude | Floating point array | Yes      |         | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma , separated. Up to 100 coordinates can be requested at once. Example for [multiple coordinates](https://api.open-meteo.com/v1/elevation?latitude=52.52,48.85&longitude=13.41,2.35). |
| apikey              | String               | No       |         | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information.                              |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### JSON Return Object

On success a JSON object is returned with just one attribute elevation. It is
always an array, even if only one coordinate is requested.

```

  "elevation": [38.0]

```

### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error":true,
  "reason":"Latitude must be in range of -90 to 90°. Given: 522.52."

```

## Citation & Acknowledgement

```
ESA - EUsers, who, in their research, use the Copernicus DEM, are requested to use the following DOI when citing the data source in their publications:

https://doi.org/10.5270/ESA-c5d3d65

```

All users of Open-Meteo data must provide a clear attribution to the Copernicus program as well as
a reference to Open-Meteo.

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
