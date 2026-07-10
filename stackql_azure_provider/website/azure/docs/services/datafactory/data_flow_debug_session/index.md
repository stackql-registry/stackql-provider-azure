--- 
title: data_flow_debug_session
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flow_debug_session
  - datafactory
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datafactory.data_flow_debug_session" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="query_by_factory"
    values={[
        { label: 'query_by_factory', value: 'query_by_factory' }
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
    <td><CopyableCode code="computeType" /></td>
    <td><code>string</code></td>
    <td>Compute type of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="coreCount" /></td>
    <td><code>integer</code></td>
    <td>Core count of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="dataFlowName" /></td>
    <td><code>string</code></td>
    <td>The name of the data flow.</td>
</tr>
<tr>
    <td><CopyableCode code="integrationRuntimeName" /></td>
    <td><code>string</code></td>
    <td>Attached integration runtime name of data flow debug session.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActivityTime" /></td>
    <td><code>string</code></td>
    <td>Last activity time of data flow debug session.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>Node count of the cluster. (deprecated property).</td>
</tr>
<tr>
    <td><CopyableCode code="sessionId" /></td>
    <td><code>string</code></td>
    <td>The ID of data flow debug session.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Start time of data flow debug session.</td>
</tr>
<tr>
    <td><CopyableCode code="timeToLiveInMinutes" /></td>
    <td><code>integer</code></td>
    <td>Compute type of the cluster.</td>
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
    <td>Query all active data flow debug sessions.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a data flow debug session.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a data flow debug session.</td>
</tr>
<tr>
    <td><a href="#add_data_flow"><CopyableCode code="add_data_flow" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add a data flow into debug session.</td>
</tr>
<tr>
    <td><a href="#execute_command"><CopyableCode code="execute_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>The factory name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="query_by_factory"
    values={[
        { label: 'query_by_factory', value: 'query_by_factory' }
    ]}
>
<TabItem value="query_by_factory">

Query all active data flow debug sessions.

```sql
SELECT
computeType,
coreCount,
dataFlowName,
integrationRuntimeName,
lastActivityTime,
nodeCount,
sessionId,
startTime,
timeToLiveInMinutes
FROM azure.datafactory.data_flow_debug_session
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a data flow debug session.

```sql
INSERT INTO azure.datafactory.data_flow_debug_session (
computeType,
coreCount,
timeToLive,
integrationRuntime,
resource_group_name,
factory_name,
subscription_id
)
SELECT 
'{{ computeType }}',
{{ coreCount }},
{{ timeToLive }},
'{{ integrationRuntime }}',
'{{ resource_group_name }}',
'{{ factory_name }}',
'{{ subscription_id }}'
RETURNING
sessionId,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_flow_debug_session
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_flow_debug_session resource.
    - name: factory_name
      value: "{{ factory_name }}"
      description: Required parameter for the data_flow_debug_session resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
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
          type: "{{ type }}"
          description: "{{ description }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a data flow debug session.

```sql
DELETE FROM azure.datafactory.data_flow_debug_session
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_data_flow"
    values={[
        { label: 'add_data_flow', value: 'add_data_flow' },
        { label: 'execute_command', value: 'execute_command' }
    ]}
>
<TabItem value="add_data_flow">

Add a data flow into debug session.

```sql
EXEC azure.datafactory.data_flow_debug_session.add_data_flow 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
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
EXEC azure.datafactory.data_flow_debug_session.execute_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
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
