--- 
title: data
hide_title: false
hide_table_of_contents: false
keywords:
  - data
  - planetarycomputer_dataplane
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

Creates, updates, deletes, gets or lists a <code>data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.planetarycomputer_dataplane.data" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_search_assets_for_tile"
    values={[
        { label: 'get_search_assets_for_tile', value: 'get_search_assets_for_tile' },
        { label: 'get_collection_assets_for_tile', value: 'get_collection_assets_for_tile' },
        { label: 'get_item_point', value: 'get_item_point' },
        { label: 'get_tileset_metadata', value: 'get_tileset_metadata' },
        { label: 'get_collection_point', value: 'get_collection_point' },
        { label: 'get_search_point', value: 'get_search_point' },
        { label: 'get_tilesets', value: 'get_tilesets' },
        { label: 'get_collection_tileset_metadata', value: 'get_collection_tileset_metadata' },
        { label: 'get_search_tileset_metadata', value: 'get_search_tileset_metadata' },
        { label: 'get_tile_matrix_definitions', value: 'get_tile_matrix_definitions' },
        { label: 'get_collection_tilesets', value: 'get_collection_tilesets' },
        { label: 'get_search_tilesets', value: 'get_search_tilesets' }
    ]}
>
<TabItem value="get_search_assets_for_tile">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the feature. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assets" /></td>
    <td><code>object</code></td>
    <td>Assets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bbox" /></td>
    <td><code>array</code></td>
    <td>Bounding box coordinates for the feature. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="collection" /></td>
    <td><code>string</code></td>
    <td>ID of the STAC collection this item belongs to.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_collection_assets_for_tile">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the feature. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assets" /></td>
    <td><code>object</code></td>
    <td>Assets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bbox" /></td>
    <td><code>array</code></td>
    <td>Bounding box coordinates for the feature. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="collection" /></td>
    <td><code>string</code></td>
    <td>ID of the STAC collection this item belongs to.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_item_point">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="band_names" /></td>
    <td><code>array</code></td>
    <td>Names of each band in the raster data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinates" /></td>
    <td><code>array</code></td>
    <td>Geographic coordinates [longitude, latitude] of the queried point. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Array of pixel values at the queried point for each band. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_tileset_metadata">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="accessConstraints" /></td>
    <td><code>string</code></td>
    <td>Access constraints for the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="boundingBox" /></td>
    <td><code>object</code></td>
    <td>Bounding box of the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="crs" /></td>
    <td><code>string</code></td>
    <td>Coordinate reference system identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Type of data in the tiles.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links related to this tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="tileMatrixSetLimits" /></td>
    <td><code>array</code></td>
    <td>Limits for each tile matrix level in the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Human-readable title of the tileset.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_collection_point">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="band_names" /></td>
    <td><code>array</code></td>
    <td>Names of each band in the raster data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinates" /></td>
    <td><code>array</code></td>
    <td>Geographic coordinates [longitude, latitude] of the queried point. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Array of pixel values at the queried point for each band. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_search_point">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="band_names" /></td>
    <td><code>array</code></td>
    <td>Names of each band in the raster data. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="coordinates" /></td>
    <td><code>array</code></td>
    <td>Geographic coordinates [longitude, latitude] of the queried point. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Array of pixel values at the queried point for each band. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_tilesets">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="tilesets" /></td>
    <td><code>array</code></td>
    <td>Array of available tilesets. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_collection_tileset_metadata">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="accessConstraints" /></td>
    <td><code>string</code></td>
    <td>Access constraints for the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="boundingBox" /></td>
    <td><code>object</code></td>
    <td>Bounding box of the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="crs" /></td>
    <td><code>string</code></td>
    <td>Coordinate reference system identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Type of data in the tiles.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links related to this tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="tileMatrixSetLimits" /></td>
    <td><code>array</code></td>
    <td>Limits for each tile matrix level in the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Human-readable title of the tileset.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_search_tileset_metadata">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="accessConstraints" /></td>
    <td><code>string</code></td>
    <td>Access constraints for the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="boundingBox" /></td>
    <td><code>object</code></td>
    <td>Bounding box of the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="crs" /></td>
    <td><code>string</code></td>
    <td>Coordinate reference system identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Type of data in the tiles.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links related to this tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="tileMatrixSetLimits" /></td>
    <td><code>array</code></td>
    <td>Limits for each tile matrix level in the tileset.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Human-readable title of the tileset.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_tile_matrix_definitions">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the tile matrix set.</td>
</tr>
<tr>
    <td><CopyableCode code="boundingBox" /></td>
    <td><code>object</code></td>
    <td>Geographic extent of the tile matrix set.</td>
</tr>
<tr>
    <td><CopyableCode code="crs" /></td>
    <td><code>string</code></td>
    <td>Coordinate reference system identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Brief narrative description of this tile matrix set, normally available for display to a human.</td>
</tr>
<tr>
    <td><CopyableCode code="keywords" /></td>
    <td><code>array</code></td>
    <td>Unordered list of one or more commonly used or formalized word(s) or phrase(s) used to describe this tile matrix set.</td>
</tr>
<tr>
    <td><CopyableCode code="orderedAxes" /></td>
    <td><code>array</code></td>
    <td>Names of the coordinate axes in order.</td>
</tr>
<tr>
    <td><CopyableCode code="tileMatrices" /></td>
    <td><code>array</code></td>
    <td>Array of tile matrices at different zoom levels. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Human-readable title of the tile matrix set.</td>
</tr>
<tr>
    <td><CopyableCode code="uri" /></td>
    <td><code>string</code></td>
    <td>URI reference to the official definition.</td>
</tr>
<tr>
    <td><CopyableCode code="wellKnownScaleSet" /></td>
    <td><code>string</code></td>
    <td>URL reference to a standardized scale set.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_collection_tilesets">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="tilesets" /></td>
    <td><code>array</code></td>
    <td>Array of available tilesets. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_search_tilesets">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="tilesets" /></td>
    <td><code>array</code></td>
    <td>Array of available tilesets. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

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
    <td><a href="#get_search_assets_for_tile"><CopyableCode code="get_search_assets_for_tile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Searches Assets For Tile Tilematrixsetid As Path. Return a list of assets which overlap a given tile.</td>
</tr>
<tr>
    <td><a href="#get_collection_assets_for_tile"><CopyableCode code="get_collection_assets_for_tile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Collection Assets For Tile Tilematrixsetid As Path. Return a list of assets which overlap a given tile for a STAC collection (with TileMatrixSetId).</td>
</tr>
<tr>
    <td><a href="#get_item_point"><CopyableCode code="get_item_point" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-longitude"><code>longitude</code></a>, <a href="#parameter-latitude"><code>latitude</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a></td>
    <td>Item Point. Get point value for a STAC item dataset.</td>
</tr>
<tr>
    <td><a href="#get_tileset_metadata"><CopyableCode code="get_tileset_metadata" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tileset Metadata. Return metadata for a specific tileset of a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_collection_point"><CopyableCode code="get_collection_point" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-longitude"><code>longitude</code></a>, <a href="#parameter-latitude"><code>latitude</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a></td>
    <td>Collection Point. Get Point value for a collection dataset.</td>
</tr>
<tr>
    <td><a href="#get_search_point"><CopyableCode code="get_search_point" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-longitude"><code>longitude</code></a>, <a href="#parameter-latitude"><code>latitude</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a></td>
    <td>Searches Point. Get Point value for a search dataset.</td>
</tr>
<tr>
    <td><a href="#get_tilesets"><CopyableCode code="get_tilesets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tileset List. Return a list of available tilesets for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_collection_tileset_metadata"><CopyableCode code="get_collection_tileset_metadata" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Collection Tileset Metadata. Return metadata for a specific tileset of a STAC collection.</td>
</tr>
<tr>
    <td><a href="#get_search_tileset_metadata"><CopyableCode code="get_search_tileset_metadata" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Searches Tileset Metadata. Return metadata for a specific tileset of a mosaic search.</td>
</tr>
<tr>
    <td><a href="#get_tile_matrix_definitions"><CopyableCode code="get_tile_matrix_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Matrix Definition. Return Matrix Definition.</td>
</tr>
<tr>
    <td><a href="#get_collection_tilesets"><CopyableCode code="get_collection_tilesets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Collection Tileset List. Return a list of available tilesets for a STAC collection.</td>
</tr>
<tr>
    <td><a href="#get_search_tilesets"><CopyableCode code="get_search_tilesets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Searches Tileset List. Return a list of available tilesets for a mosaic search.</td>
</tr>
<tr>
    <td><a href="#get_tile_matrices"><CopyableCode code="get_tile_matrices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Matrix List. Return Matrix List.</td>
</tr>
<tr>
    <td><a href="#get_class_map_legend"><CopyableCode code="get_class_map_legend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-classmap_name"><code>classmap_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-trim_start"><code>trim_start</code></a>, <a href="#parameter-trim_end"><code>trim_end</code></a></td>
    <td>Get ClassMap Legend. Generate values and color swatches mapping for a given classmap.</td>
</tr>
<tr>
    <td><a href="#get_interval_legend"><CopyableCode code="get_interval_legend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-classmap_name"><code>classmap_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-trim_start"><code>trim_start</code></a>, <a href="#parameter-trim_end"><code>trim_end</code></a></td>
    <td>Get Interval Legend. Generate values and color swatches mapping for a given interval classmap. Returns a color map for intervals, where each interval is defined by a numeric range [min, max] representing the interval boundaries and an RGBA color [red, green, blue, alpha] associated with the interval. The response is a 2D array of interval definitions, where each element is a pair: the first element is an array of two numbers [min, max] defining the interval, and the second element is an array of four numbers [red, green, blue, alpha] defining the RGBA color. Example: [[ [-2, 0], [0, 0, 0, 0] ], [ [1, 32], [255, 255, 178, 255] ]]. This defines two intervals: [-2, 0] mapped to transparent black and [1, 32] mapped to opaque yellow.</td>
</tr>
<tr>
    <td><a href="#get_legend"><CopyableCode code="get_legend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-color_map_name"><code>color_map_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-trim_start"><code>trim_start</code></a>, <a href="#parameter-trim_end"><code>trim_end</code></a></td>
    <td>Get Legend. Generate a legend image for a given colormap. If the colormap has non-contiguous values at the beginning or end, which aren't desired in the output image, they can be trimmed by specifying the number of values to trim.</td>
</tr>
<tr>
    <td><a href="#get_tile"><CopyableCode code="get_tile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Tilematrixsetid Plain. Create map tile from a dataset (without scale or format in path).</td>
</tr>
<tr>
    <td><a href="#get_tile_by_format"><CopyableCode code="get_tile_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Tilematrixsetid Format. Create map tile from a dataset (with format in path, without scale).</td>
</tr>
<tr>
    <td><a href="#get_tile_by_scale"><CopyableCode code="get_tile_by_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Tilematrixsetid Scale. Create map tile from a dataset (with scale in path, without format).</td>
</tr>
<tr>
    <td><a href="#get_tile_by_scale_and_format"><CopyableCode code="get_tile_by_scale_and_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Tilematrixsetid. Create map tile from a dataset (with TileMatrixSetId, scale, and format in path).</td>
</tr>
<tr>
    <td><a href="#get_tile_no_tms"><CopyableCode code="get_tile_no_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Plain. Create map tile from a dataset (without TileMatrixSetId, scale or format in path).</td>
</tr>
<tr>
    <td><a href="#get_tile_no_tms_by_format"><CopyableCode code="get_tile_no_tms_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Format. Create map tile from a dataset (with format in path, without TileMatrixSetId or scale).</td>
</tr>
<tr>
    <td><a href="#get_tile_no_tms_by_scale"><CopyableCode code="get_tile_no_tms_by_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile Scale. Create map tile from a dataset (with scale in path, without TileMatrixSetId or format).</td>
</tr>
<tr>
    <td><a href="#get_tile_no_tms_by_scale_and_format"><CopyableCode code="get_tile_no_tms_by_scale_and_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Tile. Create map tile from a dataset (with scale and format in path, without TileMatrixSetId).</td>
</tr>
<tr>
    <td><a href="#get_item_bounds"><CopyableCode code="get_item_bounds" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Bounds. Return the bounds for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_info"><CopyableCode code="get_item_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Info. Return dataset's basic info for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_info_geo_json"><CopyableCode code="get_item_info_geo_json" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Info Geojson. Return info as GeoJSON for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_available_assets"><CopyableCode code="get_item_available_assets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Available Assets. Return a list of supported assets for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_asset_statistics"><CopyableCode code="get_item_asset_statistics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-categorical"><code>categorical</code></a>, <a href="#parameter-c"><code>c</code></a>, <a href="#parameter-p"><code>p</code></a>, <a href="#parameter-histogram_bins"><code>histogram_bins</code></a>, <a href="#parameter-histogram_range"><code>histogram_range</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-asset_expression"><code>asset_expression</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a></td>
    <td>Item Asset Statistics. Per asset statistics for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_statistics"><CopyableCode code="get_item_statistics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-categorical"><code>categorical</code></a>, <a href="#parameter-c"><code>c</code></a>, <a href="#parameter-p"><code>p</code></a>, <a href="#parameter-histogram_bins"><code>histogram_bins</code></a>, <a href="#parameter-histogram_range"><code>histogram_range</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a></td>
    <td>Item Statistics. Merged assets statistics for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_feature_statistics"><CopyableCode code="get_item_feature_statistics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-categorical"><code>categorical</code></a>, <a href="#parameter-c"><code>c</code></a>, <a href="#parameter-p"><code>p</code></a>, <a href="#parameter-histogram_bins"><code>histogram_bins</code></a>, <a href="#parameter-histogram_range"><code>histogram_range</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a></td>
    <td>Item Geojson Statistics. Get statistics from a GeoJSON feature for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_tile_json"><CopyableCode code="get_item_tile_json" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item TileJson. Return TileJSON document for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_tile_json_by_tms"><CopyableCode code="get_item_tile_json_by_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item TileJson Tilematrixsetid As Path. Return TileJSON document for a STAC item with TileMatrixSetId as path.</td>
</tr>
<tr>
    <td><a href="#get_item_wmts_capabilities"><CopyableCode code="get_item_wmts_capabilities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Wmts. OGC WMTS endpoint for a STAC item.</td>
</tr>
<tr>
    <td><a href="#get_item_wmts_capabilities_by_tms"><CopyableCode code="get_item_wmts_capabilities_by_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Wmts Tilematrixsetid As Path. OGC WMTS endpoint for a STAC item with TileMatrixSetId as path.</td>
</tr>
<tr>
    <td><a href="#get_item_preview"><CopyableCode code="get_item_preview" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Preview. Create preview of a STAC item dataset.</td>
</tr>
<tr>
    <td><a href="#get_item_preview_with_format"><CopyableCode code="get_item_preview_with_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Preview With Format. Create preview of a STAC item dataset with format.</td>
</tr>
<tr>
    <td><a href="#get_item_bbox_crop"><CopyableCode code="get_item_bbox_crop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Bbox. Create an image from part of a STAC item dataset (bounding box crop).</td>
</tr>
<tr>
    <td><a href="#get_item_bbox_crop_with_dimensions"><CopyableCode code="get_item_bbox_crop_with_dimensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Item Bbox With Dimensions. Create an image from part of a STAC item dataset (bounding box crop with dimensions).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_by_scale_and_format"><CopyableCode code="get_collection_tile_by_scale_and_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Tilematrixsetid. Create map tile for a STAC collection (with TileMatrixSetId, scale, and format in path).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile"><CopyableCode code="get_collection_tile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Tilematrixsetid Plain. Create map tile for a STAC collection (with TileMatrixSetId, without scale or format).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_by_format"><CopyableCode code="get_collection_tile_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Tilematrixsetid Format. Create map tile for a STAC collection (with TileMatrixSetId and format, without scale).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_by_scale"><CopyableCode code="get_collection_tile_by_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Tilematrixsetid Scale. Create map tile for a STAC collection (with TileMatrixSetId and scale, without format).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_no_tms_by_scale_and_format"><CopyableCode code="get_collection_tile_no_tms_by_scale_and_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile. Create map tile for a STAC collection (without TileMatrixSetId, with scale and format).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_no_tms"><CopyableCode code="get_collection_tile_no_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Plain. Create map tile for a STAC collection (without TileMatrixSetId, scale, or format).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_no_tms_by_format"><CopyableCode code="get_collection_tile_no_tms_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Format. Create map tile for a STAC collection (with format, without TileMatrixSetId or scale).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_no_tms_by_scale"><CopyableCode code="get_collection_tile_no_tms_by_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection Tile Scale. Create map tile for a STAC collection (with scale, without TileMatrixSetId or format).</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_json"><CopyableCode code="get_collection_tile_json" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection TileJson. Return TileJSON document for a STAC collection.</td>
</tr>
<tr>
    <td><a href="#get_collection_tile_json_by_tms"><CopyableCode code="get_collection_tile_json_by_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Collection TileJson Tilematrixsetid As Path. Return TileJSON document for a STAC collection with TileMatrixSetId as path.</td>
</tr>
<tr>
    <td><a href="#get_collection_wmts_capabilities"><CopyableCode code="get_collection_wmts_capabilities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a></td>
    <td>Collection Wmts. OGC WMTS endpoint for a STAC collection.</td>
</tr>
<tr>
    <td><a href="#get_collection_wmts_capabilities_by_tms"><CopyableCode code="get_collection_wmts_capabilities_by_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a></td>
    <td>Collection Wmts Tilematrixsetid As Path. OGC WMTS endpoint for a STAC collection with TileMatrixSetId as path.</td>
</tr>
<tr>
    <td><a href="#get_collection_assets_for_tile_no_tms"><CopyableCode code="get_collection_assets_for_tile_no_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a></td>
    <td>Collection Assets For Tile. Return a list of assets which overlap a given tile for a STAC collection (without TileMatrixSetId).</td>
</tr>
<tr>
    <td><a href="#get_collection_assets_for_bbox"><CopyableCode code="get_collection_assets_for_bbox" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a></td>
    <td>Collection Assets For Bbox. Return a list of assets which overlap a given bounding box for a STAC collection.</td>
</tr>
<tr>
    <td><a href="#get_collection_info"><CopyableCode code="get_collection_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Collection Info. Return search query info from a STAC collection identifier.</td>
</tr>
<tr>
    <td><a href="#get_collection_bbox_crop"><CopyableCode code="get_collection_bbox_crop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a></td>
    <td>Collection Bbox. Create an image from part of a STAC collection dataset (bounding box crop).</td>
</tr>
<tr>
    <td><a href="#get_collection_bbox_crop_with_dimensions"><CopyableCode code="get_collection_bbox_crop_with_dimensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a></td>
    <td>Collection Bbox With Dimensions. Create an image from part of a STAC collection dataset (bounding box crop with dimensions).</td>
</tr>
<tr>
    <td><a href="#get_collection_point_assets"><CopyableCode code="get_collection_point_assets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-longitude"><code>longitude</code></a>, <a href="#parameter-latitude"><code>latitude</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a></td>
    <td>Collection Point Assets. Return a list of assets for a given point in a collection.</td>
</tr>
<tr>
    <td><a href="#get_search_tile_by_scale_and_format"><CopyableCode code="get_search_tile_by_scale_and_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Tilematrixsetid. Create map tile (with TileMatrixSetId, scale, and format in path).</td>
</tr>
<tr>
    <td><a href="#get_search_tile"><CopyableCode code="get_search_tile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Tilematrixsetid Plain. Create map tile (with TileMatrixSetId, without scale or format).</td>
</tr>
<tr>
    <td><a href="#get_search_tile_by_format"><CopyableCode code="get_search_tile_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Tilematrixsetid Format. Create map tile (with TileMatrixSetId and format, without scale).</td>
</tr>
<tr>
    <td><a href="#get_search_tile_by_scale"><CopyableCode code="get_search_tile_by_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Tilematrixsetid Scale. Create map tile (with TileMatrixSetId and scale, without format).</td>
</tr>
<tr>
    <td><a href="#get_search_tile_json_by_tms"><CopyableCode code="get_search_tile_json_by_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches TileJson Tilematrixsetid As Path. Return TileJSON document for a search with TileMatrixSetId as path.</td>
</tr>
<tr>
    <td><a href="#get_search_wmts_capabilities_by_tms"><CopyableCode code="get_search_wmts_capabilities_by_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-tile_matrix_set_id"><code>tile_matrix_set_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a></td>
    <td>Searches Wmts Tilematrixsetid As Path. OGC WMTS endpoint with TileMatrixSetId as path.</td>
</tr>
<tr>
    <td><a href="#get_search_info"><CopyableCode code="get_search_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Searches Info. Get Search query metadata.</td>
</tr>
<tr>
    <td><a href="#get_search_bbox_crop"><CopyableCode code="get_search_bbox_crop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a></td>
    <td>Searches Bbox. Create an image from part of a dataset (bounding box crop).</td>
</tr>
<tr>
    <td><a href="#get_search_bbox_crop_with_dimensions"><CopyableCode code="get_search_bbox_crop_with_dimensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a></td>
    <td>Searches Bbox With Dimensions. Create an image from part of a dataset (bounding box crop with dimensions).</td>
</tr>
<tr>
    <td><a href="#get_search_bbox_assets"><CopyableCode code="get_search_bbox_assets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-minx"><code>minx</code></a>, <a href="#parameter-miny"><code>miny</code></a>, <a href="#parameter-maxx"><code>maxx</code></a>, <a href="#parameter-maxy"><code>maxy</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a></td>
    <td>Searches Assets For Bbox. Return a list of assets which overlap a given bounding box for a search.</td>
</tr>
<tr>
    <td><a href="#get_search_wmts_capabilities"><CopyableCode code="get_search_wmts_capabilities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a></td>
    <td>Searches Wmts. OGC WMTS endpoint.</td>
</tr>
<tr>
    <td><a href="#get_search_tile_json"><CopyableCode code="get_search_tile_json" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-tile_format"><code>tile_format</code></a>, <a href="#parameter-tile_scale"><code>tile_scale</code></a>, <a href="#parameter-minzoom"><code>minzoom</code></a>, <a href="#parameter-maxzoom"><code>maxzoom</code></a>, <a href="#parameter-padding"><code>padding</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a></td>
    <td>Searches TileJson. Return TileJSON document for a search.</td>
</tr>
<tr>
    <td><a href="#get_search_tile_no_tms"><CopyableCode code="get_search_tile_no_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Plain. The most basic operation.</td>
</tr>
<tr>
    <td><a href="#get_search_tile_no_tms_by_format"><CopyableCode code="get_search_tile_no_tms_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Format. The most basic operation.</td>
</tr>
<tr>
    <td><a href="#get_search_tile_no_tms_by_scale"><CopyableCode code="get_search_tile_no_tms_by_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile Scale. The most basic operation.</td>
</tr>
<tr>
    <td><a href="#get_search_tile_no_tms_by_scale_and_format"><CopyableCode code="get_search_tile_no_tms_by_scale_and_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-scale"><code>scale</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a>, <a href="#parameter-buffer"><code>buffer</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-padding"><code>padding</code></a></td>
    <td>Searches Tile. The most basic operation.</td>
</tr>
<tr>
    <td><a href="#get_search_assets_for_tile_no_tms"><CopyableCode code="get_search_assets_for_tile_no_tms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-z"><code>z</code></a>, <a href="#parameter-x"><code>x</code></a>, <a href="#parameter-y"><code>y</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-TileMatrixSetId"><code>TileMatrixSetId</code></a></td>
    <td>Searches Assets For Tile. The most basic operation.</td>
</tr>
<tr>
    <td><a href="#get_search_point_with_assets"><CopyableCode code="get_search_point_with_assets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-longitude"><code>longitude</code></a>, <a href="#parameter-latitude"><code>latitude</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a></td>
    <td>Searches Point Assets. Return a list of assets for a given point in a search.</td>
</tr>
<tr>
    <td><a href="#register_mosaics_search"><CopyableCode code="register_mosaics_search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Register Search. Register a Search query.</td>
</tr>
<tr>
    <td><a href="#crop_feature"><CopyableCode code="crop_feature" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Geojson Feature. Create image from a geojson feature (without format in path).</td>
</tr>
<tr>
    <td><a href="#crop_feature_by_format"><CopyableCode code="crop_feature_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Geojson Feature Crop With Format. Create image from a geojson feature with format.</td>
</tr>
<tr>
    <td><a href="#crop_feature_width_by_height"><CopyableCode code="crop_feature_width_by_height" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a></td>
    <td>Geojson Feature Crop With Dimensions. Create image from a geojson feature with dimensions.</td>
</tr>
<tr>
    <td><a href="#crop_collection_feature"><CopyableCode code="crop_collection_feature" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Collection Geojson Feature. Create image from a geojson feature (without format in path).</td>
</tr>
<tr>
    <td><a href="#crop_collection_feature_by_format"><CopyableCode code="crop_collection_feature_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a></td>
    <td>Collection Geojson Feature Crop With Format. Create image from a geojson feature with format.</td>
</tr>
<tr>
    <td><a href="#crop_collection_feature_width_by_height"><CopyableCode code="crop_collection_feature_width_by_height" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-ids"><code>ids</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-sortby"><code>sortby</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a></td>
    <td>Collection Geojson Feature Crop With Dimensions. Create image from a geojson feature with dimensions.</td>
</tr>
<tr>
    <td><a href="#crop_search_feature"><CopyableCode code="crop_search_feature" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Searches Geojson Feature. Create image from a geojson feature (without format in path).</td>
</tr>
<tr>
    <td><a href="#crop_search_feature_by_format"><CopyableCode code="crop_search_feature_by_format" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a></td>
    <td>Searches Geojson Feature Crop With Format. Create image from a geojson feature with format.</td>
</tr>
<tr>
    <td><a href="#crop_search_feature_width_by_height"><CopyableCode code="crop_search_feature_width_by_height" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-width"><code>width</code></a>, <a href="#parameter-height"><code>height</code></a>, <a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-asset_bidx"><code>asset_bidx</code></a>, <a href="#parameter-asset_as_band"><code>asset_as_band</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-unscale"><code>unscale</code></a>, <a href="#parameter-reproject"><code>reproject</code></a>, <a href="#parameter-scan_limit"><code>scan_limit</code></a>, <a href="#parameter-items_limit"><code>items_limit</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-exitwhenfull"><code>exitwhenfull</code></a>, <a href="#parameter-skipcovered"><code>skipcovered</code></a>, <a href="#parameter-subdataset_name"><code>subdataset_name</code></a>, <a href="#parameter-subdataset_bands"><code>subdataset_bands</code></a>, <a href="#parameter-crs"><code>crs</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sel_method"><code>sel_method</code></a>, <a href="#parameter-algorithm"><code>algorithm</code></a>, <a href="#parameter-algorithm_params"><code>algorithm_params</code></a>, <a href="#parameter-coord_crs"><code>coord_crs</code></a>, <a href="#parameter-max_size"><code>max_size</code></a>, <a href="#parameter-color_formula"><code>color_formula</code></a>, <a href="#parameter-collection"><code>collection</code></a>, <a href="#parameter-resampling"><code>resampling</code></a>, <a href="#parameter-pixel_selection"><code>pixel_selection</code></a>, <a href="#parameter-colormap_name"><code>colormap_name</code></a>, <a href="#parameter-colormap"><code>colormap</code></a>, <a href="#parameter-return_mask"><code>return_mask</code></a>, <a href="#parameter-dst_crs"><code>dst_crs</code></a></td>
    <td>Searches Geojson Feature Crop With Dimensions. Create image from a geojson feature with dimensions.</td>
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
<tr id="parameter-classmap_name">
    <td><CopyableCode code="classmap_name" /></td>
    <td><code>string</code></td>
    <td>classmap name. Required.</td>
</tr>
<tr id="parameter-collection">
    <td><CopyableCode code="collection" /></td>
    <td><code>string</code></td>
    <td>STAC Collection Identifier. Required.</td>
</tr>
<tr id="parameter-collection_id">
    <td><CopyableCode code="collection_id" /></td>
    <td><code>string</code></td>
    <td>STAC Collection Identifier. Required.</td>
</tr>
<tr id="parameter-color_map_name">
    <td><CopyableCode code="color_map_name" /></td>
    <td><code>string</code></td>
    <td>The name of the registered colormap to generate a legend for. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Output format for the tile or image (e.g., png, jpeg, webp). Required.</td>
</tr>
<tr id="parameter-height">
    <td><CopyableCode code="height" /></td>
    <td><code>integer</code></td>
    <td>Height in pixels for the output image. Required.</td>
</tr>
<tr id="parameter-item_id">
    <td><CopyableCode code="item_id" /></td>
    <td><code>string</code></td>
    <td>STAC Item Identifier. Required.</td>
</tr>
<tr id="parameter-latitude">
    <td><CopyableCode code="latitude" /></td>
    <td><code>number</code></td>
    <td>Latitude. Required.</td>
</tr>
<tr id="parameter-longitude">
    <td><CopyableCode code="longitude" /></td>
    <td><code>number</code></td>
    <td>Longitude. Required.</td>
</tr>
<tr id="parameter-maxx">
    <td><CopyableCode code="maxx" /></td>
    <td><code>number</code></td>
    <td>Bounding box max X. Required.</td>
</tr>
<tr id="parameter-maxy">
    <td><CopyableCode code="maxy" /></td>
    <td><code>number</code></td>
    <td>Bounding box max Y. Required.</td>
</tr>
<tr id="parameter-minx">
    <td><CopyableCode code="minx" /></td>
    <td><code>number</code></td>
    <td>Bounding box min X. Required.</td>
</tr>
<tr id="parameter-miny">
    <td><CopyableCode code="miny" /></td>
    <td><code>number</code></td>
    <td>Bounding box min Y. Required.</td>
</tr>
<tr id="parameter-scale">
    <td><CopyableCode code="scale" /></td>
    <td><code>number</code></td>
    <td>Numeric scale factor for the tile. Higher values produce larger tiles. Required.</td>
</tr>
<tr id="parameter-search_id">
    <td><CopyableCode code="search_id" /></td>
    <td><code>string</code></td>
    <td>Search Id (pgSTAC Search Hash). Required.</td>
</tr>
<tr id="parameter-tile_matrix_set_id">
    <td><CopyableCode code="tile_matrix_set_id" /></td>
    <td><code>string</code></td>
    <td>Identifier selecting one of the TileMatrixSetId supported. Required.</td>
</tr>
<tr id="parameter-width">
    <td><CopyableCode code="width" /></td>
    <td><code>integer</code></td>
    <td>Width in pixels for the output image. Required.</td>
</tr>
<tr id="parameter-x">
    <td><CopyableCode code="x" /></td>
    <td><code>number</code></td>
    <td>Column (X) index of the tile on the selected TileMatrix. It cannot exceed the MatrixHeight-1 for the selected TileMatrix. Required.</td>
</tr>
<tr id="parameter-y">
    <td><CopyableCode code="y" /></td>
    <td><code>number</code></td>
    <td>Row (Y) index of the tile on the selected TileMatrix. It cannot exceed the MatrixWidth-1 for the selected TileMatrix. Required.</td>
</tr>
<tr id="parameter-z">
    <td><CopyableCode code="z" /></td>
    <td><code>number</code></td>
    <td>Identifier (Z) selecting one of the scales defined in the TileMatrixSet and representing the scaleDenominator the tile. Required.</td>
</tr>
<tr id="parameter-TileMatrixSetId">
    <td><CopyableCode code="TileMatrixSetId" /></td>
    <td><code>string</code></td>
    <td>Identifier selecting one of the TileMatrixSetId supported (default: 'WebMercatorQuad'). Known values are: "CanadianNAD83_LCC", "EuropeanETRS89_LAEAQuad", "LINZAntarticaMapTilegrid", "NZTM2000Quad", "UPSAntarcticWGS84Quad", "UPSArcticWGS84Quad", "UTM31WGS84Quad", "WGS1984Quad", "WebMercatorQuad", "WorldCRS84Quad", and "WorldMercatorWGS84Quad". Default value is None.</td>
</tr>
<tr id="parameter-algorithm">
    <td><CopyableCode code="algorithm" /></td>
    <td><code>string</code></td>
    <td>Terrain algorithm name. Known values are: "hillshade", "contours", "normalizedIndex", "terrarium", "terrainrgb", "slope", "cast", "ceil", "floor", "min", "max", "median", "mean", "std", and "var". Default value is None.</td>
</tr>
<tr id="parameter-algorithm_params">
    <td><CopyableCode code="algorithm_params" /></td>
    <td><code>string</code></td>
    <td>Terrain algorithm parameters. Default value is None.</td>
</tr>
<tr id="parameter-asset_as_band">
    <td><CopyableCode code="asset_as_band" /></td>
    <td><code>boolean</code></td>
    <td>Asset as Band. Default value is None.</td>
</tr>
<tr id="parameter-asset_bidx">
    <td><CopyableCode code="asset_bidx" /></td>
    <td><code>array</code></td>
    <td>Per asset band indexes (coma separated indexes, e.g. "image|1,2,3" means use the bands 1, 2, and 3 from the asset named "image"). Default value is None.</td>
</tr>
<tr id="parameter-asset_expression">
    <td><CopyableCode code="asset_expression" /></td>
    <td><code>array</code></td>
    <td>Per asset band expression. Default value is None.</td>
</tr>
<tr id="parameter-bbox">
    <td><CopyableCode code="bbox" /></td>
    <td><code>string</code></td>
    <td>Bounding box (west, south, east, north). Default value is None.</td>
</tr>
<tr id="parameter-buffer">
    <td><CopyableCode code="buffer" /></td>
    <td><code>number</code></td>
    <td>Buffer on each side of the given tile. It must be a multiple of `0.5`. Output **tilesize** will be expanded to `tilesize + 2 * buffer` (e.g 0.5 = 257x257, 1.0 = 258x258). Default value is None.</td>
</tr>
<tr id="parameter-c">
    <td><CopyableCode code="c" /></td>
    <td><code>array</code></td>
    <td>List of pixel categorical values for which to report counts. Default value is None.</td>
</tr>
<tr id="parameter-categorical">
    <td><CopyableCode code="categorical" /></td>
    <td><code>boolean</code></td>
    <td>Return statistics for categorical dataset. Default value is None.</td>
</tr>
<tr id="parameter-collection">
    <td><CopyableCode code="collection" /></td>
    <td><code>string</code></td>
    <td>STAC Collection ID. Default value is None.</td>
</tr>
<tr id="parameter-color_formula">
    <td><CopyableCode code="color_formula" /></td>
    <td><code>string</code></td>
    <td>rio-color formula (info: `https://github.com/mapbox/rio-color `_). Default value is None.</td>
</tr>
<tr id="parameter-colormap">
    <td><CopyableCode code="colormap" /></td>
    <td><code>string</code></td>
    <td>JSON encoded custom Colormap. Default value is None.</td>
</tr>
<tr id="parameter-colormap_name">
    <td><CopyableCode code="colormap_name" /></td>
    <td><code>string</code></td>
    <td>Colormap name. Known values are: "accent", "accent_r", "afmhot", "afmhot_r", "ai4g-lulc", "alos-fnf", "alos-palsar-mask", "autumn", "autumn_r", "binary", "binary_r", "blues", "blues_r", "bone", "bone_r", "brbg", "brbg_r", "brg", "brg_r", "bugn", "bugn_r", "bupu", "bupu_r", "bwr", "bwr_r", "c-cap", "cfastie", "chesapeake-lc-13", "chesapeake-lc-7", "chesapeake-lu", "chloris-biomass", "cividis", "cividis_r", "cmrmap", "cmrmap_r", "cool", "cool_r", "coolwarm", "coolwarm_r", "copper", "copper_r", "cubehelix", "cubehelix_r", "dark2", "dark2_r", "drcog-lulc", "esa-cci-lc", "esa-worldcover", "flag", "flag_r", "gap-lulc", "gist_earth", "gist_earth_r", "gist_gray", "gist_gray_r", "gist_heat", "gist_heat_r", "gist_ncar", "gist_ncar_r", "gist_rainbow", "gist_rainbow_r", "gist_stern", "gist_stern_r", "gist_yarg", "gist_yarg_r", "gnbu", "gnbu_r", "gnuplot", "gnuplot2", "gnuplot2_r", "gnuplot_r", "gray", "gray_r", "greens", "greens_r", "greys", "greys_r", "hot", "hot_r", "hsv", "hsv_r", "inferno", "inferno_r", "io-bii", "io-lulc", "io-lulc-9-class", "jet", "jet_r", "jrc-change", "jrc-extent", "jrc-occurrence", "jrc-recurrence", "jrc-seasonality", "jrc-transitions", "lidar-classification", "lidar-hag", "lidar-hag-alternative", "lidar-intensity", "lidar-returns", "magma", "magma_r", "modis-10A1", "modis-10A2", "modis-13A1|Q1", "modis-14A1|A2", "modis-15A2H|A3H", "modis-16A3GF-ET", "modis-16A3GF-PET", "modis-17A2H|A2HGF", "modis-17A3HGF", "modis-64A1", "mtbs-severity", "nipy_spectral", "nipy_spectral_r", "nrcan-lulc", "ocean", "ocean_r", "oranges", "oranges_r", "orrd", "orrd_r", "paired", "paired_r", "pastel1", "pastel1_r", "pastel2", "pastel2_r", "pink", "pink_r", "piyg", "piyg_r", "plasma", "plasma_r", "prgn", "prgn_r", "prism", "prism_r", "pubu", "pubu_r", "pubugn", "pubugn_r", "puor", "puor_r", "purd", "purd_r", "purples", "purples_r", "qpe", "rainbow", "rainbow_r", "rdbu", "rdbu_r", "rdgy", "rdgy_r", "rdpu", "rdpu_r", "rdylbu", "rdylbu_r", "rdylgn", "rdylgn_r", "reds", "reds_r", "rplumbo", "schwarzwald", "seismic", "seismic_r", "set1", "set1_r", "set2", "set2_r", "set3", "set3_r", "spectral", "spectral_r", "spring", "spring_r", "summer", "summer_r", "tab10", "tab10_r", "tab20", "tab20_r", "tab20b", "tab20b_r", "tab20c", "tab20c_r", "terrain", "terrain_r", "twilight", "twilight_r", "twilight_shifted", "twilight_shifted_r", "usda-cdl", "usda-cdl-corn", "usda-cdl-cotton", "usda-cdl-soybeans", "usda-cdl-wheat", "usgs-lcmap", "viirs-10a1", "viirs-13a1", "viirs-14a1", "viirs-15a2H", "viridis", "viridis_r", "winter", "winter_r", "wistia", "wistia_r", "ylgn", "ylgn_r", "ylgnbu", "ylgnbu_r", "ylorbr", "ylorbr_r", "ylorrd", "ylorrd_r", "algae", "algae_r", "amp", "amp_r", "balance", "balance_r", "curl", "curl_r", "deep", "deep_r", "delta", "delta_r", "dense", "dense_r", "diff", "diff_r", "haline", "haline_r", "ice", "ice_r", "matter", "matter_r", "oxy", "oxy_r", "phase", "phase_r", "rain", "rain_r", "solar", "solar_r", "speed", "speed_r", "tarn", "tarn_r", "tempo", "tempo_r", "thermal", "thermal_r", "topo", "topo_r", "turbid", "turbid_r", "turbo", and "turbo_r". Default value is None.</td>
</tr>
<tr id="parameter-coord_crs">
    <td><CopyableCode code="coord_crs" /></td>
    <td><code>string</code></td>
    <td>Coordinate Reference System of the input coords. Default to `epsg:4326`. Default value is None.</td>
</tr>
<tr id="parameter-crs">
    <td><CopyableCode code="crs" /></td>
    <td><code>string</code></td>
    <td>Coordinate Reference System. Default value is None.</td>
</tr>
<tr id="parameter-datetime">
    <td><CopyableCode code="datetime" /></td>
    <td><code>string</code></td>
    <td>Datetime to use for subsetting the asset. Default value is None.</td>
</tr>
<tr id="parameter-dst_crs">
    <td><CopyableCode code="dst_crs" /></td>
    <td><code>string</code></td>
    <td>Output Coordinate Reference System. Default value is None.</td>
</tr>
<tr id="parameter-exitwhenfull">
    <td><CopyableCode code="exitwhenfull" /></td>
    <td><code>boolean</code></td>
    <td>Return as soon as the geometry is fully covered (defaults to True). Default value is None.</td>
</tr>
<tr id="parameter-expression">
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>Band math expression between assets. Default value is None.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Output image format. Known values are: "png", "npy", "tif", "jpeg", "jpg", "jp2", "webp", and "pngraw". Default value is None.</td>
</tr>
<tr id="parameter-height">
    <td><CopyableCode code="height" /></td>
    <td><code>integer</code></td>
    <td>Height in pixels for the output image. Default value is None.</td>
</tr>
<tr id="parameter-histogram_bins">
    <td><CopyableCode code="histogram_bins" /></td>
    <td><code>string</code></td>
    <td>Defines the number of equal-width bins in the given range (10, by default). If bins is a sequence (comma `,` delimited values), it defines a monotonically increasing array of bin edges, including the rightmost edge, allowing for non-uniform bin widths. link: `https://numpy.org/doc/stable/reference/generated/numpy.histogram.html `_. Default value is None.</td>
</tr>
<tr id="parameter-histogram_range">
    <td><CopyableCode code="histogram_range" /></td>
    <td><code>string</code></td>
    <td>Comma `,` delimited range of the bins. The lower and upper range of the bins. If not provided, range is simply (a.min(), a.max()). Values outside the range are ignored. The first element of the range must be less than or equal to the second. range affects the automatic bin computation as well. link: `https://numpy.org/doc/stable/reference/generated/numpy.histogram.html `_. Default value is None.</td>
</tr>
<tr id="parameter-ids">
    <td><CopyableCode code="ids" /></td>
    <td><code>string</code></td>
    <td>Array of Item ids. Default value is None.</td>
</tr>
<tr id="parameter-items_limit">
    <td><CopyableCode code="items_limit" /></td>
    <td><code>integer</code></td>
    <td>Return as soon as we have N items per geometry (defaults to 100). Default value is None.</td>
</tr>
<tr id="parameter-max_size">
    <td><CopyableCode code="max_size" /></td>
    <td><code>integer</code></td>
    <td>Image output size limit if width and height limits are not set. Default value is None.</td>
</tr>
<tr id="parameter-maxzoom">
    <td><CopyableCode code="maxzoom" /></td>
    <td><code>integer</code></td>
    <td>Overwrite default maxzoom. Default value is None.</td>
</tr>
<tr id="parameter-minzoom">
    <td><CopyableCode code="minzoom" /></td>
    <td><code>integer</code></td>
    <td>Overwrite default minzoom. Default value is None.</td>
</tr>
<tr id="parameter-nodata">
    <td><CopyableCode code="nodata" /></td>
    <td><code>string</code></td>
    <td>Overwrite internal Nodata value. Default value is None.</td>
</tr>
<tr id="parameter-p">
    <td><CopyableCode code="p" /></td>
    <td><code>array</code></td>
    <td>List of percentile values (default to [2, 98]). Default value is None.</td>
</tr>
<tr id="parameter-padding">
    <td><CopyableCode code="padding" /></td>
    <td><code>integer</code></td>
    <td>Padding to apply to each tile edge. Helps reduce resampling artefacts along edges. Defaults to `0`. Default value is None.</td>
</tr>
<tr id="parameter-pixel_selection">
    <td><CopyableCode code="pixel_selection" /></td>
    <td><code>string</code></td>
    <td>Pixel selection method. Known values are: "first", "highest", "lowest", "mean", "median", "stdev", "lastbandlow", "lastbandhigh", and "count". Default value is None.</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>JSON query expression for filtering items. Default value is None.</td>
</tr>
<tr id="parameter-reproject">
    <td><CopyableCode code="reproject" /></td>
    <td><code>string</code></td>
    <td>WarpKernel resampling algorithm (only used when doing re-projection). Defaults to `nearest`. Known values are: "nearest", "bilinear", "cubic", "cubic_spline", "lanczos", "average", "mode", "max", "min", "med", "q1", "q3", "sum", and "rms". Default value is None.</td>
</tr>
<tr id="parameter-resampling">
    <td><CopyableCode code="resampling" /></td>
    <td><code>string</code></td>
    <td>Resampling method. Known values are: "nearest", "bilinear", "cubic", "cubic_spline", "lanczos", "average", "mode", "gauss", and "rms". Default value is None.</td>
</tr>
<tr id="parameter-return_mask">
    <td><CopyableCode code="return_mask" /></td>
    <td><code>boolean</code></td>
    <td>Add mask to the output data. Default value is None.</td>
</tr>
<tr id="parameter-scale">
    <td><CopyableCode code="scale" /></td>
    <td><code>integer</code></td>
    <td>Numeric scale factor for the tile. Higher values produce larger tiles. Default value is None.</td>
</tr>
<tr id="parameter-scan_limit">
    <td><CopyableCode code="scan_limit" /></td>
    <td><code>integer</code></td>
    <td>Return as soon as we scan N items (defaults to 10000). Default value is None.</td>
</tr>
<tr id="parameter-sel_method">
    <td><CopyableCode code="sel_method" /></td>
    <td><code>string</code></td>
    <td>Xarray indexing method to use for inexact matches. Known values are: "nearest", "linear", "bilinear", "cubic", "cubic_spline", "lanczos", "area", and "mode". Default value is None.</td>
</tr>
<tr id="parameter-skipcovered">
    <td><CopyableCode code="skipcovered" /></td>
    <td><code>boolean</code></td>
    <td>Skip any items that would show up completely under the previous items (defaults to True). Default value is None.</td>
</tr>
<tr id="parameter-sortby">
    <td><CopyableCode code="sortby" /></td>
    <td><code>string</code></td>
    <td>Sorting expression (e.g. +/-property). Default value is None.</td>
</tr>
<tr id="parameter-subdataset_bands">
    <td><CopyableCode code="subdataset_bands" /></td>
    <td><code>array</code></td>
    <td>The index of a subdataset band within the asset. Default value is None.</td>
</tr>
<tr id="parameter-subdataset_name">
    <td><CopyableCode code="subdataset_name" /></td>
    <td><code>string</code></td>
    <td>The name of a subdataset within the asset. Default value is None.</td>
</tr>
<tr id="parameter-tile_format">
    <td><CopyableCode code="tile_format" /></td>
    <td><code>string</code></td>
    <td>Default will be automatically defined if the output image needs a mask (png) or not (jpeg). Known values are: "png", "npy", "tif", "jpeg", "jpg", "jp2", "webp", and "pngraw". Default value is None.</td>
</tr>
<tr id="parameter-tile_scale">
    <td><CopyableCode code="tile_scale" /></td>
    <td><code>integer</code></td>
    <td>Tile scale factor affecting output size. Values &gt; 1 produce larger tiles (e.g., 1=256x256, 2=512x512). Default value is None.</td>
</tr>
<tr id="parameter-time_limit">
    <td><CopyableCode code="time_limit" /></td>
    <td><code>integer</code></td>
    <td>Return after N seconds to avoid long requests (defaults to 5). Default value is None.</td>
</tr>
<tr id="parameter-trim_end">
    <td><CopyableCode code="trim_end" /></td>
    <td><code>integer</code></td>
    <td>Number of items to trim from the end of the cmap. Default value is None.</td>
</tr>
<tr id="parameter-trim_start">
    <td><CopyableCode code="trim_start" /></td>
    <td><code>integer</code></td>
    <td>Number of items to trim from the start of the cmap. Default value is None.</td>
</tr>
<tr id="parameter-unscale">
    <td><CopyableCode code="unscale" /></td>
    <td><code>boolean</code></td>
    <td>Apply internal Scale or Offset. Default value is None.</td>
</tr>
<tr id="parameter-width">
    <td><CopyableCode code="width" /></td>
    <td><code>integer</code></td>
    <td>Width in pixels for the output image. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_search_assets_for_tile"
    values={[
        { label: 'get_search_assets_for_tile', value: 'get_search_assets_for_tile' },
        { label: 'get_collection_assets_for_tile', value: 'get_collection_assets_for_tile' },
        { label: 'get_item_point', value: 'get_item_point' },
        { label: 'get_tileset_metadata', value: 'get_tileset_metadata' },
        { label: 'get_collection_point', value: 'get_collection_point' },
        { label: 'get_search_point', value: 'get_search_point' },
        { label: 'get_tilesets', value: 'get_tilesets' },
        { label: 'get_collection_tileset_metadata', value: 'get_collection_tileset_metadata' },
        { label: 'get_search_tileset_metadata', value: 'get_search_tileset_metadata' },
        { label: 'get_tile_matrix_definitions', value: 'get_tile_matrix_definitions' },
        { label: 'get_collection_tilesets', value: 'get_collection_tilesets' },
        { label: 'get_search_tilesets', value: 'get_search_tilesets' }
    ]}
>
<TabItem value="get_search_assets_for_tile">

Searches Assets For Tile Tilematrixsetid As Path. Return a list of assets which overlap a given tile.

```sql
SELECT
id,
assets,
bbox,
collection
FROM azure.planetarycomputer_dataplane.data
WHERE search_id = '{{ search_id }}' -- required
AND tile_matrix_set_id = '{{ tile_matrix_set_id }}' -- required
AND z = '{{ z }}' -- required
AND x = '{{ x }}' -- required
AND y = '{{ y }}' -- required
AND collection = '{{ collection }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND scan_limit = '{{ scan_limit }}'
AND items_limit = '{{ items_limit }}'
AND time_limit = '{{ time_limit }}'
AND exitwhenfull = '{{ exitwhenfull }}'
AND skipcovered = '{{ skipcovered }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_collection_assets_for_tile">

Collection Assets For Tile Tilematrixsetid As Path. Return a list of assets which overlap a given tile for a STAC collection (with TileMatrixSetId).

```sql
SELECT
id,
assets,
bbox,
collection
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND tile_matrix_set_id = '{{ tile_matrix_set_id }}' -- required
AND z = '{{ z }}' -- required
AND x = '{{ x }}' -- required
AND y = '{{ y }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND scan_limit = '{{ scan_limit }}'
AND items_limit = '{{ items_limit }}'
AND time_limit = '{{ time_limit }}'
AND exitwhenfull = '{{ exitwhenfull }}'
AND skipcovered = '{{ skipcovered }}'
AND ids = '{{ ids }}'
AND bbox = '{{ bbox }}'
AND query = '{{ query }}'
AND sortby = '{{ sortby }}'
AND datetime = '{{ datetime }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_point">

Item Point. Get point value for a STAC item dataset.

```sql
SELECT
band_names,
coordinates,
values
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND item_id = '{{ item_id }}' -- required
AND longitude = '{{ longitude }}' -- required
AND latitude = '{{ latitude }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND expression = '{{ expression }}'
AND asset_bidx = '{{ asset_bidx }}'
AND asset_as_band = '{{ asset_as_band }}'
AND nodata = '{{ nodata }}'
AND unscale = '{{ unscale }}'
AND reproject = '{{ reproject }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
AND coord_crs = '{{ coord_crs }}'
AND resampling = '{{ resampling }}'
;
```
</TabItem>
<TabItem value="get_tileset_metadata">

Tileset Metadata. Return metadata for a specific tileset of a STAC item.

```sql
SELECT
accessConstraints,
boundingBox,
crs,
dataType,
links,
tileMatrixSetLimits,
title
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND item_id = '{{ item_id }}' -- required
AND tile_matrix_set_id = '{{ tile_matrix_set_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_collection_point">

Collection Point. Get Point value for a collection dataset.

```sql
SELECT
band_names,
coordinates,
values
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND longitude = '{{ longitude }}' -- required
AND latitude = '{{ latitude }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND scan_limit = '{{ scan_limit }}'
AND items_limit = '{{ items_limit }}'
AND time_limit = '{{ time_limit }}'
AND exitwhenfull = '{{ exitwhenfull }}'
AND skipcovered = '{{ skipcovered }}'
AND ids = '{{ ids }}'
AND bbox = '{{ bbox }}'
AND query = '{{ query }}'
AND sortby = '{{ sortby }}'
AND datetime = '{{ datetime }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND sel_method = '{{ sel_method }}'
AND expression = '{{ expression }}'
AND asset_bidx = '{{ asset_bidx }}'
AND asset_as_band = '{{ asset_as_band }}'
AND nodata = '{{ nodata }}'
AND unscale = '{{ unscale }}'
AND reproject = '{{ reproject }}'
AND coord_crs = '{{ coord_crs }}'
AND resampling = '{{ resampling }}'
;
```
</TabItem>
<TabItem value="get_search_point">

Searches Point. Get Point value for a search dataset.

```sql
SELECT
band_names,
coordinates,
values
FROM azure.planetarycomputer_dataplane.data
WHERE search_id = '{{ search_id }}' -- required
AND longitude = '{{ longitude }}' -- required
AND latitude = '{{ latitude }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND scan_limit = '{{ scan_limit }}'
AND items_limit = '{{ items_limit }}'
AND time_limit = '{{ time_limit }}'
AND exitwhenfull = '{{ exitwhenfull }}'
AND skipcovered = '{{ skipcovered }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
AND expression = '{{ expression }}'
AND asset_bidx = '{{ asset_bidx }}'
AND asset_as_band = '{{ asset_as_band }}'
AND nodata = '{{ nodata }}'
AND unscale = '{{ unscale }}'
AND reproject = '{{ reproject }}'
AND coord_crs = '{{ coord_crs }}'
AND resampling = '{{ resampling }}'
;
```
</TabItem>
<TabItem value="get_tilesets">

Tileset List. Return a list of available tilesets for a STAC item.

```sql
SELECT
tilesets
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND item_id = '{{ item_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_collection_tileset_metadata">

Collection Tileset Metadata. Return metadata for a specific tileset of a STAC collection.

```sql
SELECT
accessConstraints,
boundingBox,
crs,
dataType,
links,
tileMatrixSetLimits,
title
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND tile_matrix_set_id = '{{ tile_matrix_set_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND ids = '{{ ids }}'
AND bbox = '{{ bbox }}'
AND query = '{{ query }}'
AND sortby = '{{ sortby }}'
AND datetime = '{{ datetime }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_search_tileset_metadata">

Searches Tileset Metadata. Return metadata for a specific tileset of a mosaic search.

```sql
SELECT
accessConstraints,
boundingBox,
crs,
dataType,
links,
tileMatrixSetLimits,
title
FROM azure.planetarycomputer_dataplane.data
WHERE search_id = '{{ search_id }}' -- required
AND tile_matrix_set_id = '{{ tile_matrix_set_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_matrix_definitions">

Matrix Definition. Return Matrix Definition.

```sql
SELECT
id,
boundingBox,
crs,
description,
keywords,
orderedAxes,
tileMatrices,
title,
uri,
wellKnownScaleSet
FROM azure.planetarycomputer_dataplane.data
WHERE tile_matrix_set_id = '{{ tile_matrix_set_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_collection_tilesets">

Collection Tileset List. Return a list of available tilesets for a STAC collection.

```sql
SELECT
tilesets
FROM azure.planetarycomputer_dataplane.data
WHERE collection_id = '{{ collection_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND ids = '{{ ids }}'
AND bbox = '{{ bbox }}'
AND query = '{{ query }}'
AND sortby = '{{ sortby }}'
AND datetime = '{{ datetime }}'
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_search_tilesets">

Searches Tileset List. Return a list of available tilesets for a mosaic search.

```sql
SELECT
tilesets
FROM azure.planetarycomputer_dataplane.data
WHERE search_id = '{{ search_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND subdataset_name = '{{ subdataset_name }}'
AND subdataset_bands = '{{ subdataset_bands }}'
AND crs = '{{ crs }}'
AND datetime = '{{ datetime }}'
AND sel_method = '{{ sel_method }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_tile_matrices"
    values={[
        { label: 'get_tile_matrices', value: 'get_tile_matrices' },
        { label: 'get_class_map_legend', value: 'get_class_map_legend' },
        { label: 'get_interval_legend', value: 'get_interval_legend' },
        { label: 'get_legend', value: 'get_legend' },
        { label: 'get_tile', value: 'get_tile' },
        { label: 'get_tile_by_format', value: 'get_tile_by_format' },
        { label: 'get_tile_by_scale', value: 'get_tile_by_scale' },
        { label: 'get_tile_by_scale_and_format', value: 'get_tile_by_scale_and_format' },
        { label: 'get_tile_no_tms', value: 'get_tile_no_tms' },
        { label: 'get_tile_no_tms_by_format', value: 'get_tile_no_tms_by_format' },
        { label: 'get_tile_no_tms_by_scale', value: 'get_tile_no_tms_by_scale' },
        { label: 'get_tile_no_tms_by_scale_and_format', value: 'get_tile_no_tms_by_scale_and_format' },
        { label: 'get_item_bounds', value: 'get_item_bounds' },
        { label: 'get_item_info', value: 'get_item_info' },
        { label: 'get_item_info_geo_json', value: 'get_item_info_geo_json' },
        { label: 'get_item_available_assets', value: 'get_item_available_assets' },
        { label: 'get_item_asset_statistics', value: 'get_item_asset_statistics' },
        { label: 'get_item_statistics', value: 'get_item_statistics' },
        { label: 'get_item_feature_statistics', value: 'get_item_feature_statistics' },
        { label: 'get_item_tile_json', value: 'get_item_tile_json' },
        { label: 'get_item_tile_json_by_tms', value: 'get_item_tile_json_by_tms' },
        { label: 'get_item_wmts_capabilities', value: 'get_item_wmts_capabilities' },
        { label: 'get_item_wmts_capabilities_by_tms', value: 'get_item_wmts_capabilities_by_tms' },
        { label: 'get_item_preview', value: 'get_item_preview' },
        { label: 'get_item_preview_with_format', value: 'get_item_preview_with_format' },
        { label: 'get_item_bbox_crop', value: 'get_item_bbox_crop' },
        { label: 'get_item_bbox_crop_with_dimensions', value: 'get_item_bbox_crop_with_dimensions' },
        { label: 'get_collection_tile_by_scale_and_format', value: 'get_collection_tile_by_scale_and_format' },
        { label: 'get_collection_tile', value: 'get_collection_tile' },
        { label: 'get_collection_tile_by_format', value: 'get_collection_tile_by_format' },
        { label: 'get_collection_tile_by_scale', value: 'get_collection_tile_by_scale' },
        { label: 'get_collection_tile_no_tms_by_scale_and_format', value: 'get_collection_tile_no_tms_by_scale_and_format' },
        { label: 'get_collection_tile_no_tms', value: 'get_collection_tile_no_tms' },
        { label: 'get_collection_tile_no_tms_by_format', value: 'get_collection_tile_no_tms_by_format' },
        { label: 'get_collection_tile_no_tms_by_scale', value: 'get_collection_tile_no_tms_by_scale' },
        { label: 'get_collection_tile_json', value: 'get_collection_tile_json' },
        { label: 'get_collection_tile_json_by_tms', value: 'get_collection_tile_json_by_tms' },
        { label: 'get_collection_wmts_capabilities', value: 'get_collection_wmts_capabilities' },
        { label: 'get_collection_wmts_capabilities_by_tms', value: 'get_collection_wmts_capabilities_by_tms' },
        { label: 'get_collection_assets_for_tile_no_tms', value: 'get_collection_assets_for_tile_no_tms' },
        { label: 'get_collection_assets_for_bbox', value: 'get_collection_assets_for_bbox' },
        { label: 'get_collection_info', value: 'get_collection_info' },
        { label: 'get_collection_bbox_crop', value: 'get_collection_bbox_crop' },
        { label: 'get_collection_bbox_crop_with_dimensions', value: 'get_collection_bbox_crop_with_dimensions' },
        { label: 'get_collection_point_assets', value: 'get_collection_point_assets' },
        { label: 'get_search_tile_by_scale_and_format', value: 'get_search_tile_by_scale_and_format' },
        { label: 'get_search_tile', value: 'get_search_tile' },
        { label: 'get_search_tile_by_format', value: 'get_search_tile_by_format' },
        { label: 'get_search_tile_by_scale', value: 'get_search_tile_by_scale' },
        { label: 'get_search_tile_json_by_tms', value: 'get_search_tile_json_by_tms' },
        { label: 'get_search_wmts_capabilities_by_tms', value: 'get_search_wmts_capabilities_by_tms' },
        { label: 'get_search_info', value: 'get_search_info' },
        { label: 'get_search_bbox_crop', value: 'get_search_bbox_crop' },
        { label: 'get_search_bbox_crop_with_dimensions', value: 'get_search_bbox_crop_with_dimensions' },
        { label: 'get_search_bbox_assets', value: 'get_search_bbox_assets' },
        { label: 'get_search_wmts_capabilities', value: 'get_search_wmts_capabilities' },
        { label: 'get_search_tile_json', value: 'get_search_tile_json' },
        { label: 'get_search_tile_no_tms', value: 'get_search_tile_no_tms' },
        { label: 'get_search_tile_no_tms_by_format', value: 'get_search_tile_no_tms_by_format' },
        { label: 'get_search_tile_no_tms_by_scale', value: 'get_search_tile_no_tms_by_scale' },
        { label: 'get_search_tile_no_tms_by_scale_and_format', value: 'get_search_tile_no_tms_by_scale_and_format' },
        { label: 'get_search_assets_for_tile_no_tms', value: 'get_search_assets_for_tile_no_tms' },
        { label: 'get_search_point_with_assets', value: 'get_search_point_with_assets' },
        { label: 'register_mosaics_search', value: 'register_mosaics_search' },
        { label: 'crop_feature', value: 'crop_feature' },
        { label: 'crop_feature_by_format', value: 'crop_feature_by_format' },
        { label: 'crop_feature_width_by_height', value: 'crop_feature_width_by_height' },
        { label: 'crop_collection_feature', value: 'crop_collection_feature' },
        { label: 'crop_collection_feature_by_format', value: 'crop_collection_feature_by_format' },
        { label: 'crop_collection_feature_width_by_height', value: 'crop_collection_feature_width_by_height' },
        { label: 'crop_search_feature', value: 'crop_search_feature' },
        { label: 'crop_search_feature_by_format', value: 'crop_search_feature_by_format' },
        { label: 'crop_search_feature_width_by_height', value: 'crop_search_feature_width_by_height' }
    ]}
>
<TabItem value="get_tile_matrices">

Matrix List. Return Matrix List.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_matrices 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_class_map_legend">

Get ClassMap Legend. Generate values and color swatches mapping for a given classmap.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_class_map_legend 
@classmap_name='{{ classmap_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@trim_start='{{ trim_start }}', 
@trim_end='{{ trim_end }}'
;
```
</TabItem>
<TabItem value="get_interval_legend">

Get Interval Legend. Generate values and color swatches mapping for a given interval classmap. Returns a color map for intervals, where each interval is defined by a numeric range [min, max] representing the interval boundaries and an RGBA color [red, green, blue, alpha] associated with the interval. The response is a 2D array of interval definitions, where each element is a pair: the first element is an array of two numbers [min, max] defining the interval, and the second element is an array of four numbers [red, green, blue, alpha] defining the RGBA color. Example: [[ [-2, 0], [0, 0, 0, 0] ], [ [1, 32], [255, 255, 178, 255] ]]. This defines two intervals: [-2, 0] mapped to transparent black and [1, 32] mapped to opaque yellow.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_interval_legend 
@classmap_name='{{ classmap_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@trim_start='{{ trim_start }}', 
@trim_end='{{ trim_end }}'
;
```
</TabItem>
<TabItem value="get_legend">

Get Legend. Generate a legend image for a given colormap. If the colormap has non-contiguous values at the beginning or end, which aren't desired in the output image, they can be trimmed by specifying the number of values to trim.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_legend 
@color_map_name='{{ color_map_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@height='{{ height }}', 
@width='{{ width }}', 
@trim_start='{{ trim_start }}', 
@trim_end='{{ trim_end }}'
;
```
</TabItem>
<TabItem value="get_tile">

Tile Tilematrixsetid Plain. Create map tile from a dataset (without scale or format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_by_format">

Tile Tilematrixsetid Format. Create map tile from a dataset (with format in path, without scale).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_by_format 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_by_scale">

Tile Tilematrixsetid Scale. Create map tile from a dataset (with scale in path, without format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_by_scale 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_by_scale_and_format">

Tile Tilematrixsetid. Create map tile from a dataset (with TileMatrixSetId, scale, and format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_by_scale_and_format 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_no_tms">

Tile Plain. Create map tile from a dataset (without TileMatrixSetId, scale or format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_no_tms 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@format='{{ format }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_no_tms_by_format">

Tile Format. Create map tile from a dataset (with format in path, without TileMatrixSetId or scale).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_no_tms_by_format 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_no_tms_by_scale">

Tile Scale. Create map tile from a dataset (with scale in path, without TileMatrixSetId or format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_no_tms_by_scale 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@format='{{ format }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_tile_no_tms_by_scale_and_format">

Tile. Create map tile from a dataset (with scale and format in path, without TileMatrixSetId).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_tile_no_tms_by_scale_and_format 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_bounds">

Item Bounds. Return the bounds for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_bounds 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_info">

Item Info. Return dataset's basic info for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_info 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_info_geo_json">

Item Info Geojson. Return info as GeoJSON for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_info_geo_json 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_available_assets">

Item Available Assets. Return a list of supported assets for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_available_assets 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_asset_statistics">

Item Asset Statistics. Per asset statistics for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_asset_statistics 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@asset_bidx='{{ asset_bidx }}', 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@categorical={{ categorical }}, 
@c='{{ c }}', 
@p='{{ p }}', 
@histogram_bins='{{ histogram_bins }}', 
@histogram_range='{{ histogram_range }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@asset_expression='{{ asset_expression }}', 
@height='{{ height }}', 
@width='{{ width }}'
;
```
</TabItem>
<TabItem value="get_item_statistics">

Item Statistics. Merged assets statistics for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_statistics 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@categorical={{ categorical }}, 
@c='{{ c }}', 
@p='{{ p }}', 
@histogram_bins='{{ histogram_bins }}', 
@histogram_range='{{ histogram_range }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@height='{{ height }}', 
@width='{{ width }}'
;
```
</TabItem>
<TabItem value="get_item_feature_statistics">

Item Geojson Statistics. Get statistics from a GeoJSON feature for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_feature_statistics 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@coord_crs='{{ coord_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@categorical={{ categorical }}, 
@c='{{ c }}', 
@p='{{ p }}', 
@histogram_bins='{{ histogram_bins }}', 
@histogram_range='{{ histogram_range }}', 
@dst_crs='{{ dst_crs }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@height='{{ height }}', 
@width='{{ width }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_item_tile_json">

Item TileJson. Return TileJSON document for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_tile_json 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_tile_json_by_tms">

Item TileJson Tilematrixsetid As Path. Return TileJSON document for a STAC item with TileMatrixSetId as path.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_tile_json_by_tms 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_wmts_capabilities">

Item Wmts. OGC WMTS endpoint for a STAC item.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_wmts_capabilities 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_wmts_capabilities_by_tms">

Item Wmts Tilematrixsetid As Path. OGC WMTS endpoint for a STAC item with TileMatrixSetId as path.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_wmts_capabilities_by_tms 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@resampling='{{ resampling }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_preview">

Item Preview. Create preview of a STAC item dataset.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_preview 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@color_formula='{{ color_formula }}', 
@dst_crs='{{ dst_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_preview_with_format">

Item Preview With Format. Create preview of a STAC item dataset with format.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_preview_with_format 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@color_formula='{{ color_formula }}', 
@dst_crs='{{ dst_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_bbox_crop">

Item Bbox. Create an image from part of a STAC item dataset (bounding box crop).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_bbox_crop 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@color_formula='{{ color_formula }}', 
@coord_crs='{{ coord_crs }}', 
@dst_crs='{{ dst_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_item_bbox_crop_with_dimensions">

Item Bbox With Dimensions. Create an image from part of a STAC item dataset (bounding box crop with dimensions).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_item_bbox_crop_with_dimensions 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@width='{{ width }}' --required, 
@height='{{ height }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@color_formula='{{ color_formula }}', 
@coord_crs='{{ coord_crs }}', 
@dst_crs='{{ dst_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_by_scale_and_format">

Collection Tile Tilematrixsetid. Create map tile for a STAC collection (with TileMatrixSetId, scale, and format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_by_scale_and_format 
@collection_id='{{ collection_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile">

Collection Tile Tilematrixsetid Plain. Create map tile for a STAC collection (with TileMatrixSetId, without scale or format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile 
@collection_id='{{ collection_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_by_format">

Collection Tile Tilematrixsetid Format. Create map tile for a STAC collection (with TileMatrixSetId and format, without scale).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_by_format 
@collection_id='{{ collection_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_by_scale">

Collection Tile Tilematrixsetid Scale. Create map tile for a STAC collection (with TileMatrixSetId and scale, without format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_by_scale 
@collection_id='{{ collection_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_no_tms_by_scale_and_format">

Collection Tile. Create map tile for a STAC collection (without TileMatrixSetId, with scale and format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_no_tms_by_scale_and_format 
@collection_id='{{ collection_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_no_tms">

Collection Tile Plain. Create map tile for a STAC collection (without TileMatrixSetId, scale, or format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_no_tms 
@collection_id='{{ collection_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@format='{{ format }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_no_tms_by_format">

Collection Tile Format. Create map tile for a STAC collection (with format, without TileMatrixSetId or scale).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_no_tms_by_format 
@collection_id='{{ collection_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_no_tms_by_scale">

Collection Tile Scale. Create map tile for a STAC collection (with scale, without TileMatrixSetId or format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_no_tms_by_scale 
@collection_id='{{ collection_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@format='{{ format }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_json">

Collection TileJson. Return TileJSON document for a STAC collection.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_json 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_tile_json_by_tms">

Collection TileJson Tilematrixsetid As Path. Return TileJSON document for a STAC collection with TileMatrixSetId as path.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_tile_json_by_tms 
@collection_id='{{ collection_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_collection_wmts_capabilities">

Collection Wmts. OGC WMTS endpoint for a STAC collection.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_wmts_capabilities 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}'
;
```
</TabItem>
<TabItem value="get_collection_wmts_capabilities_by_tms">

Collection Wmts Tilematrixsetid As Path. OGC WMTS endpoint for a STAC collection with TileMatrixSetId as path.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_wmts_capabilities_by_tms 
@collection_id='{{ collection_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}'
;
```
</TabItem>
<TabItem value="get_collection_assets_for_tile_no_tms">

Collection Assets For Tile. Return a list of assets which overlap a given tile for a STAC collection (without TileMatrixSetId).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_assets_for_tile_no_tms 
@collection_id='{{ collection_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}'
;
```
</TabItem>
<TabItem value="get_collection_assets_for_bbox">

Collection Assets For Bbox. Return a list of assets which overlap a given bounding box for a STAC collection.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_assets_for_bbox 
@collection_id='{{ collection_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@coord_crs='{{ coord_crs }}'
;
```
</TabItem>
<TabItem value="get_collection_info">

Collection Info. Return search query info from a STAC collection identifier.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_info 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_collection_bbox_crop">

Collection Bbox. Create an image from part of a STAC collection dataset (bounding box crop).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_bbox_crop 
@collection_id='{{ collection_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@dst_crs='{{ dst_crs }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}
;
```
</TabItem>
<TabItem value="get_collection_bbox_crop_with_dimensions">

Collection Bbox With Dimensions. Create an image from part of a STAC collection dataset (bounding box crop with dimensions).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_bbox_crop_with_dimensions 
@collection_id='{{ collection_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@width='{{ width }}' --required, 
@height='{{ height }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@dst_crs='{{ dst_crs }}', 
@max_size='{{ max_size }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}
;
```
</TabItem>
<TabItem value="get_collection_point_assets">

Collection Point Assets. Return a list of assets for a given point in a collection.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_collection_point_assets 
@collection_id='{{ collection_id }}' --required, 
@longitude='{{ longitude }}' --required, 
@latitude='{{ latitude }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@coord_crs='{{ coord_crs }}'
;
```
</TabItem>
<TabItem value="get_search_tile_by_scale_and_format">

Searches Tile Tilematrixsetid. Create map tile (with TileMatrixSetId, scale, and format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_by_scale_and_format 
@search_id='{{ search_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile">

Searches Tile Tilematrixsetid Plain. Create map tile (with TileMatrixSetId, without scale or format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile 
@search_id='{{ search_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile_by_format">

Searches Tile Tilematrixsetid Format. Create map tile (with TileMatrixSetId and format, without scale).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_by_format 
@search_id='{{ search_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile_by_scale">

Searches Tile Tilematrixsetid Scale. Create map tile (with TileMatrixSetId and scale, without format).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_by_scale 
@search_id='{{ search_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@format='{{ format }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile_json_by_tms">

Searches TileJson Tilematrixsetid As Path. Return TileJSON document for a search with TileMatrixSetId as path.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_json_by_tms 
@search_id='{{ search_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_wmts_capabilities_by_tms">

Searches Wmts Tilematrixsetid As Path. OGC WMTS endpoint with TileMatrixSetId as path.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_wmts_capabilities_by_tms 
@search_id='{{ search_id }}' --required, 
@tile_matrix_set_id='{{ tile_matrix_set_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}'
;
```
</TabItem>
<TabItem value="get_search_info">

Searches Info. Get Search query metadata.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_info 
@search_id='{{ search_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_search_bbox_crop">

Searches Bbox. Create an image from part of a dataset (bounding box crop).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_bbox_crop 
@search_id='{{ search_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@dst_crs='{{ dst_crs }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}
;
```
</TabItem>
<TabItem value="get_search_bbox_crop_with_dimensions">

Searches Bbox With Dimensions. Create an image from part of a dataset (bounding box crop with dimensions).

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_bbox_crop_with_dimensions 
@search_id='{{ search_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@width='{{ width }}' --required, 
@height='{{ height }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@dst_crs='{{ dst_crs }}', 
@max_size='{{ max_size }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}
;
```
</TabItem>
<TabItem value="get_search_bbox_assets">

Searches Assets For Bbox. Return a list of assets which overlap a given bounding box for a search.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_bbox_assets 
@search_id='{{ search_id }}' --required, 
@minx='{{ minx }}' --required, 
@miny='{{ miny }}' --required, 
@maxx='{{ maxx }}' --required, 
@maxy='{{ maxy }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@coord_crs='{{ coord_crs }}'
;
```
</TabItem>
<TabItem value="get_search_wmts_capabilities">

Searches Wmts. OGC WMTS endpoint.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_wmts_capabilities 
@search_id='{{ search_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}'
;
```
</TabItem>
<TabItem value="get_search_tile_json">

Searches TileJson. Return TileJSON document for a search.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_json 
@search_id='{{ search_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@tile_format='{{ tile_format }}', 
@tile_scale='{{ tile_scale }}', 
@minzoom='{{ minzoom }}', 
@maxzoom='{{ maxzoom }}', 
@padding='{{ padding }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}
;
```
</TabItem>
<TabItem value="get_search_tile_no_tms">

Searches Tile Plain. The most basic operation.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_no_tms 
@search_id='{{ search_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@format='{{ format }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile_no_tms_by_format">

Searches Tile Format. The most basic operation.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_no_tms_by_format 
@search_id='{{ search_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@scale='{{ scale }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile_no_tms_by_scale">

Searches Tile Scale. The most basic operation.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_no_tms_by_scale 
@search_id='{{ search_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@format='{{ format }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_tile_no_tms_by_scale_and_format">

Searches Tile. The most basic operation.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_tile_no_tms_by_scale_and_format 
@search_id='{{ search_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@scale='{{ scale }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}', 
@buffer='{{ buffer }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@padding='{{ padding }}'
;
```
</TabItem>
<TabItem value="get_search_assets_for_tile_no_tms">

Searches Assets For Tile. The most basic operation.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_assets_for_tile_no_tms 
@search_id='{{ search_id }}' --required, 
@z='{{ z }}' --required, 
@x='{{ x }}' --required, 
@y='{{ y }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@TileMatrixSetId='{{ TileMatrixSetId }}'
;
```
</TabItem>
<TabItem value="get_search_point_with_assets">

Searches Point Assets. Return a list of assets for a given point in a search.

```sql
EXEC azure.planetarycomputer_dataplane.data.get_search_point_with_assets 
@search_id='{{ search_id }}' --required, 
@longitude='{{ longitude }}' --required, 
@latitude='{{ latitude }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@coord_crs='{{ coord_crs }}'
;
```
</TabItem>
<TabItem value="register_mosaics_search">

Register Search. Register a Search query.

```sql
EXEC azure.planetarycomputer_dataplane.data.register_mosaics_search 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="crop_feature">

Geojson Feature. Create image from a geojson feature (without format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_feature 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@color_formula='{{ color_formula }}', 
@coord_crs='{{ coord_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@format='{{ format }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_feature_by_format">

Geojson Feature Crop With Format. Create image from a geojson feature with format.

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_feature_by_format 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@color_formula='{{ color_formula }}', 
@coord_crs='{{ coord_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_feature_width_by_height">

Geojson Feature Crop With Dimensions. Create image from a geojson feature with dimensions.

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_feature_width_by_height 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@width='{{ width }}' --required, 
@height='{{ height }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@color_formula='{{ color_formula }}', 
@coord_crs='{{ coord_crs }}', 
@resampling='{{ resampling }}', 
@max_size='{{ max_size }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_collection_feature">

Collection Geojson Feature. Create image from a geojson feature (without format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_collection_feature 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}', 
@format='{{ format }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_collection_feature_by_format">

Collection Geojson Feature Crop With Format. Create image from a geojson feature with format.

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_collection_feature_by_format 
@collection_id='{{ collection_id }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_collection_feature_width_by_height">

Collection Geojson Feature Crop With Dimensions. Create image from a geojson feature with dimensions.

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_collection_feature_width_by_height 
@collection_id='{{ collection_id }}' --required, 
@width='{{ width }}' --required, 
@height='{{ height }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@ids='{{ ids }}', 
@bbox='{{ bbox }}', 
@query='{{ query }}', 
@sortby='{{ sortby }}', 
@datetime='{{ datetime }}', 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@max_size='{{ max_size }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_search_feature">

Searches Geojson Feature. Create image from a geojson feature (without format in path).

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_search_feature 
@search_id='{{ search_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}', 
@format='{{ format }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_search_feature_by_format">

Searches Geojson Feature Crop With Format. Create image from a geojson feature with format.

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_search_feature_by_format 
@search_id='{{ search_id }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@max_size='{{ max_size }}', 
@height='{{ height }}', 
@width='{{ width }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="crop_search_feature_width_by_height">

Searches Geojson Feature Crop With Dimensions. Create image from a geojson feature with dimensions.

```sql
EXEC azure.planetarycomputer_dataplane.data.crop_search_feature_width_by_height 
@search_id='{{ search_id }}' --required, 
@width='{{ width }}' --required, 
@height='{{ height }}' --required, 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@expression='{{ expression }}', 
@asset_bidx='{{ asset_bidx }}', 
@asset_as_band={{ asset_as_band }}, 
@nodata='{{ nodata }}', 
@unscale={{ unscale }}, 
@reproject='{{ reproject }}', 
@scan_limit='{{ scan_limit }}', 
@items_limit='{{ items_limit }}', 
@time_limit='{{ time_limit }}', 
@exitwhenfull={{ exitwhenfull }}, 
@skipcovered={{ skipcovered }}, 
@subdataset_name='{{ subdataset_name }}', 
@subdataset_bands='{{ subdataset_bands }}', 
@crs='{{ crs }}', 
@datetime='{{ datetime }}', 
@sel_method='{{ sel_method }}', 
@algorithm='{{ algorithm }}', 
@algorithm_params='{{ algorithm_params }}', 
@coord_crs='{{ coord_crs }}', 
@max_size='{{ max_size }}', 
@color_formula='{{ color_formula }}', 
@collection='{{ collection }}', 
@resampling='{{ resampling }}', 
@pixel_selection='{{ pixel_selection }}', 
@colormap_name='{{ colormap_name }}', 
@colormap='{{ colormap }}', 
@return_mask={{ return_mask }}, 
@dst_crs='{{ dst_crs }}' 
@@json=
'{
"geometry": "{{ geometry }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
