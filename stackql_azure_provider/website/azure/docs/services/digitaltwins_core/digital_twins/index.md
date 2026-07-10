--- 
title: digital_twins
hide_title: false
hide_table_of_contents: false
keywords:
  - digital_twins
  - digitaltwins_core
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

Creates, updates, deletes, gets or lists a <code>digital_twins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="digital_twins" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digitaltwins_core.digital_twins" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_incoming_relationships"
    values={[
        { label: 'list_incoming_relationships', value: 'list_incoming_relationships' }
    ]}
>
<TabItem value="list_incoming_relationships">

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
    <td><CopyableCode code="$relationshipId" /></td>
    <td><code>string</code></td>
    <td>A user-provided string representing the id of this relationship, unique in the context of the source digital twin, i.e. sourceId + relationshipId is unique in the context of the service.</td>
</tr>
<tr>
    <td><CopyableCode code="$relationshipLink" /></td>
    <td><code>string</code></td>
    <td>Link to the relationship, to be used for deletion.</td>
</tr>
<tr>
    <td><CopyableCode code="$relationshipName" /></td>
    <td><code>string</code></td>
    <td>The name of the relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="$sourceId" /></td>
    <td><code>string</code></td>
    <td>The id of the source digital twin.</td>
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
    <td><a href="#list_incoming_relationships"><CopyableCode code="list_incoming_relationships" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Retrieves all incoming relationship for a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or payload is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * ValidationFailed - Applying the patch results in an invalid digital twin. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a digital twin. All relationships referencing the digital twin must already be deleted. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * RelationshipsNotDeleted - The digital twin contains relationships. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#list_relationships"><CopyableCode code="list_relationships" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-relationshipName"><code>relationshipName</code></a></td>
    <td>Retrieves the relationships from a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.</td>
</tr>
<tr>
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Retrieves a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Adds or replaces a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id or payload is invalid. * ModelDecommissioned - The model for the digital twin is decommissioned. * TwinLimitReached - The maximum number of digital twins allowed has been reached. * ValidationFailed - The digital twin payload is not valid. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#get_relationship_by_id"><CopyableCode code="get_relationship_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-relationship_id"><code>relationship_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Retrieves a relationship between two digital twins. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id or relationship id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * RelationshipNotFound - The relationship was not found.</td>
</tr>
<tr>
    <td><a href="#add_relationship"><CopyableCode code="add_relationship" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-relationship_id"><code>relationship_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Adds a relationship between two digital twins. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id, relationship id, or payload is invalid. * InvalidRelationship - The relationship is invalid. * OperationNotAllowed - The relationship cannot connect to the same digital twin. * ValidationFailed - The relationship content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * TargetTwinNotFound - The digital twin target of the relationship was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#delete_relationship"><CopyableCode code="delete_relationship" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-relationship_id"><code>relationship_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a relationship between two digital twins. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or relationship id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * RelationshipNotFound - The relationship was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#update_relationship"><CopyableCode code="update_relationship" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-relationship_id"><code>relationship_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates the properties on a relationship between two digital twins. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or relationship id is invalid. * InvalidRelationship - The relationship is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * ValidationFailed - The relationship content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * RelationshipNotFound - The relationship was not found. * 409 Conflict * RelationshipAlreadyExists - The relationship already exists. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#get_component"><CopyableCode code="get_component" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-component_path"><code>component_path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Retrieves a component from a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id or component path is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * ComponentNotFound - The component path was not found.</td>
</tr>
<tr>
    <td><a href="#update_component"><CopyableCode code="update_component" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-component_path"><code>component_path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates a component on a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id, component path, or payload is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * ValidationFailed - Applying the patch results in an invalid digital twin. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.</td>
</tr>
<tr>
    <td><a href="#send_telemetry"><CopyableCode code="send_telemetry" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-Message-Id"><code>Message-Id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-Telemetry-Source-Time"><code>Telemetry-Source-Time</code></a></td>
    <td>Sends telemetry on behalf of a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or message id is invalid. * ValidationFailed - The telemetry content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.</td>
</tr>
<tr>
    <td><a href="#send_component_telemetry"><CopyableCode code="send_component_telemetry" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-component_path"><code>component_path</code></a>, <a href="#parameter-Message-Id"><code>Message-Id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-Telemetry-Source-Time"><code>Telemetry-Source-Time</code></a></td>
    <td>Sends telemetry on behalf of a component in a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id, message id, or component path is invalid. * ValidationFailed - The telemetry content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * ComponentNotFound - The component path was not found.</td>
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
<tr id="parameter-Message-Id">
    <td><CopyableCode code="Message-Id" /></td>
    <td><code>string</code></td>
    <td>A unique message identifier (in the scope of the digital twin id) that is commonly used for de-duplicating messages. Required.</td>
</tr>
<tr id="parameter-component_path">
    <td><CopyableCode code="component_path" /></td>
    <td><code>string</code></td>
    <td>The name of the DTDL component. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the digital twin. The id is unique within the service and case sensitive. Required.</td>
</tr>
<tr id="parameter-relationship_id">
    <td><CopyableCode code="relationship_id" /></td>
    <td><code>string</code></td>
    <td>The id of the relationship. The id is unique within the digital twin and case sensitive. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-Telemetry-Source-Time">
    <td><CopyableCode code="Telemetry-Source-Time" /></td>
    <td><code>string</code></td>
    <td>An RFC 3339 timestamp that identifies the time the telemetry was measured. Default value is None.</td>
</tr>
<tr id="parameter-relationshipName">
    <td><CopyableCode code="relationshipName" /></td>
    <td><code>string</code></td>
    <td>The name of the relationship. Default value is None.</td>
</tr>
<tr id="parameter-traceparent">
    <td><CopyableCode code="traceparent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tracestate">
    <td><CopyableCode code="tracestate" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_incoming_relationships"
    values={[
        { label: 'list_incoming_relationships', value: 'list_incoming_relationships' }
    ]}
>
<TabItem value="list_incoming_relationships">

Retrieves all incoming relationship for a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.

```sql
SELECT
$relationshipId,
$relationshipLink,
$relationshipName,
$sourceId
FROM azure.digitaltwins_core.digital_twins
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or payload is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * ValidationFailed - Applying the patch results in an invalid digital twin. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
UPDATE azure.digitaltwins_core.digital_twins
SET 
traceparent = '{{ traceparent }}',
tracestate = '{{ tracestate }}',
If-Match = '{{ If-Match }}'
WHERE 
id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND traceparent = '{{ traceparent}}'
AND tracestate = '{{ tracestate}}'
AND If-Match = '{{ If-Match}}';
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

Deletes a digital twin. All relationships referencing the digital twin must already be deleted. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * RelationshipsNotDeleted - The digital twin contains relationships. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
DELETE FROM azure.digitaltwins_core.digital_twins
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_relationships"
    values={[
        { label: 'list_relationships', value: 'list_relationships' },
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'add', value: 'add' },
        { label: 'get_relationship_by_id', value: 'get_relationship_by_id' },
        { label: 'add_relationship', value: 'add_relationship' },
        { label: 'delete_relationship', value: 'delete_relationship' },
        { label: 'update_relationship', value: 'update_relationship' },
        { label: 'get_component', value: 'get_component' },
        { label: 'update_component', value: 'update_component' },
        { label: 'send_telemetry', value: 'send_telemetry' },
        { label: 'send_component_telemetry', value: 'send_component_telemetry' }
    ]}
>
<TabItem value="list_relationships">

Retrieves the relationships from a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.

```sql
EXEC azure.digitaltwins_core.digital_twins.list_relationships 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@relationshipName='{{ relationshipName }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
<TabItem value="get_by_id">

Retrieves a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.

```sql
EXEC azure.digitaltwins_core.digital_twins.get_by_id 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
<TabItem value="add">

Adds or replaces a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id or payload is invalid. * ModelDecommissioned - The model for the digital twin is decommissioned. * TwinLimitReached - The maximum number of digital twins allowed has been reached. * ValidationFailed - The digital twin payload is not valid. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
EXEC azure.digitaltwins_core.digital_twins.add 
@id='{{ id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@If-None-Match='{{ If-None-Match }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}", 
"If-None-Match": "{{ If-None-Match }}"
}'
;
```
</TabItem>
<TabItem value="get_relationship_by_id">

Retrieves a relationship between two digital twins. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id or relationship id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * RelationshipNotFound - The relationship was not found.

```sql
EXEC azure.digitaltwins_core.digital_twins.get_relationship_by_id 
@id='{{ id }}' --required, 
@relationship_id='{{ relationship_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
<TabItem value="add_relationship">

Adds a relationship between two digital twins. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id, relationship id, or payload is invalid. * InvalidRelationship - The relationship is invalid. * OperationNotAllowed - The relationship cannot connect to the same digital twin. * ValidationFailed - The relationship content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * TargetTwinNotFound - The digital twin target of the relationship was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
EXEC azure.digitaltwins_core.digital_twins.add_relationship 
@id='{{ id }}' --required, 
@relationship_id='{{ relationship_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@If-None-Match='{{ If-None-Match }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}", 
"If-None-Match": "{{ If-None-Match }}"
}'
;
```
</TabItem>
<TabItem value="delete_relationship">

Deletes a relationship between two digital twins. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or relationship id is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * RelationshipNotFound - The relationship was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
EXEC azure.digitaltwins_core.digital_twins.delete_relationship 
@id='{{ id }}' --required, 
@relationship_id='{{ relationship_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@If-Match='{{ If-Match }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}", 
"If-Match": "{{ If-Match }}"
}'
;
```
</TabItem>
<TabItem value="update_relationship">

Updates the properties on a relationship between two digital twins. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or relationship id is invalid. * InvalidRelationship - The relationship is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * ValidationFailed - The relationship content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * RelationshipNotFound - The relationship was not found. * 409 Conflict * RelationshipAlreadyExists - The relationship already exists. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
EXEC azure.digitaltwins_core.digital_twins.update_relationship 
@id='{{ id }}' --required, 
@relationship_id='{{ relationship_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@If-Match='{{ If-Match }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}", 
"If-Match": "{{ If-Match }}"
}'
;
```
</TabItem>
<TabItem value="get_component">

Retrieves a component from a digital twin. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The digital twin id or component path is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * ComponentNotFound - The component path was not found.

```sql
EXEC azure.digitaltwins_core.digital_twins.get_component 
@id='{{ id }}' --required, 
@component_path='{{ component_path }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
<TabItem value="update_component">

Updates a component on a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id, component path, or payload is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * ValidationFailed - Applying the patch results in an invalid digital twin. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * 412 Precondition Failed * PreconditionFailed - The precondition check (If-Match or If-None-Match) failed.

```sql
EXEC azure.digitaltwins_core.digital_twins.update_component 
@id='{{ id }}' --required, 
@component_path='{{ component_path }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@If-Match='{{ If-Match }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}", 
"If-Match": "{{ If-Match }}"
}'
;
```
</TabItem>
<TabItem value="send_telemetry">

Sends telemetry on behalf of a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id or message id is invalid. * ValidationFailed - The telemetry content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found.

```sql
EXEC azure.digitaltwins_core.digital_twins.send_telemetry 
@id='{{ id }}' --required, 
@Message-Id='{{ Message-Id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@Telemetry-Source-Time='{{ Telemetry-Source-Time }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
<TabItem value="send_component_telemetry">

Sends telemetry on behalf of a component in a digital twin. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The digital twin id, message id, or component path is invalid. * ValidationFailed - The telemetry content is invalid. * 404 Not Found * DigitalTwinNotFound - The digital twin was not found. * ComponentNotFound - The component path was not found.

```sql
EXEC azure.digitaltwins_core.digital_twins.send_component_telemetry 
@id='{{ id }}' --required, 
@component_path='{{ component_path }}' --required, 
@Message-Id='{{ Message-Id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@traceparent='{{ traceparent }}', 
@tracestate='{{ tracestate }}', 
@Telemetry-Source-Time='{{ Telemetry-Source-Time }}' 
@@json=
'{
"traceparent": "{{ traceparent }}", 
"tracestate": "{{ tracestate }}"
}'
;
```
</TabItem>
</Tabs>
