--- 
title: kql_script
hide_title: false
hide_table_of_contents: false
keywords:
  - kql_script
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

Creates, updates, deletes, gets or lists a <code>kql_script</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kql_script" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.kql_script" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' }
    ]}
>
<TabItem value="get_by_name">

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
    <td>:vartype id: str</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>:vartype content: ~azure.synapse.artifacts.models.KqlScriptContent</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>:vartype type: str</td>
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
    <td><a href="#get_by_name"><CopyableCode code="get_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-kql_script_name"><code>kql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get KQL script by name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-kql_script_name"><code>kql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a KQL Script.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-kql_script_name"><code>kql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a KQL Script.</td>
</tr>
<tr>
    <td><a href="#delete_by_name"><CopyableCode code="delete_by_name" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-kql_script_name"><code>kql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete KQL script by name.</td>
</tr>
<tr>
    <td><a href="#rename"><CopyableCode code="rename" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-kql_script_name"><code>kql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Rename KQL script.</td>
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
<tr id="parameter-kql_script_name">
    <td><CopyableCode code="kql_script_name" /></td>
    <td><code>string</code></td>
    <td>KQL script name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' }
    ]}
>
<TabItem value="get_by_name">

Get KQL script by name.

```sql
SELECT
id,
name,
content,
type
FROM azure.synapse_artifacts.kql_script
WHERE kql_script_name = '{{ kql_script_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a KQL Script.

```sql
INSERT INTO azure.synapse_artifacts.kql_script (
id,
name,
type,
properties,
kql_script_name,
endpoint
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ type }}',
'{{ properties }}',
'{{ kql_script_name }}',
'{{ endpoint }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: kql_script
  props:
    - name: kql_script_name
      value: "{{ kql_script_name }}"
      description: Required parameter for the kql_script resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the kql_script resource.
    - name: id
      value: "{{ id }}"
      description: |
        :vartype id: str
    - name: name
      value: "{{ name }}"
      description: |
        :vartype name: str
    - name: type
      value: "{{ type }}"
      description: |
        :vartype type: str
    - name: properties
      description: |
        Properties of sql script.
      value:
        content:
          query: "{{ query }}"
          metadata:
            language: "{{ language }}"
          currentConnection:
            name: "{{ name }}"
            poolName: "{{ poolName }}"
            databaseName: "{{ databaseName }}"
            type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a KQL Script.

```sql
REPLACE azure.synapse_artifacts.kql_script
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
properties = '{{ properties }}'
WHERE 
kql_script_name = '{{ kql_script_name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_name"
    values={[
        { label: 'delete_by_name', value: 'delete_by_name' }
    ]}
>
<TabItem value="delete_by_name">

Delete KQL script by name.

```sql
DELETE FROM azure.synapse_artifacts.kql_script
WHERE kql_script_name = '{{ kql_script_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename"
    values={[
        { label: 'rename', value: 'rename' }
    ]}
>
<TabItem value="rename">

Rename KQL script.

```sql
EXEC azure.synapse_artifacts.kql_script.rename 
@kql_script_name='{{ kql_script_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
