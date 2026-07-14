--- 
title: virtual_network_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_addresses
  - oracle_database
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

Creates, updates, deletes, gets or lists a <code>virtual_network_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_addresses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.virtual_network_addresses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
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
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Virtual network address fully qualified domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Virtual network Address address.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state of the application virtual IP (VIP) address.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>virtual network address lifecycle state. Known values are: "Provisioning", "Available", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Application VIP OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeAssigned" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the create operation for the application virtual IP (VIP) address completed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmOcid" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine OCID.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_parent">

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
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Virtual network address fully qualified domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Virtual network Address address.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state of the application virtual IP (VIP) address.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>virtual network address lifecycle state. Known values are: "Provisioning", "Available", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Application VIP OCID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeAssigned" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the create operation for the application virtual IP (VIP) address completed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmOcid" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine OCID.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-virtualnetworkaddressname"><code>virtualnetworkaddressname</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a VirtualNetworkAddress.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List VirtualNetworkAddress resources by CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-virtualnetworkaddressname"><code>virtualnetworkaddressname</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a VirtualNetworkAddress.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-virtualnetworkaddressname"><code>virtualnetworkaddressname</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a VirtualNetworkAddress.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-virtualnetworkaddressname"><code>virtualnetworkaddressname</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a VirtualNetworkAddress.</td>
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
<tr id="parameter-cloudvmclustername">
    <td><CopyableCode code="cloudvmclustername" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster name. Required.</td>
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
<tr id="parameter-virtualnetworkaddressname">
    <td><CopyableCode code="virtualnetworkaddressname" /></td>
    <td><code>string</code></td>
    <td>Virtual IP address hostname. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="get">

Get a VirtualNetworkAddress.

```sql
SELECT
id,
name,
domain,
ipAddress,
lifecycleDetails,
lifecycleState,
ocid,
provisioningState,
systemData,
timeAssigned,
type,
vmOcid
FROM azure_isv.oracle_database.virtual_network_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudvmclustername = '{{ cloudvmclustername }}' -- required
AND virtualnetworkaddressname = '{{ virtualnetworkaddressname }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List VirtualNetworkAddress resources by CloudVmCluster.

```sql
SELECT
id,
name,
domain,
ipAddress,
lifecycleDetails,
lifecycleState,
ocid,
provisioningState,
systemData,
timeAssigned,
type,
vmOcid
FROM azure_isv.oracle_database.virtual_network_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudvmclustername = '{{ cloudvmclustername }}' -- required
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

Create a VirtualNetworkAddress.

```sql
INSERT INTO azure_isv.oracle_database.virtual_network_addresses (
properties,
resource_group_name,
cloudvmclustername,
virtualnetworkaddressname,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cloudvmclustername }}',
'{{ virtualnetworkaddressname }}',
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
- name: virtual_network_addresses
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_addresses resource.
    - name: cloudvmclustername
      value: "{{ cloudvmclustername }}"
      description: Required parameter for the virtual_network_addresses resource.
    - name: virtualnetworkaddressname
      value: "{{ virtualnetworkaddressname }}"
      description: Required parameter for the virtual_network_addresses resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_addresses resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        ipAddress: "{{ ipAddress }}"
        vmOcid: "{{ vmOcid }}"
        ocid: "{{ ocid }}"
        domain: "{{ domain }}"
        lifecycleDetails: "{{ lifecycleDetails }}"
        provisioningState: "{{ provisioningState }}"
        lifecycleState: "{{ lifecycleState }}"
        timeAssigned: "{{ timeAssigned }}"
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

Create a VirtualNetworkAddress.

```sql
REPLACE azure_isv.oracle_database.virtual_network_addresses
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cloudvmclustername = '{{ cloudvmclustername }}' --required
AND virtualnetworkaddressname = '{{ virtualnetworkaddressname }}' --required
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

Delete a VirtualNetworkAddress.

```sql
DELETE FROM azure_isv.oracle_database.virtual_network_addresses
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cloudvmclustername = '{{ cloudvmclustername }}' --required
AND virtualnetworkaddressname = '{{ virtualnetworkaddressname }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
