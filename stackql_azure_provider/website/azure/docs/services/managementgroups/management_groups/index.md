--- 
title: management_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - management_groups
  - managementgroups
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

Creates, updates, deletes, gets or lists a <code>management_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="management_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managementgroups.management_groups" /></td></tr>
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
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="children" /></td>
    <td><code>array</code></td>
    <td>The list of children.</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>The details of a management group.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the management group.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000.</td>
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
    <td>The fully qualified ID for the management group. For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the management group. For example, 00000000-0000-0000-0000-000000000000.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the management group.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. For example, Microsoft.Management/managementGroups.</td>
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
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$recurse"><code>$recurse</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Get the details of the management group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>List management groups for the authenticated user.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Update a management group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Delete management group. If a management group contains child resources, the request will fail.</td>
</tr>
<tr>
    <td><a href="#get_descendants"><CopyableCode code="get_descendants" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List all entities that descend from a management group.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>Management Group ID. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The $expand=children query string parameter allows clients to request inclusion of children in the response payload. $expand=path includes the path from the root group to the current group. $expand=ancestors includes the ancestor Ids of the current group. Known values are: "children", "path", and "ancestors". Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>A filter which allows the exclusion of subscriptions from results (i.e. '$filter=children.childType ne Subscription'). Default value is None.</td>
</tr>
<tr id="parameter-$recurse">
    <td><CopyableCode code="$recurse" /></td>
    <td><code>boolean</code></td>
    <td>The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. Note that $expand=children must be passed up if $recurse is set to true. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Passing this in will override $skipToken. Default value is None.</td>
</tr>
<tr id="parameter-Cache-Control">
    <td><CopyableCode code="Cache-Control" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".</td>
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

Get the details of the management group.

```sql
SELECT
id,
name,
children,
details,
displayName,
systemData,
tenantId,
type
FROM azure.managementgroups.management_groups
WHERE group_id = '{{ group_id }}' -- required
AND $expand = '{{ $expand }}'
AND $recurse = '{{ $recurse }}'
AND $filter = '{{ $filter }}'
AND Cache-Control = '{{ Cache-Control }}'
;
```
</TabItem>
<TabItem value="list">

List management groups for the authenticated user.

```sql
SELECT
id,
name,
displayName,
tenantId,
type
FROM azure.managementgroups.management_groups
WHERE Cache-Control = '{{ Cache-Control }}'
AND $skiptoken = '{{ $skiptoken }}'
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

Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.

```sql
INSERT INTO azure.managementgroups.management_groups (
name,
properties,
group_id,
Cache-Control
)
SELECT 
'{{ name }}',
'{{ properties }}',
'{{ group_id }}',
'{{ Cache-Control }}'
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
- name: management_groups
  props:
    - name: group_id
      value: "{{ group_id }}"
      description: Required parameter for the management_groups resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the management group. For example, 00000000-0000-0000-0000-000000000000.
    - name: properties
      description: |
        The generic properties of a management group used during creation.
      value:
        tenantId: "{{ tenantId }}"
        displayName: "{{ displayName }}"
        details:
          version: {{ version }}
          updatedTime: "{{ updatedTime }}"
          updatedBy: "{{ updatedBy }}"
          parent:
            id: "{{ id }}"
            name: "{{ name }}"
            displayName: "{{ displayName }}"
        children:
          - type: "{{ type }}"
            id: "{{ id }}"
            name: "{{ name }}"
            displayName: "{{ displayName }}"
            children: "{{ children }}"
    - name: Cache-Control
      value: "{{ Cache-Control }}"
      description: Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
      description: Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
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

Update a management group.

```sql
UPDATE azure.managementgroups.management_groups
SET 
displayName = '{{ displayName }}',
parentGroupId = '{{ parentGroupId }}'
WHERE 
group_id = '{{ group_id }}' --required
AND Cache-Control = '{{ Cache-Control}}'
RETURNING
id,
name,
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

Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated.

```sql
REPLACE azure.managementgroups.management_groups
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
group_id = '{{ group_id }}' --required
AND Cache-Control = '{{ Cache-Control}}'
RETURNING
id,
name,
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

Delete management group. If a management group contains child resources, the request will fail.

```sql
DELETE FROM azure.managementgroups.management_groups
WHERE group_id = '{{ group_id }}' --required
AND Cache-Control = '{{ Cache-Control }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_descendants"
    values={[
        { label: 'get_descendants', value: 'get_descendants' }
    ]}
>
<TabItem value="get_descendants">

List all entities that descend from a management group.

```sql
EXEC azure.managementgroups.management_groups.get_descendants 
@group_id='{{ group_id }}' --required, 
@$skiptoken='{{ $skiptoken }}', 
@$top='{{ $top }}'
;
```
</TabItem>
</Tabs>
