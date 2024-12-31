---
api-endpoint: https://geocoding-api.open-meteo.com/v1/search
date: 2024-01-01
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Geocoding API
url: https://open-meteo.com/en/docs/geocoding-api
---

## Preview and API URL

| Name | Latitude | Longitude | Elevation | Population | Admin1 | Admin2 | Admin3 | Admin4 | Feature code | |
|---|---|---|---|---|---|---|---|---|---|---|
| Berlin | 52.52437 | 13.41053 | 74 | 3426354 | Land Berlin | Berlin, Stadt | Berlin | PPLC | ||
| Berlin | 44.46867 | -71.18508 | 311 | 9367 | New Hampshire | Coos | City of Berlin | PPL | ||
| Berlin | 39.79123 | -74.92905 | 50 | 7590 | New Jersey | Camden | Borough of Berlin | PPL | ||
| Berlin | 43.96804 | -88.94345 | 246 | 5420 | Wisconsin | Green Lake | City of Berlin | PPL | ||
| Berlin | 38.32262 | -75.21769 | 11 | 4529 | Maryland | Worcester | PPL | |||
| Berlin | 42.3812 | -71.63701 | 100 | 2422 | Massachusetts | Worcester | Town of Berlin | PPL | ||
| Berlin | 39.92064 | -78.9578 | 710 | 2019 | Pennsylvania | Somerset | Borough of Berlin | PPL | ||
| East Berlin | 39.9376 | -76.97859 | 131 | 1534 | Pennsylvania | Adams | Borough of East Berlin | PPL | ||
| Berlin | 40.56117 | -81.7943 | 391 | 898 | Ohio | Holmes | Berlin Township | PPL | ||
| Berlin | 54.00603 | 61.19308 | 228 | 613 | Chelyabinsk | Troitskiy Rayon | PPL |

## API Documentation

The API endpoint https://geocoding-api.open-meteo.com/v1/search accepts a search term and returns a list of matching locations. URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
|---|---|---|---|---|
| name | String | Yes | String to search for. An empty string or only 1 character will return an empty result. 2 characters will only match exact matching locations. 3 and more characters will perform fuzzy matching. The search string can be a location name or a postal code. | |
| count | Integer | No | 10 | The number of search results to return. Up to 100 results can be retrieved. |
| format | String | No | json | By default, results are returned as JSON. Alternatively, protobuf is
supported for more efficient encoding and transfer. The .proto file to decode the
protobuf message is available in the
|

[pricing](https://open-meteo.com/en/pricing)for more information.### JSON Return Object

On success a JSON object will be returned. Empty fields are not returned. E.g. admin4 will be missing if no fourth administrative level is available.

` ````
"results": [
{
"id": 2950159,
"name": "Berlin",
"latitude": 52.52437,
"longitude": 13.41053,
"elevation": 74.0,
"feature_code": "PPLC",
"country_code": "DE",
"admin1_id": 2950157,
"admin2_id": 0,
"admin3_id": 6547383,
"admin4_id": 6547539,
"timezone": "Europe/Berlin",
"population": 3426354,
"postcodes": [
"10967",
"13347"
],
"country_id": 2921044,
"country": "Deutschland",
"admin1": "Berlin",
"admin2": "",
"admin3": "Berlin, Stadt",
"admin4": "Berlin"
},
{
...
}]
```


| Parameter | Format | Description |
|---|---|---|
| id | Integer | Unique ID for this location |
| name | String | Location name. Localized following the &language= parameter, if possible |
| latitude, longitude | Floating point | Geographical WGS84 coordinates of this location |
| elevation | Floating point | Elevation above mean sea level of this location |
| timezone | String | Time zone using
|

[GeoNames feature_code definition](https://www.geonames.org/export/codes.html)[country code](https://en.wikipedia.org/wiki/List_of_FIPS_country_codes). E.g. DE for Germany[https://geocoding-api.open-meteo.com/v1/get?id=2950159](https://geocoding-api.open-meteo.com/v1/get?id=2950159)

### Errors

` ````
"error": true,
"reason": "Parameter count must be between 1 and 100."
```