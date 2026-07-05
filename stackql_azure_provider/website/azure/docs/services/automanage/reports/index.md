--- 
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - automanage
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.reports" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_configuration_profile_assignments', value: 'list_by_configuration_profile_assignments' }
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
    <td><CopyableCode code="configurationProfile" /></td>
    <td><code>string</code></td>
    <td>The configurationProfile linked to the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>Duration of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>End time of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error message, if any, returned by the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string</code></td>
    <td>Last modified time of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="reportFormatVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the report format.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>List of resources processed by the configuration profile assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Start time of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the configuration profile assignment.</td>
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
<TabItem value="list_by_configuration_profile_assignments">

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
    <td><CopyableCode code="configurationProfile" /></td>
    <td><code>string</code></td>
    <td>The configurationProfile linked to the assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>Duration of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string</code></td>
    <td>End time of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error message, if any, returned by the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string</code></td>
    <td>Last modified time of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="reportFormatVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the report format.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>List of resources processed by the configuration profile assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string</code></td>
    <td>Start time of the configuration profile assignment processing.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the configuration profile assignment.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-configuration_profile_assignment_name"><code>configuration_profile_assignment_name</code></a>, <a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get information about a report associated with a configuration profile assignment run.</td>
</tr>
<tr>
    <td><a href="#list_by_configuration_profile_assignments"><CopyableCode code="list_by_configuration_profile_assignments" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-configuration_profile_assignment_name"><code>configuration_profile_assignment_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a list of reports within a given configuration profile assignment.</td>
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
<tr id="parameter-configuration_profile_assignment_name">
    <td><CopyableCode code="configuration_profile_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The configuration profile assignment name. Required.</td>
</tr>
<tr id="parameter-report_name">
    <td><CopyableCode code="report_name" /></td>
    <td><code>string</code></td>
    <td>The report name. Required.</td>
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
        { label: 'list_by_configuration_profile_assignments', value: 'list_by_configuration_profile_assignments' }
    ]}
>
<TabItem value="get">

Get information about a report associated with a configuration profile assignment run.

```sql
SELECT
id,
name,
configurationProfile,
duration,
endTime,
error,
lastModifiedTime,
reportFormatVersion,
resources,
startTime,
status,
systemData,
type
FROM azure.automanage.reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND configuration_profile_assignment_name = '{{ configuration_profile_assignment_name }}' -- required
AND report_name = '{{ report_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_configuration_profile_assignments">

Retrieve a list of reports within a given configuration profile assignment.

```sql
SELECT
id,
name,
configurationProfile,
duration,
endTime,
error,
lastModifiedTime,
reportFormatVersion,
resources,
startTime,
status,
systemData,
type
FROM azure.automanage.reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND configuration_profile_assignment_name = '{{ configuration_profile_assignment_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
