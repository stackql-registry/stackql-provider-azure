--- 
title: operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_status
  - databoxedge
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

Creates, updates, deletes, gets or lists an <code>operations_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operations_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databoxedge.operations_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="currentStage" /></td>
    <td><code>string</code></td>
    <td>Current stage of the update operation. Known values are: "Unknown", "Initial", "ScanStarted", "ScanComplete", "ScanFailed", "DownloadStarted", "DownloadComplete", "DownloadFailed", "InstallStarted", "InstallComplete", "InstallFailed", "RebootInitiated", "Success", "Failure", "RescanStarted", "RescanComplete", and "RescanFailed". (Unknown, Initial, ScanStarted, ScanComplete, ScanFailed, DownloadStarted, DownloadComplete, DownloadFailed, InstallStarted, InstallComplete, InstallFailed, RebootInitiated, Success, Failure, RescanStarted, RescanComplete, RescanFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="downloadProgress" /></td>
    <td><code>object</code></td>
    <td>The download progress.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job completed.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error details.</td>
</tr>
<tr>
    <td><CopyableCode code="errorManifestFile" /></td>
    <td><code>string</code></td>
    <td>Local share/remote container relative path to the error manifest file of the refresh.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>string</code></td>
    <td>If only subfolders need to be refreshed, then the subfolder path inside the share or container. (The path is empty if there are no subfolders.).</td>
</tr>
<tr>
    <td><CopyableCode code="installProgress" /></td>
    <td><code>object</code></td>
    <td>The install progress.</td>
</tr>
<tr>
    <td><CopyableCode code="jobType" /></td>
    <td><code>string</code></td>
    <td>The type of the job. Known values are: "Invalid", "ScanForUpdates", "DownloadUpdates", "InstallUpdates", "RefreshShare", "RefreshContainer", "Backup", "Restore", and "TriggerSupportPackage". (Invalid, ScanForUpdates, DownloadUpdates, InstallUpdates, RefreshShare, RefreshContainer, Backup, Restore, TriggerSupportPackage)</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>integer</code></td>
    <td>The percentage of the job that is complete.</td>
</tr>
<tr>
    <td><CopyableCode code="refreshedEntityId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the entity that was refreshed.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC date and time at which the job started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the job. Known values are: "Invalid", "Running", "Succeeded", "Failed", "Canceled", "Paused", and "Scheduled". (Invalid, Running, Succeeded, Failed, Canceled, Paused, Scheduled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRefreshErrors" /></td>
    <td><code>integer</code></td>
    <td>Total number of errors encountered during the refresh process.</td>
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
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a specified job on a Data Box Edge/Data Box Gateway device. Gets the details of a specified job on a Data Box Edge/Data Box Gateway device.</td>
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
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The job name. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the details of a specified job on a Data Box Edge/Data Box Gateway device. Gets the details of a specified job on a Data Box Edge/Data Box Gateway device.

```sql
SELECT
id,
name,
currentStage,
downloadProgress,
endTime,
error,
errorManifestFile,
folder,
installProgress,
jobType,
percentComplete,
refreshedEntityId,
startTime,
status,
systemData,
totalRefreshErrors,
type
FROM azure.databoxedge.operations_status
WHERE device_name = '{{ device_name }}' -- required
AND name = '{{ name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
