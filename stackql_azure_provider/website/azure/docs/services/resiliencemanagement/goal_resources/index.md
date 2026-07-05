--- 
title: goal_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - goal_resources
  - resiliencemanagement
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

Creates, updates, deletes, gets or lists a <code>goal_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="goal_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resiliencemanagement.goal_resources" /></td></tr>
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
    <td><CopyableCode code="disasterRecoveryAttestationStatus" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is manually attested for disaster recovery recommendation. Known values are: "NotAttested" and "ManuallyAttested". (NotAttested, ManuallyAttested)</td>
</tr>
<tr>
    <td><CopyableCode code="disasterRecoveryGoalParticipation" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is excluded for disaster recovery recommendation. Known values are: "Excluded" and "Included". (Excluded, Included)</td>
</tr>
<tr>
    <td><CopyableCode code="exclusionReasonForDisasterRecoveryGoals" /></td>
    <td><code>string</code></td>
    <td>Reason for exclusion from disaster recovery goals. Known values are: "UserSelectedExclusion", "FailedOverResource", and "UnsupportedResource". (UserSelectedExclusion, FailedOverResource, UnsupportedResource)</td>
</tr>
<tr>
    <td><CopyableCode code="exclusionReasonForHighAvailabilityGoals" /></td>
    <td><code>string</code></td>
    <td>Reason for exclusion from high availability goals. Known values are: "UserSelectedExclusion", "FailedOverResource", and "UnsupportedResource". (UserSelectedExclusion, FailedOverResource, UnsupportedResource)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityAttestationStatus" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is manually attested for high availability recommendation. Required. Known values are: "NotAttested" and "ManuallyAttested". (NotAttested, ManuallyAttested)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityGoalParticipation" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is excluded for high availability recommendation. Required. Known values are: "Excluded" and "Included". (Excluded, Included)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceArmId" /></td>
    <td><code>string</code></td>
    <td>Arm Id of resource under the SG for which the extension resource is maintained. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGroupMemberships" /></td>
    <td><code>array</code></td>
    <td>List of service groups of which this resource is memberof.</td>
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
    <td><CopyableCode code="userConfirmationForHighAvailability" /></td>
    <td><code>array</code></td>
    <td>List of user confirmations for high availability solutions.</td>
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
    <td><CopyableCode code="disasterRecoveryAttestationStatus" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is manually attested for disaster recovery recommendation. Known values are: "NotAttested" and "ManuallyAttested". (NotAttested, ManuallyAttested)</td>
</tr>
<tr>
    <td><CopyableCode code="disasterRecoveryGoalParticipation" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is excluded for disaster recovery recommendation. Known values are: "Excluded" and "Included". (Excluded, Included)</td>
</tr>
<tr>
    <td><CopyableCode code="exclusionReasonForDisasterRecoveryGoals" /></td>
    <td><code>string</code></td>
    <td>Reason for exclusion from disaster recovery goals. Known values are: "UserSelectedExclusion", "FailedOverResource", and "UnsupportedResource". (UserSelectedExclusion, FailedOverResource, UnsupportedResource)</td>
</tr>
<tr>
    <td><CopyableCode code="exclusionReasonForHighAvailabilityGoals" /></td>
    <td><code>string</code></td>
    <td>Reason for exclusion from high availability goals. Known values are: "UserSelectedExclusion", "FailedOverResource", and "UnsupportedResource". (UserSelectedExclusion, FailedOverResource, UnsupportedResource)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityAttestationStatus" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is manually attested for high availability recommendation. Required. Known values are: "NotAttested" and "ManuallyAttested". (NotAttested, ManuallyAttested)</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityGoalParticipation" /></td>
    <td><code>string</code></td>
    <td>Flag which depicts whether the Arm resource is excluded for high availability recommendation. Required. Known values are: "Excluded" and "Included". (Excluded, Included)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceArmId" /></td>
    <td><code>string</code></td>
    <td>Arm Id of resource under the SG for which the extension resource is maintained. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceGroupMemberships" /></td>
    <td><code>array</code></td>
    <td>List of service groups of which this resource is memberof.</td>
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
    <td><CopyableCode code="userConfirmationForHighAvailability" /></td>
    <td><code>array</code></td>
    <td>List of user confirmations for high availability solutions.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a>, <a href="#parameter-goal_resource_name"><code>goal_resource_name</code></a></td>
    <td></td>
    <td>Get a GoalResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List GoalResource resources by GoalAssignment.</td>
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
<tr id="parameter-goal_assignment_name">
    <td><CopyableCode code="goal_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the GoalAssignment. Required.</td>
</tr>
<tr id="parameter-goal_resource_name">
    <td><CopyableCode code="goal_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the GoalAssignment. Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip over when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Default value is None.</td>
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

Get a GoalResource.

```sql
SELECT
id,
name,
disasterRecoveryAttestationStatus,
disasterRecoveryGoalParticipation,
exclusionReasonForDisasterRecoveryGoals,
exclusionReasonForHighAvailabilityGoals,
highAvailabilityAttestationStatus,
highAvailabilityGoalParticipation,
provisioningState,
resourceArmId,
serviceGroupMemberships,
systemData,
type,
userConfirmationForHighAvailability
FROM azure.resiliencemanagement.goal_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND goal_assignment_name = '{{ goal_assignment_name }}' -- required
AND goal_resource_name = '{{ goal_resource_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List GoalResource resources by GoalAssignment.

```sql
SELECT
id,
name,
disasterRecoveryAttestationStatus,
disasterRecoveryGoalParticipation,
exclusionReasonForDisasterRecoveryGoals,
exclusionReasonForHighAvailabilityGoals,
highAvailabilityAttestationStatus,
highAvailabilityGoalParticipation,
provisioningState,
resourceArmId,
serviceGroupMemberships,
systemData,
type,
userConfirmationForHighAvailability
FROM azure.resiliencemanagement.goal_resources
WHERE service_group_name = '{{ service_group_name }}' -- required
AND goal_assignment_name = '{{ goal_assignment_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>
