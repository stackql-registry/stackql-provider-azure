--- 
title: replication_network_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_network_mappings
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_network_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_network_mappings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_network_mappings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_networks', value: 'list_by_replication_networks' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricSpecificSettings" /></td>
    <td><code>object</code></td>
    <td>The fabric specific settings.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryNetworkFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary network friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryNetworkId" /></td>
    <td><code>string</code></td>
    <td>The primary network id for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricArmId" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryNetworkFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery network friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryNetworkId" /></td>
    <td><code>string</code></td>
    <td>The recovery network id for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The pairing state for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_replication_networks">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricSpecificSettings" /></td>
    <td><code>object</code></td>
    <td>The fabric specific settings.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryNetworkFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary network friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryNetworkId" /></td>
    <td><code>string</code></td>
    <td>The primary network id for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricArmId" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryNetworkFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery network friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryNetworkId" /></td>
    <td><code>string</code></td>
    <td>The recovery network id for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The pairing state for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricSpecificSettings" /></td>
    <td><code>object</code></td>
    <td>The fabric specific settings.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryNetworkFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The primary network friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryNetworkId" /></td>
    <td><code>string</code></td>
    <td>The primary network id for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricArmId" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryNetworkFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The recovery network friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryNetworkId" /></td>
    <td><code>string</code></td>
    <td>The recovery network id for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The pairing state for network mapping.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-network_name"><code>network_name</code></a>, <a href="#parameter-network_mapping_name"><code>network_mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets network mapping by name. Gets the details of an ASR network mapping.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_networks"><CopyableCode code="list_by_replication_networks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-network_name"><code>network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the network mappings under a network. Lists all ASR network mappings for the specified network.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the network mappings under a vault. Lists all ASR network mappings in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-network_name"><code>network_name</code></a>, <a href="#parameter-network_mapping_name"><code>network_mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates network mapping. The operation to create an ASR network mapping.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-network_name"><code>network_name</code></a>, <a href="#parameter-network_mapping_name"><code>network_mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates network mapping. The operation to update an ASR network mapping.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-network_name"><code>network_name</code></a>, <a href="#parameter-network_mapping_name"><code>network_mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete network mapping. The operation to delete a network mapping.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-network_mapping_name">
    <td><CopyableCode code="network_mapping_name" /></td>
    <td><code>string</code></td>
    <td>Network mapping name. Required.</td>
</tr>
<tr id="parameter-network_name">
    <td><CopyableCode code="network_name" /></td>
    <td><code>string</code></td>
    <td>Primary network name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
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
        { label: 'list_by_replication_networks', value: 'list_by_replication_networks' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets network mapping by name. Gets the details of an ASR network mapping.

```sql
SELECT
id,
name,
fabricSpecificSettings,
location,
primaryFabricFriendlyName,
primaryNetworkFriendlyName,
primaryNetworkId,
recoveryFabricArmId,
recoveryFabricFriendlyName,
recoveryNetworkFriendlyName,
recoveryNetworkId,
state,
systemData,
type
FROM azure.recovery_services_site_recovery.replication_network_mappings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND network_name = '{{ network_name }}' -- required
AND network_mapping_name = '{{ network_mapping_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_networks">

Gets all the network mappings under a network. Lists all ASR network mappings for the specified network.

```sql
SELECT
id,
name,
fabricSpecificSettings,
location,
primaryFabricFriendlyName,
primaryNetworkFriendlyName,
primaryNetworkId,
recoveryFabricArmId,
recoveryFabricFriendlyName,
recoveryNetworkFriendlyName,
recoveryNetworkId,
state,
systemData,
type
FROM azure.recovery_services_site_recovery.replication_network_mappings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND network_name = '{{ network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the network mappings under a vault. Lists all ASR network mappings in the vault.

```sql
SELECT
id,
name,
fabricSpecificSettings,
location,
primaryFabricFriendlyName,
primaryNetworkFriendlyName,
primaryNetworkId,
recoveryFabricArmId,
recoveryFabricFriendlyName,
recoveryNetworkFriendlyName,
recoveryNetworkId,
state,
systemData,
type
FROM azure.recovery_services_site_recovery.replication_network_mappings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates network mapping. The operation to create an ASR network mapping.

```sql
INSERT INTO azure.recovery_services_site_recovery.replication_network_mappings (
properties,
resource_group_name,
resource_name,
fabric_name,
network_name,
network_mapping_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ network_name }}',
'{{ network_mapping_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_network_mappings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_network_mappings resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_network_mappings resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_network_mappings resource.
    - name: network_name
      value: "{{ network_name }}"
      description: Required parameter for the replication_network_mappings resource.
    - name: network_mapping_name
      value: "{{ network_mapping_name }}"
      description: Required parameter for the replication_network_mappings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_network_mappings resource.
    - name: properties
      description: |
        Input properties for creating network mapping. Required.
      value:
        recoveryFabricName: "{{ recoveryFabricName }}"
        recoveryNetworkId: "{{ recoveryNetworkId }}"
        fabricSpecificDetails:
          instanceType: "{{ instanceType }}"
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

Updates network mapping. The operation to update an ASR network mapping.

```sql
UPDATE azure.recovery_services_site_recovery.replication_network_mappings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND network_name = '{{ network_name }}' --required
AND network_mapping_name = '{{ network_mapping_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
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

Delete network mapping. The operation to delete a network mapping.

```sql
DELETE FROM azure.recovery_services_site_recovery.replication_network_mappings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND network_name = '{{ network_name }}' --required
AND network_mapping_name = '{{ network_mapping_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
