--- 
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - ai_discovery
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_discovery.tasks" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedTo" /></td>
    <td><code>object</code></td>
    <td>Application or user assigned to this task.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>array</code></td>
    <td>Comments or notes about the task.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who created this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>Type of entity that created the resource (User, Application, System, or custom type). Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOn" /></td>
    <td><code>array</code></td>
    <td>IDs of tasks that must complete before this task can be executed.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="executionHistory" /></td>
    <td><code>array</code></td>
    <td>History of execution events for this task.</td>
</tr>
<tr>
    <td><CopyableCode code="investigationId" /></td>
    <td><code>string</code></td>
    <td>The investigation identifier associated with the task.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who updated this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who updated this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="parentId" /></td>
    <td><code>string</code></td>
    <td>ID of the parent task if this is a subtask.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the task. Known values are: "Low", "Medium", and "High". (Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="relatedTo" /></td>
    <td><code>array</code></td>
    <td>IDs of tasks that are related to this task.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the task. Known values are: "New", "OnHold", "Complete", "Removed", "FlaggedHuman", "FlaggedAi", "Executing", "ExecutionDone", "Stale", "Failed", and "Incomplete". (New, OnHold, Complete, Removed, FlaggedHuman, FlaggedAi, Executing, ExecutionDone, Stale, Failed, Incomplete)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAssetIds" /></td>
    <td><code>array</code></td>
    <td>List of storage assets related to the task.</td>
</tr>
<tr>
    <td><CopyableCode code="taskResult" /></td>
    <td><code>object</code></td>
    <td>Task execution result with text and storage assets.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="validationRequirements" /></td>
    <td><code>array</code></td>
    <td>Array of validation requirements for the task.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedTo" /></td>
    <td><code>object</code></td>
    <td>Application or user assigned to this task.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>array</code></td>
    <td>Comments or notes about the task.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who created this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>Type of entity that created the resource (User, Application, System, or custom type). Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOn" /></td>
    <td><code>array</code></td>
    <td>IDs of tasks that must complete before this task can be executed.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="executionHistory" /></td>
    <td><code>array</code></td>
    <td>History of execution events for this task.</td>
</tr>
<tr>
    <td><CopyableCode code="investigationId" /></td>
    <td><code>string</code></td>
    <td>The investigation identifier associated with the task.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who updated this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who updated this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="parentId" /></td>
    <td><code>string</code></td>
    <td>ID of the parent task if this is a subtask.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the task. Known values are: "Low", "Medium", and "High". (Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="relatedTo" /></td>
    <td><code>array</code></td>
    <td>IDs of tasks that are related to this task.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the task. Known values are: "New", "OnHold", "Complete", "Removed", "FlaggedHuman", "FlaggedAi", "Executing", "ExecutionDone", "Stale", "Failed", and "Incomplete". (New, OnHold, Complete, Removed, FlaggedHuman, FlaggedAi, Executing, ExecutionDone, Stale, Failed, Incomplete)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAssetIds" /></td>
    <td><code>array</code></td>
    <td>List of storage assets related to the task.</td>
</tr>
<tr>
    <td><CopyableCode code="taskResult" /></td>
    <td><code>object</code></td>
    <td>Task execution result with text and storage assets.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the task.</td>
</tr>
<tr>
    <td><CopyableCode code="validationRequirements" /></td>
    <td><code>array</code></td>
    <td>Array of validation requirements for the task.</td>
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
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a task by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a></td>
    <td>List tasks with optional OData filters.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new task.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Patch (partial update) a task (e.g. status, description, validation requirements, dependencies, result).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a task by ID.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Start execution of a task.</td>
</tr>
<tr>
    <td><a href="#add_comment"><CopyableCode code="add_comment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-createdBy"><code>createdBy</code></a>, <a href="#parameter-createdByType"><code>createdByType</code></a>, <a href="#parameter-text"><code>text</code></a></td>
    <td></td>
    <td>Add a comment to a task.</td>
</tr>
<tr>
    <td><a href="#add_execution_history"><CopyableCode code="add_execution_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-task_name"><code>task_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-createdAt"><code>createdAt</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-createdBy"><code>createdBy</code></a>, <a href="#parameter-createdByType"><code>createdByType</code></a></td>
    <td></td>
    <td>Add an execution history entry to a task.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-investigation_name">
    <td><CopyableCode code="investigation_name" /></td>
    <td><code>string</code></td>
    <td>The investigation name. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The project name. Required.</td>
</tr>
<tr id="parameter-task_name">
    <td><CopyableCode code="task_name" /></td>
    <td><code>string</code></td>
    <td>The task name. Required.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Supported fields: investigationId, status, createdByType, priority, createdAt, lastModifiedAt. Example: status eq 'new' or status eq 'executing'. Default value is None.</td>
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

Get a task by ID.

```sql
SELECT
name,
assignedTo,
comments,
createdAt,
createdBy,
createdByType,
dependsOn,
description,
executionHistory,
investigationId,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
parentId,
priority,
relatedTo,
status,
storageAssetIds,
taskResult,
title,
validationRequirements
FROM azure.ai_discovery.tasks
WHERE project_name = '{{ project_name }}' -- required
AND investigation_name = '{{ investigation_name }}' -- required
AND task_name = '{{ task_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List tasks with optional OData filters.

```sql
SELECT
name,
assignedTo,
comments,
createdAt,
createdBy,
createdByType,
dependsOn,
description,
executionHistory,
investigationId,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
parentId,
priority,
relatedTo,
status,
storageAssetIds,
taskResult,
title,
validationRequirements
FROM azure.ai_discovery.tasks
WHERE project_name = '{{ project_name }}' -- required
AND investigation_name = '{{ investigation_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND filter = '{{ filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new task.

```sql
INSERT INTO azure.ai_discovery.tasks (
title,
priority,
description,
validationRequirements,
parentId,
dependsOn,
relatedTo,
assignedTo,
comments,
status,
createdByType,
investigationId,
taskResult,
storageAssetIds,
project_name,
investigation_name,
endpoint
)
SELECT 
'{{ title }}',
'{{ priority }}',
'{{ description }}',
'{{ validationRequirements }}',
'{{ parentId }}',
'{{ dependsOn }}',
'{{ relatedTo }}',
'{{ assignedTo }}',
'{{ comments }}',
'{{ status }}',
'{{ createdByType }}',
'{{ investigationId }}',
'{{ taskResult }}',
'{{ storageAssetIds }}',
'{{ project_name }}',
'{{ investigation_name }}',
'{{ endpoint }}'
RETURNING
name,
assignedTo,
comments,
createdAt,
createdBy,
createdByType,
dependsOn,
description,
executionHistory,
investigationId,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
parentId,
priority,
relatedTo,
status,
storageAssetIds,
taskResult,
title,
validationRequirements
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tasks
  props:
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the tasks resource.
    - name: investigation_name
      value: "{{ investigation_name }}"
      description: Required parameter for the tasks resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the tasks resource.
    - name: title
      value: "{{ title }}"
      description: |
        The title of the task.
    - name: priority
      value: "{{ priority }}"
      description: |
        The priority of the task. Known values are: "Low", "Medium", and "High".
      valid_values: ['Low', 'Medium', 'High']
    - name: description
      value: "{{ description }}"
      description: |
        The description of the task.
    - name: validationRequirements
      value:
        - "{{ validationRequirements }}"
      description: |
        Array of validation requirements for the task.
    - name: parentId
      value: "{{ parentId }}"
      description: |
        ID of the parent task if this is a subtask.
    - name: dependsOn
      value:
        - "{{ dependsOn }}"
      description: |
        IDs of tasks that must complete before this task can be executed.
    - name: relatedTo
      value:
        - "{{ relatedTo }}"
      description: |
        IDs of tasks that are related to this task.
    - name: assignedTo
      description: |
        Application or user assigned to this task.
      value:
        id: "{{ id }}"
        type: "{{ type }}"
    - name: comments
      description: |
        Comments or notes about the task.
      value:
        - timestamp: "{{ timestamp }}"
          createdBy: "{{ createdBy }}"
          createdByType: "{{ createdByType }}"
          text: "{{ text }}"
    - name: status
      value: "{{ status }}"
      description: |
        The current status of the task. Known values are: "New", "OnHold", "Complete", "Removed", "FlaggedHuman", "FlaggedAi", "Executing", "ExecutionDone", "Stale", "Failed", and "Incomplete".
      valid_values: ['New', 'OnHold', 'Complete', 'Removed', 'FlaggedHuman', 'FlaggedAi', 'Executing', 'ExecutionDone', 'Stale', 'Failed', 'Incomplete']
    - name: createdByType
      value: "{{ createdByType }}"
      description: |
        Type of entity that created the resource (User, Application, System, or custom type). Known values are: "User", "Application", and "System".
      valid_values: ['User', 'Application', 'System']
    - name: investigationId
      value: "{{ investigationId }}"
      description: |
        The investigation identifier associated with the task.
    - name: taskResult
      description: |
        Task execution result with text and storage assets.
      value:
        text: "{{ text }}"
        storageAssetIds:
          - "{{ storageAssetIds }}"
    - name: storageAssetIds
      value:
        - "{{ storageAssetIds }}"
      description: |
        List of storage assets related to the task.
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

Patch (partial update) a task (e.g. status, description, validation requirements, dependencies, result).

```sql
UPDATE azure.ai_discovery.tasks
SET 
title = '{{ title }}',
priority = '{{ priority }}',
description = '{{ description }}',
validationRequirements = '{{ validationRequirements }}',
parentId = '{{ parentId }}',
dependsOn = '{{ dependsOn }}',
relatedTo = '{{ relatedTo }}',
assignedTo = '{{ assignedTo }}',
comments = '{{ comments }}',
status = '{{ status }}',
createdByType = '{{ createdByType }}',
investigationId = '{{ investigationId }}',
taskResult = '{{ taskResult }}',
storageAssetIds = '{{ storageAssetIds }}'
WHERE 
project_name = '{{ project_name }}' --required
AND investigation_name = '{{ investigation_name }}' --required
AND task_name = '{{ task_name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
name,
assignedTo,
comments,
createdAt,
createdBy,
createdByType,
dependsOn,
description,
executionHistory,
investigationId,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
parentId,
priority,
relatedTo,
status,
storageAssetIds,
taskResult,
title,
validationRequirements;
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

Delete a task by ID.

```sql
DELETE FROM azure.ai_discovery.tasks
WHERE project_name = '{{ project_name }}' --required
AND investigation_name = '{{ investigation_name }}' --required
AND task_name = '{{ task_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'add_comment', value: 'add_comment' },
        { label: 'add_execution_history', value: 'add_execution_history' }
    ]}
>
<TabItem value="start">

Start execution of a task.

```sql
EXEC azure.ai_discovery.tasks.start 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@task_name='{{ task_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"assignee": "{{ assignee }}"
}'
;
```
</TabItem>
<TabItem value="add_comment">

Add a comment to a task.

```sql
EXEC azure.ai_discovery.tasks.add_comment 
@task_name='{{ task_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"timestamp": "{{ timestamp }}", 
"createdBy": "{{ createdBy }}", 
"createdByType": "{{ createdByType }}", 
"text": "{{ text }}"
}'
;
```
</TabItem>
<TabItem value="add_execution_history">

Add an execution history entry to a task.

```sql
EXEC azure.ai_discovery.tasks.add_execution_history 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@task_name='{{ task_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"createdAt": "{{ createdAt }}", 
"action": "{{ action }}", 
"createdBy": "{{ createdBy }}", 
"createdByType": "{{ createdByType }}", 
"summary": "{{ summary }}", 
"responseMessageText": "{{ responseMessageText }}", 
"responseMessageId": "{{ responseMessageId }}", 
"additionalDetails": "{{ additionalDetails }}"
}'
;
```
</TabItem>
</Tabs>
