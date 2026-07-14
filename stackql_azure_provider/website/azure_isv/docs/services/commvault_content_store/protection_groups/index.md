--- 
title: protection_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_groups
  - commvault_content_store
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

Creates, updates, deletes, gets or lists a <code>protection_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protection_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.commvault_content_store.protection_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cloud_account', value: 'list_by_cloud_account' }
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
    <td><CopyableCode code="backupActivityStatus" /></td>
    <td><code>string</code></td>
    <td>The backup activity status indicating if backup is enabled or not on the protection group.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceType" /></td>
    <td><code>string</code></td>
    <td>The datasource type of Commvault Protection Group. Required. Default value is "AzureVM".</td>
</tr>
<tr>
    <td><CopyableCode code="lastBackUpTime" /></td>
    <td><code>integer</code></td>
    <td>The Commvault Protection Group backup time.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfProtectedItems" /></td>
    <td><code>integer</code></td>
    <td>The number of ProtectedItems under the Protection Group.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>The Commvault Plan to be associated with the Protection Group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>The protection group schedule. Known values are: "all", "protected", "not_protected", "pending", "backed_up_with_error", and "discovered". (all, protected, not_protected, pending, backed_up_with_error, discovered)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>object</code></td>
    <td>The resources to be protected under Protection Group. Required.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_cloud_account">

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
    <td><CopyableCode code="backupActivityStatus" /></td>
    <td><code>string</code></td>
    <td>The backup activity status indicating if backup is enabled or not on the protection group.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceType" /></td>
    <td><code>string</code></td>
    <td>The datasource type of Commvault Protection Group. Required. Default value is "AzureVM".</td>
</tr>
<tr>
    <td><CopyableCode code="lastBackUpTime" /></td>
    <td><code>integer</code></td>
    <td>The Commvault Protection Group backup time.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfProtectedItems" /></td>
    <td><code>integer</code></td>
    <td>The number of ProtectedItems under the Protection Group.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>The Commvault Plan to be associated with the Protection Group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>The protection group schedule. Known values are: "all", "protected", "not_protected", "pending", "backed_up_with_error", and "discovered". (all, protected, not_protected, pending, backed_up_with_error, discovered)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>object</code></td>
    <td>The resources to be protected under Protection Group. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ProtectionGroup.</td>
</tr>
<tr>
    <td><a href="#list_by_cloud_account"><CopyableCode code="list_by_cloud_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ProtectionGroup resources by CloudAccount.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ProtectionGroup.</td>
</tr>
<tr>
    <td><a href="#create_orupdate"><CopyableCode code="create_orupdate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ProtectionGroup.</td>
</tr>
<tr>
    <td><a href="#stop_backup"><CopyableCode code="stop_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-reason"><code>reason</code></a></td>
    <td></td>
    <td>Stop Backup for a Protection Group.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-inPlaceRestore"><code>inPlaceRestore</code></a>, <a href="#parameter-vmDestinationInfo"><code>vmDestinationInfo</code></a></td>
    <td></td>
    <td>Restore resource for a protected items in given protection group.</td>
</tr>
<tr>
    <td><a href="#resume_backup"><CopyableCode code="resume_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resume Backup for a Protection Group.</td>
</tr>
<tr>
    <td><a href="#backup"><CopyableCode code="backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-protection_group_name"><code>protection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-vmList"><code>vmList</code></a>, <a href="#parameter-backupOptions"><code>backupOptions</code></a></td>
    <td></td>
    <td>Ad-hoc backup of protected items resource in given protection group.</td>
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
<tr id="parameter-cloud_account_name">
    <td><CopyableCode code="cloud_account_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Cloud Account resource. Required.</td>
</tr>
<tr id="parameter-protection_group_name">
    <td><CopyableCode code="protection_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the ProtectionGroup resource. Required.</td>
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
        { label: 'list_by_cloud_account', value: 'list_by_cloud_account' }
    ]}
>
<TabItem value="get">

Get a ProtectionGroup.

```sql
SELECT
id,
name,
backupActivityStatus,
dataSourceType,
lastBackUpTime,
numberOfProtectedItems,
plan,
protectionStatus,
provisioningState,
resources,
systemData,
type
FROM azure_isv.commvault_content_store.protection_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_account_name = '{{ cloud_account_name }}' -- required
AND protection_group_name = '{{ protection_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cloud_account">

List ProtectionGroup resources by CloudAccount.

```sql
SELECT
id,
name,
backupActivityStatus,
dataSourceType,
lastBackUpTime,
numberOfProtectedItems,
plan,
protectionStatus,
provisioningState,
resources,
systemData,
type
FROM azure_isv.commvault_content_store.protection_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_account_name = '{{ cloud_account_name }}' -- required
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

Delete a ProtectionGroup.

```sql
DELETE FROM azure_isv.commvault_content_store.protection_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cloud_account_name = '{{ cloud_account_name }}' --required
AND protection_group_name = '{{ protection_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_orupdate"
    values={[
        { label: 'create_orupdate', value: 'create_orupdate' },
        { label: 'stop_backup', value: 'stop_backup' },
        { label: 'restore', value: 'restore' },
        { label: 'resume_backup', value: 'resume_backup' },
        { label: 'backup', value: 'backup' }
    ]}
>
<TabItem value="create_orupdate">

Create a ProtectionGroup.

```sql
EXEC azure_isv.commvault_content_store.protection_groups.create_orupdate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="stop_backup">

Stop Backup for a Protection Group.

```sql
EXEC azure_isv.commvault_content_store.protection_groups.stop_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"reason": "{{ reason }}", 
"comment": "{{ comment }}"
}'
;
```
</TabItem>
<TabItem value="restore">

Restore resource for a protected items in given protection group.

```sql
EXEC azure_isv.commvault_content_store.protection_groups.restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"inPlaceRestore": {{ inPlaceRestore }}, 
"restoreType": "{{ restoreType }}", 
"toTime": "{{ toTime }}", 
"vmDestinationInfo": "{{ vmDestinationInfo }}"
}'
;
```
</TabItem>
<TabItem value="resume_backup">

Resume Backup for a Protection Group.

```sql
EXEC azure_isv.commvault_content_store.protection_groups.resume_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="backup">

Ad-hoc backup of protected items resource in given protection group.

```sql
EXEC azure_isv.commvault_content_store.protection_groups.backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@protection_group_name='{{ protection_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vmList": "{{ vmList }}", 
"backupOptions": "{{ backupOptions }}"
}'
;
```
</TabItem>
</Tabs>
