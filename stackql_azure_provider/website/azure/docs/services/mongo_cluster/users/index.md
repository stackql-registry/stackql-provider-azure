--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - mongo_cluster
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mongo_cluster.users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_mongo_cluster', value: 'list_by_mongo_cluster' }
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
    <td><CopyableCode code="identityProvider" /></td>
    <td><code>object</code></td>
    <td>The user's identity provider definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the user. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", "Updating", and "Dropping". (Succeeded, Failed, Canceled, InProgress, Updating, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>Database roles that are assigned to the user.</td>
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
<TabItem value="list_by_mongo_cluster">

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
    <td><CopyableCode code="identityProvider" /></td>
    <td><code>object</code></td>
    <td>The user's identity provider definition.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the user. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", "Updating", and "Dropping". (Succeeded, Failed, Canceled, InProgress, Updating, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>Database roles that are assigned to the user.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-user_name"><code>user_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the defintion of a Mongo cluster user.</td>
</tr>
<tr>
    <td><a href="#list_by_mongo_cluster"><CopyableCode code="list_by_mongo_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the users on a mongo cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-user_name"><code>user_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new user or updates an existing user on a mongo cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-user_name"><code>user_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new user or updates an existing user on a mongo cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-user_name"><code>user_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a mongo cluster user.</td>
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
<tr id="parameter-mongo_cluster_name">
    <td><CopyableCode code="mongo_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the mongo cluster. Required.</td>
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
<tr id="parameter-user_name">
    <td><CopyableCode code="user_name" /></td>
    <td><code>string</code></td>
    <td>The name of the mongo cluster user. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_mongo_cluster', value: 'list_by_mongo_cluster' }
    ]}
>
<TabItem value="get">

Gets the defintion of a Mongo cluster user.

```sql
SELECT
id,
name,
identityProvider,
provisioningState,
roles,
systemData,
type
FROM azure.mongo_cluster.users
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' -- required
AND user_name = '{{ user_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_mongo_cluster">

List all the users on a mongo cluster.

```sql
SELECT
id,
name,
identityProvider,
provisioningState,
roles,
systemData,
type
FROM azure.mongo_cluster.users
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' -- required
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

Creates a new user or updates an existing user on a mongo cluster.

```sql
INSERT INTO azure.mongo_cluster.users (
properties,
resource_group_name,
mongo_cluster_name,
user_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ mongo_cluster_name }}',
'{{ user_name }}',
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
- name: users
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the users resource.
    - name: mongo_cluster_name
      value: "{{ mongo_cluster_name }}"
      description: Required parameter for the users resource.
    - name: user_name
      value: "{{ user_name }}"
      description: Required parameter for the users resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the users resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        identityProvider:
          type: "{{ type }}"
        roles:
          - db: "{{ db }}"
            role: "{{ role }}"
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

Creates a new user or updates an existing user on a mongo cluster.

```sql
REPLACE azure.mongo_cluster.users
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' --required
AND user_name = '{{ user_name }}' --required
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

Deletes a mongo cluster user.

```sql
DELETE FROM azure.mongo_cluster.users
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' --required
AND user_name = '{{ user_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
