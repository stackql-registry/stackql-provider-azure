--- 
title: avs_assessed_machines_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - avs_assessed_machines_operations
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

Creates, updates, deletes, gets or lists an <code>avs_assessed_machines_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="avs_assessed_machines_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migration_assessment.avs_assessed_machines_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_avs_assessment', value: 'list_by_avs_assessment' }
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
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine first created.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterMachineArmId" /></td>
    <td><code>string</code></td>
    <td>Data center machine ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerArmId" /></td>
    <td><code>string</code></td>
    <td>Data center management server ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerName" /></td>
    <td><code>string</code></td>
    <td>Data center management server name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>object</code></td>
    <td>List of Disks that were assessed as part of this machine's assessment.</td>
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
    <td><CopyableCode code="megabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Megabytes of memory found allocated for the machine in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAdapters" /></td>
    <td><code>object</code></td>
    <td>List of Network Adapters that were assessed as part of this machine's assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores found on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemArchitecture" /></td>
    <td><code>string</code></td>
    <td>Operating system architecture as reported by datacenter management solution. Known values are: "Unknown", "X86", and "X64".</td>
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
    <td><CopyableCode code="percentageCoresUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Cores Utilized noted during time period T. Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageMemoryUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Memory Utilized noted during time period T. .. code-block:: Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="storageInUseGB" /></td>
    <td><code>number</code></td>
    <td>Gets the storage in use.</td>
</tr>
<tr>
    <td><CopyableCode code="suitability" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether machine is suitable for the cloud platform selected. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityDetail" /></td>
    <td><code>string</code></td>
    <td>Gets the details if machine is not suitable for cloud. Known values are: "None", "PercentageOfCoresUtilizedMissing", "PercentageOfMemoryUtilizedMissing", "PercentageOfCoresUtilizedOutOfRange", "PercentageOfMemoryUtilizedOutOfRange", and "PercentageOfStorageUtilizedOutOfRange".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityExplanation" /></td>
    <td><code>string</code></td>
    <td>Gets the explanation if machine is not suitable for cloud. Known values are: "Unknown", "NotApplicable", "IpV6NotSupported", and "UnsupportedOperatingSystem".</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_avs_assessment">

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
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine first created.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterMachineArmId" /></td>
    <td><code>string</code></td>
    <td>Data center machine ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerArmId" /></td>
    <td><code>string</code></td>
    <td>Data center management server ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerName" /></td>
    <td><code>string</code></td>
    <td>Data center management server name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>object</code></td>
    <td>List of Disks that were assessed as part of this machine's assessment.</td>
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
    <td><CopyableCode code="megabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Megabytes of memory found allocated for the machine in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAdapters" /></td>
    <td><code>object</code></td>
    <td>List of Network Adapters that were assessed as part of this machine's assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores found on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemArchitecture" /></td>
    <td><code>string</code></td>
    <td>Operating system architecture as reported by datacenter management solution. Known values are: "Unknown", "X86", and "X64".</td>
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
    <td><CopyableCode code="percentageCoresUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Cores Utilized noted during time period T. Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageMemoryUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Memory Utilized noted during time period T. .. code-block:: Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="storageInUseGB" /></td>
    <td><code>number</code></td>
    <td>Gets the storage in use.</td>
</tr>
<tr>
    <td><CopyableCode code="suitability" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether machine is suitable for the cloud platform selected. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityDetail" /></td>
    <td><code>string</code></td>
    <td>Gets the details if machine is not suitable for cloud. Known values are: "None", "PercentageOfCoresUtilizedMissing", "PercentageOfMemoryUtilizedMissing", "PercentageOfCoresUtilizedOutOfRange", "PercentageOfMemoryUtilizedOutOfRange", and "PercentageOfStorageUtilizedOutOfRange".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityExplanation" /></td>
    <td><code>string</code></td>
    <td>Gets the explanation if machine is not suitable for cloud. Known values are: "Unknown", "NotApplicable", "IpV6NotSupported", and "UnsupportedOperatingSystem".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-avs_assessed_machine_name"><code>avs_assessed_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AvsAssessedMachine.</td>
</tr>
<tr>
    <td><a href="#list_by_avs_assessment"><CopyableCode code="list_by_avs_assessment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-totalRecordCount"><code>totalRecordCount</code></a></td>
    <td>List AvsAssessedMachine resources by AvsAssessment.</td>
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
<tr id="parameter-assessment_name">
    <td><CopyableCode code="assessment_name" /></td>
    <td><code>string</code></td>
    <td>AVS Assessment ARM name. Required.</td>
</tr>
<tr id="parameter-avs_assessed_machine_name">
    <td><CopyableCode code="avs_assessed_machine_name" /></td>
    <td><code>string</code></td>
    <td>AVS assessment Assessed Machine ARM name. Required.</td>
</tr>
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
        { label: 'list_by_avs_assessment', value: 'list_by_avs_assessment' }
    ]}
>
<TabItem value="get">

Get a AvsAssessedMachine.

```sql
SELECT
id,
name,
bootType,
confidenceRatingInPercentage,
createdTimestamp,
datacenterMachineArmId,
datacenterManagementServerArmId,
datacenterManagementServerName,
description,
disks,
displayName,
errors,
megabytesOfMemory,
networkAdapters,
numberOfCores,
operatingSystemArchitecture,
operatingSystemName,
operatingSystemType,
operatingSystemVersion,
percentageCoresUtilization,
percentageMemoryUtilization,
storageInUseGB,
suitability,
suitabilityDetail,
suitabilityExplanation,
systemData,
type,
updatedTimestamp
FROM azure.migration_assessment.avs_assessed_machines_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND avs_assessed_machine_name = '{{ avs_assessed_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_avs_assessment">

List AvsAssessedMachine resources by AvsAssessment.

```sql
SELECT
id,
name,
bootType,
confidenceRatingInPercentage,
createdTimestamp,
datacenterMachineArmId,
datacenterManagementServerArmId,
datacenterManagementServerName,
description,
disks,
displayName,
errors,
megabytesOfMemory,
networkAdapters,
numberOfCores,
operatingSystemArchitecture,
operatingSystemName,
operatingSystemType,
operatingSystemVersion,
percentageCoresUtilization,
percentageMemoryUtilization,
storageInUseGB,
suitability,
suitabilityDetail,
suitabilityExplanation,
systemData,
type,
updatedTimestamp
FROM azure.migration_assessment.avs_assessed_machines_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND pageSize = '{{ pageSize }}'
AND continuationToken = '{{ continuationToken }}'
AND totalRecordCount = '{{ totalRecordCount }}'
;
```
</TabItem>
</Tabs>
