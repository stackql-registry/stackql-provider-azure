--- 
title: mongo_mi_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_mi_resources
  - cosmosdb
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

Creates, updates, deletes, gets or lists a <code>mongo_mi_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mongo_mi_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.mongo_mi_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_mongo_mi_role_definition"
    values={[
        { label: 'get_mongo_mi_role_definition', value: 'get_mongo_mi_role_definition' },
        { label: 'get_mongo_mi_role_assignment', value: 'get_mongo_mi_role_assignment' },
        { label: 'list_mongo_mi_role_definitions', value: 'list_mongo_mi_role_definitions' }
    ]}
>
<TabItem value="get_mongo_mi_role_definition">

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
    <td><CopyableCode code="assignableScopes" /></td>
    <td><code>array</code></td>
    <td>A set of fully qualified Scopes at or below which MongoMI Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>The set of operations allowed through this Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the Role Definition. Must be unique for the database account.</td>
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
<TabItem value="get_mongo_mi_role_assignment">

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
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated AAD principal in the AAD graph to which access is being granted through this MongoMI Role Assignment. Tenant ID for the principal is inferred using the tenant associated with the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The data plane resource path for which access is being granted through this MongoMI Role Assignment.</td>
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
<TabItem value="list_mongo_mi_role_definitions">

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
    <td><CopyableCode code="assignableScopes" /></td>
    <td><code>array</code></td>
    <td>A set of fully qualified Scopes at or below which MongoMI Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>The set of operations allowed through this Role Definition.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the Role Definition. Must be unique for the database account.</td>
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
    <td><a href="#get_mongo_mi_role_definition"><CopyableCode code="get_mongo_mi_role_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB MongoMI Role Definition with the given Id.</td>
</tr>
<tr>
    <td><a href="#get_mongo_mi_role_assignment"><CopyableCode code="get_mongo_mi_role_assignment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the properties of an existing Azure Cosmos DB MongoMI Role Assignment with the given Id.</td>
</tr>
<tr>
    <td><a href="#list_mongo_mi_role_definitions"><CopyableCode code="list_mongo_mi_role_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB MongoMI Role Definitions.</td>
</tr>
<tr>
    <td><a href="#create_update_mongo_mi_role_definition"><CopyableCode code="create_update_mongo_mi_role_definition" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB MongoMI Role Definition.</td>
</tr>
<tr>
    <td><a href="#create_update_mongo_mi_role_assignment"><CopyableCode code="create_update_mongo_mi_role_assignment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Azure Cosmos DB MongoMI Role Assignment.</td>
</tr>
<tr>
    <td><a href="#delete_mongo_mi_role_definition"><CopyableCode code="delete_mongo_mi_role_definition" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_definition_id"><code>role_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB MongoMI Role Definition.</td>
</tr>
<tr>
    <td><a href="#delete_mongo_mi_role_assignment"><CopyableCode code="delete_mongo_mi_role_assignment" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-role_assignment_id"><code>role_assignment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Cosmos DB MongoMI Role Assignment.</td>
</tr>
<tr>
    <td><a href="#list_mongo_mi_role_assignments"><CopyableCode code="list_mongo_mi_role_assignments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the list of all Azure Cosmos DB MongoMI Role Assignments.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB database account name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-role_assignment_id">
    <td><CopyableCode code="role_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The GUID for the Role Assignment. Required.</td>
</tr>
<tr id="parameter-role_definition_id">
    <td><CopyableCode code="role_definition_id" /></td>
    <td><code>string</code></td>
    <td>The GUID for the Role Definition. Required.</td>
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
    defaultValue="get_mongo_mi_role_definition"
    values={[
        { label: 'get_mongo_mi_role_definition', value: 'get_mongo_mi_role_definition' },
        { label: 'get_mongo_mi_role_assignment', value: 'get_mongo_mi_role_assignment' },
        { label: 'list_mongo_mi_role_definitions', value: 'list_mongo_mi_role_definitions' }
    ]}
>
<TabItem value="get_mongo_mi_role_definition">

Retrieves the properties of an existing Azure Cosmos DB MongoMI Role Definition with the given Id.

```sql
SELECT
id,
name,
assignableScopes,
permissions,
roleName,
systemData,
type
FROM azure.cosmosdb.mongo_mi_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND role_definition_id = '{{ role_definition_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_mongo_mi_role_assignment">

Retrieves the properties of an existing Azure Cosmos DB MongoMI Role Assignment with the given Id.

```sql
SELECT
id,
name,
principalId,
provisioningState,
roleDefinitionId,
scope,
systemData,
type
FROM azure.cosmosdb.mongo_mi_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND role_assignment_id = '{{ role_assignment_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_mongo_mi_role_definitions">

Retrieves the list of all Azure Cosmos DB MongoMI Role Definitions.

```sql
SELECT
id,
name,
assignableScopes,
permissions,
roleName,
systemData,
type
FROM azure.cosmosdb.mongo_mi_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_update_mongo_mi_role_definition"
    values={[
        { label: 'create_update_mongo_mi_role_definition', value: 'create_update_mongo_mi_role_definition' },
        { label: 'create_update_mongo_mi_role_assignment', value: 'create_update_mongo_mi_role_assignment' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_update_mongo_mi_role_definition">

Creates or updates an Azure Cosmos DB MongoMI Role Definition.

```sql
INSERT INTO azure.cosmosdb.mongo_mi_resources (
properties,
resource_group_name,
account_name,
role_definition_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ role_definition_id }}',
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
<TabItem value="create_update_mongo_mi_role_assignment">

Creates or updates an Azure Cosmos DB MongoMI Role Assignment.

```sql
INSERT INTO azure.cosmosdb.mongo_mi_resources (
properties,
resource_group_name,
account_name,
role_assignment_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ role_assignment_id }}',
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
- name: mongo_mi_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the mongo_mi_resources resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the mongo_mi_resources resource.
    - name: role_definition_id
      value: "{{ role_definition_id }}"
      description: Required parameter for the mongo_mi_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the mongo_mi_resources resource.
    - name: role_assignment_id
      value: "{{ role_assignment_id }}"
      description: Required parameter for the mongo_mi_resources resource.
    - name: properties
      description: |
        Properties to create and update an Azure Cosmos DB MongoMI Role Assignment.
      value:
        roleDefinitionId: "{{ roleDefinitionId }}"
        scope: "{{ scope }}"
        principalId: "{{ principalId }}"
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_mongo_mi_role_definition"
    values={[
        { label: 'delete_mongo_mi_role_definition', value: 'delete_mongo_mi_role_definition' },
        { label: 'delete_mongo_mi_role_assignment', value: 'delete_mongo_mi_role_assignment' }
    ]}
>
<TabItem value="delete_mongo_mi_role_definition">

Deletes an existing Azure Cosmos DB MongoMI Role Definition.

```sql
DELETE FROM azure.cosmosdb.mongo_mi_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND role_definition_id = '{{ role_definition_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_mongo_mi_role_assignment">

Deletes an existing Azure Cosmos DB MongoMI Role Assignment.

```sql
DELETE FROM azure.cosmosdb.mongo_mi_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND role_assignment_id = '{{ role_assignment_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_mongo_mi_role_assignments"
    values={[
        { label: 'list_mongo_mi_role_assignments', value: 'list_mongo_mi_role_assignments' }
    ]}
>
<TabItem value="list_mongo_mi_role_assignments">

Retrieves the list of all Azure Cosmos DB MongoMI Role Assignments.

```sql
EXEC azure.cosmosdb.mongo_mi_resources.list_mongo_mi_role_assignments 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
