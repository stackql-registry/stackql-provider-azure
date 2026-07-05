--- 
title: sql_assessment_v2_summary_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_assessment_v2_summary_operations
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

Creates, updates, deletes, gets or lists a <code>sql_assessment_v2_summary_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_assessment_v2_summary_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrationassessment.sql_assessment_v2_summary_operations" /></td></tr>
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
    <td><CopyableCode code="assessmentSummary" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Assessment summary.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDistributionBySizingCriterion" /></td>
    <td><code>object</code></td>
    <td>Gets the database distribution by sizing criterion.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionByServicePackInsight" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution distribution of sqlInstances by service pack insight.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionBySqlEdition" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution of sqlInstances by sql edition.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionBySqlVersion" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution of sqlInstances by sql version.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionBySupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution of sqlInstances by support status.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceDistributionBySizingCriterion" /></td>
    <td><code>object</code></td>
    <td>Gets the instance distribution by sizing criterion.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFciInstances" /></td>
    <td><code>integer</code></td>
    <td>Number of sql failover cluster instances part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Number of machines part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSqlAvailabilityGroups" /></td>
    <td><code>integer</code></td>
    <td>Number of sql availability groups part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSqlDatabases" /></td>
    <td><code>integer</code></td>
    <td>Number of sql databases part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSqlInstances" /></td>
    <td><code>integer</code></td>
    <td>Number of sql instances part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSuccessfullyDiscoveredSqlInstances" /></td>
    <td><code>integer</code></td>
    <td>Number of successfully discovered sql instances part of the assessment.</td>
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
    <td><CopyableCode code="assessmentSummary" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the Assessment summary.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseDistributionBySizingCriterion" /></td>
    <td><code>object</code></td>
    <td>Gets the database distribution by sizing criterion.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionByServicePackInsight" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution distribution of sqlInstances by service pack insight.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionBySqlEdition" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution of sqlInstances by sql edition.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionBySqlVersion" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution of sqlInstances by sql version.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionBySupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the distribution of sqlInstances by support status.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceDistributionBySizingCriterion" /></td>
    <td><code>object</code></td>
    <td>Gets the instance distribution by sizing criterion.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfFciInstances" /></td>
    <td><code>integer</code></td>
    <td>Number of sql failover cluster instances part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Number of machines part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSqlAvailabilityGroups" /></td>
    <td><code>integer</code></td>
    <td>Number of sql availability groups part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSqlDatabases" /></td>
    <td><code>integer</code></td>
    <td>Number of sql databases part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSqlInstances" /></td>
    <td><code>integer</code></td>
    <td>Number of sql instances part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSuccessfullyDiscoveredSqlInstances" /></td>
    <td><code>integer</code></td>
    <td>Number of successfully discovered sql instances part of the assessment.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-summary_name"><code>summary_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a SqlAssessmentV2Summary.</td>
</tr>
<tr>
    <td><a href="#list_by_sql_assessment_v2"><CopyableCode code="list_by_sql_assessment_v2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List SqlAssessmentV2Summary resources by SqlAssessmentV2.</td>
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
<tr id="parameter-summary_name">
    <td><CopyableCode code="summary_name" /></td>
    <td><code>string</code></td>
    <td>Gets the Name of the SQL Summary. Required.</td>
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

Get a SqlAssessmentV2Summary.

```sql
SELECT
id,
name,
assessmentSummary,
databaseDistributionBySizingCriterion,
distributionByServicePackInsight,
distributionBySqlEdition,
distributionBySqlVersion,
distributionBySupportStatus,
instanceDistributionBySizingCriterion,
numberOfFciInstances,
numberOfMachines,
numberOfSqlAvailabilityGroups,
numberOfSqlDatabases,
numberOfSqlInstances,
numberOfSuccessfullyDiscoveredSqlInstances,
systemData,
type
FROM azure.migrationassessment.sql_assessment_v2_summary_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND summary_name = '{{ summary_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sql_assessment_v2">

List SqlAssessmentV2Summary resources by SqlAssessmentV2.

```sql
SELECT
id,
name,
assessmentSummary,
databaseDistributionBySizingCriterion,
distributionByServicePackInsight,
distributionBySqlEdition,
distributionBySqlVersion,
distributionBySupportStatus,
instanceDistributionBySizingCriterion,
numberOfFciInstances,
numberOfMachines,
numberOfSqlAvailabilityGroups,
numberOfSqlDatabases,
numberOfSqlInstances,
numberOfSuccessfullyDiscoveredSqlInstances,
systemData,
type
FROM azure.migrationassessment.sql_assessment_v2_summary_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
