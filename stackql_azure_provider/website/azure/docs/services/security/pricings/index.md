--- 
title: pricings
hide_title: false
hide_table_of_contents: false
keywords:
  - pricings
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

Creates, updates, deletes, gets or lists a <code>pricings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pricings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.pricings" /></td></tr>
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
    <td><CopyableCode code="deprecated" /></td>
    <td><code>boolean</code></td>
    <td>Optional. True if the plan is deprecated. If there are replacing plans they will appear in `replacedBy` property.</td>
</tr>
<tr>
    <td><CopyableCode code="enablementTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Optional. If `pricingTier` is `Standard` then this property holds the date of the last time the `pricingTier` was set to `Standard`, when available (e.g 2023-03-01T12:42:42.1921106Z).</td>
</tr>
<tr>
    <td><CopyableCode code="enforce" /></td>
    <td><code>string</code></td>
    <td>If set to "False", it allows the descendants of this scope to override the pricing configuration set on this scope (allows setting inherited="False"). If set to "True", it prevents overrides and forces this pricing configuration on all the descendants of this scope. This field is only available for subscription-level pricing. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Optional. List of extensions offered under a plan.</td>
</tr>
<tr>
    <td><CopyableCode code="freeTrialRemainingTime" /></td>
    <td><code>string</code></td>
    <td>The duration left for the subscriptions free trial period - in ISO 8601 format (e.g. P3Y6M4DT12H30M5S).</td>
</tr>
<tr>
    <td><CopyableCode code="inherited" /></td>
    <td><code>string</code></td>
    <td>"inherited" = "True" indicates that the current scope inherits its pricing configuration from its parent. The ID of the parent scope that provides the inherited configuration is displayed in the "inheritedFrom" field. On the other hand, "inherited" = "False" indicates that the current scope has its own pricing configuration explicitly set, and does not inherit from its parent. This field is read only and available only for resource-level pricing. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="inheritedFrom" /></td>
    <td><code>string</code></td>
    <td>The id of the scope inherited from. "Null" if not inherited. This field is only available for resource-level pricing.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingTier" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the Defender plan is enabled on the selected scope. Microsoft Defender for Cloud is provided in two pricing tiers: free and standard. The standard tier offers advanced security capabilities, while the free tier offers basic security features. Required. Known values are: "Free" and "Standard". (Free, Standard)</td>
</tr>
<tr>
    <td><CopyableCode code="replacedBy" /></td>
    <td><code>array</code></td>
    <td>Optional. List of plans that replace this plan. This property exists only if this plan is deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcesCoverageStatus" /></td>
    <td><code>string</code></td>
    <td>This field is available for subscription-level only, and reflects the coverage status of the resources under the subscription. Please note: The "pricingTier" field reflects the plan status of the subscription. However, since the plan status can also be defined at the resource level, there might be misalignment between the subscription's plan status and the resource status. This field helps indicate the coverage status of the resources. Known values are: "FullyCovered", "PartiallyCovered", and "NotCovered". (FullyCovered, PartiallyCovered, NotCovered)</td>
</tr>
<tr>
    <td><CopyableCode code="subPlan" /></td>
    <td><code>string</code></td>
    <td>The sub-plan selected for a Standard pricing configuration, when more than one sub-plan is available. Each sub-plan enables a set of security features. When not specified, full plan is applied. For VirtualMachines plan, available sub plans are 'P1' & 'P2', where for resource level only 'P1' sub plan is supported.</td>
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
    <td><CopyableCode code="deprecated" /></td>
    <td><code>boolean</code></td>
    <td>Optional. True if the plan is deprecated. If there are replacing plans they will appear in `replacedBy` property.</td>
</tr>
<tr>
    <td><CopyableCode code="enablementTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Optional. If `pricingTier` is `Standard` then this property holds the date of the last time the `pricingTier` was set to `Standard`, when available (e.g 2023-03-01T12:42:42.1921106Z).</td>
</tr>
<tr>
    <td><CopyableCode code="enforce" /></td>
    <td><code>string</code></td>
    <td>If set to "False", it allows the descendants of this scope to override the pricing configuration set on this scope (allows setting inherited="False"). If set to "True", it prevents overrides and forces this pricing configuration on all the descendants of this scope. This field is only available for subscription-level pricing. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Optional. List of extensions offered under a plan.</td>
</tr>
<tr>
    <td><CopyableCode code="freeTrialRemainingTime" /></td>
    <td><code>string</code></td>
    <td>The duration left for the subscriptions free trial period - in ISO 8601 format (e.g. P3Y6M4DT12H30M5S).</td>
</tr>
<tr>
    <td><CopyableCode code="inherited" /></td>
    <td><code>string</code></td>
    <td>"inherited" = "True" indicates that the current scope inherits its pricing configuration from its parent. The ID of the parent scope that provides the inherited configuration is displayed in the "inheritedFrom" field. On the other hand, "inherited" = "False" indicates that the current scope has its own pricing configuration explicitly set, and does not inherit from its parent. This field is read only and available only for resource-level pricing. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="inheritedFrom" /></td>
    <td><code>string</code></td>
    <td>The id of the scope inherited from. "Null" if not inherited. This field is only available for resource-level pricing.</td>
</tr>
<tr>
    <td><CopyableCode code="pricingTier" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the Defender plan is enabled on the selected scope. Microsoft Defender for Cloud is provided in two pricing tiers: free and standard. The standard tier offers advanced security capabilities, while the free tier offers basic security features. Required. Known values are: "Free" and "Standard". (Free, Standard)</td>
</tr>
<tr>
    <td><CopyableCode code="replacedBy" /></td>
    <td><code>array</code></td>
    <td>Optional. List of plans that replace this plan. This property exists only if this plan is deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="resourcesCoverageStatus" /></td>
    <td><code>string</code></td>
    <td>This field is available for subscription-level only, and reflects the coverage status of the resources under the subscription. Please note: The "pricingTier" field reflects the plan status of the subscription. However, since the plan status can also be defined at the resource level, there might be misalignment between the subscription's plan status and the resource status. This field helps indicate the coverage status of the resources. Known values are: "FullyCovered", "PartiallyCovered", and "NotCovered". (FullyCovered, PartiallyCovered, NotCovered)</td>
</tr>
<tr>
    <td><CopyableCode code="subPlan" /></td>
    <td><code>string</code></td>
    <td>The sub-plan selected for a Standard pricing configuration, when more than one sub-plan is available. Each sub-plan enables a set of security features. When not specified, full plan is applied. For VirtualMachines plan, available sub plans are 'P1' & 'P2', where for resource level only 'P1' sub plan is supported.</td>
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
    <td><a href="#parameter-scope_id"><code>scope_id</code></a>, <a href="#parameter-pricing_name"><code>pricing_name</code></a></td>
    <td></td>
    <td>Get the Defender plans pricing configurations of the selected scope (valid scopes are resource id or a subscription id). At the resource level, supported resource types are 'VirtualMachines, VMSS and ARC Machines'.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope_id"><code>scope_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists Microsoft Defender for Cloud pricing configurations of the scopeId, that match the optional given $filter. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines'). Valid $filter is: 'name in (&#123;planName1&#125;,&#123;planName2&#125;,...)'. If $filter is not provided, the unfiltered list will be returned. If '$filter=name in (planName1,planName2)' is provided, the returned list includes the pricings set for 'planName1' and 'planName2' only.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope_id"><code>scope_id</code></a>, <a href="#parameter-pricing_name"><code>pricing_name</code></a></td>
    <td></td>
    <td>Updates a provided Microsoft Defender for Cloud pricing configuration in the scope. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines' and only for plan='VirtualMachines' and subPlan='P1').</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope_id"><code>scope_id</code></a>, <a href="#parameter-pricing_name"><code>pricing_name</code></a></td>
    <td></td>
    <td>Deletes a provided Microsoft Defender for Cloud pricing configuration in a specific resource. Valid only for resource scope (Supported resources are: 'VirtualMachines, VMSS, ARC Machines, and Containers').</td>
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
<tr id="parameter-pricing_name">
    <td><CopyableCode code="pricing_name" /></td>
    <td><code>string</code></td>
    <td>name of the pricing configuration. Required.</td>
</tr>
<tr id="parameter-scope_id">
    <td><CopyableCode code="scope_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
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

Get the Defender plans pricing configurations of the selected scope (valid scopes are resource id or a subscription id). At the resource level, supported resource types are 'VirtualMachines, VMSS and ARC Machines'.

```sql
SELECT
id,
name,
deprecated,
enablementTime,
enforce,
extensions,
freeTrialRemainingTime,
inherited,
inheritedFrom,
pricingTier,
replacedBy,
resourcesCoverageStatus,
subPlan,
systemData,
type
FROM azure.security.pricings
WHERE scope_id = '{{ scope_id }}' -- required
AND pricing_name = '{{ pricing_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Microsoft Defender for Cloud pricing configurations of the scopeId, that match the optional given $filter. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines'). Valid $filter is: 'name in (&#123;planName1&#125;,&#123;planName2&#125;,...)'. If $filter is not provided, the unfiltered list will be returned. If '$filter=name in (planName1,planName2)' is provided, the returned list includes the pricings set for 'planName1' and 'planName2' only.

```sql
SELECT
id,
name,
deprecated,
enablementTime,
enforce,
extensions,
freeTrialRemainingTime,
inherited,
inheritedFrom,
pricingTier,
replacedBy,
resourcesCoverageStatus,
subPlan,
systemData,
type
FROM azure.security.pricings
WHERE scope_id = '{{ scope_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a provided Microsoft Defender for Cloud pricing configuration in the scope. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines' and only for plan='VirtualMachines' and subPlan='P1').

```sql
UPDATE azure.security.pricings
SET 
properties = '{{ properties }}'
WHERE 
scope_id = '{{ scope_id }}' --required
AND pricing_name = '{{ pricing_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
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

Deletes a provided Microsoft Defender for Cloud pricing configuration in a specific resource. Valid only for resource scope (Supported resources are: 'VirtualMachines, VMSS, ARC Machines, and Containers').

```sql
DELETE FROM azure.security.pricings
WHERE scope_id = '{{ scope_id }}' --required
AND pricing_name = '{{ pricing_name }}' --required
;
```
</TabItem>
</Tabs>
