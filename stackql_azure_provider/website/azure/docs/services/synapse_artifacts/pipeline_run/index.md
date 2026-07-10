--- 
title: pipeline_run
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_run
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>pipeline_run</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline_run" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.pipeline_run" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_pipeline_run"
    values={[
        { label: 'get_pipeline_run', value: 'get_pipeline_run' }
    ]}
>
<TabItem value="get_pipeline_run">

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
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="durationInMs" /></td>
    <td><code>integer</code></td>
    <td>The duration of a pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="invokedBy" /></td>
    <td><code>object</code></td>
    <td>Entity that started the pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="isLatest" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the recovered pipeline run is the latest in its group.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last updated timestamp for the pipeline run event in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The message from a pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The full or partial list of parameter name, value pair used in the pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="pipelineName" /></td>
    <td><code>string</code></td>
    <td>The pipeline name.</td>
</tr>
<tr>
    <td><CopyableCode code="runEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of a pipeline run in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="runGroupId" /></td>
    <td><code>string</code></td>
    <td>Identifier that correlates all the recovery runs of a pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="runId" /></td>
    <td><code>string</code></td>
    <td>Identifier of a run.</td>
</tr>
<tr>
    <td><CopyableCode code="runStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of a pipeline run in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of a pipeline run.</td>
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
    <td><a href="#get_pipeline_run"><CopyableCode code="get_pipeline_run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a pipeline run by its run ID.</td>
</tr>
<tr>
    <td><a href="#query_pipeline_runs_by_workspace"><CopyableCode code="query_pipeline_runs_by_workspace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-lastUpdatedAfter"><code>lastUpdatedAfter</code></a>, <a href="#parameter-lastUpdatedBefore"><code>lastUpdatedBefore</code></a></td>
    <td></td>
    <td>Query pipeline runs in the workspace based on input filter conditions.</td>
</tr>
<tr>
    <td><a href="#query_activity_runs"><CopyableCode code="query_activity_runs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-lastUpdatedAfter"><code>lastUpdatedAfter</code></a>, <a href="#parameter-lastUpdatedBefore"><code>lastUpdatedBefore</code></a></td>
    <td></td>
    <td>Query activity runs based on input filter conditions.</td>
</tr>
<tr>
    <td><a href="#cancel_pipeline_run"><CopyableCode code="cancel_pipeline_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-isRecursive"><code>isRecursive</code></a></td>
    <td>Cancel a pipeline run by its run ID.</td>
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
<tr id="parameter-pipeline_name">
    <td><CopyableCode code="pipeline_name" /></td>
    <td><code>string</code></td>
    <td>The pipeline name. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The pipeline run identifier. Required.</td>
</tr>
<tr id="parameter-isRecursive">
    <td><CopyableCode code="isRecursive" /></td>
    <td><code>boolean</code></td>
    <td>If true, cancel all the Child pipelines that are triggered by the current pipeline. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_pipeline_run"
    values={[
        { label: 'get_pipeline_run', value: 'get_pipeline_run' }
    ]}
>
<TabItem value="get_pipeline_run">

Get a pipeline run by its run ID.

```sql
SELECT
,
durationInMs,
invokedBy,
isLatest,
lastUpdated,
message,
parameters,
pipelineName,
runEnd,
runGroupId,
runId,
runStart,
status
FROM azure.synapse_artifacts.pipeline_run
WHERE run_id = '{{ run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="query_pipeline_runs_by_workspace"
    values={[
        { label: 'query_pipeline_runs_by_workspace', value: 'query_pipeline_runs_by_workspace' },
        { label: 'query_activity_runs', value: 'query_activity_runs' },
        { label: 'cancel_pipeline_run', value: 'cancel_pipeline_run' }
    ]}
>
<TabItem value="query_pipeline_runs_by_workspace">

Query pipeline runs in the workspace based on input filter conditions.

```sql
EXEC azure.synapse_artifacts.pipeline_run.query_pipeline_runs_by_workspace 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"continuationToken": "{{ continuationToken }}", 
"lastUpdatedAfter": "{{ lastUpdatedAfter }}", 
"lastUpdatedBefore": "{{ lastUpdatedBefore }}", 
"filters": "{{ filters }}", 
"orderBy": "{{ orderBy }}"
}'
;
```
</TabItem>
<TabItem value="query_activity_runs">

Query activity runs based on input filter conditions.

```sql
EXEC azure.synapse_artifacts.pipeline_run.query_activity_runs 
@pipeline_name='{{ pipeline_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"continuationToken": "{{ continuationToken }}", 
"lastUpdatedAfter": "{{ lastUpdatedAfter }}", 
"lastUpdatedBefore": "{{ lastUpdatedBefore }}", 
"filters": "{{ filters }}", 
"orderBy": "{{ orderBy }}"
}'
;
```
</TabItem>
<TabItem value="cancel_pipeline_run">

Cancel a pipeline run by its run ID.

```sql
EXEC azure.synapse_artifacts.pipeline_run.cancel_pipeline_run 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@isRecursive={{ isRecursive }}
;
```
</TabItem>
</Tabs>
