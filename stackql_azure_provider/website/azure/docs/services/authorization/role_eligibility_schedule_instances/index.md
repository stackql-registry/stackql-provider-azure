--- 
title: role_eligibility_schedule_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - role_eligibility_schedule_instances
  - authorization
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

Creates, updates, deletes, gets or lists a <code>role_eligibility_schedule_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_eligibility_schedule_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_eligibility_schedule_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when role eligibility schedule was created.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The endDateTime of the role eligibility schedule instance.</td>
</tr>
<tr>
    <td><CopyableCode code="expandedProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of principal, scope and role definition.</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code>string</code></td>
    <td>Membership type of the role eligibility schedule. Known values are: "Inherited", "Direct", and "Group". (Inherited, Direct, Group)</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="roleEligibilityScheduleId" /></td>
    <td><code>string</code></td>
    <td>Id of the master role eligibility schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role eligibility schedule scope.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The startDateTime of the role eligibility schedule instance.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the role eligibility schedule instance. Known values are: "Accepted", "PendingEvaluation", "Granted", "Denied", "PendingProvisioning", "Provisioned", "PendingRevocation", "Revoked", "Canceled", "Failed", "PendingApprovalProvisioning", "PendingApproval", "FailedAsResourceIsLocked", "PendingAdminDecision", "AdminApproved", "AdminDenied", "TimedOut", "ProvisioningStarted", "Invalid", "PendingScheduleCreation", "ScheduleCreated", and "PendingExternalProvisioning". (Accepted, PendingEvaluation, Granted, Denied, PendingProvisioning, Provisioned, PendingRevocation, Revoked, Canceled, Failed, PendingApprovalProvisioning, PendingApproval, FailedAsResourceIsLocked, PendingAdminDecision, AdminApproved, AdminDenied, TimedOut, ProvisioningStarted, Invalid, PendingScheduleCreation, ScheduleCreated, PendingExternalProvisioning)</td>
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
<TabItem value="list_for_scope">

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
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td>The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the condition. Currently accepted value is '2.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when role eligibility schedule was created.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The endDateTime of the role eligibility schedule instance.</td>
</tr>
<tr>
    <td><CopyableCode code="expandedProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of principal, scope and role definition.</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code>string</code></td>
    <td>Membership type of the role eligibility schedule. Known values are: "Inherited", "Direct", and "Group". (Inherited, Direct, Group)</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID.</td>
</tr>
<tr>
    <td><CopyableCode code="roleEligibilityScheduleId" /></td>
    <td><code>string</code></td>
    <td>Id of the master role eligibility schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role eligibility schedule scope.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The startDateTime of the role eligibility schedule instance.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the role eligibility schedule instance. Known values are: "Accepted", "PendingEvaluation", "Granted", "Denied", "PendingProvisioning", "Provisioned", "PendingRevocation", "Revoked", "Canceled", "Failed", "PendingApprovalProvisioning", "PendingApproval", "FailedAsResourceIsLocked", "PendingAdminDecision", "AdminApproved", "AdminDenied", "TimedOut", "ProvisioningStarted", "Invalid", "PendingScheduleCreation", "ScheduleCreated", and "PendingExternalProvisioning". (Accepted, PendingEvaluation, Granted, Denied, PendingProvisioning, Provisioned, PendingRevocation, Revoked, Canceled, Failed, PendingApprovalProvisioning, PendingApproval, FailedAsResourceIsLocked, PendingAdminDecision, AdminApproved, AdminDenied, TimedOut, ProvisioningStarted, Invalid, PendingScheduleCreation, ScheduleCreated, PendingExternalProvisioning)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_eligibility_schedule_instance_name"><code>role_eligibility_schedule_instance_name</code></a></td>
    <td></td>
    <td>Gets the specified role eligibility schedule instance.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets role eligibility schedule instances of a role eligibility schedule.</td>
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
<tr id="parameter-role_eligibility_schedule_instance_name">
    <td><CopyableCode code="role_eligibility_schedule_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name (hash of schedule name + time) of the role eligibility schedule to get. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Use $filter=atScope() to return all role assignment schedules at or above the scope. Use $filter=principalId eq &#123;id&#125; to return all role assignment schedules at, above or below the scope for the specified principal. Use $filter=assignedTo('&#123;userId&#125;') to return all role eligibility schedules for the user. Use $filter=asTarget() to return all role eligibility schedules created for the current user. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
    ]}
>
<TabItem value="get">

Gets the specified role eligibility schedule instance.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdOn,
endDateTime,
expandedProperties,
memberType,
principalId,
principalType,
roleDefinitionId,
roleEligibilityScheduleId,
scope,
startDateTime,
status,
systemData,
type
FROM azure.authorization.role_eligibility_schedule_instances
WHERE scope = '{{ scope }}' -- required
AND role_eligibility_schedule_instance_name = '{{ role_eligibility_schedule_instance_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_scope">

Gets role eligibility schedule instances of a role eligibility schedule.

```sql
SELECT
id,
name,
condition,
conditionVersion,
createdOn,
endDateTime,
expandedProperties,
memberType,
principalId,
principalType,
roleDefinitionId,
roleEligibilityScheduleId,
scope,
startDateTime,
status,
systemData,
type
FROM azure.authorization.role_eligibility_schedule_instances
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
