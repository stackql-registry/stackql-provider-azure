--- 
title: weather
hide_title: false
hide_table_of_contents: false
keywords:
  - weather
  - maps_weather
  - azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure resources using SQL
custom_edit_url: null
image: /img/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>weather</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="weather" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps_weather.weather" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get_hourly_forecast"><CopyableCode code="get_hourly_forecast" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a detailed hourly weather forecast for up to 24 hours or a daily forecast for up to 10 days. The `Get Hourly Forecast` API is an HTTP `GET` that Request detailed weather forecast by the hour for the next 1, 12, 24 (1 day), 72 (3 days), 120 (5 days), and 240 hours (10 days) for the given the given coordinate location. The API returns details such as temperature, humidity, wind, precipitation, and ultraviolet (UV) index. For more information, see `Request hourly weather forecast data `__. If you are using the Gen1 S0 pricing tier, you can request hourly forecast for the next 1, 12, 24 hours (1 day), and 72 hours (3 days). If you are using Gen1 S1 or Gen2 pricing tier, you can also request hourly forecast for the next 120 (5 days) and 240 hours (10 days).</td>
</tr>
<tr>
    <td><a href="#get_minute_forecast"><CopyableCode code="get_minute_forecast" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a minute-by-minute forecast for the next 120 minutes in intervals of 1, 5 and 15 minutes. The `Get Minute Forecast` API is an HTTP `GET` request that returns minute-by-minute forecasts for a given location for the next 120 minutes. Users can request weather forecasts in intervals of 1, 5 and 15 minutes. The response will include details such as the type of precipitation (including rain, snow, or a mixture of both), start time, and precipitation intensity value (dBZ). For more information, see `Request minute-by-minute weather forecast data `__.</td>
</tr>
<tr>
    <td><a href="#get_quarter_day_forecast"><CopyableCode code="get_quarter_day_forecast" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a Quarter-Day Forecast for the next 1, 5, 10, or 15 days. The `Get Quarter-Day Forecast` API is an HTTP `GET` request that returns a detailed weather forecast by quarter-day for the next 1, 5, 10, or 15 days for a given location. Response data is presented by quarters of the day - morning, afternoon, evening, and overnight. Details such as temperature, humidity, wind, precipitation, and UV index are returned.</td>
</tr>
<tr>
    <td><a href="#get_current_conditions"><CopyableCode code="get_current_conditions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-details"><code>details</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get current weather conditions. The `Get Current Conditions` API is an HTTP `GET` request that returns detailed current weather conditions such as precipitation, temperature and wind for a given coordinate location. Also, observations from the past 6 or 24 hours for a particular location can be retrieved. The basic information returned with The response includes details such as observation date and time, brief description of the weather conditions, weather icon, precipitation indicator flags, and temperature. Additional details such as RealFeel™ Temperature and UV index are also returned. For more information, see `Request real-time weather data `__.</td>
</tr>
<tr>
    <td><a href="#get_daily_forecast"><CopyableCode code="get_daily_forecast" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a daily detailed weather forecast for the next 1, 5, 10, 15, 25, or 45 days. The `Get Daily Forecast` API is an HTTP `GET` request that returns detailed weather forecast such as temperature and wind by day for the next 1, 5, 10, 15, 25, or 45 days for a given coordinate location. The response includes details such as temperature, wind, precipitation, air quality, and UV index. For more information, see `Request daily weather forecast data `__. If you are using the Gen1 S0 pricing tier, you can request daily forecast for the next 1, 5, 10, and 15 days. If you are using Gen1 S1 or Gen2 pricing tier, you can also request daily forecast for the next 25 days, and 45 days.</td>
</tr>
<tr>
    <td><a href="#get_weather_along_route"><CopyableCode code="get_weather_along_route" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a locationally precise, up-to-the-minute forecast that includes weather hazard assessments and notifications along a route. The `Get Weather Along Route` API is an HTTP `GET` request that returns hyper local (one kilometer or less), up-to-the-minute weather nowcasts, weather hazard assessments, and notifications along a route described as a sequence of waypoints. This includes a list of weather hazards affecting the waypoint or route, and the aggregated hazard index for each waypoint might be used to paint each portion of a route according to how safe it is for the driver. When submitting the waypoints, it is recommended to stay within, or close to, the distance that can be traveled within 120-mins or shortly after. Data is updated every five minutes. The service supplements Azure Maps `Route Service `__ that allows you to first request a route between an origin and a destination and use that as an input for Weather Along Route endpoint. In addition, the service supports scenarios to generate weather notifications for waypoints that experience an increase in intensity of a weather hazard. For example, if the vehicle is expected to begin experiencing heavy rain as it reaches a waypoint, a weather notification for heavy rain will be generated for that waypoint allowing the end product to display a heavy rain notification before the driver reaches that waypoint. The trigger for when to display the notification for a waypoint could be based, for example, on a `geofence `__\ , or selectable distance to the waypoint. The API covers all regions of the planet except latitudes above Greenland and Antarctica.</td>
</tr>
<tr>
    <td><a href="#get_severe_weather_alerts"><CopyableCode code="get_severe_weather_alerts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-details"><code>details</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get information about severe weather conditions such as hurricanes, thunderstorms, flooding, lightning, heat waves or forest fires for a given location. Severe weather phenomenon can significantly impact our everyday life and business operations. For example, severe weather conditions such as tropical storms, high winds or flooding can close roads and force logistics companies to reroute their fleet causing delays in reaching destinations and breaking the cold chain of refrigerated food products. The `Get Severe Weather Alerts` API is an HTTP `GET` request that returns the severe weather alerts that are available worldwide from both official Government Meteorological Agencies and leading global to regional weather alert providers. The service can return details such as alert type, category, level and detailed description about the active severe alerts for the requested location, like hurricanes, thunderstorms, lightning, heat waves or forest fires. For more information, see `Request severe weather alerts `__.</td>
</tr>
<tr>
    <td><a href="#get_daily_indices"><CopyableCode code="get_daily_indices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-indexId"><code>indexId</code></a>, <a href="#parameter-indexGroupId"><code>indexGroupId</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use when you want to know if the weather conditions are optimal for a specific activity such as outdoor sporting activities, construction, or farming (results includes soil moisture information). The `Get Daily Indices` API is an HTTP `GET` request returns index values that provide guidance to help when planning future activities. For example, a health mobile application can notify users that today is good weather for running or for other outdoors activities like playing golf or flying a kite. Retail stores can optimize their digital marketing campaigns based on predicted index values. The service returns in daily indices values for current and next 5, 10 and 15 days starting from current day.</td>
</tr>
<tr>
    <td><a href="#get_tropical_storm_active"><CopyableCode code="get_tropical_storm_active" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a list of the active tropical storms issued by national weather forecasting agencies. The `Get Tropical Storm Active` API is an HTTP `GET` request that returns a list of all government-issued active tropical storms. Information about the tropical storms includes, government ID, basin ID, year of origin, name and if it is subtropical.</td>
</tr>
<tr>
    <td><a href="#get_tropical_storm_forecast"><CopyableCode code="get_tropical_storm_forecast" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-year"><code>year</code></a>, <a href="#parameter-basinId"><code>basinId</code></a>, <a href="#parameter-govId"><code>govId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-details"><code>details</code></a>, <a href="#parameter-radiiGeometry"><code>radiiGeometry</code></a>, <a href="#parameter-windowGeometry"><code>windowGeometry</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a list of tropical storms forecasted by national weather forecasting agencies. The `Get Tropical Storm Forecasts` API is an HTTP `GET` request that returns individual government-issued tropical storm forecasts. Information about the forecasted tropical storms includes, location, status, date the forecast was created, window, wind speed and wind radii.</td>
</tr>
<tr>
    <td><a href="#get_tropical_storm_locations"><CopyableCode code="get_tropical_storm_locations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-year"><code>year</code></a>, <a href="#parameter-basinId"><code>basinId</code></a>, <a href="#parameter-govId"><code>govId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-details"><code>details</code></a>, <a href="#parameter-radiiGeometry"><code>radiiGeometry</code></a>, <a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-current"><code>current</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the location of tropical storms from individual national weather forecasting agencies. The `Get Tropical Storm Locations` API is an HTTP `GET` request that returns the location of individual government-issued tropical storms. Information about the tropical storms includes, location coordinates, geometry, basin ID, date, wind details and wind radii.</td>
</tr>
<tr>
    <td><a href="#get_current_air_quality"><CopyableCode code="get_current_air_quality" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-pollutants"><code>pollutants</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get current air quality information that includes potential risks and suggested precautions. The `Get Current Air Quality` API is an HTTP `GET` request that returns detailed information about the concentration of pollutants and overall status for current air quality, including pollution levels, air quality index values, the dominant pollutant, and a brief statement summarizing risk level and suggested precautions.</td>
</tr>
<tr>
    <td><a href="#get_air_quality_daily_forecasts"><CopyableCode code="get_air_quality_daily_forecasts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get daily air quality forecasts for the next one to seven days that include pollutant levels, potential risks and suggested precautions. The `Get Air Quality Daily Forecasts` API is an HTTP `GET` request that returns detailed information about the concentration of pollutants and overall status of forecasted daily air quality. The service can provide forecasted daily air quality information for the upcoming 1 to 7 days, including pollution levels, air quality index values, the dominant pollutant, and a brief statement summarizing risk level and suggested precautions.</td>
</tr>
<tr>
    <td><a href="#get_air_quality_hourly_forecasts"><CopyableCode code="get_air_quality_hourly_forecasts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-pollutants"><code>pollutants</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get hourly air quality forecasts for the next one to 96 hours that include pollutant levels, potential risks and suggested precautions. The `Get Air Quality Hourly Forecasts` API is an HTTP `GET` request that returns detailed information about the concentration of pollutants and overall status for forecasted upcoming hourly air quality. The service can provide forecasted hourly air quality information for the upcoming time spans of 1, 12, 24, 48, 72, and 96 hours, including pollution levels, air quality index values, the dominant pollutant, and a brief statement summarizing risk level and suggested precautions.</td>
</tr>
<tr>
    <td><a href="#get_daily_historical_actuals"><CopyableCode code="get_daily_historical_actuals" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get climatology data such as past daily actual observed temperatures, precipitation, snowfall and snow depth. The `Get Daily Historical Actuals` API is an HTTP `GET` request that returns climatology data such as past daily actual observed temperatures, precipitation, snowfall, snow depth and cooling/heating degree day information, for the day at a given coordinate location. The data is requested for a specified date range, up to 31 days in a single API request. Generally, historical data may be available as far back as the last 5 to 40+ years, depending on the location.</td>
</tr>
<tr>
    <td><a href="#get_daily_historical_records"><CopyableCode code="get_daily_historical_records" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get climatology data such as past daily record temperatures, precipitation and snowfall at a given location. The `Get Daily Historical Records` API is an HTTP `GET` request that returns climatology data such as past daily record temperatures, precipitation and snowfall at a given coordinate location. Availability of records data will vary by location. Generally, historical data may be available as far back as the last 5 to 40+ years, depending on the location.</td>
</tr>
<tr>
    <td><a href="#get_daily_historical_normals"><CopyableCode code="get_daily_historical_normals" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-startDate"><code>startDate</code></a>, <a href="#parameter-endDate"><code>endDate</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-unit"><code>unit</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get climatology data such as past daily normal temperatures, precipitation and cooling/heating degree day information for a given location. The `Get Daily Historical Normals` API is an HTTP `GET` request that returns climatology data such as past daily normal temperatures, precipitation and cooling/heating degree day information for the day at a given coordinate location. The historical normals are a 30-year average for temperatures and precipitation for a specific location. As is standard practice in climatology, the 30-year average covers years 1991-2020, this data will be used for one decade and then will reset in the year 2030. Generally, historical data may be available as far back as the last 5 to 40+ years, depending on the location.</td>
</tr>
<tr>
    <td><a href="#search_tropical_storm"><CopyableCode code="search_tropical_storm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-year"><code>year</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-basinId"><code>basinId</code></a>, <a href="#parameter-govId"><code>govId</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get a list of storms issued by national weather forecasting agencies. The `Get Tropical Storm Search` API is an HTTP `GET` request that returns a list of government-issued tropical storms by year, basin ID, and government ID. Information about the tropical storms includes, government ID, basin ID, status, year, name and if it is subtropical.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-basinId">
    <td><CopyableCode code="basinId" /></td>
    <td><code>string</code></td>
    <td>Basin identifier. Known values are: "AL", "EP", "SI", "NI", "CP", "NP", and "SP". Required.</td>
</tr>
<tr id="parameter-endDate">
    <td><CopyableCode code="endDate" /></td>
    <td><code>string (date)</code></td>
    <td>End date in ISO 8601 format, for example, 2019-10-28. The date range supported is 1 to 31 calendar days, so be sure to specify a startDate and endDate that does not exceed a maximum of 31 days (i.e.: startDate=2012-01-01&endDate=2012-01-31). Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Desired format of the response. Only `json` format is supported. "json" Default value is "json".</td>
</tr>
<tr id="parameter-govId">
    <td><CopyableCode code="govId" /></td>
    <td><code>integer</code></td>
    <td>Government storm Id. Required.</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>array</code></td>
    <td>The applicable query specified as a comma separated string composed by latitude followed by longitude e.g. "47.641268,-122.125679". Weather information is generally available for locations on land, bodies of water surrounded by land, and areas of the ocean that are within approximately 50 nautical miles of a coastline. Required.</td>
</tr>
<tr id="parameter-startDate">
    <td><CopyableCode code="startDate" /></td>
    <td><code>string (date)</code></td>
    <td>Start date in ISO 8601 format, for example, 2019-10-27. The date range supported is 1 to 31 calendar days, so be sure to specify a startDate and endDate that does not exceed a maximum of 31 days (i.e.: startDate=2012-01-01&endDate=2012-01-31). Required.</td>
</tr>
<tr id="parameter-year">
    <td><CopyableCode code="year" /></td>
    <td><code>integer</code></td>
    <td>Year of the cyclone(s). Required.</td>
</tr>
<tr id="parameter-basinId">
    <td><CopyableCode code="basinId" /></td>
    <td><code>string</code></td>
    <td>Basin identifier. Known values are: "AL", "EP", "SI", "NI", "CP", "NP", and "SP". Default value is None.</td>
</tr>
<tr id="parameter-current">
    <td><CopyableCode code="current" /></td>
    <td><code>boolean</code></td>
    <td>When true, return the current storm location. Default value is False.</td>
</tr>
<tr id="parameter-details">
    <td><CopyableCode code="details" /></td>
    <td><code>boolean</code></td>
    <td>When true, wind radii summary data is included in the response. Default value is False.</td>
</tr>
<tr id="parameter-duration">
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>Specifies for how many hours from now we would like to know about the air quality. Available values are 1, 12, 24, 48, 72, 96. Default value is 1 hour. Known values are: 1, 12, 24, 48, 72, and 96. Default value is 1.</td>
</tr>
<tr id="parameter-govId">
    <td><CopyableCode code="govId" /></td>
    <td><code>integer</code></td>
    <td>Government storm Id. Default value is None.</td>
</tr>
<tr id="parameter-indexGroupId">
    <td><CopyableCode code="indexGroupId" /></td>
    <td><code>integer</code></td>
    <td>Numeric index group identifier that can be used for restricting returned results to the corresponding subset of indices (index group). Cannot be paired with `indexId`. Please refer to `Weather services in Azure Maps `__ for details and to see the supported index groups. Default value is None.</td>
</tr>
<tr id="parameter-indexId">
    <td><CopyableCode code="indexId" /></td>
    <td><code>integer</code></td>
    <td>Numeric index identifier that can be used for restricting returned results to the corresponding index type. Cannot be paired with `indexGroupId`. Please refer to `Weather services in Azure Maps `__ for details and to see the supported indices. Default value is None.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>Specifies time interval in minutes for the returned weather forecast. Supported values are * `1` - Retrieve forecast for 1-minute intervals. Returned by default. * `5` - Retrieve forecasts for 5-minute intervals. * `15` - Retrieve forecasts for 15-minute intervals. Default value is None.</td>
</tr>
<tr id="parameter-language">
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Language in which search results should be returned. Should be one of supported IETF language tags, case insensitive. When data in specified language is not available for a specific field, default language is used. Please refer to `Supported Languages `__ for details. Default value is None.</td>
</tr>
<tr id="parameter-pollutants">
    <td><CopyableCode code="pollutants" /></td>
    <td><code>boolean</code></td>
    <td>Boolean value that returns detailed information about each pollutant. By default is True. Default value is None.</td>
</tr>
<tr id="parameter-radiiGeometry">
    <td><CopyableCode code="radiiGeometry" /></td>
    <td><code>boolean</code></td>
    <td>When true, wind radii summary data and geoJSON details are included in the response. Default value is False.</td>
</tr>
<tr id="parameter-unit">
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>Specifies to return the data in either metric units or imperial units. Default value is metric. Known values are: "metric" and "imperial". Default value is None.</td>
</tr>
<tr id="parameter-windowGeometry">
    <td><CopyableCode code="windowGeometry" /></td>
    <td><code>boolean</code></td>
    <td>When true, window geometry data (geoJSON) is included in the response. Default value is False.</td>
</tr>
<tr id="parameter-x-ms-client-id">
    <td><CopyableCode code="x-ms-client-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_hourly_forecast"
    values={[
        { label: 'get_hourly_forecast', value: 'get_hourly_forecast' },
        { label: 'get_minute_forecast', value: 'get_minute_forecast' },
        { label: 'get_quarter_day_forecast', value: 'get_quarter_day_forecast' },
        { label: 'get_current_conditions', value: 'get_current_conditions' },
        { label: 'get_daily_forecast', value: 'get_daily_forecast' },
        { label: 'get_weather_along_route', value: 'get_weather_along_route' },
        { label: 'get_severe_weather_alerts', value: 'get_severe_weather_alerts' },
        { label: 'get_daily_indices', value: 'get_daily_indices' },
        { label: 'get_tropical_storm_active', value: 'get_tropical_storm_active' },
        { label: 'get_tropical_storm_forecast', value: 'get_tropical_storm_forecast' },
        { label: 'get_tropical_storm_locations', value: 'get_tropical_storm_locations' },
        { label: 'get_current_air_quality', value: 'get_current_air_quality' },
        { label: 'get_air_quality_daily_forecasts', value: 'get_air_quality_daily_forecasts' },
        { label: 'get_air_quality_hourly_forecasts', value: 'get_air_quality_hourly_forecasts' },
        { label: 'get_daily_historical_actuals', value: 'get_daily_historical_actuals' },
        { label: 'get_daily_historical_records', value: 'get_daily_historical_records' },
        { label: 'get_daily_historical_normals', value: 'get_daily_historical_normals' },
        { label: 'search_tropical_storm', value: 'search_tropical_storm' }
    ]}
>
<TabItem value="get_hourly_forecast">

Use to get a detailed hourly weather forecast for up to 24 hours or a daily forecast for up to 10 days. The `Get Hourly Forecast` API is an HTTP `GET` that Request detailed weather forecast by the hour for the next 1, 12, 24 (1 day), 72 (3 days), 120 (5 days), and 240 hours (10 days) for the given the given coordinate location. The API returns details such as temperature, humidity, wind, precipitation, and ultraviolet (UV) index. For more information, see `Request hourly weather forecast data `__. If you are using the Gen1 S0 pricing tier, you can request hourly forecast for the next 1, 12, 24 hours (1 day), and 72 hours (3 days). If you are using Gen1 S1 or Gen2 pricing tier, you can also request hourly forecast for the next 120 (5 days) and 240 hours (10 days).

```sql
EXEC azure.maps_weather.weather.get_hourly_forecast 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@duration='{{ duration }}', 
@language='{{ language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_minute_forecast">

Use to get a minute-by-minute forecast for the next 120 minutes in intervals of 1, 5 and 15 minutes. The `Get Minute Forecast` API is an HTTP `GET` request that returns minute-by-minute forecasts for a given location for the next 120 minutes. Users can request weather forecasts in intervals of 1, 5 and 15 minutes. The response will include details such as the type of precipitation (including rain, snow, or a mixture of both), start time, and precipitation intensity value (dBZ). For more information, see `Request minute-by-minute weather forecast data `__.

```sql
EXEC azure.maps_weather.weather.get_minute_forecast 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@interval='{{ interval }}', 
@language='{{ language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_quarter_day_forecast">

Use to get a Quarter-Day Forecast for the next 1, 5, 10, or 15 days. The `Get Quarter-Day Forecast` API is an HTTP `GET` request that returns a detailed weather forecast by quarter-day for the next 1, 5, 10, or 15 days for a given location. Response data is presented by quarters of the day - morning, afternoon, evening, and overnight. Details such as temperature, humidity, wind, precipitation, and UV index are returned.

```sql
EXEC azure.maps_weather.weather.get_quarter_day_forecast 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@duration='{{ duration }}', 
@language='{{ language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_current_conditions">

Use to get current weather conditions. The `Get Current Conditions` API is an HTTP `GET` request that returns detailed current weather conditions such as precipitation, temperature and wind for a given coordinate location. Also, observations from the past 6 or 24 hours for a particular location can be retrieved. The basic information returned with The response includes details such as observation date and time, brief description of the weather conditions, weather icon, precipitation indicator flags, and temperature. Additional details such as RealFeel™ Temperature and UV index are also returned. For more information, see `Request real-time weather data `__.

```sql
EXEC azure.maps_weather.weather.get_current_conditions 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@details='{{ details }}', 
@duration='{{ duration }}', 
@language='{{ language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_daily_forecast">

Use to get a daily detailed weather forecast for the next 1, 5, 10, 15, 25, or 45 days. The `Get Daily Forecast` API is an HTTP `GET` request that returns detailed weather forecast such as temperature and wind by day for the next 1, 5, 10, 15, 25, or 45 days for a given coordinate location. The response includes details such as temperature, wind, precipitation, air quality, and UV index. For more information, see `Request daily weather forecast data `__. If you are using the Gen1 S0 pricing tier, you can request daily forecast for the next 1, 5, 10, and 15 days. If you are using Gen1 S1 or Gen2 pricing tier, you can also request daily forecast for the next 25 days, and 45 days.

```sql
EXEC azure.maps_weather.weather.get_daily_forecast 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@duration='{{ duration }}', 
@language='{{ language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_weather_along_route">

Use to get a locationally precise, up-to-the-minute forecast that includes weather hazard assessments and notifications along a route. The `Get Weather Along Route` API is an HTTP `GET` request that returns hyper local (one kilometer or less), up-to-the-minute weather nowcasts, weather hazard assessments, and notifications along a route described as a sequence of waypoints. This includes a list of weather hazards affecting the waypoint or route, and the aggregated hazard index for each waypoint might be used to paint each portion of a route according to how safe it is for the driver. When submitting the waypoints, it is recommended to stay within, or close to, the distance that can be traveled within 120-mins or shortly after. Data is updated every five minutes. The service supplements Azure Maps `Route Service `__ that allows you to first request a route between an origin and a destination and use that as an input for Weather Along Route endpoint. In addition, the service supports scenarios to generate weather notifications for waypoints that experience an increase in intensity of a weather hazard. For example, if the vehicle is expected to begin experiencing heavy rain as it reaches a waypoint, a weather notification for heavy rain will be generated for that waypoint allowing the end product to display a heavy rain notification before the driver reaches that waypoint. The trigger for when to display the notification for a waypoint could be based, for example, on a `geofence `__\ , or selectable distance to the waypoint. The API covers all regions of the planet except latitudes above Greenland and Antarctica.

```sql
EXEC azure.maps_weather.weather.get_weather_along_route 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_severe_weather_alerts">

Use to get information about severe weather conditions such as hurricanes, thunderstorms, flooding, lightning, heat waves or forest fires for a given location. Severe weather phenomenon can significantly impact our everyday life and business operations. For example, severe weather conditions such as tropical storms, high winds or flooding can close roads and force logistics companies to reroute their fleet causing delays in reaching destinations and breaking the cold chain of refrigerated food products. The `Get Severe Weather Alerts` API is an HTTP `GET` request that returns the severe weather alerts that are available worldwide from both official Government Meteorological Agencies and leading global to regional weather alert providers. The service can return details such as alert type, category, level and detailed description about the active severe alerts for the requested location, like hurricanes, thunderstorms, lightning, heat waves or forest fires. For more information, see `Request severe weather alerts `__.

```sql
EXEC azure.maps_weather.weather.get_severe_weather_alerts 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@details='{{ details }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_daily_indices">

Use when you want to know if the weather conditions are optimal for a specific activity such as outdoor sporting activities, construction, or farming (results includes soil moisture information). The `Get Daily Indices` API is an HTTP `GET` request returns index values that provide guidance to help when planning future activities. For example, a health mobile application can notify users that today is good weather for running or for other outdoors activities like playing golf or flying a kite. Retail stores can optimize their digital marketing campaigns based on predicted index values. The service returns in daily indices values for current and next 5, 10 and 15 days starting from current day.

```sql
EXEC azure.maps_weather.weather.get_daily_indices 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@duration='{{ duration }}', 
@indexId='{{ indexId }}', 
@indexGroupId='{{ indexGroupId }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_tropical_storm_active">

Use to get a list of the active tropical storms issued by national weather forecasting agencies. The `Get Tropical Storm Active` API is an HTTP `GET` request that returns a list of all government-issued active tropical storms. Information about the tropical storms includes, government ID, basin ID, year of origin, name and if it is subtropical.

```sql
EXEC azure.maps_weather.weather.get_tropical_storm_active 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_tropical_storm_forecast">

Use to get a list of tropical storms forecasted by national weather forecasting agencies. The `Get Tropical Storm Forecasts` API is an HTTP `GET` request that returns individual government-issued tropical storm forecasts. Information about the forecasted tropical storms includes, location, status, date the forecast was created, window, wind speed and wind radii.

```sql
EXEC azure.maps_weather.weather.get_tropical_storm_forecast 
@format='{{ format }}' --required, 
@year='{{ year }}' --required, 
@basinId='{{ basinId }}' --required, 
@govId='{{ govId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@details={{ details }}, 
@radiiGeometry={{ radiiGeometry }}, 
@windowGeometry={{ windowGeometry }}, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_tropical_storm_locations">

Use to get the location of tropical storms from individual national weather forecasting agencies. The `Get Tropical Storm Locations` API is an HTTP `GET` request that returns the location of individual government-issued tropical storms. Information about the tropical storms includes, location coordinates, geometry, basin ID, date, wind details and wind radii.

```sql
EXEC azure.maps_weather.weather.get_tropical_storm_locations 
@format='{{ format }}' --required, 
@year='{{ year }}' --required, 
@basinId='{{ basinId }}' --required, 
@govId='{{ govId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@details={{ details }}, 
@radiiGeometry={{ radiiGeometry }}, 
@unit='{{ unit }}', 
@current={{ current }}, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_current_air_quality">

Use to get current air quality information that includes potential risks and suggested precautions. The `Get Current Air Quality` API is an HTTP `GET` request that returns detailed information about the concentration of pollutants and overall status for current air quality, including pollution levels, air quality index values, the dominant pollutant, and a brief statement summarizing risk level and suggested precautions.

```sql
EXEC azure.maps_weather.weather.get_current_air_quality 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@pollutants={{ pollutants }}, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_air_quality_daily_forecasts">

Use to get daily air quality forecasts for the next one to seven days that include pollutant levels, potential risks and suggested precautions. The `Get Air Quality Daily Forecasts` API is an HTTP `GET` request that returns detailed information about the concentration of pollutants and overall status of forecasted daily air quality. The service can provide forecasted daily air quality information for the upcoming 1 to 7 days, including pollution levels, air quality index values, the dominant pollutant, and a brief statement summarizing risk level and suggested precautions.

```sql
EXEC azure.maps_weather.weather.get_air_quality_daily_forecasts 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@duration='{{ duration }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_air_quality_hourly_forecasts">

Use to get hourly air quality forecasts for the next one to 96 hours that include pollutant levels, potential risks and suggested precautions. The `Get Air Quality Hourly Forecasts` API is an HTTP `GET` request that returns detailed information about the concentration of pollutants and overall status for forecasted upcoming hourly air quality. The service can provide forecasted hourly air quality information for the upcoming time spans of 1, 12, 24, 48, 72, and 96 hours, including pollution levels, air quality index values, the dominant pollutant, and a brief statement summarizing risk level and suggested precautions.

```sql
EXEC azure.maps_weather.weather.get_air_quality_hourly_forecasts 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@duration='{{ duration }}', 
@pollutants={{ pollutants }}, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_daily_historical_actuals">

Use to get climatology data such as past daily actual observed temperatures, precipitation, snowfall and snow depth. The `Get Daily Historical Actuals` API is an HTTP `GET` request that returns climatology data such as past daily actual observed temperatures, precipitation, snowfall, snow depth and cooling/heating degree day information, for the day at a given coordinate location. The data is requested for a specified date range, up to 31 days in a single API request. Generally, historical data may be available as far back as the last 5 to 40+ years, depending on the location.

```sql
EXEC azure.maps_weather.weather.get_daily_historical_actuals 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@startDate='{{ startDate }}' --required, 
@endDate='{{ endDate }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_daily_historical_records">

Use to get climatology data such as past daily record temperatures, precipitation and snowfall at a given location. The `Get Daily Historical Records` API is an HTTP `GET` request that returns climatology data such as past daily record temperatures, precipitation and snowfall at a given coordinate location. Availability of records data will vary by location. Generally, historical data may be available as far back as the last 5 to 40+ years, depending on the location.

```sql
EXEC azure.maps_weather.weather.get_daily_historical_records 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@startDate='{{ startDate }}' --required, 
@endDate='{{ endDate }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_daily_historical_normals">

Use to get climatology data such as past daily normal temperatures, precipitation and cooling/heating degree day information for a given location. The `Get Daily Historical Normals` API is an HTTP `GET` request that returns climatology data such as past daily normal temperatures, precipitation and cooling/heating degree day information for the day at a given coordinate location. The historical normals are a 30-year average for temperatures and precipitation for a specific location. As is standard practice in climatology, the 30-year average covers years 1991-2020, this data will be used for one decade and then will reset in the year 2030. Generally, historical data may be available as far back as the last 5 to 40+ years, depending on the location.

```sql
EXEC azure.maps_weather.weather.get_daily_historical_normals 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@startDate='{{ startDate }}' --required, 
@endDate='{{ endDate }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@unit='{{ unit }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="search_tropical_storm">

Use to get a list of storms issued by national weather forecasting agencies. The `Get Tropical Storm Search` API is an HTTP `GET` request that returns a list of government-issued tropical storms by year, basin ID, and government ID. Information about the tropical storms includes, government ID, basin ID, status, year, name and if it is subtropical.

```sql
EXEC azure.maps_weather.weather.search_tropical_storm 
@format='{{ format }}' --required, 
@year='{{ year }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@basinId='{{ basinId }}', 
@govId='{{ govId }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
</Tabs>
