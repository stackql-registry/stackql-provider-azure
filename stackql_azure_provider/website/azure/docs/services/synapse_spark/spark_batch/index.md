--- 
title: spark_batch
hide_title: false
hide_table_of_contents: false
keywords:
  - spark_batch
  - synapse_spark
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

Creates, updates, deletes, gets or lists a <code>spark_batch</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="spark_batch" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_spark.spark_batch" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_spark_batch_job"
    values={[
        { label: 'get_spark_batch_job', value: 'get_spark_batch_job' },
        { label: 'get_spark_batch_jobs', value: 'get_spark_batch_jobs' }
    ]}
>
<TabItem value="get_spark_batch_job">

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
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appInfo" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="artifactId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="errorInfo" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="livyInfo" /></td>
    <td><code>object</code></td>
    <td>SparkBatchJobState.</td>
</tr>
<tr>
    <td><CopyableCode code="log" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pluginInfo" /></td>
    <td><code>object</code></td>
    <td>SparkServicePlugin.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schedulerInfo" /></td>
    <td><code>object</code></td>
    <td>SparkScheduler.</td>
</tr>
<tr>
    <td><CopyableCode code="sparkPoolName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="submitterId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="submitterName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workspaceName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_spark_batch_jobs">

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
    <td><CopyableCode code="from" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sessions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="total" /></td>
    <td><code>integer</code></td>
    <td></td>
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
    <td><a href="#get_spark_batch_job"><CopyableCode code="get_spark_batch_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-batch_id"><code>batch_id</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>Gets a single spark batch job.</td>
</tr>
<tr>
    <td><a href="#get_spark_batch_jobs"><CopyableCode code="get_spark_batch_jobs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-from"><code>from</code></a>, <a href="#parameter-size"><code>size</code></a>, <a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>List all spark batch jobs which are running under a particular spark pool.</td>
</tr>
<tr>
    <td><a href="#create_spark_batch_job"><CopyableCode code="create_spark_batch_job" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td><a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>Create new spark batch job.</td>
</tr>
<tr>
    <td><a href="#cancel_spark_batch_job"><CopyableCode code="cancel_spark_batch_job" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-batch_id"><code>batch_id</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancels a running spark batch job.</td>
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
<tr id="parameter-batch_id">
    <td><CopyableCode code="batch_id" /></td>
    <td><code>integer</code></td>
    <td>Identifier for the batch job.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-livy_api_version">
    <td><CopyableCode code="livy_api_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-spark_pool_name">
    <td><CopyableCode code="spark_pool_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-detailed">
    <td><CopyableCode code="detailed" /></td>
    <td><code>boolean</code></td>
    <td>Optional query param specifying whether detailed response is returned beyond plain livy.</td>
</tr>
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>integer</code></td>
    <td>Optional param specifying which index the list should begin from.</td>
</tr>
<tr id="parameter-size">
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>Optional param specifying the size of the returned list. By default it is 20 and that is the maximum.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_spark_batch_job"
    values={[
        { label: 'get_spark_batch_job', value: 'get_spark_batch_job' },
        { label: 'get_spark_batch_jobs', value: 'get_spark_batch_jobs' }
    ]}
>
<TabItem value="get_spark_batch_job">

Gets a single spark batch job.

```sql
SELECT
id,
name,
appId,
appInfo,
artifactId,
errorInfo,
jobType,
livyInfo,
log,
pluginInfo,
result,
schedulerInfo,
sparkPoolName,
state,
submitterId,
submitterName,
tags,
workspaceName
FROM azure.synapse_spark.spark_batch
WHERE batch_id = '{{ batch_id }}' -- required
AND livy_api_version = '{{ livy_api_version }}' -- required
AND spark_pool_name = '{{ spark_pool_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND detailed = '{{ detailed }}'
;
```
</TabItem>
<TabItem value="get_spark_batch_jobs">

List all spark batch jobs which are running under a particular spark pool.

```sql
SELECT
from,
sessions,
total
FROM azure.synapse_spark.spark_batch
WHERE livy_api_version = '{{ livy_api_version }}' -- required
AND spark_pool_name = '{{ spark_pool_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND from = '{{ from }}'
AND size = '{{ size }}'
AND detailed = '{{ detailed }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_spark_batch_job"
    values={[
        { label: 'create_spark_batch_job', value: 'create_spark_batch_job' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_spark_batch_job">

Create new spark batch job.

```sql
INSERT INTO azure.synapse_spark.spark_batch (
tags,
artifactId,
name,
file,
className,
args,
jars,
pyFiles,
files,
archives,
conf,
driverMemory,
driverCores,
executorMemory,
executorCores,
numExecutors,
livy_api_version,
spark_pool_name,
endpoint,
detailed
)
SELECT 
'{{ tags }}',
'{{ artifactId }}',
'{{ name }}' /* required */,
'{{ file }}' /* required */,
'{{ className }}',
'{{ args }}',
'{{ jars }}',
'{{ pyFiles }}',
'{{ files }}',
'{{ archives }}',
'{{ conf }}',
'{{ driverMemory }}',
{{ driverCores }},
'{{ executorMemory }}',
{{ executorCores }},
{{ numExecutors }},
'{{ livy_api_version }}',
'{{ spark_pool_name }}',
'{{ endpoint }}',
'{{ detailed }}'
RETURNING
id,
name,
appId,
appInfo,
artifactId,
errorInfo,
jobType,
livyInfo,
log,
pluginInfo,
result,
schedulerInfo,
sparkPoolName,
state,
submitterId,
submitterName,
tags,
workspaceName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: spark_batch
  props:
    - name: livy_api_version
      value: "{{ livy_api_version }}"
      description: Required parameter for the spark_batch resource.
    - name: spark_pool_name
      value: "{{ spark_pool_name }}"
      description: Required parameter for the spark_batch resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the spark_batch resource.
    - name: tags
      value: "{{ tags }}"
    - name: artifactId
      value: "{{ artifactId }}"
    - name: name
      value: "{{ name }}"
    - name: file
      value: "{{ file }}"
    - name: className
      value: "{{ className }}"
    - name: args
      value:
        - "{{ args }}"
    - name: jars
      value:
        - "{{ jars }}"
    - name: pyFiles
      value:
        - "{{ pyFiles }}"
    - name: files
      value:
        - "{{ files }}"
    - name: archives
      value:
        - "{{ archives }}"
    - name: conf
      value: "{{ conf }}"
    - name: driverMemory
      value: "{{ driverMemory }}"
    - name: driverCores
      value: {{ driverCores }}
    - name: executorMemory
      value: "{{ executorMemory }}"
    - name: executorCores
      value: {{ executorCores }}
    - name: numExecutors
      value: {{ numExecutors }}
    - name: detailed
      value: {{ detailed }}
      description: Optional query param specifying whether detailed response is returned beyond plain livy.
      description: Optional query param specifying whether detailed response is returned beyond plain livy.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="cancel_spark_batch_job"
    values={[
        { label: 'cancel_spark_batch_job', value: 'cancel_spark_batch_job' }
    ]}
>
<TabItem value="cancel_spark_batch_job">

Cancels a running spark batch job.

```sql
DELETE FROM azure.synapse_spark.spark_batch
WHERE batch_id = '{{ batch_id }}' --required
AND livy_api_version = '{{ livy_api_version }}' --required
AND spark_pool_name = '{{ spark_pool_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
