--- 
title: firewall_policy_idps_signatures_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures_overrides
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_idps_signatures_overrides</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_policy_idps_signatures_overrides" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_idps_signatures_overrides" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="signatures" /></td>
    <td><code>object</code></td>
    <td>Dictionary of .</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all signatures overrides for a specific policy.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Will override/create a new signature overrides for the policy's IDPS.</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Will update the status of policy's signature overrides for IDPS.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all signatures overrides objects for a specific policy as a list containing a single value.</td>
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
<tr id="parameter-firewall_policy_name">
    <td><CopyableCode code="firewall_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Firewall Policy. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns all signatures overrides for a specific policy.

```sql
SELECT
id,
name,
signatures,
type
FROM azure.network.firewall_policy_idps_signatures_overrides
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND firewall_policy_name = '{{ firewall_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' },
        { label: 'patch', value: 'patch' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="put">

Will override/create a new signature overrides for the policy's IDPS.

```sql
EXEC azure.network.firewall_policy_idps_signatures_overrides.put 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_policy_name='{{ firewall_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"name": "{{ name }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="patch">

Will update the status of policy's signature overrides for IDPS.

```sql
EXEC azure.network.firewall_policy_idps_signatures_overrides.patch 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_policy_name='{{ firewall_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"name": "{{ name }}", 
"type": "{{ type }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="list_raw">

Returns all signatures overrides objects for a specific policy as a list containing a single value.

```sql
EXEC azure.network.firewall_policy_idps_signatures_overrides.list_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@firewall_policy_name='{{ firewall_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
