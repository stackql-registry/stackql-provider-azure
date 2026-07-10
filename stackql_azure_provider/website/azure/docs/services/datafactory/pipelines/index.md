--- 
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - datafactory
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipelines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datafactory.pipelines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_factory', value: 'list_by_factory' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
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
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
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
    <td><CopyableCode code="policy" /></td>
    <td><code>object</code></td>
    <td>Pipeline Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="runDimensions" /></td>
    <td><code>object</code></td>
    <td>Dimensions emitted by Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
<TabItem value="list_by_factory">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
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
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
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
    <td><CopyableCode code="policy" /></td>
    <td><code>object</code></td>
    <td>Pipeline Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="runDimensions" /></td>
    <td><code>object</code></td>
    <td>Dimensions emitted by Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a pipeline.</td>
</tr>
<tr>
    <td><a href="#list_by_factory"><CopyableCode code="list_by_factory" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists pipelines.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a pipeline.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a pipeline.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a pipeline.</td>
</tr>
<tr>
    <td><a href="#create_run"><CopyableCode code="create_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-referencePipelineRunId"><code>referencePipelineRunId</code></a>, <a href="#parameter-isRecovery"><code>isRecovery</code></a>, <a href="#parameter-startActivityName"><code>startActivityName</code></a>, <a href="#parameter-startFromFailure"><code>startFromFailure</code></a></td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>The factory name. Required.</td>
</tr>
<tr id="parameter-pipeline_name">
    <td><CopyableCode code="pipeline_name" /></td>
    <td><code>string</code></td>
    <td>The pipeline name. Required.</td>
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
<tr id="parameter-startFromFailure">
    <td><CopyableCode code="startFromFailure" /></td>
    <td><code>boolean</code></td>
    <td>In recovery mode, if set to true, the rerun will start from failed activities. The property will be used only if startActivityName is not specified. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_factory', value: 'list_by_factory' }
    ]}
>
<TabItem value="get">

Gets a pipeline.

```sql
SELECT
id,
name,
activities,
annotations,
concurrency,
description,
etag,
folder,
parameters,
policy,
runDimensions,
systemData,
type,
variables
FROM azure.datafactory.pipelines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND pipeline_name = '{{ pipeline_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_factory">

Lists pipelines.

```sql
SELECT
id,
name,
activities,
annotations,
concurrency,
description,
etag,
folder,
parameters,
policy,
runDimensions,
systemData,
type,
variables
FROM azure.datafactory.pipelines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a pipeline.

```sql
INSERT INTO azure.datafactory.pipelines (
properties,
resource_group_name,
factory_name,
pipeline_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ factory_name }}',
'{{ pipeline_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: pipelines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the pipelines resource.
    - name: factory_name
      value: "{{ factory_name }}"
      description: Required parameter for the pipelines resource.
    - name: pipeline_name
      value: "{{ pipeline_name }}"
      description: Required parameter for the pipelines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the pipelines resource.
    - name: properties
      description: |
        Properties of the pipeline. Required.
      value:
        description: "{{ description }}"
        activities:
          - name: "{{ name }}"
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
        policy:
          elapsedTimeMetric:
            duration: "{{ duration }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a pipeline.

```sql
REPLACE azure.datafactory.pipelines
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND pipeline_name = '{{ pipeline_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
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

Deletes a pipeline.

```sql
DELETE FROM azure.datafactory.pipelines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND factory_name = '{{ factory_name }}' --required
AND pipeline_name = '{{ pipeline_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_run"
    values={[
        { label: 'create_run', value: 'create_run' }
    ]}
>
<TabItem value="create_run">

Creates a run of a pipeline.

```sql
EXEC azure.datafactory.pipelines.create_run 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@pipeline_name='{{ pipeline_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@referencePipelineRunId='{{ referencePipelineRunId }}', 
@isRecovery={{ isRecovery }}, 
@startActivityName='{{ startActivityName }}', 
@startFromFailure={{ startFromFailure }}
;
```
</TabItem>
</Tabs>
