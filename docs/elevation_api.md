---
api-endpoint: https://api.open-meteo.com/v1/elevation
date: 2024-01-01
description: Get detailed elevation information for any set of coordinates using our
  digital elevation model. With impressive resolution up to 90 meters, gain valuable
  insights into terrain and elevation variations for different geographic points.
  Enhance your understanding and analysis of topography with our reliable elevation
  data.
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Elevation API
url: https://open-meteo.com/en/docs/elevation-api
---

[blog article](https://openmeteo.substack.com/p/87a094f1-325d-497a-8a9d-4d16b794fd15).

## API Documentation

The API endpoint /v1/elevation accepts one or multiple geographical coordinate and returns the terrain elevation for those points.

Data is based on the [Copernicus DEM 2021 release GLO-90](https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model) with 90 meters resolution. The GLO-90 dataset is available worldwide with a free license.

All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| latitude longitude | Floating point array | Yes | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma ,
separated. Up to 100 coordinates can be requested at once. Example for
|

[pricing](https://open-meteo.com/en/pricing)for more information.### JSON Return Object

On success a JSON object is returned with just one attribute elevation. It is always an array, even if only one coordinate is requested.

` ````
"elevation": [38.0]
```


### Errors

` ````
"error":true,
"reason":"Latitude must be in range of -90 to 90°. Given: 522.52."
```


## Citation & Acknowledgement

ESA - EUsers, who, in their research, use the Copernicus DEM, are requested to use the following DOI when citing the data source in their publications: https://doi.org/10.5270/ESA-c5d3d65

All users of Open-Meteo data must provide a clear attribution to the Copernicus program as well as a reference to Open-Meteo.