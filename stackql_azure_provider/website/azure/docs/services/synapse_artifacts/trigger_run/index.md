--- 
title: trigger_run
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger_run
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

Creates, updates, deletes, gets or lists a <code>trigger_run</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="trigger_run" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.trigger_run" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="query_trigger_runs_by_workspace"
    values={[
        { label: 'query_trigger_runs_by_workspace', value: 'query_trigger_runs_by_workspace' }
    ]}
>
<TabItem value="query_trigger_runs_by_workspace">

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
    <td>List of trigger runs. Required.</td>
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
    <td><a href="#query_trigger_runs_by_workspace"><CopyableCode code="query_trigger_runs_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Query trigger runs.</td>
</tr>
<tr>
    <td><a href="#rerun_trigger_instance"><CopyableCode code="rerun_trigger_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Rerun single trigger instance by runId.</td>
</tr>
<tr>
    <td><a href="#cancel_trigger_instance"><CopyableCode code="cancel_trigger_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel single trigger instance by runId.</td>
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
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The pipeline run identifier. Required.</td>
</tr>
<tr id="parameter-trigger_name">
    <td><CopyableCode code="trigger_name" /></td>
    <td><code>string</code></td>
    <td>The trigger name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="query_trigger_runs_by_workspace"
    values={[
        { label: 'query_trigger_runs_by_workspace', value: 'query_trigger_runs_by_workspace' }
    ]}
>
<TabItem value="query_trigger_runs_by_workspace">

Query trigger runs.

```sql
SELECT
continuationToken,
value
FROM azure.synapse_artifacts.trigger_run
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rerun_trigger_instance"
    values={[
        { label: 'rerun_trigger_instance', value: 'rerun_trigger_instance' },
        { label: 'cancel_trigger_instance', value: 'cancel_trigger_instance' }
    ]}
>
<TabItem value="rerun_trigger_instance">

Rerun single trigger instance by runId.

```sql
EXEC azure.synapse_artifacts.trigger_run.rerun_trigger_instance 
@trigger_name='{{ trigger_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_trigger_instance">

Cancel single trigger instance by runId.

```sql
EXEC azure.synapse_artifacts.trigger_run.cancel_trigger_instance 
@trigger_name='{{ trigger_name }}' --required, 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
