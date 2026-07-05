--- 
title: edge_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_machines
  - azurestackhci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>edge_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="edge_machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azurestackhci.edge_machines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="arcGatewayResourceId" /></td>
    <td><code>string</code></td>
    <td>Link to Arc Gateway ARM resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="arcMachineResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>Optional property to create arc machine in custom resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="arcMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>Arc machine instance resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="claimedBy" /></td>
    <td><code>string</code></td>
    <td>Tracks the ID of the consuming resource, setting the machine as in-use.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>machine connectivity status. Known values are: "NotSpecified", "Disconnected", and "Connected". (NotSpecified, Disconnected, Connected)</td>
</tr>
<tr>
    <td><CopyableCode code="devicePoolResourceId" /></td>
    <td><code>string</code></td>
    <td>A machine can only be assigned to single device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="edgeMachineKind" /></td>
    <td><code>string</code></td>
    <td>Edge Machine type. Known values are: "Standard" and "Dedicated". (Standard, Dedicated)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time data updated to service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineState" /></td>
    <td><code>string</code></td>
    <td>OS configuration status details. Known values are: "Created", "Registering", "Unpurposed", "Transitioning", "Purposed", "Updating", "Resetting", "Failed", and "Preparing". (Created, Registering, Unpurposed, Transitioning, Purposed, Updating, Resetting, Failed, Preparing)</td>
</tr>
<tr>
    <td><CopyableCode code="operationDetails" /></td>
    <td><code>array</code></td>
    <td>operation status details for edge machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownershipVoucherDetails" /></td>
    <td><code>object</code></td>
    <td>Ownership voucher details for provisioned machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningDetails" /></td>
    <td><code>object</code></td>
    <td>Details for device provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Reported properties for edge machine.</td>
</tr>
<tr>
    <td><CopyableCode code="siteDetails" /></td>
    <td><code>object</code></td>
    <td>Service fetches common configuration from site.</td>
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
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="arcGatewayResourceId" /></td>
    <td><code>string</code></td>
    <td>Link to Arc Gateway ARM resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="arcMachineResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>Optional property to create arc machine in custom resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="arcMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>Arc machine instance resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="claimedBy" /></td>
    <td><code>string</code></td>
    <td>Tracks the ID of the consuming resource, setting the machine as in-use.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>machine connectivity status. Known values are: "NotSpecified", "Disconnected", and "Connected". (NotSpecified, Disconnected, Connected)</td>
</tr>
<tr>
    <td><CopyableCode code="devicePoolResourceId" /></td>
    <td><code>string</code></td>
    <td>A machine can only be assigned to single device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="edgeMachineKind" /></td>
    <td><code>string</code></td>
    <td>Edge Machine type. Known values are: "Standard" and "Dedicated". (Standard, Dedicated)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time data updated to service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineState" /></td>
    <td><code>string</code></td>
    <td>OS configuration status details. Known values are: "Created", "Registering", "Unpurposed", "Transitioning", "Purposed", "Updating", "Resetting", "Failed", and "Preparing". (Created, Registering, Unpurposed, Transitioning, Purposed, Updating, Resetting, Failed, Preparing)</td>
</tr>
<tr>
    <td><CopyableCode code="operationDetails" /></td>
    <td><code>array</code></td>
    <td>operation status details for edge machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownershipVoucherDetails" /></td>
    <td><code>object</code></td>
    <td>Ownership voucher details for provisioned machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningDetails" /></td>
    <td><code>object</code></td>
    <td>Details for device provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Reported properties for edge machine.</td>
</tr>
<tr>
    <td><CopyableCode code="siteDetails" /></td>
    <td><code>object</code></td>
    <td>Service fetches common configuration from site.</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="arcGatewayResourceId" /></td>
    <td><code>string</code></td>
    <td>Link to Arc Gateway ARM resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="arcMachineResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>Optional property to create arc machine in custom resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="arcMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>Arc machine instance resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="claimedBy" /></td>
    <td><code>string</code></td>
    <td>Tracks the ID of the consuming resource, setting the machine as in-use.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>machine connectivity status. Known values are: "NotSpecified", "Disconnected", and "Connected". (NotSpecified, Disconnected, Connected)</td>
</tr>
<tr>
    <td><CopyableCode code="devicePoolResourceId" /></td>
    <td><code>string</code></td>
    <td>A machine can only be assigned to single device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="edgeMachineKind" /></td>
    <td><code>string</code></td>
    <td>Edge Machine type. Known values are: "Standard" and "Dedicated". (Standard, Dedicated)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time data updated to service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="machineState" /></td>
    <td><code>string</code></td>
    <td>OS configuration status details. Known values are: "Created", "Registering", "Unpurposed", "Transitioning", "Purposed", "Updating", "Resetting", "Failed", and "Preparing". (Created, Registering, Unpurposed, Transitioning, Purposed, Updating, Resetting, Failed, Preparing)</td>
</tr>
<tr>
    <td><CopyableCode code="operationDetails" /></td>
    <td><code>array</code></td>
    <td>operation status details for edge machine.</td>
</tr>
<tr>
    <td><CopyableCode code="ownershipVoucherDetails" /></td>
    <td><code>object</code></td>
    <td>Ownership voucher details for provisioned machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningDetails" /></td>
    <td><code>object</code></td>
    <td>Details for device provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="reportedProperties" /></td>
    <td><code>object</code></td>
    <td>Reported properties for edge machine.</td>
</tr>
<tr>
    <td><CopyableCode code="siteDetails" /></td>
    <td><code>object</code></td>
    <td>Service fetches common configuration from site.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an edge machine.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all edge machines in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all edge machines in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an edge machine.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an edge machine.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an edge machine.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-edge_machine_name"><code>edge_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an edge machine.</td>
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
<tr id="parameter-edge_machine_name">
    <td><CopyableCode code="edge_machine_name" /></td>
    <td><code>string</code></td>
    <td>Name of Device. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get an edge machine.

```sql
SELECT
id,
name,
arcGatewayResourceId,
arcMachineResourceGroupId,
arcMachineResourceId,
claimedBy,
cloudId,
connectivityStatus,
devicePoolResourceId,
edgeMachineKind,
identity,
lastSyncTimestamp,
location,
machineState,
operationDetails,
ownershipVoucherDetails,
provisioningDetails,
provisioningState,
reportedProperties,
siteDetails,
systemData,
tags,
type
FROM azure_stack.azurestackhci.edge_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND edge_machine_name = '{{ edge_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all edge machines in a resource group.

```sql
SELECT
id,
name,
arcGatewayResourceId,
arcMachineResourceGroupId,
arcMachineResourceId,
claimedBy,
cloudId,
connectivityStatus,
devicePoolResourceId,
edgeMachineKind,
identity,
lastSyncTimestamp,
location,
machineState,
operationDetails,
ownershipVoucherDetails,
provisioningDetails,
provisioningState,
reportedProperties,
siteDetails,
systemData,
tags,
type
FROM azure_stack.azurestackhci.edge_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all edge machines in a subscription.

```sql
SELECT
id,
name,
arcGatewayResourceId,
arcMachineResourceGroupId,
arcMachineResourceId,
claimedBy,
cloudId,
connectivityStatus,
devicePoolResourceId,
edgeMachineKind,
identity,
lastSyncTimestamp,
location,
machineState,
operationDetails,
ownershipVoucherDetails,
provisioningDetails,
provisioningState,
reportedProperties,
siteDetails,
systemData,
tags,
type
FROM azure_stack.azurestackhci.edge_machines
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or update an edge machine.

```sql
INSERT INTO azure_stack.azurestackhci.edge_machines (
tags,
location,
properties,
identity,
resource_group_name,
edge_machine_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ edge_machine_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: edge_machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the edge_machines resource.
    - name: edge_machine_name
      value: "{{ edge_machine_name }}"
      description: Required parameter for the edge_machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the edge_machines resource.
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
        The resource-specific properties for this resource.
      value:
        edgeMachineKind: "{{ edgeMachineKind }}"
        provisioningState: "{{ provisioningState }}"
        cloudId: "{{ cloudId }}"
        arcMachineResourceGroupId: "{{ arcMachineResourceGroupId }}"
        arcMachineResourceId: "{{ arcMachineResourceId }}"
        arcGatewayResourceId: "{{ arcGatewayResourceId }}"
        siteDetails:
          siteResourceId: "{{ siteResourceId }}"
          deviceConfiguration:
            network:
              networkAdapters:
                - ipAssignmentType: "{{ ipAssignmentType }}"
                  ipAddress: "{{ ipAddress }}"
                  adapterName: "{{ adapterName }}"
                  macAddress: "{{ macAddress }}"
                  ipAddressRange:
                    startIp: "{{ startIp }}"
                    endIp: "{{ endIp }}"
                  gateway: "{{ gateway }}"
                  subnetMask: "{{ subnetMask }}"
                  dnsAddressArray: "{{ dnsAddressArray }}"
                  vlanId: "{{ vlanId }}"
            hostName: "{{ hostName }}"
            webProxy:
              connectionUri: "{{ connectionUri }}"
              port: "{{ port }}"
              bypassList:
                - "{{ bypassList }}"
            time:
              primaryTimeServer: "{{ primaryTimeServer }}"
              secondaryTimeServer: "{{ secondaryTimeServer }}"
              timeZone: "{{ timeZone }}"
            storage:
              partitionSize: "{{ partitionSize }}"
        ownershipVoucherDetails:
          ownershipVoucher: "{{ ownershipVoucher }}"
          ownerKeyType: "{{ ownerKeyType }}"
          validationDetails:
            validationStatus: "{{ validationStatus }}"
            serialNumber: "{{ serialNumber }}"
            id: "{{ id }}"
            manufacturer: "{{ manufacturer }}"
            modelName: "{{ modelName }}"
            version: "{{ version }}"
            azureMachineId: "{{ azureMachineId }}"
            error:
              code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details:
                - code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
              additionalInfo:
                - type: "{{ type }}"
                  info: "{{ info }}"
        provisioningDetails:
          osProfile:
            osName: "{{ osName }}"
            osType: "{{ osType }}"
            osVersion: "{{ osVersion }}"
            osImageLocation: "{{ osImageLocation }}"
            vsrVersion: "{{ vsrVersion }}"
            imageHash: "{{ imageHash }}"
            gpgPubKey: "{{ gpgPubKey }}"
            operationType: "{{ operationType }}"
          userDetails:
            - userName: "{{ userName }}"
              secretType: "{{ secretType }}"
              secretLocation: "{{ secretLocation }}"
              sshPubKey: "{{ sshPubKey }}"
        devicePoolResourceId: "{{ devicePoolResourceId }}"
        machineState: "{{ machineState }}"
        connectivityStatus: "{{ connectivityStatus }}"
        claimedBy: "{{ claimedBy }}"
        reportedProperties:
          lastUpdated: "{{ lastUpdated }}"
          networkProfile:
            nicDetails:
              - adapterName: "{{ adapterName }}"
                interfaceDescription: "{{ interfaceDescription }}"
                componentId: "{{ componentId }}"
                driverVersion: "{{ driverVersion }}"
                ip4Address: "{{ ip4Address }}"
                subnetMask: "{{ subnetMask }}"
                defaultGateway: "{{ defaultGateway }}"
                dnsServers: "{{ dnsServers }}"
                defaultIsolationId: "{{ defaultIsolationId }}"
                macAddress: "{{ macAddress }}"
                slot: "{{ slot }}"
                switchName: "{{ switchName }}"
                nicType: "{{ nicType }}"
                vlanId: "{{ vlanId }}"
                nicStatus: "{{ nicStatus }}"
                rdmaCapability: "{{ rdmaCapability }}"
            switchDetails:
              - switchName: "{{ switchName }}"
                switchType: "{{ switchType }}"
                extensions: "{{ extensions }}"
          osProfile:
            bootType: "{{ bootType }}"
            assemblyVersion: "{{ assemblyVersion }}"
            osType: "{{ osType }}"
            osSku: "{{ osSku }}"
            osVersion: "{{ osVersion }}"
            buildNumber: "{{ buildNumber }}"
            baseImageVersion: "{{ baseImageVersion }}"
            imageVersion: "{{ imageVersion }}"
          hardwareProfile:
            cpuCores: {{ cpuCores }}
            cpuSockets: {{ cpuSockets }}
            memoryCapacityInGb: {{ memoryCapacityInGb }}
            model: "{{ model }}"
            manufacturer: "{{ manufacturer }}"
            serialNumber: "{{ serialNumber }}"
            processorType: "{{ processorType }}"
          storageProfile:
            poolableDisksCount: {{ poolableDisksCount }}
          sbeDeploymentPackageInfo:
            code: "{{ code }}"
            message: "{{ message }}"
            sbeManifest: "{{ sbeManifest }}"
          extensionProfile:
            extensions:
              - extensionName: "{{ extensionName }}"
                state: "{{ state }}"
                errorDetails: "{{ errorDetails }}"
                extensionResourceId: "{{ extensionResourceId }}"
                typeHandlerVersion: "{{ typeHandlerVersion }}"
                managedBy: "{{ managedBy }}"
        operationDetails:
          - name: "{{ name }}"
            id: "{{ id }}"
            type: "{{ type }}"
            resourceId: "{{ resourceId }}"
            description: "{{ description }}"
            status: "{{ status }}"
            error:
              code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details:
                - code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
              additionalInfo:
                - type: "{{ type }}"
                  info: "{{ info }}"
        lastSyncTimestamp: "{{ lastSyncTimestamp }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update an edge machine.

```sql
UPDATE azure_stack.azurestackhci.edge_machines
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND edge_machine_name = '{{ edge_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type;
```
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

Create or update an edge machine.

```sql
REPLACE azure_stack.azurestackhci.edge_machines
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND edge_machine_name = '{{ edge_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Delete an edge machine.

```sql
DELETE FROM azure_stack.azurestackhci.edge_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND edge_machine_name = '{{ edge_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
