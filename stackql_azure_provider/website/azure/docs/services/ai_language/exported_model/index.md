--- 
title: exported_model
hide_title: false
hide_table_of_contents: false
keywords:
  - exported_model
  - ai_language
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

Creates, updates, deletes, gets or lists an <code>exported_model</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exported_model" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language.exported_model" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_exported_model_job_status"
    values={[
        { label: 'get_exported_model_job_status', value: 'get_exported_model_job_status' },
        { label: 'get_exported_model', value: 'get_exported_model' }
    ]}
>
<TabItem value="get_exported_model_job_status">

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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date time of the job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The errors encountered while executing the job.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>The job ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last date time the job was updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The job status. Required. Known values are: "notStarted", "running", "succeeded", "failed", "cancelled", "cancelling", and "partiallyCompleted". (notStarted, running, succeeded, failed, cancelled, cancelling, partiallyCompleted)</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>The warnings that were encountered while executing the job.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_exported_model">

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
    <td><CopyableCode code="exportedModelName" /></td>
    <td><code>string</code></td>
    <td>The exported model name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastExportedModelDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last exported date time of the model. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last trained date time of the model. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelExpirationDate" /></td>
    <td><code>string (date)</code></td>
    <td>The model expiration date. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>The model ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelTrainingConfigVersion" /></td>
    <td><code>string</code></td>
    <td>The model training config version. Required.</td>
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
    <td><a href="#get_exported_model_job_status"><CopyableCode code="get_exported_model_job_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-exported_model_name"><code>exported_model_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the status for an existing job to create or update an exported model.</td>
</tr>
<tr>
    <td><a href="#get_exported_model"><CopyableCode code="get_exported_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-exported_model_name"><code>exported_model_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the details of an exported model.</td>
</tr>
<tr>
    <td><a href="#create_or_update_exported_model"><CopyableCode code="create_or_update_exported_model" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-exported_model_name"><code>exported_model_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-trainedModelLabel"><code>trainedModelLabel</code></a></td>
    <td></td>
    <td>Creates a new exported model or replaces an existing one.</td>
</tr>
<tr>
    <td><a href="#create_or_update_exported_model"><CopyableCode code="create_or_update_exported_model" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-exported_model_name"><code>exported_model_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-trainedModelLabel"><code>trainedModelLabel</code></a></td>
    <td></td>
    <td>Creates a new exported model or replaces an existing one.</td>
</tr>
<tr>
    <td><a href="#delete_exported_model"><CopyableCode code="delete_exported_model" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-exported_model_name"><code>exported_model_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes an existing exported model.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-exported_model_name">
    <td><CopyableCode code="exported_model_name" /></td>
    <td><code>string</code></td>
    <td>The exported model name. Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job ID. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_exported_model_job_status"
    values={[
        { label: 'get_exported_model_job_status', value: 'get_exported_model_job_status' },
        { label: 'get_exported_model', value: 'get_exported_model' }
    ]}
>
<TabItem value="get_exported_model_job_status">

Gets the status for an existing job to create or update an exported model.

```sql
SELECT
createdDateTime,
errors,
expirationDateTime,
jobId,
lastUpdatedDateTime,
status,
warnings
FROM azure.ai_language.exported_model
WHERE exported_model_name = '{{ exported_model_name }}' -- required
AND job_id = '{{ job_id }}' -- required
AND project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_exported_model">

Gets the details of an exported model.

```sql
SELECT
exportedModelName,
lastExportedModelDateTime,
lastTrainedDateTime,
modelExpirationDate,
modelId,
modelTrainingConfigVersion
FROM azure.ai_language.exported_model
WHERE exported_model_name = '{{ exported_model_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_exported_model"
    values={[
        { label: 'create_or_update_exported_model', value: 'create_or_update_exported_model' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_exported_model">

Creates a new exported model or replaces an existing one.

```sql
INSERT INTO azure.ai_language.exported_model (
trainedModelLabel,
exported_model_name,
project_name,
endpoint
)
SELECT 
'{{ trainedModelLabel }}' /* required */,
'{{ exported_model_name }}',
'{{ project_name }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: exported_model
  props:
    - name: exported_model_name
      value: "{{ exported_model_name }}"
      description: Required parameter for the exported_model resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the exported_model resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the exported_model resource.
    - name: trainedModelLabel
      value: "{{ trainedModelLabel }}"
      description: |
        The trained model label. Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_exported_model"
    values={[
        { label: 'create_or_update_exported_model', value: 'create_or_update_exported_model' }
    ]}
>
<TabItem value="create_or_update_exported_model">

Creates a new exported model or replaces an existing one.

```sql
REPLACE azure.ai_language.exported_model
SET 
trainedModelLabel = '{{ trainedModelLabel }}'
WHERE 
exported_model_name = '{{ exported_model_name }}' --required
AND project_name = '{{ project_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND trainedModelLabel = '{{ trainedModelLabel }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_exported_model"
    values={[
        { label: 'delete_exported_model', value: 'delete_exported_model' }
    ]}
>
<TabItem value="delete_exported_model">

Deletes an existing exported model.

```sql
DELETE FROM azure.ai_language.exported_model
WHERE exported_model_name = '{{ exported_model_name }}' --required
AND project_name = '{{ project_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
