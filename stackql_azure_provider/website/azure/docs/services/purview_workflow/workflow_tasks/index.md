--- 
title: workflow_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_tasks
  - purview_workflow
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

Creates, updates, deletes, gets or lists a <code>workflow_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workflow_tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_workflow.workflow_tasks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-viewMode"><code>viewMode</code></a>, <a href="#parameter-workflowIds"><code>workflowIds</code></a>, <a href="#parameter-timeWindow"><code>timeWindow</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-taskTypes"><code>taskTypes</code></a>, <a href="#parameter-taskStatuses"><code>taskStatuses</code></a>, <a href="#parameter-requestors"><code>requestors</code></a>, <a href="#parameter-assignees"><code>assignees</code></a>, <a href="#parameter-workflowNameKeyword"><code>workflowNameKeyword</code></a></td>
    <td>Get all workflow tasks.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-assignees">
    <td><CopyableCode code="assignees" /></td>
    <td><code>array</code></td>
    <td>Assignees' ids to filter. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>The key word which used to sort the results. Known values are: "status desc", "status asc", "requestor desc", "requestor asc", "startTime desc", "startTime asc", "createdTime desc", and "createdTime asc". Default value is None.</td>
</tr>
<tr id="parameter-requestors">
    <td><CopyableCode code="requestors" /></td>
    <td><code>array</code></td>
    <td>Requestors' ids to filter. Default value is None.</td>
</tr>
<tr id="parameter-taskStatuses">
    <td><CopyableCode code="taskStatuses" /></td>
    <td><code>array</code></td>
    <td>Filter workflow tasks by status. Default value is None.</td>
</tr>
<tr id="parameter-taskTypes">
    <td><CopyableCode code="taskTypes" /></td>
    <td><code>array</code></td>
    <td>Filter items by workflow task type. Default value is None.</td>
</tr>
<tr id="parameter-timeWindow">
    <td><CopyableCode code="timeWindow" /></td>
    <td><code>string</code></td>
    <td>Time window of filtering items. Known values are: "1d", "7d", "30d", and "90d". Default value is None.</td>
</tr>
<tr id="parameter-viewMode">
    <td><CopyableCode code="viewMode" /></td>
    <td><code>string</code></td>
    <td>To filter user's sent, received or history workflow tasks. Default value is None.</td>
</tr>
<tr id="parameter-workflowIds">
    <td><CopyableCode code="workflowIds" /></td>
    <td><code>array</code></td>
    <td>Filter items by workflow id list. Default value is None.</td>
</tr>
<tr id="parameter-workflowNameKeyword">
    <td><CopyableCode code="workflowNameKeyword" /></td>
    <td><code>string</code></td>
    <td>The key word which could used to filter workflow item with related workflow. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

Get all workflow tasks.

```sql
EXEC azure.purview_workflow.workflow_tasks.list_raw 
@endpoint='{{ endpoint }}' --required, 
@viewMode='{{ viewMode }}', 
@workflowIds='{{ workflowIds }}', 
@timeWindow='{{ timeWindow }}', 
@maxpagesize='{{ maxpagesize }}', 
@orderby='{{ orderby }}', 
@taskTypes='{{ taskTypes }}', 
@taskStatuses='{{ taskStatuses }}', 
@requestors='{{ requestors }}', 
@assignees='{{ assignees }}', 
@workflowNameKeyword='{{ workflowNameKeyword }}'
;
```
</TabItem>
</Tabs>
