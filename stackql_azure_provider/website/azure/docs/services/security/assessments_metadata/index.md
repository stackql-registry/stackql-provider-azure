--- 
title: assessments_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments_metadata
  - security
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

Creates, updates, deletes, gets or lists an <code>assessments_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assessments_metadata" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.assessments_metadata" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_in_subscription"
    values={[
        { label: 'get_in_subscription', value: 'get_in_subscription' },
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_in_subscription">

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
    <td><CopyableCode code="assessmentType" /></td>
    <td><code>string</code></td>
    <td>BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition. Required. Known values are: "Unknown", "BuiltIn", "Custom", "CustomPolicy", "CustomerManaged", "BuiltInPolicy", "VerifiedPartner", "ManualBuiltInPolicy", "ManualBuiltIn", "ManualCustomPolicy", and "DynamicBuiltIn". (Unknown, BuiltIn, Custom, CustomPolicy, CustomerManaged, BuiltInPolicy, VerifiedPartner, ManualBuiltInPolicy, ManualBuiltIn, ManualCustomPolicy, DynamicBuiltIn)</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>:vartype categories: list[str or ~azure.mgmt.security.models.Categories]</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Human readable description of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the assessment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationEffort" /></td>
    <td><code>string</code></td>
    <td>The implementation effort required to remediate this assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerData" /></td>
    <td><code>object</code></td>
    <td>Describes the partner that created the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="plannedDeprecationDate" /></td>
    <td><code>string</code></td>
    <td>:vartype planned_deprecation_date: str</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the policy definition that turns this assessment calculation on.</td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>boolean</code></td>
    <td>True if this assessment is in preview release status.</td>
</tr>
<tr>
    <td><CopyableCode code="publishDates" /></td>
    <td><code>object</code></td>
    <td>:vartype publish_dates: ~azure.mgmt.security.models.SecurityAssessmentMetadataPropertiesResponsePublishDates</td>
</tr>
<tr>
    <td><CopyableCode code="remediationDescription" /></td>
    <td><code>string</code></td>
    <td>Human readable description of what you should do to mitigate this security issue.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The severity level of the assessment. Required. Known values are: "Low", "Medium", "High", and "Critical". (Low, Medium, High, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tactics" /></td>
    <td><code>array</code></td>
    <td>:vartype tactics: list[str or ~azure.mgmt.security.models.Tactics]</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>:vartype techniques: list[str or ~azure.mgmt.security.models.Techniques]</td>
</tr>
<tr>
    <td><CopyableCode code="threats" /></td>
    <td><code>array</code></td>
    <td>:vartype threats: list[str or ~azure.mgmt.security.models.Threats]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userImpact" /></td>
    <td><code>string</code></td>
    <td>The user impact of the assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="assessmentType" /></td>
    <td><code>string</code></td>
    <td>BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition. Required. Known values are: "Unknown", "BuiltIn", "Custom", "CustomPolicy", "CustomerManaged", "BuiltInPolicy", "VerifiedPartner", "ManualBuiltInPolicy", "ManualBuiltIn", "ManualCustomPolicy", and "DynamicBuiltIn". (Unknown, BuiltIn, Custom, CustomPolicy, CustomerManaged, BuiltInPolicy, VerifiedPartner, ManualBuiltInPolicy, ManualBuiltIn, ManualCustomPolicy, DynamicBuiltIn)</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>:vartype categories: list[str or ~azure.mgmt.security.models.Categories]</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Human readable description of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the assessment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationEffort" /></td>
    <td><code>string</code></td>
    <td>The implementation effort required to remediate this assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerData" /></td>
    <td><code>object</code></td>
    <td>Describes the partner that created the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="plannedDeprecationDate" /></td>
    <td><code>string</code></td>
    <td>:vartype planned_deprecation_date: str</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the policy definition that turns this assessment calculation on.</td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>boolean</code></td>
    <td>True if this assessment is in preview release status.</td>
</tr>
<tr>
    <td><CopyableCode code="publishDates" /></td>
    <td><code>object</code></td>
    <td>:vartype publish_dates: ~azure.mgmt.security.models.SecurityAssessmentMetadataPropertiesResponsePublishDates</td>
</tr>
<tr>
    <td><CopyableCode code="remediationDescription" /></td>
    <td><code>string</code></td>
    <td>Human readable description of what you should do to mitigate this security issue.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The severity level of the assessment. Required. Known values are: "Low", "Medium", "High", and "Critical". (Low, Medium, High, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tactics" /></td>
    <td><code>array</code></td>
    <td>:vartype tactics: list[str or ~azure.mgmt.security.models.Tactics]</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>:vartype techniques: list[str or ~azure.mgmt.security.models.Techniques]</td>
</tr>
<tr>
    <td><CopyableCode code="threats" /></td>
    <td><code>array</code></td>
    <td>:vartype threats: list[str or ~azure.mgmt.security.models.Threats]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userImpact" /></td>
    <td><code>string</code></td>
    <td>The user impact of the assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="assessmentType" /></td>
    <td><code>string</code></td>
    <td>BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition. Required. Known values are: "Unknown", "BuiltIn", "Custom", "CustomPolicy", "CustomerManaged", "BuiltInPolicy", "VerifiedPartner", "ManualBuiltInPolicy", "ManualBuiltIn", "ManualCustomPolicy", and "DynamicBuiltIn". (Unknown, BuiltIn, Custom, CustomPolicy, CustomerManaged, BuiltInPolicy, VerifiedPartner, ManualBuiltInPolicy, ManualBuiltIn, ManualCustomPolicy, DynamicBuiltIn)</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>:vartype categories: list[str or ~azure.mgmt.security.models.Categories]</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Human readable description of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the assessment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationEffort" /></td>
    <td><code>string</code></td>
    <td>The implementation effort required to remediate this assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerData" /></td>
    <td><code>object</code></td>
    <td>Describes the partner that created the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="plannedDeprecationDate" /></td>
    <td><code>string</code></td>
    <td>:vartype planned_deprecation_date: str</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the policy definition that turns this assessment calculation on.</td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>boolean</code></td>
    <td>True if this assessment is in preview release status.</td>
</tr>
<tr>
    <td><CopyableCode code="publishDates" /></td>
    <td><code>object</code></td>
    <td>:vartype publish_dates: ~azure.mgmt.security.models.SecurityAssessmentMetadataPropertiesResponsePublishDates</td>
</tr>
<tr>
    <td><CopyableCode code="remediationDescription" /></td>
    <td><code>string</code></td>
    <td>Human readable description of what you should do to mitigate this security issue.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The severity level of the assessment. Required. Known values are: "Low", "Medium", "High", and "Critical". (Low, Medium, High, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tactics" /></td>
    <td><code>array</code></td>
    <td>:vartype tactics: list[str or ~azure.mgmt.security.models.Tactics]</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>:vartype techniques: list[str or ~azure.mgmt.security.models.Techniques]</td>
</tr>
<tr>
    <td><CopyableCode code="threats" /></td>
    <td><code>array</code></td>
    <td>:vartype threats: list[str or ~azure.mgmt.security.models.Threats]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userImpact" /></td>
    <td><code>string</code></td>
    <td>The user impact of the assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentType" /></td>
    <td><code>string</code></td>
    <td>BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition. Required. Known values are: "Unknown", "BuiltIn", "Custom", "CustomPolicy", "CustomerManaged", "BuiltInPolicy", "VerifiedPartner", "ManualBuiltInPolicy", "ManualBuiltIn", "ManualCustomPolicy", and "DynamicBuiltIn". (Unknown, BuiltIn, Custom, CustomPolicy, CustomerManaged, BuiltInPolicy, VerifiedPartner, ManualBuiltInPolicy, ManualBuiltIn, ManualCustomPolicy, DynamicBuiltIn)</td>
</tr>
<tr>
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>:vartype categories: list[str or ~azure.mgmt.security.models.Categories]</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Human readable description of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the assessment. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationEffort" /></td>
    <td><code>string</code></td>
    <td>The implementation effort required to remediate this assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerData" /></td>
    <td><code>object</code></td>
    <td>Describes the partner that created the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="plannedDeprecationDate" /></td>
    <td><code>string</code></td>
    <td>:vartype planned_deprecation_date: str</td>
</tr>
<tr>
    <td><CopyableCode code="policyDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the policy definition that turns this assessment calculation on.</td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>boolean</code></td>
    <td>True if this assessment is in preview release status.</td>
</tr>
<tr>
    <td><CopyableCode code="publishDates" /></td>
    <td><code>object</code></td>
    <td>:vartype publish_dates: ~azure.mgmt.security.models.SecurityAssessmentMetadataPropertiesResponsePublishDates</td>
</tr>
<tr>
    <td><CopyableCode code="remediationDescription" /></td>
    <td><code>string</code></td>
    <td>Human readable description of what you should do to mitigate this security issue.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The severity level of the assessment. Required. Known values are: "Low", "Medium", "High", and "Critical". (Low, Medium, High, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tactics" /></td>
    <td><code>array</code></td>
    <td>:vartype tactics: list[str or ~azure.mgmt.security.models.Tactics]</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>:vartype techniques: list[str or ~azure.mgmt.security.models.Techniques]</td>
</tr>
<tr>
    <td><CopyableCode code="threats" /></td>
    <td><code>array</code></td>
    <td>:vartype threats: list[str or ~azure.mgmt.security.models.Threats]</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userImpact" /></td>
    <td><code>string</code></td>
    <td>The user impact of the assessment. Known values are: "Low", "Moderate", and "High". (Low, Moderate, High)</td>
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
    <td><a href="#get_in_subscription"><CopyableCode code="get_in_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-assessment_metadata_name"><code>assessment_metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metadata information on an assessment type in a specific subscription.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-assessment_metadata_name"><code>assessment_metadata_name</code></a></td>
    <td></td>
    <td>Get metadata information on an assessment type.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metadata information on all assessment types in a specific subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get metadata information on all assessment types.</td>
</tr>
<tr>
    <td><a href="#create_in_subscription"><CopyableCode code="create_in_subscription" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-assessment_metadata_name"><code>assessment_metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create metadata information on an assessment type in a specific subscription.</td>
</tr>
<tr>
    <td><a href="#delete_in_subscription"><CopyableCode code="delete_in_subscription" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-assessment_metadata_name"><code>assessment_metadata_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription.</td>
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
<tr id="parameter-assessment_metadata_name">
    <td><CopyableCode code="assessment_metadata_name" /></td>
    <td><code>string</code></td>
    <td>The Assessment Key - Unique key for the assessment type. Required.</td>
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
    defaultValue="get_in_subscription"
    values={[
        { label: 'get_in_subscription', value: 'get_in_subscription' },
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_in_subscription">

Get metadata information on an assessment type in a specific subscription.

```sql
SELECT
id,
name,
assessmentType,
categories,
description,
displayName,
implementationEffort,
partnerData,
plannedDeprecationDate,
policyDefinitionId,
preview,
publishDates,
remediationDescription,
severity,
systemData,
tactics,
techniques,
threats,
type,
userImpact
FROM azure.security.assessments_metadata
WHERE assessment_metadata_name = '{{ assessment_metadata_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get metadata information on an assessment type.

```sql
SELECT
id,
name,
assessmentType,
categories,
description,
displayName,
implementationEffort,
partnerData,
plannedDeprecationDate,
policyDefinitionId,
preview,
publishDates,
remediationDescription,
severity,
systemData,
tactics,
techniques,
threats,
type,
userImpact
FROM azure.security.assessments_metadata
WHERE assessment_metadata_name = '{{ assessment_metadata_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get metadata information on all assessment types in a specific subscription.

```sql
SELECT
id,
name,
assessmentType,
categories,
description,
displayName,
implementationEffort,
partnerData,
plannedDeprecationDate,
policyDefinitionId,
preview,
publishDates,
remediationDescription,
severity,
systemData,
tactics,
techniques,
threats,
type,
userImpact
FROM azure.security.assessments_metadata
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get metadata information on all assessment types.

```sql
SELECT
id,
name,
assessmentType,
categories,
description,
displayName,
implementationEffort,
partnerData,
plannedDeprecationDate,
policyDefinitionId,
preview,
publishDates,
remediationDescription,
severity,
systemData,
tactics,
techniques,
threats,
type,
userImpact
FROM azure.security.assessments_metadata
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_in_subscription"
    values={[
        { label: 'create_in_subscription', value: 'create_in_subscription' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_in_subscription">

Create metadata information on an assessment type in a specific subscription.

```sql
INSERT INTO azure.security.assessments_metadata (
properties,
assessment_metadata_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ assessment_metadata_name }}',
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
- name: assessments_metadata
  props:
    - name: assessment_metadata_name
      value: "{{ assessment_metadata_name }}"
      description: Required parameter for the assessments_metadata resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the assessments_metadata resource.
    - name: properties
      description: |
        Describes properties of an assessment metadata response.
      value:
        displayName: "{{ displayName }}"
        policyDefinitionId: "{{ policyDefinitionId }}"
        description: "{{ description }}"
        remediationDescription: "{{ remediationDescription }}"
        categories:
          - "{{ categories }}"
        severity: "{{ severity }}"
        userImpact: "{{ userImpact }}"
        implementationEffort: "{{ implementationEffort }}"
        threats:
          - "{{ threats }}"
        preview: {{ preview }}
        assessmentType: "{{ assessmentType }}"
        partnerData:
          partnerName: "{{ partnerName }}"
          productName: "{{ productName }}"
          secret: "{{ secret }}"
        publishDates:
          GA: "{{ GA }}"
          public: "{{ public }}"
        plannedDeprecationDate: "{{ plannedDeprecationDate }}"
        tactics:
          - "{{ tactics }}"
        techniques:
          - "{{ techniques }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_in_subscription"
    values={[
        { label: 'delete_in_subscription', value: 'delete_in_subscription' }
    ]}
>
<TabItem value="delete_in_subscription">

Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription.

```sql
DELETE FROM azure.security.assessments_metadata
WHERE assessment_metadata_name = '{{ assessment_metadata_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
