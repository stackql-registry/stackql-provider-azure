--- 
title: service_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - service_groups
  - servicegroups
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

Creates, updates, deletes, gets or lists a <code>service_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicegroups.service_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the serviceGroup. For example, ServiceGroupTest1.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the serviceGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td>The details of the parent serviceGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the serviceGroup. For example, Running. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The serviceGroup tags.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Get the details of the serviceGroup.</td>
</tr>
<tr>
    <td><a href="#create_or_update_service_group"><CopyableCode code="create_or_update_service_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Create or Update a serviceGroup.</td>
</tr>
<tr>
    <td><a href="#update_service_group"><CopyableCode code="update_service_group" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Update a serviceGroup.</td>
</tr>
<tr>
    <td><a href="#create_or_update_service_group"><CopyableCode code="create_or_update_service_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Create or Update a serviceGroup.</td>
</tr>
<tr>
    <td><a href="#delete_service_group"><CopyableCode code="delete_service_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Delete a ServiceGroup.</td>
</tr>
<tr>
    <td><a href="#list_ancestors"><CopyableCode code="list_ancestors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Get the details of the serviceGroup's ancestors.</td>
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
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>ServiceGroup Name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the details of the serviceGroup.

```sql
SELECT
id,
name,
displayName,
kind,
parent,
provisioningState,
systemData,
tags,
type
FROM azure.servicegroups.service_groups
WHERE service_group_name = '{{ service_group_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_service_group"
    values={[
        { label: 'create_or_update_service_group', value: 'create_or_update_service_group' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_service_group">

Create or Update a serviceGroup.

```sql
INSERT INTO azure.servicegroups.service_groups (
properties,
kind,
tags,
service_group_name
)
SELECT 
'{{ properties }}',
'{{ kind }}',
'{{ tags }}',
'{{ service_group_name }}'
RETURNING
id,
name,
kind,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_groups
  props:
    - name: service_group_name
      value: "{{ service_group_name }}"
      description: Required parameter for the service_groups resource.
    - name: properties
      description: |
        ServiceGroup creation request body parameters.
      value:
        provisioningState: "{{ provisioningState }}"
        displayName: "{{ displayName }}"
        parent:
          resourceId: "{{ resourceId }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the serviceGroup.
    - name: tags
      value: "{{ tags }}"
      description: |
        The serviceGroup tags.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_service_group"
    values={[
        { label: 'update_service_group', value: 'update_service_group' }
    ]}
>
<TabItem value="update_service_group">

Update a serviceGroup.

```sql
UPDATE azure.servicegroups.service_groups
SET 
properties = '{{ properties }}',
kind = '{{ kind }}',
tags = '{{ tags }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_service_group"
    values={[
        { label: 'create_or_update_service_group', value: 'create_or_update_service_group' }
    ]}
>
<TabItem value="create_or_update_service_group">

Create or Update a serviceGroup.

```sql
REPLACE azure.servicegroups.service_groups
SET 
properties = '{{ properties }}',
kind = '{{ kind }}',
tags = '{{ tags }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_service_group"
    values={[
        { label: 'delete_service_group', value: 'delete_service_group' }
    ]}
>
<TabItem value="delete_service_group">

Delete a ServiceGroup.

```sql
DELETE FROM azure.servicegroups.service_groups
WHERE service_group_name = '{{ service_group_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_ancestors"
    values={[
        { label: 'list_ancestors', value: 'list_ancestors' }
    ]}
>
<TabItem value="list_ancestors">

Get the details of the serviceGroup's ancestors.

```sql
EXEC azure.servicegroups.service_groups.list_ancestors 
@service_group_name='{{ service_group_name }}' --required
;
```
</TabItem>
</Tabs>
