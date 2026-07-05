--- 
title: crypto_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_keys
  - iotfirmwaredefense
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

Creates, updates, deletes, gets or lists a <code>crypto_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="crypto_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotfirmwaredefense.crypto_keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_firmware"
    values={[
        { label: 'list_by_firmware', value: 'list_by_firmware' }
    ]}
>
<TabItem value="list_by_firmware">

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
    <td><CopyableCode code="cryptoKeyId" /></td>
    <td><code>string</code></td>
    <td>ID for the key result.</td>
</tr>
<tr>
    <td><CopyableCode code="cryptoKeySize" /></td>
    <td><code>integer</code></td>
    <td>Size of the key in bits.</td>
</tr>
<tr>
    <td><CopyableCode code="filePaths" /></td>
    <td><code>array</code></td>
    <td>List of files where this key was found.</td>
</tr>
<tr>
    <td><CopyableCode code="isShortKeySize" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the key size is considered too small to be secure for the algorithm according to NIST guidance.</td>
</tr>
<tr>
    <td><CopyableCode code="keyAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Key algorithm name.</td>
</tr>
<tr>
    <td><CopyableCode code="keyType" /></td>
    <td><code>string</code></td>
    <td>Type of the key (public or private). Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="pairedKey" /></td>
    <td><code>object</code></td>
    <td>A matching paired key or certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Extracting", and "Analyzing". (Succeeded, Failed, Canceled, Pending, Extracting, Analyzing)</td>
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
    <td><CopyableCode code="usage" /></td>
    <td><code>array</code></td>
    <td>Functions the key can fulfill.</td>
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
    <td><a href="#list_by_firmware"><CopyableCode code="list_by_firmware" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-firmware_id"><code>firmware_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists crypto key analysis results of a firmware.</td>
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
<tr id="parameter-firmware_id">
    <td><CopyableCode code="firmware_id" /></td>
    <td><code>string</code></td>
    <td>The id of the firmware. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the firmware analysis workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_firmware"
    values={[
        { label: 'list_by_firmware', value: 'list_by_firmware' }
    ]}
>
<TabItem value="list_by_firmware">

Lists crypto key analysis results of a firmware.

```sql
SELECT
id,
name,
cryptoKeyId,
cryptoKeySize,
filePaths,
isShortKeySize,
keyAlgorithm,
keyType,
pairedKey,
provisioningState,
systemData,
type,
usage
FROM azure.iotfirmwaredefense.crypto_keys
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND firmware_id = '{{ firmware_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
