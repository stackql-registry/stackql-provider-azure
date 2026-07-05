--- 
title: blob_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_containers
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

Creates, updates, deletes, gets or lists a <code>blob_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="blob_containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.blob_containers" /></td></tr>
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
    <td><CopyableCode code="defaultEncryptionScope" /></td>
    <td><code>string</code></td>
    <td>Default the container to use specified encryption scope for all writes.</td>
</tr>
<tr>
    <td><CopyableCode code="deleted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the blob container was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Blob container deletion time.</td>
</tr>
<tr>
    <td><CopyableCode code="denyEncryptionScopeOverride" /></td>
    <td><code>boolean</code></td>
    <td>Block override of encryption scope from the container default.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNfsV3AllSquash" /></td>
    <td><code>boolean</code></td>
    <td>Enable NFSv3 all squash on blob container.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNfsV3RootSquash" /></td>
    <td><code>boolean</code></td>
    <td>Enable NFSv3 root squash on blob container.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="hasImmutabilityPolicy" /></td>
    <td><code>boolean</code></td>
    <td>The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container.</td>
</tr>
<tr>
    <td><CopyableCode code="hasLegalHold" /></td>
    <td><code>boolean</code></td>
    <td>The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold=true for a given account.</td>
</tr>
<tr>
    <td><CopyableCode code="immutabilityPolicy" /></td>
    <td><code>object</code></td>
    <td>The ImmutabilityPolicy property of the container.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableStorageWithVersioning" /></td>
    <td><code>object</code></td>
    <td>The object level immutability property of the container. The property is immutable and can only be set to true at the container creation time. Existing containers must undergo a migration process.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the date and time the container was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="leaseDuration" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased. Known values are: "Infinite" and "Fixed". (Infinite, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseState" /></td>
    <td><code>string</code></td>
    <td>Lease state of the container. Known values are: "Available", "Leased", "Expired", "Breaking", and "Broken". (Available, Leased, Expired, Breaking, Broken)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseStatus" /></td>
    <td><code>string</code></td>
    <td>The lease status of the container. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="legalHold" /></td>
    <td><code>object</code></td>
    <td>The LegalHold property of the container.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A name-value pair to associate with the container as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="publicAccess" /></td>
    <td><code>string</code></td>
    <td>Specifies whether data in the container may be accessed publicly and the level of access. Known values are: "Container", "Blob", and "None". (Container, Blob, None)</td>
</tr>
<tr>
    <td><CopyableCode code="remainingRetentionDays" /></td>
    <td><code>integer</code></td>
    <td>Remaining retention days for soft deleted blob container.</td>
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
    <td>The version of the deleted blob container.</td>
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
    <td><CopyableCode code="defaultEncryptionScope" /></td>
    <td><code>string</code></td>
    <td>Default the container to use specified encryption scope for all writes.</td>
</tr>
<tr>
    <td><CopyableCode code="deleted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the blob container was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Blob container deletion time.</td>
</tr>
<tr>
    <td><CopyableCode code="denyEncryptionScopeOverride" /></td>
    <td><code>boolean</code></td>
    <td>Block override of encryption scope from the container default.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNfsV3AllSquash" /></td>
    <td><code>boolean</code></td>
    <td>Enable NFSv3 all squash on blob container.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNfsV3RootSquash" /></td>
    <td><code>boolean</code></td>
    <td>Enable NFSv3 root squash on blob container.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="hasImmutabilityPolicy" /></td>
    <td><code>boolean</code></td>
    <td>The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container.</td>
</tr>
<tr>
    <td><CopyableCode code="hasLegalHold" /></td>
    <td><code>boolean</code></td>
    <td>The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold=true for a given account.</td>
</tr>
<tr>
    <td><CopyableCode code="immutabilityPolicy" /></td>
    <td><code>object</code></td>
    <td>The ImmutabilityPolicy property of the container.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableStorageWithVersioning" /></td>
    <td><code>object</code></td>
    <td>The object level immutability property of the container. The property is immutable and can only be set to true at the container creation time. Existing containers must undergo a migration process.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Returns the date and time the container was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="leaseDuration" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased. Known values are: "Infinite" and "Fixed". (Infinite, Fixed)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseState" /></td>
    <td><code>string</code></td>
    <td>Lease state of the container. Known values are: "Available", "Leased", "Expired", "Breaking", and "Broken". (Available, Leased, Expired, Breaking, Broken)</td>
</tr>
<tr>
    <td><CopyableCode code="leaseStatus" /></td>
    <td><code>string</code></td>
    <td>The lease status of the container. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="legalHold" /></td>
    <td><code>object</code></td>
    <td>The LegalHold property of the container.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>A name-value pair to associate with the container as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="publicAccess" /></td>
    <td><code>string</code></td>
    <td>Specifies whether data in the container may be accessed publicly and the level of access. Known values are: "Container", "Blob", and "None". (Container, Blob, None)</td>
</tr>
<tr>
    <td><CopyableCode code="remainingRetentionDays" /></td>
    <td><code>integer</code></td>
    <td>Remaining retention days for soft deleted blob container.</td>
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
    <td>The version of the deleted blob container.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets properties of a specified container.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$maxpagesize"><code>$maxpagesize</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$include"><code>$include</code></a></td>
    <td>Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token.</td>
</tr>
<tr>
    <td><a href="#create_or_update_immutability_policy"><CopyableCode code="create_or_update_immutability_policy" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn't already exist.</td>
</tr>
<tr>
    <td><a href="#create_or_update_immutability_policy"><CopyableCode code="create_or_update_immutability_policy" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes specified container under its account.</td>
</tr>
<tr>
    <td><a href="#get_immutability_policy"><CopyableCode code="get_immutability_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the existing immutability policy along with the corresponding ETag in response headers and body.</td>
</tr>
<tr>
    <td><a href="#delete_immutability_policy"><CopyableCode code="delete_immutability_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, the only way is to delete the container after deleting all expired blobs inside the policy locked container.</td>
</tr>
<tr>
    <td><a href="#set_legal_hold"><CopyableCode code="set_legal_hold" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td></td>
    <td>Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request.</td>
</tr>
<tr>
    <td><a href="#clear_legal_hold"><CopyableCode code="clear_legal_hold" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td></td>
    <td>Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request.</td>
</tr>
<tr>
    <td><a href="#lease"><CopyableCode code="lease" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.</td>
</tr>
<tr>
    <td><a href="#object_level_worm"><CopyableCode code="object_level_worm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation migrates a blob container from container level WORM to object level immutability enabled container. Prerequisites require a container level immutability policy either in locked or unlocked state, Account level versioning must be enabled and there should be no Legal hold on the container.</td>
</tr>
<tr>
    <td><a href="#lock_immutability_policy"><CopyableCode code="lock_immutability_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation.</td>
</tr>
<tr>
    <td><a href="#extend_immutability_policy"><CopyableCode code="extend_immutability_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation.</td>
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
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Optional. When specified, only container names starting with the filter will be listed. Default value is None.</td>
</tr>
<tr id="parameter-$include">
    <td><CopyableCode code="$include" /></td>
    <td><code>string</code></td>
    <td>Optional, used to include the properties for soft deleted blob containers. "deleted" Default value is None.</td>
</tr>
<tr id="parameter-$maxpagesize">
    <td><CopyableCode code="$maxpagesize" /></td>
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

Gets properties of a specified container.

```sql
SELECT
id,
name,
defaultEncryptionScope,
deleted,
deletedTime,
denyEncryptionScopeOverride,
enableNfsV3AllSquash,
enableNfsV3RootSquash,
etag,
hasImmutabilityPolicy,
hasLegalHold,
immutabilityPolicy,
immutableStorageWithVersioning,
lastModifiedTime,
leaseDuration,
leaseState,
leaseStatus,
legalHold,
metadata,
publicAccess,
remainingRetentionDays,
systemData,
type,
version
FROM azure.storage.blob_containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token.

```sql
SELECT
id,
name,
defaultEncryptionScope,
deleted,
deletedTime,
denyEncryptionScopeOverride,
enableNfsV3AllSquash,
enableNfsV3RootSquash,
etag,
hasImmutabilityPolicy,
hasLegalHold,
immutabilityPolicy,
immutableStorageWithVersioning,
lastModifiedTime,
leaseDuration,
leaseState,
leaseStatus,
legalHold,
metadata,
publicAccess,
remainingRetentionDays,
systemData,
type,
version
FROM azure.storage.blob_containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $maxpagesize = '{{ $maxpagesize }}'
AND $filter = '{{ $filter }}'
AND $include = '{{ $include }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_immutability_policy"
    values={[
        { label: 'create_or_update_immutability_policy', value: 'create_or_update_immutability_policy' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_immutability_policy">

Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.

```sql
INSERT INTO azure.storage.blob_containers (
properties,
resource_group_name,
account_name,
container_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ container_name }}',
'{{ subscription_id }}'
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
<TabItem value="create">

Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container.

```sql
INSERT INTO azure.storage.blob_containers (
properties,
resource_group_name,
account_name,
container_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ container_name }}',
'{{ subscription_id }}'
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
- name: blob_containers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the blob_containers resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the blob_containers resource.
    - name: container_name
      value: "{{ container_name }}"
      description: Required parameter for the blob_containers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the blob_containers resource.
    - name: properties
      description: |
        Properties of the blob container.
      value:
        version: "{{ version }}"
        deleted: {{ deleted }}
        deletedTime: "{{ deletedTime }}"
        remainingRetentionDays: {{ remainingRetentionDays }}
        defaultEncryptionScope: "{{ defaultEncryptionScope }}"
        denyEncryptionScopeOverride: {{ denyEncryptionScopeOverride }}
        publicAccess: "{{ publicAccess }}"
        lastModifiedTime: "{{ lastModifiedTime }}"
        leaseStatus: "{{ leaseStatus }}"
        leaseState: "{{ leaseState }}"
        leaseDuration: "{{ leaseDuration }}"
        metadata: "{{ metadata }}"
        immutabilityPolicy:
          properties:
            immutabilityPeriodSinceCreationInDays: {{ immutabilityPeriodSinceCreationInDays }}
            state: "{{ state }}"
            allowProtectedAppendWrites: {{ allowProtectedAppendWrites }}
            allowProtectedAppendWritesAll: {{ allowProtectedAppendWritesAll }}
          etag: "{{ etag }}"
          updateHistory:
            - update: "{{ update }}"
              immutabilityPeriodSinceCreationInDays: {{ immutabilityPeriodSinceCreationInDays }}
              timestamp: "{{ timestamp }}"
              objectIdentifier: "{{ objectIdentifier }}"
              tenantId: "{{ tenantId }}"
              upn: "{{ upn }}"
              allowProtectedAppendWrites: {{ allowProtectedAppendWrites }}
              allowProtectedAppendWritesAll: {{ allowProtectedAppendWritesAll }}
        legalHold:
          hasLegalHold: {{ hasLegalHold }}
          tags:
            - tag: "{{ tag }}"
              timestamp: "{{ timestamp }}"
              objectIdentifier: "{{ objectIdentifier }}"
              tenantId: "{{ tenantId }}"
              upn: "{{ upn }}"
          protectedAppendWritesHistory:
            allowProtectedAppendWritesAll: {{ allowProtectedAppendWritesAll }}
            timestamp: "{{ timestamp }}"
        hasLegalHold: {{ hasLegalHold }}
        hasImmutabilityPolicy: {{ hasImmutabilityPolicy }}
        immutableStorageWithVersioning:
          enabled: {{ enabled }}
          timeStamp: "{{ timeStamp }}"
          migrationState: "{{ migrationState }}"
        enableNfsV3RootSquash: {{ enableNfsV3RootSquash }}
        enableNfsV3AllSquash: {{ enableNfsV3AllSquash }}
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

Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn't already exist.

```sql
UPDATE azure.storage.blob_containers
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND container_name = '{{ container_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_immutability_policy"
    values={[
        { label: 'create_or_update_immutability_policy', value: 'create_or_update_immutability_policy' }
    ]}
>
<TabItem value="create_or_update_immutability_policy">

Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.

```sql
REPLACE azure.storage.blob_containers
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND container_name = '{{ container_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Deletes specified container under its account.

```sql
DELETE FROM azure.storage.blob_containers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND container_name = '{{ container_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_immutability_policy"
    values={[
        { label: 'get_immutability_policy', value: 'get_immutability_policy' },
        { label: 'delete_immutability_policy', value: 'delete_immutability_policy' },
        { label: 'set_legal_hold', value: 'set_legal_hold' },
        { label: 'clear_legal_hold', value: 'clear_legal_hold' },
        { label: 'lease', value: 'lease' },
        { label: 'object_level_worm', value: 'object_level_worm' },
        { label: 'lock_immutability_policy', value: 'lock_immutability_policy' },
        { label: 'extend_immutability_policy', value: 'extend_immutability_policy' }
    ]}
>
<TabItem value="get_immutability_policy">

Gets the existing immutability policy along with the corresponding ETag in response headers and body.

```sql
EXEC azure.storage.blob_containers.get_immutability_policy 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_immutability_policy">

Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, the only way is to delete the container after deleting all expired blobs inside the policy locked container.

```sql
EXEC azure.storage.blob_containers.delete_immutability_policy 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_legal_hold">

Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request.

```sql
EXEC azure.storage.blob_containers.set_legal_hold 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"allowProtectedAppendWritesAll": {{ allowProtectedAppendWritesAll }}
}'
;
```
</TabItem>
<TabItem value="clear_legal_hold">

Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request.

```sql
EXEC azure.storage.blob_containers.clear_legal_hold 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"allowProtectedAppendWritesAll": {{ allowProtectedAppendWritesAll }}
}'
;
```
</TabItem>
<TabItem value="lease">

The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.

```sql
EXEC azure.storage.blob_containers.lease 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
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
<TabItem value="object_level_worm">

This operation migrates a blob container from container level WORM to object level immutability enabled container. Prerequisites require a container level immutability policy either in locked or unlocked state, Account level versioning must be enabled and there should be no Legal hold on the container.

```sql
EXEC azure.storage.blob_containers.object_level_worm 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="lock_immutability_policy">

Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation.

```sql
EXEC azure.storage.blob_containers.lock_immutability_policy 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="extend_immutability_policy">

Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation.

```sql
EXEC azure.storage.blob_containers.extend_immutability_policy 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
