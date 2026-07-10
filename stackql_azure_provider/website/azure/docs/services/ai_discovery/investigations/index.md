--- 
title: investigations
hide_title: false
hide_table_of_contents: false
keywords:
  - investigations
  - ai_discovery
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

Creates, updates, deletes, gets or lists an <code>investigations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="investigations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_discovery.investigations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_status"
    values={[
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_operation_status">

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
    <td>The unique ID of the operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error object that describes the error when status is "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>The result of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the operation. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The investigation name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who created this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who created this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The title.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who updated this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who updated this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The parent project name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Created", "Validated", and "Failed". (Created, Validated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The investigation name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who created this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who created this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The title.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who updated this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who updated this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The parent project name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Created", "Validated", and "Failed". (Created, Validated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags.</td>
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
    <td><a href="#get_operation_status"><CopyableCode code="get_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the status of a long-running operation.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a Investigation by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createdSince"><code>createdSince</code></a></td>
    <td>List Investigation resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Updates an Investigation.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Updates an Investigation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a Investigation.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates an Investigation.</td>
</tr>
<tr>
    <td><a href="#get_discovery_engine"><CopyableCode code="get_discovery_engine" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the discovery engine for an investigation.</td>
</tr>
<tr>
    <td><a href="#update_discovery_engine"><CopyableCode code="update_discovery_engine" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the discovery engine for an investigation. This will create the discovery engine if it does not already exist.</td>
</tr>
<tr>
    <td><a href="#get_discovery_engine_memory"><CopyableCode code="get_discovery_engine_memory" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-maxPageSize"><code>maxPageSize</code></a></td>
    <td>List discovery engine working memory entries for an investigation.</td>
</tr>
<tr>
    <td><a href="#start_discovery_engine"><CopyableCode code="start_discovery_engine" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Start the discovery engine for an investigation.</td>
</tr>
<tr>
    <td><a href="#stop_discovery_engine"><CopyableCode code="stop_discovery_engine" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-investigation_name"><code>investigation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stop the discovery engine for an investigation.</td>
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
<tr id="parameter-investigation_name">
    <td><CopyableCode code="investigation_name" /></td>
    <td><code>string</code></td>
    <td>The investigation name. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the operation. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The project name. Required.</td>
</tr>
<tr id="parameter-createdSince">
    <td><CopyableCode code="createdSince" /></td>
    <td><code>string (date-time)</code></td>
    <td>The oldest creation timestamp to keep. Default value is None.</td>
</tr>
<tr id="parameter-maxPageSize">
    <td><CopyableCode code="maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>Bound the number of results that come back in one response. Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>Skip results. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Query the top results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_operation_status"
    values={[
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_operation_status">

Get the status of a long-running operation.

```sql
SELECT
id,
error,
result,
status
FROM azure.ai_discovery.investigations
WHERE project_name = '{{ project_name }}' -- required
AND investigation_name = '{{ investigation_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Fetch a Investigation by name.

```sql
SELECT
name,
createdAt,
createdBy,
createdByType,
description,
displayName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName,
status,
tags
FROM azure.ai_discovery.investigations
WHERE project_name = '{{ project_name }}' -- required
AND investigation_name = '{{ investigation_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Investigation resources.

```sql
SELECT
name,
createdAt,
createdBy,
createdByType,
description,
displayName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName,
status,
tags
FROM azure.ai_discovery.investigations
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND createdSince = '{{ createdSince }}'
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

Updates an Investigation.

```sql
INSERT INTO azure.ai_discovery.investigations (
description,
tags,
displayName,
project_name,
investigation_name,
endpoint
)
SELECT 
'{{ description }}',
'{{ tags }}',
'{{ displayName }}',
'{{ project_name }}',
'{{ investigation_name }}',
'{{ endpoint }}'
RETURNING
name,
createdAt,
createdBy,
createdByType,
description,
displayName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName,
status,
tags
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: investigations
  props:
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the investigations resource.
    - name: investigation_name
      value: "{{ investigation_name }}"
      description: Required parameter for the investigations resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the investigations resource.
    - name: description
      value: "{{ description }}"
      description: |
        The description.
    - name: tags
      description: |
        The tags.
      value:
        - key: "{{ key }}"
          value: "{{ value }}"
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The title.
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

Updates an Investigation.

```sql
REPLACE azure.ai_discovery.investigations
SET 
description = '{{ description }}',
tags = '{{ tags }}',
displayName = '{{ displayName }}'
WHERE 
project_name = '{{ project_name }}' --required
AND investigation_name = '{{ investigation_name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
name,
createdAt,
createdBy,
createdByType,
description,
displayName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName,
status,
tags;
```
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

Delete a Investigation.

```sql
DELETE FROM azure.ai_discovery.investigations
WHERE project_name = '{{ project_name }}' --required
AND investigation_name = '{{ investigation_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'get_discovery_engine', value: 'get_discovery_engine' },
        { label: 'update_discovery_engine', value: 'update_discovery_engine' },
        { label: 'get_discovery_engine_memory', value: 'get_discovery_engine_memory' },
        { label: 'start_discovery_engine', value: 'start_discovery_engine' },
        { label: 'stop_discovery_engine', value: 'stop_discovery_engine' }
    ]}
>
<TabItem value="create_or_replace">

Creates an Investigation.

```sql
EXEC azure.ai_discovery.investigations.create_or_replace 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"description": "{{ description }}", 
"tags": "{{ tags }}", 
"displayName": "{{ displayName }}"
}'
;
```
</TabItem>
<TabItem value="get_discovery_engine">

Get the discovery engine for an investigation.

```sql
EXEC azure.ai_discovery.investigations.get_discovery_engine 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="update_discovery_engine">

Update the discovery engine for an investigation. This will create the discovery engine if it does not already exist.

```sql
EXEC azure.ai_discovery.investigations.update_discovery_engine 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"discoveryEngineStatus": "{{ discoveryEngineStatus }}", 
"systemPrompt": "{{ systemPrompt }}", 
"configuration": "{{ configuration }}"
}'
;
```
</TabItem>
<TabItem value="get_discovery_engine_memory">

List discovery engine working memory entries for an investigation.

```sql
EXEC azure.ai_discovery.investigations.get_discovery_engine_memory 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@skip='{{ skip }}', 
@top='{{ top }}', 
@maxPageSize='{{ maxPageSize }}'
;
```
</TabItem>
<TabItem value="start_discovery_engine">

Start the discovery engine for an investigation.

```sql
EXEC azure.ai_discovery.investigations.start_discovery_engine 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="stop_discovery_engine">

Stop the discovery engine for an investigation.

```sql
EXEC azure.ai_discovery.investigations.stop_discovery_engine 
@project_name='{{ project_name }}' --required, 
@investigation_name='{{ investigation_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
