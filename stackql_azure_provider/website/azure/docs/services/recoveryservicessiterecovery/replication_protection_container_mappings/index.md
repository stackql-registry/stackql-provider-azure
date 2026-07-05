--- 
title: replication_protection_container_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_container_mappings
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_protection_container_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_protection_container_mappings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_protection_container_mappings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
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
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Health of pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>Health error.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of replication policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>Policy ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>Provider specific provider details.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of source fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of source protection container.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Association Status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of target fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of paired container.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProtectionContainerId" /></td>
    <td><code>string</code></td>
    <td>Paired protection container ARM ID.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_replication_protection_containers">

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
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Health of pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>Health error.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of replication policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>Policy ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>Provider specific provider details.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of source fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of source protection container.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Association Status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of target fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of paired container.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProtectionContainerId" /></td>
    <td><code>string</code></td>
    <td>Paired protection container ARM ID.</td>
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
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Health of pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>Health error.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of replication policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>Policy ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>Provider specific provider details.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of source fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of source protection container.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Association Status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of target fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of paired container.</td>
</tr>
<tr>
    <td><CopyableCode code="targetProtectionContainerId" /></td>
    <td><code>string</code></td>
    <td>Paired protection container ARM ID.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-mapping_name"><code>mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a protection container mapping. Gets the details of a protection container mapping.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_protection_containers"><CopyableCode code="list_by_replication_protection_containers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of protection container mappings for a protection container. Lists the protection container mappings for a protection container.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of all protection container mappings in a vault. Lists the protection container mappings in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-mapping_name"><code>mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create protection container mapping. The operation to create a protection container mapping.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-mapping_name"><code>mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update protection container mapping. The operation to update protection container mapping.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-mapping_name"><code>mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove protection container mapping. The operation to delete or remove a protection container mapping.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-mapping_name"><code>mapping_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Purge protection container mapping. The operation to purge(force delete) a protection container mapping.</td>
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
<tr id="parameter-mapping_name">
    <td><CopyableCode code="mapping_name" /></td>
    <td><code>string</code></td>
    <td>Protection Container mapping name. Required.</td>
</tr>
<tr id="parameter-protection_container_name">
    <td><CopyableCode code="protection_container_name" /></td>
    <td><code>string</code></td>
    <td>Protection container name. Required.</td>
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
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a protection container mapping. Gets the details of a protection container mapping.

```sql
SELECT
id,
name,
health,
healthErrorDetails,
location,
policyFriendlyName,
policyId,
providerSpecificDetails,
sourceFabricFriendlyName,
sourceProtectionContainerFriendlyName,
state,
systemData,
targetFabricFriendlyName,
targetProtectionContainerFriendlyName,
targetProtectionContainerId,
type
FROM azure.recoveryservicessiterecovery.replication_protection_container_mappings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND mapping_name = '{{ mapping_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_protection_containers">

Gets the list of protection container mappings for a protection container. Lists the protection container mappings for a protection container.

```sql
SELECT
id,
name,
health,
healthErrorDetails,
location,
policyFriendlyName,
policyId,
providerSpecificDetails,
sourceFabricFriendlyName,
sourceProtectionContainerFriendlyName,
state,
systemData,
targetFabricFriendlyName,
targetProtectionContainerFriendlyName,
targetProtectionContainerId,
type
FROM azure.recoveryservicessiterecovery.replication_protection_container_mappings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of all protection container mappings in a vault. Lists the protection container mappings in the vault.

```sql
SELECT
id,
name,
health,
healthErrorDetails,
location,
policyFriendlyName,
policyId,
providerSpecificDetails,
sourceFabricFriendlyName,
sourceProtectionContainerFriendlyName,
state,
systemData,
targetFabricFriendlyName,
targetProtectionContainerFriendlyName,
targetProtectionContainerId,
type
FROM azure.recoveryservicessiterecovery.replication_protection_container_mappings
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

Create protection container mapping. The operation to create a protection container mapping.

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_protection_container_mappings (
properties,
resource_group_name,
resource_name,
fabric_name,
protection_container_name,
mapping_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ protection_container_name }}',
'{{ mapping_name }}',
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
- name: replication_protection_container_mappings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_protection_container_mappings resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_protection_container_mappings resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_protection_container_mappings resource.
    - name: protection_container_name
      value: "{{ protection_container_name }}"
      description: Required parameter for the replication_protection_container_mappings resource.
    - name: mapping_name
      value: "{{ mapping_name }}"
      description: Required parameter for the replication_protection_container_mappings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_protection_container_mappings resource.
    - name: properties
      description: |
        Configure protection input properties.
      value:
        targetProtectionContainerId: "{{ targetProtectionContainerId }}"
        policyId: "{{ policyId }}"
        providerSpecificInput:
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

Update protection container mapping. The operation to update protection container mapping.

```sql
UPDATE azure.recoveryservicessiterecovery.replication_protection_container_mappings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND mapping_name = '{{ mapping_name }}' --required
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

Remove protection container mapping. The operation to delete or remove a protection container mapping.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_protection_container_mappings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND mapping_name = '{{ mapping_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="purge"
    values={[
        { label: 'purge', value: 'purge' }
    ]}
>
<TabItem value="purge">

Purge protection container mapping. The operation to purge(force delete) a protection container mapping.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_container_mappings.purge 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@mapping_name='{{ mapping_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
