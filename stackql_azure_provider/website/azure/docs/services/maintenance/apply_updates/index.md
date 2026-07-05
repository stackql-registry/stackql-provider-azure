--- 
title: apply_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - apply_updates
  - maintenance
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

Creates, updates, deletes, gets or lists an <code>apply_updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apply_updates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.apply_updates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_parent"
    values={[
        { label: 'get_parent', value: 'get_parent' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_parent">

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
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Update time.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resourceId.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Pending", "InProgress", "Completed", "RetryNow", "RetryLater", "NoUpdatesPending", "Cancel", and "Cancelled". (Pending, InProgress, Completed, RetryNow, RetryLater, NoUpdatesPending, Cancel, Cancelled)</td>
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
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Update time.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resourceId.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Pending", "InProgress", "Completed", "RetryNow", "RetryLater", "NoUpdatesPending", "Cancel", and "Cancelled". (Pending, InProgress, Completed, RetryNow, RetryLater, NoUpdatesPending, Cancel, Cancelled)</td>
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
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Update time.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resourceId.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Pending", "InProgress", "Completed", "RetryNow", "RetryLater", "NoUpdatesPending", "Cancel", and "Cancelled". (Pending, InProgress, Completed, RetryNow, RetryLater, NoUpdatesPending, Cancel, Cancelled)</td>
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
    <td><a href="#get_parent"><CopyableCode code="get_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_parent_type"><code>resource_parent_type</code></a>, <a href="#parameter-resource_parent_name"><code>resource_parent_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-apply_update_name"><code>apply_update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Track maintenance updates to resource with parent.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-apply_update_name"><code>apply_update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Track maintenance updates to resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Configuration records within a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update_parent"><CopyableCode code="create_or_update_parent" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_parent_type"><code>resource_parent_type</code></a>, <a href="#parameter-resource_parent_name"><code>resource_parent_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply Updates to resource with parent. Apply maintenance updates to resource with parent.</td>
</tr>
<tr>
    <td><a href="#create_or_update_or_cancel"><CopyableCode code="create_or_update_or_cancel" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-apply_update_name"><code>apply_update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply maintenance updates to resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply Updates to resource. Apply maintenance updates to resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_parent"><CopyableCode code="create_or_update_parent" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_parent_type"><code>resource_parent_type</code></a>, <a href="#parameter-resource_parent_name"><code>resource_parent_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply Updates to resource with parent. Apply maintenance updates to resource with parent.</td>
</tr>
<tr>
    <td><a href="#create_or_update_or_cancel"><CopyableCode code="create_or_update_or_cancel" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-apply_update_name"><code>apply_update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply maintenance updates to resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply Updates to resource. Apply maintenance updates to resource.</td>
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
<tr id="parameter-apply_update_name">
    <td><CopyableCode code="apply_update_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ApplyUpdate. Required.</td>
</tr>
<tr id="parameter-provider_name">
    <td><CopyableCode code="provider_name" /></td>
    <td><code>string</code></td>
    <td>Resource provider name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Resource identifier. Required.</td>
</tr>
<tr id="parameter-resource_parent_name">
    <td><CopyableCode code="resource_parent_name" /></td>
    <td><code>string</code></td>
    <td>Resource parent identifier. Required.</td>
</tr>
<tr id="parameter-resource_parent_type">
    <td><CopyableCode code="resource_parent_type" /></td>
    <td><code>string</code></td>
    <td>Resource parent type. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Resource type. Required.</td>
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
    defaultValue="get_parent"
    values={[
        { label: 'get_parent', value: 'get_parent' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_parent">

Track maintenance updates to resource with parent.

```sql
SELECT
id,
name,
lastUpdateTime,
resourceId,
status,
systemData,
type
FROM azure.maintenance.apply_updates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provider_name = '{{ provider_name }}' -- required
AND resource_parent_type = '{{ resource_parent_type }}' -- required
AND resource_parent_name = '{{ resource_parent_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND apply_update_name = '{{ apply_update_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Track maintenance updates to resource.

```sql
SELECT
id,
name,
lastUpdateTime,
resourceId,
status,
systemData,
type
FROM azure.maintenance.apply_updates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provider_name = '{{ provider_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND apply_update_name = '{{ apply_update_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get Configuration records within a subscription.

```sql
SELECT
id,
name,
lastUpdateTime,
resourceId,
status,
systemData,
type
FROM azure.maintenance.apply_updates
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_parent"
    values={[
        { label: 'create_or_update_parent', value: 'create_or_update_parent' },
        { label: 'create_or_update_or_cancel', value: 'create_or_update_or_cancel' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_parent">

Apply Updates to resource with parent. Apply maintenance updates to resource with parent.

```sql
INSERT INTO azure.maintenance.apply_updates (
resource_group_name,
provider_name,
resource_parent_type,
resource_parent_name,
resource_type,
resource_name,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ provider_name }}',
'{{ resource_parent_type }}',
'{{ resource_parent_name }}',
'{{ resource_type }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_or_update_or_cancel">

Apply maintenance updates to resource.

```sql
INSERT INTO azure.maintenance.apply_updates (
properties,
resource_group_name,
provider_name,
resource_type,
resource_name,
apply_update_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ provider_name }}',
'{{ resource_type }}',
'{{ resource_name }}',
'{{ apply_update_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_or_update">

Apply Updates to resource. Apply maintenance updates to resource.

```sql
INSERT INTO azure.maintenance.apply_updates (
resource_group_name,
provider_name,
resource_type,
resource_name,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ provider_name }}',
'{{ resource_type }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: apply_updates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the apply_updates resource.
    - name: provider_name
      value: "{{ provider_name }}"
      description: Required parameter for the apply_updates resource.
    - name: resource_parent_type
      value: "{{ resource_parent_type }}"
      description: Required parameter for the apply_updates resource.
    - name: resource_parent_name
      value: "{{ resource_parent_name }}"
      description: Required parameter for the apply_updates resource.
    - name: resource_type
      value: "{{ resource_type }}"
      description: Required parameter for the apply_updates resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the apply_updates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the apply_updates resource.
    - name: apply_update_name
      value: "{{ apply_update_name }}"
      description: Required parameter for the apply_updates resource.
    - name: properties
      description: |
        Properties of the apply update.
      value:
        status: "{{ status }}"
        resourceId: "{{ resourceId }}"
        lastUpdateTime: "{{ lastUpdateTime }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_parent"
    values={[
        { label: 'create_or_update_parent', value: 'create_or_update_parent' },
        { label: 'create_or_update_or_cancel', value: 'create_or_update_or_cancel' },
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update_parent">

Apply Updates to resource with parent. Apply maintenance updates to resource with parent.

```sql
REPLACE azure.maintenance.apply_updates
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provider_name = '{{ provider_name }}' --required
AND resource_parent_type = '{{ resource_parent_type }}' --required
AND resource_parent_name = '{{ resource_parent_name }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_or_cancel">

Apply maintenance updates to resource.

```sql
REPLACE azure.maintenance.apply_updates
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provider_name = '{{ provider_name }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND apply_update_name = '{{ apply_update_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update">

Apply Updates to resource. Apply maintenance updates to resource.

```sql
REPLACE azure.maintenance.apply_updates
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provider_name = '{{ provider_name }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
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
