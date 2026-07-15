--- 
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
  - ai_evaluation
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

Creates, updates, deletes, gets or lists an <code>insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="insights" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_evaluation.insights" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_insight"
    values={[
        { label: 'get_insight', value: 'get_insight' },
        { label: 'list_insights', value: 'list_insights' }
    ]}
>
<TabItem value="get_insight">

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
<TabItem value="list_insights">

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
    <td><a href="#get_insight"><CopyableCode code="get_insight" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeCoordinates"><code>includeCoordinates</code></a></td>
    <td>Get a specific insight by Id.</td>
</tr>
<tr>
    <td><a href="#list_insights"><CopyableCode code="list_insights" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-evalId"><code>evalId</code></a>, <a href="#parameter-runId"><code>runId</code></a>, <a href="#parameter-agentName"><code>agentName</code></a>, <a href="#parameter-includeCoordinates"><code>includeCoordinates</code></a></td>
    <td>List all insights in reverse chronological order (newest first).</td>
</tr>
<tr>
    <td><a href="#generate_insights"><CopyableCode code="generate_insights" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-displayName"><code>displayName</code></a>, <a href="#parameter-request"><code>request</code></a></td>
    <td></td>
    <td>Generate Insights.</td>
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
    defaultValue="get_insight"
    values={[
        { label: 'get_insight', value: 'get_insight' },
        { label: 'list_insights', value: 'list_insights' }
    ]}
>
<TabItem value="get_insight">

Get a specific insight by Id.

```sql
SELECT
id,
displayName,
metadata,
request,
result,
state
FROM azure.ai_evaluation.insights
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND includeCoordinates = '{{ includeCoordinates }}'
;
```
</TabItem>
<TabItem value="list_insights">

List all insights in reverse chronological order (newest first).

```sql
SELECT
id,
displayName,
metadata,
request,
result,
state
FROM azure.ai_evaluation.insights
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
    defaultValue="generate_insights"
    values={[
        { label: 'generate_insights', value: 'generate_insights' }
    ]}
>
<TabItem value="generate_insights">

Generate Insights.

```sql
EXEC azure.ai_evaluation.insights.generate_insights 
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
