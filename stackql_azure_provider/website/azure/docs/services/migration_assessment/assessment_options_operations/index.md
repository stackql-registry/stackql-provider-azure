--- 
title: assessment_options_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_options_operations
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

Creates, updates, deletes, gets or lists an <code>assessment_options_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assessment_options_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migration_assessment.assessment_options_operations" /></td></tr>
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
    <td><CopyableCode code="premiumDiskVmFamilies" /></td>
    <td><code>array</code></td>
    <td>List of VM Families that support premium disks for assessments.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceSupportedCurrencies" /></td>
    <td><code>array</code></td>
    <td>List of supported currencies for reserved instances.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceSupportedLocations" /></td>
    <td><code>array</code></td>
    <td>List of supported Azure regions for reserved instances.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceSupportedOffers" /></td>
    <td><code>array</code></td>
    <td>List of supported Azure offer codes for reserved instances.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceVmFamilies" /></td>
    <td><code>array</code></td>
    <td>List of supported VM Families.</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlanSupportedLocations" /></td>
    <td><code>array</code></td>
    <td>List of Azure locations that support Savings plan offer for assessments.</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlanVmFamilies" /></td>
    <td><code>array</code></td>
    <td>List of VM Families that support Savings plan offer for assessments.</td>
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
    <td><CopyableCode code="ultraDiskVmFamilies" /></td>
    <td><code>array</code></td>
    <td>Ultra disk related assessment options.</td>
</tr>
<tr>
    <td><CopyableCode code="vmFamilies" /></td>
    <td><code>array</code></td>
    <td>Dictionary of VM families grouped by vm family name describing the targeted azure locations of VM family and the category of the family.</td>
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
    <td><CopyableCode code="premiumDiskVmFamilies" /></td>
    <td><code>array</code></td>
    <td>List of VM Families that support premium disks for assessments.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceSupportedCurrencies" /></td>
    <td><code>array</code></td>
    <td>List of supported currencies for reserved instances.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceSupportedLocations" /></td>
    <td><code>array</code></td>
    <td>List of supported Azure regions for reserved instances.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceSupportedOffers" /></td>
    <td><code>array</code></td>
    <td>List of supported Azure offer codes for reserved instances.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstanceVmFamilies" /></td>
    <td><code>array</code></td>
    <td>List of supported VM Families.</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlanSupportedLocations" /></td>
    <td><code>array</code></td>
    <td>List of Azure locations that support Savings plan offer for assessments.</td>
</tr>
<tr>
    <td><CopyableCode code="savingsPlanVmFamilies" /></td>
    <td><code>array</code></td>
    <td>List of VM Families that support Savings plan offer for assessments.</td>
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
    <td><CopyableCode code="ultraDiskVmFamilies" /></td>
    <td><code>array</code></td>
    <td>Ultra disk related assessment options.</td>
</tr>
<tr>
    <td><CopyableCode code="vmFamilies" /></td>
    <td><code>array</code></td>
    <td>Dictionary of VM families grouped by vm family name describing the targeted azure locations of VM family and the category of the family.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-assessment_options_name"><code>assessment_options_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AssessmentOptions.</td>
</tr>
<tr>
    <td><a href="#list_by_assessment_project"><CopyableCode code="list_by_assessment_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AssessmentOptions resources by AssessmentProject.</td>
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
<tr id="parameter-assessment_options_name">
    <td><CopyableCode code="assessment_options_name" /></td>
    <td><code>string</code></td>
    <td>assessment options ARM name. Accepted value is 'default'. Required.</td>
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

Get a AssessmentOptions.

```sql
SELECT
id,
name,
premiumDiskVmFamilies,
reservedInstanceSupportedCurrencies,
reservedInstanceSupportedLocations,
reservedInstanceSupportedOffers,
reservedInstanceVmFamilies,
savingsPlanSupportedLocations,
savingsPlanVmFamilies,
systemData,
type,
ultraDiskVmFamilies,
vmFamilies
FROM azure.migration_assessment.assessment_options_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND assessment_options_name = '{{ assessment_options_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_assessment_project">

List AssessmentOptions resources by AssessmentProject.

```sql
SELECT
id,
name,
premiumDiskVmFamilies,
reservedInstanceSupportedCurrencies,
reservedInstanceSupportedLocations,
reservedInstanceSupportedOffers,
reservedInstanceVmFamilies,
savingsPlanSupportedLocations,
savingsPlanVmFamilies,
systemData,
type,
ultraDiskVmFamilies,
vmFamilies
FROM azure.migration_assessment.assessment_options_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
