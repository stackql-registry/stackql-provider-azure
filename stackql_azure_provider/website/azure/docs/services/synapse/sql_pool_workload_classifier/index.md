--- 
title: sql_pool_workload_classifier
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_workload_classifier
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_workload_classifier</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_pool_workload_classifier" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_workload_classifier" /></td></tr>
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
    <td><CopyableCode code="context" /></td>
    <td><code>string</code></td>
    <td>The workload classifier context.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>The workload classifier end time for classification.</td>
</tr>
<tr>
    <td><CopyableCode code="importance" /></td>
    <td><code>string</code></td>
    <td>The workload classifier importance.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The workload classifier label.</td>
</tr>
<tr>
    <td><CopyableCode code="memberName" /></td>
    <td><code>string</code></td>
    <td>The workload classifier member name.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The workload classifier start time for classification.</td>
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
    <td><CopyableCode code="context" /></td>
    <td><code>string</code></td>
    <td>The workload classifier context.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>The workload classifier end time for classification.</td>
</tr>
<tr>
    <td><CopyableCode code="importance" /></td>
    <td><code>string</code></td>
    <td>The workload classifier importance.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The workload classifier label.</td>
</tr>
<tr>
    <td><CopyableCode code="memberName" /></td>
    <td><code>string</code></td>
    <td>The workload classifier member name.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>The workload classifier start time for classification.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-workload_group_name"><code>workload_group_name</code></a>, <a href="#parameter-workload_classifier_name"><code>workload_classifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get workload classifier. Get a workload classifier of Sql pool's workload group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-workload_group_name"><code>workload_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sql pool's workload classifier. Get list of Sql pool's workload classifier for workload groups.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-workload_group_name"><code>workload_group_name</code></a>, <a href="#parameter-workload_classifier_name"><code>workload_classifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Or Update workload classifier. Create Or Update workload classifier for a Sql pool's workload group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-workload_group_name"><code>workload_group_name</code></a>, <a href="#parameter-workload_classifier_name"><code>workload_classifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Or Update workload classifier. Create Or Update workload classifier for a Sql pool's workload group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-workload_group_name"><code>workload_group_name</code></a>, <a href="#parameter-workload_classifier_name"><code>workload_classifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove workload classifier. Remove workload classifier of a Sql pool's workload group.</td>
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
<tr id="parameter-sql_pool_name">
    <td><CopyableCode code="sql_pool_name" /></td>
    <td><code>string</code></td>
    <td>SQL pool name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workload_classifier_name">
    <td><CopyableCode code="workload_classifier_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workload classifier. Required.</td>
</tr>
<tr id="parameter-workload_group_name">
    <td><CopyableCode code="workload_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workload group. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get workload classifier. Get a workload classifier of Sql pool's workload group.

```sql
SELECT
id,
name,
context,
endTime,
importance,
label,
memberName,
startTime,
type
FROM azure.synapse.sql_pool_workload_classifier
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND workload_group_name = '{{ workload_group_name }}' -- required
AND workload_classifier_name = '{{ workload_classifier_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Sql pool's workload classifier. Get list of Sql pool's workload classifier for workload groups.

```sql
SELECT
id,
name,
context,
endTime,
importance,
label,
memberName,
startTime,
type
FROM azure.synapse.sql_pool_workload_classifier
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND workload_group_name = '{{ workload_group_name }}' -- required
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

Create Or Update workload classifier. Create Or Update workload classifier for a Sql pool's workload group.

```sql
INSERT INTO azure.synapse.sql_pool_workload_classifier (
properties,
resource_group_name,
workspace_name,
sql_pool_name,
workload_group_name,
workload_classifier_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ sql_pool_name }}',
'{{ workload_group_name }}',
'{{ workload_classifier_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sql_pool_workload_classifier
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_pool_workload_classifier resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the sql_pool_workload_classifier resource.
    - name: sql_pool_name
      value: "{{ sql_pool_name }}"
      description: Required parameter for the sql_pool_workload_classifier resource.
    - name: workload_group_name
      value: "{{ workload_group_name }}"
      description: Required parameter for the sql_pool_workload_classifier resource.
    - name: workload_classifier_name
      value: "{{ workload_classifier_name }}"
      description: Required parameter for the sql_pool_workload_classifier resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_pool_workload_classifier resource.
    - name: properties
      value:
        memberName: "{{ memberName }}"
        label: "{{ label }}"
        context: "{{ context }}"
        startTime: "{{ startTime }}"
        endTime: "{{ endTime }}"
        importance: "{{ importance }}"
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

Create Or Update workload classifier. Create Or Update workload classifier for a Sql pool's workload group.

```sql
REPLACE azure.synapse.sql_pool_workload_classifier
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND workload_group_name = '{{ workload_group_name }}' --required
AND workload_classifier_name = '{{ workload_classifier_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Remove workload classifier. Remove workload classifier of a Sql pool's workload group.

```sql
DELETE FROM azure.synapse.sql_pool_workload_classifier
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND workload_group_name = '{{ workload_group_name }}' --required
AND workload_classifier_name = '{{ workload_classifier_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
