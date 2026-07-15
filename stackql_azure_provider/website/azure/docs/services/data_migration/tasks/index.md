--- 
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.tasks" /></td></tr>
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
    <td><CopyableCode code="clientData" /></td>
    <td><code>object</code></td>
    <td>Key value pairs of client data to attach meta data information to task.</td>
</tr>
<tr>
    <td><CopyableCode code="commands" /></td>
    <td><code>array</code></td>
    <td>Array of command properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Array of errors. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the task. This is ignored if submitted. Known values are: "Unknown", "Queued", "Running", "Canceled", "Succeeded", "Failed", "FailedInputValidation", and "Faulted". (Unknown, Queued, Running, Canceled, Succeeded, Failed, FailedInputValidation, Faulted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskType" /></td>
    <td><code>string</code></td>
    <td>Task type. Required. Known values are: "Connect.MongoDb", "ConnectToSource.SqlServer", "ConnectToSource.SqlServer.Sync", "ConnectToSource.PostgreSql.Sync", "ConnectToSource.MySql", "ConnectToSource.Oracle.Sync", "ConnectToTarget.SqlDb", "ConnectToTarget.SqlDb.Sync", "ConnectToTarget.AzureDbForPostgreSql.Sync", "ConnectToTarget.Oracle.AzureDbForPostgreSql.Sync", "ConnectToTarget.AzureSqlDbMI", "ConnectToTarget.AzureSqlDbMI.Sync.LRS", "ConnectToTarget.AzureDbForMySql", "GetUserTables.Sql", "GetUserTables.AzureSqlDb.Sync", "GetUserTablesOracle", "GetUserTablesPostgreSql", "GetUserTablesMySql", "Migrate.MongoDb", "Migrate.SqlServer.AzureSqlDbMI", "Migrate.SqlServer.AzureSqlDbMI.Sync.LRS", "Migrate.SqlServer.SqlDb", "Migrate.SqlServer.AzureSqlDb.Sync", "Migrate.MySql.AzureDbForMySql.Sync", "Migrate.MySql.AzureDbForMySql", "Migrate.PostgreSql.AzureDbForPostgreSql.SyncV2", "Migrate.Oracle.AzureDbForPostgreSql.Sync", "ValidateMigrationInput.SqlServer.SqlDb.Sync", "ValidateMigrationInput.SqlServer.AzureSqlDbMI", "ValidateMigrationInput.SqlServer.AzureSqlDbMI.Sync.LRS", "Validate.MongoDb", "Validate.Oracle.AzureDbPostgreSql.Sync", "GetTDECertificates.Sql", "Migrate.Ssis", "Service.Check.OCI", "Service.Upload.OCI", "Service.Install.OCI", and "MigrateSchemaSqlServerSqlDb".</td>
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
    <td><CopyableCode code="clientData" /></td>
    <td><code>object</code></td>
    <td>Key value pairs of client data to attach meta data information to task.</td>
</tr>
<tr>
    <td><CopyableCode code="commands" /></td>
    <td><code>array</code></td>
    <td>Array of command properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Array of errors. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>HTTP strong entity tag value. This is ignored if submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the task. This is ignored if submitted. Known values are: "Unknown", "Queued", "Running", "Canceled", "Succeeded", "Failed", "FailedInputValidation", and "Faulted". (Unknown, Queued, Running, Canceled, Succeeded, Failed, FailedInputValidation, Faulted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskType" /></td>
    <td><code>string</code></td>
    <td>Task type. Required. Known values are: "Connect.MongoDb", "ConnectToSource.SqlServer", "ConnectToSource.SqlServer.Sync", "ConnectToSource.PostgreSql.Sync", "ConnectToSource.MySql", "ConnectToSource.Oracle.Sync", "ConnectToTarget.SqlDb", "ConnectToTarget.SqlDb.Sync", "ConnectToTarget.AzureDbForPostgreSql.Sync", "ConnectToTarget.Oracle.AzureDbForPostgreSql.Sync", "ConnectToTarget.AzureSqlDbMI", "ConnectToTarget.AzureSqlDbMI.Sync.LRS", "ConnectToTarget.AzureDbForMySql", "GetUserTables.Sql", "GetUserTables.AzureSqlDb.Sync", "GetUserTablesOracle", "GetUserTablesPostgreSql", "GetUserTablesMySql", "Migrate.MongoDb", "Migrate.SqlServer.AzureSqlDbMI", "Migrate.SqlServer.AzureSqlDbMI.Sync.LRS", "Migrate.SqlServer.SqlDb", "Migrate.SqlServer.AzureSqlDb.Sync", "Migrate.MySql.AzureDbForMySql.Sync", "Migrate.MySql.AzureDbForMySql", "Migrate.PostgreSql.AzureDbForPostgreSql.SyncV2", "Migrate.Oracle.AzureDbForPostgreSql.Sync", "ValidateMigrationInput.SqlServer.SqlDb.Sync", "ValidateMigrationInput.SqlServer.AzureSqlDbMI", "ValidateMigrationInput.SqlServer.AzureSqlDbMI.Sync.LRS", "Validate.MongoDb", "Validate.Oracle.AzureDbPostgreSql.Sync", "GetTDECertificates.Sql", "Migrate.Ssis", "Service.Check.OCI", "Service.Upload.OCI", "Service.Install.OCI", and "MigrateSchemaSqlServerSqlDb".</td>
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
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get task information. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The GET method retrieves information about a task.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-taskType"><code>taskType</code></a></td>
    <td>Get tasks in a service. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteRunningTasks"><code>deleteRunningTasks</code></a></td>
    <td>Delete task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The DELETE method deletes a task, canceling it first if it's running.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel a task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method cancels a task if it's currently queued or running.</td>
</tr>
<tr>
    <td><a href="#command"><CopyableCode code="command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-commandType"><code>commandType</code></a></td>
    <td></td>
    <td>Execute a command on a task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method executes a command on a running task.</td>
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
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-task_name">
    <td><CopyableCode code="task_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Task. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expand the response. Default value is None.</td>
</tr>
<tr id="parameter-deleteRunningTasks">
    <td><CopyableCode code="deleteRunningTasks" /></td>
    <td><code>boolean</code></td>
    <td>Delete the resource even if it contains running tasks. Default value is None.</td>
</tr>
<tr id="parameter-taskType">
    <td><CopyableCode code="taskType" /></td>
    <td><code>string</code></td>
    <td>Filter tasks by task type. Default value is None.</td>
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

Get task information. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The GET method retrieves information about a task.

```sql
SELECT
id,
name,
clientData,
commands,
errors,
etag,
state,
systemData,
taskType,
type
FROM azure.data_migration.tasks
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND task_name = '{{ task_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get tasks in a service. The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.

```sql
SELECT
id,
name,
clientData,
commands,
errors,
etag,
state,
systemData,
taskType,
type
FROM azure.data_migration.tasks
WHERE group_name = '{{ group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND taskType = '{{ taskType }}'
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

Create or update task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one.

```sql
INSERT INTO azure.data_migration.tasks (
properties,
etag,
group_name,
service_name,
project_name,
task_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ group_name }}',
'{{ service_name }}',
'{{ project_name }}',
'{{ task_name }}',
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
- name: tasks
  props:
    - name: group_name
      value: "{{ group_name }}"
      description: Required parameter for the tasks resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the tasks resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the tasks resource.
    - name: task_name
      value: "{{ task_name }}"
      description: Required parameter for the tasks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the tasks resource.
    - name: properties
      description: |
        Custom task properties.
      value:
        taskType: "{{ taskType }}"
        errors:
          - code: "{{ code }}"
            message: "{{ message }}"
            details: "{{ details }}"
        state: "{{ state }}"
        commands:
          - commandType: "{{ commandType }}"
            errors: "{{ errors }}"
            state: "{{ state }}"
        clientData: "{{ clientData }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        HTTP strong entity tag value. This is ignored if submitted.
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

Create or update task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so.

```sql
UPDATE azure.data_migration.tasks
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND task_name = '{{ task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new task or updates an existing one, although since tasks have no mutable custom properties, there is little reason to update an existing one.

```sql
REPLACE azure.data_migration.tasks
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND task_name = '{{ task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Delete task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The DELETE method deletes a task, canceling it first if it's running.

```sql
DELETE FROM azure.data_migration.tasks
WHERE group_name = '{{ group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND project_name = '{{ project_name }}' --required
AND task_name = '{{ task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteRunningTasks = '{{ deleteRunningTasks }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'command', value: 'command' }
    ]}
>
<TabItem value="cancel">

Cancel a task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method cancels a task if it's currently queued or running.

```sql
EXEC azure.data_migration.tasks.cancel 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@task_name='{{ task_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="command">

Execute a command on a task. The tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method executes a command on a running task.

```sql
EXEC azure.data_migration.tasks.command 
@group_name='{{ group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@task_name='{{ task_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"commandType": "{{ commandType }}"
}'
;
```
</TabItem>
</Tabs>
