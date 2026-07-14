--- 
title: major_version_upgrade_precheck
hide_title: false
hide_table_of_contents: false
keywords:
  - major_version_upgrade_precheck
  - postgresql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>major_version_upgrade_precheck</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="major_version_upgrade_precheck" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_flexible_servers.major_version_upgrade_precheck" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the precheck was created.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDetails" /></td>
    <td><code>array</code></td>
    <td>Array of policy validation details.</td>
</tr>
<tr>
    <td><CopyableCode code="precheckResult" /></td>
    <td><code>object</code></td>
    <td>The detailed result of the precheck operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the precheck validation. Known values are: "Validating", "Succeeded", "Failed", and "Canceled". (Validating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetVersion" /></td>
    <td><code>string</code></td>
    <td>The target PostgreSQL major version for the upgrade. Known values are: "18", "17", "16", "15", "14", "13", "12", and "11". (18, 17, 16, 15, 14, 13, 12, 11)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="createTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the precheck was created.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDetails" /></td>
    <td><code>array</code></td>
    <td>Array of policy validation details.</td>
</tr>
<tr>
    <td><CopyableCode code="precheckResult" /></td>
    <td><code>object</code></td>
    <td>The detailed result of the precheck operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the precheck validation. Known values are: "Validating", "Succeeded", "Failed", and "Canceled". (Validating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetVersion" /></td>
    <td><code>string</code></td>
    <td>The target PostgreSQL major version for the upgrade. Known values are: "18", "17", "16", "15", "14", "13", "12", and "11". (18, 17, 16, 15, 14, 13, 12, 11)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-precheck_validation_id"><code>precheck_validation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a major version upgrade precheck for a flexible server.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists major version upgrade prechecks for a flexible server.</td>
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
<tr id="parameter-precheck_validation_id">
    <td><CopyableCode code="precheck_validation_id" /></td>
    <td><code>string</code></td>
    <td>The name of the MajorVersionUpgradePrecheckResource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets information about a major version upgrade precheck for a flexible server.

```sql
SELECT
id,
name,
createTime,
policyDetails,
precheckResult,
status,
systemData,
targetVersion,
type
FROM azure.postgresql_flexible_servers.major_version_upgrade_precheck
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND precheck_validation_id = '{{ precheck_validation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists major version upgrade prechecks for a flexible server.

```sql
SELECT
id,
name,
createTime,
policyDetails,
precheckResult,
status,
systemData,
targetVersion,
type
FROM azure.postgresql_flexible_servers.major_version_upgrade_precheck
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
