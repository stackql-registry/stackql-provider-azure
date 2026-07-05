--- 
title: geolocation
hide_title: false
hide_table_of_contents: false
keywords:
  - geolocation
  - maps_geolocation
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

Creates, updates, deletes, gets or lists a <code>geolocation</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="geolocation" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps_geolocation.geolocation" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_location"
    values={[
        { label: 'get_location', value: 'get_location' }
    ]}
>
<TabItem value="get_location">

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
    <td><CopyableCode code="countryRegion" /></td>
    <td><code>object</code></td>
    <td>The object containing the country/region information.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP Address of the request.</td>
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
    <td><a href="#get_location"><CopyableCode code="get_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-ip"><code>ip</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to:** see pricing `tiers `_. This service will return the ISO country code for the provided IP address. Developers can use this information to block or alter certain content based on geographical locations where the application is being viewed from.</td>
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
<tr id="parameter-ip">
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>The IP address. Both IPv4 and IPv6 are allowed. Required.</td>
</tr>
<tr id="parameter-x-ms-client-id">
    <td><CopyableCode code="x-ms-client-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_location"
    values={[
        { label: 'get_location', value: 'get_location' }
    ]}
>
<TabItem value="get_location">

**Applies to:** see pricing `tiers `_. This service will return the ISO country code for the provided IP address. Developers can use this information to block or alter certain content based on geographical locations where the application is being viewed from.

```sql
SELECT
countryRegion,
ipAddress
FROM azure.maps_geolocation.geolocation
WHERE format = '{{ format }}' -- required
AND ip = '{{ ip }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND x-ms-client-id = '{{ x-ms-client-id }}'
;
```
</TabItem>
</Tabs>
