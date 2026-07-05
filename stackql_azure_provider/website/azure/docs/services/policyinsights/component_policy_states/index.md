--- 
title: component_policy_states
hide_title: false
hide_table_of_contents: false
keywords:
  - component_policy_states
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

Creates, updates, deletes, gets or lists a <code>component_policy_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="component_policy_states" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policyinsights.component_policy_states" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#list_query_results_for_subscription"><CopyableCode code="list_query_results_for_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-component_policy_states_resource"><code>component_policy_states_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a></td>
    <td>Queries component policy states under subscription scope.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource_group"><CopyableCode code="list_query_results_for_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-component_policy_states_resource"><code>component_policy_states_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a></td>
    <td>Queries component policy states under resource group scope.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource"><CopyableCode code="list_query_results_for_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-component_policy_states_resource"><code>component_policy_states_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Queries component policy states for the resource.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_policy_definition"><CopyableCode code="list_query_results_for_policy_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a>, <a href="#parameter-component_policy_states_resource"><code>component_policy_states_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a></td>
    <td>Queries component policy states for the subscription level policy definition.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_subscription_level_policy_assignment"><CopyableCode code="list_query_results_for_subscription_level_policy_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a>, <a href="#parameter-component_policy_states_resource"><code>component_policy_states_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a></td>
    <td>Queries component policy states for the subscription level policy assignment.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource_group_level_policy_assignment"><CopyableCode code="list_query_results_for_resource_group_level_policy_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a>, <a href="#parameter-component_policy_states_resource"><code>component_policy_states_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a></td>
    <td>Queries component policy states for the resource group level policy assignment.</td>
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
<tr id="parameter-component_policy_states_resource">
    <td><CopyableCode code="component_policy_states_resource" /></td>
    <td><code>string</code></td>
    <td>The virtual resource under ComponentPolicyStates resource type. In a given time range, 'latest' represents the latest component policy state(s). "latest" Required.</td>
</tr>
<tr id="parameter-policy_assignment_name">
    <td><CopyableCode code="policy_assignment_name" /></td>
    <td><code>string</code></td>
    <td>Policy assignment name. Required.</td>
</tr>
<tr id="parameter-policy_definition_name">
    <td><CopyableCode code="policy_definition_name" /></td>
    <td><code>string</code></td>
    <td>Policy definition name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Resource group name. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Resource ID. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the target subscription. The value must be an UUID. Required.</td>
</tr>
<tr id="parameter-$apply">
    <td><CopyableCode code="$apply" /></td>
    <td><code>string</code></td>
    <td>OData apply expression for aggregations. Default value is None.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The $expand query parameter. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Default value is None.</td>
</tr>
<tr id="parameter-$from">
    <td><CopyableCode code="$from" /></td>
    <td><code>string (date-time)</code></td>
    <td>ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Ordering expression using OData notation. One or more comma-separated column names with an optional "desc" (the default) or "asc", e.g. "$orderby=PolicyAssignmentId, ResourceId asc". Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>Select expression using OData notation. Limits the columns on each record to just those requested, e.g. "$select=PolicyAssignmentId, ResourceId". Default value is None.</td>
</tr>
<tr id="parameter-$to">
    <td><CopyableCode code="$to" /></td>
    <td><code>string (date-time)</code></td>
    <td>ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of records to return. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_query_results_for_subscription"
    values={[
        { label: 'list_query_results_for_subscription', value: 'list_query_results_for_subscription' },
        { label: 'list_query_results_for_resource_group', value: 'list_query_results_for_resource_group' },
        { label: 'list_query_results_for_resource', value: 'list_query_results_for_resource' },
        { label: 'list_query_results_for_policy_definition', value: 'list_query_results_for_policy_definition' },
        { label: 'list_query_results_for_subscription_level_policy_assignment', value: 'list_query_results_for_subscription_level_policy_assignment' },
        { label: 'list_query_results_for_resource_group_level_policy_assignment', value: 'list_query_results_for_resource_group_level_policy_assignment' }
    ]}
>
<TabItem value="list_query_results_for_subscription">

Queries component policy states under subscription scope.

```sql
EXEC azure.policyinsights.component_policy_states.list_query_results_for_subscription 
@subscription_id='{{ subscription_id }}' --required, 
@component_policy_states_resource='{{ component_policy_states_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource_group">

Queries component policy states under resource group scope.

```sql
EXEC azure.policyinsights.component_policy_states.list_query_results_for_resource_group 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@component_policy_states_resource='{{ component_policy_states_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource">

Queries component policy states for the resource.

```sql
EXEC azure.policyinsights.component_policy_states.list_query_results_for_resource 
@resource_id='{{ resource_id }}' --required, 
@component_policy_states_resource='{{ component_policy_states_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_policy_definition">

Queries component policy states for the subscription level policy definition.

```sql
EXEC azure.policyinsights.component_policy_states.list_query_results_for_policy_definition 
@subscription_id='{{ subscription_id }}' --required, 
@policy_definition_name='{{ policy_definition_name }}' --required, 
@component_policy_states_resource='{{ component_policy_states_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_subscription_level_policy_assignment">

Queries component policy states for the subscription level policy assignment.

```sql
EXEC azure.policyinsights.component_policy_states.list_query_results_for_subscription_level_policy_assignment 
@subscription_id='{{ subscription_id }}' --required, 
@policy_assignment_name='{{ policy_assignment_name }}' --required, 
@component_policy_states_resource='{{ component_policy_states_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource_group_level_policy_assignment">

Queries component policy states for the resource group level policy assignment.

```sql
EXEC azure.policyinsights.component_policy_states.list_query_results_for_resource_group_level_policy_assignment 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@policy_assignment_name='{{ policy_assignment_name }}' --required, 
@component_policy_states_resource='{{ component_policy_states_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}'
;
```
</TabItem>
</Tabs>
