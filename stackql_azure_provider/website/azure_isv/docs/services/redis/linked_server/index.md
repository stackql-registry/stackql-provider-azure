--- 
title: linked_server
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_server
  - redis
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>linked_server</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="linked_server" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.linked_server" /></td></tr>
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
    <td><CopyableCode code="geoReplicatedPrimaryHostName" /></td>
    <td><code>string</code></td>
    <td>The unchanging DNS name which will always point to current geo-primary cache among the linked redis caches for seamless Geo Failover experience.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedRedisCacheId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resourceId of the linked redis cache. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedRedisCacheLocation" /></td>
    <td><code>string</code></td>
    <td>Location of the linked redis cache. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryHostName" /></td>
    <td><code>string</code></td>
    <td>The changing DNS name that resolves to the current geo-primary cache among the linked redis caches before or after the Geo Failover.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Terminal state of the link between primary and secondary redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="serverRole" /></td>
    <td><code>string</code></td>
    <td>Role of the linked server. Required. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
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
    <td><CopyableCode code="geoReplicatedPrimaryHostName" /></td>
    <td><code>string</code></td>
    <td>The unchanging DNS name which will always point to current geo-primary cache among the linked redis caches for seamless Geo Failover experience.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedRedisCacheId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resourceId of the linked redis cache. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedRedisCacheLocation" /></td>
    <td><code>string</code></td>
    <td>Location of the linked redis cache. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryHostName" /></td>
    <td><code>string</code></td>
    <td>The changing DNS name that resolves to the current geo-primary cache among the linked redis caches before or after the Geo Failover.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Terminal state of the link between primary and secondary redis cache.</td>
</tr>
<tr>
    <td><CopyableCode code="serverRole" /></td>
    <td><code>string</code></td>
    <td>Role of the linked server. Required. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_server_name"><code>linked_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the detailed information about a linked server of a redis cache (requires Premium SKU).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of linked servers associated with this redis cache (requires Premium SKU).</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_server_name"><code>linked_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Adds a linked server to the Redis cache (requires Premium SKU).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-linked_server_name"><code>linked_server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the linked server from a redis cache (requires Premium SKU).</td>
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
<tr id="parameter-linked_server_name">
    <td><CopyableCode code="linked_server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the RedisLinkedServerWithProperties. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the redis cache. Required.</td>
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

Gets the detailed information about a linked server of a redis cache (requires Premium SKU).

```sql
SELECT
id,
name,
geoReplicatedPrimaryHostName,
linkedRedisCacheId,
linkedRedisCacheLocation,
primaryHostName,
provisioningState,
serverRole,
systemData,
type
FROM azure_isv.redis.linked_server
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND linked_server_name = '{{ linked_server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of linked servers associated with this redis cache (requires Premium SKU).

```sql
SELECT
id,
name,
geoReplicatedPrimaryHostName,
linkedRedisCacheId,
linkedRedisCacheLocation,
primaryHostName,
provisioningState,
serverRole,
systemData,
type
FROM azure_isv.redis.linked_server
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
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

Adds a linked server to the Redis cache (requires Premium SKU).

```sql
INSERT INTO azure_isv.redis.linked_server (
properties,
resource_group_name,
name,
linked_server_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ name }}',
'{{ linked_server_name }}',
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
- name: linked_server
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the linked_server resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the linked_server resource.
    - name: linked_server_name
      value: "{{ linked_server_name }}"
      description: Required parameter for the linked_server resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the linked_server resource.
    - name: properties
      description: |
        Properties required to create a linked server. Required.
      value:
        linkedRedisCacheId: "{{ linkedRedisCacheId }}"
        linkedRedisCacheLocation: "{{ linkedRedisCacheLocation }}"
        serverRole: "{{ serverRole }}"
        geoReplicatedPrimaryHostName: "{{ geoReplicatedPrimaryHostName }}"
        primaryHostName: "{{ primaryHostName }}"
`}</CodeBlock>

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

Deletes the linked server from a redis cache (requires Premium SKU).

```sql
DELETE FROM azure_isv.redis.linked_server
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND linked_server_name = '{{ linked_server_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
