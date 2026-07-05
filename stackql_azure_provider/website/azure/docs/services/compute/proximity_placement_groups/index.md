--- 
title: proximity_placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - proximity_placement_groups
  - compute
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

Creates, updates, deletes, gets or lists a <code>proximity_placement_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="proximity_placement_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.proximity_placement_groups" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySets" /></td>
    <td><code>array</code></td>
    <td>A list of references to all availability sets in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="colocationStatus" /></td>
    <td><code>object</code></td>
    <td>Instance view status.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>object</code></td>
    <td>Specifies the user intent of the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroupType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the proximity placement group. Possible values are: **Standard** : Co-locate resources within an Azure region or Availability Zone. **Ultra** : For future use. Known values are: "Standard" and "Ultra". (Standard, Ultra)</td>
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
    <td><CopyableCode code="virtualMachineScaleSets" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machine scale sets in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySets" /></td>
    <td><code>array</code></td>
    <td>A list of references to all availability sets in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="colocationStatus" /></td>
    <td><code>object</code></td>
    <td>Instance view status.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>object</code></td>
    <td>Specifies the user intent of the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroupType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the proximity placement group. Possible values are: **Standard** : Co-locate resources within an Azure region or Availability Zone. **Ultra** : For future use. Known values are: "Standard" and "Ultra". (Standard, Ultra)</td>
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
    <td><CopyableCode code="virtualMachineScaleSets" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machine scale sets in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySets" /></td>
    <td><code>array</code></td>
    <td>A list of references to all availability sets in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="colocationStatus" /></td>
    <td><code>object</code></td>
    <td>Instance view status.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>object</code></td>
    <td>Specifies the user intent of the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroupType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the proximity placement group. Possible values are: **Standard** : Co-locate resources within an Azure region or Availability Zone. **Ultra** : For future use. Known values are: "Standard" and "Ultra". (Standard, Ultra)</td>
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
    <td><CopyableCode code="virtualMachineScaleSets" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machine scale sets in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the proximity placement group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-proximity_placement_group_name"><code>proximity_placement_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-includeColocationStatus"><code>includeColocationStatus</code></a></td>
    <td>Retrieves information about a proximity placement group .</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all proximity placement groups in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all proximity placement groups in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-proximity_placement_group_name"><code>proximity_placement_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a proximity placement group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-proximity_placement_group_name"><code>proximity_placement_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a proximity placement group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-proximity_placement_group_name"><code>proximity_placement_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a proximity placement group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-proximity_placement_group_name"><code>proximity_placement_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a proximity placement group.</td>
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
<tr id="parameter-proximity_placement_group_name">
    <td><CopyableCode code="proximity_placement_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the proximity placement group. Required.</td>
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
<tr id="parameter-includeColocationStatus">
    <td><CopyableCode code="includeColocationStatus" /></td>
    <td><code>string</code></td>
    <td>includeColocationStatus=true enables fetching the colocation status of all the resources in the proximity placement group. Default value is None.</td>
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

Retrieves information about a proximity placement group .

```sql
SELECT
id,
name,
availabilitySets,
colocationStatus,
intent,
location,
proximityPlacementGroupType,
systemData,
tags,
type,
virtualMachineScaleSets,
virtualMachines,
zones
FROM azure.compute.proximity_placement_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND proximity_placement_group_name = '{{ proximity_placement_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND includeColocationStatus = '{{ includeColocationStatus }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all proximity placement groups in a resource group.

```sql
SELECT
id,
name,
availabilitySets,
colocationStatus,
intent,
location,
proximityPlacementGroupType,
systemData,
tags,
type,
virtualMachineScaleSets,
virtualMachines,
zones
FROM azure.compute.proximity_placement_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all proximity placement groups in a subscription.

```sql
SELECT
id,
name,
availabilitySets,
colocationStatus,
intent,
location,
proximityPlacementGroupType,
systemData,
tags,
type,
virtualMachineScaleSets,
virtualMachines,
zones
FROM azure.compute.proximity_placement_groups
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

Create or update a proximity placement group.

```sql
INSERT INTO azure.compute.proximity_placement_groups (
tags,
location,
properties,
zones,
resource_group_name,
proximity_placement_group_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ proximity_placement_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: proximity_placement_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the proximity_placement_groups resource.
    - name: proximity_placement_group_name
      value: "{{ proximity_placement_group_name }}"
      description: Required parameter for the proximity_placement_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the proximity_placement_groups resource.
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
        Describes the properties of a Proximity Placement Group.
      value:
        proximityPlacementGroupType: "{{ proximityPlacementGroupType }}"
        virtualMachines:
          - id: "{{ id }}"
            colocationStatus:
              code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        virtualMachineScaleSets:
          - id: "{{ id }}"
            colocationStatus:
              code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        availabilitySets:
          - id: "{{ id }}"
            colocationStatus:
              code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        colocationStatus:
          code: "{{ code }}"
          level: "{{ level }}"
          displayStatus: "{{ displayStatus }}"
          message: "{{ message }}"
          time: "{{ time }}"
        intent:
          vmSizes:
            - "{{ vmSizes }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

Update a proximity placement group.

```sql
UPDATE azure.compute.proximity_placement_groups
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND proximity_placement_group_name = '{{ proximity_placement_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones;
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

Create or update a proximity placement group.

```sql
REPLACE azure.compute.proximity_placement_groups
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND proximity_placement_group_name = '{{ proximity_placement_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones;
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

Delete a proximity placement group.

```sql
DELETE FROM azure.compute.proximity_placement_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND proximity_placement_group_name = '{{ proximity_placement_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
