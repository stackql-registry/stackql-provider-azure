--- 
title: fetch_cross_region_restore_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - fetch_cross_region_restore_jobs
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>fetch_cross_region_restore_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fetch_cross_region_restore_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.fetch_cross_region_restore_jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="activityID" /></td>
    <td><code>string</code></td>
    <td>Job Activity Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="backupInstanceFriendlyName" /></td>
    <td><code>string</code></td>
    <td>Name of the Backup Instance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="backupInstanceId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the Backup Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the DataSource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceLocation" /></td>
    <td><code>string</code></td>
    <td>Location of the DataSource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceName" /></td>
    <td><code>string</code></td>
    <td>User Friendly Name of the DataSource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceSetName" /></td>
    <td><code>string</code></td>
    <td>Data Source Set Name of the DataSource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceType" /></td>
    <td><code>string</code></td>
    <td>Type of DataSource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationDataStoreName" /></td>
    <td><code>string</code></td>
    <td>:vartype destination_data_store_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>Total run time of the job. ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>EndTime of the job(in UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>array</code></td>
    <td>A List, detailing the errors related to the job.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>:vartype etag: str</td>
</tr>
<tr>
    <td><CopyableCode code="extendedInfo" /></td>
    <td><code>object</code></td>
    <td>Extended Information about the job.</td>
</tr>
<tr>
    <td><CopyableCode code="isUserTriggered" /></td>
    <td><code>boolean</code></td>
    <td>Indicated that whether the job is adhoc(true) or scheduled(false). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="operation" /></td>
    <td><code>string</code></td>
    <td>It indicates the type of Job i.e. Backup:full/log/diff ;Restore:ALR/OLR; Tiering:Backup/Archive ; Management:ConfigureProtection/UnConfigure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="operationCategory" /></td>
    <td><code>string</code></td>
    <td>It indicates the type of Job i.e. Backup/Restore/Tiering/Management. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>ARM ID of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyName" /></td>
    <td><code>string</code></td>
    <td>Name of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="progressEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicated whether progress is enabled for the job. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="progressUrl" /></td>
    <td><code>string</code></td>
    <td>Url which contains job's progress.</td>
</tr>
<tr>
    <td><CopyableCode code="rehydrationPriority" /></td>
    <td><code>string</code></td>
    <td>Priority to be used for rehydration.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreType" /></td>
    <td><code>string</code></td>
    <td>It indicates the sub type of operation i.e. in case of Restore it can be ALR/OLR.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDataStoreName" /></td>
    <td><code>string</code></td>
    <td>:vartype source_data_store_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource Group Name of the Datasource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSubscriptionID" /></td>
    <td><code>string</code></td>
    <td>SubscriptionId corresponding to the DataSource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>StartTime of the job(in UTC). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the job like InProgress/Completed/Failed/Cancelled/CompletedWithWarnings/Cancelling/Paused. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription Id of the corresponding backup vault. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedActions" /></td>
    <td><code>array</code></td>
    <td>List of supported actions. Required.</td>
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
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>Name of the vault. Required.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Fetches list of Cross Region Restore job belonging to the vault.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Fetches list of Cross Region Restore job belonging to the vault.

```sql
SELECT
id,
name,
activityID,
backupInstanceFriendlyName,
backupInstanceId,
dataSourceId,
dataSourceLocation,
dataSourceName,
dataSourceSetName,
dataSourceType,
destinationDataStoreName,
duration,
endTime,
errorDetails,
etag,
extendedInfo,
isUserTriggered,
operation,
operationCategory,
policyId,
policyName,
progressEnabled,
progressUrl,
rehydrationPriority,
restoreType,
sourceDataStoreName,
sourceResourceGroup,
sourceSubscriptionID,
startTime,
status,
subscriptionId,
supportedActions,
systemData,
type,
vaultName
FROM azure.data_protection.fetch_cross_region_restore_jobs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
