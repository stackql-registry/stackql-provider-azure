--- 
title: geodatas
hide_title: false
hide_table_of_contents: false
keywords:
  - geodatas
  - securityinsight
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

Creates, updates, deletes, gets or lists a <code>geodatas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="geodatas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.securityinsight.geodatas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_geodata_by_ip"
    values={[
        { label: 'list_geodata_by_ip', value: 'list_geodata_by_ip' }
    ]}
>
<TabItem value="list_geodata_by_ip">

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
    <td><CopyableCode code="asn" /></td>
    <td><code>string</code></td>
    <td>The autonomous system number associated with this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="carrier" /></td>
    <td><code>string</code></td>
    <td>The name of the carrier for this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>The city this IP address is located in.</td>
</tr>
<tr>
    <td><CopyableCode code="cityConfidenceFactor" /></td>
    <td><code>integer</code></td>
    <td>A numeric rating of confidence that the value in the 'city' field is correct, on a scale of 0-100.</td>
</tr>
<tr>
    <td><CopyableCode code="continent" /></td>
    <td><code>string</code></td>
    <td>The continent this IP address is located on.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The county this IP address is located in.</td>
</tr>
<tr>
    <td><CopyableCode code="countryConfidenceFactor" /></td>
    <td><code>integer</code></td>
    <td>A numeric rating of confidence that the value in the 'country' field is correct on a scale of 0-100.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddr" /></td>
    <td><code>string</code></td>
    <td>The dotted-decimal or colon-separated string representation of the IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipRoutingType" /></td>
    <td><code>string</code></td>
    <td>A description of the connection type of this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>string</code></td>
    <td>The latitude of this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>string</code></td>
    <td>The longitude of this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="organization" /></td>
    <td><code>string</code></td>
    <td>The name of the organization for this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationType" /></td>
    <td><code>string</code></td>
    <td>The type of the organization for this IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The geographic region this IP address is located in.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state this IP address is located in.</td>
</tr>
<tr>
    <td><CopyableCode code="stateCode" /></td>
    <td><code>string</code></td>
    <td>The abbreviated name for the state this IP address is located in.</td>
</tr>
<tr>
    <td><CopyableCode code="stateConfidenceFactor" /></td>
    <td><code>integer</code></td>
    <td>A numeric rating of confidence that the value in the 'state' field is correct on a scale of 0-100.</td>
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
    <td><a href="#list_geodata_by_ip"><CopyableCode code="list_geodata_by_ip" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-enrichment_type"><code>enrichment_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get geodata for a single IP address.</td>
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
<tr id="parameter-enrichment_type">
    <td><CopyableCode code="enrichment_type" /></td>
    <td><code>string</code></td>
    <td>Enrichment type. "main" Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_geodata_by_ip"
    values={[
        { label: 'list_geodata_by_ip', value: 'list_geodata_by_ip' }
    ]}
>
<TabItem value="list_geodata_by_ip">

Get geodata for a single IP address.

```sql
SELECT
asn,
carrier,
city,
cityConfidenceFactor,
continent,
country,
countryConfidenceFactor,
ipAddr,
ipRoutingType,
latitude,
longitude,
organization,
organizationType,
region,
state,
stateCode,
stateConfidenceFactor
FROM azure.securityinsight.geodatas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND enrichment_type = '{{ enrichment_type }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
