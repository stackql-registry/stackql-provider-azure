--- 
title: backup_status
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_status
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>backup_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_status" /></td></tr>
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
    <td><CopyableCode code="acquireStorageAccountLock" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the storage account lock has been acquired or not. Known values are: "Acquire" and "NotAcquire". (Acquire, NotAcquire)</td>
</tr>
<tr>
    <td><CopyableCode code="containerName" /></td>
    <td><code>string</code></td>
    <td>Specifies the product specific container name. E.g. iaasvmcontainer;iaasvmcontainer;csname;vmname.</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>string</code></td>
    <td>ErrorCode in case of intent failed.</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>ErrorMessage in case of intent failed.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricName" /></td>
    <td><code>string</code></td>
    <td>Specifies the fabric name - Azure or AD. Known values are: "Invalid" and "Azure". (Invalid, Azure)</td>
</tr>
<tr>
    <td><CopyableCode code="policyName" /></td>
    <td><code>string</code></td>
    <td>Specifies the policy name which is used for protection.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemName" /></td>
    <td><code>string</code></td>
    <td>Specifies the product specific ds name. E.g. vm;iaasvmcontainer;csname;vmname.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemsCount" /></td>
    <td><code>integer</code></td>
    <td>Number of protected items.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the container is registered or not. Known values are: "Invalid", "NotProtected", "Protecting", "Protected", and "ProtectionFailed". (Invalid, NotProtected, Protecting, Protected, ProtectionFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>Container registration status.</td>
</tr>
<tr>
    <td><CopyableCode code="vaultId" /></td>
    <td><code>string</code></td>
    <td>Specifies the arm resource id of the vault.</td>
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
    <td><a href="#parameter-azure_region"><code>azure_region</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the container backup status. Get the container backup status.</td>
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
<tr id="parameter-azure_region">
    <td><CopyableCode code="azure_region" /></td>
    <td><code>string</code></td>
    <td>Azure region to hit Api. Required.</td>
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

Get the container backup status. Get the container backup status.

```sql
SELECT
acquireStorageAccountLock,
containerName,
errorCode,
errorMessage,
fabricName,
policyName,
protectedItemName,
protectedItemsCount,
protectionStatus,
registrationStatus,
vaultId
FROM azure.recovery_services_backup.backup_status
WHERE azure_region = '{{ azure_region }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
