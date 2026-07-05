--- 
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - peering
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

Creates, updates, deletes, gets or lists a <code>peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="peerings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.peerings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

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
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="direct" /></td>
    <td><code>object</code></td>
    <td>The properties that define a direct peering.</td>
</tr>
<tr>
    <td><CopyableCode code="exchange" /></td>
    <td><code>object</code></td>
    <td>The properties that define an exchange peering.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the peering. Required. Known values are: "Direct" and "Exchange".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU that defines the tier and kind of the peering. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="direct" /></td>
    <td><code>object</code></td>
    <td>The properties that define a direct peering.</td>
</tr>
<tr>
    <td><CopyableCode code="exchange" /></td>
    <td><code>object</code></td>
    <td>The properties that define an exchange peering.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the peering. Required. Known values are: "Direct" and "Exchange".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU that defines the tier and kind of the peering. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>The ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="direct" /></td>
    <td><code>object</code></td>
    <td>The properties that define a direct peering.</td>
</tr>
<tr>
    <td><CopyableCode code="exchange" /></td>
    <td><code>object</code></td>
    <td>The properties that define an exchange peering.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the peering. Required. Known values are: "Direct" and "Exchange".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>The location of the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU that defines the tier and kind of the peering. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing peering with the specified name under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the peerings under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the peerings under the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags for a peering with the specified name under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing peering with the specified name under the given subscription and resource group.</td>
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
<tr id="parameter-peering_name">
    <td><CopyableCode code="peering_name" /></td>
    <td><code>string</code></td>
    <td>The name of the peering. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets an existing peering with the specified name under the given subscription and resource group.

```sql
SELECT
id,
name,
direct,
exchange,
kind,
location,
peeringLocation,
provisioningState,
sku,
tags,
type
FROM azure.peering.peerings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the peerings under the given subscription and resource group.

```sql
SELECT
id,
name,
direct,
exchange,
kind,
location,
peeringLocation,
provisioningState,
sku,
tags,
type
FROM azure.peering.peerings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all of the peerings under the given subscription.

```sql
SELECT
id,
name,
direct,
exchange,
kind,
location,
peeringLocation,
provisioningState,
sku,
tags,
type
FROM azure.peering.peerings
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group.

```sql
INSERT INTO azure.peering.peerings (
sku,
kind,
location,
tags,
properties,
resource_group_name,
peering_name,
subscription_id
)
SELECT 
'{{ sku }}' /* required */,
'{{ kind }}' /* required */,
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ peering_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: peerings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the peerings resource.
    - name: peering_name
      value: "{{ peering_name }}"
      description: Required parameter for the peerings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the peerings resource.
    - name: sku
      description: |
        The SKU that defines the tier and kind of the peering. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        family: "{{ family }}"
        size: "{{ size }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the peering. Required. Known values are: "Direct" and "Exchange".
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: properties
      value:
        direct:
          connections:
            - bandwidthInMbps: {{ bandwidthInMbps }}
              provisionedBandwidthInMbps: {{ provisionedBandwidthInMbps }}
              sessionAddressProvider: "{{ sessionAddressProvider }}"
              useForPeeringService: {{ useForPeeringService }}
              peeringDBFacilityId: {{ peeringDBFacilityId }}
              connectionState: "{{ connectionState }}"
              bgpSession:
                sessionPrefixV4: "{{ sessionPrefixV4 }}"
                sessionPrefixV6: "{{ sessionPrefixV6 }}"
                microsoftSessionIPv4Address: "{{ microsoftSessionIPv4Address }}"
                microsoftSessionIPv6Address: "{{ microsoftSessionIPv6Address }}"
                peerSessionIPv4Address: "{{ peerSessionIPv4Address }}"
                peerSessionIPv6Address: "{{ peerSessionIPv6Address }}"
                sessionStateV4: "{{ sessionStateV4 }}"
                sessionStateV6: "{{ sessionStateV6 }}"
                maxPrefixesAdvertisedV4: {{ maxPrefixesAdvertisedV4 }}
                maxPrefixesAdvertisedV6: {{ maxPrefixesAdvertisedV6 }}
                md5AuthenticationKey: "{{ md5AuthenticationKey }}"
              connectionIdentifier: "{{ connectionIdentifier }}"
          useForPeeringService: {{ useForPeeringService }}
          peerAsn:
            id: "{{ id }}"
          directPeeringType: "{{ directPeeringType }}"
        exchange:
          connections:
            - peeringDBFacilityId: {{ peeringDBFacilityId }}
              connectionState: "{{ connectionState }}"
              bgpSession:
                sessionPrefixV4: "{{ sessionPrefixV4 }}"
                sessionPrefixV6: "{{ sessionPrefixV6 }}"
                microsoftSessionIPv4Address: "{{ microsoftSessionIPv4Address }}"
                microsoftSessionIPv6Address: "{{ microsoftSessionIPv6Address }}"
                peerSessionIPv4Address: "{{ peerSessionIPv4Address }}"
                peerSessionIPv6Address: "{{ peerSessionIPv6Address }}"
                sessionStateV4: "{{ sessionStateV4 }}"
                sessionStateV6: "{{ sessionStateV6 }}"
                maxPrefixesAdvertisedV4: {{ maxPrefixesAdvertisedV4 }}
                maxPrefixesAdvertisedV6: {{ maxPrefixesAdvertisedV6 }}
                md5AuthenticationKey: "{{ md5AuthenticationKey }}"
              connectionIdentifier: "{{ connectionIdentifier }}"
          peerAsn:
            id: "{{ id }}"
        peeringLocation: "{{ peeringLocation }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates tags for a peering with the specified name under the given subscription and resource group.

```sql
UPDATE azure.peering.peerings
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
sku,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group.

```sql
REPLACE azure.peering.peerings
SET 
sku = '{{ sku }}',
kind = '{{ kind }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND sku = '{{ sku }}' --required
AND kind = '{{ kind }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
kind,
location,
properties,
sku,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an existing peering with the specified name under the given subscription and resource group.

```sql
DELETE FROM azure.peering.peerings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
