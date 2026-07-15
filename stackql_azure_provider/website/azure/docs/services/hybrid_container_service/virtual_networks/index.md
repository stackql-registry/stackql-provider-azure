--- 
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - hybrid_container_service
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

Creates, updates, deletes, gets or lists a <code>virtual_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_container_service.virtual_networks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServers" /></td>
    <td><code>array</code></td>
    <td>List of DNS server IP Addresses associated with the network.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location pointing to the underlying infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>string</code></td>
    <td>IP Address of the Gateway associated with the network.</td>
</tr>
<tr>
    <td><CopyableCode code="infraVnetProfile" /></td>
    <td><code>object</code></td>
    <td>:vartype infra_vnet_profile: ~azure.mgmt.hybridcontainerservice.models.VirtualNetworkPropertiesInfraVnetProfile</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>IP Address Prefix of the network.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Deleting", "Updating", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of the virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipPool" /></td>
    <td><code>array</code></td>
    <td>Range of IP Addresses for Kubernetes API Server and services if using HA Proxy load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="vlanID" /></td>
    <td><code>integer</code></td>
    <td>VLAN Id used by the network.</td>
</tr>
<tr>
    <td><CopyableCode code="vmipPool" /></td>
    <td><code>array</code></td>
    <td>Range of IP Addresses for Kubernetes node VMs.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServers" /></td>
    <td><code>array</code></td>
    <td>List of DNS server IP Addresses associated with the network.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location pointing to the underlying infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>string</code></td>
    <td>IP Address of the Gateway associated with the network.</td>
</tr>
<tr>
    <td><CopyableCode code="infraVnetProfile" /></td>
    <td><code>object</code></td>
    <td>:vartype infra_vnet_profile: ~azure.mgmt.hybridcontainerservice.models.VirtualNetworkPropertiesInfraVnetProfile</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>IP Address Prefix of the network.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Deleting", "Updating", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of the virtual network resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipPool" /></td>
    <td><code>array</code></td>
    <td>Range of IP Addresses for Kubernetes API Server and services if using HA Proxy load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="vlanID" /></td>
    <td><code>integer</code></td>
    <td>VLAN Id used by the network.</td>
</tr>
<tr>
    <td><CopyableCode code="vmipPool" /></td>
    <td><code>array</code></td>
    <td>Range of IP Addresses for Kubernetes node VMs.</td>
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
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the virtual networks in the specified resource group. Lists the virtual networks in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the virtual networks in the specified subscription. Lists the virtual networks in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates the virtual network resource. Creates or updates the virtual network resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patches the virtual network resource. Patches the virtual network resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates the virtual network resource. Creates or updates the virtual network resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified virtual network resource. Deletes the specified virtual network resource.</td>
</tr>
<tr>
    <td><a href="#retrieve"><CopyableCode code="retrieve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified virtual network resource. Gets the specified virtual network resource.</td>
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
<tr id="parameter-virtual_network_name">
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>Parameter for the name of the virtual network. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_by_resource_group">

Lists the virtual networks in the specified resource group. Lists the virtual networks in the specified resource group.

```sql
SELECT
id,
name,
dnsServers,
extendedLocation,
gateway,
infraVnetProfile,
ipAddressPrefix,
location,
provisioningState,
status,
systemData,
tags,
type,
vipPool,
vlanID,
vmipPool
FROM azure.hybrid_container_service.virtual_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists the virtual networks in the specified subscription. Lists the virtual networks in the specified subscription.

```sql
SELECT
id,
name,
dnsServers,
extendedLocation,
gateway,
infraVnetProfile,
ipAddressPrefix,
location,
provisioningState,
status,
systemData,
tags,
type,
vipPool,
vlanID,
vmipPool
FROM azure.hybrid_container_service.virtual_networks
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

Creates or updates the virtual network resource. Creates or updates the virtual network resource.

```sql
INSERT INTO azure.hybrid_container_service.virtual_networks (
tags,
location,
properties,
extendedLocation,
resource_group_name,
virtual_network_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ virtual_network_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_networks resource.
    - name: virtual_network_name
      value: "{{ virtual_network_name }}"
      description: Required parameter for the virtual_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_networks resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of the virtual network resource.
      value:
        infraVnetProfile:
          hci:
            mocGroup: "{{ mocGroup }}"
            mocLocation: "{{ mocLocation }}"
            mocVnetName: "{{ mocVnetName }}"
        vipPool:
          - endIP: "{{ endIP }}"
            startIP: "{{ startIP }}"
        vmipPool:
          - endIP: "{{ endIP }}"
            startIP: "{{ startIP }}"
        dnsServers:
          - "{{ dnsServers }}"
        gateway: "{{ gateway }}"
        ipAddressPrefix: "{{ ipAddressPrefix }}"
        vlanID: {{ vlanID }}
        provisioningState: "{{ provisioningState }}"
        status:
          operationStatus:
            error:
              code: "{{ code }}"
              message: "{{ message }}"
            operationId: "{{ operationId }}"
            status: "{{ status }}"
    - name: extendedLocation
      description: |
        Extended location pointing to the underlying infrastructure.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
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

Patches the virtual network resource. Patches the virtual network resource.

```sql
UPDATE azure.hybrid_container_service.virtual_networks
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
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

Creates or updates the virtual network resource. Creates or updates the virtual network resource.

```sql
REPLACE azure.hybrid_container_service.virtual_networks
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
location,
properties,
systemData,
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

Deletes the specified virtual network resource. Deletes the specified virtual network resource.

```sql
DELETE FROM azure.hybrid_container_service.virtual_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_name = '{{ virtual_network_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="retrieve"
    values={[
        { label: 'retrieve', value: 'retrieve' }
    ]}
>
<TabItem value="retrieve">

Gets the specified virtual network resource. Gets the specified virtual network resource.

```sql
EXEC azure.hybrid_container_service.virtual_networks.retrieve 
@resource_group_name='{{ resource_group_name }}' --required, 
@virtual_network_name='{{ virtual_network_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
