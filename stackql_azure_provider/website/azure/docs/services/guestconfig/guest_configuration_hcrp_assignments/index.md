--- 
title: guest_configuration_hcrp_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_configuration_hcrp_assignments
  - guestconfig
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

Creates, updates, deletes, gets or lists a <code>guest_configuration_hcrp_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="guest_configuration_hcrp_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guestconfig.guest_configuration_hcrp_assignments" /></td></tr>
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
    <td>ARM resource id of the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentHash" /></td>
    <td><code>string</code></td>
    <td>Combined hash of the configuration package and parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating compliance status of the machine for the assigned guest configuration. Known values are: "Compliant", "NonCompliant", and "Pending".</td>
</tr>
<tr>
    <td><CopyableCode code="context" /></td>
    <td><code>string</code></td>
    <td>The source which initiated the guest configuration assignment. Ex: Azure Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="guestConfiguration" /></td>
    <td><code>object</code></td>
    <td>The guest configuration to assign.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStatusChecked" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when last compliance status was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="latestAssignmentReport" /></td>
    <td><code>object</code></td>
    <td>Last reported guest configuration assignment report.</td>
</tr>
<tr>
    <td><CopyableCode code="latestReportId" /></td>
    <td><code>string</code></td>
    <td>Id of the latest report for the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region where the VM is located.</td>
</tr>
<tr>
    <td><CopyableCode code="parameterHash" /></td>
    <td><code>string</code></td>
    <td>parameter hash for the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Succeeded", "Failed", "Canceled", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Type of the resource - VMSS / VM.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>VM resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssVMList" /></td>
    <td><code>array</code></td>
    <td>The list of VM Compliance data for VMSS.</td>
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
    <td>ARM resource id of the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentHash" /></td>
    <td><code>string</code></td>
    <td>Combined hash of the configuration package and parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating compliance status of the machine for the assigned guest configuration. Known values are: "Compliant", "NonCompliant", and "Pending".</td>
</tr>
<tr>
    <td><CopyableCode code="context" /></td>
    <td><code>string</code></td>
    <td>The source which initiated the guest configuration assignment. Ex: Azure Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="guestConfiguration" /></td>
    <td><code>object</code></td>
    <td>The guest configuration to assign.</td>
</tr>
<tr>
    <td><CopyableCode code="lastComplianceStatusChecked" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when last compliance status was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="latestAssignmentReport" /></td>
    <td><code>object</code></td>
    <td>Last reported guest configuration assignment report.</td>
</tr>
<tr>
    <td><CopyableCode code="latestReportId" /></td>
    <td><code>string</code></td>
    <td>Id of the latest report for the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Region where the VM is located.</td>
</tr>
<tr>
    <td><CopyableCode code="parameterHash" /></td>
    <td><code>string</code></td>
    <td>parameter hash for the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Succeeded", "Failed", "Canceled", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Type of the resource - VMSS / VM.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>VM resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssVMList" /></td>
    <td><code>array</code></td>
    <td>The list of VM Compliance data for VMSS.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-guest_configuration_assignment_name"><code>guest_configuration_assignment_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get information about a guest configuration assignment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all guest configuration assignments for an ARC machine.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-guest_configuration_assignment_name"><code>guest_configuration_assignment_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an association between a ARC machine and guest configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-guest_configuration_assignment_name"><code>guest_configuration_assignment_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an association between a ARC machine and guest configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-guest_configuration_assignment_name"><code>guest_configuration_assignment_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a guest configuration assignment.</td>
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
<tr id="parameter-guest_configuration_assignment_name">
    <td><CopyableCode code="guest_configuration_assignment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the guest configuration assignment. Required.</td>
</tr>
<tr id="parameter-machine_name">
    <td><CopyableCode code="machine_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ARC machine. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
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

Get information about a guest configuration assignment.

```sql
SELECT
id,
name,
assignmentHash,
complianceStatus,
context,
guestConfiguration,
lastComplianceStatusChecked,
latestAssignmentReport,
latestReportId,
location,
parameterHash,
provisioningState,
resourceType,
systemData,
targetResourceId,
type,
vmssVMList
FROM azure.guestconfig.guest_configuration_hcrp_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND guest_configuration_assignment_name = '{{ guest_configuration_assignment_name }}' -- required
AND machine_name = '{{ machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all guest configuration assignments for an ARC machine.

```sql
SELECT
id,
name,
assignmentHash,
complianceStatus,
context,
guestConfiguration,
lastComplianceStatusChecked,
latestAssignmentReport,
latestReportId,
location,
parameterHash,
provisioningState,
resourceType,
systemData,
targetResourceId,
type,
vmssVMList
FROM azure.guestconfig.guest_configuration_hcrp_assignments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND machine_name = '{{ machine_name }}' -- required
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

Creates an association between a ARC machine and guest configuration.

```sql
INSERT INTO azure.guestconfig.guest_configuration_hcrp_assignments (
name,
location,
properties,
guest_configuration_assignment_name,
resource_group_name,
machine_name,
subscription_id
)
SELECT 
'{{ name }}',
'{{ location }}',
'{{ properties }}',
'{{ guest_configuration_assignment_name }}',
'{{ resource_group_name }}',
'{{ machine_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: guest_configuration_hcrp_assignments
  props:
    - name: guest_configuration_assignment_name
      value: "{{ guest_configuration_assignment_name }}"
      description: Required parameter for the guest_configuration_hcrp_assignments resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the guest_configuration_hcrp_assignments resource.
    - name: machine_name
      value: "{{ machine_name }}"
      description: Required parameter for the guest_configuration_hcrp_assignments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the guest_configuration_hcrp_assignments resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the guest configuration assignment.
    - name: location
      value: "{{ location }}"
      description: |
        Region where the VM is located.
    - name: properties
      description: |
        Properties of the Guest configuration assignment.
      value:
        targetResourceId: "{{ targetResourceId }}"
        guestConfiguration:
          kind: "{{ kind }}"
          name: "{{ name }}"
          version: "{{ version }}"
          contentUri: "{{ contentUri }}"
          contentHash: "{{ contentHash }}"
          assignmentType: "{{ assignmentType }}"
          assignmentSource: "{{ assignmentSource }}"
          contentType: "{{ contentType }}"
          configurationParameter:
            - name: "{{ name }}"
              value: "{{ value }}"
          configurationProtectedParameter:
            - name: "{{ name }}"
              value: "{{ value }}"
          configurationSetting:
            configurationMode: "{{ configurationMode }}"
            allowModuleOverwrite: {{ allowModuleOverwrite }}
            actionAfterReboot: "{{ actionAfterReboot }}"
            refreshFrequencyMins: {{ refreshFrequencyMins }}
            rebootIfNeeded: {{ rebootIfNeeded }}
            configurationModeFrequencyMins: {{ configurationModeFrequencyMins }}
        complianceStatus: "{{ complianceStatus }}"
        lastComplianceStatusChecked: "{{ lastComplianceStatusChecked }}"
        latestReportId: "{{ latestReportId }}"
        parameterHash: "{{ parameterHash }}"
        latestAssignmentReport:
          id: "{{ id }}"
          reportId: "{{ reportId }}"
          assignment:
            name: "{{ name }}"
            configuration:
              name: "{{ name }}"
              version: "{{ version }}"
          vm:
            id: "{{ id }}"
            uuid: "{{ uuid }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
          complianceStatus: "{{ complianceStatus }}"
          operationType: "{{ operationType }}"
          resources:
            - complianceStatus: "{{ complianceStatus }}"
              resourceId: "{{ resourceId }}"
              reasons: "{{ reasons }}"
              properties: "{{ properties }}"
        context: "{{ context }}"
        assignmentHash: "{{ assignmentHash }}"
        provisioningState: "{{ provisioningState }}"
        resourceType: "{{ resourceType }}"
        vmssVMList:
          - vmId: "{{ vmId }}"
            vmResourceId: "{{ vmResourceId }}"
            complianceStatus: "{{ complianceStatus }}"
            latestReportId: "{{ latestReportId }}"
            lastComplianceChecked: "{{ lastComplianceChecked }}"
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

Creates an association between a ARC machine and guest configuration.

```sql
REPLACE azure.guestconfig.guest_configuration_hcrp_assignments
SET 
name = '{{ name }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
guest_configuration_assignment_name = '{{ guest_configuration_assignment_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
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

Delete a guest configuration assignment.

```sql
DELETE FROM azure.guestconfig.guest_configuration_hcrp_assignments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND guest_configuration_assignment_name = '{{ guest_configuration_assignment_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
