--- 
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - resource
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tags" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.tags" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get_at_scope', value: 'get_at_scope' }
    ]}
>
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
    <td>The tag name ID.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>object</code></td>
    <td>The total number of resources that use the resource tag. When a tag is initially created and has no associated resources, the value is 0.</td>
</tr>
<tr>
    <td><CopyableCode code="tagName" /></td>
    <td><code>string</code></td>
    <td>The tag name.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>The list of tag values.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_scope">

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
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a summary of tag usage under the subscription. This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result.</td>
</tr>
<tr>
    <td><a href="#get_at_scope"><CopyableCode code="get_at_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Gets the entire set of tags on a resource or subscription. Gets the entire set of tags on a resource or subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update_value"><CopyableCode code="create_or_update_value" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-tag_name"><code>tag_name</code></a>, <a href="#parameter-tag_value"><code>tag_value</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a predefined value for a predefined tag name. This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-tag_name"><code>tag_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a predefined tag name. This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_scope"><CopyableCode code="create_or_update_at_scope" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates the entire set of tags on a resource or subscription. This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.</td>
</tr>
<tr>
    <td><a href="#update_at_scope"><CopyableCode code="update_at_scope" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Selectively updates the set of tags on a resource or subscription. This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The 'replace' option replaces the entire set of existing tags with a new set. The 'merge' option allows adding tags with new names and updating the values of tags with existing names. The 'delete' option allows selectively deleting tags based on given names or name/value pairs.</td>
</tr>
<tr>
    <td><a href="#create_or_update_value"><CopyableCode code="create_or_update_value" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-tag_name"><code>tag_name</code></a>, <a href="#parameter-tag_value"><code>tag_value</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a predefined value for a predefined tag name. This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-tag_name"><code>tag_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a predefined tag name. This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_scope"><CopyableCode code="create_or_update_at_scope" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates the entire set of tags on a resource or subscription. This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.</td>
</tr>
<tr>
    <td><a href="#delete_value"><CopyableCode code="delete_value" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-tag_name"><code>tag_name</code></a>, <a href="#parameter-tag_value"><code>tag_value</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a predefined tag value for a predefined tag name. This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-tag_name"><code>tag_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a predefined tag name. This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted.</td>
</tr>
<tr>
    <td><a href="#delete_at_scope"><CopyableCode code="delete_at_scope" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Deletes the entire set of tags on a resource or subscription. Deletes the entire set of tags on a resource or subscription.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag_name">
    <td><CopyableCode code="tag_name" /></td>
    <td><code>string</code></td>
    <td>The name of the tag. Required.</td>
</tr>
<tr id="parameter-tag_value">
    <td><CopyableCode code="tag_value" /></td>
    <td><code>string</code></td>
    <td>The value of the tag to delete. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' },
        { label: 'get_at_scope', value: 'get_at_scope' }
    ]}
>
<TabItem value="list">

Gets a summary of tag usage under the subscription. This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result.

```sql
SELECT
id,
count,
tagName,
values
FROM azure.resource.tags
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_scope">

Gets the entire set of tags on a resource or subscription. Gets the entire set of tags on a resource or subscription.

```sql
SELECT
id,
name,
systemData,
tags,
type
FROM azure.resource.tags
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_value"
    values={[
        { label: 'create_or_update_value', value: 'create_or_update_value' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_scope', value: 'create_or_update_at_scope' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_value">

Creates a predefined value for a predefined tag name. This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.

```sql
INSERT INTO azure.resource.tags (
tag_name,
tag_value,
subscription_id
)
SELECT 
'{{ tag_name }}',
'{{ tag_value }}',
'{{ subscription_id }}'
RETURNING
id,
count,
tagValue
;
```
</TabItem>
<TabItem value="create_or_update">

Creates a predefined tag name. This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'.

```sql
INSERT INTO azure.resource.tags (
tag_name,
subscription_id
)
SELECT 
'{{ tag_name }}',
'{{ subscription_id }}'
RETURNING
id,
count,
tagName,
values
;
```
</TabItem>
<TabItem value="create_or_update_at_scope">

Creates or updates the entire set of tags on a resource or subscription. This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.

```sql
INSERT INTO azure.resource.tags (
properties,
scope
)
SELECT 
'{{ properties }}' /* required */,
'{{ scope }}'
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
- name: tags
  props:
    - name: tag_name
      value: "{{ tag_name }}"
      description: Required parameter for the tags resource.
    - name: tag_value
      value: "{{ tag_value }}"
      description: Required parameter for the tags resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the tags resource.
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the tags resource.
    - name: properties
      description: |
        The set of tags. Required.
      value:
        tags: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_at_scope"
    values={[
        { label: 'update_at_scope', value: 'update_at_scope' }
    ]}
>
<TabItem value="update_at_scope">

Selectively updates the set of tags on a resource or subscription. This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The 'replace' option replaces the entire set of existing tags with a new set. The 'merge' option allows adding tags with new names and updating the values of tags with existing names. The 'delete' option allows selectively deleting tags based on given names or name/value pairs.

```sql
UPDATE azure.resource.tags
SET 
operation = '{{ operation }}',
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_value"
    values={[
        { label: 'create_or_update_value', value: 'create_or_update_value' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_scope', value: 'create_or_update_at_scope' }
    ]}
>
<TabItem value="create_or_update_value">

Creates a predefined value for a predefined tag name. This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.

```sql
REPLACE azure.resource.tags
SET 
-- No updatable properties
WHERE 
tag_name = '{{ tag_name }}' --required
AND tag_value = '{{ tag_value }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
count,
tagValue;
```
</TabItem>
<TabItem value="create_or_update">

Creates a predefined tag name. This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'.

```sql
REPLACE azure.resource.tags
SET 
-- No updatable properties
WHERE 
tag_name = '{{ tag_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
count,
tagName,
values;
```
</TabItem>
<TabItem value="create_or_update_at_scope">

Creates or updates the entire set of tags on a resource or subscription. This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.

```sql
REPLACE azure.resource.tags
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_value"
    values={[
        { label: 'delete_value', value: 'delete_value' },
        { label: 'delete', value: 'delete' },
        { label: 'delete_at_scope', value: 'delete_at_scope' }
    ]}
>
<TabItem value="delete_value">

Deletes a predefined tag value for a predefined tag name. This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource.

```sql
DELETE FROM azure.resource.tags
WHERE tag_name = '{{ tag_name }}' --required
AND tag_value = '{{ tag_value }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a predefined tag name. This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted.

```sql
DELETE FROM azure.resource.tags
WHERE tag_name = '{{ tag_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_scope">

Deletes the entire set of tags on a resource or subscription. Deletes the entire set of tags on a resource or subscription.

```sql
DELETE FROM azure.resource.tags
WHERE scope = '{{ scope }}' --required
;
```
</TabItem>
</Tabs>
