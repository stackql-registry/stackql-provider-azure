--- 
title: bulk_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - bulk_actions
  - compute_bulk_actions
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

Creates, updates, deletes, gets or lists a <code>bulk_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bulk_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute_bulk_actions.bulk_actions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_operation_status', value: 'get_operation_status' },
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
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>Total capacity to achieve. It can be in terms of VMs or vCPUs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityType" /></td>
    <td><code>string</code></td>
    <td>Specifies capacity type for launching instances. It can be in terms of VMs or vCPUs. Known values are: "VM" and "VCpu". (VM, VCpu)</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>Compute Profile to configure the Virtual Machines. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Details of the resource plan.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Regular or Spot instances in LaunchBulkInstancesOperation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Creating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Succeeded, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="retryPolicy" /></td>
    <td><code>object</code></td>
    <td>Retry policy the user can pass.</td>
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
<tr>
    <td><CopyableCode code="vmAttributes" /></td>
    <td><code>object</code></td>
    <td>Attributes to launch instances.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSizesProfile" /></td>
    <td><code>array</code></td>
    <td>List of VM sizes supported for LaunchBulkInstancesOperation.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneAllocationPolicy" /></td>
    <td><code>object</code></td>
    <td>Zone Allocation Policy for launching instances.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Zones in which the LaunchBulkInstancesOperation is available.</td>
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
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>Total capacity to achieve. It can be in terms of VMs or vCPUs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityType" /></td>
    <td><code>string</code></td>
    <td>Specifies capacity type for launching instances. It can be in terms of VMs or vCPUs. Known values are: "VM" and "VCpu". (VM, VCpu)</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>Compute Profile to configure the Virtual Machines. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Details of the resource plan.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Regular or Spot instances in LaunchBulkInstancesOperation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Creating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Succeeded, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="retryPolicy" /></td>
    <td><code>object</code></td>
    <td>Retry policy the user can pass.</td>
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
<tr>
    <td><CopyableCode code="vmAttributes" /></td>
    <td><code>object</code></td>
    <td>Attributes to launch instances.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSizesProfile" /></td>
    <td><code>array</code></td>
    <td>List of VM sizes supported for LaunchBulkInstancesOperation.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneAllocationPolicy" /></td>
    <td><code>object</code></td>
    <td>Zone Allocation Policy for launching instances.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Zones in which the LaunchBulkInstancesOperation is available.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_operation_status">

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
    <td>Fully qualified ID for the async operation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the async operation.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>If present, details of the operation error.</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>The operations list.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>number</code></td>
    <td>Percent of the operation that is complete.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified ID of the resource against which the original async operation was started.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Required.</td>
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
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>Total capacity to achieve. It can be in terms of VMs or vCPUs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityType" /></td>
    <td><code>string</code></td>
    <td>Specifies capacity type for launching instances. It can be in terms of VMs or vCPUs. Known values are: "VM" and "VCpu". (VM, VCpu)</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>Compute Profile to configure the Virtual Machines. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Details of the resource plan.</td>
</tr>
<tr>
    <td><CopyableCode code="priorityProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration Options for Regular or Spot instances in LaunchBulkInstancesOperation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Creating", "Succeeded", "Failed", "Deleting", and "Canceled". (Creating, Succeeded, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="retryPolicy" /></td>
    <td><code>object</code></td>
    <td>Retry policy the user can pass.</td>
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
<tr>
    <td><CopyableCode code="vmAttributes" /></td>
    <td><code>object</code></td>
    <td>Attributes to launch instances.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSizesProfile" /></td>
    <td><code>array</code></td>
    <td>List of VM sizes supported for LaunchBulkInstancesOperation.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneAllocationPolicy" /></td>
    <td><code>object</code></td>
    <td>Zone Allocation Policy for launching instances.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Zones in which the LaunchBulkInstancesOperation is available.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an instance of LaunchBulkInstancesOperations.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List LaunchBulkInstancesOperation resources by resource group.</td>
</tr>
<tr>
    <td><a href="#get_operation_status"><CopyableCode code="get_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of a LaunchBulkInstancesOperation.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List LaunchBulkInstancesOperation resources by subscriptionId.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates LaunchBulkInstancesOperations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates LaunchBulkInstancesOperations.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteInstances"><code>deleteInstances</code></a></td>
    <td>Deletes LaunchBulkInstancesOperations.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machines"><CopyableCode code="list_virtual_machines" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>List VirtualMachine resources of a LaunchBulkInstancesOperation.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels LaunchBulkInstancesOperation instances that have not yet launched.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_deallocate"><CopyableCode code="virtual_machines_execute_deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteDeallocate: Execute deallocate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_hibernate"><CopyableCode code="virtual_machines_execute_hibernate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteHibernate: Execute hibernate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_start"><CopyableCode code="virtual_machines_execute_start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteStart: Execute start operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_create"><CopyableCode code="virtual_machines_execute_create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceConfigParameters"><code>resourceConfigParameters</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteCreate: Execute create operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_execute_delete"><CopyableCode code="virtual_machines_execute_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-executionParameters"><code>executionParameters</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesExecuteDelete: Execute delete operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_get_operation_status"><CopyableCode code="virtual_machines_get_operation_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-operationIds"><code>operationIds</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesGetOperationStatus: Polling endpoint to read status of operations performed on virtual machines.</td>
</tr>
<tr>
    <td><a href="#virtual_machines_cancel_operations"><CopyableCode code="virtual_machines_cancel_operations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-operationIds"><code>operationIds</code></a>, <a href="#parameter-correlationid"><code>correlationid</code></a></td>
    <td></td>
    <td>VirtualMachinesCancelOperations: Cancel a previously submitted (start/deallocate/hibernate) request.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The async operation id. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the LaunchBulkInstancesOperation. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter expression to filter the virtual machines. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Skip token for pagination. Uses the token from a previous response to fetch the next page of results. Default value is None.</td>
</tr>
<tr id="parameter-deleteInstances">
    <td><CopyableCode code="deleteInstances" /></td>
    <td><code>boolean</code></td>
    <td>When true, deletes all virtual machines created by this BulkAction Operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets an instance of LaunchBulkInstancesOperations.

```sql
SELECT
id,
name,
capacity,
capacityType,
computeProfile,
identity,
plan,
priorityProfile,
provisioningState,
retryPolicy,
systemData,
tags,
type,
vmAttributes,
vmSizesProfile,
zoneAllocationPolicy,
zones
FROM azure.compute_bulk_actions.bulk_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List LaunchBulkInstancesOperation resources by resource group.

```sql
SELECT
id,
name,
capacity,
capacityType,
computeProfile,
identity,
plan,
priorityProfile,
provisioningState,
retryPolicy,
systemData,
tags,
type,
vmAttributes,
vmSizesProfile,
zoneAllocationPolicy,
zones
FROM azure.compute_bulk_actions.bulk_actions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_operation_status">

Get the status of a LaunchBulkInstancesOperation.

```sql
SELECT
id,
name,
endTime,
error,
operations,
percentComplete,
resourceId,
startTime,
status
FROM azure.compute_bulk_actions.bulk_actions
WHERE location = '{{ location }}' -- required
AND id = '{{ id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List LaunchBulkInstancesOperation resources by subscriptionId.

```sql
SELECT
id,
name,
capacity,
capacityType,
computeProfile,
identity,
plan,
priorityProfile,
provisioningState,
retryPolicy,
systemData,
tags,
type,
vmAttributes,
vmSizesProfile,
zoneAllocationPolicy,
zones
FROM azure.compute_bulk_actions.bulk_actions
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates LaunchBulkInstancesOperations.

```sql
INSERT INTO azure.compute_bulk_actions.bulk_actions (
properties,
zones,
tags,
identity,
plan,
resource_group_name,
location,
name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ zones }}',
'{{ tags }}',
'{{ identity }}',
'{{ plan }}',
'{{ resource_group_name }}',
'{{ location }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
plan,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bulk_actions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bulk_actions resource.
    - name: location
      value: "{{ location }}"
      description: Required parameter for the bulk_actions resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the bulk_actions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bulk_actions resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        capacity: {{ capacity }}
        capacityType: "{{ capacityType }}"
        priorityProfile:
          type: "{{ type }}"
          maxPricePerVM: {{ maxPricePerVM }}
          evictionPolicy: "{{ evictionPolicy }}"
          allocationStrategy: "{{ allocationStrategy }}"
        vmSizesProfile:
          - name: "{{ name }}"
            rank: {{ rank }}
        vmAttributes:
          vCpuCount:
            min: {{ min }}
            max: {{ max }}
          memoryInGiB:
            min: {{ min }}
            max: {{ max }}
          architectureTypes:
            - "{{ architectureTypes }}"
          memoryInGiBPerVCpu:
            min: {{ min }}
            max: {{ max }}
          localStorageSupport: "{{ localStorageSupport }}"
          localStorageInGiB:
            min: {{ min }}
            max: {{ max }}
          localStorageDiskTypes:
            - "{{ localStorageDiskTypes }}"
          dataDiskCount:
            min: {{ min }}
            max: {{ max }}
          networkInterfaceCount:
            min: {{ min }}
            max: {{ max }}
          networkBandwidthInMbps:
            min: {{ min }}
            max: {{ max }}
          rdmaSupport: "{{ rdmaSupport }}"
          rdmaNetworkInterfaceCount:
            min: {{ min }}
            max: {{ max }}
          acceleratorSupport: "{{ acceleratorSupport }}"
          acceleratorManufacturers:
            - "{{ acceleratorManufacturers }}"
          acceleratorTypes:
            - "{{ acceleratorTypes }}"
          acceleratorCount:
            min: {{ min }}
            max: {{ max }}
          vmCategories:
            - "{{ vmCategories }}"
          cpuManufacturers:
            - "{{ cpuManufacturers }}"
          hyperVGenerations:
            - "{{ hyperVGenerations }}"
          burstableSupport: "{{ burstableSupport }}"
          allowedVMSizes:
            - "{{ allowedVMSizes }}"
          excludedVMSizes:
            - "{{ excludedVMSizes }}"
        computeProfile:
          virtualMachineProfile:
            scheduledEventsPolicy:
              userInitiatedRedeploy:
                automaticallyApprove: {{ automaticallyApprove }}
              userInitiatedReboot:
                automaticallyApprove: {{ automaticallyApprove }}
              scheduledEventsAdditionalPublishingTargets:
                eventGridAndResourceGraph: "{{ eventGridAndResourceGraph }}"
              allInstancesDown:
                automaticallyApprove: {{ automaticallyApprove }}
            storageProfile:
              imageReference:
                id: "{{ id }}"
                publisher: "{{ publisher }}"
                offer: "{{ offer }}"
                sku: "{{ sku }}"
                version: "{{ version }}"
                sharedGalleryImageId: "{{ sharedGalleryImageId }}"
                communityGalleryImageId: "{{ communityGalleryImageId }}"
              osDisk:
                osType: "{{ osType }}"
                encryptionSettings: "{{ encryptionSettings }}"
                name: "{{ name }}"
                vhd: "{{ vhd }}"
                image: "{{ image }}"
                caching: "{{ caching }}"
                writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
                diffDiskSettings: "{{ diffDiskSettings }}"
                createOption: "{{ createOption }}"
                diskSizeGB: {{ diskSizeGB }}
                managedDisk: "{{ managedDisk }}"
                deleteOption: "{{ deleteOption }}"
              dataDisks:
                - lun: {{ lun }}
                  name: "{{ name }}"
                  vhd:
                    uri: "{{ uri }}"
                  image:
                    uri: "{{ uri }}"
                  caching: "{{ caching }}"
                  writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
                  createOption: "{{ createOption }}"
                  diskSizeGB: {{ diskSizeGB }}
                  managedDisk:
                    id: "{{ id }}"
                    storageAccountType: "{{ storageAccountType }}"
                    diskEncryptionSet: "{{ diskEncryptionSet }}"
                    securityProfile: "{{ securityProfile }}"
                  sourceResource:
                    id: "{{ id }}"
                  toBeDetached: {{ toBeDetached }}
                  detachOption: "{{ detachOption }}"
                  deleteOption: "{{ deleteOption }}"
              diskControllerType: "{{ diskControllerType }}"
            additionalCapabilities:
              ultraSSDEnabled: {{ ultraSSDEnabled }}
              hibernationEnabled: {{ hibernationEnabled }}
            osProfile:
              computerName: "{{ computerName }}"
              adminUsername: "{{ adminUsername }}"
              adminPassword: "{{ adminPassword }}"
              customData: "{{ customData }}"
              windowsConfiguration:
                provisionVMAgent: {{ provisionVMAgent }}
                enableAutomaticUpdates: {{ enableAutomaticUpdates }}
                timeZone: "{{ timeZone }}"
                additionalUnattendContent: "{{ additionalUnattendContent }}"
                patchSettings: "{{ patchSettings }}"
                winRM: "{{ winRM }}"
              linuxConfiguration:
                disablePasswordAuthentication: {{ disablePasswordAuthentication }}
                ssh: "{{ ssh }}"
                provisionVMAgent: {{ provisionVMAgent }}
                patchSettings: "{{ patchSettings }}"
                enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
              secrets:
                - sourceVault:
                    id: "{{ id }}"
                  vaultCertificates: "{{ vaultCertificates }}"
              allowExtensionOperations: {{ allowExtensionOperations }}
              requireGuestProvisionSignal: {{ requireGuestProvisionSignal }}
            networkProfile:
              networkInterfaces:
                - id: "{{ id }}"
                  properties:
                    primary: {{ primary }}
                    deleteOption: "{{ deleteOption }}"
              networkApiVersion: "{{ networkApiVersion }}"
              networkInterfaceConfigurations:
                - name: "{{ name }}"
                  properties:
                    primary: {{ primary }}
                    deleteOption: "{{ deleteOption }}"
                    enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
                    disableTcpStateTracking: {{ disableTcpStateTracking }}
                    enableFpga: {{ enableFpga }}
                    enableIPForwarding: {{ enableIPForwarding }}
                    networkSecurityGroup: "{{ networkSecurityGroup }}"
                    dnsSettings: "{{ dnsSettings }}"
                    ipConfigurations: "{{ ipConfigurations }}"
                    dscpConfiguration: "{{ dscpConfiguration }}"
                    auxiliaryMode: "{{ auxiliaryMode }}"
                    auxiliarySku: "{{ auxiliarySku }}"
                  tags: "{{ tags }}"
            securityProfile:
              uefiSettings:
                secureBootEnabled: {{ secureBootEnabled }}
                vTpmEnabled: {{ vTpmEnabled }}
              encryptionAtHost: {{ encryptionAtHost }}
              securityType: "{{ securityType }}"
              encryptionIdentity:
                userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
              proxyAgentSettings:
                enabled: {{ enabled }}
                mode: "{{ mode }}"
                keyIncarnationId: {{ keyIncarnationId }}
                wireServer: "{{ wireServer }}"
                imds: "{{ imds }}"
                addProxyAgentExtension: {{ addProxyAgentExtension }}
            diagnosticsProfile:
              bootDiagnostics:
                enabled: {{ enabled }}
                storageUri: "{{ storageUri }}"
            licenseType: "{{ licenseType }}"
            extensionsTimeBudget: "{{ extensionsTimeBudget }}"
            scheduledEventsProfile:
              terminateNotificationProfile:
                notBeforeTimeout: "{{ notBeforeTimeout }}"
                enable: {{ enable }}
              osImageNotificationProfile:
                notBeforeTimeout: "{{ notBeforeTimeout }}"
                enable: {{ enable }}
            userData: "{{ userData }}"
            capacityReservation:
              capacityReservationGroup:
                id: "{{ id }}"
            applicationProfile:
              galleryApplications:
                - tags: "{{ tags }}"
                  order: {{ order }}
                  packageReferenceId: "{{ packageReferenceId }}"
                  configurationReference: "{{ configurationReference }}"
                  treatFailureAsDeploymentFailure: {{ treatFailureAsDeploymentFailure }}
                  enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
          extensions:
            - name: "{{ name }}"
              properties:
                forceUpdateTag: "{{ forceUpdateTag }}"
                publisher: "{{ publisher }}"
                type: "{{ type }}"
                typeHandlerVersion: "{{ typeHandlerVersion }}"
                autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
                enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
                settings: "{{ settings }}"
                protectedSettings: "{{ protectedSettings }}"
                suppressFailures: {{ suppressFailures }}
                protectedSettingsFromKeyVault:
                  secretUrl: "{{ secretUrl }}"
                  sourceVault: "{{ sourceVault }}"
                provisionAfterExtensions:
                  - "{{ provisionAfterExtensions }}"
          computeApiVersion: "{{ computeApiVersion }}"
        zoneAllocationPolicy:
          distributionStrategy: "{{ distributionStrategy }}"
          zonePreferences:
            - zone: "{{ zone }}"
              rank: {{ rank }}
        retryPolicy:
          retryCount: {{ retryCount }}
          retryWindowInMinutes: {{ retryWindowInMinutes }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        Zones in which the LaunchBulkInstancesOperation is available.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: plan
      description: |
        Details of the resource plan.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
`}</CodeBlock>

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

Creates or updates LaunchBulkInstancesOperations.

```sql
REPLACE azure.compute_bulk_actions.bulk_actions
SET 
properties = '{{ properties }}',
zones = '{{ zones }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
plan = '{{ plan }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND location = '{{ location }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
plan,
properties,
systemData,
tags,
type,
zones;
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

Deletes LaunchBulkInstancesOperations.

```sql
DELETE FROM azure.compute_bulk_actions.bulk_actions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND location = '{{ location }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteInstances = '{{ deleteInstances }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_virtual_machines"
    values={[
        { label: 'list_virtual_machines', value: 'list_virtual_machines' },
        { label: 'cancel', value: 'cancel' },
        { label: 'virtual_machines_execute_deallocate', value: 'virtual_machines_execute_deallocate' },
        { label: 'virtual_machines_execute_hibernate', value: 'virtual_machines_execute_hibernate' },
        { label: 'virtual_machines_execute_start', value: 'virtual_machines_execute_start' },
        { label: 'virtual_machines_execute_create', value: 'virtual_machines_execute_create' },
        { label: 'virtual_machines_execute_delete', value: 'virtual_machines_execute_delete' },
        { label: 'virtual_machines_get_operation_status', value: 'virtual_machines_get_operation_status' },
        { label: 'virtual_machines_cancel_operations', value: 'virtual_machines_cancel_operations' }
    ]}
>
<TabItem value="list_virtual_machines">

List VirtualMachine resources of a LaunchBulkInstancesOperation.

```sql
EXEC azure.compute_bulk_actions.bulk_actions.list_virtual_machines 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="cancel">

Cancels LaunchBulkInstancesOperation instances that have not yet launched.

```sql
EXEC azure.compute_bulk_actions.bulk_actions.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="virtual_machines_execute_deallocate">

VirtualMachinesExecuteDeallocate: Execute deallocate operation for a batch of virtual machines, this operation is triggered as soon as Computeschedule receives it.

```sql
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_execute_deallocate 
@location='{{ location }}' --required, 
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
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_execute_hibernate 
@location='{{ location }}' --required, 
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
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_execute_start 
@location='{{ location }}' --required, 
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
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_execute_create 
@location='{{ location }}' --required, 
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
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_execute_delete 
@location='{{ location }}' --required, 
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
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_get_operation_status 
@location='{{ location }}' --required, 
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
EXEC azure.compute_bulk_actions.bulk_actions.virtual_machines_cancel_operations 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"operationIds": "{{ operationIds }}", 
"correlationid": "{{ correlationid }}"
}'
;
```
</TabItem>
</Tabs>
