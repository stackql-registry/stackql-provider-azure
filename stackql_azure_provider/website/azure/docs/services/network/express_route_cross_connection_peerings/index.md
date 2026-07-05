--- 
title: express_route_cross_connection_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connection_peerings
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

Creates, updates, deletes, gets or lists an <code>express_route_cross_connection_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_cross_connection_peerings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_cross_connection_peerings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureASN" /></td>
    <td><code>integer</code></td>
    <td>The Azure ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayManagerEtag" /></td>
    <td><code>string</code></td>
    <td>The GatewayManager Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6PeeringConfig" /></td>
    <td><code>object</code></td>
    <td>The IPv6 peering configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>Who was the last to modify the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="microsoftPeeringConfig" /></td>
    <td><code>object</code></td>
    <td>The Microsoft peering configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="peerASN" /></td>
    <td><code>integer</code></td>
    <td>The peer ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringType" /></td>
    <td><code>string</code></td>
    <td>The peering type. Known values are: "AzurePublicPeering", "AzurePrivatePeering", and "MicrosoftPeering". (AzurePublicPeering, AzurePrivatePeering, MicrosoftPeering)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The primary port.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryPeerAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The primary address prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route cross connection peering resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The secondary port.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryPeerAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The secondary address prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>The shared key.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The peering state. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="vlanId" /></td>
    <td><code>integer</code></td>
    <td>The VLAN ID.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="azureASN" /></td>
    <td><code>integer</code></td>
    <td>The Azure ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayManagerEtag" /></td>
    <td><code>string</code></td>
    <td>The GatewayManager Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6PeeringConfig" /></td>
    <td><code>object</code></td>
    <td>The IPv6 peering configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>Who was the last to modify the peering.</td>
</tr>
<tr>
    <td><CopyableCode code="microsoftPeeringConfig" /></td>
    <td><code>object</code></td>
    <td>The Microsoft peering configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="peerASN" /></td>
    <td><code>integer</code></td>
    <td>The peer ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringType" /></td>
    <td><code>string</code></td>
    <td>The peering type. Known values are: "AzurePublicPeering", "AzurePrivatePeering", and "MicrosoftPeering". (AzurePublicPeering, AzurePrivatePeering, MicrosoftPeering)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The primary port.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryPeerAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The primary address prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route cross connection peering resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryAzurePort" /></td>
    <td><code>string</code></td>
    <td>The secondary port.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryPeerAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The secondary address prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedKey" /></td>
    <td><code>string</code></td>
    <td>The shared key.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The peering state. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="vlanId" /></td>
    <td><code>integer</code></td>
    <td>The VLAN ID.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified peering for the ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all peerings in a specified ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a peering in the specified ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a peering in the specified ExpressRouteCrossConnection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cross_connection_name"><code>cross_connection_name</code></a>, <a href="#parameter-peering_name"><code>peering_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified peering from the ExpressRouteCrossConnection.</td>
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
<tr id="parameter-cross_connection_name">
    <td><CopyableCode code="cross_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name for the express route cross connection. Required.</td>
</tr>
<tr id="parameter-peering_name">
    <td><CopyableCode code="peering_name" /></td>
    <td><code>string</code></td>
    <td>The name of the peering. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified peering for the ExpressRouteCrossConnection.

```sql
SELECT
id,
name,
azureASN,
etag,
gatewayManagerEtag,
ipv6PeeringConfig,
lastModifiedBy,
microsoftPeeringConfig,
peerASN,
peeringType,
primaryAzurePort,
primaryPeerAddressPrefix,
provisioningState,
secondaryAzurePort,
secondaryPeerAddressPrefix,
sharedKey,
state,
vlanId
FROM azure.network.express_route_cross_connection_peerings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cross_connection_name = '{{ cross_connection_name }}' -- required
AND peering_name = '{{ peering_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all peerings in a specified ExpressRouteCrossConnection.

```sql
SELECT
id,
name,
azureASN,
etag,
gatewayManagerEtag,
ipv6PeeringConfig,
lastModifiedBy,
microsoftPeeringConfig,
peerASN,
peeringType,
primaryAzurePort,
primaryPeerAddressPrefix,
provisioningState,
secondaryAzurePort,
secondaryPeerAddressPrefix,
sharedKey,
state,
vlanId
FROM azure.network.express_route_cross_connection_peerings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cross_connection_name = '{{ cross_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a peering in the specified ExpressRouteCrossConnection.

```sql
INSERT INTO azure.network.express_route_cross_connection_peerings (
id,
properties,
name,
resource_group_name,
cross_connection_name,
peering_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ properties }}',
'{{ name }}',
'{{ resource_group_name }}',
'{{ cross_connection_name }}',
'{{ peering_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: express_route_cross_connection_peerings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_cross_connection_peerings resource.
    - name: cross_connection_name
      value: "{{ cross_connection_name }}"
      description: Required parameter for the express_route_cross_connection_peerings resource.
    - name: peering_name
      value: "{{ peering_name }}"
      description: Required parameter for the express_route_cross_connection_peerings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_cross_connection_peerings resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: properties
      description: |
        Properties of the express route cross connection peering.
      value:
        peeringType: "{{ peeringType }}"
        state: "{{ state }}"
        azureASN: {{ azureASN }}
        peerASN: {{ peerASN }}
        primaryPeerAddressPrefix: "{{ primaryPeerAddressPrefix }}"
        secondaryPeerAddressPrefix: "{{ secondaryPeerAddressPrefix }}"
        primaryAzurePort: "{{ primaryAzurePort }}"
        secondaryAzurePort: "{{ secondaryAzurePort }}"
        sharedKey: "{{ sharedKey }}"
        vlanId: {{ vlanId }}
        microsoftPeeringConfig:
          advertisedPublicPrefixes:
            - "{{ advertisedPublicPrefixes }}"
          advertisedCommunities:
            - "{{ advertisedCommunities }}"
          advertisedPublicPrefixesState: "{{ advertisedPublicPrefixesState }}"
          legacyMode: {{ legacyMode }}
          customerASN: {{ customerASN }}
          routingRegistryName: "{{ routingRegistryName }}"
          advertisedPublicPrefixInfo:
            - prefix: "{{ prefix }}"
              validationId: "{{ validationId }}"
              signature: "{{ signature }}"
              validationState: "{{ validationState }}"
        provisioningState: "{{ provisioningState }}"
        gatewayManagerEtag: "{{ gatewayManagerEtag }}"
        lastModifiedBy: "{{ lastModifiedBy }}"
        ipv6PeeringConfig:
          primaryPeerAddressPrefix: "{{ primaryPeerAddressPrefix }}"
          secondaryPeerAddressPrefix: "{{ secondaryPeerAddressPrefix }}"
          microsoftPeeringConfig:
            advertisedPublicPrefixes:
              - "{{ advertisedPublicPrefixes }}"
            advertisedCommunities:
              - "{{ advertisedCommunities }}"
            advertisedPublicPrefixesState: "{{ advertisedPublicPrefixesState }}"
            legacyMode: {{ legacyMode }}
            customerASN: {{ customerASN }}
            routingRegistryName: "{{ routingRegistryName }}"
            advertisedPublicPrefixInfo:
              - prefix: "{{ prefix }}"
                validationId: "{{ validationId }}"
                signature: "{{ signature }}"
                validationState: "{{ validationState }}"
          routeFilter:
            id: "{{ id }}"
          state: "{{ state }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
`}</CodeBlock>

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

Creates or updates a peering in the specified ExpressRouteCrossConnection.

```sql
REPLACE azure.network.express_route_cross_connection_peerings
SET 
id = '{{ id }}',
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cross_connection_name = '{{ cross_connection_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties;
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

Deletes the specified peering from the ExpressRouteCrossConnection.

```sql
DELETE FROM azure.network.express_route_cross_connection_peerings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cross_connection_name = '{{ cross_connection_name }}' --required
AND peering_name = '{{ peering_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
