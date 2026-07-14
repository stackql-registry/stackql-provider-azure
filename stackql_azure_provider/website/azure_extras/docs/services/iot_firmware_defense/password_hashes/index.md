--- 
title: password_hashes
hide_title: false
hide_table_of_contents: false
keywords:
  - password_hashes
  - iot_firmware_defense
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>password_hashes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="password_hashes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.iot_firmware_defense.password_hashes" /></td></tr>
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
    <td><CopyableCode code="algorithm" /></td>
    <td><code>string</code></td>
    <td>Algorithm of the password hash.</td>
</tr>
<tr>
    <td><CopyableCode code="context" /></td>
    <td><code>string</code></td>
    <td>Context of password hash.</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>File path of the password hash.</td>
</tr>
<tr>
    <td><CopyableCode code="hash" /></td>
    <td><code>string</code></td>
    <td>Hash of the password.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordHashId" /></td>
    <td><code>string</code></td>
    <td>ID for password hash.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Extracting", and "Analyzing". (Succeeded, Failed, Canceled, Pending, Extracting, Analyzing)</td>
</tr>
<tr>
    <td><CopyableCode code="salt" /></td>
    <td><code>string</code></td>
    <td>Salt of the password hash.</td>
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
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>User name of password hash.</td>
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
    <td>Lists password hash analysis results of a firmware.</td>
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

Lists password hash analysis results of a firmware.

```sql
SELECT
id,
name,
algorithm,
context,
filePath,
hash,
passwordHashId,
provisioningState,
salt,
systemData,
type,
username
FROM azure_extras.iot_firmware_defense.password_hashes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND firmware_id = '{{ firmware_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
