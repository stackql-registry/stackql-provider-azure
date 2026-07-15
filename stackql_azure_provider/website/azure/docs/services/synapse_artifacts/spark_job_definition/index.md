--- 
title: spark_job_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - spark_job_definition
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

Creates, updates, deletes, gets or lists a <code>spark_job_definition</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="spark_job_definition" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.spark_job_definition" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_spark_job_definition"
    values={[
        { label: 'get_spark_job_definition', value: 'get_spark_job_definition' },
        { label: 'get_spark_job_definitions_by_workspace', value: 'get_spark_job_definitions_by_workspace' }
    ]}
>
<TabItem value="get_spark_job_definition">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the Spark job definition.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this Spark job definition is in. If not specified, this Spark job definition will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="jobProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of the Spark job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>The language of the Spark application.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredSparkVersion" /></td>
    <td><code>string</code></td>
    <td>The required Spark version of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="targetBigDataPool" /></td>
    <td><code>object</code></td>
    <td>Big data pool reference. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSparkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The spark configuration of the spark job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_spark_job_definitions_by_workspace">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the Spark job definition.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this Spark job definition is in. If not specified, this Spark job definition will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="jobProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of the Spark job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>The language of the Spark application.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredSparkVersion" /></td>
    <td><code>string</code></td>
    <td>The required Spark version of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="targetBigDataPool" /></td>
    <td><code>object</code></td>
    <td>Big data pool reference. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSparkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The spark configuration of the spark job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_spark_job_definition"><CopyableCode code="get_spark_job_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-spark_job_definition_name"><code>spark_job_definition_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a Spark Job Definition.</td>
</tr>
<tr>
    <td><a href="#get_spark_job_definitions_by_workspace"><CopyableCode code="get_spark_job_definitions_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists spark job definitions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_spark_job_definition"><CopyableCode code="create_or_update_spark_job_definition" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-spark_job_definition_name"><code>spark_job_definition_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetBigDataPool"><code>targetBigDataPool</code></a>, <a href="#parameter-jobProperties"><code>jobProperties</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a Spark Job Definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update_spark_job_definition"><CopyableCode code="create_or_update_spark_job_definition" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-spark_job_definition_name"><code>spark_job_definition_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetBigDataPool"><code>targetBigDataPool</code></a>, <a href="#parameter-jobProperties"><code>jobProperties</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a Spark Job Definition.</td>
</tr>
<tr>
    <td><a href="#delete_spark_job_definition"><CopyableCode code="delete_spark_job_definition" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-spark_job_definition_name"><code>spark_job_definition_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a Spark Job Definition.</td>
</tr>
<tr>
    <td><a href="#execute_spark_job_definition"><CopyableCode code="execute_spark_job_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-spark_job_definition_name"><code>spark_job_definition_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Executes the spark job definition.</td>
</tr>
<tr>
    <td><a href="#rename_spark_job_definition"><CopyableCode code="rename_spark_job_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-spark_job_definition_name"><code>spark_job_definition_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a sparkJobDefinition.</td>
</tr>
<tr>
    <td><a href="#debug_spark_job_definition"><CopyableCode code="debug_spark_job_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetBigDataPool"><code>targetBigDataPool</code></a>, <a href="#parameter-jobProperties"><code>jobProperties</code></a></td>
    <td></td>
    <td>Debug the spark job definition.</td>
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
<tr id="parameter-spark_job_definition_name">
    <td><CopyableCode code="spark_job_definition_name" /></td>
    <td><code>string</code></td>
    <td>The spark job definition name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the Spark Job Definition entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the Spark Job Definition entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_spark_job_definition"
    values={[
        { label: 'get_spark_job_definition', value: 'get_spark_job_definition' },
        { label: 'get_spark_job_definitions_by_workspace', value: 'get_spark_job_definitions_by_workspace' }
    ]}
>
<TabItem value="get_spark_job_definition">

Gets a Spark Job Definition.

```sql
SELECT
id,
name,
,
description,
etag,
folder,
jobProperties,
language,
requiredSparkVersion,
targetBigDataPool,
targetSparkConfiguration,
type
FROM azure.synapse_artifacts.spark_job_definition
WHERE spark_job_definition_name = '{{ spark_job_definition_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_spark_job_definitions_by_workspace">

Lists spark job definitions.

```sql
SELECT
id,
name,
,
description,
etag,
folder,
jobProperties,
language,
requiredSparkVersion,
targetBigDataPool,
targetSparkConfiguration,
type
FROM azure.synapse_artifacts.spark_job_definition
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_spark_job_definition"
    values={[
        { label: 'create_or_update_spark_job_definition', value: 'create_or_update_spark_job_definition' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_spark_job_definition">

Creates or updates a Spark Job Definition.

```sql
INSERT INTO azure.synapse_artifacts.spark_job_definition (
,
description,
targetBigDataPool,
targetSparkConfiguration,
requiredSparkVersion,
language,
jobProperties,
folder,
spark_job_definition_name,
endpoint,
If-Match
)
SELECT 
'{{  }}',
'{{ description }}',
'{{ targetBigDataPool }}' /* required */,
'{{ targetSparkConfiguration }}',
'{{ requiredSparkVersion }}',
'{{ language }}',
'{{ jobProperties }}' /* required */,
'{{ folder }}',
'{{ spark_job_definition_name }}',
'{{ endpoint }}',
'{{ If-Match }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: spark_job_definition
  props:
    - name: spark_job_definition_name
      value: "{{ spark_job_definition_name }}"
      description: Required parameter for the spark_job_definition resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the spark_job_definition resource.
    - name: 
      value: "{{  }}"
      description: |
        Unmatched properties from the message are deserialized to this collection.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the Spark job definition.
    - name: targetBigDataPool
      description: |
        Big data pool reference. Required.
      value:
        type: "{{ type }}"
        referenceName: "{{ referenceName }}"
    - name: targetSparkConfiguration
      description: |
        The spark configuration of the spark job.
      value:
        type: "{{ type }}"
        referenceName: "{{ referenceName }}"
    - name: requiredSparkVersion
      value: "{{ requiredSparkVersion }}"
      description: |
        The required Spark version of the application.
    - name: language
      value: "{{ language }}"
      description: |
        The language of the Spark application.
    - name: jobProperties
      description: |
        The properties of the Spark job. Required.
      value:
        : "{{  }}"
        name: "{{ name }}"
        file: "{{ file }}"
        className: "{{ className }}"
        conf: "{{ conf }}"
        args:
          - "{{ args }}"
        jars:
          - "{{ jars }}"
        files:
          - "{{ files }}"
        archives:
          - "{{ archives }}"
        driverMemory: "{{ driverMemory }}"
        driverCores: {{ driverCores }}
        executorMemory: "{{ executorMemory }}"
        executorCores: {{ executorCores }}
        numExecutors: {{ numExecutors }}
    - name: folder
      description: |
        The folder that this Spark job definition is in. If not specified, this Spark job definition will appear at the root level.
      value:
        name: "{{ name }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the Spark Job Definition entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the Spark Job Definition entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_spark_job_definition"
    values={[
        { label: 'create_or_update_spark_job_definition', value: 'create_or_update_spark_job_definition' }
    ]}
>
<TabItem value="create_or_update_spark_job_definition">

Creates or updates a Spark Job Definition.

```sql
REPLACE azure.synapse_artifacts.spark_job_definition
SET 
 = '{{  }}',
description = '{{ description }}',
targetBigDataPool = '{{ targetBigDataPool }}',
targetSparkConfiguration = '{{ targetSparkConfiguration }}',
requiredSparkVersion = '{{ requiredSparkVersion }}',
language = '{{ language }}',
jobProperties = '{{ jobProperties }}',
folder = '{{ folder }}'
WHERE 
spark_job_definition_name = '{{ spark_job_definition_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND targetBigDataPool = '{{ targetBigDataPool }}' --required
AND jobProperties = '{{ jobProperties }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_spark_job_definition"
    values={[
        { label: 'delete_spark_job_definition', value: 'delete_spark_job_definition' }
    ]}
>
<TabItem value="delete_spark_job_definition">

Deletes a Spark Job Definition.

```sql
DELETE FROM azure.synapse_artifacts.spark_job_definition
WHERE spark_job_definition_name = '{{ spark_job_definition_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute_spark_job_definition"
    values={[
        { label: 'execute_spark_job_definition', value: 'execute_spark_job_definition' },
        { label: 'rename_spark_job_definition', value: 'rename_spark_job_definition' },
        { label: 'debug_spark_job_definition', value: 'debug_spark_job_definition' }
    ]}
>
<TabItem value="execute_spark_job_definition">

Executes the spark job definition.

```sql
EXEC azure.synapse_artifacts.spark_job_definition.execute_spark_job_definition 
@spark_job_definition_name='{{ spark_job_definition_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="rename_spark_job_definition">

Renames a sparkJobDefinition.

```sql
EXEC azure.synapse_artifacts.spark_job_definition.rename_spark_job_definition 
@spark_job_definition_name='{{ spark_job_definition_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="debug_spark_job_definition">

Debug the spark job definition.

```sql
EXEC azure.synapse_artifacts.spark_job_definition.debug_spark_job_definition 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"": "{{  }}", 
"description": "{{ description }}", 
"targetBigDataPool": "{{ targetBigDataPool }}", 
"targetSparkConfiguration": "{{ targetSparkConfiguration }}", 
"requiredSparkVersion": "{{ requiredSparkVersion }}", 
"language": "{{ language }}", 
"jobProperties": "{{ jobProperties }}", 
"folder": "{{ folder }}"
}'
;
```
</TabItem>
</Tabs>
