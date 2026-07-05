--- 
title: role_assignment_schedule_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignment_schedule_requests
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

Creates, updates, deletes, gets or lists a <code>role_assignment_schedule_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_assignment_schedule_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignment_schedule_requests" /></td></tr>
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
    <td><CopyableCode code="approvalId" /></td>
    <td><code>string</code></td>
    <td>The approvalId of the role assignment schedule request.</td>
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
    <td>DateTime when role assignment schedule request was created.</td>
</tr>
<tr>
    <td><CopyableCode code="expandedProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of principal, scope and role definition.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedRoleEligibilityScheduleId" /></td>
    <td><code>string</code></td>
    <td>The linked role eligibility schedule id - to activate an eligibility.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="requestType" /></td>
    <td><code>string</code></td>
    <td>The type of the role assignment schedule request. Eg: SelfActivate, AdminAssign etc. Required. Known values are: "AdminAssign", "AdminRemove", "AdminUpdate", "AdminExtend", "AdminRenew", "SelfActivate", "SelfDeactivate", "SelfExtend", and "SelfRenew". (AdminAssign, AdminRemove, AdminUpdate, AdminExtend, AdminRenew, SelfActivate, SelfDeactivate, SelfExtend, SelfRenew)</td>
</tr>
<tr>
    <td><CopyableCode code="requestorId" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created this request.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code>object</code></td>
    <td>Schedule info of the role assignment schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment schedule request scope.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the role assignment schedule request. Known values are: "Accepted", "PendingEvaluation", "Granted", "Denied", "PendingProvisioning", "Provisioned", "PendingRevocation", "Revoked", "Canceled", "Failed", "PendingApprovalProvisioning", "PendingApproval", "FailedAsResourceIsLocked", "PendingAdminDecision", "AdminApproved", "AdminDenied", "TimedOut", "ProvisioningStarted", "Invalid", "PendingScheduleCreation", "ScheduleCreated", and "PendingExternalProvisioning". (Accepted, PendingEvaluation, Granted, Denied, PendingProvisioning, Provisioned, PendingRevocation, Revoked, Canceled, Failed, PendingApprovalProvisioning, PendingApproval, FailedAsResourceIsLocked, PendingAdminDecision, AdminApproved, AdminDenied, TimedOut, ProvisioningStarted, Invalid, PendingScheduleCreation, ScheduleCreated, PendingExternalProvisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRoleAssignmentScheduleId" /></td>
    <td><code>string</code></td>
    <td>The resultant role assignment schedule id or the role assignment schedule id being updated.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRoleAssignmentScheduleInstanceId" /></td>
    <td><code>string</code></td>
    <td>The role assignment schedule instance id being updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ticketInfo" /></td>
    <td><code>object</code></td>
    <td>Ticket Info of the role assignment.</td>
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
    <td><CopyableCode code="approvalId" /></td>
    <td><code>string</code></td>
    <td>The approvalId of the role assignment schedule request.</td>
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
    <td>DateTime when role assignment schedule request was created.</td>
</tr>
<tr>
    <td><CopyableCode code="expandedProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of principal, scope and role definition.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedRoleEligibilityScheduleId" /></td>
    <td><code>string</code></td>
    <td>The linked role eligibility schedule id - to activate an eligibility.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The principal ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The principal type of the assigned principal ID. Known values are: "User", "Group", "ServicePrincipal", "ForeignGroup", and "Device". (User, Group, ServicePrincipal, ForeignGroup, Device)</td>
</tr>
<tr>
    <td><CopyableCode code="requestType" /></td>
    <td><code>string</code></td>
    <td>The type of the role assignment schedule request. Eg: SelfActivate, AdminAssign etc. Required. Known values are: "AdminAssign", "AdminRemove", "AdminUpdate", "AdminExtend", "AdminRenew", "SelfActivate", "SelfDeactivate", "SelfExtend", and "SelfRenew". (AdminAssign, AdminRemove, AdminUpdate, AdminExtend, AdminRenew, SelfActivate, SelfDeactivate, SelfExtend, SelfRenew)</td>
</tr>
<tr>
    <td><CopyableCode code="requestorId" /></td>
    <td><code>string</code></td>
    <td>Id of the user who created this request.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code>object</code></td>
    <td>Schedule info of the role assignment schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role assignment schedule request scope.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the role assignment schedule request. Known values are: "Accepted", "PendingEvaluation", "Granted", "Denied", "PendingProvisioning", "Provisioned", "PendingRevocation", "Revoked", "Canceled", "Failed", "PendingApprovalProvisioning", "PendingApproval", "FailedAsResourceIsLocked", "PendingAdminDecision", "AdminApproved", "AdminDenied", "TimedOut", "ProvisioningStarted", "Invalid", "PendingScheduleCreation", "ScheduleCreated", and "PendingExternalProvisioning". (Accepted, PendingEvaluation, Granted, Denied, PendingProvisioning, Provisioned, PendingRevocation, Revoked, Canceled, Failed, PendingApprovalProvisioning, PendingApproval, FailedAsResourceIsLocked, PendingAdminDecision, AdminApproved, AdminDenied, TimedOut, ProvisioningStarted, Invalid, PendingScheduleCreation, ScheduleCreated, PendingExternalProvisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRoleAssignmentScheduleId" /></td>
    <td><code>string</code></td>
    <td>The resultant role assignment schedule id or the role assignment schedule id being updated.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRoleAssignmentScheduleInstanceId" /></td>
    <td><code>string</code></td>
    <td>The role assignment schedule instance id being updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ticketInfo" /></td>
    <td><code>object</code></td>
    <td>Ticket Info of the role assignment.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_schedule_request_name"><code>role_assignment_schedule_request_name</code></a></td>
    <td></td>
    <td>Get the specified role assignment schedule request.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets role assignment schedule requests for a scope.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_schedule_request_name"><code>role_assignment_schedule_request_name</code></a></td>
    <td></td>
    <td>Creates a role assignment schedule request.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_schedule_request_name"><code>role_assignment_schedule_request_name</code></a></td>
    <td></td>
    <td>Cancels a pending role assignment schedule request.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_assignment_schedule_request_name"><code>role_assignment_schedule_request_name</code></a></td>
    <td></td>
    <td>Validates a new role assignment schedule request.</td>
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
<tr id="parameter-role_assignment_schedule_request_name">
    <td><CopyableCode code="role_assignment_schedule_request_name" /></td>
    <td><code>string</code></td>
    <td>The name (guid) of the role assignment schedule request to get. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Use $filter=atScope() to return all role assignment schedule requests at or above the scope. Use $filter=principalId eq &#123;id&#125; to return all role assignment schedule requests at, above or below the scope for the specified principal. Use $filter=asRequestor() to return all role assignment schedule requests requested by the current user. Use $filter=asTarget() to return all role assignment schedule requests created for the current user. Use $filter=asApprover() to return all role assignment schedule requests where the current user is an approver. Default value is None.</td>
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

Get the specified role assignment schedule request.

```sql
SELECT
id,
name,
approvalId,
condition,
conditionVersion,
createdOn,
expandedProperties,
justification,
linkedRoleEligibilityScheduleId,
principalId,
principalType,
requestType,
requestorId,
roleDefinitionId,
scheduleInfo,
scope,
status,
systemData,
targetRoleAssignmentScheduleId,
targetRoleAssignmentScheduleInstanceId,
ticketInfo,
type
FROM azure.authorization.role_assignment_schedule_requests
WHERE scope = '{{ scope }}' -- required
AND role_assignment_schedule_request_name = '{{ role_assignment_schedule_request_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_scope">

Gets role assignment schedule requests for a scope.

```sql
SELECT
id,
name,
approvalId,
condition,
conditionVersion,
createdOn,
expandedProperties,
justification,
linkedRoleEligibilityScheduleId,
principalId,
principalType,
requestType,
requestorId,
roleDefinitionId,
scheduleInfo,
scope,
status,
systemData,
targetRoleAssignmentScheduleId,
targetRoleAssignmentScheduleInstanceId,
ticketInfo,
type
FROM azure.authorization.role_assignment_schedule_requests
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a role assignment schedule request.

```sql
INSERT INTO azure.authorization.role_assignment_schedule_requests (
properties,
scope,
role_assignment_schedule_request_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ role_assignment_schedule_request_name }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: role_assignment_schedule_requests
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the role_assignment_schedule_requests resource.
    - name: role_assignment_schedule_request_name
      value: "{{ role_assignment_schedule_request_name }}"
      description: Required parameter for the role_assignment_schedule_requests resource.
    - name: properties
      description: |
        Role assignment schedule request properties.
      value:
        scope: "{{ scope }}"
        roleDefinitionId: "{{ roleDefinitionId }}"
        principalId: "{{ principalId }}"
        principalType: "{{ principalType }}"
        requestType: "{{ requestType }}"
        status: "{{ status }}"
        approvalId: "{{ approvalId }}"
        targetRoleAssignmentScheduleId: "{{ targetRoleAssignmentScheduleId }}"
        targetRoleAssignmentScheduleInstanceId: "{{ targetRoleAssignmentScheduleInstanceId }}"
        scheduleInfo:
          startDateTime: "{{ startDateTime }}"
          expiration:
            type: "{{ type }}"
            endDateTime: "{{ endDateTime }}"
            duration: "{{ duration }}"
        linkedRoleEligibilityScheduleId: "{{ linkedRoleEligibilityScheduleId }}"
        justification: "{{ justification }}"
        ticketInfo:
          ticketNumber: "{{ ticketNumber }}"
          ticketSystem: "{{ ticketSystem }}"
        condition: "{{ condition }}"
        conditionVersion: "{{ conditionVersion }}"
        createdOn: "{{ createdOn }}"
        requestorId: "{{ requestorId }}"
        expandedProperties:
          scope:
            id: "{{ id }}"
            displayName: "{{ displayName }}"
            type: "{{ type }}"
          roleDefinition:
            id: "{{ id }}"
            displayName: "{{ displayName }}"
            type: "{{ type }}"
          principal:
            id: "{{ id }}"
            displayName: "{{ displayName }}"
            email: "{{ email }}"
            type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="cancel">

Cancels a pending role assignment schedule request.

```sql
EXEC azure.authorization.role_assignment_schedule_requests.cancel 
@scope='{{ scope }}' --required, 
@role_assignment_schedule_request_name='{{ role_assignment_schedule_request_name }}' --required
;
```
</TabItem>
<TabItem value="validate">

Validates a new role assignment schedule request.

```sql
EXEC azure.authorization.role_assignment_schedule_requests.validate 
@scope='{{ scope }}' --required, 
@role_assignment_schedule_request_name='{{ role_assignment_schedule_request_name }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
