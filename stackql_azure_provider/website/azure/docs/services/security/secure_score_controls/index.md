--- 
title: secure_score_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - secure_score_controls
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

Creates, updates, deletes, gets or lists a <code>secure_score_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secure_score_controls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.secure_score_controls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_secure_score"
    values={[
        { label: 'list_by_secure_score', value: 'list_by_secure_score' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_secure_score">

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
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Information about the security control.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the control.</td>
</tr>
<tr>
    <td><CopyableCode code="healthyResourceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of healthy resources in the control.</td>
</tr>
<tr>
    <td><CopyableCode code="notApplicableResourceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of not applicable resources in the control.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>object</code></td>
    <td>Actual score object for the control.</td>
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
    <td><CopyableCode code="unhealthyResourceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of unhealthy resources in the control.</td>
</tr>
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>The relative weight for this specific control in each of your subscriptions. Used when calculating an aggregated score for this control across all of your subscriptions.</td>
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
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Information about the security control.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the control.</td>
</tr>
<tr>
    <td><CopyableCode code="healthyResourceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of healthy resources in the control.</td>
</tr>
<tr>
    <td><CopyableCode code="notApplicableResourceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of not applicable resources in the control.</td>
</tr>
<tr>
    <td><CopyableCode code="score" /></td>
    <td><code>object</code></td>
    <td>Actual score object for the control.</td>
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
    <td><CopyableCode code="unhealthyResourceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of unhealthy resources in the control.</td>
</tr>
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>The relative weight for this specific control in each of your subscriptions. Used when calculating an aggregated score for this control across all of your subscriptions.</td>
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
    <td><a href="#list_by_secure_score"><CopyableCode code="list_by_secure_score" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-secure_score_name"><code>secure_score_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get all security controls for a specific initiative within a scope.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get all security controls within a scope.</td>
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
<tr id="parameter-secure_score_name">
    <td><CopyableCode code="secure_score_name" /></td>
    <td><code>string</code></td>
    <td>The initiative name. For the ASC Default initiative, use 'ascScore' as in the sample request below. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>OData expand. Optional. "definition" Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_secure_score"
    values={[
        { label: 'list_by_secure_score', value: 'list_by_secure_score' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_secure_score">

Get all security controls for a specific initiative within a scope.

```sql
SELECT
id,
name,
definition,
displayName,
healthyResourceCount,
notApplicableResourceCount,
score,
systemData,
type,
unhealthyResourceCount,
weight
FROM azure.security.secure_score_controls
WHERE secure_score_name = '{{ secure_score_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get all security controls within a scope.

```sql
SELECT
id,
name,
definition,
displayName,
healthyResourceCount,
notApplicableResourceCount,
score,
systemData,
type,
unhealthyResourceCount,
weight
FROM azure.security.secure_score_controls
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
