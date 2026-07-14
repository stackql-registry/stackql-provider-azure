--- 
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - compute_schedule
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

Creates, updates, deletes, gets or lists a <code>scheduled_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scheduled_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute_schedule.scheduled_actions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The action the scheduled action should perform in the resources. Required. Known values are: "Start", "Deallocate", and "Hibernate". (Start, Deallocate, Hibernate)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>Tell if the scheduled action is disabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the scheduled action is supposed to stop scheduling.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSettings" /></td>
    <td><code>array</code></td>
    <td>The notification settings for the scheduled action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last provisioning operation performed on the resource. Known values are: "Succeeded", "Failed", "Canceled", and "Deleting". (Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The type of resource the scheduled action is targeting. Required. Known values are: "VirtualMachine" and "VirtualMachineScaleSet". (VirtualMachine, VirtualMachineScaleSet)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>The schedule the scheduled action is supposed to follow. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time which the scheduled action is supposed to start running. Required.</td>
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
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The action the scheduled action should perform in the resources. Required. Known values are: "Start", "Deallocate", and "Hibernate". (Start, Deallocate, Hibernate)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>Tell if the scheduled action is disabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the scheduled action is supposed to stop scheduling.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSettings" /></td>
    <td><code>array</code></td>
    <td>The notification settings for the scheduled action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last provisioning operation performed on the resource. Known values are: "Succeeded", "Failed", "Canceled", and "Deleting". (Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The type of resource the scheduled action is targeting. Required. Known values are: "VirtualMachine" and "VirtualMachineScaleSet". (VirtualMachine, VirtualMachineScaleSet)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>The schedule the scheduled action is supposed to follow. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time which the scheduled action is supposed to start running. Required.</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>The action the scheduled action should perform in the resources. Required. Known values are: "Start", "Deallocate", and "Hibernate". (Start, Deallocate, Hibernate)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>Tell if the scheduled action is disabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the scheduled action is supposed to stop scheduling.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSettings" /></td>
    <td><code>array</code></td>
    <td>The notification settings for the scheduled action. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last provisioning operation performed on the resource. Known values are: "Succeeded", "Failed", "Canceled", and "Deleting". (Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The type of resource the scheduled action is targeting. Required. Known values are: "VirtualMachine" and "VirtualMachineScaleSet". (VirtualMachine, VirtualMachineScaleSet)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>The schedule the scheduled action is supposed to follow. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time which the scheduled action is supposed to start running. Required.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ScheduledAction.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ScheduledAction resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ScheduledAction resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ScheduledAction.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a ScheduledAction.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ScheduledAction.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ScheduledAction.</td>
</tr>
<tr>
    <td><a href="#list_resources"><CopyableCode code="list_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List resources attached to Scheduled Actions.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_submit_deallocate"><CopyableCode code="virtual_machines_submit_deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-schedule"><code>schedule</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesSubmitDeallocate: Schedule deallocate operation for a batch of virtual machines at datetime in future.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_submit_hibernate"><CopyableCode code="virtual_machines_submit_hibernate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-schedule"><code>schedule</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesSubmitHibernate: Schedule hibernate operation for a batch of virtual machines at datetime in future.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_submit_start"><CopyableCode code="virtual_machines_submit_start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-schedule"><code>schedule</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesSubmitStart: Schedule start operation for a batch of virtual machines at datetime in future.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_deallocate"><CopyableCode code="virtual_machines_execute_deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteDeallocate: Execute deallocate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_hibernate"><CopyableCode code="virtual_machines_execute_hibernate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteHibernate: Execute hibernate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_start"><CopyableCode code="virtual_machines_execute_start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteStart: Execute start operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_create"><CopyableCode code="virtual_machines_execute_create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceConfigParameters"><code>resourceConfigParameters</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteCreate: Execute create operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_delete"><CopyableCode code="virtual_machines_execute_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-resources"><code>resources</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteDelete: Execute delete operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_get_operation_status"><CopyableCode code="virtual_machines_get_operation_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-operationIds"><code>operationIds</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesGetOperationStatus: Polling endpoint to read status of operations performed on virtual machines.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_cancel_operations"><CopyableCode code="virtual_machines_cancel_operations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-operationIds"><code>operationIds</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesCancelOperations: Cancel a previously submitted (start/deallocate/hibernate) request.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_get_operation_errors"><CopyableCode code="virtual_machines_get_operation_errors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-locationparameter"><code>locationparameter</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-operationIds"><code>operationIds</code></a></td>
    <td></td>
    <td>VirtualMachinesGetOperationErrors: Get error details on operation errors (like transient errors encountered, additional logs) if they exist.</td>
</tr>
<tr>
    <td><a href="#attach_resources"><CopyableCode code="attach_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resources"><code>resources</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#detach_resources"><CopyableCode code="detach_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resources"><code>resources</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#patch_resources"><CopyableCode code="patch_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resources"><code>resources</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#cancel_next_occurrence"><CopyableCode code="cancel_next_occurrence" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceIds"><code>resourceIds</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
</tr>
<tr>
    <td><a href="#trigger_manual_occurrence"><CopyableCode code="trigger_manual_occurrence" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-scheduled_action_name"><code>scheduled_action_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>A synchronous resource action.</td>
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
<tr id="parameter-locationparameter">
    <td><CopyableCode code="locationparameter" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scheduled_action_name">
    <td><CopyableCode code="scheduled_action_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ScheduledAction. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a ScheduledAction.

```sql
SELECT
id,
name,
actionType,
disabled,
endTime,
location,
notificationSettings,
provisioningState,
resourceType,
schedule,
startTime,
systemData,
tags,
type
FROM azure.compute_schedule.scheduled_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND scheduled_action_name = '{{ scheduled_action_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List ScheduledAction resources by resource group.

```sql
SELECT
id,
name,
actionType,
disabled,
endTime,
location,
notificationSettings,
provisioningState,
resourceType,
schedule,
startTime,
systemData,
tags,
type
FROM azure.compute_schedule.scheduled_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List ScheduledAction resources by subscription ID.

```sql
SELECT
id,
name,
actionType,
disabled,
endTime,
location,
notificationSettings,
provisioningState,
resourceType,
schedule,
startTime,
systemData,
tags,
type
FROM azure.compute_schedule.scheduled_actions
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create a ScheduledAction.

```sql
INSERT INTO azure.compute_schedule.scheduled_actions (
tags,
location,
properties,
resource_group_name,
scheduled_action_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ scheduled_action_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: scheduled_actions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scheduled_actions resource.
    - name: scheduled_action_name
      value: "{{ scheduled_action_name }}"
      description: Required parameter for the scheduled_actions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scheduled_actions resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        resourceType: "{{ resourceType }}"
        actionType: "{{ actionType }}"
        startTime: "{{ startTime }}"
        endTime: "{{ endTime }}"
        schedule:
          scheduledTime: "{{ scheduledTime }}"
          timeZone: "{{ timeZone }}"
          requestedWeekDays:
            - "{{ requestedWeekDays }}"
          requestedMonths:
            - "{{ requestedMonths }}"
          requestedDaysOfTheMonth:
            - {{ requestedDaysOfTheMonth }}
          executionParameters:
            optimizationPreference: "{{ optimizationPreference }}"
            retryPolicy:
              retryCount: {{ retryCount }}
              retryWindowInMinutes: {{ retryWindowInMinutes }}
          deadlineType: "{{ deadlineType }}"
        notificationSettings:
          - destination: "{{ destination }}"
            type: "{{ type }}"
            language: "{{ language }}"
            disabled: {{ disabled }}
        disabled: {{ disabled }}
        provisioningState: "{{ provisioningState }}"
`}</CodeBlock>

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

Update a ScheduledAction.

```sql
UPDATE azure.compute_schedule.scheduled_actions
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND scheduled_action_name = '{{ scheduled_action_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a ScheduledAction.

```sql
REPLACE azure.compute_schedule.scheduled_actions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND scheduled_action_name = '{{ scheduled_action_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a ScheduledAction.

```sql
DELETE FROM azure.compute_schedule.scheduled_actions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND scheduled_action_name = '{{ scheduled_action_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_resources"
    values={[
        { label: 'list_resources', value: 'list_resources' },
        { label: 'virtual_machines_submit_deallocate', value: 'virtual_machines_submit_deallocate' },
        { label: 'virtual_machines_submit_hibernate', value: 'virtual_machines_submit_hibernate' },
        { label: 'virtual_machines_submit_start', value: 'virtual_machines_submit_start' },
        { label: 'virtual_machines_execute_deallocate', value: 'virtual_machines_execute_deallocate' },
        { label: 'virtual_machines_execute_hibernate', value: 'virtual_machines_execute_hibernate' },
        { label: 'virtual_machines_execute_start', value: 'virtual_machines_execute_start' },
        { label: 'virtual_machines_execute_create', value: 'virtual_machines_execute_create' },
        { label: 'virtual_machines_execute_delete', value: 'virtual_machines_execute_delete' },
        { label: 'virtual_machines_get_operation_status', value: 'virtual_machines_get_operation_status' },
        { label: 'virtual_machines_cancel_operations', value: 'virtual_machines_cancel_operations' },
        { label: 'virtual_machines_get_operation_errors', value: 'virtual_machines_get_operation_errors' },
        { label: 'attach_resources', value: 'attach_resources' },
        { label: 'detach_resources', value: 'detach_resources' },
        { label: 'patch_resources', value: 'patch_resources' },
        { label: 'disable', value: 'disable' },
        { label: 'enable', value: 'enable' },
        { label: 'cancel_next_occurrence', value: 'cancel_next_occurrence' },
        { label: 'trigger_manual_occurrence', value: 'trigger_manual_occurrence' }
    ]}
>
<TabItem value="list_resources">

List resources attached to Scheduled Actions.

```sql
EXEC azure.compute_schedule.scheduled_actions.list_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="virtual_machines_submit_deallocate">

VirtualMachinesSubmitDeallocate: Schedule deallocate operation for a batch of virtual machines at datetime in future.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_submit_deallocate 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"schedule": "{{ schedule }}", 
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_submit_hibernate">

VirtualMachinesSubmitHibernate: Schedule hibernate operation for a batch of virtual machines at datetime in future.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_submit_hibernate 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"schedule": "{{ schedule }}", 
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_submit_start">

VirtualMachinesSubmitStart: Schedule start operation for a batch of virtual machines at datetime in future.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_submit_start 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"schedule": "{{ schedule }}", 
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_execute_deallocate">

VirtualMachinesExecuteDeallocate: Execute deallocate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_execute_deallocate 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_execute_hibernate">

VirtualMachinesExecuteHibernate: Execute hibernate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_execute_hibernate 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_execute_start">

VirtualMachinesExecuteStart: Execute start operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_execute_start 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_execute_create">

VirtualMachinesExecuteCreate: Execute create operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_execute_create 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceConfigParameters": "{{ resourceConfigParameters }}", 
"executionParameters": "{{ executionParameters }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_execute_delete">

VirtualMachinesExecuteDelete: Execute delete operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_execute_delete 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"executionParameters": "{{ executionParameters }}", 
"resources": "{{ resources }}", 
"correlationid": "{{ correlationid }}", 
"forceDeletion": {{ forceDeletion }}
}'
;
```
</TabItem>
<TabItem value="virtual_machines_get_operation_status">

VirtualMachinesGetOperationStatus: Polling endpoint to read status of operations performed on virtual machines.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_get_operation_status 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"operationIds": "{{ operationIds }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_cancel_operations">

VirtualMachinesCancelOperations: Cancel a previously submitted (start/deallocate/hibernate) request.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_cancel_operations 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"operationIds": "{{ operationIds }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
<TabItem value="virtual_machines_get_operation_errors">

VirtualMachinesGetOperationErrors: Get error details on operation errors (like transient errors encountered, additional logs) if they exist.

```sql
EXEC azure.compute_schedule.scheduled_actions.virtual_machines_get_operation_errors 
@locationparameter='{{ locationparameter }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"operationIds": "{{ operationIds }}"
}'
;
```
</TabItem>
<TabItem value="attach_resources">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.attach_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resources": "{{ resources }}"
}'
;
```
</TabItem>
<TabItem value="detach_resources">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.detach_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resources": "{{ resources }}"
}'
;
```
</TabItem>
<TabItem value="patch_resources">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.patch_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resources": "{{ resources }}"
}'
;
```
</TabItem>
<TabItem value="disable">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.disable 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.enable 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel_next_occurrence">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.cancel_next_occurrence 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}"
}'
;
```
</TabItem>
<TabItem value="trigger_manual_occurrence">

A synchronous resource action.

```sql
EXEC azure.compute_schedule.scheduled_actions.trigger_manual_occurrence 
@resource_group_name='{{ resource_group_name }}' --required, 
@scheduled_action_name='{{ scheduled_action_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
