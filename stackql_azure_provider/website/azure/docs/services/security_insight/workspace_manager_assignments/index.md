--- 
title: workspace_manager_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_manager_assignments
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>workspace_manager_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_manager_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.workspace_manager_assignments" /></td></tr>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="items_" /></td>
    <td><code>array</code></td>
    <td>List of resources included in this workspace manager assignment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastJobEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the last job associated to this assignment ended at.</td>
</tr>
<tr>
    <td><CopyableCode code="lastJobProvisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the last job associated to this assignment. Known values are: "Accepted", "InProgress", "Succeeded", "Failed", and "Canceled". (Accepted, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceName" /></td>
    <td><code>string</code></td>
    <td>The resource name of the workspace manager group targeted by the workspace manager assignment. Required.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="items_" /></td>
    <td><code>array</code></td>
    <td>List of resources included in this workspace manager assignment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastJobEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the last job associated to this assignment ended at.</td>
</tr>
<tr>
    <td><CopyableCode code="lastJobProvisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the last job associated to this assignment. Known values are: "Accepted", "InProgress", "Succeeded", "Failed", and "Canceled". (Accepted, InProgress, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceName" /></td>
    <td><code>string</code></td>
    <td>The resource name of the workspace manager group targeted by the workspace manager assignment. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-workspace_manager_assignment_name"><code>workspace_manager_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a workspace manager assignment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get all workspace manager assignments for the Sentinel workspace manager.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-workspace_manager_assignment_name"><code>workspace_manager_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a workspace manager assignment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-workspace_manager_assignment_name"><code>workspace_manager_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a workspace manager assignment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-workspace_manager_assignment_name"><code>workspace_manager_assignment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a workspace manager assignment.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_manager_assignment_name">
    <td><CopyableCode code="workspace_manager_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace manager assignment. Required.</td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Returns only the first n results. Optional. Default value is None.</td>
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

Gets a workspace manager assignment.

```sql
SELECT
id,
name,
etag,
items_,
lastJobEndTime,
lastJobProvisioningState,
systemData,
targetResourceName,
type
FROM azure.security_insight.workspace_manager_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND workspace_manager_assignment_name = '{{ workspace_manager_assignment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all workspace manager assignments for the Sentinel workspace manager.

```sql
SELECT
id,
name,
etag,
items_,
lastJobEndTime,
lastJobProvisioningState,
systemData,
targetResourceName,
type
FROM azure.security_insight.workspace_manager_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $orderby = '{{ $orderby }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Creates or updates a workspace manager assignment.

```sql
INSERT INTO azure.security_insight.workspace_manager_assignments (
properties,
resource_group_name,
workspace_name,
workspace_manager_assignment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ workspace_manager_assignment_name }}',
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
- name: workspace_manager_assignments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_manager_assignments resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the workspace_manager_assignments resource.
    - name: workspace_manager_assignment_name
      value: "{{ workspace_manager_assignment_name }}"
      description: Required parameter for the workspace_manager_assignments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_manager_assignments resource.
    - name: properties
      description: |
        The workspace manager assignment object.
      value:
        targetResourceName: "{{ targetResourceName }}"
        lastJobEndTime: "{{ lastJobEndTime }}"
        lastJobProvisioningState: "{{ lastJobProvisioningState }}"
        items_:
          - resourceId: "{{ resourceId }}"
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

Creates or updates a workspace manager assignment.

```sql
REPLACE azure.security_insight.workspace_manager_assignments
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND workspace_manager_assignment_name = '{{ workspace_manager_assignment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Deletes a workspace manager assignment.

```sql
DELETE FROM azure.security_insight.workspace_manager_assignments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND workspace_manager_assignment_name = '{{ workspace_manager_assignment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
