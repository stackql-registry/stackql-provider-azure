--- 
title: groups_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_operations
  - migration_assessment
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

Creates, updates, deletes, gets or lists a <code>groups_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migration_assessment.groups_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_assessment_project', value: 'list_by_assessment_project' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="areAssessmentsRunning" /></td>
    <td><code>boolean</code></td>
    <td>If the assessments are in running state.</td>
</tr>
<tr>
    <td><CopyableCode code="assessments" /></td>
    <td><code>array</code></td>
    <td>List of References to Assessments created on this group.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this group was created. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="groupStatus" /></td>
    <td><code>string</code></td>
    <td>Whether the group has been created and is valid. Known values are: "Created", "Updated", "Running", "Completed", and "Invalid".</td>
</tr>
<tr>
    <td><CopyableCode code="groupType" /></td>
    <td><code>string</code></td>
    <td>The type of group. Known values are: "Default", "Import", and "Import".</td>
</tr>
<tr>
    <td><CopyableCode code="machineCount" /></td>
    <td><code>integer</code></td>
    <td>Number of machines part of this group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAssessmentTypes" /></td>
    <td><code>array</code></td>
    <td>List of assessment types supported on this group.</td>
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
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this group was last updated. Date-Time represented in ISO-8601 format.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_assessment_project">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="areAssessmentsRunning" /></td>
    <td><code>boolean</code></td>
    <td>If the assessments are in running state.</td>
</tr>
<tr>
    <td><CopyableCode code="assessments" /></td>
    <td><code>array</code></td>
    <td>List of References to Assessments created on this group.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this group was created. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="groupStatus" /></td>
    <td><code>string</code></td>
    <td>Whether the group has been created and is valid. Known values are: "Created", "Updated", "Running", "Completed", and "Invalid".</td>
</tr>
<tr>
    <td><CopyableCode code="groupType" /></td>
    <td><code>string</code></td>
    <td>The type of group. Known values are: "Default", "Import", and "Import".</td>
</tr>
<tr>
    <td><CopyableCode code="machineCount" /></td>
    <td><code>integer</code></td>
    <td>Number of machines part of this group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAssessmentTypes" /></td>
    <td><code>array</code></td>
    <td>List of assessment types supported on this group.</td>
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
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this group was last updated. Date-Time represented in ISO-8601 format.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Group.</td>
</tr>
<tr>
    <td><a href="#list_by_assessment_project"><CopyableCode code="list_by_assessment_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Group resources by AssessmentProject.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Group.</td>
</tr>
<tr>
    <td><a href="#update_machines"><CopyableCode code="update_machines" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update machines in group. Update machines in group by adding or removing machines.</td>
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
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Group ARM name. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Assessment Project Name. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_assessment_project', value: 'list_by_assessment_project' }
    ]}
>
<TabItem value="get">

Get a Group.

```sql
SELECT
id,
name,
areAssessmentsRunning,
assessments,
createdTimestamp,
groupStatus,
groupType,
machineCount,
provisioningState,
supportedAssessmentTypes,
systemData,
type,
updatedTimestamp
FROM azure.migration_assessment.groups_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_assessment_project">

List Group resources by AssessmentProject.

```sql
SELECT
id,
name,
areAssessmentsRunning,
assessments,
createdTimestamp,
groupStatus,
groupType,
machineCount,
provisioningState,
supportedAssessmentTypes,
systemData,
type,
updatedTimestamp
FROM azure.migration_assessment.groups_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a Group.

```sql
INSERT INTO azure.migration_assessment.groups_operations (
properties,
resource_group_name,
project_name,
group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ project_name }}',
'{{ group_name }}',
'{{ subscription_id }}'
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
- name: groups_operations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the groups_operations resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the groups_operations resource.
    - name: group_name
      value: "{{ group_name }}"
      description: Required parameter for the groups_operations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the groups_operations resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        groupStatus: "{{ groupStatus }}"
        machineCount: {{ machineCount }}
        assessments:
          - "{{ assessments }}"
        supportedAssessmentTypes:
          - "{{ supportedAssessmentTypes }}"
        areAssessmentsRunning: {{ areAssessmentsRunning }}
        createdTimestamp: "{{ createdTimestamp }}"
        updatedTimestamp: "{{ updatedTimestamp }}"
        groupType: "{{ groupType }}"
`}</CodeBlock>

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

Delete a Group.

```sql
DELETE FROM azure.migration_assessment.groups_operations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND group_name = '{{ group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_machines"
    values={[
        { label: 'update_machines', value: 'update_machines' }
    ]}
>
<TabItem value="update_machines">

Update machines in group. Update machines in group by adding or removing machines.

```sql
EXEC azure.migration_assessment.groups_operations.update_machines 
@resource_group_name='{{ resource_group_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@group_name='{{ group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"eTag": "{{ eTag }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
