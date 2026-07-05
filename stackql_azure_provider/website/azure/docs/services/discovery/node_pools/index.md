--- 
title: node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - node_pools
  - discovery
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

Creates, updates, deletes, gets or lists a <code>node_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.discovery.node_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_supercomputer', value: 'list_by_supercomputer' }
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSetPriority" /></td>
    <td><code>string</code></td>
    <td>The Virtual Machine Scale Set priority. If not specified, the default is 'Regular'. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The node pool subnet. Required.</td>
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
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the underlying Azure VM. Required. Known values are: "Standard_NC24ads_A100_v4", "Standard_NC48ads_A100_v4", "Standard_NC96ads_A100_v4", "Standard_NC4as_T4_v3", "Standard_NC8as_T4_v3", "Standard_NC16as_T4_v3", "Standard_NC64as_T4_v3", "Standard_NV6ads_A10_v5", "Standard_NV12ads_A10_v5", "Standard_NV24ads_A10_v5", "Standard_NV36ads_A10_v5", "Standard_NV36adms_A10_v5", "Standard_NV72ads_A10_v5", and "Standard_ND40rs_v2". (Standard_NC24ads_A100_v4, Standard_NC48ads_A100_v4, Standard_NC96ads_A100_v4, Standard_NC4as_T4_v3, Standard_NC8as_T4_v3, Standard_NC16as_T4_v3, Standard_NC64as_T4_v3, Standard_NV6ads_A10_v5, Standard_NV12ads_A10_v5, Standard_NV24ads_A10_v5, Standard_NV36ads_A10_v5, Standard_NV36adms_A10_v5, Standard_NV72ads_A10_v5, Standard_ND40rs_v2)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_supercomputer">

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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minNodeCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSetPriority" /></td>
    <td><code>string</code></td>
    <td>The Virtual Machine Scale Set priority. If not specified, the default is 'Regular'. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The node pool subnet. Required.</td>
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
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the underlying Azure VM. Required. Known values are: "Standard_NC24ads_A100_v4", "Standard_NC48ads_A100_v4", "Standard_NC96ads_A100_v4", "Standard_NC4as_T4_v3", "Standard_NC8as_T4_v3", "Standard_NC16as_T4_v3", "Standard_NC64as_T4_v3", "Standard_NV6ads_A10_v5", "Standard_NV12ads_A10_v5", "Standard_NV24ads_A10_v5", "Standard_NV36ads_A10_v5", "Standard_NV36adms_A10_v5", "Standard_NV72ads_A10_v5", and "Standard_ND40rs_v2". (Standard_NC24ads_A100_v4, Standard_NC48ads_A100_v4, Standard_NC96ads_A100_v4, Standard_NC4as_T4_v3, Standard_NC8as_T4_v3, Standard_NC16as_T4_v3, Standard_NC64as_T4_v3, Standard_NV6ads_A10_v5, Standard_NV12ads_A10_v5, Standard_NV24ads_A10_v5, Standard_NV36ads_A10_v5, Standard_NV36adms_A10_v5, Standard_NV72ads_A10_v5, Standard_ND40rs_v2)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-node_pool_name"><code>node_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a NodePool.</td>
</tr>
<tr>
    <td><a href="#list_by_supercomputer"><CopyableCode code="list_by_supercomputer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List NodePool resources by Supercomputer.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-node_pool_name"><code>node_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a NodePool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-node_pool_name"><code>node_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Update a NodePool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-node_pool_name"><code>node_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a NodePool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-node_pool_name"><code>node_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a NodePool.</td>
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
<tr id="parameter-node_pool_name">
    <td><CopyableCode code="node_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NodePool. Required.</td>
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
<tr id="parameter-supercomputer_name">
    <td><CopyableCode code="supercomputer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Supercomputer. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_supercomputer', value: 'list_by_supercomputer' }
    ]}
>
<TabItem value="get">

Get a NodePool.

```sql
SELECT
id,
name,
location,
maxNodeCount,
minNodeCount,
provisioningState,
scaleSetPriority,
subnetId,
systemData,
tags,
type,
vmSize
FROM azure.discovery.node_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND supercomputer_name = '{{ supercomputer_name }}' -- required
AND node_pool_name = '{{ node_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_supercomputer">

List NodePool resources by Supercomputer.

```sql
SELECT
id,
name,
location,
maxNodeCount,
minNodeCount,
provisioningState,
scaleSetPriority,
subnetId,
systemData,
tags,
type,
vmSize
FROM azure.discovery.node_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND supercomputer_name = '{{ supercomputer_name }}' -- required
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

Create a NodePool.

```sql
INSERT INTO azure.discovery.node_pools (
tags,
location,
properties,
resource_group_name,
supercomputer_name,
node_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ supercomputer_name }}',
'{{ node_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: node_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the node_pools resource.
    - name: supercomputer_name
      value: "{{ supercomputer_name }}"
      description: Required parameter for the node_pools resource.
    - name: node_pool_name
      value: "{{ node_pool_name }}"
      description: Required parameter for the node_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the node_pools resource.
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
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        subnetId: "{{ subnetId }}"
        vmSize: "{{ vmSize }}"
        maxNodeCount: {{ maxNodeCount }}
        minNodeCount: {{ minNodeCount }}
        scaleSetPriority: "{{ scaleSetPriority }}"
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

Update a NodePool.

```sql
UPDATE azure.discovery.node_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND supercomputer_name = '{{ supercomputer_name }}' --required
AND node_pool_name = '{{ node_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Create a NodePool.

```sql
REPLACE azure.discovery.node_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND supercomputer_name = '{{ supercomputer_name }}' --required
AND node_pool_name = '{{ node_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete a NodePool.

```sql
DELETE FROM azure.discovery.node_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND supercomputer_name = '{{ supercomputer_name }}' --required
AND node_pool_name = '{{ node_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
