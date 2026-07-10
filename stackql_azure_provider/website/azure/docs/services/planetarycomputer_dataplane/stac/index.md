--- 
title: stac
hide_title: false
hide_table_of_contents: false
keywords:
  - stac
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

Creates, updates, deletes, gets or lists a <code>stac</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="stac" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.planetarycomputer_dataplane.stac" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_mosaic"
    values={[
        { label: 'get_mosaic', value: 'get_mosaic' },
        { label: 'get_render_option', value: 'get_render_option' },
        { label: 'get_item', value: 'get_item' },
        { label: 'get_collection_configuration', value: 'get_collection_configuration' },
        { label: 'get_collections', value: 'get_collections' }
    ]}
>
<TabItem value="get_mosaic">

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
    <td>Unique identifier for the mosaic. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Short descriptive name for the mosaic. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cql" /></td>
    <td><code>array</code></td>
    <td>A list of valid CQL2-JSON expressions used to filter the collection to moasic. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the mosaic.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_render_option">

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
    <td>Unique identifier for the render option. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Short descriptive name for the render option. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="conditions" /></td>
    <td><code>array</code></td>
    <td>A list of property/value conditions that must be in the active mosaic CQL for this render option to be enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A longer description of the render option that can be used to explain its content.</td>
</tr>
<tr>
    <td><CopyableCode code="legend" /></td>
    <td><code>object</code></td>
    <td>Legend configuration for this render option.</td>
</tr>
<tr>
    <td><CopyableCode code="minZoom" /></td>
    <td><code>integer</code></td>
    <td>Minimum zoom level at which to display this layer.</td>
</tr>
<tr>
    <td><CopyableCode code="options" /></td>
    <td><code>string</code></td>
    <td>A URL query-string encoded string of TiTiler rendering options. Valid only for `raster-tile` types. See `Query Parameters `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of rendering to apply (raster or vector). Known values are: "raster-tile", "vt-polygon", and "vt-line". (raster-tile, vt-polygon, vt-line)</td>
</tr>
<tr>
    <td><CopyableCode code="vectorOptions" /></td>
    <td><code>object</code></td>
    <td>Options for rendering vector tiles. Valid only for `vt-polygon` and `vt-line` types.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_item">

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
    <td><CopyableCode code="_msft:etag" /></td>
    <td><code>string</code></td>
    <td>MSFT ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="_msft:ts" /></td>
    <td><code>string (date-time)</code></td>
    <td>MSFT Timestamp.</td>
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
<tr>
    <td><CopyableCode code="constellation" /></td>
    <td><code>string</code></td>
    <td>Constellation of satellites that acquired the data.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation timestamp of the data.</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string</code></td>
    <td>Datetime the asset represents in RFC 3339 format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the item.</td>
</tr>
<tr>
    <td><CopyableCode code="end_datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the item observation period.</td>
</tr>
<tr>
    <td><CopyableCode code="geometry" /></td>
    <td><code>object</code></td>
    <td>Geometry object defining the feature's shape. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="gsd" /></td>
    <td><code>number</code></td>
    <td>Ground sample distance in meters.</td>
</tr>
<tr>
    <td><CopyableCode code="instruments" /></td>
    <td><code>array</code></td>
    <td>Instruments that acquired the data.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links to related resources and endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="mission" /></td>
    <td><code>string</code></td>
    <td>Mission associated with the data.</td>
</tr>
<tr>
    <td><CopyableCode code="msft:_created" /></td>
    <td><code>string (date-time)</code></td>
    <td>MSFT Created.</td>
</tr>
<tr>
    <td><CopyableCode code="msft:_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>MSFT Updated.</td>
</tr>
<tr>
    <td><CopyableCode code="msft:short_description" /></td>
    <td><code>string</code></td>
    <td>MSFT Short Description.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>Platform that acquired the data.</td>
</tr>
<tr>
    <td><CopyableCode code="providers" /></td>
    <td><code>array</code></td>
    <td>Organizations or individuals who provide the data.</td>
</tr>
<tr>
    <td><CopyableCode code="stac_extensions" /></td>
    <td><code>array</code></td>
    <td>URLs to STAC extensions implemented by this STAC resource.</td>
</tr>
<tr>
    <td><CopyableCode code="stac_version" /></td>
    <td><code>string</code></td>
    <td>Stac Version.</td>
</tr>
<tr>
    <td><CopyableCode code="start_datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the item observation period.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Human-readable title for the item.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>GeoJSON type identifier for Feature. Required. GeoJSON Feature type.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last update timestamp of the data.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_collection_configuration">

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
    <td><CopyableCode code="mosaicInfo" /></td>
    <td><code>object</code></td>
    <td>Settings for data mosaic visualization. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tileSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for map tile visualization. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_collections">

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
    <td><CopyableCode code="collections" /></td>
    <td><code>array</code></td>
    <td>Array of STAC collections available in the catalog. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Links to related resources and endpoints. Required.</td>
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
    <td><a href="#get_mosaic"><CopyableCode code="get_mosaic" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-mosaic_id"><code>mosaic_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Collection Mosaic. Get a mosaic definition from a given collection.</td>
</tr>
<tr>
    <td><a href="#get_render_option"><CopyableCode code="get_render_option" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-render_option_id"><code>render_option_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Collection Render Option. Get a render option for a given collection.</td>
</tr>
<tr>
    <td><a href="#get_item"><CopyableCode code="get_item" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-sign"><code>sign</code></a>, <a href="#parameter-duration"><code>duration</code></a></td>
    <td>Fetch a single STAC Item.</td>
</tr>
<tr>
    <td><a href="#get_collection_configuration"><CopyableCode code="get_collection_configuration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Config. Get the complete user configuration for a given collection.</td>
</tr>
<tr>
    <td><a href="#get_collections"><CopyableCode code="get_collections" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-sign"><code>sign</code></a>, <a href="#parameter-duration"><code>duration</code></a></td>
    <td>Get Collections. List all collections in the GeoCatalog instance.</td>
</tr>
<tr>
    <td><a href="#replace_mosaic"><CopyableCode code="replace_mosaic" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-mosaic_id"><code>mosaic_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-cql"><code>cql</code></a></td>
    <td></td>
    <td>Update Collection Mosaic. Update a mosaic definition from a given collection.</td>
</tr>
<tr>
    <td><a href="#delete_mosaic"><CopyableCode code="delete_mosaic" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-mosaic_id"><code>mosaic_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Collection Mosaic. Delete a mosaic definition from a given collection.</td>
</tr>
<tr>
    <td><a href="#get_mosaics"><CopyableCode code="get_mosaics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Collection Mosaics. Get the mosaic definitions for a given collection.</td>
</tr>
<tr>
    <td><a href="#add_mosaic"><CopyableCode code="add_mosaic" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-cql"><code>cql</code></a></td>
    <td></td>
    <td>Add Collection Mosaic. Add a mosaic definition to a given collection.</td>
</tr>
<tr>
    <td><a href="#get_collection"><CopyableCode code="get_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-sign"><code>sign</code></a>, <a href="#parameter-duration"><code>duration</code></a></td>
    <td>Get Collection. Get a collection in the GeoCatalog instance.</td>
</tr>
<tr>
    <td><a href="#replace_collection"><CopyableCode code="replace_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-links"><code>links</code></a>, <a href="#parameter-license"><code>license</code></a>, <a href="#parameter-extent"><code>extent</code></a></td>
    <td></td>
    <td>Replace Collection. Replace an existing collection in the GeoCatalog instance.</td>
</tr>
<tr>
    <td><a href="#delete_collection"><CopyableCode code="delete_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Collection. Delete a collection in the GeoCatalog instance.</td>
</tr>
<tr>
    <td><a href="#create_collection"><CopyableCode code="create_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-links"><code>links</code></a>, <a href="#parameter-license"><code>license</code></a>, <a href="#parameter-extent"><code>extent</code></a></td>
    <td></td>
    <td>Create Collection. Create a new collection in the GeoCatalog instance.</td>
</tr>
<tr>
    <td><a href="#get_partition_type"><CopyableCode code="get_partition_type" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Partitiontype. Get the partitiontype for a GeoCatalog Collection.</td>
</tr>
<tr>
    <td><a href="#replace_partition_type"><CopyableCode code="replace_partition_type" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create Partitiontype. Updates partition type for a GeoCatalog Collection. This will determine the partitioning scheme for items within the database, and can only be set before any items are loaded. Ideal partitioning schemes result in partitions of roughly 100k items each. The default partitioning scheme is "none" which does not partition items.</td>
</tr>
<tr>
    <td><a href="#replace_render_option"><CopyableCode code="replace_render_option" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-render_option_id"><code>render_option_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Update Collection Render Option. Update a render option for a given collection.</td>
</tr>
<tr>
    <td><a href="#delete_render_option"><CopyableCode code="delete_render_option" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-render_option_id"><code>render_option_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Collection Render Option. Delete a render option for a given collection.</td>
</tr>
<tr>
    <td><a href="#get_render_options"><CopyableCode code="get_render_options" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Collection Render Options. Get all render options for a given collection.</td>
</tr>
<tr>
    <td><a href="#create_render_option"><CopyableCode code="create_render_option" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Add Collection Render Option. Add a render option for a given collection.</td>
</tr>
<tr>
    <td><a href="#get_collection_thumbnail"><CopyableCode code="get_collection_thumbnail" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Collection Thumbnail. Get thumbnail for given collection.</td>
</tr>
<tr>
    <td><a href="#get_tile_settings"><CopyableCode code="get_tile_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Collection Tile Settings. Get the tile settings for a given collection.</td>
</tr>
<tr>
    <td><a href="#replace_tile_settings"><CopyableCode code="replace_tile_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-minZoom"><code>minZoom</code></a>, <a href="#parameter-maxItemsPerTile"><code>maxItemsPerTile</code></a></td>
    <td></td>
    <td>Update Collection Tile Settings. Update the tile settings for a given collection.</td>
</tr>
<tr>
    <td><a href="#get_conformance_classes"><CopyableCode code="get_conformance_classes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Conformance Classes. Returns the STAC conformance classes.</td>
</tr>
<tr>
    <td><a href="#get_landing_page"><CopyableCode code="get_landing_page" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Landing Page. Return the STAC landing page.</td>
</tr>
<tr>
    <td><a href="#replace_item"><CopyableCode code="replace_item" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-assets"><code>assets</code></a></td>
    <td></td>
    <td>Replace a STAC item in a collection.</td>
</tr>
<tr>
    <td><a href="#delete_item"><CopyableCode code="delete_item" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a STAC item from a collection.</td>
</tr>
<tr>
    <td><a href="#update_item"><CopyableCode code="update_item" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-geometry"><code>geometry</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-assets"><code>assets</code></a></td>
    <td></td>
    <td>Update a STAC item in a collection.</td>
</tr>
<tr>
    <td><a href="#get_item_collection"><CopyableCode code="get_item_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-datetime"><code>datetime</code></a>, <a href="#parameter-sign"><code>sign</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-token"><code>token</code></a></td>
    <td>Fetch features of the feature collection with id `collectionId`. Every feature in a dataset belongs to a collection. A dataset may consist of multiple feature collections. A feature collection is often a collection of features of a similar type, based on a common schema.</td>
</tr>
<tr>
    <td><a href="#create_item"><CopyableCode code="create_item" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create a new STAC item or a set of items in a collection.</td>
</tr>
<tr>
    <td><a href="#get_queryables"><CopyableCode code="get_queryables" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Queryables. List all queryables in the GeoCatalog instance.</td>
</tr>
<tr>
    <td><a href="#get_collection_queryables"><CopyableCode code="get_collection_queryables" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Collection Queryables. List all queryables in a given collection.</td>
</tr>
<tr>
    <td><a href="#create_queryables"><CopyableCode code="create_queryables" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-definition"><code>definition</code></a></td>
    <td></td>
    <td>Set Collection Queryables. Set queryables for a collection given a list of queryable definitions.</td>
</tr>
<tr>
    <td><a href="#create_collection_asset"><CopyableCode code="create_collection_asset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-data"><code>data</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>Create Collection Asset. Create a new asset in the Collection metadata and write the associated file to managed storage.</td>
</tr>
<tr>
    <td><a href="#replace_collection_asset"><CopyableCode code="replace_collection_asset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-asset_id"><code>asset_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-data"><code>data</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>Update Collection Asset. Update an existing asset in a given collection.</td>
</tr>
<tr>
    <td><a href="#delete_collection_asset"><CopyableCode code="delete_collection_asset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-asset_id"><code>asset_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Collection Asset. Delete an asset from a given collection.</td>
</tr>
<tr>
    <td><a href="#replace_queryable"><CopyableCode code="replace_queryable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-queryable_name"><code>queryable_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-definition"><code>definition</code></a></td>
    <td></td>
    <td>Update Collection Queryables. Updates a queryable given a queryable definition and corresponding collection id.</td>
</tr>
<tr>
    <td><a href="#delete_queryable"><CopyableCode code="delete_queryable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-collection_id"><code>collection_id</code></a>, <a href="#parameter-queryable_name"><code>queryable_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Queryables. Delete queryables by name for specified collection.</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-sign"><code>sign</code></a>, <a href="#parameter-duration"><code>duration</code></a></td>
    <td>Search. STAC search operation.</td>
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
<tr id="parameter-asset_id">
    <td><CopyableCode code="asset_id" /></td>
    <td><code>string</code></td>
    <td>STAC Asset ID. Required.</td>
</tr>
<tr id="parameter-collection_id">
    <td><CopyableCode code="collection_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the STAC collection. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-item_id">
    <td><CopyableCode code="item_id" /></td>
    <td><code>string</code></td>
    <td>STAC Item id. Required.</td>
</tr>
<tr id="parameter-mosaic_id">
    <td><CopyableCode code="mosaic_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the mosaic configuration. Required.</td>
</tr>
<tr id="parameter-queryable_name">
    <td><CopyableCode code="queryable_name" /></td>
    <td><code>string</code></td>
    <td>Name of the queryable property to operate on. Required.</td>
</tr>
<tr id="parameter-render_option_id">
    <td><CopyableCode code="render_option_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the render option. Required.</td>
</tr>
<tr id="parameter-bbox">
    <td><CopyableCode code="bbox" /></td>
    <td><code>array</code></td>
    <td>Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth): * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Minimum value, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Maximum value, coordinate axis 3 (optional) The coordinate reference system of the values is WGS 84 longitude/latitude (`http://www.opengis.net/def/crs/OGC/1.3/CRS84 `_). For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge). If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box. If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. Default value is None.</td>
</tr>
<tr id="parameter-datetime">
    <td><CopyableCode code="datetime" /></td>
    <td><code>string</code></td>
    <td>Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots. Examples: * A date-time: "2018-02-12T23:20:50Z" * A closed interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z" * Open intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z" Only features that have a temporal property that intersects the value of `datetime` are selected. If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties. Default value is None.</td>
</tr>
<tr id="parameter-duration">
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>URL signature duration in minutes. Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The optional limit parameter recommends the number of items that should be present in the response document. If the limit parameter value is greater than advertised limit maximum, the server must return the maximum possible number of items, rather than responding with an error. Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items must not be counted. Minimum = 1. Maximum = 10000. Default = 10. Default value is None.</td>
</tr>
<tr id="parameter-sign">
    <td><CopyableCode code="sign" /></td>
    <td><code>string</code></td>
    <td>Whether to sign asset URLs in the response. Known values are: "true" and "false". Default value is None.</td>
</tr>
<tr id="parameter-token">
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td>Pagination token for fetching the next set of results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_mosaic"
    values={[
        { label: 'get_mosaic', value: 'get_mosaic' },
        { label: 'get_render_option', value: 'get_render_option' },
        { label: 'get_item', value: 'get_item' },
        { label: 'get_collection_configuration', value: 'get_collection_configuration' },
        { label: 'get_collections', value: 'get_collections' }
    ]}
>
<TabItem value="get_mosaic">

Get Collection Mosaic. Get a mosaic definition from a given collection.

```sql
SELECT
id,
name,
cql,
description
FROM azure.planetarycomputer_dataplane.stac
WHERE collection_id = '{{ collection_id }}' -- required
AND mosaic_id = '{{ mosaic_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_render_option">

Get Collection Render Option. Get a render option for a given collection.

```sql
SELECT
id,
name,
conditions,
description,
legend,
minZoom,
options,
type,
vectorOptions
FROM azure.planetarycomputer_dataplane.stac
WHERE collection_id = '{{ collection_id }}' -- required
AND render_option_id = '{{ render_option_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_item">

Fetch a single STAC Item.

```sql
SELECT
id,
_msft:etag,
_msft:ts,
assets,
bbox,
collection,
constellation,
created,
datetime,
description,
end_datetime,
geometry,
gsd,
instruments,
links,
mission,
msft:_created,
msft:_updated,
msft:short_description,
platform,
providers,
stac_extensions,
stac_version,
start_datetime,
title,
type,
updated
FROM azure.planetarycomputer_dataplane.stac
WHERE collection_id = '{{ collection_id }}' -- required
AND item_id = '{{ item_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND sign = '{{ sign }}'
AND duration = '{{ duration }}'
;
```
</TabItem>
<TabItem value="get_collection_configuration">

Get Config. Get the complete user configuration for a given collection.

```sql
SELECT
mosaicInfo,
tileSettings
FROM azure.planetarycomputer_dataplane.stac
WHERE collection_id = '{{ collection_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_collections">

Get Collections. List all collections in the GeoCatalog instance.

```sql
SELECT
collections,
links
FROM azure.planetarycomputer_dataplane.stac
WHERE endpoint = '{{ endpoint }}' -- required
AND sign = '{{ sign }}'
AND duration = '{{ duration }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="replace_mosaic"
    values={[
        { label: 'replace_mosaic', value: 'replace_mosaic' },
        { label: 'delete_mosaic', value: 'delete_mosaic' },
        { label: 'get_mosaics', value: 'get_mosaics' },
        { label: 'add_mosaic', value: 'add_mosaic' },
        { label: 'get_collection', value: 'get_collection' },
        { label: 'replace_collection', value: 'replace_collection' },
        { label: 'delete_collection', value: 'delete_collection' },
        { label: 'create_collection', value: 'create_collection' },
        { label: 'get_partition_type', value: 'get_partition_type' },
        { label: 'replace_partition_type', value: 'replace_partition_type' },
        { label: 'replace_render_option', value: 'replace_render_option' },
        { label: 'delete_render_option', value: 'delete_render_option' },
        { label: 'get_render_options', value: 'get_render_options' },
        { label: 'create_render_option', value: 'create_render_option' },
        { label: 'get_collection_thumbnail', value: 'get_collection_thumbnail' },
        { label: 'get_tile_settings', value: 'get_tile_settings' },
        { label: 'replace_tile_settings', value: 'replace_tile_settings' },
        { label: 'get_conformance_classes', value: 'get_conformance_classes' },
        { label: 'get_landing_page', value: 'get_landing_page' },
        { label: 'replace_item', value: 'replace_item' },
        { label: 'delete_item', value: 'delete_item' },
        { label: 'update_item', value: 'update_item' },
        { label: 'get_item_collection', value: 'get_item_collection' },
        { label: 'create_item', value: 'create_item' },
        { label: 'get_queryables', value: 'get_queryables' },
        { label: 'get_collection_queryables', value: 'get_collection_queryables' },
        { label: 'create_queryables', value: 'create_queryables' },
        { label: 'create_collection_asset', value: 'create_collection_asset' },
        { label: 'replace_collection_asset', value: 'replace_collection_asset' },
        { label: 'delete_collection_asset', value: 'delete_collection_asset' },
        { label: 'replace_queryable', value: 'replace_queryable' },
        { label: 'delete_queryable', value: 'delete_queryable' },
        { label: 'search', value: 'search' }
    ]}
>
<TabItem value="replace_mosaic">

Update Collection Mosaic. Update a mosaic definition from a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_mosaic 
@collection_id='{{ collection_id }}' --required, 
@mosaic_id='{{ mosaic_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"name": "{{ name }}", 
"description": "{{ description }}", 
"cql": "{{ cql }}"
}'
;
```
</TabItem>
<TabItem value="delete_mosaic">

Delete Collection Mosaic. Delete a mosaic definition from a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.delete_mosaic 
@collection_id='{{ collection_id }}' --required, 
@mosaic_id='{{ mosaic_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_mosaics">

Get Collection Mosaics. Get the mosaic definitions for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_mosaics 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_mosaic">

Add Collection Mosaic. Add a mosaic definition to a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.add_mosaic 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"name": "{{ name }}", 
"description": "{{ description }}", 
"cql": "{{ cql }}"
}'
;
```
</TabItem>
<TabItem value="get_collection">

Get Collection. Get a collection in the GeoCatalog instance.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_collection 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@sign='{{ sign }}', 
@duration='{{ duration }}'
;
```
</TabItem>
<TabItem value="replace_collection">

Replace Collection. Replace an existing collection in the GeoCatalog instance.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_collection 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"msft:_created": "{{ msft:_created }}", 
"msft:_updated": "{{ msft:_updated }}", 
"msft:short_description": "{{ msft:short_description }}", 
"stac_extensions": "{{ stac_extensions }}", 
"id": "{{ id }}", 
"description": "{{ description }}", 
"stac_version": "{{ stac_version }}", 
"links": "{{ links }}", 
"title": "{{ title }}", 
"type": "{{ type }}", 
"assets": "{{ assets }}", 
"item_assets": "{{ item_assets }}", 
"license": "{{ license }}", 
"extent": "{{ extent }}", 
"keywords": "{{ keywords }}", 
"providers": "{{ providers }}", 
"summaries": "{{ summaries }}"
}'
;
```
</TabItem>
<TabItem value="delete_collection">

Delete Collection. Delete a collection in the GeoCatalog instance.

```sql
EXEC azure.planetarycomputer_dataplane.stac.delete_collection 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_collection">

Create Collection. Create a new collection in the GeoCatalog instance.

```sql
EXEC azure.planetarycomputer_dataplane.stac.create_collection 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"msft:_created": "{{ msft:_created }}", 
"msft:_updated": "{{ msft:_updated }}", 
"msft:short_description": "{{ msft:short_description }}", 
"stac_extensions": "{{ stac_extensions }}", 
"id": "{{ id }}", 
"description": "{{ description }}", 
"stac_version": "{{ stac_version }}", 
"links": "{{ links }}", 
"title": "{{ title }}", 
"type": "{{ type }}", 
"assets": "{{ assets }}", 
"item_assets": "{{ item_assets }}", 
"license": "{{ license }}", 
"extent": "{{ extent }}", 
"keywords": "{{ keywords }}", 
"providers": "{{ providers }}", 
"summaries": "{{ summaries }}"
}'
;
```
</TabItem>
<TabItem value="get_partition_type">

Get Partitiontype. Get the partitiontype for a GeoCatalog Collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_partition_type 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="replace_partition_type">

Create Partitiontype. Updates partition type for a GeoCatalog Collection. This will determine the partitioning scheme for items within the database, and can only be set before any items are loaded. Ideal partitioning schemes result in partitions of roughly 100k items each. The default partitioning scheme is "none" which does not partition items.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_partition_type 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"scheme": "{{ scheme }}"
}'
;
```
</TabItem>
<TabItem value="replace_render_option">

Update Collection Render Option. Update a render option for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_render_option 
@collection_id='{{ collection_id }}' --required, 
@render_option_id='{{ render_option_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"name": "{{ name }}", 
"description": "{{ description }}", 
"type": "{{ type }}", 
"options": "{{ options }}", 
"vectorOptions": "{{ vectorOptions }}", 
"minZoom": {{ minZoom }}, 
"legend": "{{ legend }}", 
"conditions": "{{ conditions }}"
}'
;
```
</TabItem>
<TabItem value="delete_render_option">

Delete Collection Render Option. Delete a render option for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.delete_render_option 
@collection_id='{{ collection_id }}' --required, 
@render_option_id='{{ render_option_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_render_options">

Get Collection Render Options. Get all render options for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_render_options 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_render_option">

Add Collection Render Option. Add a render option for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.create_render_option 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"name": "{{ name }}", 
"description": "{{ description }}", 
"type": "{{ type }}", 
"options": "{{ options }}", 
"vectorOptions": "{{ vectorOptions }}", 
"minZoom": {{ minZoom }}, 
"legend": "{{ legend }}", 
"conditions": "{{ conditions }}"
}'
;
```
</TabItem>
<TabItem value="get_collection_thumbnail">

Get Collection Thumbnail. Get thumbnail for given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_collection_thumbnail 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_tile_settings">

Get Collection Tile Settings. Get the tile settings for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_tile_settings 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="replace_tile_settings">

Update Collection Tile Settings. Update the tile settings for a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_tile_settings 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"minZoom": {{ minZoom }}, 
"maxItemsPerTile": {{ maxItemsPerTile }}, 
"defaultLocation": "{{ defaultLocation }}"
}'
;
```
</TabItem>
<TabItem value="get_conformance_classes">

Conformance Classes. Returns the STAC conformance classes.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_conformance_classes 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_landing_page">

Landing Page. Return the STAC landing page.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_landing_page 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="replace_item">

Replace a STAC item in a collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_item 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"type": "{{ type }}", 
"stac_version": "{{ stac_version }}", 
"links": "{{ links }}", 
"msft:_created": "{{ msft:_created }}", 
"msft:_updated": "{{ msft:_updated }}", 
"msft:short_description": "{{ msft:short_description }}", 
"stac_extensions": "{{ stac_extensions }}", 
"geometry": "{{ geometry }}", 
"id": "{{ id }}", 
"collection": "{{ collection }}", 
"bbox": "{{ bbox }}", 
"properties": "{{ properties }}", 
"assets": "{{ assets }}", 
"_msft:ts": "{{ _msft:ts }}", 
"_msft:etag": "{{ _msft:etag }}"
}'
;
```
</TabItem>
<TabItem value="delete_item">

Delete a STAC item from a collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.delete_item 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="update_item">

Update a STAC item in a collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.update_item 
@collection_id='{{ collection_id }}' --required, 
@item_id='{{ item_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"type": "{{ type }}", 
"stac_version": "{{ stac_version }}", 
"links": "{{ links }}", 
"msft:_created": "{{ msft:_created }}", 
"msft:_updated": "{{ msft:_updated }}", 
"msft:short_description": "{{ msft:short_description }}", 
"stac_extensions": "{{ stac_extensions }}", 
"geometry": "{{ geometry }}", 
"id": "{{ id }}", 
"collection": "{{ collection }}", 
"bbox": "{{ bbox }}", 
"properties": "{{ properties }}", 
"assets": "{{ assets }}", 
"_msft:ts": "{{ _msft:ts }}", 
"_msft:etag": "{{ _msft:etag }}"
}'
;
```
</TabItem>
<TabItem value="get_item_collection">

Fetch features of the feature collection with id `collectionId`. Every feature in a dataset belongs to a collection. A dataset may consist of multiple feature collections. A feature collection is often a collection of features of a similar type, based on a common schema.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_item_collection 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@bbox='{{ bbox }}', 
@datetime='{{ datetime }}', 
@sign='{{ sign }}', 
@duration='{{ duration }}', 
@token='{{ token }}'
;
```
</TabItem>
<TabItem value="create_item">

Create a new STAC item or a set of items in a collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.create_item 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"type": "{{ type }}", 
"stac_version": "{{ stac_version }}", 
"links": "{{ links }}", 
"msft:_created": "{{ msft:_created }}", 
"msft:_updated": "{{ msft:_updated }}", 
"msft:short_description": "{{ msft:short_description }}", 
"stac_extensions": "{{ stac_extensions }}"
}'
;
```
</TabItem>
<TabItem value="get_queryables">

Queryables. List all queryables in the GeoCatalog instance.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_queryables 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_collection_queryables">

Collection Queryables. List all queryables in a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.get_collection_queryables 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_queryables">

Set Collection Queryables. Set queryables for a collection given a list of queryable definitions.

```sql
EXEC azure.planetarycomputer_dataplane.stac.create_queryables 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"name": "{{ name }}", 
"definition": "{{ definition }}", 
"create_index": {{ create_index }}, 
"data_type": "{{ data_type }}"
}'
;
```
</TabItem>
<TabItem value="create_collection_asset">

Create Collection Asset. Create a new asset in the Collection metadata and write the associated file to managed storage.

```sql
EXEC azure.planetarycomputer_dataplane.stac.create_collection_asset 
@collection_id='{{ collection_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"data": "{{ data }}", 
"file": "{{ file }}"
}'
;
```
</TabItem>
<TabItem value="replace_collection_asset">

Update Collection Asset. Update an existing asset in a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_collection_asset 
@collection_id='{{ collection_id }}' --required, 
@asset_id='{{ asset_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"data": "{{ data }}", 
"file": "{{ file }}"
}'
;
```
</TabItem>
<TabItem value="delete_collection_asset">

Delete Collection Asset. Delete an asset from a given collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.delete_collection_asset 
@collection_id='{{ collection_id }}' --required, 
@asset_id='{{ asset_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="replace_queryable">

Update Collection Queryables. Updates a queryable given a queryable definition and corresponding collection id.

```sql
EXEC azure.planetarycomputer_dataplane.stac.replace_queryable 
@collection_id='{{ collection_id }}' --required, 
@queryable_name='{{ queryable_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"name": "{{ name }}", 
"definition": "{{ definition }}", 
"create_index": {{ create_index }}, 
"data_type": "{{ data_type }}"
}'
;
```
</TabItem>
<TabItem value="delete_queryable">

Delete Queryables. Delete queryables by name for specified collection.

```sql
EXEC azure.planetarycomputer_dataplane.stac.delete_queryable 
@collection_id='{{ collection_id }}' --required, 
@queryable_name='{{ queryable_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="search">

Search. STAC search operation.

```sql
EXEC azure.planetarycomputer_dataplane.stac.search 
@endpoint='{{ endpoint }}' --required, 
@sign='{{ sign }}', 
@duration='{{ duration }}' 
@@json=
'{
"collections": "{{ collections }}", 
"ids": "{{ ids }}", 
"bbox": "{{ bbox }}", 
"intersects": "{{ intersects }}", 
"datetime": "{{ datetime }}", 
"limit": {{ limit }}, 
"conf": "{{ conf }}", 
"query": "{{ query }}", 
"sortby": "{{ sortby }}", 
"fields": "{{ fields }}", 
"filter": "{{ filter }}", 
"filter-crs": "{{ filter-crs }}", 
"filter-lang": "{{ filter-lang }}", 
"token": "{{ token }}"
}'
;
```
</TabItem>
</Tabs>
