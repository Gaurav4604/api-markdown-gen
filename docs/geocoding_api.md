
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

# Geocoding API

Search locations globally in any language

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

## Search for cities or postal code

 Name EnglishGermanFrenchSpanishItalianPortugueseRussianTurkishHindi Language 1102050100 Number of results jsonprotobuf Format

* Usage License:
* Non-Commercial
* Commercial
* Self-Hosted
 Only for **non-commercial use** and less than 10.000 daily API calls. See [Terms](/en/terms) for more details.
## Preview and API URL

Loading...  API URL ([Open in new tab](https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=10&language=en&format=json))  You can copy this API URL into your application
## API Documentation

The API endpoint https://geocoding-api.open-meteo.com/v1/search accepts a search term
and returns a list of matching locations. URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| name | String | Yes |  | String to search for. An empty string or only 1 character will return an empty result. 2 characters will only match exact matching locations. 3 and more characters will perform fuzzy matching. The search string can be a location name or a postal code. |
| count | Integer | No | 10 | The number of search results to return. Up to 100 results can be retrieved. |
| format | String | No | json | By default, results are returned as JSON. Alternatively, protobuf is supported for more efficient encoding and transfer. The .proto file to decode the protobuf message is available in the [geocoding GitHub repository](https://github.com/open-meteo/geocoding-api/blob/main/Sources/App/api.proto). |
| language | String | No | en | Return translated results, if available, otherwise return english or the native location name. Lower-cased. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### JSON Return Object

On success a JSON object will be returned. Empty fields are not returned. E.g. admin4 will be missing if no fourth administrative level is available.

```

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
| --- | --- | --- |
| id | Integer | Unique ID for this location |
| name | String | Location name. Localized following the &language= parameter, if possible |
| latitude, longitude | Floating point | Geographical WGS84 coordinates of this location |
| elevation | Floating point | Elevation above mean sea level of this location |
| timezone | String | Time zone using [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) definitions |
| feature\_code | String | Type of this location. Following the [GeoNames feature\_code definition](https://www.geonames.org/export/codes.html) |
| country\_code | String | 2-Character FIPS [country code](https://en.wikipedia.org/wiki/List_of_FIPS_country_codes). E.g. DE for Germany |
| country | String | Country name. Localized following the &language= parameter, if possible |
| country\_id | Integer | Unique ID for this country |
| population | Integer | Number of inhabitants |
| postcodes | String array | List of postcodes for this location |
| admin1, admin2, admin3, admin4 | String | Name of hierarchical administrative areas this location resides in. Admin1 is the first administrative level. Admin2 the second administrative level. Localized following the &language= parameter, if possible |
| admin1\_id, admin2\_id, admin3\_id, admin4\_id | Integer | Unique IDs for the administrative areas |

\*Note: All IDs can be can be resolved via the API endpoint<https://geocoding-api.open-meteo.com/v1/get?id=2950159>
### Errors

In case an error occurs, for example a URL parameter is not correctly specified, a JSON error
object is returned with a HTTP 400 status code.

```

  "error": true,
  "reason": "Parameter count must be between 1 and 100."

```

### Attribution

* Location data based on [GeoNames](https://www.geonames.org)
* Country flags from [HatScripts/circle-flags](https://github.com/HatScripts/circle-flags)

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

