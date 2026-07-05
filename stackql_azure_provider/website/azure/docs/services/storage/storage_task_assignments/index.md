--- 
title: storage_task_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_task_assignments
  - storage
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

Creates, updates, deletes, gets or lists a <code>storage_task_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_task_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.storage_task_assignments" /></td></tr>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text that describes the purpose of the storage task assignment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the storage task assignment is enabled or not. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="executionContext" /></td>
    <td><code>object</code></td>
    <td>The storage task assignment execution context. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage task assignment. Known values are: "ValidateSubscriptionQuotaBegin", "ValidateSubscriptionQuotaEnd", "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (ValidateSubscriptionQuotaBegin, ValidateSubscriptionQuotaEnd, Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="report" /></td>
    <td><code>object</code></td>
    <td>The storage task assignment report. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="runStatus" /></td>
    <td><code>object</code></td>
    <td>Run status of storage task assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskId" /></td>
    <td><code>string</code></td>
    <td>Id of the corresponding storage task. Required.</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text that describes the purpose of the storage task assignment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the storage task assignment is enabled or not. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="executionContext" /></td>
    <td><code>object</code></td>
    <td>The storage task assignment execution context. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage task assignment. Known values are: "ValidateSubscriptionQuotaBegin", "ValidateSubscriptionQuotaEnd", "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (ValidateSubscriptionQuotaBegin, ValidateSubscriptionQuotaEnd, Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="report" /></td>
    <td><code>object</code></td>
    <td>The storage task assignment report. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="runStatus" /></td>
    <td><code>object</code></td>
    <td>Run status of storage task assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskId" /></td>
    <td><code>string</code></td>
    <td>Id of the corresponding storage task. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-storage_task_assignment_name"><code>storage_task_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the storage task assignment properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>List all the storage task assignments in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-storage_task_assignment_name"><code>storage_task_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Asynchronously creates a new storage task assignment sub-resource with the specified parameters. If a storage task assignment is already created and a subsequent create request is issued with different properties, the storage task assignment properties will be updated. If a storage task assignment is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-storage_task_assignment_name"><code>storage_task_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update storage task assignment properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-storage_task_assignment_name"><code>storage_task_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the storage task assignment sub-resource.</td>
</tr>
<tr>
    <td><a href="#stop_assignment"><CopyableCode code="stop_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-storage_task_assignment_name"><code>storage_task_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops any active running storage action for the storage task assignment.</td>
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
    <td>The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_task_assignment_name">
    <td><CopyableCode code="storage_task_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the storage task assignment within the specified resource group. Storage task assignment names must be between 3 and 24 characters in length and use numbers and lower-case letters only. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Optional, specifies the maximum number of storage task assignment Ids to be included in the list response. Default value is None.</td>
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

Get the storage task assignment properties.

```sql
SELECT
id,
name,
description,
enabled,
executionContext,
provisioningState,
report,
runStatus,
systemData,
taskId,
type
FROM azure.storage.storage_task_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND storage_task_assignment_name = '{{ storage_task_assignment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all the storage task assignments in an account.

```sql
SELECT
id,
name,
description,
enabled,
executionContext,
provisioningState,
report,
runStatus,
systemData,
taskId,
type
FROM azure.storage.storage_task_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Asynchronously creates a new storage task assignment sub-resource with the specified parameters. If a storage task assignment is already created and a subsequent create request is issued with different properties, the storage task assignment properties will be updated. If a storage task assignment is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.

```sql
INSERT INTO azure.storage.storage_task_assignments (
properties,
resource_group_name,
account_name,
storage_task_assignment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ storage_task_assignment_name }}',
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
- name: storage_task_assignments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the storage_task_assignments resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the storage_task_assignments resource.
    - name: storage_task_assignment_name
      value: "{{ storage_task_assignment_name }}"
      description: Required parameter for the storage_task_assignments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the storage_task_assignments resource.
    - name: properties
      description: |
        Properties of the storage task assignment.
      value:
        taskId: "{{ taskId }}"
        enabled: {{ enabled }}
        description: "{{ description }}"
        executionContext:
          target:
            prefix:
              - "{{ prefix }}"
            excludePrefix:
              - "{{ excludePrefix }}"
          trigger:
            type: "{{ type }}"
            parameters:
              startFrom: "{{ startFrom }}"
              interval: {{ interval }}
              intervalUnit: "{{ intervalUnit }}"
              endBy: "{{ endBy }}"
              startOn: "{{ startOn }}"
        report:
          prefix: "{{ prefix }}"
        provisioningState: "{{ provisioningState }}"
        runStatus:
          taskAssignmentId: "{{ taskAssignmentId }}"
          storageAccountId: "{{ storageAccountId }}"
          startTime: "{{ startTime }}"
          finishTime: "{{ finishTime }}"
          objectsTargetedCount: "{{ objectsTargetedCount }}"
          objectsOperatedOnCount: "{{ objectsOperatedOnCount }}"
          objectFailedCount: "{{ objectFailedCount }}"
          objectsSucceededCount: "{{ objectsSucceededCount }}"
          runStatusError: "{{ runStatusError }}"
          runStatusEnum: "{{ runStatusEnum }}"
          summaryReportPath: "{{ summaryReportPath }}"
          taskId: "{{ taskId }}"
          taskVersion: "{{ taskVersion }}"
          runResult: "{{ runResult }}"
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

Update storage task assignment properties.

```sql
UPDATE azure.storage.storage_task_assignments
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND storage_task_assignment_name = '{{ storage_task_assignment_name }}' --required
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

Delete the storage task assignment sub-resource.

```sql
DELETE FROM azure.storage.storage_task_assignments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND storage_task_assignment_name = '{{ storage_task_assignment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop_assignment"
    values={[
        { label: 'stop_assignment', value: 'stop_assignment' }
    ]}
>
<TabItem value="stop_assignment">

Stops any active running storage action for the storage task assignment.

```sql
EXEC azure.storage.storage_task_assignments.stop_assignment 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@storage_task_assignment_name='{{ storage_task_assignment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
