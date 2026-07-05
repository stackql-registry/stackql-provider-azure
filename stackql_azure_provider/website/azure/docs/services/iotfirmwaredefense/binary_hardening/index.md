--- 
title: binary_hardening
hide_title: false
hide_table_of_contents: false
keywords:
  - binary_hardening
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

Creates, updates, deletes, gets or lists a <code>binary_hardening</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="binary_hardening" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotfirmwaredefense.binary_hardening" /></td></tr>
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
    <td><CopyableCode code="binaryHardeningId" /></td>
    <td><code>string</code></td>
    <td>ID for the binary hardening result.</td>
</tr>
<tr>
    <td><CopyableCode code="executableArchitecture" /></td>
    <td><code>string</code></td>
    <td>The architecture of the binary being reported on.</td>
</tr>
<tr>
    <td><CopyableCode code="executableClass" /></td>
    <td><code>string</code></td>
    <td>The executable class to indicate 32 or 64 bit. Known values are: "x86" and "x64". (x86, x64)</td>
</tr>
<tr>
    <td><CopyableCode code="filePath" /></td>
    <td><code>string</code></td>
    <td>The path to the binary in the firmware.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Extracting", and "Analyzing". (Succeeded, Failed, Canceled, Pending, Extracting, Analyzing)</td>
</tr>
<tr>
    <td><CopyableCode code="rpath" /></td>
    <td><code>string</code></td>
    <td>The rpath property of the uploaded binary, which is a deprecated method of specifying additional paths to load objects at runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="runpath" /></td>
    <td><code>string</code></td>
    <td>The runpath property of the uploaded binary, which is a method of specifying additional paths to load objects at runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="securityHardeningFeatures" /></td>
    <td><code>object</code></td>
    <td>The security hardening features of the binary.</td>
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
    <td><a href="#list_by_firmware"><CopyableCode code="list_by_firmware" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-firmware_id"><code>firmware_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists binary hardening analysis results of a firmware.</td>
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

Lists binary hardening analysis results of a firmware.

```sql
SELECT
id,
name,
binaryHardeningId,
executableArchitecture,
executableClass,
filePath,
provisioningState,
rpath,
runpath,
securityHardeningFeatures,
systemData,
type
FROM azure.iotfirmwaredefense.binary_hardening
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND firmware_id = '{{ firmware_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
