--- 
title: inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs
  - streamanalytics
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

Creates, updates, deletes, gets or lists an <code>inputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="inputs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.streamanalytics.inputs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_streaming_job', value: 'list_by_streaming_job' }
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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="compression" /></td>
    <td><code>object</code></td>
    <td>Describes how input data is compressed.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the input. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionKey" /></td>
    <td><code>string</code></td>
    <td>partitionKey Describes a key in the input data which is used for partitioning the input data.</td>
</tr>
<tr>
    <td><CopyableCode code="serialization" /></td>
    <td><code>object</code></td>
    <td>Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="watermarkSettings" /></td>
    <td><code>object</code></td>
    <td>Settings which determine whether to read watermark events.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_streaming_job">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="compression" /></td>
    <td><code>object</code></td>
    <td>Describes how input data is compressed.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the input. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionKey" /></td>
    <td><code>string</code></td>
    <td>partitionKey Describes a key in the input data which is used for partitioning the input data.</td>
</tr>
<tr>
    <td><CopyableCode code="serialization" /></td>
    <td><code>object</code></td>
    <td>Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="watermarkSettings" /></td>
    <td><code>object</code></td>
    <td>Settings which determine whether to read watermark events.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-input_name"><code>input_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details about the specified input.</td>
</tr>
<tr>
    <td><a href="#list_by_streaming_job"><CopyableCode code="list_by_streaming_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a></td>
    <td>Lists all of the inputs under the specified streaming job.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-input_name"><code>input_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates an input or replaces an already existing input under an existing streaming job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-input_name"><code>input_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates an existing input under an existing streaming job. This can be used to partially update (ie. update one or two properties) an input without affecting the rest the job or input definition.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-input_name"><code>input_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates an input or replaces an already existing input under an existing streaming job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-input_name"><code>input_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an input from the streaming job.</td>
</tr>
<tr>
    <td><a href="#test"><CopyableCode code="test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-input_name"><code>input_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tests whether an input’s datasource is reachable and usable by the Azure Stream Analytics service.</td>
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
<tr id="parameter-input_name">
    <td><CopyableCode code="input_name" /></td>
    <td><code>string</code></td>
    <td>The name of the input. Required.</td>
</tr>
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The name of the streaming job. Required.</td>
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
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>The $select OData query parameter. This is a comma-separated list of structural properties to include in the response, or "\ *" to include all properties. By default, all properties are returned except diagnostics. Currently only accepts '*\ ' as a valid value. Default value is None.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>Set to '*' to allow a new input to be created, but to prevent updating an existing input. Other values will result in a 412 Pre-condition Failed response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_streaming_job', value: 'list_by_streaming_job' }
    ]}
>
<TabItem value="get">

Gets details about the specified input.

```sql
SELECT
id,
name,
compression,
diagnostics,
etag,
partitionKey,
serialization,
type,
watermarkSettings
FROM azure.streamanalytics.inputs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND input_name = '{{ input_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_streaming_job">

Lists all of the inputs under the specified streaming job.

```sql
SELECT
id,
name,
compression,
diagnostics,
etag,
partitionKey,
serialization,
type,
watermarkSettings
FROM azure.streamanalytics.inputs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $select = '{{ $select }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_replace">

Creates an input or replaces an already existing input under an existing streaming job.

```sql
INSERT INTO azure.streamanalytics.inputs (
name,
properties,
resource_group_name,
job_name,
input_name,
subscription_id,
If-Match,
If-None-Match
)
SELECT 
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ job_name }}',
'{{ input_name }}',
'{{ subscription_id }}',
'{{ If-Match }}',
'{{ If-None-Match }}'
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
- name: inputs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the inputs resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the inputs resource.
    - name: input_name
      value: "{{ input_name }}"
      description: Required parameter for the inputs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the inputs resource.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name.
    - name: properties
      description: |
        The properties that are associated with an input. Required on PUT (CreateOrReplace) requests.
      value:
        type: "{{ type }}"
        serialization:
          type: "{{ type }}"
        diagnostics:
          conditions:
            - since: "{{ since }}"
              code: "{{ code }}"
              message: "{{ message }}"
        etag: "{{ etag }}"
        compression:
          type: "{{ type }}"
        partitionKey: "{{ partitionKey }}"
        watermarkSettings:
          watermarkMode: "{{ watermarkMode }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
      description: The ETag of the input. Omit this value to always overwrite the current input. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
    - name: If-None-Match
      value: "{{ If-None-Match }}"
      description: Set to '*' to allow a new input to be created, but to prevent updating an existing input. Other values will result in a 412 Pre-condition Failed response. Default value is None.
      description: Set to '*' to allow a new input to be created, but to prevent updating an existing input. Other values will result in a 412 Pre-condition Failed response. Default value is None.
`}</CodeBlock>

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

Updates an existing input under an existing streaming job. This can be used to partially update (ie. update one or two properties) an input without affecting the rest the job or input definition.

```sql
UPDATE azure.streamanalytics.inputs
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND input_name = '{{ input_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
properties,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' }
    ]}
>
<TabItem value="create_or_replace">

Creates an input or replaces an already existing input under an existing streaming job.

```sql
REPLACE azure.streamanalytics.inputs
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND input_name = '{{ input_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
AND If-None-Match = '{{ If-None-Match}}'
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an input from the streaming job.

```sql
DELETE FROM azure.streamanalytics.inputs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND input_name = '{{ input_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="test"
    values={[
        { label: 'test', value: 'test' }
    ]}
>
<TabItem value="test">

Tests whether an input’s datasource is reachable and usable by the Azure Stream Analytics service.

```sql
EXEC azure.streamanalytics.inputs.test 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@input_name='{{ input_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
