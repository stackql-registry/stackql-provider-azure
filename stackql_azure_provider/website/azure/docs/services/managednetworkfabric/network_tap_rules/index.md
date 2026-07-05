--- 
title: network_tap_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - network_tap_rules
  - managednetworkfabric
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

Creates, updates, deletes, gets or lists a <code>network_tap_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_tap_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managednetworkfabric.network_tap_rules" /></td></tr>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationType" /></td>
    <td><code>string</code></td>
    <td>Input method to configure Network Tap Rule. Required. Known values are: "File" and "Inline". (File, Inline)</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMatchConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of dynamic match configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="globalNetworkTapRuleActions" /></td>
    <td><code>object</code></td>
    <td>Global network tap rule actions.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySelector" /></td>
    <td><code>object</code></td>
    <td>The selection of the managed identity to use with this storage account. The identity type must be either system assigned or user assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="matchConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of match configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricIds" /></td>
    <td><code>array</code></td>
    <td>Associated Network Fabric Resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="networkTapId" /></td>
    <td><code>string</code></td>
    <td>The ARM resource Id of the NetworkTap.</td>
</tr>
<tr>
    <td><CopyableCode code="networkTapIds" /></td>
    <td><code>array</code></td>
    <td>The ARM resource Id of the NetworkTap Rules.</td>
</tr>
<tr>
    <td><CopyableCode code="pollingIntervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Polling interval in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
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
    <td><CopyableCode code="tapRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Network Tap Rules file URL.</td>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationType" /></td>
    <td><code>string</code></td>
    <td>Input method to configure Network Tap Rule. Required. Known values are: "File" and "Inline". (File, Inline)</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMatchConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of dynamic match configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="globalNetworkTapRuleActions" /></td>
    <td><code>object</code></td>
    <td>Global network tap rule actions.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySelector" /></td>
    <td><code>object</code></td>
    <td>The selection of the managed identity to use with this storage account. The identity type must be either system assigned or user assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="matchConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of match configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricIds" /></td>
    <td><code>array</code></td>
    <td>Associated Network Fabric Resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="networkTapId" /></td>
    <td><code>string</code></td>
    <td>The ARM resource Id of the NetworkTap.</td>
</tr>
<tr>
    <td><CopyableCode code="networkTapIds" /></td>
    <td><code>array</code></td>
    <td>The ARM resource Id of the NetworkTap Rules.</td>
</tr>
<tr>
    <td><CopyableCode code="pollingIntervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Polling interval in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
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
    <td><CopyableCode code="tapRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Network Tap Rules file URL.</td>
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
    <td><CopyableCode code="administrativeState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the resource. Known values are: "Enabled", "Disabled", "MAT", "RMA", "UnderMaintenance", and "EnabledDegraded". (Enabled, Disabled, MAT, RMA, UnderMaintenance, EnabledDegraded)</td>
</tr>
<tr>
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationState" /></td>
    <td><code>string</code></td>
    <td>Configuration state of the resource. Known values are: "Succeeded", "Failed", "Rejected", "Accepted", "Provisioned", "ErrorProvisioning", "Deprovisioning", "Deprovisioned", "ErrorDeprovisioning", "DeferredControl", "Provisioning", "PendingCommit", and "PendingAdministrativeUpdate". (Succeeded, Failed, Rejected, Accepted, Provisioned, ErrorProvisioning, Deprovisioning, Deprovisioned, ErrorDeprovisioning, DeferredControl, Provisioning, PendingCommit, PendingAdministrativeUpdate)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationType" /></td>
    <td><code>string</code></td>
    <td>Input method to configure Network Tap Rule. Required. Known values are: "File" and "Inline". (File, Inline)</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicMatchConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of dynamic match configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="globalNetworkTapRuleActions" /></td>
    <td><code>object</code></td>
    <td>Global network tap rule actions.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySelector" /></td>
    <td><code>object</code></td>
    <td>The selection of the managed identity to use with this storage account. The identity type must be either system assigned or user assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last sync timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="matchConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of match configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricIds" /></td>
    <td><code>array</code></td>
    <td>Associated Network Fabric Resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="networkTapId" /></td>
    <td><code>string</code></td>
    <td>The ARM resource Id of the NetworkTap.</td>
</tr>
<tr>
    <td><CopyableCode code="networkTapIds" /></td>
    <td><code>array</code></td>
    <td>The ARM resource Id of the NetworkTap Rules.</td>
</tr>
<tr>
    <td><CopyableCode code="pollingIntervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>Polling interval in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
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
    <td><CopyableCode code="tapRulesUrl" /></td>
    <td><code>string</code></td>
    <td>Network Tap Rules file URL.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Network Tap Rule resource details.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Tap Rule resources in the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the Network Tap Rule resources in the given subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create Network Tap Rule resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update certain properties of the Network Tap Rule resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Network Tap Rule resource.</td>
</tr>
<tr>
    <td><a href="#update_administrative_state"><CopyableCode code="update_administrative_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements the operation to the underlying resources.</td>
</tr>
<tr>
    <td><a href="#resync"><CopyableCode code="resync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements the operation to the underlying resources.</td>
</tr>
<tr>
    <td><a href="#validate_configuration"><CopyableCode code="validate_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_tap_rule_name"><code>network_tap_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements the operation to the underlying resources.</td>
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
<tr id="parameter-network_tap_rule_name">
    <td><CopyableCode code="network_tap_rule_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Tap Rule. Required.</td>
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

Get Network Tap Rule resource details.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
configurationType,
dynamicMatchConfigurations,
globalNetworkTapRuleActions,
identity,
identitySelector,
lastOperation,
lastSyncedTime,
location,
matchConfigurations,
networkFabricIds,
networkTapId,
networkTapIds,
pollingIntervalInSeconds,
provisioningState,
systemData,
tags,
tapRulesUrl,
type
FROM azure.managednetworkfabric.network_tap_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_tap_rule_name = '{{ network_tap_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all the Network Tap Rule resources in the given resource group.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
configurationType,
dynamicMatchConfigurations,
globalNetworkTapRuleActions,
identity,
identitySelector,
lastOperation,
lastSyncedTime,
location,
matchConfigurations,
networkFabricIds,
networkTapId,
networkTapIds,
pollingIntervalInSeconds,
provisioningState,
systemData,
tags,
tapRulesUrl,
type
FROM azure.managednetworkfabric.network_tap_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all the Network Tap Rule resources in the given subscription.

```sql
SELECT
id,
name,
administrativeState,
annotation,
configurationState,
configurationType,
dynamicMatchConfigurations,
globalNetworkTapRuleActions,
identity,
identitySelector,
lastOperation,
lastSyncedTime,
location,
matchConfigurations,
networkFabricIds,
networkTapId,
networkTapIds,
pollingIntervalInSeconds,
provisioningState,
systemData,
tags,
tapRulesUrl,
type
FROM azure.managednetworkfabric.network_tap_rules
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create Network Tap Rule resource.

```sql
INSERT INTO azure.managednetworkfabric.network_tap_rules (
tags,
location,
properties,
identity,
resource_group_name,
network_tap_rule_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_tap_rule_name }}',
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
- name: network_tap_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_tap_rules resource.
    - name: network_tap_rule_name
      value: "{{ network_tap_rule_name }}"
      description: Required parameter for the network_tap_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_tap_rules resource.
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
        The NetworkTapRule Properties. Required.
      value:
        annotation: "{{ annotation }}"
        configurationType: "{{ configurationType }}"
        tapRulesUrl: "{{ tapRulesUrl }}"
        identitySelector:
          identityType: "{{ identityType }}"
          userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
        matchConfigurations:
          - matchConfigurationName: "{{ matchConfigurationName }}"
            sequenceNumber: {{ sequenceNumber }}
            ipAddressType: "{{ ipAddressType }}"
            matchConditions: "{{ matchConditions }}"
            actions: "{{ actions }}"
        dynamicMatchConfigurations:
          - ipGroups: "{{ ipGroups }}"
            vlanGroups: "{{ vlanGroups }}"
            portGroups: "{{ portGroups }}"
        networkTapId: "{{ networkTapId }}"
        networkTapIds:
          - "{{ networkTapIds }}"
        pollingIntervalInSeconds: {{ pollingIntervalInSeconds }}
        lastSyncedTime: "{{ lastSyncedTime }}"
        globalNetworkTapRuleActions:
          enableCount: "{{ enableCount }}"
          truncate: "{{ truncate }}"
        lastOperation:
          details: "{{ details }}"
        networkFabricIds:
          - "{{ networkFabricIds }}"
        configurationState: "{{ configurationState }}"
        provisioningState: "{{ provisioningState }}"
        administrativeState: "{{ administrativeState }}"
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

Update certain properties of the Network Tap Rule resource.

```sql
UPDATE azure.managednetworkfabric.network_tap_rules
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_tap_rule_name = '{{ network_tap_rule_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete Network Tap Rule resource.

```sql
DELETE FROM azure.managednetworkfabric.network_tap_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_tap_rule_name = '{{ network_tap_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_administrative_state"
    values={[
        { label: 'update_administrative_state', value: 'update_administrative_state' },
        { label: 'resync', value: 'resync' },
        { label: 'validate_configuration', value: 'validate_configuration' }
    ]}
>
<TabItem value="update_administrative_state">

Implements the operation to the underlying resources.

```sql
EXEC azure.managednetworkfabric.network_tap_rules.update_administrative_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_tap_rule_name='{{ network_tap_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"state": "{{ state }}"
}'
;
```
</TabItem>
<TabItem value="resync">

Implements the operation to the underlying resources.

```sql
EXEC azure.managednetworkfabric.network_tap_rules.resync 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_tap_rule_name='{{ network_tap_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_configuration">

Implements the operation to the underlying resources.

```sql
EXEC azure.managednetworkfabric.network_tap_rules.validate_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_tap_rule_name='{{ network_tap_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
