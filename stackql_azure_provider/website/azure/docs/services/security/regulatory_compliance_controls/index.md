--- 
title: regulatory_compliance_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_controls
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

Creates, updates, deletes, gets or lists a <code>regulatory_compliance_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="regulatory_compliance_controls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.regulatory_compliance_controls" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the regulatory compliance control.</td>
</tr>
<tr>
    <td><CopyableCode code="failedAssessments" /></td>
    <td><code>integer</code></td>
    <td>The number of supported regulatory compliance assessments of the given control with a failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="passedAssessments" /></td>
    <td><code>integer</code></td>
    <td>The number of supported regulatory compliance assessments of the given control with a passed state.</td>
</tr>
<tr>
    <td><CopyableCode code="skippedAssessments" /></td>
    <td><code>integer</code></td>
    <td>The number of supported regulatory compliance assessments of the given control with a skipped state.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Aggregative state based on the control's supported assessments states. Known values are: "Passed", "Failed", "Skipped", "Unsupported", "On", and "Off". (Passed, Failed, Skipped, Unsupported, On, Off)</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the regulatory compliance control.</td>
</tr>
<tr>
    <td><CopyableCode code="failedAssessments" /></td>
    <td><code>integer</code></td>
    <td>The number of supported regulatory compliance assessments of the given control with a failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="passedAssessments" /></td>
    <td><code>integer</code></td>
    <td>The number of supported regulatory compliance assessments of the given control with a passed state.</td>
</tr>
<tr>
    <td><CopyableCode code="skippedAssessments" /></td>
    <td><code>integer</code></td>
    <td>The number of supported regulatory compliance assessments of the given control with a skipped state.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Aggregative state based on the control's supported assessments states. Known values are: "Passed", "Failed", "Skipped", "Unsupported", "On", and "Off". (Passed, Failed, Skipped, Unsupported, On, Off)</td>
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
    <td><a href="#parameter-regulatory_compliance_standard_name"><code>regulatory_compliance_standard_name</code></a>, <a href="#parameter-regulatory_compliance_control_name"><code>regulatory_compliance_control_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Selected regulatory compliance control details and state.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-regulatory_compliance_standard_name"><code>regulatory_compliance_standard_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>All supported regulatory compliance controls details and state for selected standard.</td>
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
<tr id="parameter-regulatory_compliance_control_name">
    <td><CopyableCode code="regulatory_compliance_control_name" /></td>
    <td><code>string</code></td>
    <td>Name of the regulatory compliance control object. Required.</td>
</tr>
<tr id="parameter-regulatory_compliance_standard_name">
    <td><CopyableCode code="regulatory_compliance_standard_name" /></td>
    <td><code>string</code></td>
    <td>Name of the regulatory compliance standard object. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter. Optional. Default value is None.</td>
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

Selected regulatory compliance control details and state.

```sql
SELECT
id,
name,
description,
failedAssessments,
passedAssessments,
skippedAssessments,
state,
systemData,
type
FROM azure.security.regulatory_compliance_controls
WHERE regulatory_compliance_standard_name = '{{ regulatory_compliance_standard_name }}' -- required
AND regulatory_compliance_control_name = '{{ regulatory_compliance_control_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

All supported regulatory compliance controls details and state for selected standard.

```sql
SELECT
id,
name,
description,
failedAssessments,
passedAssessments,
skippedAssessments,
state,
systemData,
type
FROM azure.security.regulatory_compliance_controls
WHERE regulatory_compliance_standard_name = '{{ regulatory_compliance_standard_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
