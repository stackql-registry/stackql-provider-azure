--- 
title: cves
hide_title: false
hide_table_of_contents: false
keywords:
  - cves
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

Creates, updates, deletes, gets or lists a <code>cves</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cves" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotfirmwaredefense.cves" /></td></tr>
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
    <td><CopyableCode code="component" /></td>
    <td><code>object</code></td>
    <td>Legacy property for what is now componentName.</td>
</tr>
<tr>
    <td><CopyableCode code="componentId" /></td>
    <td><code>string</code></td>
    <td>ID of the affected SBOM component.</td>
</tr>
<tr>
    <td><CopyableCode code="componentName" /></td>
    <td><code>string</code></td>
    <td>Name of the affected SBOM component.</td>
</tr>
<tr>
    <td><CopyableCode code="componentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the affected SBOM component.</td>
</tr>
<tr>
    <td><CopyableCode code="cveId" /></td>
    <td><code>string</code></td>
    <td>ID of the CVE result.</td>
</tr>
<tr>
    <td><CopyableCode code="cveName" /></td>
    <td><code>string</code></td>
    <td>Name of the CVE.</td>
</tr>
<tr>
    <td><CopyableCode code="cvssScore" /></td>
    <td><code>string</code></td>
    <td>Legacy property for the effective CVE score.</td>
</tr>
<tr>
    <td><CopyableCode code="cvssScores" /></td>
    <td><code>array</code></td>
    <td>All known CVSS scores for the CVE.</td>
</tr>
<tr>
    <td><CopyableCode code="cvssV2Score" /></td>
    <td><code>string</code></td>
    <td>Legacy property for the CVE CVSS version 2 score, if one existed.</td>
</tr>
<tr>
    <td><CopyableCode code="cvssV3Score" /></td>
    <td><code>string</code></td>
    <td>Legacy property for the CVE CVSS version 3 score, if one existed.</td>
</tr>
<tr>
    <td><CopyableCode code="cvssVersion" /></td>
    <td><code>string</code></td>
    <td>Legacy property for the what CVSS version score was stored in the cvssScore property.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The CVE description.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveCvssScore" /></td>
    <td><code>number</code></td>
    <td>The most recent CVSS score of the CVE.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveCvssVersion" /></td>
    <td><code>integer</code></td>
    <td>The version of the effectiveCvssScore property.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>The list of reference links for the CVE.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Extracting", and "Analyzing". (Succeeded, Failed, Canceled, Pending, Extracting, Analyzing)</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>Severity of the CVE.</td>
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
    <td>Lists CVE analysis results of a firmware.</td>
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

Lists CVE analysis results of a firmware.

```sql
SELECT
id,
name,
component,
componentId,
componentName,
componentVersion,
cveId,
cveName,
cvssScore,
cvssScores,
cvssV2Score,
cvssV3Score,
cvssVersion,
description,
effectiveCvssScore,
effectiveCvssVersion,
links,
provisioningState,
severity,
systemData,
type
FROM azure.iotfirmwaredefense.cves
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND firmware_id = '{{ firmware_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
