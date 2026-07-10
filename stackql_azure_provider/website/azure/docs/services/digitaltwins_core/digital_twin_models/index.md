--- 
title: digital_twin_models
hide_title: false
hide_table_of_contents: false
keywords:
  - digital_twin_models
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

Creates, updates, deletes, gets or lists a <code>digital_twin_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="digital_twin_models" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digitaltwins_core.digital_twin_models" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

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
    <td>The id of the model as specified in the model definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="decommissioned" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the model is decommissioned. Decommissioned models cannot be referenced by newly created digital twins.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>object</code></td>
    <td>A language map that contains the localized descriptions as specified in the model definition.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>object</code></td>
    <td>A language map that contains the localized display names as specified in the model definition.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>object</code></td>
    <td>The model definition.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the model was uploaded to the service.</td>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the model as specified in the model definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="decommissioned" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the model is decommissioned. Decommissioned models cannot be referenced by newly created digital twins.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>object</code></td>
    <td>A language map that contains the localized descriptions as specified in the model definition.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>object</code></td>
    <td>A language map that contains the localized display names as specified in the model definition.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>object</code></td>
    <td>The model definition.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the model was uploaded to the service.</td>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-includeModelDefinition"><code>includeModelDefinition</code></a></td>
    <td>Retrieves model metadata and optionally the model definition. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The model id is invalid. * MissingArgument - The model id was not provided. * 404 Not Found * ModelNotFound - The model was not found.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a>, <a href="#parameter-includeModelDefinition"><code>includeModelDefinition</code></a>, <a href="#parameter-max-items-per-page"><code>max-items-per-page</code></a></td>
    <td>Retrieves model metadata and, optionally, model definitions. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The model id is invalid. * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been reached. * 404 Not Found * ModelNotFound - The model was not found.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Updates the metadata for a model. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The model id is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * MissingArgument - The model id was not provided. * 404 Not Found * ModelNotFound - The model was not found. * 409 Conflict * ModelReferencesNotDecommissioned - The model refers to models that are not decommissioned.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Deletes a model. A model can only be deleted if no other models reference it. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The model id is invalid. * MissingArgument - The model id was not provided. * 404 Not Found * ModelNotFound - The model was not found. * 409 Conflict * ModelReferencesNotDeleted - The model refers to models that are not deleted.</td>
</tr>
<tr>
    <td><a href="#add"><CopyableCode code="add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-traceparent"><code>traceparent</code></a>, <a href="#parameter-tracestate"><code>tracestate</code></a></td>
    <td>Uploads one or more models. When any error occurs, no models are uploaded. Status codes: * 201 Created * 400 Bad Request * DTDLParserError - The models provided are not valid DTDL. * InvalidArgument - The model id is invalid. * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been reached. * ModelVersionNotSupported - The version of DTDL used is not supported. * 409 Conflict * ModelAlreadyExists - The model provided already exists.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id for the model. The id is globally unique and case sensitive. Required.</td>
</tr>
<tr id="parameter-includeModelDefinition">
    <td><CopyableCode code="includeModelDefinition" /></td>
    <td><code>boolean</code></td>
    <td>When true the model definition will be returned as part of the result. Default value is False.</td>
</tr>
<tr id="parameter-max-items-per-page">
    <td><CopyableCode code="max-items-per-page" /></td>
    <td><code>integer</code></td>
    <td></td>
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
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

Retrieves model metadata and optionally the model definition. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The model id is invalid. * MissingArgument - The model id was not provided. * 404 Not Found * ModelNotFound - The model was not found.

```sql
SELECT
id,
decommissioned,
description,
displayName,
model,
uploadTime
FROM azure.digitaltwins_core.digital_twin_models
WHERE id = '{{ id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
AND includeModelDefinition = '{{ includeModelDefinition }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves model metadata and, optionally, model definitions. Status codes: * 200 OK * 400 Bad Request * InvalidArgument - The model id is invalid. * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been reached. * 404 Not Found * ModelNotFound - The model was not found.

```sql
SELECT
id,
decommissioned,
description,
displayName,
model,
uploadTime
FROM azure.digitaltwins_core.digital_twin_models
WHERE endpoint = '{{ endpoint }}' -- required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
AND includeModelDefinition = '{{ includeModelDefinition }}'
AND max-items-per-page = '{{ max-items-per-page }}'
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

Updates the metadata for a model. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The model id is invalid. * JsonPatchInvalid - The JSON Patch provided is invalid. * MissingArgument - The model id was not provided. * 404 Not Found * ModelNotFound - The model was not found. * 409 Conflict * ModelReferencesNotDecommissioned - The model refers to models that are not decommissioned.

```sql
UPDATE azure.digitaltwins_core.digital_twin_models
SET 
traceparent = '{{ traceparent }}',
tracestate = '{{ tracestate }}'
WHERE 
id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND traceparent = '{{ traceparent}}'
AND tracestate = '{{ tracestate}}';
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

Deletes a model. A model can only be deleted if no other models reference it. Status codes: * 204 No Content * 400 Bad Request * InvalidArgument - The model id is invalid. * MissingArgument - The model id was not provided. * 404 Not Found * ModelNotFound - The model was not found. * 409 Conflict * ModelReferencesNotDeleted - The model refers to models that are not deleted.

```sql
DELETE FROM azure.digitaltwins_core.digital_twin_models
WHERE id = '{{ id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND traceparent = '{{ traceparent }}'
AND tracestate = '{{ tracestate }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add"
    values={[
        { label: 'add', value: 'add' }
    ]}
>
<TabItem value="add">

Uploads one or more models. When any error occurs, no models are uploaded. Status codes: * 201 Created * 400 Bad Request * DTDLParserError - The models provided are not valid DTDL. * InvalidArgument - The model id is invalid. * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been reached. * ModelVersionNotSupported - The version of DTDL used is not supported. * 409 Conflict * ModelAlreadyExists - The model provided already exists.

```sql
EXEC azure.digitaltwins_core.digital_twin_models.add 
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
</Tabs>
