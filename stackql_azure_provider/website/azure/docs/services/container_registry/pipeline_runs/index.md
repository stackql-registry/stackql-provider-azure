--- 
title: pipeline_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_runs
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>pipeline_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipeline_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.pipeline_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>The name of the private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a pipeline run. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The request parameters for a pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The response of a pipeline run.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="forceUpdateTag" /></td>
    <td><code>string</code></td>
    <td>How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a pipeline run. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The request parameters for a pipeline run.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The response of a pipeline run.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-pipeline_run_name"><code>pipeline_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the detailed information for a given pipeline run.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the pipeline runs for the specified container registry.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-pipeline_run_name"><code>pipeline_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a pipeline run for a container registry with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-pipeline_run_name"><code>pipeline_run_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a pipeline run from a container registry.</td>
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
<tr id="parameter-pipeline_run_name">
    <td><CopyableCode code="pipeline_run_name" /></td>
    <td><code>string</code></td>
    <td>The name of the pipeline run. Required.</td>
</tr>
<tr id="parameter-registry_name">
    <td><CopyableCode code="registry_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container registry. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the detailed information for a given pipeline run.

```sql
SELECT
id,
name,
forceUpdateTag,
provisioningState,
request,
response,
systemData,
type
FROM azure.container_registry.pipeline_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND pipeline_run_name = '{{ pipeline_run_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the pipeline runs for the specified container registry.

```sql
SELECT
id,
name,
forceUpdateTag,
provisioningState,
request,
response,
systemData,
type
FROM azure.container_registry.pipeline_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a pipeline run for a container registry with the specified parameters.

```sql
INSERT INTO azure.container_registry.pipeline_runs (
properties,
resource_group_name,
registry_name,
pipeline_run_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ registry_name }}',
'{{ pipeline_run_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: pipeline_runs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the pipeline_runs resource.
    - name: registry_name
      value: "{{ registry_name }}"
      description: Required parameter for the pipeline_runs resource.
    - name: pipeline_run_name
      value: "{{ pipeline_run_name }}"
      description: Required parameter for the pipeline_runs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the pipeline_runs resource.
    - name: properties
      description: |
        The properties of a pipeline run.
      value:
        provisioningState: "{{ provisioningState }}"
        request:
          pipelineResourceId: "{{ pipelineResourceId }}"
          artifacts:
            - "{{ artifacts }}"
          source:
            type: "{{ type }}"
            name: "{{ name }}"
          target:
            type: "{{ type }}"
            name: "{{ name }}"
          catalogDigest: "{{ catalogDigest }}"
        response:
          status: "{{ status }}"
          importedArtifacts:
            - "{{ importedArtifacts }}"
          progress:
            percentage: "{{ percentage }}"
          startTime: "{{ startTime }}"
          finishTime: "{{ finishTime }}"
          source:
            type: "{{ type }}"
            uri: "{{ uri }}"
            keyVaultUri: "{{ keyVaultUri }}"
            storageAccessMode: "{{ storageAccessMode }}"
          target:
            type: "{{ type }}"
            uri: "{{ uri }}"
            keyVaultUri: "{{ keyVaultUri }}"
            storageAccessMode: "{{ storageAccessMode }}"
          catalogDigest: "{{ catalogDigest }}"
          trigger:
            sourceTrigger:
              timestamp: "{{ timestamp }}"
          pipelineRunErrorMessage: "{{ pipelineRunErrorMessage }}"
        forceUpdateTag: "{{ forceUpdateTag }}"
`}</CodeBlock>

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

Deletes a pipeline run from a container registry.

```sql
DELETE FROM azure.container_registry.pipeline_runs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND pipeline_run_name = '{{ pipeline_run_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
