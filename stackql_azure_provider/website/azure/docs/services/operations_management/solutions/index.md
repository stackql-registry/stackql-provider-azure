--- 
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - operations_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.solutions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="containedResources" /></td>
    <td><code>array</code></td>
    <td>The azure resources that will be contained within the solutions. They will be locked and gets deleted automatically when the solution is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for solution object supported by the OperationsManagement resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state for the solution.</td>
</tr>
<tr>
    <td><CopyableCode code="referencedResources" /></td>
    <td><code>array</code></td>
    <td>The resources that will be referenced from this solution. Deleting any of those solution out of band will break the solution.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceResourceId" /></td>
    <td><code>string</code></td>
    <td>The azure resourceId for the workspace where the solution will be deployed/enabled. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="containedResources" /></td>
    <td><code>array</code></td>
    <td>The azure resources that will be contained within the solutions. They will be locked and gets deleted automatically when the solution is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for solution object supported by the OperationsManagement resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state for the solution.</td>
</tr>
<tr>
    <td><CopyableCode code="referencedResources" /></td>
    <td><code>array</code></td>
    <td>The resources that will be referenced from this solution. Deleting any of those solution out of band will break the solution.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceResourceId" /></td>
    <td><code>string</code></td>
    <td>The azure resourceId for the workspace where the solution will be deployed/enabled. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="containedResources" /></td>
    <td><code>array</code></td>
    <td>The azure resources that will be contained within the solutions. They will be locked and gets deleted automatically when the solution is deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for solution object supported by the OperationsManagement resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state for the solution.</td>
</tr>
<tr>
    <td><CopyableCode code="referencedResources" /></td>
    <td><code>array</code></td>
    <td>The resources that will be referenced from this solution. Deleting any of those solution out of band will break the solution.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceResourceId" /></td>
    <td><code>string</code></td>
    <td>The azure resourceId for the workspace where the solution will be deployed/enabled. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve solution. Retrieves the user solution.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the solution list for the subscription. Retrieves the solution list. It will retrieve both first party and third party solutions.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the solution list for the subscription. Retrieves the solution list. It will retrieve both first party and third party solutions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create/Update Solution. Creates or updates the Solution.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a Solution. Patch a Solution. Only updating tags supported.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create/Update Solution. Creates or updates the Solution.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the solution. Deletes the solution in the subscription.</td>
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
    <td>The name of the resource group to get. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-solution_name">
    <td><CopyableCode code="solution_name" /></td>
    <td><code>string</code></td>
    <td>User Solution Name. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieve solution. Retrieves the user solution.

```sql
SELECT
id,
name,
containedResources,
location,
plan,
provisioningState,
referencedResources,
tags,
type,
workspaceResourceId
FROM azure.operations_management.solutions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND solution_name = '{{ solution_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieves the solution list for the subscription. Retrieves the solution list. It will retrieve both first party and third party solutions.

```sql
SELECT
id,
name,
containedResources,
location,
plan,
provisioningState,
referencedResources,
tags,
type,
workspaceResourceId
FROM azure.operations_management.solutions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieves the solution list for the subscription. Retrieves the solution list. It will retrieve both first party and third party solutions.

```sql
SELECT
id,
name,
containedResources,
location,
plan,
provisioningState,
referencedResources,
tags,
type,
workspaceResourceId
FROM azure.operations_management.solutions
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create/Update Solution. Creates or updates the Solution.

```sql
INSERT INTO azure.operations_management.solutions (
location,
tags,
plan,
properties,
resource_group_name,
solution_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ plan }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ solution_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
plan,
properties,
tags,
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
    - name: solution_name
      value: "{{ solution_name }}"
      description: Required parameter for the solutions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the solutions resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: plan
      description: |
        Plan for solution object supported by the OperationsManagement resource provider.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        promotionCode: "{{ promotionCode }}"
        product: "{{ product }}"
    - name: properties
      description: |
        Properties for solution object supported by the OperationsManagement resource provider.
      value:
        workspaceResourceId: "{{ workspaceResourceId }}"
        provisioningState: "{{ provisioningState }}"
        containedResources:
          - "{{ containedResources }}"
        referencedResources:
          - "{{ referencedResources }}"
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

Patch a Solution. Patch a Solution. Only updating tags supported.

```sql
UPDATE azure.operations_management.solutions
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND solution_name = '{{ solution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
plan,
properties,
tags,
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

Create/Update Solution. Creates or updates the Solution.

```sql
REPLACE azure.operations_management.solutions
SET 
location = '{{ location }}',
tags = '{{ tags }}',
plan = '{{ plan }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND solution_name = '{{ solution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
plan,
properties,
tags,
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

Deletes the solution. Deletes the solution in the subscription.

```sql
DELETE FROM azure.operations_management.solutions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND solution_name = '{{ solution_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
