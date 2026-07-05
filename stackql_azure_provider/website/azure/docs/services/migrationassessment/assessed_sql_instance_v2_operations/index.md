--- 
title: assessed_sql_instance_v2_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessed_sql_instance_v2_operations
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

Creates, updates, deletes, gets or lists an <code>assessed_sql_instance_v2_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assessed_sql_instance_v2_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrationassessment.assessed_sql_instance_v2_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_assessment_v2', value: 'list_by_sql_assessment_v2' }
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
    <td><CopyableCode code="availabilityReplicaSummary" /></td>
    <td><code>object</code></td>
    <td>Gets the overview counts of availability replicas in the assessed instance, by commit mode and read type.</td>
</tr>
<tr>
    <td><CopyableCode code="azureSqlDBSuitabilityDetails" /></td>
    <td><code>object</code></td>
    <td>SQL instance azure SQL DB suitability details.</td>
</tr>
<tr>
    <td><CopyableCode code="azureSqlMISuitabilityDetails" /></td>
    <td><code>object</code></td>
    <td>SQL instance azure SQL MI suitability details.</td>
</tr>
<tr>
    <td><CopyableCode code="azureSqlVMSuitabilityDetails" /></td>
    <td><code>object</code></td>
    <td>SQL instance azure SQL VM suitability details.</td>
</tr>
<tr>
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was assessed SQL instance first created.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseSummary" /></td>
    <td><code>object</code></td>
    <td>The databases summary.</td>
</tr>
<tr>
    <td><CopyableCode code="fciMetadata" /></td>
    <td><code>object</code></td>
    <td>Gets the FCI metadata if this instance represents an FCI instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hasScanOccurred" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether SQL instance has been deep discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceName" /></td>
    <td><code>string</code></td>
    <td>SQL instance name.</td>
</tr>
<tr>
    <td><CopyableCode code="isClustered" /></td>
    <td><code>boolean</code></td>
    <td>Gets a value indicating whether the SQL instance is clustered or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isHighAvailabilityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets a value indicating whether the high availability is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="logicalDisks" /></td>
    <td><code>array</code></td>
    <td>The logical disk details.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmId" /></td>
    <td><code>string</code></td>
    <td>Machine arm id.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>Machine display name.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryInUseInMB" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the memory used by SQL instance in megabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCoresAllocated" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores assigned to the SQL instance.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageCoresUtilization" /></td>
    <td><code>number</code></td>
    <td>The percentage of the total number of cores being utilized by the SQL instance.</td>
</tr>
<tr>
    <td><CopyableCode code="productSupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the product support status related details.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedAzureSqlTargetType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the recommended azure SQL target type. Known values are: "Unknown", "Recommended", "AzureSqlDatabase", "AzureSqlManagedInstance", "AzureSqlVirtualMachine", and "AzureVirtualMachine".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedSuitability" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the recommended azure SQL suitability. Known values are: "Unknown", "SuitableForSqlDB", "SuitableForSqlMI", "SuitableForVM", "PotentiallySuitableForVM", "ReadinessUnknown", "NotSuitable", "SuitableForSqlVM", "ConditionallySuitableForSqlDB", "ConditionallySuitableForSqlMI", "ConditionallySuitableForVM", and "ConditionallySuitableForSqlVM".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedTargetReasonings" /></td>
    <td><code>array</code></td>
    <td>Gets the list of recommended target reasoning.</td>
</tr>
<tr>
    <td><CopyableCode code="sizingCriterion" /></td>
    <td><code>string</code></td>
    <td>Assessment sizing criterion. Known values are: "PerformanceBased" and "AsOnPremises".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlEdition" /></td>
    <td><code>string</code></td>
    <td>SQL instance edition.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlInstanceSdsArmId" /></td>
    <td><code>string</code></td>
    <td>SQL instance SDS arm id.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlVersion" /></td>
    <td><code>string</code></td>
    <td>SQL instance version.</td>
</tr>
<tr>
    <td><CopyableCode code="storageTypeBasedDetails" /></td>
    <td><code>array</code></td>
    <td>Gets the storage details.</td>
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
    <td>When was assessed SQL instance last updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_sql_assessment_v2">

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
    <td><CopyableCode code="availabilityReplicaSummary" /></td>
    <td><code>object</code></td>
    <td>Gets the overview counts of availability replicas in the assessed instance, by commit mode and read type.</td>
</tr>
<tr>
    <td><CopyableCode code="azureSqlDBSuitabilityDetails" /></td>
    <td><code>object</code></td>
    <td>SQL instance azure SQL DB suitability details.</td>
</tr>
<tr>
    <td><CopyableCode code="azureSqlMISuitabilityDetails" /></td>
    <td><code>object</code></td>
    <td>SQL instance azure SQL MI suitability details.</td>
</tr>
<tr>
    <td><CopyableCode code="azureSqlVMSuitabilityDetails" /></td>
    <td><code>object</code></td>
    <td>SQL instance azure SQL VM suitability details.</td>
</tr>
<tr>
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was assessed SQL instance first created.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseSummary" /></td>
    <td><code>object</code></td>
    <td>The databases summary.</td>
</tr>
<tr>
    <td><CopyableCode code="fciMetadata" /></td>
    <td><code>object</code></td>
    <td>Gets the FCI metadata if this instance represents an FCI instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hasScanOccurred" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether SQL instance has been deep discovered.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceName" /></td>
    <td><code>string</code></td>
    <td>SQL instance name.</td>
</tr>
<tr>
    <td><CopyableCode code="isClustered" /></td>
    <td><code>boolean</code></td>
    <td>Gets a value indicating whether the SQL instance is clustered or not.</td>
</tr>
<tr>
    <td><CopyableCode code="isHighAvailabilityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets a value indicating whether the high availability is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="logicalDisks" /></td>
    <td><code>array</code></td>
    <td>The logical disk details.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmId" /></td>
    <td><code>string</code></td>
    <td>Machine arm id.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>Machine display name.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryInUseInMB" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the memory used by SQL instance in megabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCoresAllocated" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores assigned to the SQL instance.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageCoresUtilization" /></td>
    <td><code>number</code></td>
    <td>The percentage of the total number of cores being utilized by the SQL instance.</td>
</tr>
<tr>
    <td><CopyableCode code="productSupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the product support status related details.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedAzureSqlTargetType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the recommended azure SQL target type. Known values are: "Unknown", "Recommended", "AzureSqlDatabase", "AzureSqlManagedInstance", "AzureSqlVirtualMachine", and "AzureVirtualMachine".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedSuitability" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the recommended azure SQL suitability. Known values are: "Unknown", "SuitableForSqlDB", "SuitableForSqlMI", "SuitableForVM", "PotentiallySuitableForVM", "ReadinessUnknown", "NotSuitable", "SuitableForSqlVM", "ConditionallySuitableForSqlDB", "ConditionallySuitableForSqlMI", "ConditionallySuitableForVM", and "ConditionallySuitableForSqlVM".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedTargetReasonings" /></td>
    <td><code>array</code></td>
    <td>Gets the list of recommended target reasoning.</td>
</tr>
<tr>
    <td><CopyableCode code="sizingCriterion" /></td>
    <td><code>string</code></td>
    <td>Assessment sizing criterion. Known values are: "PerformanceBased" and "AsOnPremises".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlEdition" /></td>
    <td><code>string</code></td>
    <td>SQL instance edition.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlInstanceSdsArmId" /></td>
    <td><code>string</code></td>
    <td>SQL instance SDS arm id.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlVersion" /></td>
    <td><code>string</code></td>
    <td>SQL instance version.</td>
</tr>
<tr>
    <td><CopyableCode code="storageTypeBasedDetails" /></td>
    <td><code>array</code></td>
    <td>Gets the storage details.</td>
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
    <td>When was assessed SQL instance last updated.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-assessed_sql_instance_name"><code>assessed_sql_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AssessedSqlInstanceV2.</td>
</tr>
<tr>
    <td><a href="#list_by_sql_assessment_v2"><CopyableCode code="list_by_sql_assessment_v2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-totalRecordCount"><code>totalRecordCount</code></a></td>
    <td>List AssessedSqlInstanceV2 resources by SqlAssessmentV2.</td>
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
<tr id="parameter-assessed_sql_instance_name">
    <td><CopyableCode code="assessed_sql_instance_name" /></td>
    <td><code>string</code></td>
    <td>Sql assessment Assessed Instance ARM name. Required.</td>
</tr>
<tr id="parameter-assessment_name">
    <td><CopyableCode code="assessment_name" /></td>
    <td><code>string</code></td>
    <td>SQL Assessment arm name. Required.</td>
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
        { label: 'list_by_sql_assessment_v2', value: 'list_by_sql_assessment_v2' }
    ]}
>
<TabItem value="get">

Get a AssessedSqlInstanceV2.

```sql
SELECT
id,
name,
availabilityReplicaSummary,
azureSqlDBSuitabilityDetails,
azureSqlMISuitabilityDetails,
azureSqlVMSuitabilityDetails,
confidenceRatingInPercentage,
createdTimestamp,
databaseSummary,
fciMetadata,
hasScanOccurred,
instanceName,
isClustered,
isHighAvailabilityEnabled,
logicalDisks,
machineArmId,
machineName,
memoryInUseInMB,
numberOfCoresAllocated,
percentageCoresUtilization,
productSupportStatus,
recommendedAzureSqlTargetType,
recommendedSuitability,
recommendedTargetReasonings,
sizingCriterion,
sqlEdition,
sqlInstanceSdsArmId,
sqlVersion,
storageTypeBasedDetails,
systemData,
type,
updatedTimestamp
FROM azure.migrationassessment.assessed_sql_instance_v2_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND assessed_sql_instance_name = '{{ assessed_sql_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sql_assessment_v2">

List AssessedSqlInstanceV2 resources by SqlAssessmentV2.

```sql
SELECT
id,
name,
availabilityReplicaSummary,
azureSqlDBSuitabilityDetails,
azureSqlMISuitabilityDetails,
azureSqlVMSuitabilityDetails,
confidenceRatingInPercentage,
createdTimestamp,
databaseSummary,
fciMetadata,
hasScanOccurred,
instanceName,
isClustered,
isHighAvailabilityEnabled,
logicalDisks,
machineArmId,
machineName,
memoryInUseInMB,
numberOfCoresAllocated,
percentageCoresUtilization,
productSupportStatus,
recommendedAzureSqlTargetType,
recommendedSuitability,
recommendedTargetReasonings,
sizingCriterion,
sqlEdition,
sqlInstanceSdsArmId,
sqlVersion,
storageTypeBasedDetails,
systemData,
type,
updatedTimestamp
FROM azure.migrationassessment.assessed_sql_instance_v2_operations
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
