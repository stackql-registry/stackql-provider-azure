--- 
title: available_ground_stations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_ground_stations
  - orbital
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>available_ground_stations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="available_ground_stations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.orbital.available_ground_stations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_capability"
    values={[
        { label: 'list_by_capability', value: 'list_by_capability' }
    ]}
>
<TabItem value="list_by_capability">

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
    <td>ID of groundStation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="altitudeMeters" /></td>
    <td><code>number</code></td>
    <td>Altitude of the ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>City of ground station.</td>
</tr>
<tr>
    <td><CopyableCode code="latitudeDegrees" /></td>
    <td><code>number</code></td>
    <td>Latitude of the ground station in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region.</td>
</tr>
<tr>
    <td><CopyableCode code="longitudeDegrees" /></td>
    <td><code>number</code></td>
    <td>Longitude of the ground station in decimal degrees.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Ground station provider name.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseMode" /></td>
    <td><code>string</code></td>
    <td>Release Status of a ground station. Known values are: "Preview" and "GA".</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#list_by_capability"><CopyableCode code="list_by_capability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-capability"><code>capability</code></a></td>
    <td></td>
    <td>Returns list of available ground stations.</td>
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
<tr id="parameter-capability">
    <td><CopyableCode code="capability" /></td>
    <td><code>string</code></td>
    <td>Ground Station Capability. Known values are: "EarthObservation" and "Communication". Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_capability"
    values={[
        { label: 'list_by_capability', value: 'list_by_capability' }
    ]}
>
<TabItem value="list_by_capability">

Returns list of available ground stations.

```sql
SELECT
id,
name,
altitudeMeters,
city,
latitudeDegrees,
location,
longitudeDegrees,
providerName,
releaseMode,
type
FROM azure_extras.orbital.available_ground_stations
WHERE subscription_id = '{{ subscription_id }}' -- required
AND capability = '{{ capability }}' -- required
;
```
</TabItem>
</Tabs>
