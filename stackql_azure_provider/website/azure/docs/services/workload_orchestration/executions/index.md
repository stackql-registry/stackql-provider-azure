--- 
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
  - workload_orchestration
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

Creates, updates, deletes, gets or lists an <code>executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="executions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.workload_orchestration.executions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workflow_version', value: 'list_by_workflow_version' }
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
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="specification" /></td>
    <td><code>object</code></td>
    <td>Execution specification.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of Execution.</td>
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
    <td><CopyableCode code="workflowVersionId" /></td>
    <td><code>string</code></td>
    <td>Workflow version of execution. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workflow_version">

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
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>:vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="specification" /></td>
    <td><code>object</code></td>
    <td>Execution specification.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Status of Execution.</td>
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
    <td><CopyableCode code="workflowVersionId" /></td>
    <td><code>string</code></td>
    <td>Workflow version of execution. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-context_name"><code>context_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-execution_name"><code>execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Execution Resource.</td>
</tr>
<tr>
    <td><a href="#list_by_workflow_version"><CopyableCode code="list_by_workflow_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-context_name"><code>context_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Execution Resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-context_name"><code>context_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-execution_name"><code>execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update Execution Resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-context_name"><code>context_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-execution_name"><code>execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>update an Execution Resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-context_name"><code>context_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-execution_name"><code>execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update Execution Resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-context_name"><code>context_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-execution_name"><code>execution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Execution Resource.</td>
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
<tr id="parameter-context_name">
    <td><CopyableCode code="context_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Context. Required.</td>
</tr>
<tr id="parameter-execution_name">
    <td><CopyableCode code="execution_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Execution. Required.</td>
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
<tr id="parameter-version_name">
    <td><CopyableCode code="version_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workflowVersion. Required.</td>
</tr>
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>Name of the workflow. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workflow_version', value: 'list_by_workflow_version' }
    ]}
>
<TabItem value="get">

Get Execution Resource.

```sql
SELECT
id,
name,
eTag,
extendedLocation,
provisioningState,
specification,
status,
systemData,
type,
workflowVersionId
FROM azure.workload_orchestration.executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND context_name = '{{ context_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND version_name = '{{ version_name }}' -- required
AND execution_name = '{{ execution_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workflow_version">

List Execution Resources.

```sql
SELECT
id,
name,
eTag,
extendedLocation,
provisioningState,
specification,
status,
systemData,
type,
workflowVersionId
FROM azure.workload_orchestration.executions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND context_name = '{{ context_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND version_name = '{{ version_name }}' -- required
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

Create or update Execution Resource.

```sql
INSERT INTO azure.workload_orchestration.executions (
properties,
extendedLocation,
resource_group_name,
context_name,
workflow_name,
version_name,
execution_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ context_name }}',
'{{ workflow_name }}',
'{{ version_name }}',
'{{ execution_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
extendedLocation,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: executions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the executions resource.
    - name: context_name
      value: "{{ context_name }}"
      description: Required parameter for the executions resource.
    - name: workflow_name
      value: "{{ workflow_name }}"
      description: Required parameter for the executions resource.
    - name: version_name
      value: "{{ version_name }}"
      description: Required parameter for the executions resource.
    - name: execution_name
      value: "{{ execution_name }}"
      description: Required parameter for the executions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the executions resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        workflowVersionId: "{{ workflowVersionId }}"
        specification: "{{ specification }}"
        status:
          updateTime: "{{ updateTime }}"
          status: {{ status }}
          statusMessage: "{{ statusMessage }}"
          stageHistory:
            - status: {{ status }}
              statusMessage: "{{ statusMessage }}"
              stage: "{{ stage }}"
              nextstage: "{{ nextstage }}"
              errorMessage: "{{ errorMessage }}"
              isActive: "{{ isActive }}"
              inputs: "{{ inputs }}"
              outputs: "{{ outputs }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        :vartype extended_location: ~azure.mgmt.workloadorchestration.models.ExtendedLocation
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

update an Execution Resource.

```sql
UPDATE azure.workload_orchestration.executions
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND context_name = '{{ context_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND version_name = '{{ version_name }}' --required
AND execution_name = '{{ execution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
extendedLocation,
properties,
systemData,
type;
```
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

Create or update Execution Resource.

```sql
REPLACE azure.workload_orchestration.executions
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND context_name = '{{ context_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND version_name = '{{ version_name }}' --required
AND execution_name = '{{ execution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
extendedLocation,
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

Delete Execution Resource.

```sql
DELETE FROM azure.workload_orchestration.executions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND context_name = '{{ context_name }}' --required
AND workflow_name = '{{ workflow_name }}' --required
AND version_name = '{{ version_name }}' --required
AND execution_name = '{{ execution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
