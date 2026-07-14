--- 
title: pipeline_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_runs
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>pipeline_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.pipeline_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="query_by_factory"
    values={[
        { label: 'query_by_factory', value: 'query_by_factory' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="query_by_factory">

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
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token for getting the next page of results, if any remaining results exist, null otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>List of pipeline runs. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="runDimensions" /></td>
    <td><code>object</code></td>
    <td>Run dimensions emitted by Pipeline run.</td>
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
    <td>The status of a pipeline run. Possible values: Queued, InProgress, Succeeded, Failed, Canceling, Cancelled.</td>
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
    <td><a href="#query_by_factory"><CopyableCode code="query_by_factory" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Query pipeline runs in the factory based on input filter conditions.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a pipeline run by its run ID.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The pipeline run identifier. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="query_by_factory"
    values={[
        { label: 'query_by_factory', value: 'query_by_factory' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="query_by_factory">

Query pipeline runs in the factory based on input filter conditions.

```sql
SELECT
continuationToken,
value
FROM azure.data_factory.pipeline_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a pipeline run by its run ID.

```sql
SELECT
durationInMs,
invokedBy,
isLatest,
lastUpdated,
message,
parameters,
pipelineName,
runDimensions,
runEnd,
runGroupId,
runId,
runStart,
status
FROM azure.data_factory.pipeline_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND run_id = '{{ run_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancel a pipeline run by its run ID.

```sql
EXEC azure.data_factory.pipeline_runs.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@isRecursive={{ isRecursive }}
;
```
</TabItem>
</Tabs>
