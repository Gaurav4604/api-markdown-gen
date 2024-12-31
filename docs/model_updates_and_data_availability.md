---
date: 2024-11-11
hostname: open-meteo.com
sitename: Open-Meteo.com
title: Model Updates and Data Availability
url: https://open-meteo.com/en/docs/status
---

## Model Updates

This page offers a brief overview of all models integrated into Open-Meteo. These models are typically updated every few hours. Open-Meteo aims to download and process the data as soon as it becomes available, immediately after it is released by national weather services.

Open-Meteo operates with geographically distributed and redundant servers. Data across all
Open-Meteo servers is [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency), meaning there may be instances where the API indicates a weather model has been updated,
but not all servers have been fully updated yet. If you need access to the most recent
forecast, it's recommended to wait an additional 10 minutes after the forecast update has
been applied.

Models with a delay exceeding 20 minutes are highlighted in yellow. If multiple weather model updates are missed, the model is marked in red. Minor delays are fairly common.

To report a model issue, please open a ticket on [GitHub](https://github.com/open-meteo/open-meteo/issues). Commercial clients can contact us directly via email.

The free and commercial API services of Open-Meteo operate on different servers, leading to slight variations in update times. Please choose the appropriate type below. Note that API calls to the metadata API are not counted toward daily or monthly request limits.

## Forecast API

| Provider | Weather Model | Area | Last Model Run | Update Available | Temporal Resolution | Update frequency | API |
|---|---|---|---|---|---|---|---|
| AM ARPAE ARPAP | COSMO 5m | 2024-12-31 00z | 03:59z | 1 hourly | Every 12 h |
|

[Link](https://api.open-meteo.com/data/arpae_cosmo_2i/static/meta.json)[Link](https://api.open-meteo.com/data/bom_access_global/static/meta.json)[Link](https://api.open-meteo.com/data/cma_grapes_global/static/meta.json)[Link](https://api.open-meteo.com/data/cmc_gem_gdps/static/meta.json)[Link](https://api.open-meteo.com/data/cmc_gem_rdps/static/meta.json)[Link](https://api.open-meteo.com/data/cmc_gem_hrdps/static/meta.json)[Link](https://api.open-meteo.com/data/dmi_harmonie_arome_europe/static/meta.json)[Link](https://api.open-meteo.com/data/dwd_icon/static/meta.json)[Link](https://api.open-meteo.com/data/dwd_icon_eu/static/meta.json)[Link](https://api.open-meteo.com/data/dwd_icon_d2/static/meta.json)[Link](https://api.open-meteo.com/data/dwd_icon_d2_15min/static/meta.json)[Link](https://api.open-meteo.com/data/ecmwf_aifs025/static/meta.json)[Link](https://api.open-meteo.com/data/ecmwf_ifs025/static/meta.json)[Link](https://api.open-meteo.com/data/jma_gsm/static/meta.json)[Link](https://api.open-meteo.com/data/jma_msm/static/meta.json)[Link](https://api.open-meteo.com/data/knmi_harmonie_arome_europe/static/meta.json)[Link](https://api.open-meteo.com/data/knmi_harmonie_arome_netherlands/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arpege_world025/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arpege_europe/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arpege_europe_probabilities/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arome_france_hd/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arome_france_hd_15min/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arome_france0025/static/meta.json)[Link](https://api.open-meteo.com/data/meteofrance_arome_france0025_15min/static/meta.json)[Link](https://api.open-meteo.com/data/metno_nordic_pp/static/meta.json)[Link](https://api.open-meteo.com/data/ncep_gfs013/static/meta.json)[Link](https://api.open-meteo.com/data/ncep_gfs025/static/meta.json)[Link](https://api.open-meteo.com/data/ncep_gfs_graphcast025/static/meta.json)[Link](https://api.open-meteo.com/data/ncep_nbm_conus/static/meta.json)[Link](https://api.open-meteo.com/data/ncep_hrrr_conus/static/meta.json)[Link](https://api.open-meteo.com/data/ncep_hrrr_conus_15min/static/meta.json)[Link](https://api.open-meteo.com/data/ukmo_global_deterministic_10km/static/meta.json)[Link](https://api.open-meteo.com/data/ukmo_uk_deterministic_2km/static/meta.json)## Historical Weather API

| Provider | Weather Model | Area | Last Model Run | Update Available | Temporal Resolution | Update frequency | API |
|---|---|---|---|---|---|---|---|
| Copernicus | ERA5 0.25° | 2024-12-25 00z | 00:46z | 1 hourly | Every 24 h |
|

[Link](https://archive-api.open-meteo.com/data/copernicus_era5_land/static/meta.json)[Link](https://archive-api.open-meteo.com/data/copernicus_era5_ensemble/static/meta.json)[Link](https://archive-api.open-meteo.com/data/ecmwf_ifs/static/meta.json)[Link](https://archive-api.open-meteo.com/data/ecmwf_ifs_analysis_long_window/static/meta.json)## Ensemble API

| Provider | Weather Model | Area | Last Model Run | Update Available | Temporal Resolution | Update frequency | API |
|---|---|---|---|---|---|---|---|
| BOM | ACCESS-GE 0.4° | 2024-12-30 18z | 13:24z | 3 hourly | Every 6 h |
|

[Link](https://ensemble-api.open-meteo.com/data/cmc_gem_geps/static/meta.json)[Link](https://ensemble-api.open-meteo.com/data/dwd_icon_eps/static/meta.json)[Link](https://ensemble-api.open-meteo.com/data/dwd_icon_eu_eps/static/meta.json)[Link](https://ensemble-api.open-meteo.com/data/dwd_icon_d2_eps/static/meta.json)[Link](https://ensemble-api.open-meteo.com/data/ecmwf_ifs025_ensemble/static/meta.json)[Link](https://ensemble-api.open-meteo.com/data/ncep_gefs025/static/meta.json)[Link](https://ensemble-api.open-meteo.com/data/ncep_gefs05/static/meta.json)## Air Quality API

| Provider | Weather Model | Area | Last Model Run | Update Available | Temporal Resolution | Update frequency | API |
|---|---|---|---|---|---|---|---|
| CAMS | CAMS GLOBAL 0.4° | 2024-12-31 00z | 09:10z | 1 hourly | Every 12 h |
|

[Link](https://air-quality-api.open-meteo.com/data/cams_europe/static/meta.json)[Link](https://air-quality-api.open-meteo.com/data/cams_global_greenhouse_gases/static/meta.json)## Marine API

| Provider | Weather Model | Area | Last Model Run | Update Available | Temporal Resolution | Update frequency | API |
|---|---|---|---|---|---|---|---|
| Météo-France | MFWAM 0.08° | 2024-12-31 00z | 12:04z | 3 hourly | Every 12 h |
|

[Link](https://marine-api.open-meteo.com/data/meteofrance_currents/static/meta.json)[Link](https://marine-api.open-meteo.com/data/ecmwf_wam025/static/meta.json)[Link](https://marine-api.open-meteo.com/data/ncep_gfswave025/static/meta.json)[Link](https://marine-api.open-meteo.com/data/ncep_gfswave016/static/meta.json)[Link](https://marine-api.open-meteo.com/data/copernicus_era5_ocean/static/meta.json)## Metadata API Documentation

You can retrieve the update times for each individual model via the API. However, these times do not directly correlate with the update times in the Forecast API, as Open-Meteo automatically selects the most appropriate weather model for each location (referred to as "Best Match"). The table above provides an API link for each model, returning a JSON object with the following fields:

**last_run_initialisation_time:**The model's initialization time or reference time represented as a Unix timestamp (e.g., 1724796000 for Tue Aug 27, 2024, 22:00:00 GMT+0000).**last_run_modification_time:**The time when the data download and conversion were completed, which does not indicate when the data became available on the API.**last_run_availability_time:**The time when the data is actually accessible on the API server. Important: Open-Meteo utilizes multiple redundant API servers, so there may be slight differences between them while the data is being copied. To ensure all API calls use the most recent data, please wait 10 minutes after the availability time.**temporal_resolution_seconds:**The temporal resolution of the model in seconds. By default, the API interpolates the data to a 1-hour resolution. However, the underlying model may only provide data in 3 or 6-hourly steps. A value of 3600 indicates that the data is 1-hourly.**update_interval_seconds:**The typical time interval between model updates, such as 3600 seconds for a model that updates every hour.

Additional attributes, such as spatial resolution, area, grid systems, and more, will be added in the future.