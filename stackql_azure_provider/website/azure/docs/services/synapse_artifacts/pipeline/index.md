--- 
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
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

Creates, updates, deletes, gets or lists a <code>pipeline</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.pipeline" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_pipeline"
    values={[
        { label: 'get_pipeline', value: 'get_pipeline' },
        { label: 'get_pipelines_by_workspace', value: 'get_pipelines_by_workspace' }
    ]}
>
<TabItem value="get_pipeline">

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
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>List of activities in pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="concurrency" /></td>
    <td><code>integer</code></td>
    <td>The max number of concurrent runs for the pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this Pipeline is in. If not specified, Pipeline will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>List of parameters for pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="runDimensions" /></td>
    <td><code>object</code></td>
    <td>Dimensions emitted by Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="variables" /></td>
    <td><code>object</code></td>
    <td>List of variables for pipeline.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_pipelines_by_workspace">

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
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>List of activities in pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="concurrency" /></td>
    <td><code>integer</code></td>
    <td>The max number of concurrent runs for the pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this Pipeline is in. If not specified, Pipeline will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>List of parameters for pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="runDimensions" /></td>
    <td><code>object</code></td>
    <td>Dimensions emitted by Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="variables" /></td>
    <td><code>object</code></td>
    <td>List of variables for pipeline.</td>
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
    <td><a href="#get_pipeline"><CopyableCode code="get_pipeline" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a pipeline.</td>
</tr>
<tr>
    <td><a href="#get_pipelines_by_workspace"><CopyableCode code="get_pipelines_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists pipelines.</td>
</tr>
<tr>
    <td><a href="#create_or_update_pipeline"><CopyableCode code="create_or_update_pipeline" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a pipeline.</td>
</tr>
<tr>
    <td><a href="#create_or_update_pipeline"><CopyableCode code="create_or_update_pipeline" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a pipeline.</td>
</tr>
<tr>
    <td><a href="#delete_pipeline"><CopyableCode code="delete_pipeline" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a pipeline.</td>
</tr>
<tr>
    <td><a href="#rename_pipeline"><CopyableCode code="rename_pipeline" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a pipeline.</td>
</tr>
<tr>
    <td><a href="#create_pipeline_run"><CopyableCode code="create_pipeline_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-referencePipelineRunId"><code>referencePipelineRunId</code></a>, <a href="#parameter-isRecovery"><code>isRecovery</code></a>, <a href="#parameter-startActivityName"><code>startActivityName</code></a></td>
    <td>Creates a run of a pipeline.</td>
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
<tr id="parameter-pipeline_name">
    <td><CopyableCode code="pipeline_name" /></td>
    <td><code>string</code></td>
    <td>The pipeline name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the pipeline entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the pipeline entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
<tr id="parameter-isRecovery">
    <td><CopyableCode code="isRecovery" /></td>
    <td><code>boolean</code></td>
    <td>Recovery mode flag. If recovery mode is set to true, the specified referenced pipeline run and the new run will be grouped under the same groupId. Default value is None.</td>
</tr>
<tr id="parameter-referencePipelineRunId">
    <td><CopyableCode code="referencePipelineRunId" /></td>
    <td><code>string</code></td>
    <td>The pipeline run identifier. If run ID is specified the parameters of the specified run will be used to create a new run. Default value is None.</td>
</tr>
<tr id="parameter-startActivityName">
    <td><CopyableCode code="startActivityName" /></td>
    <td><code>string</code></td>
    <td>In recovery mode, the rerun will start from this activity. If not specified, all activities will run. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_pipeline"
    values={[
        { label: 'get_pipeline', value: 'get_pipeline' },
        { label: 'get_pipelines_by_workspace', value: 'get_pipelines_by_workspace' }
    ]}
>
<TabItem value="get_pipeline">

Gets a pipeline.

```sql
SELECT
id,
name,
,
activities,
annotations,
concurrency,
description,
etag,
folder,
parameters,
runDimensions,
type,
variables
FROM azure.synapse_artifacts.pipeline
WHERE pipeline_name = '{{ pipeline_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_pipelines_by_workspace">

Lists pipelines.

```sql
SELECT
id,
name,
,
activities,
annotations,
concurrency,
description,
etag,
folder,
parameters,
runDimensions,
type,
variables
FROM azure.synapse_artifacts.pipeline
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_pipeline"
    values={[
        { label: 'create_or_update_pipeline', value: 'create_or_update_pipeline' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_pipeline">

Creates or updates a pipeline.

```sql
INSERT INTO azure.synapse_artifacts.pipeline (
,
properties,
pipeline_name,
endpoint,
If-Match
)
SELECT 
'{{  }}',
'{{ properties }}',
'{{ pipeline_name }}',
'{{ endpoint }}',
'{{ If-Match }}'
RETURNING
id,
name,
,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: pipeline
  props:
    - name: pipeline_name
      value: "{{ pipeline_name }}"
      description: Required parameter for the pipeline resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the pipeline resource.
    - name: 
      value: "{{  }}"
      description: |
        Unmatched properties from the message are deserialized to this collection.
    - name: properties
      value:
        description: "{{ description }}"
        activities:
          - : "{{  }}"
            name: "{{ name }}"
            type: "{{ type }}"
            description: "{{ description }}"
            state: "{{ state }}"
            onInactiveMarkAs: "{{ onInactiveMarkAs }}"
            dependsOn: "{{ dependsOn }}"
            userProperties: "{{ userProperties }}"
        parameters: "{{ parameters }}"
        variables: "{{ variables }}"
        concurrency: {{ concurrency }}
        annotations: "{{ annotations }}"
        runDimensions: "{{ runDimensions }}"
        folder:
          name: "{{ name }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the pipeline entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the pipeline entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_pipeline"
    values={[
        { label: 'create_or_update_pipeline', value: 'create_or_update_pipeline' }
    ]}
>
<TabItem value="create_or_update_pipeline">

Creates or updates a pipeline.

```sql
REPLACE azure.synapse_artifacts.pipeline
SET 
 = '{{  }}',
properties = '{{ properties }}'
WHERE 
pipeline_name = '{{ pipeline_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
,
etag,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_pipeline"
    values={[
        { label: 'delete_pipeline', value: 'delete_pipeline' }
    ]}
>
<TabItem value="delete_pipeline">

Deletes a pipeline.

```sql
DELETE FROM azure.synapse_artifacts.pipeline
WHERE pipeline_name = '{{ pipeline_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_pipeline"
    values={[
        { label: 'rename_pipeline', value: 'rename_pipeline' },
        { label: 'create_pipeline_run', value: 'create_pipeline_run' }
    ]}
>
<TabItem value="rename_pipeline">

Renames a pipeline.

```sql
EXEC azure.synapse_artifacts.pipeline.rename_pipeline 
@pipeline_name='{{ pipeline_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_pipeline_run">

Creates a run of a pipeline.

```sql
EXEC azure.synapse_artifacts.pipeline.create_pipeline_run 
@pipeline_name='{{ pipeline_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@referencePipelineRunId='{{ referencePipelineRunId }}', 
@isRecovery={{ isRecovery }}, 
@startActivityName='{{ startActivityName }}'
;
```
</TabItem>
</Tabs>
