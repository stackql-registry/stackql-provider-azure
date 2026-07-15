--- 
title: backup_instances_extension_routing
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances_extension_routing
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

Creates, updates, deletes, gets or lists a <code>backup_instances_extension_routing</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_instances_extension_routing" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_instances_extension_routing" /></td></tr>
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
    <td><CopyableCode code="currentProtectionState" /></td>
    <td><code>string</code></td>
    <td>Specifies the current protection state of the resource. Known values are: "Invalid", "NotProtected", "ConfiguringProtection", "ProtectionConfigured", "BackupSchedulesSuspended", "RetentionSchedulesSuspended", "ProtectionStopped", "ProtectionError", "ConfiguringProtectionFailed", "SoftDeleting", "SoftDeleted", and "UpdatingProtection". (Invalid, NotProtected, ConfiguringProtection, ProtectionConfigured, BackupSchedulesSuspended, RetentionSchedulesSuspended, ProtectionStopped, ProtectionError, ConfiguringProtectionFailed, SoftDeleting, SoftDeleted, UpdatingProtection)</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the data source information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSourceSetInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the data source set information.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceAuthCredentials" /></td>
    <td><code>object</code></td>
    <td>Credentials to use to authenticate with data source provider.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Backup Instance friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="identityDetails" /></td>
    <td><code>object</code></td>
    <td>Contains information of the Identity Details for the BI. If it is null, default will be considered as System Assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policyInfo" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the policy information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionErrorDetails" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection error of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>object</code></td>
    <td>Specifies the protection status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Specifies the provisioning state of the resource i.e. provisioning/updating/Succeeded/Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuardOperationRequests on which LAC check will be performed.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Proxy Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of validation. In case of DeepValidation, all validations from /validateForBackup API will run again. Known values are: "ShallowValidation" and "DeepValidation". (ShallowValidation, DeepValidation)</td>
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
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Gets a list of backup instances associated with a tracked resource.</td>
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
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>ARM path of the resource to be protected using Microsoft.DataProtection. Required.</td>
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

Gets a list of backup instances associated with a tracked resource.

```sql
SELECT
id,
name,
currentProtectionState,
dataSourceInfo,
dataSourceSetInfo,
datasourceAuthCredentials,
friendlyName,
identityDetails,
objectType,
policyInfo,
protectionErrorDetails,
protectionStatus,
provisioningState,
resourceGuardOperationRequests,
systemData,
tags,
type,
validationType
FROM azure.data_protection.backup_instances_extension_routing
WHERE resource_id = '{{ resource_id }}' -- required
;
```
</TabItem>
</Tabs>
