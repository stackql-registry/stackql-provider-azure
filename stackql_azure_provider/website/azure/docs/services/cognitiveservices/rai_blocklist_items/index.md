--- 
title: rai_blocklist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_blocklist_items
  - cognitiveservices
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

Creates, updates, deletes, gets or lists a <code>rai_blocklist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rai_blocklist_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitiveservices.rai_blocklist_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="isRegex" /></td>
    <td><code>boolean</code></td>
    <td>If the pattern is a regex pattern.</td>
</tr>
<tr>
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td>Pattern to match against.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="isRegex" /></td>
    <td><code>boolean</code></td>
    <td>If the pattern is a regex pattern.</td>
</tr>
<tr>
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td>Pattern to match against.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-rai_blocklist_item_name"><code>rai_blocklist_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified custom blocklist Item associated with the custom blocklist.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the blocklist items associated with the custom blocklist.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-rai_blocklist_item_name"><code>rai_blocklist_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified blocklist item associated with the Azure OpenAI account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-rai_blocklist_item_name"><code>rai_blocklist_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the state of specified blocklist item associated with the Azure OpenAI account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-rai_blocklist_item_name"><code>rai_blocklist_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified blocklist Item associated with the custom blocklist.</td>
</tr>
<tr>
    <td><a href="#batch_add"><CopyableCode code="batch_add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Batch operation to add blocklist items.</td>
</tr>
<tr>
    <td><a href="#batch_delete"><CopyableCode code="batch_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-rai_blocklist_name"><code>rai_blocklist_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Batch operation to delete blocklist items.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of Cognitive Services account. Required.</td>
</tr>
<tr id="parameter-rai_blocklist_item_name">
    <td><CopyableCode code="rai_blocklist_item_name" /></td>
    <td><code>string</code></td>
    <td>The name of the RaiBlocklist Item associated with the custom blocklist. Required.</td>
</tr>
<tr id="parameter-rai_blocklist_name">
    <td><CopyableCode code="rai_blocklist_name" /></td>
    <td><code>string</code></td>
    <td>The name of the RaiBlocklist associated with the Cognitive Services Account. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified custom blocklist Item associated with the custom blocklist.

```sql
SELECT
id,
name,
etag,
isRegex,
pattern,
systemData,
tags,
type
FROM azure.cognitiveservices.rai_blocklist_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND rai_blocklist_name = '{{ rai_blocklist_name }}' -- required
AND rai_blocklist_item_name = '{{ rai_blocklist_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the blocklist items associated with the custom blocklist.

```sql
SELECT
id,
name,
etag,
isRegex,
pattern,
systemData,
tags,
type
FROM azure.cognitiveservices.rai_blocklist_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND rai_blocklist_name = '{{ rai_blocklist_name }}' -- required
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

Update the state of specified blocklist item associated with the Azure OpenAI account.

```sql
INSERT INTO azure.cognitiveservices.rai_blocklist_items (
properties,
tags,
resource_group_name,
account_name,
rai_blocklist_name,
rai_blocklist_item_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ rai_blocklist_name }}',
'{{ rai_blocklist_item_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: rai_blocklist_items
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the rai_blocklist_items resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the rai_blocklist_items resource.
    - name: rai_blocklist_name
      value: "{{ rai_blocklist_name }}"
      description: Required parameter for the rai_blocklist_items resource.
    - name: rai_blocklist_item_name
      value: "{{ rai_blocklist_item_name }}"
      description: Required parameter for the rai_blocklist_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the rai_blocklist_items resource.
    - name: properties
      description: |
        Properties of Cognitive Services RaiBlocklist Item.
      value:
        pattern: "{{ pattern }}"
        isRegex: {{ isRegex }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
`}</CodeBlock>

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

Update the state of specified blocklist item associated with the Azure OpenAI account.

```sql
REPLACE azure.cognitiveservices.rai_blocklist_items
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND rai_blocklist_name = '{{ rai_blocklist_name }}' --required
AND rai_blocklist_item_name = '{{ rai_blocklist_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Deletes the specified blocklist Item associated with the custom blocklist.

```sql
DELETE FROM azure.cognitiveservices.rai_blocklist_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND rai_blocklist_name = '{{ rai_blocklist_name }}' --required
AND rai_blocklist_item_name = '{{ rai_blocklist_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch_add"
    values={[
        { label: 'batch_add', value: 'batch_add' },
        { label: 'batch_delete', value: 'batch_delete' }
    ]}
>
<TabItem value="batch_add">

Batch operation to add blocklist items.

```sql
EXEC azure.cognitiveservices.rai_blocklist_items.batch_add 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@rai_blocklist_name='{{ rai_blocklist_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="batch_delete">

Batch operation to delete blocklist items.

```sql
EXEC azure.cognitiveservices.rai_blocklist_items.batch_delete 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@rai_blocklist_name='{{ rai_blocklist_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
