--- 
title: virtual_machine_scale_set_life_cycle_hook_events
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_life_cycle_hook_events
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_set_life_cycle_hook_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_scale_set_life_cycle_hook_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_life_cycle_hook_events" /></td></tr>
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
    <td><CopyableCode code="additionalContext" /></td>
    <td><code>object</code></td>
    <td>Additional key-value pairs set on the lifecycle hook event that gives customer some useful context/data. The keys in this dictionary are specific to the lifecycle hook type. Different lifecycle hook events can have different sets of keys in the additional context depending on the lifecycle hook type. For example, for a lifecycle hook event with UpgradeAutoOSScheduling type, the additional context can contain the key "priority" that helps customer identify the priority of the Auto OS Upgrade operation triggered on the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultAction" /></td>
    <td><code>string</code></td>
    <td>Specify the action that will be applied on the a target resource in the virtual machine scale set lifecycle hook event if the platform does not get a response from the customer for the target resource before waitUntil. Known values are: "Approve" and "Reject". (Approve, Reject)</td>
</tr>
<tr>
    <td><CopyableCode code="maxWaitUntil" /></td>
    <td><code>string</code></td>
    <td>Specifies the exact UTC timestamp in ISO 8601 format till when the customer can delay the lifecycle hook event. The customer will not be allowed to delay the event to a timestamp beyond this.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the virtual machine scale set lifecycle hook event. Known values are: "Active" and "Completed". (Active, Completed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResources" /></td>
    <td><code>array</code></td>
    <td>List of target resources which are getting processed in the virtual machine scale set lifecycle hook event.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string</code></td>
    <td>The UTC timestamp in ISO 8601 format at which the platform creates the virtual machine scale set lifecycle hook event entity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="waitUntil" /></td>
    <td><code>string</code></td>
    <td>Specifies the exact UTC timestamp in ISO 8601 format till which the event would remain in the current lifecycle state waiting for an action from the customer. Beyond this timestamp, the platform will apply the defaultAction for the event.</td>
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
    <td><CopyableCode code="additionalContext" /></td>
    <td><code>object</code></td>
    <td>Additional key-value pairs set on the lifecycle hook event that gives customer some useful context/data. The keys in this dictionary are specific to the lifecycle hook type. Different lifecycle hook events can have different sets of keys in the additional context depending on the lifecycle hook type. For example, for a lifecycle hook event with UpgradeAutoOSScheduling type, the additional context can contain the key "priority" that helps customer identify the priority of the Auto OS Upgrade operation triggered on the virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultAction" /></td>
    <td><code>string</code></td>
    <td>Specify the action that will be applied on the a target resource in the virtual machine scale set lifecycle hook event if the platform does not get a response from the customer for the target resource before waitUntil. Known values are: "Approve" and "Reject". (Approve, Reject)</td>
</tr>
<tr>
    <td><CopyableCode code="maxWaitUntil" /></td>
    <td><code>string</code></td>
    <td>Specifies the exact UTC timestamp in ISO 8601 format till when the customer can delay the lifecycle hook event. The customer will not be allowed to delay the event to a timestamp beyond this.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the virtual machine scale set lifecycle hook event. Known values are: "Active" and "Completed". (Active, Completed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResources" /></td>
    <td><code>array</code></td>
    <td>List of target resources which are getting processed in the virtual machine scale set lifecycle hook event.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string</code></td>
    <td>The UTC timestamp in ISO 8601 format at which the platform creates the virtual machine scale set lifecycle hook event entity.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="waitUntil" /></td>
    <td><code>string</code></td>
    <td>Specifies the exact UTC timestamp in ISO 8601 format till which the event would remain in the current lifecycle state waiting for an action from the customer. Beyond this timestamp, the platform will apply the defaultAction for the event.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-lifecycle_hook_event_name"><code>lifecycle_hook_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a virtual machine scale set lifecycle hook event.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of virtual machine scale set lifecycle hook events created for a virtual machine scale set resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_scale_set_name"><code>vm_scale_set_name</code></a>, <a href="#parameter-lifecycle_hook_event_name"><code>lifecycle_hook_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update a virtual machine scale set lifecycle hook event.</td>
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
<tr id="parameter-lifecycle_hook_event_name">
    <td><CopyableCode code="lifecycle_hook_event_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VMScaleSetLifecycleHookEvent. Required.</td>
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
<tr id="parameter-vm_scale_set_name">
    <td><CopyableCode code="vm_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VM scale set. Required.</td>
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

Gets a virtual machine scale set lifecycle hook event.

```sql
SELECT
id,
name,
additionalContext,
defaultAction,
maxWaitUntil,
state,
systemData,
targetResources,
timeCreated,
type,
waitUntil
FROM azure.compute.virtual_machine_scale_set_life_cycle_hook_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' -- required
AND lifecycle_hook_event_name = '{{ lifecycle_hook_event_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of virtual machine scale set lifecycle hook events created for a virtual machine scale set resource.

```sql
SELECT
id,
name,
additionalContext,
defaultAction,
maxWaitUntil,
state,
systemData,
targetResources,
timeCreated,
type,
waitUntil
FROM azure.compute.virtual_machine_scale_set_life_cycle_hook_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

The operation to update a virtual machine scale set lifecycle hook event.

```sql
UPDATE azure.compute.virtual_machine_scale_set_life_cycle_hook_events
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_scale_set_name = '{{ vm_scale_set_name }}' --required
AND lifecycle_hook_event_name = '{{ lifecycle_hook_event_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
