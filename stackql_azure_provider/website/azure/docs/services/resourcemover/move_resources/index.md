--- 
title: move_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - move_resources
  - resourcemover
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

Creates, updates, deletes, gets or lists a <code>move_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="move_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resourcemover.move_resources" /></td></tr>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOn" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the move resource dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOnOverrides" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the move resource dependencies overrides.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the move resource errors.</td>
</tr>
<tr>
    <td><CopyableCode code="existingTargetId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the existing target ARM Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isResolveRequired" /></td>
    <td><code>boolean</code></td>
    <td>Gets a value indicating whether the resolve action is required over the move collection.</td>
</tr>
<tr>
    <td><CopyableCode code="moveStatus" /></td>
    <td><code>object</code></td>
    <td>Defines the move resource status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSettings" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the resource settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Source ARM Id of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceSettings" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the source resource settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Target ARM Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOn" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the move resource dependencies.</td>
</tr>
<tr>
    <td><CopyableCode code="dependsOnOverrides" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the move resource dependencies overrides.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the move resource errors.</td>
</tr>
<tr>
    <td><CopyableCode code="existingTargetId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the existing target ARM Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isResolveRequired" /></td>
    <td><code>boolean</code></td>
    <td>Gets a value indicating whether the resolve action is required over the move collection.</td>
</tr>
<tr>
    <td><CopyableCode code="moveStatus" /></td>
    <td><code>object</code></td>
    <td>Defines the move resource status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSettings" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the resource settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Source ARM Id of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceSettings" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the source resource settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Target ARM Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-move_resource_name"><code>move_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Move Resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists the Move Resources in the move collection.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-move_resource_name"><code>move_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Move Resource in the move collection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-move_collection_name"><code>move_collection_name</code></a>, <a href="#parameter-move_resource_name"><code>move_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Move Resource from the move collection.</td>
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
<tr id="parameter-move_collection_name">
    <td><CopyableCode code="move_collection_name" /></td>
    <td><code>string</code></td>
    <td>The Move Collection Name. Required.</td>
</tr>
<tr id="parameter-move_resource_name">
    <td><CopyableCode code="move_resource_name" /></td>
    <td><code>string</code></td>
    <td>The Move Resource Name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The Resource Group Name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. For example, you can use $filter=Properties/ProvisioningState eq 'Succeeded'. Default value is None.</td>
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

Gets the Move Resource.

```sql
SELECT
id,
name,
dependsOn,
dependsOnOverrides,
errors,
existingTargetId,
isResolveRequired,
moveStatus,
provisioningState,
resourceSettings,
sourceId,
sourceResourceSettings,
systemData,
targetId,
type
FROM azure.resourcemover.move_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND move_collection_name = '{{ move_collection_name }}' -- required
AND move_resource_name = '{{ move_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the Move Resources in the move collection.

```sql
SELECT
id,
name,
dependsOn,
dependsOnOverrides,
errors,
existingTargetId,
isResolveRequired,
moveStatus,
provisioningState,
resourceSettings,
sourceId,
sourceResourceSettings,
systemData,
targetId,
type
FROM azure.resourcemover.move_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND move_collection_name = '{{ move_collection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Creates or updates a Move Resource in the move collection.

```sql
INSERT INTO azure.resourcemover.move_resources (
properties,
resource_group_name,
move_collection_name,
move_resource_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ move_collection_name }}',
'{{ move_resource_name }}',
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
- name: move_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the move_resources resource.
    - name: move_collection_name
      value: "{{ move_collection_name }}"
      description: Required parameter for the move_resources resource.
    - name: move_resource_name
      value: "{{ move_resource_name }}"
      description: Required parameter for the move_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the move_resources resource.
    - name: properties
      description: |
        Defines the move resource properties.
      value:
        provisioningState: "{{ provisioningState }}"
        sourceId: "{{ sourceId }}"
        targetId: "{{ targetId }}"
        existingTargetId: "{{ existingTargetId }}"
        resourceSettings:
          resourceType: "{{ resourceType }}"
          targetResourceName: "{{ targetResourceName }}"
          targetResourceGroupName: "{{ targetResourceGroupName }}"
        sourceResourceSettings:
          resourceType: "{{ resourceType }}"
          targetResourceName: "{{ targetResourceName }}"
          targetResourceGroupName: "{{ targetResourceGroupName }}"
        moveStatus:
          moveState: "{{ moveState }}"
          jobStatus:
            jobName: "{{ jobName }}"
            jobProgress: "{{ jobProgress }}"
          errors:
            properties:
              code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details:
                - code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
        dependsOn:
          - id: "{{ id }}"
            resolutionStatus: "{{ resolutionStatus }}"
            resolutionType: "{{ resolutionType }}"
            dependencyType: "{{ dependencyType }}"
            manualResolution:
              targetId: "{{ targetId }}"
            automaticResolution:
              moveResourceId: "{{ moveResourceId }}"
            isOptional: "{{ isOptional }}"
        dependsOnOverrides:
          - id: "{{ id }}"
            targetId: "{{ targetId }}"
        isResolveRequired: {{ isResolveRequired }}
        errors:
          properties:
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                target: "{{ target }}"
                details: "{{ details }}"
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

Deletes a Move Resource from the move collection.

```sql
DELETE FROM azure.resourcemover.move_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND move_collection_name = '{{ move_collection_name }}' --required
AND move_resource_name = '{{ move_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
