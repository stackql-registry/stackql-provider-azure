--- 
title: trained_model
hide_title: false
hide_table_of_contents: false
keywords:
  - trained_model
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

Creates, updates, deletes, gets or lists a <code>trained_model</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="trained_model" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language.trained_model" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_evaluation_status"
    values={[
        { label: 'get_evaluation_status', value: 'get_evaluation_status' },
        { label: 'get_model_evaluation_results', value: 'get_model_evaluation_results' },
        { label: 'get_trained_model', value: 'get_trained_model' }
    ]}
>
<TabItem value="get_evaluation_status">

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
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Represents evaluation task detailed result. Required.</td>
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
<TabItem value="get_model_evaluation_results">

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
    <td><CopyableCode code="entitiesResult" /></td>
    <td><code>object</code></td>
    <td>Represents the entities results for the utterance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="intentsResult" /></td>
    <td><code>object</code></td>
    <td>Represents the intents results for the utterance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Represents the utterance language. This is BCP-47 representation of a language. For example, use "en" for English, "en-gb" for English (UK), "es" for Spanish etc. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>Represents the utterance text. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_trained_model">

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
    <td><CopyableCode code="hasSnapshot" /></td>
    <td><code>boolean</code></td>
    <td>The flag to indicate if the trained model has a snapshot ready. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The trained model label. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last trained date time of the model. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainingDurationInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration of the model's last training request in seconds. Required.</td>
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
    <td><a href="#get_evaluation_status"><CopyableCode code="get_evaluation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the status for an evaluation job.</td>
</tr>
<tr>
    <td><a href="#get_model_evaluation_results"><CopyableCode code="get_model_evaluation_results" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-stringIndexType"><code>stringIndexType</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Gets the detailed results of the evaluation for a trained model. This includes the raw inference results for the data included in the evaluation process.</td>
</tr>
<tr>
    <td><a href="#get_trained_model"><CopyableCode code="get_trained_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the details of a trained model.</td>
</tr>
<tr>
    <td><a href="#delete_trained_model"><CopyableCode code="delete_trained_model" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes an existing trained model.</td>
</tr>
<tr>
    <td><a href="#get_model_evaluation_summary"><CopyableCode code="get_model_evaluation_summary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the evaluation summary of a trained model. The summary includes high level performance measurements of the model e.g., F1, Precision, Recall, etc.</td>
</tr>
<tr>
    <td><a href="#get_load_snapshot_status"><CopyableCode code="get_load_snapshot_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the status for loading a snapshot.</td>
</tr>
<tr>
    <td><a href="#evaluate_model"><CopyableCode code="evaluate_model" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Triggers evaluation operation on a trained model.</td>
</tr>
<tr>
    <td><a href="#load_snapshot"><CopyableCode code="load_snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-trained_model_label"><code>trained_model_label</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Restores the snapshot of this trained model to be the current working directory of the project.</td>
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
<tr id="parameter-stringIndexType">
    <td><CopyableCode code="stringIndexType" /></td>
    <td><code>string</code></td>
    <td>Specifies the method used to interpret string offsets. For additional information see `https://aka.ms/text-analytics-offsets `_. Known values are: "Utf16CodeUnit", "Utf8CodeUnit", and "Utf32CodeUnit". Required.</td>
</tr>
<tr id="parameter-trained_model_label">
    <td><CopyableCode code="trained_model_label" /></td>
    <td><code>string</code></td>
    <td>The trained model label. Required.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_evaluation_status"
    values={[
        { label: 'get_evaluation_status', value: 'get_evaluation_status' },
        { label: 'get_model_evaluation_results', value: 'get_model_evaluation_results' },
        { label: 'get_trained_model', value: 'get_trained_model' }
    ]}
>
<TabItem value="get_evaluation_status">

Gets the status for an evaluation job.

```sql
SELECT
createdDateTime,
errors,
expirationDateTime,
jobId,
lastUpdatedDateTime,
result,
status,
warnings
FROM azure.ai_language.trained_model
WHERE trained_model_label = '{{ trained_model_label }}' -- required
AND job_id = '{{ job_id }}' -- required
AND project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_model_evaluation_results">

Gets the detailed results of the evaluation for a trained model. This includes the raw inference results for the data included in the evaluation process.

```sql
SELECT
entitiesResult,
intentsResult,
language,
text
FROM azure.ai_language.trained_model
WHERE trained_model_label = '{{ trained_model_label }}' -- required
AND project_name = '{{ project_name }}' -- required
AND stringIndexType = '{{ stringIndexType }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
<TabItem value="get_trained_model">

Gets the details of a trained model.

```sql
SELECT
hasSnapshot,
label,
lastTrainedDateTime,
lastTrainingDurationInSeconds,
modelExpirationDate,
modelId,
modelTrainingConfigVersion
FROM azure.ai_language.trained_model
WHERE trained_model_label = '{{ trained_model_label }}' -- required
AND project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_trained_model"
    values={[
        { label: 'delete_trained_model', value: 'delete_trained_model' }
    ]}
>
<TabItem value="delete_trained_model">

Deletes an existing trained model.

```sql
DELETE FROM azure.ai_language.trained_model
WHERE trained_model_label = '{{ trained_model_label }}' --required
AND project_name = '{{ project_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_model_evaluation_summary"
    values={[
        { label: 'get_model_evaluation_summary', value: 'get_model_evaluation_summary' },
        { label: 'get_load_snapshot_status', value: 'get_load_snapshot_status' },
        { label: 'evaluate_model', value: 'evaluate_model' },
        { label: 'load_snapshot', value: 'load_snapshot' }
    ]}
>
<TabItem value="get_model_evaluation_summary">

Gets the evaluation summary of a trained model. The summary includes high level performance measurements of the model e.g., F1, Precision, Recall, etc.

```sql
EXEC azure.ai_language.trained_model.get_model_evaluation_summary 
@trained_model_label='{{ trained_model_label }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_load_snapshot_status">

Gets the status for loading a snapshot.

```sql
EXEC azure.ai_language.trained_model.get_load_snapshot_status 
@trained_model_label='{{ trained_model_label }}' --required, 
@job_id='{{ job_id }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="evaluate_model">

Triggers evaluation operation on a trained model.

```sql
EXEC azure.ai_language.trained_model.evaluate_model 
@trained_model_label='{{ trained_model_label }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"trainingSplitPercentage": {{ trainingSplitPercentage }}, 
"testingSplitPercentage": {{ testingSplitPercentage }}
}'
;
```
</TabItem>
<TabItem value="load_snapshot">

Restores the snapshot of this trained model to be the current working directory of the project.

```sql
EXEC azure.ai_language.trained_model.load_snapshot 
@trained_model_label='{{ trained_model_label }}' --required, 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
