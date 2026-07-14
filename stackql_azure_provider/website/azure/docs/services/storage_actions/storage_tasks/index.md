--- 
title: storage_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_tasks
  - storage_actions
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

Creates, updates, deletes, gets or lists a <code>storage_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_actions.storage_tasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The storage task action that is executed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date and time of the storage task in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text that describes the purpose of the storage task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Storage Task is enabled when set to true and disabled when set to false. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identity of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage task. Known values are: "ValidateSubscriptionQuotaBegin", "ValidateSubscriptionQuotaEnd", "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (ValidateSubscriptionQuotaBegin, ValidateSubscriptionQuotaEnd, Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
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
    <td><CopyableCode code="taskVersion" /></td>
    <td><code>integer</code></td>
    <td>Storage task version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The storage task action that is executed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date and time of the storage task in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text that describes the purpose of the storage task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Storage Task is enabled when set to true and disabled when set to false. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identity of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage task. Known values are: "ValidateSubscriptionQuotaBegin", "ValidateSubscriptionQuotaEnd", "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (ValidateSubscriptionQuotaBegin, ValidateSubscriptionQuotaEnd, Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
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
    <td><CopyableCode code="taskVersion" /></td>
    <td><code>integer</code></td>
    <td>Storage task version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The storage task action that is executed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date and time of the storage task in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text that describes the purpose of the storage task. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Storage Task is enabled when set to true and disabled when set to false. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identity of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Represents the provisioning state of the storage task. Known values are: "ValidateSubscriptionQuotaBegin", "ValidateSubscriptionQuotaEnd", "Accepted", "Creating", "Succeeded", "Deleting", "Canceled", and "Failed". (ValidateSubscriptionQuotaBegin, ValidateSubscriptionQuotaEnd, Accepted, Creating, Succeeded, Deleting, Canceled, Failed)</td>
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
    <td><CopyableCode code="taskVersion" /></td>
    <td><code>integer</code></td>
    <td>Storage task version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_task_name"><code>storage_task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the storage task properties.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the storage tasks available under the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the storage tasks available under the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_task_name"><code>storage_task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-identity"><code>identity</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Asynchronously creates a new storage task resource with the specified parameters. If a storage task is already created and a subsequent create request is issued with different properties, the storage task properties will be updated. If a storage task is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_task_name"><code>storage_task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update storage task properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_task_name"><code>storage_task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the storage task resource.</td>
</tr>
<tr>
    <td><a href="#preview_actions"><CopyableCode code="preview_actions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Runs the input conditions against input object metadata properties and designates matched objects in response.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_task_name">
    <td><CopyableCode code="storage_task_name" /></td>
    <td><code>string</code></td>
    <td>The name of the storage task within the specified resource group. Storage task names must be between 3 and 18 characters in length and use numbers and lower-case letters only. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get the storage task properties.

```sql
SELECT
id,
name,
action,
creationTimeInUtc,
description,
enabled,
identity,
location,
provisioningState,
systemData,
tags,
taskVersion,
type
FROM azure.storage_actions.storage_tasks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_task_name = '{{ storage_task_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the storage tasks available under the given resource group.

```sql
SELECT
id,
name,
action,
creationTimeInUtc,
description,
enabled,
identity,
location,
provisioningState,
systemData,
tags,
taskVersion,
type
FROM azure.storage_actions.storage_tasks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all the storage tasks available under the subscription.

```sql
SELECT
id,
name,
action,
creationTimeInUtc,
description,
enabled,
identity,
location,
provisioningState,
systemData,
tags,
taskVersion,
type
FROM azure.storage_actions.storage_tasks
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Asynchronously creates a new storage task resource with the specified parameters. If a storage task is already created and a subsequent create request is issued with different properties, the storage task properties will be updated. If a storage task is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.

```sql
INSERT INTO azure.storage_actions.storage_tasks (
tags,
location,
identity,
properties,
resource_group_name,
storage_task_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ identity }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ storage_task_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: storage_tasks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the storage_tasks resource.
    - name: storage_task_name
      value: "{{ storage_task_name }}"
      description: Required parameter for the storage_tasks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the storage_tasks resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: identity
      description: |
        The managed service identity of the resource. Required.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      description: |
        Properties of the storage task. Required.
      value:
        taskVersion: {{ taskVersion }}
        enabled: {{ enabled }}
        description: "{{ description }}"
        action:
          if:
            condition: "{{ condition }}"
            operations:
              - name: "{{ name }}"
                parameters: "{{ parameters }}"
                onSuccess: "{{ onSuccess }}"
                onFailure: "{{ onFailure }}"
          else:
            operations:
              - name: "{{ name }}"
                parameters: "{{ parameters }}"
                onSuccess: "{{ onSuccess }}"
                onFailure: "{{ onFailure }}"
        provisioningState: "{{ provisioningState }}"
        creationTimeInUtc: "{{ creationTimeInUtc }}"
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

Update storage task properties.

```sql
UPDATE azure.storage_actions.storage_tasks
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_task_name = '{{ storage_task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
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

Delete the storage task resource.

```sql
DELETE FROM azure.storage_actions.storage_tasks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_task_name = '{{ storage_task_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="preview_actions"
    values={[
        { label: 'preview_actions', value: 'preview_actions' }
    ]}
>
<TabItem value="preview_actions">

Runs the input conditions against input object metadata properties and designates matched objects in response.

```sql
EXEC azure.storage_actions.storage_tasks.preview_actions 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
