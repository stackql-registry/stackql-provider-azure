--- 
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - recoveryservices
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

Creates, updates, deletes, gets or lists an <code>operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservices.operation_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_result"
    values={[
        { label: 'get_operation_result', value: 'get_operation_result' }
    ]}
>
<TabItem value="get_operation_result">

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
    <td><CopyableCode code="backupStorageVersion" /></td>
    <td><code>string</code></td>
    <td>Backup storage version. Known values are: "V1", "V2", and "Unassigned". (V1, V2, Unassigned)</td>
</tr>
<tr>
    <td><CopyableCode code="bcdrSecurityLevel" /></td>
    <td><code>string</code></td>
    <td>Security levels of Recovery Services Vault for business continuity and disaster recovery. Known values are: "Poor", "Fair", "Good", and "Excellent". (Poor, Fair, Good, Excellent)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer Managed Key details of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSettings" /></td>
    <td><code>object</code></td>
    <td>Monitoring Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="moveDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the latest move operation performed on the Azure Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="moveState" /></td>
    <td><code>string</code></td>
    <td>The State of the Resource after the move operation. Known values are: "Unknown", "InProgress", "PrepareFailed", "CommitFailed", "PrepareTimedout", "CommitTimedout", "MoveSucceeded", "Failure", "CriticalFailure", and "PartialSuccess". (Unknown, InProgress, PrepareFailed, CommitFailed, PrepareTimedout, CommitTimedout, MoveSucceeded, Failure, CriticalFailure, PartialSuccess)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForBackup" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for backup. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointStateForSiteRecovery" /></td>
    <td><code>string</code></td>
    <td>Private endpoint state for site recovery. Known values are: "None" and "Enabled". (None, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>property to enable or disable resource provider inbound network traffic from public clients. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="redundancySettings" /></td>
    <td><code>object</code></td>
    <td>The redundancy Settings of a Vault.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreSettings" /></td>
    <td><code>object</code></td>
    <td>Restore Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="secureScore" /></td>
    <td><code>string</code></td>
    <td>Secure Score of Recovery Services Vault. Known values are: "None", "Minimum", "Adequate", and "Maximum". (None, Minimum, Adequate, Maximum)</td>
</tr>
<tr>
    <td><CopyableCode code="securitySettings" /></td>
    <td><code>object</code></td>
    <td>Security Settings of the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Identifies the unique system identifier for each Azure resource.</td>
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
<tr>
    <td><CopyableCode code="upgradeDetails" /></td>
    <td><code>object</code></td>
    <td>Details for upgrading vault.</td>
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
    <td><a href="#get_operation_result"><CopyableCode code="get_operation_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the operation result for a resource.</td>
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
    <td>The name of the Vault. Required.</td>
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
    <td>The name of the Vault. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_operation_result"
    values={[
        { label: 'get_operation_result', value: 'get_operation_result' }
    ]}
>
<TabItem value="get_operation_result">

Gets the operation result for a resource.

```sql
SELECT
id,
name,
backupStorageVersion,
bcdrSecurityLevel,
encryption,
etag,
identity,
location,
monitoringSettings,
moveDetails,
moveState,
privateEndpointConnections,
privateEndpointStateForBackup,
privateEndpointStateForSiteRecovery,
provisioningState,
publicNetworkAccess,
redundancySettings,
resourceGuardOperationRequests,
restoreSettings,
secureScore,
securitySettings,
sku,
systemData,
tags,
type,
upgradeDetails
FROM azure.recoveryservices.operation_results
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
