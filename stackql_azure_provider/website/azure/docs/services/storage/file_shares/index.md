--- 
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
  - storage
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.file_shares" /></td></tr>
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
    <td><CopyableCode code="accessTier" /></td>
    <td><code>string</code></td>
    <td>Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium. Known values are: "TransactionOptimized", "Hot", "Cool", and "Premium". (TransactionOptimized, Hot, Cool, Premium)</td>
</tr>
<tr>
    <td><CopyableCode code="accessTierChangeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last modification time for share access tier.</td>
</tr>
<tr>
    <td><CopyableCode code="accessTierStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates if there is a pending transition for access tier.</td>
</tr>
<tr>
    <td><CopyableCode code="deleted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the share was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The deleted time if the share was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledProtocols" /></td>
    <td><code>string</code></td>
    <td>The authentication protocol that is used for the file share. Can only be specified when creating a share. Known values are: "SMB" and "NFS". (SMB, NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSharePaidBursting" /></td>
    <td><code>object</code></td>
    <td>File Share Paid Bursting properties.</td>
</tr>
<tr>
    <td><CopyableCode code="includedBurstIops" /></td>
    <td><code>integer</code></td>
    <td>The calculated burst IOPS of the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the date and time the share was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="leaseDuration" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the lease on a share is of infinite or fixed duration, only when the share is leased. Known values are: "Infinite" and "Fixed". (Infinite, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseState" /></td>
    <td><code>string</code></td>
    <td>Lease state of the share. Known values are: "Available", "Leased", "Expired", "Breaking", and "Broken". (Available, Leased, Expired, Breaking, Broken)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseStatus" /></td>
    <td><code>string</code></td>
    <td>The lease status of the share. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="maxBurstCreditsForIops" /></td>
    <td><code>integer</code></td>
    <td>The calculated maximum burst credits for the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A name-value pair to associate with the share as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAllowedProvisionedBandwidthDowngradeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the next allowed provisioned bandwidth downgrade time for the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAllowedProvisionedIopsDowngradeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the next allowed provisioned IOPS downgrade time for the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAllowedQuotaDowngradeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the next allowed provisioned storage size downgrade time for the share. This property is only for file shares created under Files Provisioned v1 SSD and Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedBandwidthMibps" /></td>
    <td><code>integer</code></td>
    <td>The provisioned bandwidth of the share, in mebibytes per second. This property is only for file shares created under Files Provisioned v2 account type. Please refer to the GetFileServiceUsage API response for the minimum and maximum allowed value for provisioned bandwidth.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIops" /></td>
    <td><code>integer</code></td>
    <td>The provisioned IOPS of the share. This property is only for file shares created under Files Provisioned v2 account type. Please refer to the GetFileServiceUsage API response for the minimum and maximum allowed value for provisioned IOPS.</td>
</tr>
<tr>
    <td><CopyableCode code="remainingRetentionDays" /></td>
    <td><code>integer</code></td>
    <td>Remaining retention days for share that was soft deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="rootSquash" /></td>
    <td><code>string</code></td>
    <td>The property is for NFS share only. The default is NoRootSquash. Known values are: "NoRootSquash", "RootSquash", and "AllSquash". (NoRootSquash, RootSquash, AllSquash)</td>
</tr>
<tr>
    <td><CopyableCode code="shareQuota" /></td>
    <td><code>integer</code></td>
    <td>The provisioned size of the share, in gibibytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400. For file shares created under Files Provisioned v2 account type, please refer to the GetFileServiceUsage API response for the minimum and maximum allowed provisioned storage size.</td>
</tr>
<tr>
    <td><CopyableCode code="shareUsageBytes" /></td>
    <td><code>integer</code></td>
    <td>The approximate size of the data stored on the share. Note that this value may not include all recently created or recently resized files.</td>
</tr>
<tr>
    <td><CopyableCode code="signedIdentifiers" /></td>
    <td><code>array</code></td>
    <td>List of stored access policies specified on the share.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of share snapshot returned in the response of list shares with expand param "snapshots".</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the share.</td>
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
    <td><CopyableCode code="accessTier" /></td>
    <td><code>string</code></td>
    <td>Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium. Known values are: "TransactionOptimized", "Hot", "Cool", and "Premium". (TransactionOptimized, Hot, Cool, Premium)</td>
</tr>
<tr>
    <td><CopyableCode code="accessTierChangeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last modification time for share access tier.</td>
</tr>
<tr>
    <td><CopyableCode code="accessTierStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates if there is a pending transition for access tier.</td>
</tr>
<tr>
    <td><CopyableCode code="deleted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the share was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The deleted time if the share was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledProtocols" /></td>
    <td><code>string</code></td>
    <td>The authentication protocol that is used for the file share. Can only be specified when creating a share. Known values are: "SMB" and "NFS". (SMB, NFS)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSharePaidBursting" /></td>
    <td><code>object</code></td>
    <td>File Share Paid Bursting properties.</td>
</tr>
<tr>
    <td><CopyableCode code="includedBurstIops" /></td>
    <td><code>integer</code></td>
    <td>The calculated burst IOPS of the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the date and time the share was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="leaseDuration" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the lease on a share is of infinite or fixed duration, only when the share is leased. Known values are: "Infinite" and "Fixed". (Infinite, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseState" /></td>
    <td><code>string</code></td>
    <td>Lease state of the share. Known values are: "Available", "Leased", "Expired", "Breaking", and "Broken". (Available, Leased, Expired, Breaking, Broken)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseStatus" /></td>
    <td><code>string</code></td>
    <td>The lease status of the share. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="maxBurstCreditsForIops" /></td>
    <td><code>integer</code></td>
    <td>The calculated maximum burst credits for the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A name-value pair to associate with the share as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAllowedProvisionedBandwidthDowngradeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the next allowed provisioned bandwidth downgrade time for the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAllowedProvisionedIopsDowngradeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the next allowed provisioned IOPS downgrade time for the share. This property is only for file shares created under Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAllowedQuotaDowngradeTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the next allowed provisioned storage size downgrade time for the share. This property is only for file shares created under Files Provisioned v1 SSD and Files Provisioned v2 account type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedBandwidthMibps" /></td>
    <td><code>integer</code></td>
    <td>The provisioned bandwidth of the share, in mebibytes per second. This property is only for file shares created under Files Provisioned v2 account type. Please refer to the GetFileServiceUsage API response for the minimum and maximum allowed value for provisioned bandwidth.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIops" /></td>
    <td><code>integer</code></td>
    <td>The provisioned IOPS of the share. This property is only for file shares created under Files Provisioned v2 account type. Please refer to the GetFileServiceUsage API response for the minimum and maximum allowed value for provisioned IOPS.</td>
</tr>
<tr>
    <td><CopyableCode code="remainingRetentionDays" /></td>
    <td><code>integer</code></td>
    <td>Remaining retention days for share that was soft deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="rootSquash" /></td>
    <td><code>string</code></td>
    <td>The property is for NFS share only. The default is NoRootSquash. Known values are: "NoRootSquash", "RootSquash", and "AllSquash". (NoRootSquash, RootSquash, AllSquash)</td>
</tr>
<tr>
    <td><CopyableCode code="shareQuota" /></td>
    <td><code>integer</code></td>
    <td>The provisioned size of the share, in gibibytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400. For file shares created under Files Provisioned v2 account type, please refer to the GetFileServiceUsage API response for the minimum and maximum allowed provisioned storage size.</td>
</tr>
<tr>
    <td><CopyableCode code="shareUsageBytes" /></td>
    <td><code>integer</code></td>
    <td>The approximate size of the data stored on the share. Note that this value may not include all recently created or recently resized files.</td>
</tr>
<tr>
    <td><CopyableCode code="signedIdentifiers" /></td>
    <td><code>array</code></td>
    <td>List of stored access policies specified on the share.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of share snapshot returned in the response of list shares with expand param "snapshots".</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the share.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-x-ms-snapshot"><code>x-ms-snapshot</code></a></td>
    <td>Gets properties of a specified share.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$maxpagesize"><code>$maxpagesize</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all shares.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-snapshot"><code>x-ms-snapshot</code></a>, <a href="#parameter-$include"><code>$include</code></a></td>
    <td>Deletes specified share under its account.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-deletedShareName"><code>deletedShareName</code></a>, <a href="#parameter-deletedShareVersion"><code>deletedShareVersion</code></a></td>
    <td></td>
    <td>Restore a file share within a valid retention days if share soft delete is enabled.</td>
</tr>
<tr>
    <td><a href="#lease"><CopyableCode code="lease" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td><a href="#parameter-x-ms-snapshot"><code>x-ms-snapshot</code></a></td>
    <td>The Lease Share operation establishes and manages a lock on a share for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.</td>
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
    <td>The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-share_name">
    <td><CopyableCode code="share_name" /></td>
    <td><code>string</code></td>
    <td>The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Optional, used to expand the properties within share's properties. Valid values are: snapshots. Should be passed as a string with delimiter ','. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Optional. When specified, only share names starting with the filter will be listed. Default value is None.</td>
</tr>
<tr id="parameter-$include">
    <td><CopyableCode code="$include" /></td>
    <td><code>string</code></td>
    <td>Optional. Valid values are: snapshots, leased-snapshots, none. The default value is snapshots. For 'snapshots', the file share is deleted including all of its file share snapshots. If the file share contains leased-snapshots, the deletion fails. For 'leased-snapshots', the file share is deleted included all of its file share snapshots (leased/unleased). For 'none', the file share is deleted if it has no share snapshots. If the file share contains any snapshots (leased or unleased), the deletion fails. Default value is None.</td>
</tr>
<tr id="parameter-$maxpagesize">
    <td><CopyableCode code="$maxpagesize" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-ms-snapshot">
    <td><CopyableCode code="x-ms-snapshot" /></td>
    <td><code>string</code></td>
    <td>Optional. Specify the snapshot time to lease a snapshot. Default value is None.</td>
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

Gets properties of a specified share.

```sql
SELECT
id,
name,
accessTier,
accessTierChangeTime,
accessTierStatus,
deleted,
deletedTime,
enabledProtocols,
etag,
fileSharePaidBursting,
includedBurstIops,
lastModifiedTime,
leaseDuration,
leaseState,
leaseStatus,
maxBurstCreditsForIops,
metadata,
nextAllowedProvisionedBandwidthDowngradeTime,
nextAllowedProvisionedIopsDowngradeTime,
nextAllowedQuotaDowngradeTime,
provisionedBandwidthMibps,
provisionedIops,
remainingRetentionDays,
rootSquash,
shareQuota,
shareUsageBytes,
signedIdentifiers,
snapshotTime,
systemData,
type,
version
FROM azure.storage.file_shares
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND x-ms-snapshot = '{{ x-ms-snapshot }}'
;
```
</TabItem>
<TabItem value="list">

Lists all shares.

```sql
SELECT
id,
name,
accessTier,
accessTierChangeTime,
accessTierStatus,
deleted,
deletedTime,
enabledProtocols,
etag,
fileSharePaidBursting,
includedBurstIops,
lastModifiedTime,
leaseDuration,
leaseState,
leaseStatus,
maxBurstCreditsForIops,
metadata,
nextAllowedProvisionedBandwidthDowngradeTime,
nextAllowedProvisionedIopsDowngradeTime,
nextAllowedQuotaDowngradeTime,
provisionedBandwidthMibps,
provisionedIops,
remainingRetentionDays,
rootSquash,
shareQuota,
shareUsageBytes,
signedIdentifiers,
snapshotTime,
systemData,
type,
version
FROM azure.storage.file_shares
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $maxpagesize = '{{ $maxpagesize }}'
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
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

Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share.

```sql
INSERT INTO azure.storage.file_shares (
properties,
resource_group_name,
account_name,
share_name,
subscription_id,
$expand
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ share_name }}',
'{{ subscription_id }}',
'{{ $expand }}'
RETURNING
id,
name,
etag,
properties,
systemData,
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
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the file_shares resource.
    - name: share_name
      value: "{{ share_name }}"
      description: Required parameter for the file_shares resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the file_shares resource.
    - name: properties
      description: |
        Properties of the file share.
      value:
        lastModifiedTime: "{{ lastModifiedTime }}"
        metadata: "{{ metadata }}"
        shareQuota: {{ shareQuota }}
        provisionedIops: {{ provisionedIops }}
        provisionedBandwidthMibps: {{ provisionedBandwidthMibps }}
        includedBurstIops: {{ includedBurstIops }}
        maxBurstCreditsForIops: {{ maxBurstCreditsForIops }}
        nextAllowedQuotaDowngradeTime: "{{ nextAllowedQuotaDowngradeTime }}"
        nextAllowedProvisionedIopsDowngradeTime: "{{ nextAllowedProvisionedIopsDowngradeTime }}"
        nextAllowedProvisionedBandwidthDowngradeTime: "{{ nextAllowedProvisionedBandwidthDowngradeTime }}"
        enabledProtocols: "{{ enabledProtocols }}"
        rootSquash: "{{ rootSquash }}"
        version: "{{ version }}"
        deleted: {{ deleted }}
        deletedTime: "{{ deletedTime }}"
        remainingRetentionDays: {{ remainingRetentionDays }}
        accessTier: "{{ accessTier }}"
        accessTierChangeTime: "{{ accessTierChangeTime }}"
        accessTierStatus: "{{ accessTierStatus }}"
        shareUsageBytes: {{ shareUsageBytes }}
        leaseStatus: "{{ leaseStatus }}"
        leaseState: "{{ leaseState }}"
        leaseDuration: "{{ leaseDuration }}"
        signedIdentifiers:
          - id: "{{ id }}"
            accessPolicy:
              startTime: "{{ startTime }}"
              expiryTime: "{{ expiryTime }}"
              permission: "{{ permission }}"
        snapshotTime: "{{ snapshotTime }}"
        fileSharePaidBursting:
          paidBurstingEnabled: {{ paidBurstingEnabled }}
          paidBurstingMaxIops: {{ paidBurstingMaxIops }}
          paidBurstingMaxBandwidthMibps: {{ paidBurstingMaxBandwidthMibps }}
    - name: $expand
      value: "{{ $expand }}"
      description: Optional, used to expand the properties within share's properties. Valid values are: snapshots. Should be passed as a string with delimiter ','. Default value is None.
      description: Optional, used to expand the properties within share's properties. Valid values are: snapshots. Should be passed as a string with delimiter ','. Default value is None.
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

Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist.

```sql
UPDATE azure.storage.file_shares
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND share_name = '{{ share_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Deletes specified share under its account.

```sql
DELETE FROM azure.storage.file_shares
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND share_name = '{{ share_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-snapshot = '{{ x-ms-snapshot }}'
AND $include = '{{ $include }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restore"
    values={[
        { label: 'restore', value: 'restore' },
        { label: 'lease', value: 'lease' }
    ]}
>
<TabItem value="restore">

Restore a file share within a valid retention days if share soft delete is enabled.

```sql
EXEC azure.storage.file_shares.restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_name='{{ share_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"deletedShareName": "{{ deletedShareName }}", 
"deletedShareVersion": "{{ deletedShareVersion }}"
}'
;
```
</TabItem>
<TabItem value="lease">

The Lease Share operation establishes and manages a lock on a share for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.

```sql
EXEC azure.storage.file_shares.lease 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_name='{{ share_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-snapshot='{{ x-ms-snapshot }}' 
@@json=
'{
"action": "{{ action }}", 
"leaseId": "{{ leaseId }}", 
"breakPeriod": {{ breakPeriod }}, 
"leaseDuration": {{ leaseDuration }}, 
"proposedLeaseId": "{{ proposedLeaseId }}"
}'
;
```
</TabItem>
</Tabs>
