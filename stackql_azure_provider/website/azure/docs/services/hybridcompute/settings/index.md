--- 
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - hybridcompute
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridcompute.settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="gatewayProperties" /></td>
    <td><code>object</code></td>
    <td>Settings Gateway properties.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Azure resource tenant Id.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-base_provider"><code>base_provider</code></a>, <a href="#parameter-base_resource_type"><code>base_resource_type</code></a>, <a href="#parameter-base_resource_name"><code>base_resource_name</code></a>, <a href="#parameter-settings_resource_name"><code>settings_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the base Settings for the target resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-base_provider"><code>base_provider</code></a>, <a href="#parameter-base_resource_type"><code>base_resource_type</code></a>, <a href="#parameter-base_resource_name"><code>base_resource_name</code></a>, <a href="#parameter-settings_resource_name"><code>settings_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the base Settings of the target resource.</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-base_provider"><code>base_provider</code></a>, <a href="#parameter-base_resource_type"><code>base_resource_type</code></a>, <a href="#parameter-base_resource_name"><code>base_resource_name</code></a>, <a href="#parameter-settings_resource_name"><code>settings_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the base Settings of the target resource.</td>
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
<tr id="parameter-base_provider">
    <td><CopyableCode code="base_provider" /></td>
    <td><code>string</code></td>
    <td>The name of the base Resource Provider. Required.</td>
</tr>
<tr id="parameter-base_resource_name">
    <td><CopyableCode code="base_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the base resource. Required.</td>
</tr>
<tr id="parameter-base_resource_type">
    <td><CopyableCode code="base_resource_type" /></td>
    <td><code>string</code></td>
    <td>The name of the base Resource Type. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-settings_resource_name">
    <td><CopyableCode code="settings_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the settings resource. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the base Settings for the target resource.

```sql
SELECT
id,
name,
gatewayProperties,
systemData,
tenantId,
type
FROM azure.hybridcompute.settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND base_provider = '{{ base_provider }}' -- required
AND base_resource_type = '{{ base_resource_type }}' -- required
AND base_resource_name = '{{ base_resource_name }}' -- required
AND settings_resource_name = '{{ settings_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
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

Updates the base Settings of the target resource.

```sql
UPDATE azure.hybridcompute.settings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND base_provider = '{{ base_provider }}' --required
AND base_resource_type = '{{ base_resource_type }}' --required
AND base_resource_name = '{{ base_resource_name }}' --required
AND settings_resource_name = '{{ settings_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' }
    ]}
>
<TabItem value="patch">

Update the base Settings of the target resource.

```sql
EXEC azure.hybridcompute.settings.patch 
@resource_group_name='{{ resource_group_name }}' --required, 
@base_provider='{{ base_provider }}' --required, 
@base_resource_type='{{ base_resource_type }}' --required, 
@base_resource_name='{{ base_resource_name }}' --required, 
@settings_resource_name='{{ settings_resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
