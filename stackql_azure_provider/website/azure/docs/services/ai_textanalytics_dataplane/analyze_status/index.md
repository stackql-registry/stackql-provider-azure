--- 
title: analyze_status
hide_title: false
hide_table_of_contents: false
keywords:
  - analyze_status
  - ai_textanalytics_dataplane
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

Creates, updates, deletes, gets or lists an <code>analyze_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyze_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_textanalytics_dataplane.analyze_status" /></td></tr>
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
    <td><a href="#analyze_status"><CopyableCode code="analyze_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-showStats"><code>showStats</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Get analysis status and results. Get the status of an analysis job. A job may consist of one or more tasks. Once all tasks are completed, the job will transition to the completed state and results will be available for each task.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Job ID for Analyze. Required.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>(Optional) Set the number of elements to offset in the response. When both $top and $skip are specified, $skip is applied first. Default value is 0.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>(Optional) Set the maximum number of results per task. When both $top and $skip are specified, $skip is applied first. Default value is 20.</td>
</tr>
<tr id="parameter-showStats">
    <td><CopyableCode code="showStats" /></td>
    <td><code>boolean</code></td>
    <td>(Optional) if set to true, response will contain request and document level statistics. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="analyze_status"
    values={[
        { label: 'analyze_status', value: 'analyze_status' }
    ]}
>
<TabItem value="analyze_status">

Get analysis status and results. Get the status of an analysis job. A job may consist of one or more tasks. Once all tasks are completed, the job will transition to the completed state and results will be available for each task.

```sql
EXEC azure.ai_textanalytics_dataplane.analyze_status.analyze_status 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@showStats={{ showStats }}, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}'
;
```
</TabItem>
</Tabs>
