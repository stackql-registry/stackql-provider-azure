--- 
title: backup_vault_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vault_operation_results
  - dataprotection
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

Creates, updates, deletes, gets or lists a <code>backup_vault_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_vault_operation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dataprotection.backup_vault_operation_results" /></td></tr>
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
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security Level of Backup Vault. Known values are: "Poor", "Fair", "Good", "Excellent", and "NotSupported". (Poor, Fair, Good, Excellent, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="featureSettings" /></td>
    <td><code>object</code></td>
    <td>Feature Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Input Managed Identity Details.</td>
</tr>
<tr>
    <td><CopyableCode code="isVaultProtectedByResourceGuard" /></td>
    <td><code>boolean</code></td>
    <td>Is vault protected by resource guard.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the BackupVault resource. Known values are: "Failed", "Provisioning", "Succeeded", "Unknown", and "Updating". (Failed, Provisioning, Succeeded, Unknown, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicatedRegions" /></td>
    <td><code>array</code></td>
    <td>List of replicated regions for Backup Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveDetails" /></td>
    <td><code>object</code></td>
    <td>Resource move details for backup vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMoveState" /></td>
    <td><code>string</code></td>
    <td>Resource move state for backup vault. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "Failed", "PrepareTimedout", "CommitTimedout", "CriticalFailure", "PartialSuccess", and "MoveSucceeded". (Unknown, InProgress, PrepareFailed, CommitFailed, Failed, PrepareTimedout, CommitTimedout, CriticalFailure, PartialSuccess, MoveSucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Backup Vault. Known values are: "None", "Minimum", "Adequate", "Maximum", and "NotSupported". (None, Minimum, Adequate, Maximum, NotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="storageSettings" /></td>
    <td><code>array</code></td>
    <td>Storage Settings.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a BackupVaultResource.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The name of the BackupVaultResource. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the BackupVaultResource. Required.</td>
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

Get a BackupVaultResource.

```sql
SELECT
id,
name,
bcdrSecurityLevel,
eTag,
featureSettings,
identity,
isVaultProtectedByResourceGuard,
location,
monitoringSettings,
provisioningState,
replicatedRegions,
resourceGuardOperationRequests,
resourceMoveDetails,
resourceMoveState,
secureScore,
securitySettings,
storageSettings,
systemData,
tags,
type
FROM azure.dataprotection.backup_vault_operation_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
