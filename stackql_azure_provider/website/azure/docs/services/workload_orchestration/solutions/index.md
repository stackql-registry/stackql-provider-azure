--- 
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
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

Creates, updates, deletes, gets or lists a <code>solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="solutions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.workload_orchestration.solutions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_target', value: 'list_by_target' }
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
    <td><CopyableCode code="availableSolutionTemplateVersions" /></td>
    <td><code>array</code></td>
    <td>List of latest revisions for available solution template versions.</td>
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
    <td><CopyableCode code="solutionTemplateId" /></td>
    <td><code>string</code></td>
    <td>Solution template Id.</td>
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
<TabItem value="list_by_target">

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
    <td><CopyableCode code="availableSolutionTemplateVersions" /></td>
    <td><code>array</code></td>
    <td>List of latest revisions for available solution template versions.</td>
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
    <td><CopyableCode code="solutionTemplateId" /></td>
    <td><code>string</code></td>
    <td>Solution template Id.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Solution resource.</td>
</tr>
<tr>
    <td><a href="#list_by_target"><CopyableCode code="list_by_target" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Solution resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Solution Resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Solution Resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Solution Resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_name"><code>target_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Solution Resource.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-solution_name">
    <td><CopyableCode code="solution_name" /></td>
    <td><code>string</code></td>
    <td>Name of the solution. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-target_name">
    <td><CopyableCode code="target_name" /></td>
    <td><code>string</code></td>
    <td>Name of the target. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_target', value: 'list_by_target' }
    ]}
>
<TabItem value="get">

Get a Solution resource.

```sql
SELECT
id,
name,
availableSolutionTemplateVersions,
eTag,
extendedLocation,
provisioningState,
solutionTemplateId,
systemData,
type
FROM azure.workload_orchestration.solutions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND target_name = '{{ target_name }}' -- required
AND solution_name = '{{ solution_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_target">

List Solution resources.

```sql
SELECT
id,
name,
availableSolutionTemplateVersions,
eTag,
extendedLocation,
provisioningState,
solutionTemplateId,
systemData,
type
FROM azure.workload_orchestration.solutions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND target_name = '{{ target_name }}' -- required
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

Create or update a Solution Resource.

```sql
INSERT INTO azure.workload_orchestration.solutions (
properties,
extendedLocation,
resource_group_name,
target_name,
solution_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ target_name }}',
'{{ solution_name }}',
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
- name: solutions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the solutions resource.
    - name: target_name
      value: "{{ target_name }}"
      description: Required parameter for the solutions resource.
    - name: solution_name
      value: "{{ solution_name }}"
      description: Required parameter for the solutions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the solutions resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        solutionTemplateId: "{{ solutionTemplateId }}"
        availableSolutionTemplateVersions:
          - solutionTemplateVersion: "{{ solutionTemplateVersion }}"
            latestConfigRevision: "{{ latestConfigRevision }}"
            isConfigured: {{ isConfigured }}
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

Update a Solution Resource.

```sql
UPDATE azure.workload_orchestration.solutions
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND target_name = '{{ target_name }}' --required
AND solution_name = '{{ solution_name }}' --required
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

Create or update a Solution Resource.

```sql
REPLACE azure.workload_orchestration.solutions
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND target_name = '{{ target_name }}' --required
AND solution_name = '{{ solution_name }}' --required
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

Delete a Solution Resource.

```sql
DELETE FROM azure.workload_orchestration.solutions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND target_name = '{{ target_name }}' --required
AND solution_name = '{{ solution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
