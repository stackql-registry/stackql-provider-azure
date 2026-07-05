--- 
title: ipam_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pools
  - network
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

Creates, updates, deletes, gets or lists an <code>ipam_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ipam_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.ipam_pools" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>List of IP address prefixes of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>String representing a friendly name for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddressType" /></td>
    <td><code>array</code></td>
    <td>List of IP address type for the IpamPool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="parentPoolName" /></td>
    <td><code>string</code></td>
    <td>String representing parent IpamPool resource name. If empty the IpamPool will be a root pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning states of a resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>List of IP address prefixes of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>String representing a friendly name for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddressType" /></td>
    <td><code>array</code></td>
    <td>List of IP address type for the IpamPool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="parentPoolName" /></td>
    <td><code>string</code></td>
    <td>String representing parent IpamPool resource name. If empty the IpamPool will be a root pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning states of a resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specific Pool resource. Gets the specific Pool resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipToken"><code>skipToken</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-sortKey"><code>sortKey</code></a>, <a href="#parameter-sortValue"><code>sortValue</code></a></td>
    <td>Gets list of Pool resources at Network Manager level. Gets list of Pool resources at Network Manager level.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates/Updates the Pool resource. Creates/Updates the Pool resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specific Pool resource. Updates the specific Pool resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the Pool resource. Delete the Pool resource.</td>
</tr>
<tr>
    <td><a href="#list_associated_resources"><CopyableCode code="list_associated_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Associated Resource in the Pool. List Associated Resource in the Pool.</td>
</tr>
<tr>
    <td><a href="#get_pool_usage"><CopyableCode code="get_pool_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Pool Usage. Get the Pool Usage.</td>
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
<tr id="parameter-network_manager_name">
    <td><CopyableCode code="network_manager_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network manager. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>Pool resource name. Required.</td>
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
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>Optional num entries to skip. Default value is 0.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Optional skip token. Default value is None.</td>
</tr>
<tr id="parameter-sortKey">
    <td><CopyableCode code="sortKey" /></td>
    <td><code>string</code></td>
    <td>Optional key by which to sort. Default value is None.</td>
</tr>
<tr id="parameter-sortValue">
    <td><CopyableCode code="sortValue" /></td>
    <td><code>string</code></td>
    <td>Optional sort value for pagination. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Optional num entries to show. Default value is 50.</td>
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

Gets the specific Pool resource. Gets the specific Pool resource.

```sql
SELECT
id,
name,
addressPrefixes,
description,
displayName,
etag,
ipAddressType,
location,
parentPoolName,
provisioningState,
systemData,
tags,
type
FROM azure.network.ipam_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_manager_name = '{{ network_manager_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets list of Pool resources at Network Manager level. Gets list of Pool resources at Network Manager level.

```sql
SELECT
id,
name,
addressPrefixes,
description,
displayName,
etag,
ipAddressType,
location,
parentPoolName,
provisioningState,
systemData,
tags,
type
FROM azure.network.ipam_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_manager_name = '{{ network_manager_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND skipToken = '{{ skipToken }}'
AND skip = '{{ skip }}'
AND top = '{{ top }}'
AND sortKey = '{{ sortKey }}'
AND sortValue = '{{ sortValue }}'
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

Creates/Updates the Pool resource. Creates/Updates the Pool resource.

```sql
INSERT INTO azure.network.ipam_pools (
tags,
location,
properties,
resource_group_name,
network_manager_name,
pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ network_manager_name }}',
'{{ pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: ipam_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the ipam_pools resource.
    - name: network_manager_name
      value: "{{ network_manager_name }}"
      description: Required parameter for the ipam_pools resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the ipam_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the ipam_pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of IpamPool resource properties which are specific to the Pool resource. Required.
      value:
        description: "{{ description }}"
        displayName: "{{ displayName }}"
        ipAddressType:
          - "{{ ipAddressType }}"
        parentPoolName: "{{ parentPoolName }}"
        addressPrefixes:
          - "{{ addressPrefixes }}"
        provisioningState: "{{ provisioningState }}"
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

Updates the specific Pool resource. Updates the specific Pool resource.

```sql
UPDATE azure.network.ipam_pools
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_manager_name = '{{ network_manager_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Delete the Pool resource. Delete the Pool resource.

```sql
DELETE FROM azure.network.ipam_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_manager_name = '{{ network_manager_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_associated_resources"
    values={[
        { label: 'list_associated_resources', value: 'list_associated_resources' },
        { label: 'get_pool_usage', value: 'get_pool_usage' }
    ]}
>
<TabItem value="list_associated_resources">

List Associated Resource in the Pool. List Associated Resource in the Pool.

```sql
EXEC azure.network.ipam_pools.list_associated_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_manager_name='{{ network_manager_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_pool_usage">

Get the Pool Usage. Get the Pool Usage.

```sql
EXEC azure.network.ipam_pools.get_pool_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_manager_name='{{ network_manager_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
