--- 
title: express_route_provider_ports_location
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_provider_ports_location
  - network
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

Creates, updates, deletes, gets or lists an <code>express_route_provider_ports_location</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_provider_ports_location" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_provider_ports_location" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="overprovisionFactor" /></td>
    <td><code>integer</code></td>
    <td>Overprovisioning factor for the port pair.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The peering location of the port pair.</td>
</tr>
<tr>
    <td><CopyableCode code="portBandwidthInMbps" /></td>
    <td><code>integer</code></td>
    <td>Bandwidth of the port in Mbps.</td>
</tr>
<tr>
    <td><CopyableCode code="portPairDescriptor" /></td>
    <td><code>string</code></td>
    <td>The name of the port pair.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the primary port.</td>
</tr>
<tr>
    <td><CopyableCode code="remainingBandwidthInMbps" /></td>
    <td><code>integer</code></td>
    <td>Remaining Bandwidth of the port in Mbps.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The name of the secondary port.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="usedBandwidthInMbps" /></td>
    <td><code>integer</code></td>
    <td>Used Bandwidth of the port in Mbps.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves all the ExpressRouteProviderPorts in a subscription.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. For example, you can use $filter=location eq '&#123;state&#125;'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieves all the ExpressRouteProviderPorts in a subscription.

```sql
SELECT
id,
name,
etag,
location,
overprovisionFactor,
peeringLocation,
portBandwidthInMbps,
portPairDescriptor,
primaryAzurePort,
remainingBandwidthInMbps,
secondaryAzurePort,
tags,
type,
usedBandwidthInMbps
FROM azure.network.express_route_provider_ports_location
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
