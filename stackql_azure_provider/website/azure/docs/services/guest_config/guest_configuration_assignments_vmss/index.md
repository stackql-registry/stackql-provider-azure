--- 
title: guest_configuration_assignments_vmss
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_configuration_assignments_vmss
  - guest_config
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

Creates, updates, deletes, gets or lists a <code>guest_configuration_assignments_vmss</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="guest_configuration_assignments_vmss" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guest_config.guest_configuration_assignments_vmss" /></td></tr>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmss_name"><code>vmss_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get information about a guest configuration assignment for VMSS.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmss_name"><code>vmss_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all guest configuration assignments for VMSS.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vmss_name"><code>vmss_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a guest configuration assignment for VMSS.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The guest configuration assignment name. Required.</td>
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
<tr id="parameter-vmss_name">
    <td><CopyableCode code="vmss_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine scale set. Required.</td>
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

Get information about a guest configuration assignment for VMSS.

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
FROM azure.guest_config.guest_configuration_assignments_vmss
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vmss_name = '{{ vmss_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all guest configuration assignments for VMSS.

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
FROM azure.guest_config.guest_configuration_assignments_vmss
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vmss_name = '{{ vmss_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
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

Delete a guest configuration assignment for VMSS.

```sql
DELETE FROM azure.guest_config.guest_configuration_assignments_vmss
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vmss_name = '{{ vmss_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
