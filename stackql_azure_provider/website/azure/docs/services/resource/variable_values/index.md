--- 
title: variable_values
hide_title: false
hide_table_of_contents: false
keywords:
  - variable_values
  - resource
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

Creates, updates, deletes, gets or lists a <code>variable_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="variable_values" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.variable_values" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'list', value: 'list' },
        { label: 'list_for_management_group', value: 'list_for_management_group' }
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
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Variable value column value array. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_management_group">

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
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Variable value column value array. Required.</td>
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
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Variable value column value array. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_management_group">

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
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Variable value column value array. Required.</td>
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
    <td><a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a variable value. This operation retrieves a single variable value; given its name, subscription it was created at and the variable it's created for.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group"><CopyableCode code="get_at_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a></td>
    <td></td>
    <td>Retrieves a variable value. This operation retrieves a single variable value; given its name, management group it was created at and the variable it's created for.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List variable values for a variable. This operation retrieves the list of all variable values associated with the given variable that is at a subscription level.</td>
</tr>
<tr>
    <td><a href="#list_for_management_group"><CopyableCode code="list_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-variable_name"><code>variable_name</code></a></td>
    <td></td>
    <td>List variable values at management group level. This operation retrieves the list of all variable values applicable the variable indicated at the management group scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a variable value. This operation creates or updates a variable value with the given subscription and name for a given variable. Variable values are scoped to the variable for which they are created for.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a></td>
    <td></td>
    <td>Creates or updates a variable value. This operation creates or updates a variable value with the given management group and name for a given variable. Variable values are scoped to the variable for which they are created for.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a variable value. This operation creates or updates a variable value with the given subscription and name for a given variable. Variable values are scoped to the variable for which they are created for.</td>
</tr>
<tr>
    <td><a href="#create_or_update_at_management_group"><CopyableCode code="create_or_update_at_management_group" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a></td>
    <td></td>
    <td>Creates or updates a variable value. This operation creates or updates a variable value with the given management group and name for a given variable. Variable values are scoped to the variable for which they are created for.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a variable value. This operation deletes a variable value, given its name, the subscription it was created in, and the variable it belongs to. The scope of a variable value is the part of its ID preceding '/providers/Microsoft.Authorization/variables/&#123;variableName&#125;'.</td>
</tr>
<tr>
    <td><a href="#delete_at_management_group"><CopyableCode code="delete_at_management_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-variable_name"><code>variable_name</code></a>, <a href="#parameter-variable_value_name"><code>variable_value_name</code></a></td>
    <td></td>
    <td>Deletes a variable value. This operation deletes a variable value, given its name, the management group it was created in, and the variable it belongs to. The scope of a variable value is the part of its ID preceding '/providers/Microsoft.Authorization/variables/&#123;variableName&#125;'.</td>
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
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the management group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-variable_name">
    <td><CopyableCode code="variable_name" /></td>
    <td><code>string</code></td>
    <td>The name of the variable to operate on. Required.</td>
</tr>
<tr id="parameter-variable_value_name">
    <td><CopyableCode code="variable_value_name" /></td>
    <td><code>string</code></td>
    <td>The name of the variable value to operate on. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_at_management_group', value: 'get_at_management_group' },
        { label: 'list', value: 'list' },
        { label: 'list_for_management_group', value: 'list_for_management_group' }
    ]}
>
<TabItem value="get">

Retrieves a variable value. This operation retrieves a single variable value; given its name, subscription it was created at and the variable it's created for.

```sql
SELECT
id,
name,
systemData,
type,
values
FROM azure.resource.variable_values
WHERE variable_name = '{{ variable_name }}' -- required
AND variable_value_name = '{{ variable_value_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_management_group">

Retrieves a variable value. This operation retrieves a single variable value; given its name, management group it was created at and the variable it's created for.

```sql
SELECT
id,
name,
systemData,
type,
values
FROM azure.resource.variable_values
WHERE management_group_id = '{{ management_group_id }}' -- required
AND variable_name = '{{ variable_name }}' -- required
AND variable_value_name = '{{ variable_value_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List variable values for a variable. This operation retrieves the list of all variable values associated with the given variable that is at a subscription level.

```sql
SELECT
id,
name,
systemData,
type,
values
FROM azure.resource.variable_values
WHERE variable_name = '{{ variable_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_management_group">

List variable values at management group level. This operation retrieves the list of all variable values applicable the variable indicated at the management group scope.

```sql
SELECT
id,
name,
systemData,
type,
values
FROM azure.resource.variable_values
WHERE management_group_id = '{{ management_group_id }}' -- required
AND variable_name = '{{ variable_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a variable value. This operation creates or updates a variable value with the given subscription and name for a given variable. Variable values are scoped to the variable for which they are created for.

```sql
INSERT INTO azure.resource.variable_values (
properties,
variable_name,
variable_value_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ variable_name }}',
'{{ variable_value_name }}',
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
<TabItem value="create_or_update_at_management_group">

Creates or updates a variable value. This operation creates or updates a variable value with the given management group and name for a given variable. Variable values are scoped to the variable for which they are created for.

```sql
INSERT INTO azure.resource.variable_values (
properties,
management_group_id,
variable_name,
variable_value_name
)
SELECT 
'{{ properties }}',
'{{ management_group_id }}',
'{{ variable_name }}',
'{{ variable_value_name }}'
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
- name: variable_values
  props:
    - name: variable_name
      value: "{{ variable_name }}"
      description: Required parameter for the variable_values resource.
    - name: variable_value_name
      value: "{{ variable_value_name }}"
      description: Required parameter for the variable_values resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the variable_values resource.
    - name: management_group_id
      value: "{{ management_group_id }}"
      description: Required parameter for the variable_values resource.
    - name: properties
      description: |
        Properties for the variable value.
      value:
        values:
          - columnName: "{{ columnName }}"
            columnValue: "{{ columnValue }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_at_management_group', value: 'create_or_update_at_management_group' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a variable value. This operation creates or updates a variable value with the given subscription and name for a given variable. Variable values are scoped to the variable for which they are created for.

```sql
REPLACE azure.resource.variable_values
SET 
properties = '{{ properties }}'
WHERE 
variable_name = '{{ variable_name }}' --required
AND variable_value_name = '{{ variable_value_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update_at_management_group">

Creates or updates a variable value. This operation creates or updates a variable value with the given management group and name for a given variable. Variable values are scoped to the variable for which they are created for.

```sql
REPLACE azure.resource.variable_values
SET 
properties = '{{ properties }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND variable_name = '{{ variable_name }}' --required
AND variable_value_name = '{{ variable_value_name }}' --required
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
        { label: 'delete', value: 'delete' },
        { label: 'delete_at_management_group', value: 'delete_at_management_group' }
    ]}
>
<TabItem value="delete">

Deletes a variable value. This operation deletes a variable value, given its name, the subscription it was created in, and the variable it belongs to. The scope of a variable value is the part of its ID preceding '/providers/Microsoft.Authorization/variables/&#123;variableName&#125;'.

```sql
DELETE FROM azure.resource.variable_values
WHERE variable_name = '{{ variable_name }}' --required
AND variable_value_name = '{{ variable_value_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_at_management_group">

Deletes a variable value. This operation deletes a variable value, given its name, the management group it was created in, and the variable it belongs to. The scope of a variable value is the part of its ID preceding '/providers/Microsoft.Authorization/variables/&#123;variableName&#125;'.

```sql
DELETE FROM azure.resource.variable_values
WHERE management_group_id = '{{ management_group_id }}' --required
AND variable_name = '{{ variable_name }}' --required
AND variable_value_name = '{{ variable_value_name }}' --required
;
```
</TabItem>
</Tabs>
