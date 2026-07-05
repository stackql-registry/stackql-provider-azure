--- 
title: policy_events
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_events
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

Creates, updates, deletes, gets or lists a <code>policy_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policyinsights.policy_events" /></td></tr>
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
    <td><a href="#list_query_results_for_management_group"><CopyableCode code="list_query_results_for_management_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-management_group_name"><code>management_group_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resources under the management group.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_subscription"><CopyableCode code="list_query_results_for_subscription" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resources under the subscription.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource_group"><CopyableCode code="list_query_results_for_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resources under the resource group.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource"><CopyableCode code="list_query_results_for_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resource.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_policy_set_definition"><CopyableCode code="list_query_results_for_policy_set_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_set_definition_name"><code>policy_set_definition_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the subscription level policy set definition.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_policy_definition"><CopyableCode code="list_query_results_for_policy_definition" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_definition_name"><code>policy_definition_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the subscription level policy definition.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_subscription_level_policy_assignment"><CopyableCode code="list_query_results_for_subscription_level_policy_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the subscription level policy assignment.</td>
</tr>
<tr>
    <td><a href="#list_query_results_for_resource_group_level_policy_assignment"><CopyableCode code="list_query_results_for_resource_group_level_policy_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_events_resource"><code>policy_events_resource</code></a>, <a href="#parameter-policy_assignment_name"><code>policy_assignment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$from"><code>$from</code></a>, <a href="#parameter-$to"><code>$to</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$apply"><code>$apply</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Queries policy events for the resource group level policy assignment.</td>
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
<tr id="parameter-policy_events_resource">
    <td><CopyableCode code="policy_events_resource" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual resource under PolicyEvents resource type; only "default" is allowed. "default" Required.</td>
</tr>
<tr id="parameter-policy_set_definition_name">
    <td><CopyableCode code="policy_set_definition_name" /></td>
    <td><code>string</code></td>
    <td>Policy set definition name. Required.</td>
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
    <td>The $expand query parameter. For example, to expand components use $expand=components. Default value is None.</td>
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
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only provided if a previous response returned a partial result as a part of nextLink element. Default value is None.</td>
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
    defaultValue="list_query_results_for_management_group"
    values={[
        { label: 'list_query_results_for_management_group', value: 'list_query_results_for_management_group' },
        { label: 'list_query_results_for_subscription', value: 'list_query_results_for_subscription' },
        { label: 'list_query_results_for_resource_group', value: 'list_query_results_for_resource_group' },
        { label: 'list_query_results_for_resource', value: 'list_query_results_for_resource' },
        { label: 'list_query_results_for_policy_set_definition', value: 'list_query_results_for_policy_set_definition' },
        { label: 'list_query_results_for_policy_definition', value: 'list_query_results_for_policy_definition' },
        { label: 'list_query_results_for_subscription_level_policy_assignment', value: 'list_query_results_for_subscription_level_policy_assignment' },
        { label: 'list_query_results_for_resource_group_level_policy_assignment', value: 'list_query_results_for_resource_group_level_policy_assignment' }
    ]}
>
<TabItem value="list_query_results_for_management_group">

Queries policy events for the resources under the management group.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_management_group 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@management_group_name='{{ management_group_name }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_subscription">

Queries policy events for the resources under the subscription.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_subscription 
@subscription_id='{{ subscription_id }}' --required, 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource_group">

Queries policy events for the resources under the resource group.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_resource_group 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource">

Queries policy events for the resource.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_resource 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@resource_id='{{ resource_id }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$expand='{{ $expand }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_policy_set_definition">

Queries policy events for the subscription level policy set definition.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_policy_set_definition 
@subscription_id='{{ subscription_id }}' --required, 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@policy_set_definition_name='{{ policy_set_definition_name }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_policy_definition">

Queries policy events for the subscription level policy definition.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_policy_definition 
@subscription_id='{{ subscription_id }}' --required, 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@policy_definition_name='{{ policy_definition_name }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_subscription_level_policy_assignment">

Queries policy events for the subscription level policy assignment.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_subscription_level_policy_assignment 
@subscription_id='{{ subscription_id }}' --required, 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@policy_assignment_name='{{ policy_assignment_name }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_query_results_for_resource_group_level_policy_assignment">

Queries policy events for the resource group level policy assignment.

```sql
EXEC azure.policyinsights.policy_events.list_query_results_for_resource_group_level_policy_assignment 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@policy_events_resource='{{ policy_events_resource }}' --required, 
@policy_assignment_name='{{ policy_assignment_name }}' --required, 
@$top='{{ $top }}', 
@$orderby='{{ $orderby }}', 
@$select='{{ $select }}', 
@$from='{{ $from }}', 
@$to='{{ $to }}', 
@$filter='{{ $filter }}', 
@$apply='{{ $apply }}', 
@$skiptoken='{{ $skiptoken }}'
;
```
</TabItem>
</Tabs>
