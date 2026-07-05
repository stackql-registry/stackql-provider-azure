--- 
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - loganalytics
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

Creates, updates, deletes, gets or lists a <code>tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.loganalytics.tables" /></td></tr>
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
    <td><CopyableCode code="archiveRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The tables long-term retention in days. Calculated as (totalRetentionInDays-retentionInDays).</td>
</tr>
<tr>
    <td><CopyableCode code="lastPlanModifiedDate" /></td>
    <td><code>string</code></td>
    <td>The timestamp that table plan was last modified (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>Instruct the system how to handle and charge the logs ingested to this table. Known values are: "Basic", "Analytics", and "Auxiliary". (Basic, Analytics, Auxiliary)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Table's current provisioning state. If set to 'updating', indicates a resource lock due to ongoing operation, forbidding any update to the table until the ongoing operation is concluded. Known values are: "Updating", "InProgress", "Succeeded", and "Deleting". (Updating, InProgress, Succeeded, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="restoredLogs" /></td>
    <td><code>object</code></td>
    <td>Parameters of the restore operation that initiated this table.</td>
</tr>
<tr>
    <td><CopyableCode code="resultStatistics" /></td>
    <td><code>object</code></td>
    <td>Search job execution statistics.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInDays" /></td>
    <td><code>integer</code></td>
    <td>In Analytics table: the tables analytics retention in days, between 4 and 730. Setting this property to -1 will default to the workspace retention. In Basic and Auxiliary table: read only property.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInDaysAsDefault" /></td>
    <td><code>boolean</code></td>
    <td>True - Value originates from workspace retention in days, False - Customer specific.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>Table schema.</td>
</tr>
<tr>
    <td><CopyableCode code="searchResults" /></td>
    <td><code>object</code></td>
    <td>Parameters of the search job that initiated this table.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The table total retention in days, between 4 and 4383. Setting this property to -1 will default to retentionInDays.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRetentionInDaysAsDefault" /></td>
    <td><code>boolean</code></td>
    <td>True - Value originates from retention in days, False - Customer specific.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="archiveRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The tables long-term retention in days. Calculated as (totalRetentionInDays-retentionInDays).</td>
</tr>
<tr>
    <td><CopyableCode code="lastPlanModifiedDate" /></td>
    <td><code>string</code></td>
    <td>The timestamp that table plan was last modified (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>Instruct the system how to handle and charge the logs ingested to this table. Known values are: "Basic", "Analytics", and "Auxiliary". (Basic, Analytics, Auxiliary)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Table's current provisioning state. If set to 'updating', indicates a resource lock due to ongoing operation, forbidding any update to the table until the ongoing operation is concluded. Known values are: "Updating", "InProgress", "Succeeded", and "Deleting". (Updating, InProgress, Succeeded, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="restoredLogs" /></td>
    <td><code>object</code></td>
    <td>Parameters of the restore operation that initiated this table.</td>
</tr>
<tr>
    <td><CopyableCode code="resultStatistics" /></td>
    <td><code>object</code></td>
    <td>Search job execution statistics.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInDays" /></td>
    <td><code>integer</code></td>
    <td>In Analytics table: the tables analytics retention in days, between 4 and 730. Setting this property to -1 will default to the workspace retention. In Basic and Auxiliary table: read only property.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionInDaysAsDefault" /></td>
    <td><code>boolean</code></td>
    <td>True - Value originates from workspace retention in days, False - Customer specific.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>Table schema.</td>
</tr>
<tr>
    <td><CopyableCode code="searchResults" /></td>
    <td><code>object</code></td>
    <td>Parameters of the search job that initiated this table.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRetentionInDays" /></td>
    <td><code>integer</code></td>
    <td>The table total retention in days, between 4 and 4383. Setting this property to -1 will default to retentionInDays.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRetentionInDaysAsDefault" /></td>
    <td><code>boolean</code></td>
    <td>True - Value originates from retention in days, False - Customer specific.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Log Analytics workspace table.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the tables for the specified Log Analytics workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update or Create a Log Analytics workspace table.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Log Analytics workspace table.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update or Create a Log Analytics workspace table.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Log Analytics workspace table.</td>
</tr>
<tr>
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrate a Log Analytics table from support of the Data Collector API and Custom Fields features to support of Data Collection Rule-based Custom Logs.</td>
</tr>
<tr>
    <td><a href="#cancel_search"><CopyableCode code="cancel_search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel a log analytics workspace search results table query run.</td>
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

Gets a Log Analytics workspace table.

```sql
SELECT
id,
name,
archiveRetentionInDays,
lastPlanModifiedDate,
plan,
provisioningState,
restoredLogs,
resultStatistics,
retentionInDays,
retentionInDaysAsDefault,
schema,
searchResults,
systemData,
totalRetentionInDays,
totalRetentionInDaysAsDefault,
type
FROM azure.loganalytics.tables
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND table_name = '{{ table_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

Gets all the tables for the specified Log Analytics workspace.

```sql
SELECT
id,
name,
archiveRetentionInDays,
lastPlanModifiedDate,
plan,
provisioningState,
restoredLogs,
resultStatistics,
retentionInDays,
retentionInDaysAsDefault,
schema,
searchResults,
systemData,
totalRetentionInDays,
totalRetentionInDaysAsDefault,
type
FROM azure.loganalytics.tables
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

Update or Create a Log Analytics workspace table.

```sql
INSERT INTO azure.loganalytics.tables (
properties,
resource_group_name,
workspace_name,
table_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ table_name }}',
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
- name: tables
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the tables resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the tables resource.
    - name: table_name
      value: "{{ table_name }}"
      description: Required parameter for the tables resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the tables resource.
    - name: properties
      description: |
        Table's properties.
      value:
        retentionInDays: {{ retentionInDays }}
        totalRetentionInDays: {{ totalRetentionInDays }}
        archiveRetentionInDays: {{ archiveRetentionInDays }}
        searchResults:
          query: "{{ query }}"
          description: "{{ description }}"
          limit: {{ limit }}
          startSearchTime: "{{ startSearchTime }}"
          endSearchTime: "{{ endSearchTime }}"
          sourceTable: "{{ sourceTable }}"
          azureAsyncOperationId: "{{ azureAsyncOperationId }}"
        restoredLogs:
          startRestoreTime: "{{ startRestoreTime }}"
          endRestoreTime: "{{ endRestoreTime }}"
          sourceTable: "{{ sourceTable }}"
          azureAsyncOperationId: "{{ azureAsyncOperationId }}"
        resultStatistics:
          progress: {{ progress }}
          ingestedRecords: {{ ingestedRecords }}
          scannedGb: {{ scannedGb }}
        plan: "{{ plan }}"
        lastPlanModifiedDate: "{{ lastPlanModifiedDate }}"
        schema:
          name: "{{ name }}"
          displayName: "{{ displayName }}"
          description: "{{ description }}"
          columns:
            - name: "{{ name }}"
              type: "{{ type }}"
              dataTypeHint: "{{ dataTypeHint }}"
              displayName: "{{ displayName }}"
              description: "{{ description }}"
              isDefaultDisplay: {{ isDefaultDisplay }}
              isHidden: {{ isHidden }}
          standardColumns:
            - name: "{{ name }}"
              type: "{{ type }}"
              dataTypeHint: "{{ dataTypeHint }}"
              displayName: "{{ displayName }}"
              description: "{{ description }}"
              isDefaultDisplay: {{ isDefaultDisplay }}
              isHidden: {{ isHidden }}
          categories:
            - "{{ categories }}"
          labels:
            - "{{ labels }}"
          source: "{{ source }}"
          tableType: "{{ tableType }}"
          tableSubType: "{{ tableSubType }}"
          solutions:
            - "{{ solutions }}"
        provisioningState: "{{ provisioningState }}"
        retentionInDaysAsDefault: {{ retentionInDaysAsDefault }}
        totalRetentionInDaysAsDefault: {{ totalRetentionInDaysAsDefault }}
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

Update a Log Analytics workspace table.

```sql
UPDATE azure.loganalytics.tables
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND table_name = '{{ table_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Update or Create a Log Analytics workspace table.

```sql
REPLACE azure.loganalytics.tables
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND table_name = '{{ table_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a Log Analytics workspace table.

```sql
DELETE FROM azure.loganalytics.tables
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND table_name = '{{ table_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="migrate"
    values={[
        { label: 'migrate', value: 'migrate' },
        { label: 'cancel_search', value: 'cancel_search' }
    ]}
>
<TabItem value="migrate">

Migrate a Log Analytics table from support of the Data Collector API and Custom Fields features to support of Data Collection Rule-based Custom Logs.

```sql
EXEC azure.loganalytics.tables.migrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_search">

Cancel a log analytics workspace search results table query run.

```sql
EXEC azure.loganalytics.tables.cancel_search 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@table_name='{{ table_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
