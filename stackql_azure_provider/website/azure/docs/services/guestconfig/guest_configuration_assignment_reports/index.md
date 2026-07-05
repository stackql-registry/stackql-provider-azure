--- 
title: guest_configuration_assignment_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_configuration_assignment_reports
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

Creates, updates, deletes, gets or lists a <code>guest_configuration_assignment_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="guest_configuration_assignment_reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guestconfig.guest_configuration_assignment_reports" /></td></tr>
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
    <td>ARM resource id of the report for the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>GUID that identifies the guest configuration assignment report under a subscription, resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="assignment" /></td>
    <td><code>object</code></td>
    <td>Configuration details of the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating compliance status of the machine for the assigned guest configuration. Known values are: "Compliant", "NonCompliant", and "Pending".</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Details of the assignment report.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date and time of the guest configuration assignment compliance status check.</td>
</tr>
<tr>
    <td><CopyableCode code="reportId" /></td>
    <td><code>string</code></td>
    <td>GUID that identifies the guest configuration assignment report under a subscription, resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date and time of the guest configuration assignment compliance status check.</td>
</tr>
<tr>
    <td><CopyableCode code="vm" /></td>
    <td><code>object</code></td>
    <td>Information about the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource Id of the VMSS.</td>
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
    <td>ARM resource id of the report for the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>GUID that identifies the guest configuration assignment report under a subscription, resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="assignment" /></td>
    <td><code>object</code></td>
    <td>Configuration details of the guest configuration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating compliance status of the machine for the assigned guest configuration. Known values are: "Compliant", "NonCompliant", and "Pending".</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Details of the assignment report.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date and time of the guest configuration assignment compliance status check.</td>
</tr>
<tr>
    <td><CopyableCode code="reportId" /></td>
    <td><code>string</code></td>
    <td>GUID that identifies the guest configuration assignment report under a subscription, resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date and time of the guest configuration assignment compliance status check.</td>
</tr>
<tr>
    <td><CopyableCode code="vm" /></td>
    <td><code>object</code></td>
    <td>Information about the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssResourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource Id of the VMSS.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-guest_configuration_assignment_name"><code>guest_configuration_assignment_name</code></a>, <a href="#parameter-report_id"><code>report_id</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a report for the guest configuration assignment, by reportId.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-guest_configuration_assignment_name"><code>guest_configuration_assignment_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all reports for the guest configuration assignment, latest report first.</td>
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
    <td>The guest configuration assignment name. Required.</td>
</tr>
<tr id="parameter-report_id">
    <td><CopyableCode code="report_id" /></td>
    <td><code>string</code></td>
    <td>The GUID for the guest configuration assignment report. Required.</td>
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
<tr id="parameter-vm_name">
    <td><CopyableCode code="vm_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine. Required.</td>
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

Get a report for the guest configuration assignment, by reportId.

```sql
SELECT
id,
name,
assignment,
complianceStatus,
details,
endTime,
reportId,
startTime,
vm,
vmssResourceId
FROM azure.guestconfig.guest_configuration_assignment_reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND guest_configuration_assignment_name = '{{ guest_configuration_assignment_name }}' -- required
AND report_id = '{{ report_id }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all reports for the guest configuration assignment, latest report first.

```sql
SELECT
id,
name,
assignment,
complianceStatus,
details,
endTime,
reportId,
startTime,
vm,
vmssResourceId
FROM azure.guestconfig.guest_configuration_assignment_reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND guest_configuration_assignment_name = '{{ guest_configuration_assignment_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
