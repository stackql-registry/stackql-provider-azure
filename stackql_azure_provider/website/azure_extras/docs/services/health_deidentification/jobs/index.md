--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - health_deidentification
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_deidentification.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_job"
    values={[
        { label: 'get_job', value: 'get_job' }
    ]}
>
<TabItem value="get_job">

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
    <td>The name of a job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the job was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="customizations" /></td>
    <td><code>object</code></td>
    <td>Customization parameters to override default service behaviors.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error when job fails in it's entirety.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the job was completed. If the job is canceled, this is the time when the job was canceled. If the job failed, this is the time when the job failed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>Operation to perform on the input documents. Known values are: "Redact", "Surrogate", "Tag", and "SurrogateOnly". (Redact, Surrogate, Tag, SurrogateOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceLocation" /></td>
    <td><code>object</code></td>
    <td>Storage location to perform the operation on. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the job was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of a job. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>object</code></td>
    <td>Summary of a job. Exists only when the job is completed.</td>
</tr>
<tr>
    <td><CopyableCode code="targetLocation" /></td>
    <td><code>object</code></td>
    <td>Target location to store output of operation. Required.</td>
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
    <td><a href="#get_job"><CopyableCode code="get_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a de-identification job. Resource read operation template.</td>
</tr>
<tr>
    <td><a href="#delete_job"><CopyableCode code="delete_job" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a de-identification job. Removes the record of the job from the service. Does not delete any documents.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of a job. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_job"
    values={[
        { label: 'get_job', value: 'get_job' }
    ]}
>
<TabItem value="get_job">

Get a de-identification job. Resource read operation template.

```sql
SELECT
name,
createdAt,
customizations,
error,
lastUpdatedAt,
operation,
sourceLocation,
startedAt,
status,
summary,
targetLocation
FROM azure_extras.health_deidentification.jobs
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_job"
    values={[
        { label: 'delete_job', value: 'delete_job' }
    ]}
>
<TabItem value="delete_job">

Delete a de-identification job. Removes the record of the job from the service. Does not delete any documents.

```sql
DELETE FROM azure_extras.health_deidentification.jobs
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
