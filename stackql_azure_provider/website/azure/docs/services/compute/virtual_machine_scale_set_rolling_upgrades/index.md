--- 
title: virtual_machine_scale_set_rolling_upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_rolling_upgrades
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_set_rolling_upgrades</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_scale_set_rolling_upgrades" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_rolling_upgrades" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_latest"
    values={[
        { label: 'get_latest', value: 'get_latest' }
    ]}
>
<TabItem value="get_latest">

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
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details for this upgrade, if there are any.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="policy" /></td>
    <td><code>object</code></td>
    <td>The rolling upgrade policies applied for this upgrade.</td>
</tr>
<tr>
    <td><CopyableCode code="progress" /></td>
    <td><code>object</code></td>
    <td>Information about the number of virtual machine instances in each upgrade state.</td>
</tr>
<tr>
    <td><CopyableCode code="runningStatus" /></td>
    <td><code>object</code></td>
    <td>Information about the current running state of the overall upgrade.</td>
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
    <td><a href="#get_latest"><CopyableCode code="get_latest" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of the latest virtual machine scale set rolling upgrade.</td>
</tr>
<tr>
    <td><a href="#start_extension_upgrade"><CopyableCode code="start_extension_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to the latest available extension version. Instances which are already running the latest extension versions are not affected.</td>
</tr>
<tr>
    <td><a href="#start_os_upgrade"><CopyableCode code="start_os_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a rolling upgrade to move all virtual machine scale set instances to the latest available Platform Image OS version. Instances which are already running the latest available OS version are not affected.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels the current virtual machine scale set rolling upgrade.</td>
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
<tr id="parameter-vm_scale_set_name">
    <td><CopyableCode code="vm_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VM scale set. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_latest"
    values={[
        { label: 'get_latest', value: 'get_latest' }
    ]}
>
<TabItem value="get_latest">

Gets the status of the latest virtual machine scale set rolling upgrade.

```sql
SELECT
id,
name,
error,
location,
policy,
progress,
runningStatus,
systemData,
tags,
type
FROM azure.compute.virtual_machine_scale_set_rolling_upgrades
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_extension_upgrade"
    values={[
        { label: 'start_extension_upgrade', value: 'start_extension_upgrade' },
        { label: 'start_os_upgrade', value: 'start_os_upgrade' },
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="start_extension_upgrade">

Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to the latest available extension version. Instances which are already running the latest extension versions are not affected.

```sql
EXEC azure.compute.virtual_machine_scale_set_rolling_upgrades.start_extension_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_os_upgrade">

Starts a rolling upgrade to move all virtual machine scale set instances to the latest available Platform Image OS version. Instances which are already running the latest available OS version are not affected.

```sql
EXEC azure.compute.virtual_machine_scale_set_rolling_upgrades.start_os_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancels the current virtual machine scale set rolling upgrade.

```sql
EXEC azure.compute.virtual_machine_scale_set_rolling_upgrades.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@vm_scale_set_name='{{ vm_scale_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
