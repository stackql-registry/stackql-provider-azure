--- 
title: sql_pool_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_sensitivity_labels
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

Creates, updates, deletes, gets or lists a <code>sql_pool_sensitivity_labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_pool_sensitivity_labels" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_recommended', value: 'list_recommended' }
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
    <td><CopyableCode code="columnName" /></td>
    <td><code>string</code></td>
    <td>The column name.</td>
</tr>
<tr>
    <td><CopyableCode code="informationType" /></td>
    <td><code>string</code></td>
    <td>The information type.</td>
</tr>
<tr>
    <td><CopyableCode code="informationTypeId" /></td>
    <td><code>string</code></td>
    <td>The information type ID.</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Is sensitivity recommendation disabled. Applicable for recommended sensitivity label only. Specifies whether the sensitivity recommendation on this column is disabled (dismissed) or not.</td>
</tr>
<tr>
    <td><CopyableCode code="labelId" /></td>
    <td><code>string</code></td>
    <td>The label ID.</td>
</tr>
<tr>
    <td><CopyableCode code="labelName" /></td>
    <td><code>string</code></td>
    <td>The label name.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>managed by.</td>
</tr>
<tr>
    <td><CopyableCode code="rank" /></td>
    <td><code>string</code></td>
    <td>Known values are: "None", "Low", "Medium", "High", and "Critical".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaName" /></td>
    <td><code>string</code></td>
    <td>The schema name.</td>
</tr>
<tr>
    <td><CopyableCode code="tableName" /></td>
    <td><code>string</code></td>
    <td>The table name.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_recommended">

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
    <td><CopyableCode code="columnName" /></td>
    <td><code>string</code></td>
    <td>The column name.</td>
</tr>
<tr>
    <td><CopyableCode code="informationType" /></td>
    <td><code>string</code></td>
    <td>The information type.</td>
</tr>
<tr>
    <td><CopyableCode code="informationTypeId" /></td>
    <td><code>string</code></td>
    <td>The information type ID.</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Is sensitivity recommendation disabled. Applicable for recommended sensitivity label only. Specifies whether the sensitivity recommendation on this column is disabled (dismissed) or not.</td>
</tr>
<tr>
    <td><CopyableCode code="labelId" /></td>
    <td><code>string</code></td>
    <td>The label ID.</td>
</tr>
<tr>
    <td><CopyableCode code="labelName" /></td>
    <td><code>string</code></td>
    <td>The label name.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>managed by.</td>
</tr>
<tr>
    <td><CopyableCode code="rank" /></td>
    <td><code>string</code></td>
    <td>Known values are: "None", "Low", "Medium", "High", and "Critical".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaName" /></td>
    <td><code>string</code></td>
    <td>The schema name.</td>
</tr>
<tr>
    <td><CopyableCode code="tableName" /></td>
    <td><code>string</code></td>
    <td>The table name.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-sensitivity_label_source"><code>sensitivity_label_source</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the sensitivity label of a given column.</td>
</tr>
<tr>
    <td><a href="#list_recommended"><CopyableCode code="list_recommended" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-includeDisabledRecommendations"><code>includeDisabledRecommendations</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets sensitivity labels of a given SQL pool. Gets sensitivity labels of a given SQL pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the sensitivity label of a given column in a Sql pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update sensitivity labels of a given SQL Pool using an operations batch.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the sensitivity label of a given column in a Sql pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the sensitivity label of a given column in a Sql pool.</td>
</tr>
<tr>
    <td><a href="#list_current"><CopyableCode code="list_current" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets SQL pool sensitivity labels. Gets SQL pool sensitivity labels.</td>
</tr>
<tr>
    <td><a href="#enable_recommendation"><CopyableCode code="enable_recommendation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns).</td>
</tr>
<tr>
    <td><a href="#disable_recommendation"><CopyableCode code="disable_recommendation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables sensitivity recommendations on a given column.</td>
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
<tr id="parameter-column_name">
    <td><CopyableCode code="column_name" /></td>
    <td><code>string</code></td>
    <td>The name of the column. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the schema. Required.</td>
</tr>
<tr id="parameter-sensitivity_label_source">
    <td><CopyableCode code="sensitivity_label_source" /></td>
    <td><code>string</code></td>
    <td>The source of the sensitivity label. Known values are: "current" and "recommended". Required.</td>
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
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>The name of the table. Required.</td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that filters elements in the collection. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>An OData query option to indicate how many elements to skip in the collection. Default value is None.</td>
</tr>
<tr id="parameter-includeDisabledRecommendations">
    <td><CopyableCode code="includeDisabledRecommendations" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to include disabled recommendations or not. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_recommended', value: 'list_recommended' }
    ]}
>
<TabItem value="get">

Gets the sensitivity label of a given column.

```sql
SELECT
id,
name,
columnName,
informationType,
informationTypeId,
isDisabled,
labelId,
labelName,
managedBy,
rank,
schemaName,
tableName,
type
FROM azure.synapse.sql_pool_sensitivity_labels
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND table_name = '{{ table_name }}' -- required
AND column_name = '{{ column_name }}' -- required
AND sensitivity_label_source = '{{ sensitivity_label_source }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_recommended">

Gets sensitivity labels of a given SQL pool. Gets sensitivity labels of a given SQL pool.

```sql
SELECT
id,
name,
columnName,
informationType,
informationTypeId,
isDisabled,
labelId,
labelName,
managedBy,
rank,
schemaName,
tableName,
type
FROM azure.synapse.sql_pool_sensitivity_labels
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND includeDisabledRecommendations = '{{ includeDisabledRecommendations }}'
AND $skipToken = '{{ $skipToken }}'
AND $filter = '{{ $filter }}'
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

Creates or updates the sensitivity label of a given column in a Sql pool.

```sql
INSERT INTO azure.synapse.sql_pool_sensitivity_labels (
properties,
resource_group_name,
workspace_name,
sql_pool_name,
schema_name,
table_name,
column_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ sql_pool_name }}',
'{{ schema_name }}',
'{{ table_name }}',
'{{ column_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
managedBy,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sql_pool_sensitivity_labels
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: sql_pool_name
      value: "{{ sql_pool_name }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: schema_name
      value: "{{ schema_name }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: table_name
      value: "{{ table_name }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: column_name
      value: "{{ column_name }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_pool_sensitivity_labels resource.
    - name: properties
      value:
        labelName: "{{ labelName }}"
        labelId: "{{ labelId }}"
        informationType: "{{ informationType }}"
        informationTypeId: "{{ informationTypeId }}"
        rank: "{{ rank }}"
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

Update sensitivity labels of a given SQL Pool using an operations batch.

```sql
UPDATE azure.synapse.sql_pool_sensitivity_labels
SET 
operations = '{{ operations }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required;
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

Creates or updates the sensitivity label of a given column in a Sql pool.

```sql
REPLACE azure.synapse.sql_pool_sensitivity_labels
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND table_name = '{{ table_name }}' --required
AND column_name = '{{ column_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
managedBy,
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

Deletes the sensitivity label of a given column in a Sql pool.

```sql
DELETE FROM azure.synapse.sql_pool_sensitivity_labels
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND table_name = '{{ table_name }}' --required
AND column_name = '{{ column_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_current"
    values={[
        { label: 'list_current', value: 'list_current' },
        { label: 'enable_recommendation', value: 'enable_recommendation' },
        { label: 'disable_recommendation', value: 'disable_recommendation' }
    ]}
>
<TabItem value="list_current">

Gets SQL pool sensitivity labels. Gets SQL pool sensitivity labels.

```sql
EXEC azure.synapse.sql_pool_sensitivity_labels.list_current 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@sql_pool_name='{{ sql_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="enable_recommendation">

Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns).

```sql
EXEC azure.synapse.sql_pool_sensitivity_labels.enable_recommendation 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@sql_pool_name='{{ sql_pool_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@column_name='{{ column_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="disable_recommendation">

Disables sensitivity recommendations on a given column.

```sql
EXEC azure.synapse.sql_pool_sensitivity_labels.disable_recommendation 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@sql_pool_name='{{ sql_pool_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@column_name='{{ column_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
