--- 
title: link_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - link_connection
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

Creates, updates, deletes, gets or lists a <code>link_connection</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="link_connection" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.link_connection" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td>Link connection id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Link connection name.</td>
</tr>
<tr>
    <td><CopyableCode code="compute" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's compute.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Link connection description.</td>
</tr>
<tr>
    <td><CopyableCode code="landingZone" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's landing zone.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabase" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's source database.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's target database.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Link connection type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td>Link connection id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Link connection name.</td>
</tr>
<tr>
    <td><CopyableCode code="compute" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's compute.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Link connection description.</td>
</tr>
<tr>
    <td><CopyableCode code="landingZone" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's landing zone.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDatabase" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's source database.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>object</code></td>
    <td>Properties of link connection's target database.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Link connection type.</td>
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
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a link connection.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List link connections.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a link connection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a link connection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a link connection.</td>
</tr>
<tr>
    <td><a href="#list_link_tables"><CopyableCode code="list_link_tables" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List the link tables of a link connection.</td>
</tr>
<tr>
    <td><a href="#get_detailed_status"><CopyableCode code="get_detailed_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the detailed status of a link connection.</td>
</tr>
<tr>
    <td><a href="#edit_tables"><CopyableCode code="edit_tables" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Edit tables for a link connection.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Start a link connection. It may take a few minutes from Starting to Running, monitor the status with LinkConnection_GetDetailedStatus.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stop a link connection. It may take a few minutes from Stopping to stopped, monitor the status with LinkConnection_GetDetailedStatus.</td>
</tr>
<tr>
    <td><a href="#query_table_status"><CopyableCode code="query_table_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Query the link table status of a link connection.</td>
</tr>
<tr>
    <td><a href="#update_landing_zone_credential"><CopyableCode code="update_landing_zone_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Update landing zone credential of a link connection.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Pause a link connection. It may take a few minutes from Pausing to Paused, monitor the status with LinkConnection_GetDetailedStatus.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-link_connection_name"><code>link_connection_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resume a link connection. It may take a few minutes from Resuming to Running, monitor the status with LinkConnection_GetDetailedStatus.</td>
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
<tr id="parameter-link_connection_name">
    <td><CopyableCode code="link_connection_name" /></td>
    <td><code>string</code></td>
    <td>The link connection name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Get a link connection.

```sql
SELECT
id,
name,
compute,
description,
landingZone,
sourceDatabase,
targetDatabase,
type
FROM azure.synapse_artifacts.link_connection
WHERE link_connection_name = '{{ link_connection_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

List link connections.

```sql
SELECT
id,
name,
compute,
description,
landingZone,
sourceDatabase,
targetDatabase,
type
FROM azure.synapse_artifacts.link_connection
WHERE endpoint = '{{ endpoint }}' -- required
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

Creates or updates a link connection.

```sql
INSERT INTO azure.synapse_artifacts.link_connection (
id,
name,
type,
properties,
description,
link_connection_name,
endpoint
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ type }}',
'{{ properties }}' /* required */,
'{{ description }}',
'{{ link_connection_name }}',
'{{ endpoint }}'
RETURNING
id,
name,
description,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: link_connection
  props:
    - name: link_connection_name
      value: "{{ link_connection_name }}"
      description: Required parameter for the link_connection resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the link_connection resource.
    - name: id
      value: "{{ id }}"
      description: |
        Link connection id.
    - name: name
      value: "{{ name }}"
      description: |
        Link connection name.
    - name: type
      value: "{{ type }}"
      description: |
        Link connection type.
    - name: properties
      description: |
        Properties of link connection. Required.
      value:
        sourceDatabase:
          linkedService:
            type: "{{ type }}"
            referenceName: "{{ referenceName }}"
            parameters: "{{ parameters }}"
          typeProperties:
            resourceId: "{{ resourceId }}"
            principalId: "{{ principalId }}"
        targetDatabase:
          linkedService:
            type: "{{ type }}"
            referenceName: "{{ referenceName }}"
            parameters: "{{ parameters }}"
          typeProperties:
            crossTableTransaction: {{ crossTableTransaction }}
            dropExistingTargetTableOnStart: {{ dropExistingTargetTableOnStart }}
            actionOnExistingTargetTable: "{{ actionOnExistingTargetTable }}"
        landingZone:
          linkedService:
            type: "{{ type }}"
            referenceName: "{{ referenceName }}"
            parameters: "{{ parameters }}"
          fileSystem: "{{ fileSystem }}"
          folderPath: "{{ folderPath }}"
          sasToken:
            type: "{{ type }}"
            value: "{{ value }}"
        compute:
          coreCount: {{ coreCount }}
          computeType: "{{ computeType }}"
          dataProcessIntervalMinutes: {{ dataProcessIntervalMinutes }}
    - name: description
      value: "{{ description }}"
      description: |
        Link connection description.
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

Creates or updates a link connection.

```sql
REPLACE azure.synapse_artifacts.link_connection
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
properties = '{{ properties }}',
description = '{{ description }}'
WHERE 
link_connection_name = '{{ link_connection_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
description,
properties,
type;
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

Delete a link connection.

```sql
DELETE FROM azure.synapse_artifacts.link_connection
WHERE link_connection_name = '{{ link_connection_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_link_tables"
    values={[
        { label: 'list_link_tables', value: 'list_link_tables' },
        { label: 'get_detailed_status', value: 'get_detailed_status' },
        { label: 'edit_tables', value: 'edit_tables' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'query_table_status', value: 'query_table_status' },
        { label: 'update_landing_zone_credential', value: 'update_landing_zone_credential' },
        { label: 'pause', value: 'pause' },
        { label: 'resume', value: 'resume' }
    ]}
>
<TabItem value="list_link_tables">

List the link tables of a link connection.

```sql
EXEC azure.synapse_artifacts.link_connection.list_link_tables 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_detailed_status">

Get the detailed status of a link connection.

```sql
EXEC azure.synapse_artifacts.link_connection.get_detailed_status 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="edit_tables">

Edit tables for a link connection.

```sql
EXEC azure.synapse_artifacts.link_connection.edit_tables 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"id": "{{ id }}", 
"source": "{{ source }}", 
"target": "{{ target }}", 
"operationType": "{{ operationType }}"
}'
;
```
</TabItem>
<TabItem value="start">

Start a link connection. It may take a few minutes from Starting to Running, monitor the status with LinkConnection_GetDetailedStatus.

```sql
EXEC azure.synapse_artifacts.link_connection.start 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop a link connection. It may take a few minutes from Stopping to stopped, monitor the status with LinkConnection_GetDetailedStatus.

```sql
EXEC azure.synapse_artifacts.link_connection.stop 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="query_table_status">

Query the link table status of a link connection.

```sql
EXEC azure.synapse_artifacts.link_connection.query_table_status 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"maxSegmentCount": {{ maxSegmentCount }}, 
"continuationToken": "{{ continuationToken }}"
}'
;
```
</TabItem>
<TabItem value="update_landing_zone_credential">

Update landing zone credential of a link connection.

```sql
EXEC azure.synapse_artifacts.link_connection.update_landing_zone_credential 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"type": "{{ type }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="pause">

Pause a link connection. It may take a few minutes from Pausing to Paused, monitor the status with LinkConnection_GetDetailedStatus.

```sql
EXEC azure.synapse_artifacts.link_connection.pause 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resume a link connection. It may take a few minutes from Resuming to Running, monitor the status with LinkConnection_GetDetailedStatus.

```sql
EXEC azure.synapse_artifacts.link_connection.resume 
@link_connection_name='{{ link_connection_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
