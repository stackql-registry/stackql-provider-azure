--- 
title: hybrid_runbook_workers
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_workers
  - automation
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

Creates, updates, deletes, gets or lists a <code>hybrid_runbook_workers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="hybrid_runbook_workers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.hybrid_runbook_workers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_hybrid_runbook_worker_group', value: 'list_by_hybrid_runbook_worker_group' }
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
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the assigned machine IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSeenDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Heartbeat from the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="registeredDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the registration time of the worker machine.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager Id for a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="workerName" /></td>
    <td><code>string</code></td>
    <td>Name of the HybridWorker.</td>
</tr>
<tr>
    <td><CopyableCode code="workerType" /></td>
    <td><code>string</code></td>
    <td>Type of the HybridWorker. Known values are: "HybridV1" and "HybridV2". (HybridV1, HybridV2)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_hybrid_runbook_worker_group">

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
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the assigned machine IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSeenDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Heartbeat from the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="registeredDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the registration time of the worker machine.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager Id for a virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="workerName" /></td>
    <td><code>string</code></td>
    <td>Name of the HybridWorker.</td>
</tr>
<tr>
    <td><CopyableCode code="workerType" /></td>
    <td><code>string</code></td>
    <td>Type of the HybridWorker. Known values are: "HybridV1" and "HybridV2". (HybridV1, HybridV2)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-hybrid_runbook_worker_group_name"><code>hybrid_runbook_worker_group_name</code></a>, <a href="#parameter-hybrid_runbook_worker_id"><code>hybrid_runbook_worker_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a hybrid runbook worker.</td>
</tr>
<tr>
    <td><a href="#list_by_hybrid_runbook_worker_group"><CopyableCode code="list_by_hybrid_runbook_worker_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-hybrid_runbook_worker_group_name"><code>hybrid_runbook_worker_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieve a list of hybrid runbook workers.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-hybrid_runbook_worker_group_name"><code>hybrid_runbook_worker_group_name</code></a>, <a href="#parameter-hybrid_runbook_worker_id"><code>hybrid_runbook_worker_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a hybrid runbook worker.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-hybrid_runbook_worker_group_name"><code>hybrid_runbook_worker_group_name</code></a>, <a href="#parameter-hybrid_runbook_worker_id"><code>hybrid_runbook_worker_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a hybrid runbook worker.</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-hybrid_runbook_worker_group_name"><code>hybrid_runbook_worker_group_name</code></a>, <a href="#parameter-hybrid_runbook_worker_id"><code>hybrid_runbook_worker_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a hybrid runbook worker.</td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-hybrid_runbook_worker_group_name"><code>hybrid_runbook_worker_group_name</code></a>, <a href="#parameter-hybrid_runbook_worker_id"><code>hybrid_runbook_worker_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Move a hybrid worker to a different group.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-hybrid_runbook_worker_group_name">
    <td><CopyableCode code="hybrid_runbook_worker_group_name" /></td>
    <td><code>string</code></td>
    <td>The hybrid runbook worker group name. Required.</td>
</tr>
<tr id="parameter-hybrid_runbook_worker_id">
    <td><CopyableCode code="hybrid_runbook_worker_id" /></td>
    <td><code>string</code></td>
    <td>The hybrid runbook worker id. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_hybrid_runbook_worker_group', value: 'list_by_hybrid_runbook_worker_group' }
    ]}
>
<TabItem value="get">

Retrieve a hybrid runbook worker.

```sql
SELECT
id,
name,
ip,
lastSeenDateTime,
location,
registeredDateTime,
systemData,
tags,
type,
vmResourceId,
workerName,
workerType
FROM azure.automation.hybrid_runbook_workers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND hybrid_runbook_worker_group_name = '{{ hybrid_runbook_worker_group_name }}' -- required
AND hybrid_runbook_worker_id = '{{ hybrid_runbook_worker_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_hybrid_runbook_worker_group">

Retrieve a list of hybrid runbook workers.

```sql
SELECT
id,
name,
ip,
lastSeenDateTime,
location,
registeredDateTime,
systemData,
tags,
type,
vmResourceId,
workerName,
workerType
FROM azure.automation.hybrid_runbook_workers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND hybrid_runbook_worker_group_name = '{{ hybrid_runbook_worker_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create a hybrid runbook worker.

```sql
INSERT INTO azure.automation.hybrid_runbook_workers (
properties,
resource_group_name,
automation_account_name,
hybrid_runbook_worker_group_name,
hybrid_runbook_worker_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ hybrid_runbook_worker_group_name }}',
'{{ hybrid_runbook_worker_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: hybrid_runbook_workers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the hybrid_runbook_workers resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the hybrid_runbook_workers resource.
    - name: hybrid_runbook_worker_group_name
      value: "{{ hybrid_runbook_worker_group_name }}"
      description: Required parameter for the hybrid_runbook_workers resource.
    - name: hybrid_runbook_worker_id
      value: "{{ hybrid_runbook_worker_id }}"
      description: Required parameter for the hybrid_runbook_workers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the hybrid_runbook_workers resource.
    - name: properties
      description: |
        Gets or sets hybrid runbook worker group create or update properties.
      value:
        vmResourceId: "{{ vmResourceId }}"
`}</CodeBlock>

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

Delete a hybrid runbook worker.

```sql
DELETE FROM azure.automation.hybrid_runbook_workers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND hybrid_runbook_worker_group_name = '{{ hybrid_runbook_worker_group_name }}' --required
AND hybrid_runbook_worker_id = '{{ hybrid_runbook_worker_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' },
        { label: 'move', value: 'move' }
    ]}
>
<TabItem value="patch">

Update a hybrid runbook worker.

```sql
EXEC azure.automation.hybrid_runbook_workers.patch 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@hybrid_runbook_worker_group_name='{{ hybrid_runbook_worker_group_name }}' --required, 
@hybrid_runbook_worker_id='{{ hybrid_runbook_worker_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="move">

Move a hybrid worker to a different group.

```sql
EXEC azure.automation.hybrid_runbook_workers.move 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@hybrid_runbook_worker_group_name='{{ hybrid_runbook_worker_group_name }}' --required, 
@hybrid_runbook_worker_id='{{ hybrid_runbook_worker_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"hybridRunbookWorkerGroupName": "{{ hybridRunbookWorkerGroupName }}"
}'
;
```
</TabItem>
</Tabs>
