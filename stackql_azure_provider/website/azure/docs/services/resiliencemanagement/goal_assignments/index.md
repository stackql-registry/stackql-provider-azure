--- 
title: goal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - goal_assignments
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

Creates, updates, deletes, gets or lists a <code>goal_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="goal_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resiliencemanagement.goal_assignments" /></td></tr>
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
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors encountered during the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="goalAssignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of goal assignment. Required. "Resiliency" (Resiliency)</td>
</tr>
<tr>
    <td><CopyableCode code="goalTemplateId" /></td>
    <td><code>string</code></td>
    <td>Arm id of the goal template. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevelResources" /></td>
    <td><code>array</code></td>
    <td>List of service level resources.</td>
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
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Details of any errors encountered during the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="goalAssignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of goal assignment. Required. "Resiliency" (Resiliency)</td>
</tr>
<tr>
    <td><CopyableCode code="goalTemplateId" /></td>
    <td><code>string</code></td>
    <td>Arm id of the goal template. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevelResources" /></td>
    <td><code>array</code></td>
    <td>List of service level resources.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td></td>
    <td>Get a GoalAssignment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List GoalAssignment resources by tenant.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td></td>
    <td>Create a GoalAssignment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td></td>
    <td>Update a GoalAssignment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td></td>
    <td>Create a GoalAssignment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td></td>
    <td>Delete a GoalAssignment.</td>
</tr>
<tr>
    <td><a href="#update_goal_resources"><CopyableCode code="update_goal_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a>, <a href="#parameter-resources"><code>resources</code></a></td>
    <td></td>
    <td>Action to exclude a resource from goal assignment.</td>
</tr>
<tr>
    <td><a href="#refresh_goal_resources"><CopyableCode code="refresh_goal_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a></td>
    <td></td>
    <td>Refreshes the goal resources under a goal assignment. This operation scans for new resources under the scope of the assignment.</td>
</tr>
<tr>
    <td><a href="#recommend_capacity"><CopyableCode code="recommend_capacity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-goal_assignment_name"><code>goal_assignment_name</code></a>, <a href="#parameter-resourceIds"><code>resourceIds</code></a></td>
    <td></td>
    <td>Recommends capacity improvements for resources under the goal assignments scope. Returns AI-powered capacity assessments and recommendations.</td>
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

Get a GoalAssignment.

```sql
SELECT
id,
name,
errorDetails,
goalAssignmentType,
goalTemplateId,
provisioningState,
serviceLevelResources,
systemData,
type
FROM azure.resiliencemanagement.goal_assignments
WHERE service_group_name = '{{ service_group_name }}' -- required
AND goal_assignment_name = '{{ goal_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List GoalAssignment resources by tenant.

```sql
SELECT
id,
name,
errorDetails,
goalAssignmentType,
goalTemplateId,
provisioningState,
serviceLevelResources,
systemData,
type
FROM azure.resiliencemanagement.goal_assignments
WHERE service_group_name = '{{ service_group_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
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

Create a GoalAssignment.

```sql
INSERT INTO azure.resiliencemanagement.goal_assignments (
properties,
service_group_name,
goal_assignment_name
)
SELECT 
'{{ properties }}',
'{{ service_group_name }}',
'{{ goal_assignment_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: goal_assignments
  props:
    - name: service_group_name
      value: "{{ service_group_name }}"
      description: Required parameter for the goal_assignments resource.
    - name: goal_assignment_name
      value: "{{ goal_assignment_name }}"
      description: Required parameter for the goal_assignments resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        goalTemplateId: "{{ goalTemplateId }}"
        goalAssignmentType: "{{ goalAssignmentType }}"
        serviceLevelResources:
          - serviceLevelIndicatorResourceId: "{{ serviceLevelIndicatorResourceId }}"
            serviceLevelObjectiveResourceId: "{{ serviceLevelObjectiveResourceId }}"
        provisioningState: "{{ provisioningState }}"
        errorDetails:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
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

Update a GoalAssignment.

```sql
UPDATE azure.resiliencemanagement.goal_assignments
SET 
properties = '{{ properties }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND goal_assignment_name = '{{ goal_assignment_name }}' --required;
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

Create a GoalAssignment.

```sql
REPLACE azure.resiliencemanagement.goal_assignments
SET 
properties = '{{ properties }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND goal_assignment_name = '{{ goal_assignment_name }}' --required;
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

Delete a GoalAssignment.

```sql
DELETE FROM azure.resiliencemanagement.goal_assignments
WHERE service_group_name = '{{ service_group_name }}' --required
AND goal_assignment_name = '{{ goal_assignment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_goal_resources"
    values={[
        { label: 'update_goal_resources', value: 'update_goal_resources' },
        { label: 'refresh_goal_resources', value: 'refresh_goal_resources' },
        { label: 'recommend_capacity', value: 'recommend_capacity' }
    ]}
>
<TabItem value="update_goal_resources">

Action to exclude a resource from goal assignment.

```sql
EXEC azure.resiliencemanagement.goal_assignments.update_goal_resources 
@service_group_name='{{ service_group_name }}' --required, 
@goal_assignment_name='{{ goal_assignment_name }}' --required 
@@json=
'{
"resources": "{{ resources }}"
}'
;
```
</TabItem>
<TabItem value="refresh_goal_resources">

Refreshes the goal resources under a goal assignment. This operation scans for new resources under the scope of the assignment.

```sql
EXEC azure.resiliencemanagement.goal_assignments.refresh_goal_resources 
@service_group_name='{{ service_group_name }}' --required, 
@goal_assignment_name='{{ goal_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="recommend_capacity">

Recommends capacity improvements for resources under the goal assignments scope. Returns AI-powered capacity assessments and recommendations.

```sql
EXEC azure.resiliencemanagement.goal_assignments.recommend_capacity 
@service_group_name='{{ service_group_name }}' --required, 
@goal_assignment_name='{{ goal_assignment_name }}' --required 
@@json=
'{
"resourceIds": "{{ resourceIds }}"
}'
;
```
</TabItem>
</Tabs>
