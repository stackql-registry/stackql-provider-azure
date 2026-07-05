--- 
title: data_flow_debug_session
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flow_debug_session
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

Creates, updates, deletes, gets or lists a <code>data_flow_debug_session</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_flow_debug_session" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.data_flow_debug_session" /></td></tr>
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
    <td><a href="#create_data_flow_debug_session"><CopyableCode code="create_data_flow_debug_session" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a data flow debug session.</td>
</tr>
<tr>
    <td><a href="#delete_data_flow_debug_session"><CopyableCode code="delete_data_flow_debug_session" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a data flow debug session.</td>
</tr>
<tr>
    <td><a href="#query_data_flow_debug_sessions_by_workspace"><CopyableCode code="query_data_flow_debug_sessions_by_workspace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Query all active data flow debug sessions.</td>
</tr>
<tr>
    <td><a href="#add_data_flow"><CopyableCode code="add_data_flow" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Add a data flow into debug session.</td>
</tr>
<tr>
    <td><a href="#execute_command"><CopyableCode code="execute_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Execute a data flow debug command.</td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_data_flow_debug_session"
    values={[
        { label: 'create_data_flow_debug_session', value: 'create_data_flow_debug_session' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_data_flow_debug_session">

Creates a data flow debug session.

```sql
INSERT INTO azure.synapse_artifacts.data_flow_debug_session (
computeType,
coreCount,
timeToLive,
integrationRuntime,
endpoint
)
SELECT 
'{{ computeType }}',
{{ coreCount }},
{{ timeToLive }},
'{{ integrationRuntime }}',
'{{ endpoint }}'
RETURNING
sessionId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_flow_debug_session
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the data_flow_debug_session resource.
    - name: computeType
      value: "{{ computeType }}"
      description: |
        Compute type of the cluster. The value will be overwritten by the same setting in integration runtime if provided.
    - name: coreCount
      value: {{ coreCount }}
      description: |
        Core count of the cluster. The value will be overwritten by the same setting in integration runtime if provided.
    - name: timeToLive
      value: {{ timeToLive }}
      description: |
        Time to live setting of the cluster in minutes.
    - name: integrationRuntime
      description: |
        Set to use integration runtime setting for data flow debug session.
      value:
        name: "{{ name }}"
        properties:
          : "{{  }}"
          type: "{{ type }}"
          description: "{{ description }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_data_flow_debug_session"
    values={[
        { label: 'delete_data_flow_debug_session', value: 'delete_data_flow_debug_session' }
    ]}
>
<TabItem value="delete_data_flow_debug_session">

Deletes a data flow debug session.

```sql
DELETE FROM azure.synapse_artifacts.data_flow_debug_session
WHERE endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="query_data_flow_debug_sessions_by_workspace"
    values={[
        { label: 'query_data_flow_debug_sessions_by_workspace', value: 'query_data_flow_debug_sessions_by_workspace' },
        { label: 'add_data_flow', value: 'add_data_flow' },
        { label: 'execute_command', value: 'execute_command' }
    ]}
>
<TabItem value="query_data_flow_debug_sessions_by_workspace">

Query all active data flow debug sessions.

```sql
EXEC azure.synapse_artifacts.data_flow_debug_session.query_data_flow_debug_sessions_by_workspace 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="add_data_flow">

Add a data flow into debug session.

```sql
EXEC azure.synapse_artifacts.data_flow_debug_session.add_data_flow 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"": "{{  }}", 
"sessionId": "{{ sessionId }}", 
"dataFlow": "{{ dataFlow }}", 
"dataFlows": "{{ dataFlows }}", 
"datasets": "{{ datasets }}", 
"linkedServices": "{{ linkedServices }}", 
"staging": "{{ staging }}", 
"debugSettings": "{{ debugSettings }}"
}'
;
```
</TabItem>
<TabItem value="execute_command">

Execute a data flow debug command.

```sql
EXEC azure.synapse_artifacts.data_flow_debug_session.execute_command 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"sessionId": "{{ sessionId }}", 
"command": "{{ command }}", 
"commandPayload": "{{ commandPayload }}"
}'
;
```
</TabItem>
</Tabs>
