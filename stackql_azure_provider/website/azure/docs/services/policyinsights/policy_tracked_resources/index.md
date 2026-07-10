--- 
title: policy_tracked_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_tracked_resources
  - policyinsights
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

Creates, updates, deletes, gets or lists a <code>policy_tracked_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_tracked_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policyinsights.policy_tracked_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_query_results_for_resource_group"
    values={[
        { label: 'list_query_results_for_resource_group', value: 'list_query_results_for_resource_group' },
        { label: 'list_query_results_for_management_group', value: 'list_query_results_for_management_group' },
        { label: 'list_query_results_for_subscription', value: 'list_query_results_for_subscription' },
        { label: 'list_query_results_for_resource', value: 'list_query_results_for_resource' }
    ]}
>
<TabItem value="list_query_results_for_resource_group">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that created the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that modified the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last update to the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the policy that require the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="trackedResourceId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy tracked resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_management_group">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that created the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that modified the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last update to the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the policy that require the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="trackedResourceId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy tracked resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_subscription">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that created the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that modified the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last update to the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the policy that require the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="trackedResourceId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy tracked resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_query_results_for_resource">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that created the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The details of the policy triggered deployment that modified the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last update to the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policyDetails" /></td>
    <td><code>object</code></td>
    <td>The details of the policy that require the tracked resource.</td>
</tr>
<tr>
    <td><CopyableCode code="trackedResourceId" /></td>
    <td><code>string</code></td>
    <td>The ID of the policy tracked resource.</td>
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
    <td><a href="#list_query_results_for_resource_group"><CopyableCode code="list_query_results_for_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_tracked_resources_resource"><code>policy_tracked_resources_resource</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Queries policy tracked resources under the resource group.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_management_group"><CopyableCode code="list_query_results_for_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-policy_tracked_resources_resource"><code>policy_tracked_resources_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Queries policy tracked resources under the management group.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_subscription"><CopyableCode code="list_query_results_for_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_tracked_resources_resource"><code>policy_tracked_resources_resource</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Queries policy tracked resources under the subscription.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource"><CopyableCode code="list_query_results_for_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-policy_tracked_resources_resource"><code>policy_tracked_resources_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Queries policy tracked resources under the resource.</td>
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
<tr id="parameter-management_group_name">
    <td><CopyableCode code="management_group_name" /></td>
    <td><code>string</code></td>
    <td>Management group name. Required.</td>
</tr>
<tr id="parameter-policy_tracked_resources_resource">
    <td><CopyableCode code="policy_tracked_resources_resource" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual resource under PolicyTrackedResources resource type; only "default" is allowed. "default" Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Resource ID. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of records to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_query_results_for_resource_group"
    values={[
        { label: 'list_query_results_for_resource_group', value: 'list_query_results_for_resource_group' },
        { label: 'list_query_results_for_management_group', value: 'list_query_results_for_management_group' },
        { label: 'list_query_results_for_subscription', value: 'list_query_results_for_subscription' },
        { label: 'list_query_results_for_resource', value: 'list_query_results_for_resource' }
    ]}
>
<TabItem value="list_query_results_for_resource_group">

Queries policy tracked resources under the resource group.

```sql
SELECT
createdBy,
lastModifiedBy,
lastUpdateUtc,
policyDetails,
trackedResourceId
FROM azure.policyinsights.policy_tracked_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND policy_tracked_resources_resource = '{{ policy_tracked_resources_resource }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_management_group">

Queries policy tracked resources under the management group.

```sql
SELECT
createdBy,
lastModifiedBy,
lastUpdateUtc,
policyDetails,
trackedResourceId
FROM azure.policyinsights.policy_tracked_resources
WHERE management_group_name = '{{ management_group_name }}' -- required
AND policy_tracked_resources_resource = '{{ policy_tracked_resources_resource }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_subscription">

Queries policy tracked resources under the subscription.

```sql
SELECT
createdBy,
lastModifiedBy,
lastUpdateUtc,
policyDetails,
trackedResourceId
FROM azure.policyinsights.policy_tracked_resources
WHERE policy_tracked_resources_resource = '{{ policy_tracked_resources_resource }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource">

Queries policy tracked resources under the resource.

```sql
SELECT
createdBy,
lastModifiedBy,
lastUpdateUtc,
policyDetails,
trackedResourceId
FROM azure.policyinsights.policy_tracked_resources
WHERE resource_id = '{{ resource_id }}' -- required
AND policy_tracked_resources_resource = '{{ policy_tracked_resources_resource }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
