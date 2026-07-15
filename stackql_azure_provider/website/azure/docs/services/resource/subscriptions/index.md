--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - resource
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.subscriptions" /></td></tr>
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
    <td>The fully qualified ID for the subscription. For example, /subscriptions/8d65815f-a5b6-402f-9298-045155da7d74.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationSource" /></td>
    <td><code>string</code></td>
    <td>The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy, RoleBased'.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The subscription display name.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByTenants" /></td>
    <td><code>array</code></td>
    <td>An array containing the tenants managing the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted. Known values are: "Enabled", "Warned", "PastDue", "Disabled", and "Deleted". (Enabled, Warned, PastDue, Disabled, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionPolicies" /></td>
    <td><code>object</code></td>
    <td>The subscription policies.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags attached to the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The subscription tenant ID.</td>
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
    <td>The fully qualified ID for the subscription. For example, /subscriptions/8d65815f-a5b6-402f-9298-045155da7d74.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationSource" /></td>
    <td><code>string</code></td>
    <td>The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy, RoleBased'.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The subscription display name.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByTenants" /></td>
    <td><code>array</code></td>
    <td>An array containing the tenants managing the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted. Known values are: "Enabled", "Warned", "PastDue", "Disabled", and "Deleted". (Enabled, Warned, PastDue, Disabled, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscription ID.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionPolicies" /></td>
    <td><code>object</code></td>
    <td>The subscription policies.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags attached to the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The subscription tenant ID.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details about a specified subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets all subscriptions for a tenant.</td>
</tr>
<tr>
    <td><a href="#list_locations"><CopyableCode code="list_locations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-includeExtendedLocations"><code>includeExtendedLocations</code></a></td>
    <td>Gets all available geo-locations. This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list.</td>
</tr>
<tr>
    <td><a href="#check_zone_peers"><CopyableCode code="check_zone_peers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Compares a subscriptions logical zone mapping.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the target subscription. The value must be an UUID. Required.</td>
</tr>
<tr id="parameter-includeExtendedLocations">
    <td><CopyableCode code="includeExtendedLocations" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include extended locations. Default value is None.</td>
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

Gets details about a specified subscription.

```sql
SELECT
id,
authorizationSource,
displayName,
managedByTenants,
state,
subscriptionId,
subscriptionPolicies,
tags,
tenantId
FROM azure.resource.subscriptions
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all subscriptions for a tenant.

```sql
SELECT
id,
authorizationSource,
displayName,
managedByTenants,
state,
subscriptionId,
subscriptionPolicies,
tags,
tenantId
FROM azure.resource.subscriptions
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_locations"
    values={[
        { label: 'list_locations', value: 'list_locations' },
        { label: 'check_zone_peers', value: 'check_zone_peers' }
    ]}
>
<TabItem value="list_locations">

Gets all available geo-locations. This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list.

```sql
EXEC azure.resource.subscriptions.list_locations 
@subscription_id='{{ subscription_id }}' --required, 
@includeExtendedLocations={{ includeExtendedLocations }}
;
```
</TabItem>
<TabItem value="check_zone_peers">

Compares a subscriptions logical zone mapping.

```sql
EXEC azure.resource.subscriptions.check_zone_peers 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"subscriptionIds": "{{ subscriptionIds }}"
}'
;
```
</TabItem>
</Tabs>
