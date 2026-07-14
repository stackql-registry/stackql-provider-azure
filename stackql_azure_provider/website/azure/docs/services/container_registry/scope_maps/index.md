--- 
title: scope_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_maps
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

Creates, updates, deletes, gets or lists a <code>scope_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scope_maps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.scope_maps" /></td></tr>
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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The list of scoped permissions for registry artifacts. E.g. repositories/repository-name/content/read, repositories/repository-name/metadata/write. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of scope map.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The user friendly description of the scope map.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The list of scoped permissions for registry artifacts. E.g. repositories/repository-name/content/read, repositories/repository-name/metadata/write. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of scope map.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The user friendly description of the scope map.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-scope_map_name"><code>scope_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the specified scope map.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the scope maps for the specified container registry.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-scope_map_name"><code>scope_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a scope map for a container registry with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-scope_map_name"><code>scope_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a scope map with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-scope_map_name"><code>scope_map_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a scope map from a container registry.</td>
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
<tr id="parameter-scope_map_name">
    <td><CopyableCode code="scope_map_name" /></td>
    <td><code>string</code></td>
    <td>The name of the scope map. Required.</td>
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

Gets the properties of the specified scope map.

```sql
SELECT
id,
name,
actions,
creationDate,
description,
provisioningState,
systemData,
type
FROM azure.container_registry.scope_maps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND scope_map_name = '{{ scope_map_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the scope maps for the specified container registry.

```sql
SELECT
id,
name,
actions,
creationDate,
description,
provisioningState,
systemData,
type
FROM azure.container_registry.scope_maps
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

Creates a scope map for a container registry with the specified parameters.

```sql
INSERT INTO azure.container_registry.scope_maps (
properties,
resource_group_name,
registry_name,
scope_map_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ registry_name }}',
'{{ scope_map_name }}',
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
- name: scope_maps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scope_maps resource.
    - name: registry_name
      value: "{{ registry_name }}"
      description: Required parameter for the scope_maps resource.
    - name: scope_map_name
      value: "{{ scope_map_name }}"
      description: Required parameter for the scope_maps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scope_maps resource.
    - name: properties
      description: |
        The properties of the scope map.
      value:
        description: "{{ description }}"
        type: "{{ type }}"
        creationDate: "{{ creationDate }}"
        provisioningState: "{{ provisioningState }}"
        actions:
          - "{{ actions }}"
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

Updates a scope map with the specified parameters.

```sql
UPDATE azure.container_registry.scope_maps
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND scope_map_name = '{{ scope_map_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Deletes a scope map from a container registry.

```sql
DELETE FROM azure.container_registry.scope_maps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND scope_map_name = '{{ scope_map_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
