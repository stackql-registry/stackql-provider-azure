--- 
title: tools
hide_title: false
hide_table_of_contents: false
keywords:
  - tools
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

Creates, updates, deletes, gets or lists a <code>tools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_discovery.tools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_run_status"
    values={[
        { label: 'get_run_status', value: 'get_run_status' },
        { label: 'get_operations', value: 'get_operations' }
    ]}
>
<TabItem value="get_run_status">

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
    <td>The unique ID of the operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error object that describes the error when status is "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>The result of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the operation. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_operations">

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
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>The link to the next page of items.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>The Operation items on this page. Required.</td>
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
    <td><a href="#get_run_status"><CopyableCode code="get_run_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-logCount"><code>logCount</code></a></td>
    <td>Used for to poll status of a Tool run.</td>
</tr>
<tr>
    <td><a href="#get_operations"><CopyableCode code="get_operations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-maxPageSize"><code>maxPageSize</code></a></td>
    <td>List tool runs.</td>
</tr>
<tr>
    <td><a href="#get_compute_usage"><CopyableCode code="get_compute_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Examine compute usage.</td>
</tr>
<tr>
    <td><a href="#run"><CopyableCode code="run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Run the specified tool in the context of the specified project.</td>
</tr>
<tr>
    <td><a href="#cancel_run"><CopyableCode code="cancel_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel an ongoing tool run.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>ID of the operation to cancel. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the associated Project. Required.</td>
</tr>
<tr id="parameter-logCount">
    <td><CopyableCode code="logCount" /></td>
    <td><code>integer</code></td>
    <td>Number of log lines to return (0-2500). Default value is None.</td>
</tr>
<tr id="parameter-maxPageSize">
    <td><CopyableCode code="maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>Bound the number of results that come back in one response (pagination control). Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>Skip results (pagination control). Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Query the top results (pagination control). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_run_status"
    values={[
        { label: 'get_run_status', value: 'get_run_status' },
        { label: 'get_operations', value: 'get_operations' }
    ]}
>
<TabItem value="get_run_status">

Used for to poll status of a Tool run.

```sql
SELECT
id,
error,
result,
status
FROM azure.ai_discovery.tools
WHERE project_name = '{{ project_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND logCount = '{{ logCount }}'
;
```
</TabItem>
<TabItem value="get_operations">

List tool runs.

```sql
SELECT
nextLink,
value
FROM azure.ai_discovery.tools
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND skip = '{{ skip }}'
AND top = '{{ top }}'
AND maxPageSize = '{{ maxPageSize }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_compute_usage"
    values={[
        { label: 'get_compute_usage', value: 'get_compute_usage' },
        { label: 'run', value: 'run' },
        { label: 'cancel_run', value: 'cancel_run' }
    ]}
>
<TabItem value="get_compute_usage">

Examine compute usage.

```sql
EXEC azure.ai_discovery.tools.get_compute_usage 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="run">

Run the specified tool in the context of the specified project.

```sql
EXEC azure.ai_discovery.tools.run 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_run">

Cancel an ongoing tool run.

```sql
EXEC azure.ai_discovery.tools.cancel_run 
@project_name='{{ project_name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
