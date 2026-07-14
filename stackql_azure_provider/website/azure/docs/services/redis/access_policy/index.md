--- 
title: access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy
  - redis
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

Creates, updates, deletes, gets or lists an <code>access_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.redis.access_policy" /></td></tr>
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
    <td><CopyableCode code="permissions" /></td>
    <td><code>string</code></td>
    <td>Permissions for the access policy. Learn how to configure permissions at `https://aka.ms/redis/AADPreRequisites `_. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of access policy. Known values are: "Updating", "Succeeded", "Deleting", "Deleted", "Canceled", and "Failed". (Updating, Succeeded, Deleting, Deleted, Canceled, Failed)</td>
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
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>string</code></td>
    <td>Permissions for the access policy. Learn how to configure permissions at `https://aka.ms/redis/AADPreRequisites `_. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of access policy. Known values are: "Updating", "Succeeded", "Deleting", "Deleted", "Canceled", and "Failed". (Updating, Succeeded, Deleting, Deleted, Canceled, Failed)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-access_policy_name"><code>access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the detailed information about an access policy of a redis cache.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of access policies associated with this redis cache.</td>
</tr>
<tr>
    <td><a href="#create_update"><CopyableCode code="create_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-access_policy_name"><code>access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds an access policy to the redis cache.</td>
</tr>
<tr>
    <td><a href="#create_update"><CopyableCode code="create_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-access_policy_name"><code>access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds an access policy to the redis cache.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cache_name"><code>cache_name</code></a>, <a href="#parameter-access_policy_name"><code>access_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the access policy from a redis cache.</td>
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
<tr id="parameter-access_policy_name">
    <td><CopyableCode code="access_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the access policy that is being added to the Redis cache. Required.</td>
</tr>
<tr id="parameter-cache_name">
    <td><CopyableCode code="cache_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Redis cache. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the detailed information about an access policy of a redis cache.

```sql
SELECT
id,
name,
permissions,
provisioningState,
systemData,
type
FROM azure.redis.access_policy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cache_name = '{{ cache_name }}' -- required
AND access_policy_name = '{{ access_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of access policies associated with this redis cache.

```sql
SELECT
id,
name,
permissions,
provisioningState,
systemData,
type
FROM azure.redis.access_policy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cache_name = '{{ cache_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_update"
    values={[
        { label: 'create_update', value: 'create_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_update">

Adds an access policy to the redis cache.

```sql
INSERT INTO azure.redis.access_policy (
properties,
resource_group_name,
cache_name,
access_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cache_name }}',
'{{ access_policy_name }}',
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
- name: access_policy
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the access_policy resource.
    - name: cache_name
      value: "{{ cache_name }}"
      description: Required parameter for the access_policy resource.
    - name: access_policy_name
      value: "{{ access_policy_name }}"
      description: Required parameter for the access_policy resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the access_policy resource.
    - name: properties
      description: |
        Properties of an access policy.
      value:
        provisioningState: "{{ provisioningState }}"
        type: "{{ type }}"
        permissions: "{{ permissions }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_update"
    values={[
        { label: 'create_update', value: 'create_update' }
    ]}
>
<TabItem value="create_update">

Adds an access policy to the redis cache.

```sql
REPLACE azure.redis.access_policy
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND access_policy_name = '{{ access_policy_name }}' --required
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

Deletes the access policy from a redis cache.

```sql
DELETE FROM azure.redis.access_policy
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cache_name = '{{ cache_name }}' --required
AND access_policy_name = '{{ access_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
