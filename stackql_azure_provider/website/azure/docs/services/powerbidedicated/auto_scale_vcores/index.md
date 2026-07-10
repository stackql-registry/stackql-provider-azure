--- 
title: auto_scale_vcores
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scale_vcores
  - powerbidedicated
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

Creates, updates, deletes, gets or lists an <code>auto_scale_vcores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="auto_scale_vcores" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbidedicated.auto_scale_vcores" /></td></tr>
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
    <td>An identifier that represents the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityLimit" /></td>
    <td><code>integer</code></td>
    <td>The maximum capacity of an auto scale v-core resource.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityObjectId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the capacity resource associated with the auto scale v-core resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the PowerBI Dedicated resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of an auto scale v-core resource. The provisioningState is to indicate states for resource provisioning. "Succeeded"</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the auto scale v-core resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of additional resource provisioning properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the PowerBI Dedicated resource.</td>
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
    <td>An identifier that represents the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityLimit" /></td>
    <td><code>integer</code></td>
    <td>The maximum capacity of an auto scale v-core resource.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityObjectId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the capacity resource associated with the auto scale v-core resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the PowerBI Dedicated resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of an auto scale v-core resource. The provisioningState is to indicate states for resource provisioning. "Succeeded"</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the auto scale v-core resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of additional resource provisioning properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the PowerBI Dedicated resource.</td>
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
    <td>An identifier that represents the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the PowerBI Dedicated resource.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityLimit" /></td>
    <td><code>integer</code></td>
    <td>The maximum capacity of an auto scale v-core resource.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityObjectId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the capacity resource associated with the auto scale v-core resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the PowerBI Dedicated resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment state of an auto scale v-core resource. The provisioningState is to indicate states for resource provisioning. "Succeeded"</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the auto scale v-core resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of additional resource provisioning properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the PowerBI Dedicated resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcore_name"><code>vcore_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details about the specified auto scale v-core.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the auto scale v-cores for the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the auto scale v-cores for the given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcore_name"><code>vcore_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Provisions the specified auto scale v-core based on the configuration specified in the request.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcore_name"><code>vcore_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the current state of the specified auto scale v-core.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vcore_name"><code>vcore_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified auto scale v-core.</td>
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
    <td>The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vcore_name">
    <td><CopyableCode code="vcore_name" /></td>
    <td><code>string</code></td>
    <td>The name of the auto scale v-core. It must be a minimum of 3 characters, and a maximum of 63. Required.</td>
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

Gets details about the specified auto scale v-core.

```sql
SELECT
id,
name,
capacityLimit,
capacityObjectId,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.powerbidedicated.auto_scale_vcores
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vcore_name = '{{ vcore_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the auto scale v-cores for the given resource group.

```sql
SELECT
id,
name,
capacityLimit,
capacityObjectId,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.powerbidedicated.auto_scale_vcores
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all the auto scale v-cores for the given subscription.

```sql
SELECT
id,
name,
capacityLimit,
capacityObjectId,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.powerbidedicated.auto_scale_vcores
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

Provisions the specified auto scale v-core based on the configuration specified in the request.

```sql
INSERT INTO azure.powerbidedicated.auto_scale_vcores (
location,
tags,
systemData,
sku,
properties,
resource_group_name,
vcore_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ systemData }}',
'{{ sku }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vcore_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: auto_scale_vcores
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the auto_scale_vcores resource.
    - name: vcore_name
      value: "{{ vcore_name }}"
      description: Required parameter for the auto_scale_vcores resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the auto_scale_vcores resource.
    - name: location
      value: "{{ location }}"
      description: |
        Location of the PowerBI Dedicated resource. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Key-value pairs of additional resource provisioning properties.
    - name: systemData
      description: |
        Metadata pertaining to creation and last modification of the resource.
      value:
        createdBy: "{{ createdBy }}"
        createdByType: "{{ createdByType }}"
        createdAt: "{{ createdAt }}"
        lastModifiedBy: "{{ lastModifiedBy }}"
        lastModifiedByType: "{{ lastModifiedByType }}"
        lastModifiedAt: "{{ lastModifiedAt }}"
    - name: sku
      description: |
        The SKU of the auto scale v-core resource. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        capacityLimit: {{ capacityLimit }}
        capacityObjectId: "{{ capacityObjectId }}"
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

Updates the current state of the specified auto scale v-core.

```sql
UPDATE azure.powerbidedicated.auto_scale_vcores
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vcore_name = '{{ vcore_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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

Deletes the specified auto scale v-core.

```sql
DELETE FROM azure.powerbidedicated.auto_scale_vcores
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vcore_name = '{{ vcore_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
