--- 
title: search
hide_title: false
hide_table_of_contents: false
keywords:
  - search
  - maps_search
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

Creates, updates, deletes, gets or lists a <code>search</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="search" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps_search.search" /></td></tr>
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
    <td><a href="#get_geocoding"><CopyableCode code="get_geocoding" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-addressLine"><code>addressLine</code></a>, <a href="#parameter-countryRegion"><code>countryRegion</code></a>, <a href="#parameter-bbox"><code>bbox</code></a>, <a href="#parameter-view"><code>view</code></a>, <a href="#parameter-coordinates"><code>coordinates</code></a>, <a href="#parameter-adminDistrict"><code>adminDistrict</code></a>, <a href="#parameter-adminDistrict2"><code>adminDistrict2</code></a>, <a href="#parameter-adminDistrict3"><code>adminDistrict3</code></a>, <a href="#parameter-locality"><code>locality</code></a>, <a href="#parameter-postalCode"><code>postalCode</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get longitude and latitude coordinates of a street address or name of a place. The `Get Geocoding` API is an HTTP `GET` request that returns the longitude and latitude coordinates of the location being searched. In many cases, the complete search service might be too much, for instance if you are only interested in traditional geocoding. Search can also be accessed for address look up exclusively. The geocoding is performed by hitting the geocoding endpoint with just the address or partial address in question. The geocoding search index will be queried for everything above the street level data. No Point of Interest (POIs) will be returned. Note that the geocoder is very tolerant of typos and incomplete addresses. It will also handle everything from exact street addresses or street or intersections as well as higher level geographies such as city centers, counties and states. The response also returns detailed address properties such as street, postal code, municipality, and country/region information.</td>
</tr>
<tr>
    <td><a href="#get_geocoding_batch"><CopyableCode code="get_geocoding_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Use to send a batch of queries to the `Geocoding `_ API in a single request. The `Get Geocoding Batch` API is an HTTP `POST` request that sends batches of up to **100** queries to the `Geocoding `_ API in a single request. Submit Synchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Synchronous API is recommended for lightweight batch requests. When the service receives a request, it will respond as soon as the batch items are calculated and there will be no possibility to retrieve the results later. The Synchronous API will return a timeout error (a 408 response) if the request takes longer than 60 seconds. The number of batch items is limited to **100** for this API. POST Body for Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^ To send the *geocoding* queries you will use a `POST` request where the request body will contain the `batchItems` array in `json` format and the `Content-Type` header will be set to `application/json`. Here's a sample request body containing 2 *geocoding* queries: A *geocoding* batchItem object can accept any of the supported *geocoding* `URI parameters `__. The batch should contain at least **1** query. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests` i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item is of one of the following types: * `GeocodingResponse `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case.</td>
</tr>
<tr>
    <td><a href="#get_polygon"><CopyableCode code="get_polygon" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-coordinates"><code>coordinates</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-view"><code>view</code></a>, <a href="#parameter-resultType"><code>resultType</code></a>, <a href="#parameter-resolution"><code>resolution</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Use to get polygon data of a geographical area shape such as a city or a country region. The `Get Polygon` API is an HTTP `GET` request that supplies polygon data of a geographical area outline such as a city or a country region.</td>
</tr>
<tr>
    <td><a href="#get_reverse_geocoding"><CopyableCode code="get_reverse_geocoding" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-coordinates"><code>coordinates</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-resultTypes"><code>resultTypes</code></a>, <a href="#parameter-view"><code>view</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Use to get a street address and location info from longitude and latitude coordinates. The `Get Reverse Geocoding` API is an HTTP `GET` request used to translate a coordinate (example: 37.786505, -122.3862) into a human understandable street address. Useful in tracking applications where you receive a GPS feed from the device or asset and wish to know the address associated with the coordinates. This endpoint will return address information for a given coordinate.</td>
</tr>
<tr>
    <td><a href="#get_reverse_geocoding_batch"><CopyableCode code="get_reverse_geocoding_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a>, <a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Use to send a batch of queries to the `Reverse Geocoding `_ API in a single request. The `Get Reverse Geocoding Batch` API is an HTTP `POST` request that sends batches of up to **100** queries to `Reverse Geocoding `_ API using a single request. Submit Synchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Synchronous API is recommended for lightweight batch requests. When the service receives a request, it will respond as soon as the batch items are calculated and there will be no possibility to retrieve the results later. The Synchronous API will return a timeout error (a 408 response) if the request takes longer than 60 seconds. The number of batch items is limited to **100** for this API. POST Body for Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^ To send the *reverse geocoding* queries you will use a `POST` request where the request body will contain the `batchItems` array in `json` format and the `Content-Type` header will be set to `application/json`. Here's a sample request body containing 2 *reverse geocoding* queries: A *reverse geocoding* batchItem object can accept any of the supported *reverse geocoding* `URI parameters `__. The batch should contain at least **1** query. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests` i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item is of one of the following types: * `GeocodingResponse `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case.</td>
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
<tr id="parameter-coordinates">
    <td><CopyableCode code="coordinates" /></td>
    <td><code>array</code></td>
    <td>The coordinates of the location that you want to reverse geocode. Example: &coordinates=lon,lat. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-Accept-Language">
    <td><CopyableCode code="Accept-Language" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-addressLine">
    <td><CopyableCode code="addressLine" /></td>
    <td><code>string</code></td>
    <td>The official street line of an address relative to the area, as specified by the locality, or postalCode, properties. Typical use of this element would be to provide a street address or any official address. **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-adminDistrict">
    <td><CopyableCode code="adminDistrict" /></td>
    <td><code>string</code></td>
    <td>The country subdivision portion of an address, such as WA. **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-adminDistrict2">
    <td><CopyableCode code="adminDistrict2" /></td>
    <td><code>string</code></td>
    <td>The county for the structured address, such as King. **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-adminDistrict3">
    <td><CopyableCode code="adminDistrict3" /></td>
    <td><code>string</code></td>
    <td>The named area for the structured address. **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-bbox">
    <td><CopyableCode code="bbox" /></td>
    <td><code>array</code></td>
    <td>A rectangular area on the earth defined as a bounding box object. The sides of the rectangles are defined by longitude and latitude values. When you specify this parameter, the geographical area is taken into account when computing the results of a location query. Example: lon1,lat1,lon2,lat2. Default value is None.</td>
</tr>
<tr id="parameter-coordinates">
    <td><CopyableCode code="coordinates" /></td>
    <td><code>array</code></td>
    <td>A point on the earth specified as a longitude and latitude. When you specify this parameter, the user’s location is taken into account and the results returned may be more relevant to the user. Example: &coordinates=lon,lat. Default value is None.</td>
</tr>
<tr id="parameter-countryRegion">
    <td><CopyableCode code="countryRegion" /></td>
    <td><code>string</code></td>
    <td>Signal for the geocoding result to an `ISO 3166-1 Alpha-2 region/country code `_ that is specified e.g. FR./ **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-locality">
    <td><CopyableCode code="locality" /></td>
    <td><code>string</code></td>
    <td>The locality portion of an address, such as Seattle. **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-postalCode">
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>The postal code portion of an address. **If query is given, should not use this parameter.**. Default value is None.</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>A string that contains information about a location, such as an address or landmark name. Default value is None.</td>
</tr>
<tr id="parameter-resolution">
    <td><CopyableCode code="resolution" /></td>
    <td><code>string</code></td>
    <td>Resolution determines the amount of points to send back. If not specified, the default is medium resolution. Known values are: "small", "medium", "large", and "huge". Default value is "medium".</td>
</tr>
<tr id="parameter-resultType">
    <td><CopyableCode code="resultType" /></td>
    <td><code>string</code></td>
    <td>The geopolitical concept to return a boundary for. If not specified, the default is `countryRegion` result type. Known values are: "countryRegion", "adminDistrict", "adminDistrict2", "postalCode", "postalCode2", "postalCode3", "postalCode4", "neighborhood", and "locality". Default value is "countryRegion".</td>
</tr>
<tr id="parameter-resultTypes">
    <td><CopyableCode code="resultTypes" /></td>
    <td><code>array</code></td>
    <td>Specify entity types that you want in the response. Only the types you specify will be returned. If the point cannot be mapped to the entity types you specify, no location information is returned in the response. Default value is all possible entities. A comma separated list of entity types selected from the following options. * Address * Neighborhood * PopulatedPlace * Postcode1 * AdminDivision1 * AdminDivision2 * CountryRegion These entity types are ordered from the most specific entity to the least specific entity. When entities of more than one entity type are found, only the most specific entity is returned. For example, if you specify Address and AdminDistrict1 as entity types and entities were found for both types, only the Address entity information is returned in the response. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of responses that will be returned. Default: 5, minimum: 1 and maximum: 20. Default value is 5.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>A string that represents an `ISO 3166-1 Alpha-2 region/country code `_. This will alter Geopolitical disputed borders and labels to align with the specified user region. By default, the View parameter is set to “Auto” even if you haven’t defined it in the request. Please refer to `Supported Views `_ for details and to see the available Views. Default value is None.</td>
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
    defaultValue="get_geocoding"
    values={[
        { label: 'get_geocoding', value: 'get_geocoding' },
        { label: 'get_geocoding_batch', value: 'get_geocoding_batch' },
        { label: 'get_polygon', value: 'get_polygon' },
        { label: 'get_reverse_geocoding', value: 'get_reverse_geocoding' },
        { label: 'get_reverse_geocoding_batch', value: 'get_reverse_geocoding_batch' }
    ]}
>
<TabItem value="get_geocoding">

Use to get longitude and latitude coordinates of a street address or name of a place. The `Get Geocoding` API is an HTTP `GET` request that returns the longitude and latitude coordinates of the location being searched. In many cases, the complete search service might be too much, for instance if you are only interested in traditional geocoding. Search can also be accessed for address look up exclusively. The geocoding is performed by hitting the geocoding endpoint with just the address or partial address in question. The geocoding search index will be queried for everything above the street level data. No Point of Interest (POIs) will be returned. Note that the geocoder is very tolerant of typos and incomplete addresses. It will also handle everything from exact street addresses or street or intersections as well as higher level geographies such as city centers, counties and states. The response also returns detailed address properties such as street, postal code, municipality, and country/region information.

```sql
EXEC azure.maps_search.search.get_geocoding 
@endpoint='{{ endpoint }}' --required, 
@top='{{ top }}', 
@query='{{ query }}', 
@addressLine='{{ addressLine }}', 
@countryRegion='{{ countryRegion }}', 
@bbox='{{ bbox }}', 
@view='{{ view }}', 
@coordinates='{{ coordinates }}', 
@adminDistrict='{{ adminDistrict }}', 
@adminDistrict2='{{ adminDistrict2 }}', 
@adminDistrict3='{{ adminDistrict3 }}', 
@locality='{{ locality }}', 
@postalCode='{{ postalCode }}', 
@Accept-Language='{{ Accept-Language }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_geocoding_batch">

Use to send a batch of queries to the `Geocoding `_ API in a single request. The `Get Geocoding Batch` API is an HTTP `POST` request that sends batches of up to **100** queries to the `Geocoding `_ API in a single request. Submit Synchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Synchronous API is recommended for lightweight batch requests. When the service receives a request, it will respond as soon as the batch items are calculated and there will be no possibility to retrieve the results later. The Synchronous API will return a timeout error (a 408 response) if the request takes longer than 60 seconds. The number of batch items is limited to **100** for this API. POST Body for Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^ To send the *geocoding* queries you will use a `POST` request where the request body will contain the `batchItems` array in `json` format and the `Content-Type` header will be set to `application/json`. Here's a sample request body containing 2 *geocoding* queries: A *geocoding* batchItem object can accept any of the supported *geocoding* `URI parameters `__. The batch should contain at least **1** query. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests` i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item is of one of the following types: * `GeocodingResponse `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case.

```sql
EXEC azure.maps_search.search.get_geocoding_batch 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}', 
@Accept-Language='{{ Accept-Language }}'
;
```
</TabItem>
<TabItem value="get_polygon">

Use to get polygon data of a geographical area shape such as a city or a country region. The `Get Polygon` API is an HTTP `GET` request that supplies polygon data of a geographical area outline such as a city or a country region.

```sql
EXEC azure.maps_search.search.get_polygon 
@coordinates='{{ coordinates }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@view='{{ view }}', 
@resultType='{{ resultType }}', 
@resolution='{{ resolution }}', 
@x-ms-client-id='{{ x-ms-client-id }}', 
@Accept-Language='{{ Accept-Language }}'
;
```
</TabItem>
<TabItem value="get_reverse_geocoding">

Use to get a street address and location info from longitude and latitude coordinates. The `Get Reverse Geocoding` API is an HTTP `GET` request used to translate a coordinate (example: 37.786505, -122.3862) into a human understandable street address. Useful in tracking applications where you receive a GPS feed from the device or asset and wish to know the address associated with the coordinates. This endpoint will return address information for a given coordinate.

```sql
EXEC azure.maps_search.search.get_reverse_geocoding 
@coordinates='{{ coordinates }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@resultTypes='{{ resultTypes }}', 
@view='{{ view }}', 
@x-ms-client-id='{{ x-ms-client-id }}', 
@Accept-Language='{{ Accept-Language }}'
;
```
</TabItem>
<TabItem value="get_reverse_geocoding_batch">

Use to send a batch of queries to the `Reverse Geocoding `_ API in a single request. The `Get Reverse Geocoding Batch` API is an HTTP `POST` request that sends batches of up to **100** queries to `Reverse Geocoding `_ API using a single request. Submit Synchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Synchronous API is recommended for lightweight batch requests. When the service receives a request, it will respond as soon as the batch items are calculated and there will be no possibility to retrieve the results later. The Synchronous API will return a timeout error (a 408 response) if the request takes longer than 60 seconds. The number of batch items is limited to **100** for this API. POST Body for Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^ To send the *reverse geocoding* queries you will use a `POST` request where the request body will contain the `batchItems` array in `json` format and the `Content-Type` header will be set to `application/json`. Here's a sample request body containing 2 *reverse geocoding* queries: A *reverse geocoding* batchItem object can accept any of the supported *reverse geocoding* `URI parameters `__. The batch should contain at least **1** query. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests` i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item is of one of the following types: * `GeocodingResponse `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case.

```sql
EXEC azure.maps_search.search.get_reverse_geocoding_batch 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}', 
@Accept-Language='{{ Accept-Language }}'
;
```
</TabItem>
</Tabs>
