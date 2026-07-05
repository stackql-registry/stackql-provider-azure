--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - connectedvmware
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connectedvmware.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Gets or sets the Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the name.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="datastoreIds" /></td>
    <td><code>array</code></td>
    <td>Gets the datastore ARM ids.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter MoRef (Managed Object Reference) ID for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="networkIds" /></td>
    <td><code>array</code></td>
    <td>Gets the network ARM ids.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system data.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuMHz" /></td>
    <td><code>integer</code></td>
    <td>Gets the max CPU usage across all cores on the cluster in MHz.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMemoryGB" /></td>
    <td><code>integer</code></td>
    <td>Gets the total amount of physical memory on the cluster in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="usedCpuMHz" /></td>
    <td><code>integer</code></td>
    <td>Gets the used CPU usage across all cores on the cluster in MHz.</td>
</tr>
<tr>
    <td><CopyableCode code="usedMemoryGB" /></td>
    <td><code>integer</code></td>
    <td>Gets the used physical memory on the cluster in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vCenterId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ARM Id of the vCenter resource in which this cluster resides.</td>
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
    <td>Gets or sets the Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the name.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="datastoreIds" /></td>
    <td><code>array</code></td>
    <td>Gets the datastore ARM ids.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter MoRef (Managed Object Reference) ID for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="networkIds" /></td>
    <td><code>array</code></td>
    <td>Gets the network ARM ids.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system data.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuMHz" /></td>
    <td><code>integer</code></td>
    <td>Gets the max CPU usage across all cores on the cluster in MHz.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMemoryGB" /></td>
    <td><code>integer</code></td>
    <td>Gets the total amount of physical memory on the cluster in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="usedCpuMHz" /></td>
    <td><code>integer</code></td>
    <td>Gets the used CPU usage across all cores on the cluster in MHz.</td>
</tr>
<tr>
    <td><CopyableCode code="usedMemoryGB" /></td>
    <td><code>integer</code></td>
    <td>Gets the used physical memory on the cluster in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vCenterId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ARM Id of the vCenter resource in which this cluster resides.</td>
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
    <td>Gets or sets the Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the name.</td>
</tr>
<tr>
    <td><CopyableCode code="customResourceName" /></td>
    <td><code>string</code></td>
    <td>Gets the name of the corresponding resource in Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="datastoreIds" /></td>
    <td><code>array</code></td>
    <td>Gets the datastore ARM ids.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="inventoryItemId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the inventory Item ID for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="moName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter Managed Object name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="moRefId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the vCenter MoRef (Managed Object Reference) ID for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="networkIds" /></td>
    <td><code>array</code></td>
    <td>Gets the network ARM ids.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system data.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuMHz" /></td>
    <td><code>integer</code></td>
    <td>Gets the max CPU usage across all cores on the cluster in MHz.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMemoryGB" /></td>
    <td><code>integer</code></td>
    <td>Gets the total amount of physical memory on the cluster in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="usedCpuMHz" /></td>
    <td><code>integer</code></td>
    <td>Gets the used CPU usage across all cores on the cluster in MHz.</td>
</tr>
<tr>
    <td><CopyableCode code="usedMemoryGB" /></td>
    <td><code>integer</code></td>
    <td>Gets the used physical memory on the cluster in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vCenterId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the ARM Id of the vCenter resource in which this cluster resides.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a cluster. Implements cluster GET method.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET clusters in a resource group. List of clusters in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements GET clusters in a subscription. List of clusters in a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements cluster PUT method. Create Or Update cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a cluster. API to update certain properties of the cluster resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes an cluster. Implements cluster DELETE method.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>Name of the cluster. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The Resource Group Name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Whether force delete was specified. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a cluster. Implements cluster GET method.

```sql
SELECT
id,
name,
customResourceName,
datastoreIds,
extendedLocation,
inventoryItemId,
kind,
location,
moName,
moRefId,
networkIds,
provisioningState,
statuses,
systemData,
tags,
totalCpuMHz,
totalMemoryGB,
type,
usedCpuMHz,
usedMemoryGB,
uuid,
vCenterId
FROM azure_isv.connectedvmware.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements GET clusters in a resource group. List of clusters in a resource group.

```sql
SELECT
id,
name,
customResourceName,
datastoreIds,
extendedLocation,
inventoryItemId,
kind,
location,
moName,
moRefId,
networkIds,
provisioningState,
statuses,
systemData,
tags,
totalCpuMHz,
totalMemoryGB,
type,
usedCpuMHz,
usedMemoryGB,
uuid,
vCenterId
FROM azure_isv.connectedvmware.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Implements GET clusters in a subscription. List of clusters in a subscription.

```sql
SELECT
id,
name,
customResourceName,
datastoreIds,
extendedLocation,
inventoryItemId,
kind,
location,
moName,
moRefId,
networkIds,
provisioningState,
statuses,
systemData,
tags,
totalCpuMHz,
totalMemoryGB,
type,
usedCpuMHz,
usedMemoryGB,
uuid,
vCenterId
FROM azure_isv.connectedvmware.clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Implements cluster PUT method. Create Or Update cluster.

```sql
INSERT INTO azure_isv.connectedvmware.clusters (
location,
extendedLocation,
tags,
kind,
properties,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ extendedLocation }}',
'{{ tags }}',
'{{ kind }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
kind,
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
- name: clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the clusters resource.
    - name: location
      value: "{{ location }}"
      description: |
        Gets or sets the location. Required.
    - name: extendedLocation
      description: |
        Gets or sets the extended location.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Gets or sets the Resource tags.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: properties
      value:
        vCenterId: "{{ vCenterId }}"
        moRefId: "{{ moRefId }}"
        inventoryItemId: "{{ inventoryItemId }}"
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

Updates a cluster. API to update certain properties of the cluster resource.

```sql
UPDATE azure_isv.connectedvmware.clusters
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
kind,
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

Deletes an cluster. Implements cluster DELETE method.

```sql
DELETE FROM azure_isv.connectedvmware.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
