--- 
title: machines_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_operations
  - migrationassessment
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

Creates, updates, deletes, gets or lists a <code>machines_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="machines_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrationassessment.machines_operations" /></td></tr>
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
    <td><CopyableCode code="bootType" /></td>
    <td><code>string</code></td>
    <td>Boot type of machine discovered in private data center. Known values are: "Unknown", "EFI", "BIOS", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine first created.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerArmId" /></td>
    <td><code>string</code></td>
    <td>The data center management server ARM Id for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerName" /></td>
    <td><code>string</code></td>
    <td>The data center management server name for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryMachineArmId" /></td>
    <td><code>string</code></td>
    <td>Site id of machine discovered in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>object</code></td>
    <td>Disks attached to the machine discovered in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name of the Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>List of errors for this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="groups" /></td>
    <td><code>array</code></td>
    <td>Gets the References to the groups that this machine is member of.</td>
</tr>
<tr>
    <td><CopyableCode code="hostProcessor" /></td>
    <td><code>object</code></td>
    <td>Gets Processor details of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="megabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Megabytes of memory found allocated for the machine in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAdapters" /></td>
    <td><code>object</code></td>
    <td>Network adapters attached to the machine discovered in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores found on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemName" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemType" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="productSupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the product support status related details.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlInstances" /></td>
    <td><code>array</code></td>
    <td>SQL instances discovered on the machine.</td>
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
    <td>When was machine last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplications" /></td>
    <td><code>array</code></td>
    <td>Web applications discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadSummary" /></td>
    <td><code>object</code></td>
    <td>Gets or sets workload summary.</td>
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
    <td><CopyableCode code="bootType" /></td>
    <td><code>string</code></td>
    <td>Boot type of machine discovered in private data center. Known values are: "Unknown", "EFI", "BIOS", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine first created.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerArmId" /></td>
    <td><code>string</code></td>
    <td>The data center management server ARM Id for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerName" /></td>
    <td><code>string</code></td>
    <td>The data center management server name for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryMachineArmId" /></td>
    <td><code>string</code></td>
    <td>Site id of machine discovered in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>object</code></td>
    <td>Disks attached to the machine discovered in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name of the Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>List of errors for this machine.</td>
</tr>
<tr>
    <td><CopyableCode code="groups" /></td>
    <td><code>array</code></td>
    <td>Gets the References to the groups that this machine is member of.</td>
</tr>
<tr>
    <td><CopyableCode code="hostProcessor" /></td>
    <td><code>object</code></td>
    <td>Gets Processor details of the host.</td>
</tr>
<tr>
    <td><CopyableCode code="megabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Megabytes of memory found allocated for the machine in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAdapters" /></td>
    <td><code>object</code></td>
    <td>Network adapters attached to the machine discovered in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores found on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemName" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemType" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="productSupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the product support status related details.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlInstances" /></td>
    <td><code>array</code></td>
    <td>SQL instances discovered on the machine.</td>
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
    <td>When was machine last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplications" /></td>
    <td><code>array</code></td>
    <td>Web applications discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadSummary" /></td>
    <td><code>object</code></td>
    <td>Gets or sets workload summary.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Machine.</td>
</tr>
<tr>
    <td><a href="#list_by_assessment_project"><CopyableCode code="list_by_assessment_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-totalRecordCount"><code>totalRecordCount</code></a></td>
    <td>List Machine resources by AssessmentProject.</td>
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
<tr id="parameter-machine_name">
    <td><CopyableCode code="machine_name" /></td>
    <td><code>string</code></td>
    <td>Assessible Machine ARM name. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter query. Default value is None.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>Optional parameter for continuation token. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Optional parameter for page size. Default value is None.</td>
</tr>
<tr id="parameter-totalRecordCount">
    <td><CopyableCode code="totalRecordCount" /></td>
    <td><code>integer</code></td>
    <td>Total record count. Default value is None.</td>
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

Get a Machine.

```sql
SELECT
id,
name,
bootType,
createdTimestamp,
datacenterManagementServerArmId,
datacenterManagementServerName,
description,
discoveryMachineArmId,
disks,
displayName,
errors,
groups,
hostProcessor,
megabytesOfMemory,
networkAdapters,
numberOfCores,
operatingSystemName,
operatingSystemType,
operatingSystemVersion,
productSupportStatus,
sqlInstances,
systemData,
type,
updatedTimestamp,
webApplications,
workloadSummary
FROM azure.migrationassessment.machines_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND machine_name = '{{ machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_assessment_project">

List Machine resources by AssessmentProject.

```sql
SELECT
id,
name,
bootType,
createdTimestamp,
datacenterManagementServerArmId,
datacenterManagementServerName,
description,
discoveryMachineArmId,
disks,
displayName,
errors,
groups,
hostProcessor,
megabytesOfMemory,
networkAdapters,
numberOfCores,
operatingSystemName,
operatingSystemType,
operatingSystemVersion,
productSupportStatus,
sqlInstances,
systemData,
type,
updatedTimestamp,
webApplications,
workloadSummary
FROM azure.migrationassessment.machines_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND pageSize = '{{ pageSize }}'
AND continuationToken = '{{ continuationToken }}'
AND totalRecordCount = '{{ totalRecordCount }}'
;
```
</TabItem>
</Tabs>
