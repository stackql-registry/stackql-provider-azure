--- 
title: entity_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_queries
  - security_insight
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

Creates, updates, deletes, gets or lists an <code>entity_queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entity_queries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.entity_queries" /></td></tr>
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
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. Known values are: "Expansion", "Insight", and "Activity".</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. Known values are: "Expansion", "Insight", and "Activity".</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-entity_query_id"><code>entity_query_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an entity query.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-kind"><code>kind</code></a></td>
    <td>Gets all entity queries.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-entity_query_id"><code>entity_query_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates or updates the entity query.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-entity_query_id"><code>entity_query_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates or updates the entity query.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-entity_query_id"><code>entity_query_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the entity query.</td>
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
<tr id="parameter-entity_query_id">
    <td><CopyableCode code="entity_query_id" /></td>
    <td><code>string</code></td>
    <td>entity query ID. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The entity query kind we want to fetch. Known values are: "Activity", "Insight", "SecurityAlert", "Bookmark", "Expansion", "GuidedInsight", and "Anomaly". Default value is None.</td>
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

Gets an entity query.

```sql
SELECT
id,
name,
etag,
kind,
systemData,
type
FROM azure.security_insight.entity_queries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND entity_query_id = '{{ entity_query_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all entity queries.

```sql
SELECT
id,
name,
etag,
kind,
systemData,
type
FROM azure.security_insight.entity_queries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND kind = '{{ kind }}'
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

Creates or updates the entity query.

```sql
INSERT INTO azure.security_insight.entity_queries (
etag,
kind,
resource_group_name,
workspace_name,
entity_query_id,
subscription_id
)
SELECT 
'{{ etag }}',
'{{ kind }}' /* required */,
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ entity_query_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entity_queries
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the entity_queries resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the entity_queries resource.
    - name: entity_query_id
      value: "{{ entity_query_id }}"
      description: Required parameter for the entity_queries resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the entity_queries resource.
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        the entity query kind. Required. "Activity"
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

Creates or updates the entity query.

```sql
REPLACE azure.security_insight.entity_queries
SET 
etag = '{{ etag }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND entity_query_id = '{{ entity_query_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
etag,
kind,
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

Delete the entity query.

```sql
DELETE FROM azure.security_insight.entity_queries
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND entity_query_id = '{{ entity_query_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
