--- 
title: render
hide_title: false
hide_table_of_contents: false
keywords:
  - render
  - maps_render
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

Creates, updates, deletes, gets or lists a <code>render</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="render" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps_render.render" /></td></tr>
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
    <td><a href="#get_map_tile"><CopyableCode code="get_map_tile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-tilesetId"><code>tilesetId</code></a>, <a href="#parameter-zoom"><code>zoom</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeStamp"><code>timeStamp</code></a>, <a href="#parameter-tileSize"><code>tileSize</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-view"><code>view</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to request map tiles in vector or raster format. The `Get Map Tiles` API in an HTTP GET request that allows users to request map tiles in vector or raster formats typically to be integrated into a map control or SDK. Some example tiles that can be requested are Azure Maps road tiles, real-time Weather Radar tiles or the map tiles created using `Azure Maps Creator `_. By default, Azure Maps uses vector tiles for its web map control (\ `Web SDK `_\ ) and `Android SDK `_.</td>
</tr>
<tr>
    <td><a href="#get_map_tileset"><CopyableCode code="get_map_tileset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-tilesetId"><code>tilesetId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get metadata for a tileset. The Get Map Tileset API allows users to request metadata for a tileset.</td>
</tr>
<tr>
    <td><a href="#get_map_attribution"><CopyableCode code="get_map_attribution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-tilesetId"><code>tilesetId</code></a>, <a href="#parameter-zoom"><code>zoom</code></a>, <a href="#parameter-bounds"><code>bounds</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get map copyright attribution information. The `Get Map Attribution` API allows users to request map copyright attribution information for a section of a tileset.</td>
</tr>
<tr>
    <td><a href="#get_map_state_tile"><CopyableCode code="get_map_state_tile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zoom"><code>zoom</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-statesetId"><code>statesetId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get state tiles in vector format that can then be used to display feature state information in an indoor map. Fetches state tiles in vector format typically to be integrated into indoor maps module of map control or SDK. The map control will call this API after user turns on dynamic styling. For more information, see `Zoom Levels and Tile Grid `__.</td>
</tr>
<tr>
    <td><a href="#get_copyright_caption"><CopyableCode code="get_copyright_caption" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get copyright information to use when rendering a tile. The `Get Copyright Caption` API is an HTTP GET request designed to serve copyright information to be used with tiles requested from the Render service. In addition to a basic copyright for the whole map, it can serve specific groups of copyrights for some countries/regions. As an alternative to copyrights for map request, it can also return captions for displaying provider information on the map.</td>
</tr>
<tr>
    <td><a href="#get_map_static_image"><CopyableCode code="get_map_static_image" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-tilesetId"><code>tilesetId</code></a>, <a href="#parameter-trafficLayer"><code>trafficLayer</code></a>, <a href="#parameter-zoom"><code>zoom</code></a>, <a href="#parameter-center"><code>center</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-view"><code>view</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>This rendering API produces static, rasterized map views of a user-defined area. It's suitable for lightweight web applications, when the desired user experience doesn't require interactive map controls, or when bandwidth is limited. This API is also useful for embedding maps in applications outside of the browser, in backend services, report generation, or desktop applications. This API includes parameters for basic data visualization: * Labeled pushpins in multiple styles. * Render circle, path, and polygon geometry types. For more information and detailed examples, see `Render custom data on a raster map `_. The dimensions of the bbox parameter are constrained, depending on the zoom level. This ensures the resulting image has an appropriate level of detail. .. list-table:: :header-rows: 1 * - Zoom Level - Min Lon Range - Max Lon Range - Min Lat Range - Max Lat Range * - 0 - 56.25 - 360.0 - 30.1105585173 - 180.0 * - 1 - 28.125 - 360.0 - 14.87468995 - 180.0 * - 2 - 14.063 - 351.5625 - 7.4130741851 - 137.9576312246 * - 3 - 7.03125 - 175.78125 - 3.7034501005 - 73.6354071932 * - 4 - 3.515625 - 87.890625 - 1.8513375155 - 35.4776115315 * - 5 - 1.7578125 - 43.9453125 - 0.925620264 - 17.4589959239 * - 6 - 0.87890625 - 21.97265625 - 0.4628040687 - 8.6907788223 * - 7 - 0.439453125 - 10.986328125 - 0.2314012764 - 4.3404320789 * - 8 - 0.2197265625 - 5.4931640625 - 0.1157005434 - 2.1695927024 * - 9 - 0.1098632812 - 2.7465820312 - 0.0578502599 - 1.0847183194 * - 10 - 0.0549316406 - 1.3732910156 - 0.0289251285 - 0.5423494021 * - 11 - 0.0274658203 - 0.6866455078 - 0.014462564 - 0.2711734813 * - 12 - 0.0137329102 - 0.3433227539 - 0.007231282 - 0.1355865882 * - 13 - 0.0068664551 - 0.171661377 - 0.003615641 - 0.067793275 * - 14 - 0.0034332275 - 0.0858306885 - 0.0018078205 - 0.0338966351 * - 15 - 0.0017166138 - 0.0429153442 - 0.0009039102 - 0.0169483173 * - 16 - 0.0008583069 - 0.0214576721 - 0.0004519551 - 0.0084741586 * - 17 - 0.0004291534 - 0.0107288361 - 0.0002259776 - 0.0042370793 * - 18 - 0.0002145767 - 0.005364418 - 0.0001129888 - 0.0021185396 * - 19 - 0.0001072884 - 0.002682209 - 5.64944E-05 - 0.0010592698 * - 20 - 5.36442E-05 - 0.0013411045 - 2.82472E-05 - 0.0005296349 *Note* : Either **center** or **bbox** parameter must be supplied to the API.</td>
</tr>
<tr>
    <td><a href="#get_copyright_from_bounding_box"><CopyableCode code="get_copyright_from_bounding_box" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-mincoordinates"><code>mincoordinates</code></a>, <a href="#parameter-maxcoordinates"><code>maxcoordinates</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-text"><code>text</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get copyright information for the specified bounding box. Returns copyright information for a given bounding box. Bounding-box requests should specify the minimum and maximum longitude and latitude (EPSG-3857) coordinates.</td>
</tr>
<tr>
    <td><a href="#get_copyright_for_tile"><CopyableCode code="get_copyright_for_tile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-zoom"><code>zoom</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-text"><code>text</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get copyright information. To obtain the copyright information for a particular tile, the request should specify the tile's zoom level and x and y coordinates. For more information, see `Zoom Levels and Tile Grid `__. Copyrights API is designed to serve copyright information for Render service. In addition to basic copyright for the whole map, API is serving specific groups of copyrights for some countries/regions.</td>
</tr>
<tr>
    <td><a href="#get_copyright_for_world"><CopyableCode code="get_copyright_for_world" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-text"><code>text</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get copyright information for for the world. Returns the copyright information for the world. To obtain the default copyright information for the whole world, don't specify a tile or bounding box. Copyrights API is designed to serve copyright information for Render service. In addition to basic copyright for the whole map, API is serving specific groups of copyrights for some countries/regions.</td>
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
<tr id="parameter-bounds">
    <td><CopyableCode code="bounds" /></td>
    <td><code>array</code></td>
    <td>The string that represents the rectangular area of a bounding box. The bounds parameter is defined by the 4 bounding box coordinates, with WGS84 longitude and latitude of the southwest corner followed by WGS84 longitude and latitude of the northeast corner. The string is presented in the following format: `[SouthwestCorner_Longitude, SouthwestCorner_Latitude, NortheastCorner_Longitude, NortheastCorner_Latitude]`. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Desired format of the response. Value can be either *json* or *xml*. Known values are: "json" and "xml". Default value is "json".</td>
</tr>
<tr id="parameter-maxcoordinates">
    <td><CopyableCode code="maxcoordinates" /></td>
    <td><code>array</code></td>
    <td>Maximum coordinates (north-east point) of bounding box in latitude longitude coordinate system. E.g. 52.41064,4.84228. Required.</td>
</tr>
<tr id="parameter-mincoordinates">
    <td><CopyableCode code="mincoordinates" /></td>
    <td><code>array</code></td>
    <td>Minimum coordinates (south-west point) of bounding box in latitude longitude coordinate system. E.g. 52.41064,4.84228. Required.</td>
</tr>
<tr id="parameter-statesetId">
    <td><CopyableCode code="statesetId" /></td>
    <td><code>string</code></td>
    <td>The stateset id. Required.</td>
</tr>
<tr id="parameter-tilesetId">
    <td><CopyableCode code="tilesetId" /></td>
    <td><code>string</code></td>
    <td>A tileset is a collection of raster or vector data broken up into a uniform grid of square tiles at preset zoom levels. Every tileset has a **tilesetId** to use when making requests. The **tilesetId** for tilesets created using `Azure Maps Creator `_ are generated through the `Tileset Create API `_. The ready-to-use tilesets supplied by Azure Maps are listed below. For example, microsoft.base. Known values are: "microsoft.base", "microsoft.base.labels", "microsoft.base.hybrid", "microsoft.terra.main", "microsoft.base.road", "microsoft.base.darkgrey", "microsoft.base.labels.road", "microsoft.base.labels.darkgrey", "microsoft.base.hybrid.road", "microsoft.base.hybrid.darkgrey", "microsoft.imagery", "microsoft.weather.radar.main", "microsoft.weather.infrared.main", "microsoft.traffic.absolute", "microsoft.traffic.absolute.main", "microsoft.traffic.relative", "microsoft.traffic.relative.main", "microsoft.traffic.relative.dark", "microsoft.traffic.delay", "microsoft.traffic.delay.main", "microsoft.traffic.reduced.main", and "microsoft.traffic.incident". Required.</td>
</tr>
<tr id="parameter-x">
    <td><CopyableCode code="x" /></td>
    <td><code>integer</code></td>
    <td>X coordinate of the tile on zoom grid. Value must be in the range [0, 2zoom`` -1]. Please see `Zoom Levels and Tile Grid `__ for details. Required.</td>
</tr>
<tr id="parameter-y">
    <td><CopyableCode code="y" /></td>
    <td><code>integer</code></td>
    <td>Y coordinate of the tile on zoom grid. Value must be in the range [0, 2zoom`` -1]. Please see `Zoom Levels and Tile Grid `__ for details. Required.</td>
</tr>
<tr id="parameter-zoom">
    <td><CopyableCode code="zoom" /></td>
    <td><code>integer</code></td>
    <td>Zoom level for the desired tile. Please see `Zoom Levels and Tile Grid `__ for details. Required.</td>
</tr>
<tr id="parameter-bbox">
    <td><CopyableCode code="bbox" /></td>
    <td><code>array</code></td>
    <td>A bounding box is defined by two latitudes and two longitudes that represent the four sides of a rectangular area on the Earth. Format : 'minLon, minLat, maxLon, maxLat' (in double). Note: Either bbox or center are required parameters. They are mutually exclusive. bbox shouldn’t be used with height or width. The maximum and minimum allowed ranges for Lat and Lon are defined for each zoom level in the table at the top of this page. Default value is None.</td>
</tr>
<tr id="parameter-center">
    <td><CopyableCode code="center" /></td>
    <td><code>array</code></td>
    <td>Coordinates of the center point in double. Format: 'lon,lat'. Longitude range: -180 to 180. Latitude range: -90 to 90. Note: Either center or bbox are required parameters. They are mutually exclusive. Default value is None.</td>
</tr>
<tr id="parameter-height">
    <td><CopyableCode code="height" /></td>
    <td><code>integer</code></td>
    <td>Height of the resulting image in pixels. Range from 80 to 1500. Default is 512. It shouldn’t be used with bbox. Default value is None.</td>
</tr>
<tr id="parameter-language">
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Language in which search results should be returned. Should be one of supported IETF language tags, case insensitive. When data in specified language is not available for a specific field, default language is used. Please refer to `Supported Languages `_ for details. Default value is None.</td>
</tr>
<tr id="parameter-text">
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>Yes/no value to exclude textual data from response. Only images and country/region names will be in response. Known values are: "yes" and "no". Default value is None.</td>
</tr>
<tr id="parameter-tileSize">
    <td><CopyableCode code="tileSize" /></td>
    <td><code>string</code></td>
    <td>The size of the returned map tile in pixels. Known values are: "256" and "512". Default value is None.</td>
</tr>
<tr id="parameter-tilesetId">
    <td><CopyableCode code="tilesetId" /></td>
    <td><code>string</code></td>
    <td>Map style to be returned. Possible values are microsoft.base.road, microsoft.base.darkgrey, and microsoft.imagery. Default value is set to be microsoft.base.road. For more information, see `Render TilesetId `_. Known values are: "microsoft.base", "microsoft.base.labels", "microsoft.base.hybrid", "microsoft.terra.main", "microsoft.base.road", "microsoft.base.darkgrey", "microsoft.base.labels.road", "microsoft.base.labels.darkgrey", "microsoft.base.hybrid.road", "microsoft.base.hybrid.darkgrey", "microsoft.imagery", "microsoft.weather.radar.main", "microsoft.weather.infrared.main", "microsoft.traffic.absolute", "microsoft.traffic.absolute.main", "microsoft.traffic.relative", "microsoft.traffic.relative.main", "microsoft.traffic.relative.dark", "microsoft.traffic.delay", "microsoft.traffic.delay.main", "microsoft.traffic.reduced.main", and "microsoft.traffic.incident". Default value is None.</td>
</tr>
<tr id="parameter-timeStamp">
    <td><CopyableCode code="timeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The desired date and time of the requested tile. This parameter must be specified in the standard date-time format (e.g. 2019-11-14T16:03:00-08:00), as defined by `ISO 8601 `_. This parameter is only supported when tilesetId parameter is set to one of the values below. * microsoft.weather.infrared.main: We provide tiles up to 3 hours in the past. Tiles are available in 10-minute intervals. We round the timeStamp value to the nearest 10-minute time frame. * microsoft.weather.radar.main: We provide tiles up to 1.5 hours in the past and up to 2 hours in the future. Tiles are available in 5-minute intervals. We round the timeStamp value to the nearest 5-minute time frame. Default value is None.</td>
</tr>
<tr id="parameter-trafficLayer">
    <td><CopyableCode code="trafficLayer" /></td>
    <td><code>string</code></td>
    <td>Optional Value, indicating no traffic flow overlaid on the image result. Possible values are microsoft.traffic.relative.main and none. Default value is none, indicating no traffic flow returned. If traffic related tilesetId is provided, will return map image with corresponding traffic layer. For more information, see `Render TilesetId `_. Known values are: "microsoft.traffic.relative.main" and "none". Default value is None.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>The View parameter (also called the "user region" parameter) allows you to show the correct maps for a certain country/region for geopolitically disputed regions. Different countries/regions have different views of such regions, and the View parameter allows your application to comply with the view required by the country/region your application will be serving. By default, the View parameter is set to “Unified” even if you haven’t defined it in the request. It is your responsibility to determine the location of your users, and then set the View parameter correctly for that location. Alternatively, you have the option to set ‘View=Auto’, which will return the map data based on the IP address of the request. The View parameter in Azure Maps must be used in compliance with applicable laws, including those regarding mapping, of the country/region where maps, images and other data and third party content that you are authorized to access via Azure Maps is made available. Example: view=IN. Please refer to `Supported Views `_ for details and to see the available Views. Known values are: "AE", "AR", "BH", "IN", "IQ", "JO", "KW", "LB", "MA", "OM", "PK", "PS", "QA", "SA", "SY", "YE", "Auto", and "Unified". Default value is None.</td>
</tr>
<tr id="parameter-width">
    <td><CopyableCode code="width" /></td>
    <td><code>integer</code></td>
    <td>Width of the resulting image in pixels. Range from 80 to 2000. Default is 512. It should not be used with bbox. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-client-id">
    <td><CopyableCode code="x-ms-client-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zoom">
    <td><CopyableCode code="zoom" /></td>
    <td><code>integer</code></td>
    <td>Desired zoom level of the map. Support zoom value range from 0-20 (inclusive) for tilesetId being microsoft.base.road or microsoft.base.darkgrey. Support zoom value range from 0-19 (inclusive) for tilesetId being microsoft.imagery. For more information, see `Zoom Levels and Tile Grid `__. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_map_tile"
    values={[
        { label: 'get_map_tile', value: 'get_map_tile' },
        { label: 'get_map_tileset', value: 'get_map_tileset' },
        { label: 'get_map_attribution', value: 'get_map_attribution' },
        { label: 'get_map_state_tile', value: 'get_map_state_tile' },
        { label: 'get_copyright_caption', value: 'get_copyright_caption' },
        { label: 'get_map_static_image', value: 'get_map_static_image' },
        { label: 'get_copyright_from_bounding_box', value: 'get_copyright_from_bounding_box' },
        { label: 'get_copyright_for_tile', value: 'get_copyright_for_tile' },
        { label: 'get_copyright_for_world', value: 'get_copyright_for_world' }
    ]}
>
<TabItem value="get_map_tile">

Use to request map tiles in vector or raster format. The `Get Map Tiles` API in an HTTP GET request that allows users to request map tiles in vector or raster formats typically to be integrated into a map control or SDK. Some example tiles that can be requested are Azure Maps road tiles, real-time Weather Radar tiles or the map tiles created using `Azure Maps Creator `_. By default, Azure Maps uses vector tiles for its web map control (\ `Web SDK `_\ ) and `Android SDK `_.

```sql
EXEC azure.maps_render.render.get_map_tile 
@tilesetId='{{ tilesetId }}' --required, 
@zoom='{{ zoom }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeStamp='{{ timeStamp }}', 
@tileSize='{{ tileSize }}', 
@language='{{ language }}', 
@view='{{ view }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_map_tileset">

Use to get metadata for a tileset. The Get Map Tileset API allows users to request metadata for a tileset.

```sql
EXEC azure.maps_render.render.get_map_tileset 
@tilesetId='{{ tilesetId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_map_attribution">

Use to get map copyright attribution information. The `Get Map Attribution` API allows users to request map copyright attribution information for a section of a tileset.

```sql
EXEC azure.maps_render.render.get_map_attribution 
@tilesetId='{{ tilesetId }}' --required, 
@zoom='{{ zoom }}' --required, 
@bounds='{{ bounds }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_map_state_tile">

Use to get state tiles in vector format that can then be used to display feature state information in an indoor map. Fetches state tiles in vector format typically to be integrated into indoor maps module of map control or SDK. The map control will call this API after user turns on dynamic styling. For more information, see `Zoom Levels and Tile Grid `__.

```sql
EXEC azure.maps_render.render.get_map_state_tile 
@zoom='{{ zoom }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@statesetId='{{ statesetId }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_copyright_caption">

Use to get copyright information to use when rendering a tile. The `Get Copyright Caption` API is an HTTP GET request designed to serve copyright information to be used with tiles requested from the Render service. In addition to a basic copyright for the whole map, it can serve specific groups of copyrights for some countries/regions. As an alternative to copyrights for map request, it can also return captions for displaying provider information on the map.

```sql
EXEC azure.maps_render.render.get_copyright_caption 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_map_static_image">

This rendering API produces static, rasterized map views of a user-defined area. It's suitable for lightweight web applications, when the desired user experience doesn't require interactive map controls, or when bandwidth is limited. This API is also useful for embedding maps in applications outside of the browser, in backend services, report generation, or desktop applications. This API includes parameters for basic data visualization: * Labeled pushpins in multiple styles. * Render circle, path, and polygon geometry types. For more information and detailed examples, see `Render custom data on a raster map `_. The dimensions of the bbox parameter are constrained, depending on the zoom level. This ensures the resulting image has an appropriate level of detail. .. list-table:: :header-rows: 1 * - Zoom Level - Min Lon Range - Max Lon Range - Min Lat Range - Max Lat Range * - 0 - 56.25 - 360.0 - 30.1105585173 - 180.0 * - 1 - 28.125 - 360.0 - 14.87468995 - 180.0 * - 2 - 14.063 - 351.5625 - 7.4130741851 - 137.9576312246 * - 3 - 7.03125 - 175.78125 - 3.7034501005 - 73.6354071932 * - 4 - 3.515625 - 87.890625 - 1.8513375155 - 35.4776115315 * - 5 - 1.7578125 - 43.9453125 - 0.925620264 - 17.4589959239 * - 6 - 0.87890625 - 21.97265625 - 0.4628040687 - 8.6907788223 * - 7 - 0.439453125 - 10.986328125 - 0.2314012764 - 4.3404320789 * - 8 - 0.2197265625 - 5.4931640625 - 0.1157005434 - 2.1695927024 * - 9 - 0.1098632812 - 2.7465820312 - 0.0578502599 - 1.0847183194 * - 10 - 0.0549316406 - 1.3732910156 - 0.0289251285 - 0.5423494021 * - 11 - 0.0274658203 - 0.6866455078 - 0.014462564 - 0.2711734813 * - 12 - 0.0137329102 - 0.3433227539 - 0.007231282 - 0.1355865882 * - 13 - 0.0068664551 - 0.171661377 - 0.003615641 - 0.067793275 * - 14 - 0.0034332275 - 0.0858306885 - 0.0018078205 - 0.0338966351 * - 15 - 0.0017166138 - 0.0429153442 - 0.0009039102 - 0.0169483173 * - 16 - 0.0008583069 - 0.0214576721 - 0.0004519551 - 0.0084741586 * - 17 - 0.0004291534 - 0.0107288361 - 0.0002259776 - 0.0042370793 * - 18 - 0.0002145767 - 0.005364418 - 0.0001129888 - 0.0021185396 * - 19 - 0.0001072884 - 0.002682209 - 5.64944E-05 - 0.0010592698 * - 20 - 5.36442E-05 - 0.0013411045 - 2.82472E-05 - 0.0005296349 *Note* : Either **center** or **bbox** parameter must be supplied to the API.

```sql
EXEC azure.maps_render.render.get_map_static_image 
@endpoint='{{ endpoint }}' --required, 
@tilesetId='{{ tilesetId }}', 
@trafficLayer='{{ trafficLayer }}', 
@zoom='{{ zoom }}', 
@center='{{ center }}', 
@bbox='{{ bbox }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@language='{{ language }}', 
@view='{{ view }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_copyright_from_bounding_box">

Use to get copyright information for the specified bounding box. Returns copyright information for a given bounding box. Bounding-box requests should specify the minimum and maximum longitude and latitude (EPSG-3857) coordinates.

```sql
EXEC azure.maps_render.render.get_copyright_from_bounding_box 
@format='{{ format }}' --required, 
@mincoordinates='{{ mincoordinates }}' --required, 
@maxcoordinates='{{ maxcoordinates }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@text='{{ text }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_copyright_for_tile">

Use to get copyright information. To obtain the copyright information for a particular tile, the request should specify the tile's zoom level and x and y coordinates. For more information, see `Zoom Levels and Tile Grid `__. Copyrights API is designed to serve copyright information for Render service. In addition to basic copyright for the whole map, API is serving specific groups of copyrights for some countries/regions.

```sql
EXEC azure.maps_render.render.get_copyright_for_tile 
@format='{{ format }}' --required, 
@zoom='{{ zoom }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@text='{{ text }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_copyright_for_world">

Use to get copyright information for for the world. Returns the copyright information for the world. To obtain the default copyright information for the whole world, don't specify a tile or bounding box. Copyrights API is designed to serve copyright information for Render service. In addition to basic copyright for the whole map, API is serving specific groups of copyrights for some countries/regions.

```sql
EXEC azure.maps_render.render.get_copyright_for_world 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@text='{{ text }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
</Tabs>
