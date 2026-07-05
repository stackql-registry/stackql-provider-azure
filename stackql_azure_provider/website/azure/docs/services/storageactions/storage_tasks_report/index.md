--- 
title: storage_tasks_report
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_tasks_report
  - storageactions
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

Creates, updates, deletes, gets or lists a <code>storage_tasks_report</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_tasks_report" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storageactions.storage_tasks_report" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="finishTime" /></td>
    <td><code>string</code></td>
    <td>End time of the run instance. Filter options such as startTime gt '2023-06-26T20:51:24.4494016Z' and other comparison operators can be used as described for DateTime properties in `https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#supported-comparison-operators `_.</td>
</tr>
<tr>
    <td><CopyableCode code="objectFailedCount" /></td>
    <td><code>string</code></td>
    <td>Total number of objects where task operation failed when was attempted. Filter options such as objectFailedCount eq 0 and other comparison operators can be used as described for Numerical properties in `https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#supported-comparison-operators `_.</td>
</tr>
<tr>
    <td><CopyableCode code="objectsOperatedOnCount" /></td>
    <td><code>string</code></td>
    <td>Total number of objects that meet the storage tasks condition and were operated upon. Filter options such as objectsOperatedOnCount ge 100 and other comparison operators can be used as described for Numerical properties in `https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#supported-comparison-operators `_.</td>
</tr>
<tr>
    <td><CopyableCode code="objectsSucceededCount" /></td>
    <td><code>string</code></td>
    <td>Total number of objects where task operation succeeded when was attempted.Filter options such as objectsSucceededCount gt 150 and other comparison operators can be used as described for Numerical properties in `https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#supported-comparison-operators `_.</td>
</tr>
<tr>
    <td><CopyableCode code="objectsTargetedCount" /></td>
    <td><code>string</code></td>
    <td>Total number of objects that meet the condition as defined in the storage task assignment execution context. Filter options such as objectsTargetedCount gt 50 and other comparison operators can be used as described for Numerical properties in `https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#supported-comparison-operators `_.</td>
</tr>
<tr>
    <td><CopyableCode code="runResult" /></td>
    <td><code>string</code></td>
    <td>Represents the overall result of the execution for the run instance. Known values are: "Succeeded" and "Failed". (Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="runStatusEnum" /></td>
    <td><code>string</code></td>
    <td>Represents the status of the execution. Known values are: "InProgress" and "Finished". (InProgress, Finished)</td>
</tr>
<tr>
    <td><CopyableCode code="runStatusError" /></td>
    <td><code>string</code></td>
    <td>Well known Azure Storage error code that represents the error encountered during execution of the run instance.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Start time of the run instance. Filter options such as startTime gt '2023-06-26T20:51:24.4494016Z' and other comparison operators can be used as described for DateTime properties in `https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#supported-comparison-operators `_.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Storage Account where this reported run executed.</td>
</tr>
<tr>
    <td><CopyableCode code="summaryReportPath" /></td>
    <td><code>string</code></td>
    <td>Full path to the verbose report stored in the reporting container as specified in the assignment execution context for the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="taskAssignmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Storage Task Assignment associated with this reported run.</td>
</tr>
<tr>
    <td><CopyableCode code="taskId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the Storage Task applied during this run.</td>
</tr>
<tr>
    <td><CopyableCode code="taskVersion" /></td>
    <td><code>string</code></td>
    <td>Storage Task Version.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_task_name"><code>storage_task_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$maxpagesize"><code>$maxpagesize</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Fetch the storage tasks run report summary for each assignment.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Optional. When specified, it can be used to query using reporting properties. Default value is None.</td>
</tr>
<tr id="parameter-$maxpagesize">
    <td><CopyableCode code="$maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Fetch the storage tasks run report summary for each assignment.

```sql
SELECT
id,
name,
finishTime,
objectFailedCount,
objectsOperatedOnCount,
objectsSucceededCount,
objectsTargetedCount,
runResult,
runStatusEnum,
runStatusError,
startTime,
storageAccountId,
summaryReportPath,
systemData,
taskAssignmentId,
taskId,
taskVersion,
type
FROM azure.storageactions.storage_tasks_report
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_task_name = '{{ storage_task_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $maxpagesize = '{{ $maxpagesize }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
