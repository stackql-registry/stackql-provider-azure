--- 
title: dedicated_cloud_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_nodes
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>dedicated_cloud_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dedicated_cloud_nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.dedicated_cloud_nodes" /></td></tr>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudNodes/&#123;dedicatedCloudNodeName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;dedicatedCloudNodeName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneId" /></td>
    <td><code>string</code></td>
    <td>Availability Zone id, e.g. "az1".</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneName" /></td>
    <td><code>string</code></td>
    <td>Availability Zone name, e.g. "Availability Zone 1".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudRackName" /></td>
    <td><code>string</code></td>
    <td>VMWare Cloud Rack Name.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>date time the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodesCount" /></td>
    <td><code>integer</code></td>
    <td>count of nodes to create.</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupId" /></td>
    <td><code>string</code></td>
    <td>Placement Group id, e.g. "n1".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupName" /></td>
    <td><code>string</code></td>
    <td>Placement Name, e.g. "Placement Group 1".</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudName" /></td>
    <td><code>string</code></td>
    <td>Resource Pool Name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseId" /></td>
    <td><code>string</code></td>
    <td>purchase id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Dedicated Cloud Nodes SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Node status, indicates is private cloud set up on this node or not. Known values are: "unused" and "used".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dedicated Cloud Nodes tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwareClusterName" /></td>
    <td><code>string</code></td>
    <td>VMWare Cluster Name.</td>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudNodes/&#123;dedicatedCloudNodeName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;dedicatedCloudNodeName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneId" /></td>
    <td><code>string</code></td>
    <td>Availability Zone id, e.g. "az1".</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneName" /></td>
    <td><code>string</code></td>
    <td>Availability Zone name, e.g. "Availability Zone 1".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudRackName" /></td>
    <td><code>string</code></td>
    <td>VMWare Cloud Rack Name.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>date time the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodesCount" /></td>
    <td><code>integer</code></td>
    <td>count of nodes to create.</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupId" /></td>
    <td><code>string</code></td>
    <td>Placement Group id, e.g. "n1".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupName" /></td>
    <td><code>string</code></td>
    <td>Placement Name, e.g. "Placement Group 1".</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudName" /></td>
    <td><code>string</code></td>
    <td>Resource Pool Name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseId" /></td>
    <td><code>string</code></td>
    <td>purchase id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Dedicated Cloud Nodes SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Node status, indicates is private cloud set up on this node or not. Known values are: "unused" and "used".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dedicated Cloud Nodes tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwareClusterName" /></td>
    <td><code>string</code></td>
    <td>VMWare Cluster Name.</td>
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
    <td>/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudNodes/&#123;dedicatedCloudNodeName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>&#123;dedicatedCloudNodeName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneId" /></td>
    <td><code>string</code></td>
    <td>Availability Zone id, e.g. "az1".</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZoneName" /></td>
    <td><code>string</code></td>
    <td>Availability Zone name, e.g. "Availability Zone 1".</td>
</tr>
<tr>
    <td><CopyableCode code="cloudRackName" /></td>
    <td><code>string</code></td>
    <td>VMWare Cloud Rack Name.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>date time the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodesCount" /></td>
    <td><code>integer</code></td>
    <td>count of nodes to create.</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupId" /></td>
    <td><code>string</code></td>
    <td>Placement Group id, e.g. "n1".</td>
</tr>
<tr>
    <td><CopyableCode code="placementGroupName" /></td>
    <td><code>string</code></td>
    <td>Placement Name, e.g. "Placement Group 1".</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudId" /></td>
    <td><code>string</code></td>
    <td>Private Cloud Id.</td>
</tr>
<tr>
    <td><CopyableCode code="privateCloudName" /></td>
    <td><code>string</code></td>
    <td>Resource Pool Name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseId" /></td>
    <td><code>string</code></td>
    <td>purchase id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Dedicated Cloud Nodes SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Node status, indicates is private cloud set up on this node or not. Known values are: "unused" and "used".</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dedicated Cloud Nodes tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="vmwareClusterName" /></td>
    <td><code>string</code></td>
    <td>VMWare Cluster Name.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_node_name"><code>dedicated_cloud_node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements dedicated cloud node GET method. Returns dedicated cloud node.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Implements list of dedicated cloud nodes within RG method. Returns list of dedicate cloud nodes within resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Implements list of dedicated cloud nodes within subscription method. Returns list of dedicate cloud nodes within subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_node_name"><code>dedicated_cloud_node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements dedicated cloud node PUT method. Returns dedicated cloud node by its name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_node_name"><code>dedicated_cloud_node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements dedicated cloud node PATCH method. Patches dedicated node properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_node_name"><code>dedicated_cloud_node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-Referer"><code>Referer</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Implements dedicated cloud node PUT method. Returns dedicated cloud node by its name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dedicated_cloud_node_name"><code>dedicated_cloud_node_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements dedicated cloud node DELETE method. Delete dedicated cloud node.</td>
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
<tr id="parameter-Referer">
    <td><CopyableCode code="Referer" /></td>
    <td><code>string</code></td>
    <td>referer url. Required.</td>
</tr>
<tr id="parameter-dedicated_cloud_node_name">
    <td><CopyableCode code="dedicated_cloud_node_name" /></td>
    <td><code>string</code></td>
    <td>dedicated cloud node name. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the list operation. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>to be used by nextLink implementation. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of record sets to return. Default value is None.</td>
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

Implements dedicated cloud node GET method. Returns dedicated cloud node.

```sql
SELECT
id,
name,
availabilityZoneId,
availabilityZoneName,
cloudRackName,
created,
location,
nodesCount,
placementGroupId,
placementGroupName,
privateCloudId,
privateCloudName,
provisioningState,
purchaseId,
sku,
skuDescription,
status,
tags,
type,
vmwareClusterName
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dedicated_cloud_node_name = '{{ dedicated_cloud_node_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Implements list of dedicated cloud nodes within RG method. Returns list of dedicate cloud nodes within resource group.

```sql
SELECT
id,
name,
availabilityZoneId,
availabilityZoneName,
cloudRackName,
created,
location,
nodesCount,
placementGroupId,
placementGroupName,
privateCloudId,
privateCloudName,
provisioningState,
purchaseId,
sku,
skuDescription,
status,
tags,
type,
vmwareClusterName
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Implements list of dedicated cloud nodes within subscription method. Returns list of dedicate cloud nodes within subscription.

```sql
SELECT
id,
name,
availabilityZoneId,
availabilityZoneName,
cloudRackName,
created,
location,
nodesCount,
placementGroupId,
placementGroupName,
privateCloudId,
privateCloudName,
provisioningState,
purchaseId,
sku,
skuDescription,
status,
tags,
type,
vmwareClusterName
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Implements dedicated cloud node PUT method. Returns dedicated cloud node by its name.

```sql
INSERT INTO azure_isv.vmware_cloud_simple.dedicated_cloud_nodes (
location,
sku,
tags,
properties,
resource_group_name,
dedicated_cloud_node_name,
subscription_id,
Referer
)
SELECT 
'{{ location }}' /* required */,
'{{ sku }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ dedicated_cloud_node_name }}',
'{{ subscription_id }}',
'{{ Referer }}'
RETURNING
id,
name,
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
- name: dedicated_cloud_nodes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dedicated_cloud_nodes resource.
    - name: dedicated_cloud_node_name
      value: "{{ dedicated_cloud_node_name }}"
      description: Required parameter for the dedicated_cloud_nodes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dedicated_cloud_nodes resource.
    - name: Referer
      value: "{{ Referer }}"
      description: Required parameter for the dedicated_cloud_nodes resource.
    - name: location
      value: "{{ location }}"
      description: |
        Azure region. Required.
    - name: sku
      description: |
        Dedicated Cloud Nodes SKU.
      value:
        capacity: "{{ capacity }}"
        description: "{{ description }}"
        family: "{{ family }}"
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Dedicated Cloud Nodes tags.
    - name: properties
      value:
        availabilityZoneId: "{{ availabilityZoneId }}"
        nodesCount: {{ nodesCount }}
        placementGroupId: "{{ placementGroupId }}"
        purchaseId: "{{ purchaseId }}"
        skuDescription:
          id: "{{ id }}"
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

Implements dedicated cloud node PATCH method. Patches dedicated node properties.

```sql
UPDATE azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_cloud_node_name = '{{ dedicated_cloud_node_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Implements dedicated cloud node PUT method. Returns dedicated cloud node by its name.

```sql
REPLACE azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
SET 
location = '{{ location }}',
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_cloud_node_name = '{{ dedicated_cloud_node_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND Referer = '{{ Referer }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Implements dedicated cloud node DELETE method. Delete dedicated cloud node.

```sql
DELETE FROM azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dedicated_cloud_node_name = '{{ dedicated_cloud_node_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
