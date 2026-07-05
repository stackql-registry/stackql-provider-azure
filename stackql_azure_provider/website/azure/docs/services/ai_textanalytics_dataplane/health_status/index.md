--- 
title: health_status
hide_title: false
hide_table_of_contents: false
keywords:
  - health_status
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

Creates, updates, deletes, gets or lists a <code>health_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="health_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_textanalytics_dataplane.health_status" /></td></tr>
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
    <td><a href="#health_status"><CopyableCode code="health_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-showStats"><code>showStats</code></a></td>
    <td>Get healthcare analysis job status and results. Get details of the healthcare prediction job specified by the jobId.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Job ID. Required.</td>
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
    defaultValue="health_status"
    values={[
        { label: 'health_status', value: 'health_status' }
    ]}
>
<TabItem value="health_status">

Get healthcare analysis job status and results. Get details of the healthcare prediction job specified by the jobId.

```sql
EXEC azure.ai_textanalytics_dataplane.health_status.health_status 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@$top='{{ $top }}', 
@$skip='{{ $skip }}', 
@showStats={{ showStats }}
;
```
</TabItem>
</Tabs>
