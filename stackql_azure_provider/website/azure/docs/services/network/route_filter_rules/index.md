--- 
title: route_filter_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filter_rules
  - network
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

Creates, updates, deletes, gets or lists a <code>route_filter_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="route_filter_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_filter_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_route_filter', value: 'list_by_route_filter' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="access" /></td>
    <td><code>string</code></td>
    <td>The access type of the rule. Required. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="communities" /></td>
    <td><code>array</code></td>
    <td>The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route filter rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routeFilterRuleType" /></td>
    <td><code>string</code></td>
    <td>The rule type of the rule. Required. "Community" (Community)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_route_filter">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="access" /></td>
    <td><code>string</code></td>
    <td>The access type of the rule. Required. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="communities" /></td>
    <td><code>array</code></td>
    <td>The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020']. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the route filter rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="routeFilterRuleType" /></td>
    <td><code>string</code></td>
    <td>The rule type of the rule. Required. "Community" (Community)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_filter_name"><code>route_filter_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified rule from a route filter.</td>
</tr>
<tr>
    <td><a href="#list_by_route_filter"><CopyableCode code="list_by_route_filter" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_filter_name"><code>route_filter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all RouteFilterRules in a route filter.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_filter_name"><code>route_filter_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a route in the specified route filter.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_filter_name"><code>route_filter_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a route in the specified route filter.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-route_filter_name"><code>route_filter_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified rule from a route filter.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-route_filter_name">
    <td><CopyableCode code="route_filter_name" /></td>
    <td><code>string</code></td>
    <td>The name of the route filter. Required.</td>
</tr>
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the route filter rule. Required.</td>
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
        { label: 'list_by_route_filter', value: 'list_by_route_filter' }
    ]}
>
<TabItem value="get">

Gets the specified rule from a route filter.

```sql
SELECT
id,
name,
access,
communities,
etag,
location,
provisioningState,
routeFilterRuleType
FROM azure.network.route_filter_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND route_filter_name = '{{ route_filter_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_route_filter">

Gets all RouteFilterRules in a route filter.

```sql
SELECT
id,
name,
access,
communities,
etag,
location,
provisioningState,
routeFilterRuleType
FROM azure.network.route_filter_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND route_filter_name = '{{ route_filter_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a route in the specified route filter.

```sql
INSERT INTO azure.network.route_filter_rules (
id,
properties,
name,
location,
resource_group_name,
route_filter_name,
rule_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ route_filter_name }}',
'{{ rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: route_filter_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the route_filter_rules resource.
    - name: route_filter_name
      value: "{{ route_filter_name }}"
      description: Required parameter for the route_filter_rules resource.
    - name: rule_name
      value: "{{ rule_name }}"
      description: Required parameter for the route_filter_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the route_filter_rules resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: properties
      description: |
        Properties of the route filter rule.
      value:
        access: "{{ access }}"
        routeFilterRuleType: "{{ routeFilterRuleType }}"
        communities:
          - "{{ communities }}"
        provisioningState: "{{ provisioningState }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a route in the specified route filter.

```sql
REPLACE azure.network.route_filter_rules
SET 
id = '{{ id }}',
properties = '{{ properties }}',
name = '{{ name }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND route_filter_name = '{{ route_filter_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties;
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

Deletes the specified rule from a route filter.

```sql
DELETE FROM azure.network.route_filter_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND route_filter_name = '{{ route_filter_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
