--- 
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
  - security
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

Creates, updates, deletes, gets or lists an <code>assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data about the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedComponent" /></td>
    <td><code>object</code></td>
    <td>Component item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedStandard" /></td>
    <td><code>object</code></td>
    <td>Standard item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>description of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>display name of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effect" /></td>
    <td><code>string</code></td>
    <td>expected effect of this assignment (Disable/Exempt/etc).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity tag is used for comparing two or more entities from the same requested resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of this assignment as a full ISO date.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data about the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedComponent" /></td>
    <td><code>object</code></td>
    <td>Component item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedStandard" /></td>
    <td><code>object</code></td>
    <td>Standard item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>description of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>display name of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effect" /></td>
    <td><code>string</code></td>
    <td>expected effect of this assignment (Disable/Exempt/etc).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity tag is used for comparing two or more entities from the same requested resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of this assignment as a full ISO date.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data about the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedComponent" /></td>
    <td><code>object</code></td>
    <td>Component item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedStandard" /></td>
    <td><code>object</code></td>
    <td>Standard item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>description of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>display name of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effect" /></td>
    <td><code>string</code></td>
    <td>expected effect of this assignment (Disable/Exempt/etc).</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity tag is used for comparing two or more entities from the same requested resource.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of this assignment as a full ISO date.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-assignment_id"><code>assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a specific standard assignment for the requested scope by resourceId.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all relevant standardAssignments available for scope.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all relevant standardAssignments over a subscription level scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-assignment_id"><code>assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a security assignment on the given scope. Will create/update the required standard assignment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-assignment_id"><code>assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a security assignment on the given scope. Will create/update the required standard assignment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-assignment_id"><code>assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a standard assignment over a given scope.</td>
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
<tr id="parameter-assignment_id">
    <td><CopyableCode code="assignment_id" /></td>
    <td><code>string</code></td>
    <td>The security assignment key - unique key for the standard assignment. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a specific standard assignment for the requested scope by resourceId.

```sql
SELECT
id,
name,
additionalData,
assignedComponent,
assignedStandard,
description,
displayName,
effect,
etag,
expiresOn,
kind,
location,
metadata,
scope,
systemData,
tags,
type
FROM azure.security.assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND assignment_id = '{{ assignment_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all relevant standardAssignments available for scope.

```sql
SELECT
id,
name,
additionalData,
assignedComponent,
assignedStandard,
description,
displayName,
effect,
etag,
expiresOn,
kind,
location,
metadata,
scope,
systemData,
tags,
type
FROM azure.security.assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get a list of all relevant standardAssignments over a subscription level scope.

```sql
SELECT
id,
name,
additionalData,
assignedComponent,
assignedStandard,
description,
displayName,
effect,
etag,
expiresOn,
kind,
location,
metadata,
scope,
systemData,
tags,
type
FROM azure.security.assignments
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

Create a security assignment on the given scope. Will create/update the required standard assignment.

```sql
INSERT INTO azure.security.assignments (
properties,
tags,
location,
kind,
etag,
resource_group_name,
assignment_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ kind }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ assignment_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: assignments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the assignments resource.
    - name: assignment_id
      value: "{{ assignment_id }}"
      description: Required parameter for the assignments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the assignments resource.
    - name: properties
      description: |
        Properties of a security assignment.
      value:
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        assignedStandard:
          id: "{{ id }}"
        assignedComponent:
          key: "{{ key }}"
        scope: "{{ scope }}"
        effect: "{{ effect }}"
        expiresOn: "{{ expiresOn }}"
        additionalData:
          exemptionCategory: "{{ exemptionCategory }}"
        metadata: "{{ metadata }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of the resource.
    - name: etag
      value: "{{ etag }}"
      description: |
        Entity tag is used for comparing two or more entities from the same requested resource.
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

Create a security assignment on the given scope. Will create/update the required standard assignment.

```sql
REPLACE azure.security.assignments
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
kind = '{{ kind }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND assignment_id = '{{ assignment_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
systemData,
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

Delete a standard assignment over a given scope.

```sql
DELETE FROM azure.security.assignments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND assignment_id = '{{ assignment_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
