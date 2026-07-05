--- 
title: outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - outputs
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

Creates, updates, deletes, gets or lists an <code>outputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="outputs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.streamanalytics.outputs" /></td></tr>
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
    <td><CopyableCode code="datasource" /></td>
    <td><code>object</code></td>
    <td>Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the output. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOutputEventTimestamps" /></td>
    <td><code>array</code></td>
    <td>A list of the last output event times for each output partition. The index of the array corresponds to the partition number.</td>
</tr>
<tr>
    <td><CopyableCode code="serialization" /></td>
    <td><code>object</code></td>
    <td>Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeWindow" /></td>
    <td><code>integer</code></td>
    <td>The size window to constrain a Stream Analytics output to.</td>
</tr>
<tr>
    <td><CopyableCode code="timeWindow" /></td>
    <td><code>string</code></td>
    <td>The time frame for filtering Stream Analytics job outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="watermarkSettings" /></td>
    <td><code>object</code></td>
    <td>Settings which determine whether to send watermarks to downstream.</td>
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
    <td><CopyableCode code="datasource" /></td>
    <td><code>object</code></td>
    <td>Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The current entity tag for the output. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOutputEventTimestamps" /></td>
    <td><code>array</code></td>
    <td>A list of the last output event times for each output partition. The index of the array corresponds to the partition number.</td>
</tr>
<tr>
    <td><CopyableCode code="serialization" /></td>
    <td><code>object</code></td>
    <td>Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeWindow" /></td>
    <td><code>integer</code></td>
    <td>The size window to constrain a Stream Analytics output to.</td>
</tr>
<tr>
    <td><CopyableCode code="timeWindow" /></td>
    <td><code>string</code></td>
    <td>The time frame for filtering Stream Analytics job outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="watermarkSettings" /></td>
    <td><code>object</code></td>
    <td>Settings which determine whether to send watermarks to downstream.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-output_name"><code>output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details about the specified output.</td>
</tr>
<tr>
    <td><a href="#list_by_streaming_job"><CopyableCode code="list_by_streaming_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a></td>
    <td>Lists all of the outputs under the specified streaming job.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-output_name"><code>output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates an output or replaces an already existing output under an existing streaming job.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-output_name"><code>output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates an existing output under an existing streaming job. This can be used to partially update (ie. update one or two properties) an output without affecting the rest the job or output definition.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-output_name"><code>output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a>, <a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Creates an output or replaces an already existing output under an existing streaming job.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-output_name"><code>output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an output from the streaming job.</td>
</tr>
<tr>
    <td><a href="#test"><CopyableCode code="test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-output_name"><code>output_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tests whether an output’s datasource is reachable and usable by the Azure Stream Analytics service.</td>
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
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The name of the streaming job. Required.</td>
</tr>
<tr id="parameter-output_name">
    <td><CopyableCode code="output_name" /></td>
    <td><code>string</code></td>
    <td>The name of the output. Required.</td>
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
    <td>The ETag of the output. Omit this value to always overwrite the current output. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>Set to '*' to allow a new output to be created, but to prevent updating an existing output. Other values will result in a 412 Pre-condition Failed response. Default value is None.</td>
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

Gets details about the specified output.

```sql
SELECT
id,
name,
datasource,
diagnostics,
etag,
lastOutputEventTimestamps,
serialization,
sizeWindow,
timeWindow,
type,
watermarkSettings
FROM azure.streamanalytics.outputs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND output_name = '{{ output_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_streaming_job">

Lists all of the outputs under the specified streaming job.

```sql
SELECT
id,
name,
datasource,
diagnostics,
etag,
lastOutputEventTimestamps,
serialization,
sizeWindow,
timeWindow,
type,
watermarkSettings
FROM azure.streamanalytics.outputs
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

Creates an output or replaces an already existing output under an existing streaming job.

```sql
INSERT INTO azure.streamanalytics.outputs (
name,
properties,
resource_group_name,
job_name,
output_name,
subscription_id,
If-Match,
If-None-Match
)
SELECT 
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ job_name }}',
'{{ output_name }}',
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
- name: outputs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the outputs resource.
    - name: job_name
      value: "{{ job_name }}"
      description: Required parameter for the outputs resource.
    - name: output_name
      value: "{{ output_name }}"
      description: Required parameter for the outputs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the outputs resource.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name.
    - name: properties
      value:
        datasource:
          type: "{{ type }}"
        timeWindow: "{{ timeWindow }}"
        sizeWindow: {{ sizeWindow }}
        serialization:
          type: "{{ type }}"
        watermarkSettings:
          watermarkMode: "{{ watermarkMode }}"
          maxWatermarkDifferenceAcrossPartitions: "{{ maxWatermarkDifferenceAcrossPartitions }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: The ETag of the output. Omit this value to always overwrite the current output. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
      description: The ETag of the output. Omit this value to always overwrite the current output. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. Default value is None.
    - name: If-None-Match
      value: "{{ If-None-Match }}"
      description: Set to '*' to allow a new output to be created, but to prevent updating an existing output. Other values will result in a 412 Pre-condition Failed response. Default value is None.
      description: Set to '*' to allow a new output to be created, but to prevent updating an existing output. Other values will result in a 412 Pre-condition Failed response. Default value is None.
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

Updates an existing output under an existing streaming job. This can be used to partially update (ie. update one or two properties) an output without affecting the rest the job or output definition.

```sql
UPDATE azure.streamanalytics.outputs
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND output_name = '{{ output_name }}' --required
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

Creates an output or replaces an already existing output under an existing streaming job.

```sql
REPLACE azure.streamanalytics.outputs
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND output_name = '{{ output_name }}' --required
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

Deletes an output from the streaming job.

```sql
DELETE FROM azure.streamanalytics.outputs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND job_name = '{{ job_name }}' --required
AND output_name = '{{ output_name }}' --required
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

Tests whether an output’s datasource is reachable and usable by the Azure Stream Analytics service.

```sql
EXEC azure.streamanalytics.outputs.test 
@resource_group_name='{{ resource_group_name }}' --required, 
@job_name='{{ job_name }}' --required, 
@output_name='{{ output_name }}' --required, 
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
