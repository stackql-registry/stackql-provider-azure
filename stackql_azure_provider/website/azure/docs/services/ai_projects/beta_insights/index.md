--- 
title: beta_insights
hide_title: false
hide_table_of_contents: false
keywords:
  - beta_insights
  - ai_projects
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

Creates, updates, deletes, gets or lists a <code>beta_insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="beta_insights" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.beta_insights" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>The unique identifier for the insights report. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name for the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the insights report. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>Request for the insights analysis. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>The result of the insights report.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the insights. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The unique identifier for the insights report. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name for the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the insights report. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>Request for the insights analysis. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>The result of the insights report.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the insights. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeCoordinates"><code>includeCoordinates</code></a></td>
    <td>Get an insight. Retrieves the specified insight report and its results.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-evalId"><code>evalId</code></a>, <a href="#parameter-runId"><code>runId</code></a>, <a href="#parameter-agentName"><code>agentName</code></a>, <a href="#parameter-includeCoordinates"><code>includeCoordinates</code></a></td>
    <td>List insights. Returns insights in reverse chronological order, with the most recent entries first.</td>
</tr>
<tr>
    <td><a href="#generate"><CopyableCode code="generate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-request"><code>request</code></a></td>
    <td></td>
    <td>Generate insights. Generates an insights report from the provided evaluation configuration.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the insights report. Required.</td>
</tr>
<tr id="parameter-agentName">
    <td><CopyableCode code="agentName" /></td>
    <td><code>string</code></td>
    <td>Filter by the agent name. Default value is None.</td>
</tr>
<tr id="parameter-evalId">
    <td><CopyableCode code="evalId" /></td>
    <td><code>string</code></td>
    <td>Filter by the evaluation ID. Default value is None.</td>
</tr>
<tr id="parameter-includeCoordinates">
    <td><CopyableCode code="includeCoordinates" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include coordinates for visualization in the response. Defaults to false. Default value is None.</td>
</tr>
<tr id="parameter-runId">
    <td><CopyableCode code="runId" /></td>
    <td><code>string</code></td>
    <td>Filter by the evaluation run ID. Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Filter by the type of analysis. Known values are: "EvaluationRunClusterInsight", "AgentClusterInsight", and "EvaluationComparison". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get an insight. Retrieves the specified insight report and its results.

```sql
SELECT
id,
displayName,
metadata,
request,
result,
state
FROM azure.ai_projects.beta_insights
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND includeCoordinates = '{{ includeCoordinates }}'
;
```
</TabItem>
<TabItem value="list">

List insights. Returns insights in reverse chronological order, with the most recent entries first.

```sql
SELECT
id,
displayName,
metadata,
request,
result,
state
FROM azure.ai_projects.beta_insights
WHERE endpoint = '{{ endpoint }}' -- required
AND type = '{{ type }}'
AND evalId = '{{ evalId }}'
AND runId = '{{ runId }}'
AND agentName = '{{ agentName }}'
AND includeCoordinates = '{{ includeCoordinates }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate"
    values={[
        { label: 'generate', value: 'generate' }
    ]}
>
<TabItem value="generate">

Generate insights. Generates an insights report from the provided evaluation configuration.

```sql
EXEC azure.ai_projects.beta_insights.generate 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"displayName": "{{ displayName }}", 
"request": "{{ request }}"
}'
;
```
</TabItem>
</Tabs>
