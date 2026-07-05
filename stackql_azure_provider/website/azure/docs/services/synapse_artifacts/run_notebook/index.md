--- 
title: run_notebook
hide_title: false
hide_table_of_contents: false
keywords:
  - run_notebook
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

Creates, updates, deletes, gets or lists a <code>run_notebook</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="run_notebook" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.run_notebook" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_status"
    values={[
        { label: 'get_status', value: 'get_status' }
    ]}
>
<TabItem value="get_status">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Response message.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Result of run notebook.</td>
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
    <td><a href="#get_status"><CopyableCode code="get_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get RunNotebook Status for run id.</td>
</tr>
<tr>
    <td><a href="#create_run"><CopyableCode code="create_run" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Run notebook.</td>
</tr>
<tr>
    <td><a href="#get_snapshot"><CopyableCode code="get_snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get RunNotebook Snapshot for run id.</td>
</tr>
<tr>
    <td><a href="#cancel_run"><CopyableCode code="cancel_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel notebook run.</td>
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
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>Notebook run id. For Create Run, you can generate a new GUID and use it here. For other actions, this is the same ID used in Create Run. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_status"
    values={[
        { label: 'get_status', value: 'get_status' }
    ]}
>
<TabItem value="get_status">

Get RunNotebook Status for run id.

```sql
SELECT
message,
result
FROM azure.synapse_artifacts.run_notebook
WHERE run_id = '{{ run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_run"
    values={[
        { label: 'create_run', value: 'create_run' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_run">

Run notebook.

```sql
INSERT INTO azure.synapse_artifacts.run_notebook (
notebook,
sparkPool,
sessionOptions,
honorSessionTimeToLive,
parameters,
run_id,
endpoint
)
SELECT 
'{{ notebook }}',
'{{ sparkPool }}',
'{{ sessionOptions }}',
{{ honorSessionTimeToLive }},
'{{ parameters }}',
'{{ run_id }}',
'{{ endpoint }}'
RETURNING
message,
result
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: run_notebook
  props:
    - name: run_id
      value: "{{ run_id }}"
      description: Required parameter for the run_notebook resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the run_notebook resource.
    - name: notebook
      value: "{{ notebook }}"
      description: |
        Notebook name.
    - name: sparkPool
      value: "{{ sparkPool }}"
      description: |
        SparkPool name.
    - name: sessionOptions
      description: |
        Session properties.
      value:
        tags: "{{ tags }}"
        kind: "{{ kind }}"
        proxyUser: "{{ proxyUser }}"
        name: "{{ name }}"
        jars:
          - "{{ jars }}"
        pyFiles:
          - "{{ pyFiles }}"
        files:
          - "{{ files }}"
        archives:
          - "{{ archives }}"
        queue: "{{ queue }}"
        conf: "{{ conf }}"
        driverMemory: "{{ driverMemory }}"
        driverCores: {{ driverCores }}
        executorMemory: "{{ executorMemory }}"
        executorCores: {{ executorCores }}
        numExecutors: {{ numExecutors }}
        isQueueable: {{ isQueueable }}
        heartbeatTimeoutInSecond: {{ heartbeatTimeoutInSecond }}
    - name: honorSessionTimeToLive
      value: {{ honorSessionTimeToLive }}
      description: |
        Whether session should run till time to live after run completes.
    - name: parameters
      value: "{{ parameters }}"
      description: |
        Run notebook parameters.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_snapshot"
    values={[
        { label: 'get_snapshot', value: 'get_snapshot' },
        { label: 'cancel_run', value: 'cancel_run' }
    ]}
>
<TabItem value="get_snapshot">

Get RunNotebook Snapshot for run id.

```sql
EXEC azure.synapse_artifacts.run_notebook.get_snapshot 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_run">

Cancel notebook run.

```sql
EXEC azure.synapse_artifacts.run_notebook.cancel_run 
@run_id='{{ run_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
