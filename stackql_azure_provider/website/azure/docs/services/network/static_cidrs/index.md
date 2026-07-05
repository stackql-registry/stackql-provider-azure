--- 
title: static_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - static_cidrs
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

Creates, updates, deletes, gets or lists a <code>static_cidrs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="static_cidrs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.static_cidrs" /></td></tr>
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
    <td>List of IP address prefixes of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfIPAddressesToAllocate" /></td>
    <td><code>string</code></td>
    <td>Number of IP addresses to allocate for a static CIDR resource. The IP addresses will be assigned based on IpamPools available space.</td>
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
    <td><CopyableCode code="totalNumberOfIPAddresses" /></td>
    <td><code>string</code></td>
    <td>Total number of IP addresses allocated for the static CIDR resource.</td>
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
    <td>List of IP address prefixes of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfIPAddressesToAllocate" /></td>
    <td><code>string</code></td>
    <td>Number of IP addresses to allocate for a static CIDR resource. The IP addresses will be assigned based on IpamPools available space.</td>
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
    <td><CopyableCode code="totalNumberOfIPAddresses" /></td>
    <td><code>string</code></td>
    <td>Total number of IP addresses allocated for the static CIDR resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-static_cidr_name"><code>static_cidr_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specific Static CIDR resource. Gets the specific Static CIDR resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipToken"><code>skipToken</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-sortKey"><code>sortKey</code></a>, <a href="#parameter-sortValue"><code>sortValue</code></a></td>
    <td>Gets list of Static CIDR resources at Network Manager level. Gets list of Static CIDR resources at Network Manager level.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-static_cidr_name"><code>static_cidr_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates/Updates the Static CIDR resource. Creates/Updates the Static CIDR resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_manager_name"><code>network_manager_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-static_cidr_name"><code>static_cidr_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the Static CIDR resource. Delete the Static CIDR resource.</td>
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
<tr id="parameter-static_cidr_name">
    <td><CopyableCode code="static_cidr_name" /></td>
    <td><code>string</code></td>
    <td>StaticCidr resource name to retrieve. Required.</td>
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

Gets the specific Static CIDR resource. Gets the specific Static CIDR resource.

```sql
SELECT
id,
name,
addressPrefixes,
description,
numberOfIPAddressesToAllocate,
provisioningState,
systemData,
totalNumberOfIPAddresses,
type
FROM azure.network.static_cidrs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_manager_name = '{{ network_manager_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND static_cidr_name = '{{ static_cidr_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets list of Static CIDR resources at Network Manager level. Gets list of Static CIDR resources at Network Manager level.

```sql
SELECT
id,
name,
addressPrefixes,
description,
numberOfIPAddressesToAllocate,
provisioningState,
systemData,
totalNumberOfIPAddresses,
type
FROM azure.network.static_cidrs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_manager_name = '{{ network_manager_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
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

Creates/Updates the Static CIDR resource. Creates/Updates the Static CIDR resource.

```sql
INSERT INTO azure.network.static_cidrs (
properties,
resource_group_name,
network_manager_name,
pool_name,
static_cidr_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_manager_name }}',
'{{ pool_name }}',
'{{ static_cidr_name }}',
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
- name: static_cidrs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the static_cidrs resource.
    - name: network_manager_name
      value: "{{ network_manager_name }}"
      description: Required parameter for the static_cidrs resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the static_cidrs resource.
    - name: static_cidr_name
      value: "{{ static_cidr_name }}"
      description: Required parameter for the static_cidrs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the static_cidrs resource.
    - name: properties
      description: |
        Properties of static CIDR resource.
      value:
        description: "{{ description }}"
        numberOfIPAddressesToAllocate: "{{ numberOfIPAddressesToAllocate }}"
        addressPrefixes:
          - "{{ addressPrefixes }}"
        totalNumberOfIPAddresses: "{{ totalNumberOfIPAddresses }}"
        provisioningState: "{{ provisioningState }}"
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

Delete the Static CIDR resource. Delete the Static CIDR resource.

```sql
DELETE FROM azure.network.static_cidrs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_manager_name = '{{ network_manager_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND static_cidr_name = '{{ static_cidr_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
