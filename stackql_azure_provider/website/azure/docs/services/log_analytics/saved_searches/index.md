--- 
title: saved_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_searches
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>saved_searches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="saved_searches" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.saved_searches" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the saved search. This helps the user to find a saved search faster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Saved search display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAlias" /></td>
    <td><code>string</code></td>
    <td>The function alias if query serves as a function.</td>
</tr>
<tr>
    <td><CopyableCode code="functionParameters" /></td>
    <td><code>string</code></td>
    <td>The optional function parameters if query serves as a function. Value should be in the following format: 'param-name1:type1 = default_value1, param-name2:type2 = default_value2'. For more examples and proper syntax please refer to `https://docs.microsoft.com/en-us/azure/kusto/query/functions/user-defined-functions `_.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The query expression for the saved search. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags attached to the saved search.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The version number of the query language. The current version is 2 and is the default.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the saved search. This helps the user to find a saved search faster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Saved search display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAlias" /></td>
    <td><code>string</code></td>
    <td>The function alias if query serves as a function.</td>
</tr>
<tr>
    <td><CopyableCode code="functionParameters" /></td>
    <td><code>string</code></td>
    <td>The optional function parameters if query serves as a function. Value should be in the following format: 'param-name1:type1 = default_value1, param-name2:type2 = default_value2'. For more examples and proper syntax please refer to `https://docs.microsoft.com/en-us/azure/kusto/query/functions/user-defined-functions `_.</td>
</tr>
<tr>
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The query expression for the saved search. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags attached to the saved search.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The version number of the query language. The current version is 2 and is the default.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-saved_search_id"><code>saved_search_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified saved search for a given workspace.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the saved searches for a given Log Analytics Workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-saved_search_id"><code>saved_search_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a saved search for a given workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-saved_search_id"><code>saved_search_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a saved search for a given workspace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-saved_search_id"><code>saved_search_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified saved search in a given workspace.</td>
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
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-saved_search_id">
    <td><CopyableCode code="saved_search_id" /></td>
    <td><code>string</code></td>
    <td>The id of the saved search. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Gets the specified saved search for a given workspace.

```sql
SELECT
id,
name,
category,
displayName,
etag,
functionAlias,
functionParameters,
query,
systemData,
tags,
type,
version
FROM azure.log_analytics.saved_searches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND saved_search_id = '{{ saved_search_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

Gets the saved searches for a given Log Analytics Workspace.

```sql
SELECT
id,
name,
category,
displayName,
etag,
functionAlias,
functionParameters,
query,
systemData,
tags,
type,
version
FROM azure.log_analytics.saved_searches
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Creates or updates a saved search for a given workspace.

```sql
INSERT INTO azure.log_analytics.saved_searches (
properties,
etag,
resource_group_name,
workspace_name,
saved_search_id,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ saved_search_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: saved_searches
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the saved_searches resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the saved_searches resource.
    - name: saved_search_id
      value: "{{ saved_search_id }}"
      description: Required parameter for the saved_searches resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the saved_searches resource.
    - name: properties
      description: |
        The properties of the saved search. Required.
      value:
        category: "{{ category }}"
        displayName: "{{ displayName }}"
        query: "{{ query }}"
        functionAlias: "{{ functionAlias }}"
        functionParameters: "{{ functionParameters }}"
        version: {{ version }}
        tags:
          - name: "{{ name }}"
            value: "{{ value }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag.
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

Creates or updates a saved search for a given workspace.

```sql
REPLACE azure.log_analytics.saved_searches
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND saved_search_id = '{{ saved_search_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
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

Deletes the specified saved search in a given workspace.

```sql
DELETE FROM azure.log_analytics.saved_searches
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND saved_search_id = '{{ saved_search_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
