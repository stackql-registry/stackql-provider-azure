--- 
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - api_management
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.reports" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_time"
    values={[
        { label: 'list_by_time', value: 'list_by_time' },
        { label: 'list_by_api', value: 'list_by_api' }
    ]}
>
<TabItem value="list_by_time">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name depending on report endpoint specifies product, API, operation or developer name.</td>
</tr>
<tr>
    <td><CopyableCode code="apiId" /></td>
    <td><code>string</code></td>
    <td>API identifier path. /apis/&#123;apiId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="apiRegion" /></td>
    <td><code>string</code></td>
    <td>API region identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="apiTimeAvg" /></td>
    <td><code>number</code></td>
    <td>Average time it took to process request.</td>
</tr>
<tr>
    <td><CopyableCode code="apiTimeMax" /></td>
    <td><code>number</code></td>
    <td>Maximum time it took to process request.</td>
</tr>
<tr>
    <td><CopyableCode code="apiTimeMin" /></td>
    <td><code>number</code></td>
    <td>Minimum time it took to process request.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidth" /></td>
    <td><code>integer</code></td>
    <td>Bandwidth consumed.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheHitCount" /></td>
    <td><code>integer</code></td>
    <td>Number of times when content was served from cache policy.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheMissCount" /></td>
    <td><code>integer</code></td>
    <td>Number of times content was fetched from backend.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountBlocked" /></td>
    <td><code>integer</code></td>
    <td>Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountFailed" /></td>
    <td><code>integer</code></td>
    <td>Number of calls failed due to gateway or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountOther" /></td>
    <td><code>integer</code></td>
    <td>Number of other calls.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountSuccess" /></td>
    <td><code>integer</code></td>
    <td>Number of successful calls. This includes calls returning HttpStatusCode &lt;= 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountTotal" /></td>
    <td><code>integer</code></td>
    <td>Total number of calls.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country to which this record data is related.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>Length of aggregation period. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (`http://en.wikipedia.org/wiki/ISO_8601#Durations `_).</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Operation identifier path. /apis/&#123;apiId&#125;/operations/&#123;operationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="productId" /></td>
    <td><code>string</code></td>
    <td>Product identifier path. /products/&#123;productId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Country region to which this record data is related.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTimeAvg" /></td>
    <td><code>number</code></td>
    <td>Average time it took to process request on backend.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTimeMax" /></td>
    <td><code>number</code></td>
    <td>Maximum time it took to process request on backend.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTimeMin" /></td>
    <td><code>number</code></td>
    <td>Minimum time it took to process request on backend.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription identifier path. /subscriptions/&#123;subscriptionId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start of aggregation period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>User identifier path. /users/&#123;userId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="zip" /></td>
    <td><code>string</code></td>
    <td>Zip code to which this record data is related.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_api">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name depending on report endpoint specifies product, API, operation or developer name.</td>
</tr>
<tr>
    <td><CopyableCode code="apiId" /></td>
    <td><code>string</code></td>
    <td>API identifier path. /apis/&#123;apiId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="apiRegion" /></td>
    <td><code>string</code></td>
    <td>API region identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="apiTimeAvg" /></td>
    <td><code>number</code></td>
    <td>Average time it took to process request.</td>
</tr>
<tr>
    <td><CopyableCode code="apiTimeMax" /></td>
    <td><code>number</code></td>
    <td>Maximum time it took to process request.</td>
</tr>
<tr>
    <td><CopyableCode code="apiTimeMin" /></td>
    <td><code>number</code></td>
    <td>Minimum time it took to process request.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidth" /></td>
    <td><code>integer</code></td>
    <td>Bandwidth consumed.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheHitCount" /></td>
    <td><code>integer</code></td>
    <td>Number of times when content was served from cache policy.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheMissCount" /></td>
    <td><code>integer</code></td>
    <td>Number of times content was fetched from backend.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountBlocked" /></td>
    <td><code>integer</code></td>
    <td>Number of calls blocked due to invalid credentials. This includes calls returning HttpStatusCode.Unauthorized and HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountFailed" /></td>
    <td><code>integer</code></td>
    <td>Number of calls failed due to gateway or backend errors. This includes calls returning HttpStatusCode.BadRequest(400) and any Code between HttpStatusCode.InternalServerError (500) and 600.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountOther" /></td>
    <td><code>integer</code></td>
    <td>Number of other calls.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountSuccess" /></td>
    <td><code>integer</code></td>
    <td>Number of successful calls. This includes calls returning HttpStatusCode &lt;= 301 and HttpStatusCode.NotModified and HttpStatusCode.TemporaryRedirect.</td>
</tr>
<tr>
    <td><CopyableCode code="callCountTotal" /></td>
    <td><code>integer</code></td>
    <td>Total number of calls.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country to which this record data is related.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>Length of aggregation period. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (`http://en.wikipedia.org/wiki/ISO_8601#Durations `_).</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Operation identifier path. /apis/&#123;apiId&#125;/operations/&#123;operationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="productId" /></td>
    <td><code>string</code></td>
    <td>Product identifier path. /products/&#123;productId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Country region to which this record data is related.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTimeAvg" /></td>
    <td><code>number</code></td>
    <td>Average time it took to process request on backend.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTimeMax" /></td>
    <td><code>number</code></td>
    <td>Maximum time it took to process request on backend.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTimeMin" /></td>
    <td><code>number</code></td>
    <td>Minimum time it took to process request on backend.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription identifier path. /subscriptions/&#123;subscriptionId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start of aggregation period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>User identifier path. /users/&#123;userId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="zip" /></td>
    <td><code>string</code></td>
    <td>Zip code to which this record data is related.</td>
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
    <td><a href="#list_by_time"><CopyableCode code="list_by_time" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-interval"><code>interval</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Lists report records by Time.</td>
</tr>
<tr>
    <td><a href="#list_by_api"><CopyableCode code="list_by_api" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Lists report records by API.</td>
</tr>
<tr>
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Lists report records by User.</td>
</tr>
<tr>
    <td><a href="#list_by_operation"><CopyableCode code="list_by_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Lists report records by API Operations.</td>
</tr>
<tr>
    <td><a href="#list_by_product"><CopyableCode code="list_by_product" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Lists report records by Product.</td>
</tr>
<tr>
    <td><a href="#list_by_geo"><CopyableCode code="list_by_geo" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Lists report records by geography.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Lists report records by subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_request"><CopyableCode code="list_by_request" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Lists report records by Request.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| timestamp | filter | ge, le | | | apiId | filter | eq | | | operationId | filter | eq | | | productId | filter | eq | | | userId | filter | eq | | | apiRegion | filter | eq | | | subscriptionId | filter | eq | | . Required.</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>By time interval. Interval must be multiple of 15 minutes and may not be zero. The value should be in ISO 8601 format (`http://en.wikipedia.org/wiki/ISO_8601#Durations).This `_ code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds)). Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>OData order by query option. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of records to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of records to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_time"
    values={[
        { label: 'list_by_time', value: 'list_by_time' },
        { label: 'list_by_api', value: 'list_by_api' }
    ]}
>
<TabItem value="list_by_time">

Lists report records by Time.

```sql
SELECT
name,
apiId,
apiRegion,
apiTimeAvg,
apiTimeMax,
apiTimeMin,
bandwidth,
cacheHitCount,
cacheMissCount,
callCountBlocked,
callCountFailed,
callCountOther,
callCountSuccess,
callCountTotal,
country,
interval,
operationId,
productId,
region,
serviceTimeAvg,
serviceTimeMax,
serviceTimeMin,
subscriptionId,
timestamp,
userId,
zip
FROM azure.api_management.reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}' -- required
AND interval = '{{ interval }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_by_api">

Lists report records by API.

```sql
SELECT
name,
apiId,
apiRegion,
apiTimeAvg,
apiTimeMax,
apiTimeMin,
bandwidth,
cacheHitCount,
cacheMissCount,
callCountBlocked,
callCountFailed,
callCountOther,
callCountSuccess,
callCountTotal,
country,
interval,
operationId,
productId,
region,
serviceTimeAvg,
serviceTimeMax,
serviceTimeMin,
subscriptionId,
timestamp,
userId,
zip
FROM azure.api_management.reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_user"
    values={[
        { label: 'list_by_user', value: 'list_by_user' },
        { label: 'list_by_operation', value: 'list_by_operation' },
        { label: 'list_by_product', value: 'list_by_product' },
        { label: 'list_by_geo', value: 'list_by_geo' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_by_request', value: 'list_by_request' }
    ]}
>
<TabItem value="list_by_user">

Lists report records by User.

```sql
EXEC azure.api_management.reports.list_by_user 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@$orderby='{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_by_operation">

Lists report records by API Operations.

```sql
EXEC azure.api_management.reports.list_by_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@$orderby='{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_by_product">

Lists report records by Product.

```sql
EXEC azure.api_management.reports.list_by_product 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@$orderby='{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_by_geo">

Lists report records by geography.

```sql
EXEC azure.api_management.reports.list_by_geo 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists report records by subscription.

```sql
EXEC azure.api_management.reports.list_by_subscription 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@$orderby='{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_by_request">

Lists report records by Request.

```sql
EXEC azure.api_management.reports.list_by_request 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}'
;
```
</TabItem>
</Tabs>
