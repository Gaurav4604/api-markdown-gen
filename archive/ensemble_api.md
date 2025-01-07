
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

# Ensemble API

Hundreds Of Weather Forecasts, Every time, Everywhere, All at Once

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
  The initial version of ensemble weather models has been integrated. You can learn more about these
models in the [blog article](https://openmeteo.substack.com/p/ensemble-weather-forecast-api).
## Location and Time

* Location:
* Coordinates
* List
  Latitude   Longitude  America/AnchorageAmerica/Los\_AngelesAmerica/DenverAmerica/ChicagoAmerica/New\_YorkAmerica/Sao\_PauloNot set (GMT+0)GMT+0Automatically detect time zoneEurope/LondonEurope/BerlinEurope/MoscowAfrica/CairoAsia/BangkokAsia/SingaporeAsia/TokyoAustralia/SydneyPacific/Auckland Timezone   Search

* Time:
* Forecast Length
* Time Interval
 1 day3 days7 days (default)14 days16 days30 days35 days Forecast days 0 (default)12351 week2 weeks1 month2 months3 months Past days
## Ensemble Models

 DWD ICON EPS Seamless  DWD ICON EPS Global  DWD ICON EPS EU  DWD ICON EPS D2   GFS Ensemble Seamless  GFS Ensemble 0.25  GFS Ensemble 0.5   ECMWF IFS 0.4° Ensemble  ECMWF IFS 0.25° Ensemble  GEM Global Ensemble  BOM ACCESS Global
## Hourly Weather Variables

 Temperature (2 m)  Relative Humidity (2 m)  Dewpoint (2 m)  Apparent Temperature  Precipitation (rain + snow)  Rain  Snowfall  Snow Depth   Weather code  Sealevel Pressure  Surface Pressure  Cloud cover Total  Visibility  Reference Evapotranspiration (ET₀)  Vapour Pressure Deficit   Wind Speed (10 m)  Wind Speed (80 m)  Wind Speed (120 m)  Wind Direction (10 m)  Wind Direction (80 m)  Wind Direction (120 m)  Wind Gusts (10 m)  Temperature (80 m)  Temperature (120 m)   Surface Temperature  Soil Temperature (0-10 cm)  Soil Temperature (10-40 cm)  Soil Temperature (40-100 cm)  Soil Temperature (100-200 cm)  Soil Moisture (0-10 cm)  Soil Moisture (10-40 cm)  Soil Moisture (40-100 cm)  Soil Moisture (100-400 cm)
## Additional Variables And Options

## Solar Radiation Variables

## Settings

Celsius °CFahrenheit °F Temperature Unit Km/hm/sMphKnots Wind Speed Unit MillimeterInch Precipitation Unit ISO 8601 (e.g. 2022-12-31)Unix timestamp Timeformat

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
  Loading...  [Download XLSX](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=icon_seamless&format=xlsx) [Download CSV](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=icon_seamless&format=csv) API URL ([Open in new tab](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=icon_seamless) or copy this
URL into your application).

Note: This API call is equivalent to **4.0** calls because of factors like long time intervals, the number of locations, variables, or models involved.

## Data Source

Ensemble models are a type of weather forecasting technique that use multiple members or
versions of a model to produce a range of possible outcomes for a given forecast. Each member is
initialized with slightly different initial conditions and/or model parameters to account for
uncertainties and variations in the atmosphere, resulting in a set of perturbed forecasts.

By combining the perturbed forecasts, the ensemble model generates a probability distribution of
possible outcomes, indicating not only the most likely forecast but also the range of possible
outcomes and their likelihoods. This probabilistic approach provides more comprehensive and
accurate forecast guidance, especially for high-impact weather events where uncertainties are
high.

Different national weather services calculate ensemble models, each with varying resolutions of
weather variables and forecast time-range. For instance, the German weather service DWD's ICON
model provides exceptionally high resolution for Europe but only forecasts up to 7 days.
Meanwhile, the GFS model can forecast up to 35 days, albeit at a lower resolution of 50 km. The
appropriate ensemble model to use would depend on the forecast horizon and region of interest.

You can find the update timings in the [model updates documentation](/en/docs/model-updates).

| National Weather Service | Weather Model | Region | Resolution | Members | Forecast Length | Update frequency |
| --- | --- | --- | --- | --- | --- | --- |
| Deutscher Wetterdienst (DWD) | ICON-D2-EPS | Central Europe | 2 km, hourly | 20 | 2 days | Every 3 hours |
| ICON-EU-EPS | Europe | 13 km, hourly | 40 | 5 days | Every 6 hours |
| ICON-EPS | Global | 26 km, hourly | 40 | 7.5 days | Every 12 hours |
| NOAA | GFS Ensemble 0.25° | Global | 25 km, 3-hourly | 31 | 10 days | Every 6 hours |
| GFS Ensemble 0.5° | Global | 50 km, 3-hourly | 31 | 35 days | Every 6 hours |
| ECMWF | IFS 0.4° | Global | 44 km, 3-hourly | 51 | 15 days | Every 6 hours |
| IFS 0.25° | Global | 25 km, 3-hourly | 51 | 15 days | Every 6 hours |
| Canadian Weather Service | GEM | Global | 25 km, 3-hourly | 21 | 16 days (32 days every thursday) | Every 12 hours |
| Australian Bureau of Meteorology (BOM) | ACCESS-GE | Global | 40 km, 3-hourly | 18 | 10 days | Every 6 hours |

To ensure ease of use, all data is interpolated to a 1-hourly time-step resolution. As the
forecast horizon extends further into the future, some ensemble models may reduce the time
resolution to 6-hourly intervals.

## API Documentation

The API endpoint /v1/ensemble accepts a geographical coordinate, a list of weather variables
and responds with a JSON hourly weather forecast for 7 days for each ensemble member. Time always starts
at 0:00 today. All URL parameters are listed below:

| Parameter | Format | Required | Default | Description |
| --- | --- | --- | --- | --- |
| latitude, longitude | Floating point | Yes |  | Geographical WGS84 coordinates of the location. Multiple coordinates can be comma separated. E.g. &latitude=52.52,48.85&longitude=13.41,2.35. To return data for multiple locations the JSON output changes to a list of structures. CSV and XLSX formats add a column location\_id. |
| models | String array | Yes |  | Select one or more ensemble weather models as comma-separated list |
| elevation | Floating point | No |  | The elevation used for statistical downscaling. Per default, a [90 meter digital elevation model is used](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). You can manually set the elevation to correctly match mountain peaks. If &elevation=nan is specified, downscaling will be disabled and the API uses the average grid-cell height. For multiple locations, elevation can also be comma separated. |
| hourly | String array | No |  | A list of weather variables which should be returned. Values can be comma separated, or multiple &hourly= parameter in the URL can be used. |
| temperature\_unit | String | No | celsius | If fahrenheit is set, all temperature values are converted to Fahrenheit. |
| wind\_speed\_unit | String | No | kmh | Other wind speed speed units: ms, mph and kn |
| precipitation\_unit | String | No | mm | Other precipitation amount units: inch |
| timeformat | String | No | iso8601 | If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. Please note that all timestamp are in GMT+0! For daily values with unix timestamps, please apply utc\_offset\_seconds again to get the correct date. |
| timezone | String | No | GMT | If timezone is set, all timestamps are returned as local-time and data is returned starting at 00:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. If auto is set as a time zone, the coordinates will be automatically resolved to the local time zone. For multiple coordinates, a comma separated list of timezones can be specified. |
| past\_days | Integer | No | 0 | If past\_days is set, past weather data can be returned. |
| forecast\_days | Integer (0-35) | No | 7 | Per default, only 7 days are returned. Up to 35 days of forecast are possible. |
| forecast\_hoursforecast\_minutely\_15past\_hourspast\_minutely\_15 | Integer (>0) | No |  | Similar to forecast\_days, the number of timesteps of hourly and 15-minutely data can controlled. Instead of using the current day as a reference, the current hour or the current 15-minute time-step is used. |
| start\_dateend\_date | String (yyyy-mm-dd) | No |  | The time interval to get weather data. A day must be specified as an ISO8601 date (e.g. 2022-06-30). |
| start\_hourend\_hourstart\_minutely\_15end\_minutely\_15 | String (yyyy-mm-ddThh:mm) | No |  | The time interval to get weather data for hourly or 15 minutely data. Time must be specified as an ISO8601 date (e.g. 2022-06-30T12:00). |
| cell\_selection | String | No | land | Set a preference how grid-cells are selected. The default land finds a suitable grid-cell on land with [similar elevation to the requested coordinates using a 90-meter digital elevation model](https://openmeteo.substack.com/p/improving-weather-forecasts-with "Elevation based grid-cell selection explained"). sea prefers grid-cells on sea. nearest selects the nearest possible grid-cell. |
| apikey | String | No |  | Only required to commercial use to access reserved API resources for customers. The server URL requires the prefix customer-. See [pricing](/en/pricing "Pricing information to use the weather API commercially") for more information. |

Additional optional URL parameters will be added. For API stability, no required parameters will
be added in the future!

### Hourly Parameter Definition

The parameter &hourly= accepts the following values. Most weather variables are given
as an instantaneous value for the indicated hour. Some variables like precipitation are calculated
from the preceding hour as an average or sum.

| Variable | Valid time | Unit | Description |
| --- | --- | --- | --- |
| temperature\_2m | Instant | °C (°F) | Air temperature at 2 meters above ground |
| relative\_humidity\_2m | Instant | % | Relative humidity at 2 meters above ground |
| dew\_point\_2m | Instant | °C (°F) | Dew point temperature at 2 meters above ground |
| apparent\_temperature | Instant | °C (°F) | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity and solar radiation |
| pressure\_mslsurface\_pressure | Instant | hPa | Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation. |
| cloud\_cover | Instant | % | Total cloud cover as an area fraction |
| wind\_speed\_10mwind\_speed\_80mwind\_speed\_120m | Instant | km/h (mph, m/s, knots) | Wind speed at 10, 80 or 120 meters above ground. Wind speed on 10 meters is the standard level. |
| wind\_direction\_10mwind\_direction\_80mwind\_direction\_120m | Instant | ° | Wind direction at 10, 80 or 120 meters above ground |
| wind\_gusts\_10m | Preceding hour max | km/h (mph, m/s, knots) | Gusts at 10 meters above ground as a maximum of the preceding hour |
| shortwave\_radiation | Preceding hour mean | W/m² | Shortwave solar radiation as average of the preceding hour. This is equal to the total global horizontal irradiation |
| direct\_radiationdirect\_normal\_irradiance | Preceding hour mean | W/m² | Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane (perpendicular to the sun). HRRR offers direct radiation directly. In GFS it is approximated based on [Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf) |
| diffuse\_radiation | Preceding hour mean | W/m² | Diffuse solar radiation as average of the preceding hour. HRRR offers diffuse radiation directly. In GFS it is approximated based on [Razo, Müller Witwer](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/36-eupvsec-2019/Guzman_5CV31.pdf) |
| global\_tilted\_irradiance | Preceding hour mean | W/m² | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. Please specify tilt and azimuth parameter. Tilt ranges from 0° to 90° and is typically around 45°. Azimuth should be close to 0° (0° south, -90° east, 90° west). If azimuth is set to "nan", the calculation assumes a horizontal tracker. If tilt is set to "nan", it is assumed that the panel has a vertical tracker. If both are set to "nan", a bi-axial tracker is assumed. |
| sunshine\_duration | Preceding hour sum | Seconds | Number of seconds of sunshine of the preceding hour per hour calculated by direct normalized irradiance exceeding 120 W/m², following the WMO definition. |
| vapour\_pressure\_deficit | Instant | kPa | Vapor Pressure Deificit (VPD) in kilopascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases |
| evapotranspiration | Preceding hour sum | mm (inch) | Evapotranspration from land surface and plants that weather models assumes for this location. Available soil water is considered. 1 mm evapotranspiration per hour equals 1 liter of water per spare meter. |
| et0\_fao\_evapotranspiration | Preceding hour sum | mm (inch) | ET₀ Reference Evapotranspiration of a well watered grass field. Based on [FAO-56 Penman-Monteith equations](https://www.fao.org/3/x0490e/x0490e04.htm) ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants. |
| weather\_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. Weather code is calculated from cloud cover analysis, precipitation, snowfall, cape, lifted index and gusts. |
| precipitation | Preceding hour sum | mm (inch) | Total precipitation (rain, showers, snow) sum of the preceding hour |
| snowfall | Preceding hour sum | cm (inch) | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent |
| rain | Preceding hour sum | mm (inch) | Liquid precipitation of the preceding hour in millimeter |
| weather\_code | Instant | WMO code | Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details. |
| snow\_depth | Instant | meters | Snow depth on the ground |
| freezing\_level\_height | Instant | meters | Altitude above sea level of the 0°C level |
| visibility | Instant | meters | Viewing distance in meters. Influenced by low clouds, humidity and aerosols. |
| cape | Instant | J/kg | Convective available potential energy. See [Wikipedia](https://en.wikipedia.org/wiki/Convective_available_potential_energy). |
| surface\_temperature | Instant | °C (°F) | Temperature of the top soil level |
| soil\_temperature\_0\_to\_10cmsoil\_temperature\_10\_to\_40cmsoil\_temperature\_40\_to\_100cmsoil\_temperature\_100\_to\_200cm | Instant | °C (°F) | Temperature in the soil as an average on 0-10, 10-40, 40-100 and 100-200 cm depths. |
| soil\_moisture\_0\_to\_10cmsoil\_moisture\_10\_to\_40cmsoil\_moisture\_40\_to\_100cmsoil\_moisture\_100\_to\_200cm | Instant | m³/m³ | Average soil water content as volumetric mixing ratio at 0-10, 10-40, 40-100 and 100-200 cm depths. |

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

