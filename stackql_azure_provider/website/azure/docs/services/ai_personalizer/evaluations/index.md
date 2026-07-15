--- 
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - ai_personalizer
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

Creates, updates, deletes, gets or lists an <code>evaluations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="evaluations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_personalizer.evaluations" /></td></tr>
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
    <td><a href="#create_evaluation"><CopyableCode code="create_evaluation" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-evaluation_id"><code>evaluation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create Offline Evaluation. Submit a new Offline Evaluation job.</td>
</tr>
<tr>
    <td><a href="#delete_evaluation"><CopyableCode code="delete_evaluation" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-evaluation_id"><code>evaluation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Offline Evaluation. Delete the Offline Evaluation associated with the Id.</td>
</tr>
<tr>
    <td><a href="#list_evaluations"><CopyableCode code="list_evaluations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>All Offline Evaluations. List of all Offline Evaluations.</td>
</tr>
<tr>
    <td><a href="#get_evaluation"><CopyableCode code="get_evaluation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-evaluation_id"><code>evaluation_id</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-intervalInMinutes"><code>intervalInMinutes</code></a>, <a href="#parameter-window"><code>window</code></a></td>
    <td>Offline Evaluation. Get the Offline Evaluation associated with the Id.</td>
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
<tr id="parameter-endTime">
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End of aggregation time interval. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-evaluation_id">
    <td><CopyableCode code="evaluation_id" /></td>
    <td><code>string</code></td>
    <td>Id of the Offline Evaluation. Required.</td>
</tr>
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start of aggregation time interval. Required.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>An expression to filter the evaluations against evaluation metadata. Only evaluations where the expression evaluates to true are included in the response. Here is an example, metadata=evaluationType eq 'Manual'. Default value is None.</td>
</tr>
<tr id="parameter-intervalInMinutes">
    <td><CopyableCode code="intervalInMinutes" /></td>
    <td><code>integer</code></td>
    <td>"Time interval for aggregation of events in minutes. Allowed intervals: 5 minutes, 60 minutes, 360 minutes, 720 minutes and 1440 minutes. Defaults to 5 minutes. Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>An offset into the collection of the first resource to be returned. Defaults to 0. Default value is 0.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the collection. Defaults to maximum value of integer. Default value is None.</td>
</tr>
<tr id="parameter-window">
    <td><CopyableCode code="window" /></td>
    <td><code>string</code></td>
    <td>Rolling or Expanding time. Rolling compatible with 60 minutes, 360 minutes, 720 minutes and 1440 minutes intervals. Expanding compatible with 5 minute time interval only. Defaults to Expanding. Known values are: "Expanding" and "Rolling". Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_evaluation"
    values={[
        { label: 'create_evaluation', value: 'create_evaluation' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_evaluation">

Create Offline Evaluation. Submit a new Offline Evaluation job.

```sql
INSERT INTO azure.ai_personalizer.evaluations (
evaluation_id,
endpoint
)
SELECT 
'{{ evaluation_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: evaluations
  props:
    - name: evaluation_id
      value: "{{ evaluation_id }}"
      description: Required parameter for the evaluations resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the evaluations resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_evaluation"
    values={[
        { label: 'delete_evaluation', value: 'delete_evaluation' }
    ]}
>
<TabItem value="delete_evaluation">

Offline Evaluation. Delete the Offline Evaluation associated with the Id.

```sql
DELETE FROM azure.ai_personalizer.evaluations
WHERE evaluation_id = '{{ evaluation_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_evaluations"
    values={[
        { label: 'list_evaluations', value: 'list_evaluations' },
        { label: 'get_evaluation', value: 'get_evaluation' }
    ]}
>
<TabItem value="list_evaluations">

All Offline Evaluations. List of all Offline Evaluations.

```sql
EXEC azure.ai_personalizer.evaluations.list_evaluations 
@endpoint='{{ endpoint }}' --required, 
@filter='{{ filter }}', 
@top='{{ top }}', 
@skip='{{ skip }}'
;
```
</TabItem>
<TabItem value="get_evaluation">

Offline Evaluation. Get the Offline Evaluation associated with the Id.

```sql
EXEC azure.ai_personalizer.evaluations.get_evaluation 
@evaluation_id='{{ evaluation_id }}' --required, 
@startTime='{{ startTime }}' --required, 
@endTime='{{ endTime }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@intervalInMinutes='{{ intervalInMinutes }}', 
@window='{{ window }}'
;
```
</TabItem>
</Tabs>
