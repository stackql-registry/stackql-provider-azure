--- 
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="updates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.updates" /></td></tr>
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
    <td><CopyableCode code="additionalProperties" /></td>
    <td><code>string</code></td>
    <td>Extensible KV pairs serialized as a string. This is currently used to report the stamp OEM family and hardware model information when an update is flagged as Invalid for the stamp based on OEM type.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityType" /></td>
    <td><code>string</code></td>
    <td>Indicates how the update content is made available for download. This determines whether the update is sourced locally, from an online repository, or requires user notification. Known values are: "Local", "Online", and "Notify". (Local, Online, Notify)</td>
</tr>
<tr>
    <td><CopyableCode code="componentVersions" /></td>
    <td><code>array</code></td>
    <td>An array of component versions for a Solution Bundle update, and an empty array otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the Update.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the package-specific checks were run.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckResult" /></td>
    <td><code>array</code></td>
    <td>An array of PrecheckResult objects.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Overall health state for update-specific health checks. Known values are: "Unknown", "Success", "Failure", "Warning", "Error", and "InProgress". (Unknown, Success, Failure, Warning, Error, InProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="installedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date that the update was installed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="minSbeVersionRequired" /></td>
    <td><code>string</code></td>
    <td>Minimum Sbe Version of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="packagePath" /></td>
    <td><code>string</code></td>
    <td>Path where the update package is available.</td>
</tr>
<tr>
    <td><CopyableCode code="packageSizeInMb" /></td>
    <td><code>number</code></td>
    <td>Size of the package. This value is a combination of the size from update metadata and size of the payload that results from the live scan operation for OS update content.</td>
</tr>
<tr>
    <td><CopyableCode code="packageType" /></td>
    <td><code>string</code></td>
    <td>Customer-visible type of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="prerequisites" /></td>
    <td><code>array</code></td>
    <td>If update State is HasPrerequisite, this property contains an array of objects describing prerequisite updates before installing this update. Otherwise, it is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Updates proxy resource. Indicates the current lifecycle status of the update operation, such as whether it has been accepted, is in progress, or has completed. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Publisher of the update package.</td>
</tr>
<tr>
    <td><CopyableCode code="rebootRequired" /></td>
    <td><code>string</code></td>
    <td>Indicates whether a reboot is required after the update or operation. Helps determine if a system restart is necessary to complete the process. Known values are: "Unknown", "True", and "False". (Unknown, True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseLink" /></td>
    <td><code>string</code></td>
    <td>Link to release notes for the update.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Represents the current state of the update as it relates to this stamp. This includes phases such as preparation, installation, scanning, and error handling, providing insight into the update's progress and any issues encountered. Known values are: "HasPrerequisite", "Obsolete", "Ready", "NotApplicableBecauseAnotherUpdateIsInProgress", "Preparing", "Installing", "Installed", "PreparationFailed", "InstallationFailed", "Invalid", "Recalled", "Downloading", "DownloadFailed", "HealthChecking", "HealthCheckFailed", "ReadyToInstall", "ScanInProgress", "ScanFailed", "AdditionalContentRequired", "HealthCheckExpired", and "PendingOEMValidation". (HasPrerequisite, Obsolete, Ready, NotApplicableBecauseAnotherUpdateIsInProgress, Preparing, Installing, Installed, PreparationFailed, InstallationFailed, Invalid, Recalled, Downloading, DownloadFailed, HealthChecking, HealthCheckFailed, ReadyToInstall, ScanInProgress, ScanFailed, AdditionalContentRequired, HealthCheckExpired, PendingOEMValidation)</td>
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
    <td><CopyableCode code="updateStateProperties" /></td>
    <td><code>object</code></td>
    <td>Additional information regarding the state of the update. See definition of UpdateStateProperties type below for more details on this property.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the update.</td>
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
    <td><CopyableCode code="additionalProperties" /></td>
    <td><code>string</code></td>
    <td>Extensible KV pairs serialized as a string. This is currently used to report the stamp OEM family and hardware model information when an update is flagged as Invalid for the stamp based on OEM type.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityType" /></td>
    <td><code>string</code></td>
    <td>Indicates how the update content is made available for download. This determines whether the update is sourced locally, from an online repository, or requires user notification. Known values are: "Local", "Online", and "Notify". (Local, Online, Notify)</td>
</tr>
<tr>
    <td><CopyableCode code="componentVersions" /></td>
    <td><code>array</code></td>
    <td>An array of component versions for a Solution Bundle update, and an empty array otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the Update.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the package-specific checks were run.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckResult" /></td>
    <td><code>array</code></td>
    <td>An array of PrecheckResult objects.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Overall health state for update-specific health checks. Known values are: "Unknown", "Success", "Failure", "Warning", "Error", and "InProgress". (Unknown, Success, Failure, Warning, Error, InProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="installedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date that the update was installed.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="minSbeVersionRequired" /></td>
    <td><code>string</code></td>
    <td>Minimum Sbe Version of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="packagePath" /></td>
    <td><code>string</code></td>
    <td>Path where the update package is available.</td>
</tr>
<tr>
    <td><CopyableCode code="packageSizeInMb" /></td>
    <td><code>number</code></td>
    <td>Size of the package. This value is a combination of the size from update metadata and size of the payload that results from the live scan operation for OS update content.</td>
</tr>
<tr>
    <td><CopyableCode code="packageType" /></td>
    <td><code>string</code></td>
    <td>Customer-visible type of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="prerequisites" /></td>
    <td><code>array</code></td>
    <td>If update State is HasPrerequisite, this property contains an array of objects describing prerequisite updates before installing this update. Otherwise, it is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Updates proxy resource. Indicates the current lifecycle status of the update operation, such as whether it has been accepted, is in progress, or has completed. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Publisher of the update package.</td>
</tr>
<tr>
    <td><CopyableCode code="rebootRequired" /></td>
    <td><code>string</code></td>
    <td>Indicates whether a reboot is required after the update or operation. Helps determine if a system restart is necessary to complete the process. Known values are: "Unknown", "True", and "False". (Unknown, True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="releaseLink" /></td>
    <td><code>string</code></td>
    <td>Link to release notes for the update.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Represents the current state of the update as it relates to this stamp. This includes phases such as preparation, installation, scanning, and error handling, providing insight into the update's progress and any issues encountered. Known values are: "HasPrerequisite", "Obsolete", "Ready", "NotApplicableBecauseAnotherUpdateIsInProgress", "Preparing", "Installing", "Installed", "PreparationFailed", "InstallationFailed", "Invalid", "Recalled", "Downloading", "DownloadFailed", "HealthChecking", "HealthCheckFailed", "ReadyToInstall", "ScanInProgress", "ScanFailed", "AdditionalContentRequired", "HealthCheckExpired", and "PendingOEMValidation". (HasPrerequisite, Obsolete, Ready, NotApplicableBecauseAnotherUpdateIsInProgress, Preparing, Installing, Installed, PreparationFailed, InstallationFailed, Invalid, Recalled, Downloading, DownloadFailed, HealthChecking, HealthCheckFailed, ReadyToInstall, ScanInProgress, ScanFailed, AdditionalContentRequired, HealthCheckExpired, PendingOEMValidation)</td>
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
    <td><CopyableCode code="updateStateProperties" /></td>
    <td><code>object</code></td>
    <td>Additional information regarding the state of the update. See definition of UpdateStateProperties type below for more details on this property.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the update.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-update_name"><code>update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get specified Update.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Updates.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-update_name"><code>update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete specified Update.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-update_name"><code>update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Put specified Update.</td>
</tr>
<tr>
    <td><a href="#post"><CopyableCode code="post" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-update_name"><code>update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Apply Update.</td>
</tr>
<tr>
    <td><a href="#prepare"><CopyableCode code="prepare" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-update_name"><code>update_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Prepare Update.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
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
<tr id="parameter-update_name">
    <td><CopyableCode code="update_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Update. Required.</td>
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

Get specified Update.

```sql
SELECT
id,
name,
additionalProperties,
availabilityType,
componentVersions,
description,
displayName,
healthCheckDate,
healthCheckResult,
healthState,
installedDate,
location,
minSbeVersionRequired,
packagePath,
packageSizeInMb,
packageType,
prerequisites,
provisioningState,
publisher,
rebootRequired,
releaseLink,
state,
systemData,
type,
updateStateProperties,
version
FROM azure_stack.azure_stack_hci.updates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND update_name = '{{ update_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Updates.

```sql
SELECT
id,
name,
additionalProperties,
availabilityType,
componentVersions,
description,
displayName,
healthCheckDate,
healthCheckResult,
healthState,
installedDate,
location,
minSbeVersionRequired,
packagePath,
packageSizeInMb,
packageType,
prerequisites,
provisioningState,
publisher,
rebootRequired,
releaseLink,
state,
systemData,
type,
updateStateProperties,
version
FROM azure_stack.azure_stack_hci.updates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
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

Delete specified Update.

```sql
DELETE FROM azure_stack.azure_stack_hci.updates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND update_name = '{{ update_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'post', value: 'post' },
        { label: 'prepare', value: 'prepare' }
    ]}
>
<TabItem value="put">

Put specified Update.

```sql
EXEC azure_stack.azure_stack_hci.updates.put 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@update_name='{{ update_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"location": "{{ location }}"
}'
;
```
</TabItem>
<TabItem value="post">

Apply Update.

```sql
EXEC azure_stack.azure_stack_hci.updates.post 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@update_name='{{ update_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="prepare">

Prepare Update.

```sql
EXEC azure_stack.azure_stack_hci.updates.prepare 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@update_name='{{ update_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
