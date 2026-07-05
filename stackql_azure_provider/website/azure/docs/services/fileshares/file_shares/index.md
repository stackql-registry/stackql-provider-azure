--- 
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
  - fileshares
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

Creates, updates, deletes, gets or lists a <code>file_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="file_shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fileshares.file_shares" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' },
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
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the file share.</td>
</tr>
<tr>
    <td><CopyableCode code="includedBurstIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>Burst IOPS are extra buffer IOPS enabling you to consume more than your provisioned IOPS for a short period of time, depending on the burst credits available for your share.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxBurstIOPerSecCredits" /></td>
    <td><code>integer</code></td>
    <td>Max burst IOPS credits shows the maximum number of burst credits the share can have at the current IOPS provisioning level.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaTier" /></td>
    <td><code>string</code></td>
    <td>The storage media tier of the file share. "SSD" (SSD)</td>
</tr>
<tr>
    <td><CopyableCode code="mountName" /></td>
    <td><code>string</code></td>
    <td>The name of the file share as seen by the end user when mounting the share, such as in a URI or UNC format in their operating system.</td>
</tr>
<tr>
    <td><CopyableCode code="nfsProtocolProperties" /></td>
    <td><code>object</code></td>
    <td>Protocol settings specific NFS.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of associated private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The file sharing protocol for this file share. "NFS" (NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>The provisioned IO / sec of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSecNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned IOPS for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedStorageGiB" /></td>
    <td><code>integer</code></td>
    <td>The provisioned storage size of the share in GiB (1 GiB is 1024^3 bytes or 1073741824 bytes). A component of the file share's bill is the provisioned storage, regardless of the amount of used storage.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedStorageNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned storage for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputMiBPerSec" /></td>
    <td><code>integer</code></td>
    <td>The provisioned throughput / sec of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned throughput for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", "Created", "TransientFailure", "Creating", "Patching", and "Posting". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted, Created, TransientFailure, Creating, Patching, Posting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicAccessProperties" /></td>
    <td><code>object</code></td>
    <td>The set of properties for control public access.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Gets or sets allow or disallow public network access to azure managed file share. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancy" /></td>
    <td><code>string</code></td>
    <td>The chosen redundancy level of the file share. Known values are: "Local" and "Zone". (Local, Zone)</td>
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
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the file share.</td>
</tr>
<tr>
    <td><CopyableCode code="includedBurstIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>Burst IOPS are extra buffer IOPS enabling you to consume more than your provisioned IOPS for a short period of time, depending on the burst credits available for your share.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxBurstIOPerSecCredits" /></td>
    <td><code>integer</code></td>
    <td>Max burst IOPS credits shows the maximum number of burst credits the share can have at the current IOPS provisioning level.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaTier" /></td>
    <td><code>string</code></td>
    <td>The storage media tier of the file share. "SSD" (SSD)</td>
</tr>
<tr>
    <td><CopyableCode code="mountName" /></td>
    <td><code>string</code></td>
    <td>The name of the file share as seen by the end user when mounting the share, such as in a URI or UNC format in their operating system.</td>
</tr>
<tr>
    <td><CopyableCode code="nfsProtocolProperties" /></td>
    <td><code>object</code></td>
    <td>Protocol settings specific NFS.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of associated private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The file sharing protocol for this file share. "NFS" (NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>The provisioned IO / sec of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSecNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned IOPS for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedStorageGiB" /></td>
    <td><code>integer</code></td>
    <td>The provisioned storage size of the share in GiB (1 GiB is 1024^3 bytes or 1073741824 bytes). A component of the file share's bill is the provisioned storage, regardless of the amount of used storage.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedStorageNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned storage for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputMiBPerSec" /></td>
    <td><code>integer</code></td>
    <td>The provisioned throughput / sec of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned throughput for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", "Created", "TransientFailure", "Creating", "Patching", and "Posting". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted, Created, TransientFailure, Creating, Patching, Posting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicAccessProperties" /></td>
    <td><code>object</code></td>
    <td>The set of properties for control public access.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Gets or sets allow or disallow public network access to azure managed file share. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancy" /></td>
    <td><code>string</code></td>
    <td>The chosen redundancy level of the file share. Known values are: "Local" and "Zone". (Local, Zone)</td>
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
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the file share.</td>
</tr>
<tr>
    <td><CopyableCode code="includedBurstIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>Burst IOPS are extra buffer IOPS enabling you to consume more than your provisioned IOPS for a short period of time, depending on the burst credits available for your share.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxBurstIOPerSecCredits" /></td>
    <td><code>integer</code></td>
    <td>Max burst IOPS credits shows the maximum number of burst credits the share can have at the current IOPS provisioning level.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaTier" /></td>
    <td><code>string</code></td>
    <td>The storage media tier of the file share. "SSD" (SSD)</td>
</tr>
<tr>
    <td><CopyableCode code="mountName" /></td>
    <td><code>string</code></td>
    <td>The name of the file share as seen by the end user when mounting the share, such as in a URI or UNC format in their operating system.</td>
</tr>
<tr>
    <td><CopyableCode code="nfsProtocolProperties" /></td>
    <td><code>object</code></td>
    <td>Protocol settings specific NFS.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of associated private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The file sharing protocol for this file share. "NFS" (NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>The provisioned IO / sec of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSecNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned IOPS for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedStorageGiB" /></td>
    <td><code>integer</code></td>
    <td>The provisioned storage size of the share in GiB (1 GiB is 1024^3 bytes or 1073741824 bytes). A component of the file share's bill is the provisioned storage, regardless of the amount of used storage.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedStorageNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned storage for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputMiBPerSec" /></td>
    <td><code>integer</code></td>
    <td>The provisioned throughput / sec of the share.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputNextAllowedDowngrade" /></td>
    <td><code>string (date-time)</code></td>
    <td>A date/time value that specifies when the provisioned throughput for the file share is permitted to be reduced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", "Created", "TransientFailure", "Creating", "Patching", and "Posting". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted, Created, TransientFailure, Creating, Patching, Posting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicAccessProperties" /></td>
    <td><code>object</code></td>
    <td>The set of properties for control public access.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Gets or sets allow or disallow public network access to azure managed file share. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancy" /></td>
    <td><code>string</code></td>
    <td>The chosen redundancy level of the file share. Known values are: "Local" and "Zone". (Local, Zone)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a FileShare.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FileShare resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FileShare resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a file share.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a FileShare.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a file share.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a FileShare.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Implements local CheckNameAvailability operations.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the file share, as seen by the administrator through Azure Resource Manager. Required.</td>
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
        { label: 'list_by_parent', value: 'list_by_parent' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a FileShare.

```sql
SELECT
id,
name,
hostName,
includedBurstIOPerSec,
location,
maxBurstIOPerSecCredits,
mediaTier,
mountName,
nfsProtocolProperties,
privateEndpointConnections,
protocol,
provisionedIOPerSec,
provisionedIOPerSecNextAllowedDowngrade,
provisionedStorageGiB,
provisionedStorageNextAllowedDowngrade,
provisionedThroughputMiBPerSec,
provisionedThroughputNextAllowedDowngrade,
provisioningState,
publicAccessProperties,
publicNetworkAccess,
redundancy,
systemData,
tags,
type
FROM azure.fileshares.file_shares
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List FileShare resources by resource group.

```sql
SELECT
id,
name,
hostName,
includedBurstIOPerSec,
location,
maxBurstIOPerSecCredits,
mediaTier,
mountName,
nfsProtocolProperties,
privateEndpointConnections,
protocol,
provisionedIOPerSec,
provisionedIOPerSecNextAllowedDowngrade,
provisionedStorageGiB,
provisionedStorageNextAllowedDowngrade,
provisionedThroughputMiBPerSec,
provisionedThroughputNextAllowedDowngrade,
provisioningState,
publicAccessProperties,
publicNetworkAccess,
redundancy,
systemData,
tags,
type
FROM azure.fileshares.file_shares
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List FileShare resources by subscription ID.

```sql
SELECT
id,
name,
hostName,
includedBurstIOPerSec,
location,
maxBurstIOPerSecCredits,
mediaTier,
mountName,
nfsProtocolProperties,
privateEndpointConnections,
protocol,
provisionedIOPerSec,
provisionedIOPerSecNextAllowedDowngrade,
provisionedStorageGiB,
provisionedStorageNextAllowedDowngrade,
provisionedThroughputMiBPerSec,
provisionedThroughputNextAllowedDowngrade,
provisioningState,
publicAccessProperties,
publicNetworkAccess,
redundancy,
systemData,
tags,
type
FROM azure.fileshares.file_shares
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

Create or update a file share.

```sql
INSERT INTO azure.fileshares.file_shares (
tags,
location,
properties,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: file_shares
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the file_shares resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the file_shares resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the file_shares resource.
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
        mountName: "{{ mountName }}"
        hostName: "{{ hostName }}"
        mediaTier: "{{ mediaTier }}"
        redundancy: "{{ redundancy }}"
        protocol: "{{ protocol }}"
        provisionedStorageGiB: {{ provisionedStorageGiB }}
        provisionedStorageNextAllowedDowngrade: "{{ provisionedStorageNextAllowedDowngrade }}"
        provisionedIOPerSec: {{ provisionedIOPerSec }}
        provisionedIOPerSecNextAllowedDowngrade: "{{ provisionedIOPerSecNextAllowedDowngrade }}"
        provisionedThroughputMiBPerSec: {{ provisionedThroughputMiBPerSec }}
        provisionedThroughputNextAllowedDowngrade: "{{ provisionedThroughputNextAllowedDowngrade }}"
        includedBurstIOPerSec: {{ includedBurstIOPerSec }}
        maxBurstIOPerSecCredits: {{ maxBurstIOPerSecCredits }}
        nfsProtocolProperties:
          rootSquash: "{{ rootSquash }}"
          encryptionInTransitRequired: "{{ encryptionInTransitRequired }}"
        publicAccessProperties:
          allowedSubnets:
            - "{{ allowedSubnets }}"
        provisioningState: "{{ provisioningState }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              groupIds:
                - "{{ groupIds }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
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

Update a FileShare.

```sql
UPDATE azure.fileshares.file_shares
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a file share.

```sql
REPLACE azure.fileshares.file_shares
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete a FileShare.

```sql
DELETE FROM azure.fileshares.file_shares
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Implements local CheckNameAvailability operations.

```sql
EXEC azure.fileshares.file_shares.check_name_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
