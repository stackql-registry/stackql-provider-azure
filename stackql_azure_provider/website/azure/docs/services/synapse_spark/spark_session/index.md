--- 
title: spark_session
hide_title: false
hide_table_of_contents: false
keywords:
  - spark_session
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

Creates, updates, deletes, gets or lists a <code>spark_session</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="spark_session" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_spark.spark_session" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_spark_statement"
    values={[
        { label: 'get_spark_statement', value: 'get_spark_statement' },
        { label: 'get_spark_session', value: 'get_spark_session' },
        { label: 'get_spark_sessions', value: 'get_spark_sessions' }
    ]}
>
<TabItem value="get_spark_statement">

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
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>object</code></td>
    <td>SparkStatementOutput. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_spark_session">

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
    <td>SparkSessionState.</td>
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
<TabItem value="get_spark_sessions">

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
    <td><a href="#get_spark_statement"><CopyableCode code="get_spark_statement" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td></td>
    <td>Gets a single statement within a spark session.</td>
</tr>
<tr>
    <td><a href="#get_spark_session"><CopyableCode code="get_spark_session" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td><a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>Gets a single spark session.</td>
</tr>
<tr>
    <td><a href="#get_spark_sessions"><CopyableCode code="get_spark_sessions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td><a href="#parameter-from"><code>from</code></a>, <a href="#parameter-size"><code>size</code></a>, <a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>List all spark sessions which are running under a particular spark pool.</td>
</tr>
<tr>
    <td><a href="#create_spark_session"><CopyableCode code="create_spark_session" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td><a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>Create new spark session.</td>
</tr>
<tr>
    <td><a href="#create_spark_statement"><CopyableCode code="create_spark_statement" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td></td>
    <td>Create statement within a spark session.</td>
</tr>
<tr>
    <td><a href="#cancel_spark_session"><CopyableCode code="cancel_spark_session" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td></td>
    <td>Cancels a running spark session.</td>
</tr>
<tr>
    <td><a href="#get_spark_statements"><CopyableCode code="get_spark_statements" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td></td>
    <td>Gets a list of statements within a spark session.</td>
</tr>
<tr>
    <td><a href="#reset_spark_session_timeout"><CopyableCode code="reset_spark_session_timeout" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td></td>
    <td>Sends a keep alive call to the current session to reset the session timeout.</td>
</tr>
<tr>
    <td><a href="#cancel_spark_statement"><CopyableCode code="cancel_spark_statement" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-statement_id"><code>statement_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-livy_api_version"><code>livy_api_version</code></a>, <a href="#parameter-spark_pool_name"><code>spark_pool_name</code></a></td>
    <td></td>
    <td>Kill a statement within a session.</td>
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
<tr id="parameter-livy_api_version">
    <td><CopyableCode code="livy_api_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>integer</code></td>
    <td>Identifier for the session.</td>
</tr>
<tr id="parameter-spark_pool_name">
    <td><CopyableCode code="spark_pool_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-statement_id">
    <td><CopyableCode code="statement_id" /></td>
    <td><code>integer</code></td>
    <td>Identifier for the statement.</td>
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
    defaultValue="get_spark_statement"
    values={[
        { label: 'get_spark_statement', value: 'get_spark_statement' },
        { label: 'get_spark_session', value: 'get_spark_session' },
        { label: 'get_spark_sessions', value: 'get_spark_sessions' }
    ]}
>
<TabItem value="get_spark_statement">

Gets a single statement within a spark session.

```sql
SELECT
id,
code,
output,
state
FROM azure.synapse_spark.spark_session
WHERE statement_id = '{{ statement_id }}' -- required
AND session_id = '{{ session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND livy_api_version = '{{ livy_api_version }}' -- required
AND spark_pool_name = '{{ spark_pool_name }}' -- required
;
```
</TabItem>
<TabItem value="get_spark_session">

Gets a single spark session.

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
FROM azure.synapse_spark.spark_session
WHERE session_id = '{{ session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND livy_api_version = '{{ livy_api_version }}' -- required
AND spark_pool_name = '{{ spark_pool_name }}' -- required
AND detailed = '{{ detailed }}'
;
```
</TabItem>
<TabItem value="get_spark_sessions">

List all spark sessions which are running under a particular spark pool.

```sql
SELECT
from,
sessions,
total
FROM azure.synapse_spark.spark_session
WHERE endpoint = '{{ endpoint }}' -- required
AND livy_api_version = '{{ livy_api_version }}' -- required
AND spark_pool_name = '{{ spark_pool_name }}' -- required
AND from = '{{ from }}'
AND size = '{{ size }}'
AND detailed = '{{ detailed }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_spark_session"
    values={[
        { label: 'create_spark_session', value: 'create_spark_session' },
        { label: 'create_spark_statement', value: 'create_spark_statement' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_spark_session">

Create new spark session.

```sql
INSERT INTO azure.synapse_spark.spark_session (
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
endpoint,
livy_api_version,
spark_pool_name,
detailed
)
SELECT 
'{{ tags }}',
'{{ artifactId }}',
'{{ name }}' /* required */,
'{{ file }}',
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
'{{ endpoint }}',
'{{ livy_api_version }}',
'{{ spark_pool_name }}',
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
<TabItem value="create_spark_statement">

Create statement within a spark session.

```sql
INSERT INTO azure.synapse_spark.spark_session (
code,
kind,
session_id,
endpoint,
livy_api_version,
spark_pool_name
)
SELECT 
'{{ code }}',
'{{ kind }}',
'{{ session_id }}',
'{{ endpoint }}',
'{{ livy_api_version }}',
'{{ spark_pool_name }}'
RETURNING
id,
code,
output,
state
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: spark_session
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the spark_session resource.
    - name: livy_api_version
      value: "{{ livy_api_version }}"
      description: Required parameter for the spark_session resource.
    - name: spark_pool_name
      value: "{{ spark_pool_name }}"
      description: Required parameter for the spark_session resource.
    - name: session_id
      value: {{ session_id }}
      description: Required parameter for the spark_session resource.
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
    - name: code
      value: "{{ code }}"
    - name: kind
      value: "{{ kind }}"
    - name: detailed
      value: {{ detailed }}
      description: Optional query param specifying whether detailed response is returned beyond plain livy.
      description: Optional query param specifying whether detailed response is returned beyond plain livy.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="cancel_spark_session"
    values={[
        { label: 'cancel_spark_session', value: 'cancel_spark_session' }
    ]}
>
<TabItem value="cancel_spark_session">

Cancels a running spark session.

```sql
DELETE FROM azure.synapse_spark.spark_session
WHERE session_id = '{{ session_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND livy_api_version = '{{ livy_api_version }}' --required
AND spark_pool_name = '{{ spark_pool_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_spark_statements"
    values={[
        { label: 'get_spark_statements', value: 'get_spark_statements' },
        { label: 'reset_spark_session_timeout', value: 'reset_spark_session_timeout' },
        { label: 'cancel_spark_statement', value: 'cancel_spark_statement' }
    ]}
>
<TabItem value="get_spark_statements">

Gets a list of statements within a spark session.

```sql
EXEC azure.synapse_spark.spark_session.get_spark_statements 
@session_id='{{ session_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@livy_api_version='{{ livy_api_version }}' --required, 
@spark_pool_name='{{ spark_pool_name }}' --required
;
```
</TabItem>
<TabItem value="reset_spark_session_timeout">

Sends a keep alive call to the current session to reset the session timeout.

```sql
EXEC azure.synapse_spark.spark_session.reset_spark_session_timeout 
@session_id='{{ session_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@livy_api_version='{{ livy_api_version }}' --required, 
@spark_pool_name='{{ spark_pool_name }}' --required
;
```
</TabItem>
<TabItem value="cancel_spark_statement">

Kill a statement within a session.

```sql
EXEC azure.synapse_spark.spark_session.cancel_spark_statement 
@statement_id='{{ statement_id }}' --required, 
@session_id='{{ session_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@livy_api_version='{{ livy_api_version }}' --required, 
@spark_pool_name='{{ spark_pool_name }}' --required
;
```
</TabItem>
</Tabs>
