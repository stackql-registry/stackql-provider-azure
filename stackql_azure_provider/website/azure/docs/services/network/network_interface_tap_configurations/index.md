--- 
title: network_interface_tap_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_tap_configurations
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

Creates, updates, deletes, gets or lists a <code>network_interface_tap_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_interface_tap_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_interface_tap_configurations" /></td></tr>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface tap configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkTap" /></td>
    <td><code>object</code></td>
    <td>Virtual Network Tap resource.</td>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network interface tap configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkTap" /></td>
    <td><code>object</code></td>
    <td>Virtual Network Tap resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-tap_configuration_name"><code>tap_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified tap configuration on a network interface.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Tap configurations in a network interface.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-tap_configuration_name"><code>tap_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Tap configuration in the specified NetworkInterface.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-tap_configuration_name"><code>tap_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Tap configuration in the specified NetworkInterface.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-tap_configuration_name"><code>tap_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified tap configuration from the NetworkInterface.</td>
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
<tr id="parameter-network_interface_name">
    <td><CopyableCode code="network_interface_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network interface. Required.</td>
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
<tr id="parameter-tap_configuration_name">
    <td><CopyableCode code="tap_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
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

Get the specified tap configuration on a network interface.

```sql
SELECT
id,
name,
etag,
provisioningState,
type,
virtualNetworkTap
FROM azure.network.network_interface_tap_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND tap_configuration_name = '{{ tap_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all Tap configurations in a network interface.

```sql
SELECT
id,
name,
etag,
provisioningState,
type,
virtualNetworkTap
FROM azure.network.network_interface_tap_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
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

Creates or updates a Tap configuration in the specified NetworkInterface.

```sql
INSERT INTO azure.network.network_interface_tap_configurations (
id,
name,
properties,
resource_group_name,
network_interface_name,
tap_configuration_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_interface_name }}',
'{{ tap_configuration_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_interface_tap_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_interface_tap_configurations resource.
    - name: network_interface_name
      value: "{{ network_interface_name }}"
      description: Required parameter for the network_interface_tap_configurations resource.
    - name: tap_configuration_name
      value: "{{ tap_configuration_name }}"
      description: Required parameter for the network_interface_tap_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_interface_tap_configurations resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource.
    - name: properties
      description: |
        Properties of the Virtual Network Tap configuration.
      value:
        virtualNetworkTap:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            networkInterfaceTapConfigurations:
              - id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                properties:
                  virtualNetworkTap: "{{ virtualNetworkTap }}"
                  provisioningState: "{{ provisioningState }}"
                etag: "{{ etag }}"
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
            destinationNetworkInterfaceIPConfiguration:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              properties:
                gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                virtualNetworkTaps: "{{ virtualNetworkTaps }}"
                applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                loadBalancerInboundNatRules: "{{ loadBalancerInboundNatRules }}"
                privateIPAddress: "{{ privateIPAddress }}"
                privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
                privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                subnet: "{{ subnet }}"
                primary: {{ primary }}
                publicIPAddress: "{{ publicIPAddress }}"
                applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                provisioningState: "{{ provisioningState }}"
                privateLinkConnectionProperties: "{{ privateLinkConnectionProperties }}"
              etag: "{{ etag }}"
            destinationLoadBalancerFrontEndIPConfiguration:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              properties:
                inboundNatRules: "{{ inboundNatRules }}"
                inboundNatPools: "{{ inboundNatPools }}"
                outboundRules: "{{ outboundRules }}"
                loadBalancingRules: "{{ loadBalancingRules }}"
                privateIPAddress: "{{ privateIPAddress }}"
                privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                subnet: "{{ subnet }}"
                publicIPAddress: "{{ publicIPAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                provisioningState: "{{ provisioningState }}"
                ddosSettings: "{{ ddosSettings }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            destinationPort: {{ destinationPort }}
          etag: "{{ etag }}"
        provisioningState: "{{ provisioningState }}"
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

Creates or updates a Tap configuration in the specified NetworkInterface.

```sql
REPLACE azure.network.network_interface_tap_configurations
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_interface_name = '{{ network_interface_name }}' --required
AND tap_configuration_name = '{{ tap_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
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

Deletes the specified tap configuration from the NetworkInterface.

```sql
DELETE FROM azure.network.network_interface_tap_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_interface_name = '{{ network_interface_name }}' --required
AND tap_configuration_name = '{{ tap_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
