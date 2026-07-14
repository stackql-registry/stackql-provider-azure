--- 
title: quota_by_period_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_by_period_keys
  - api_management
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

Creates, updates, deletes, gets or lists a <code>quota_by_period_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="quota_by_period_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.quota_by_period_keys" /></td></tr>
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
    <td><CopyableCode code="counterKey" /></td>
    <td><code>string</code></td>
    <td>The Key value of the Counter. Must not be empty. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="periodEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the end of Counter Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="periodKey" /></td>
    <td><code>string</code></td>
    <td>Identifier of the Period for which the counter was collected. Must not be empty. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="periodStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the start of Counter Period. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>object</code></td>
    <td>Quota Value Properties.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-quota_counter_key"><code>quota_counter_key</code></a>, <a href="#parameter-quota_period_key"><code>quota_period_key</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-quota_counter_key"><code>quota_counter_key</code></a>, <a href="#parameter-quota_period_key"><code>quota_period_key</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing quota counter value in the specified service instance.</td>
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
<tr id="parameter-quota_counter_key">
    <td><CopyableCode code="quota_counter_key" /></td>
    <td><code>string</code></td>
    <td>Quota counter key identifier. This is the result of expression defined in `counter-key` attribute of the quota-by-key policy. For example, if you specify `counter-key="boo"` in the policy, then it’s accessible by `"boo"` counter key. But if it’s defined as `counter-key="@("b"+"a")"` then it will be accessible by `"ba"` key. Required.</td>
</tr>
<tr id="parameter-quota_period_key">
    <td><CopyableCode code="quota_period_key" /></td>
    <td><code>string</code></td>
    <td>Quota period key identifier. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
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

Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance.

```sql
SELECT
counterKey,
periodEndTime,
periodKey,
periodStartTime,
value
FROM azure.api_management.quota_by_period_keys
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND quota_counter_key = '{{ quota_counter_key }}' -- required
AND quota_period_key = '{{ quota_period_key }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Updates an existing quota counter value in the specified service instance.

```sql
UPDATE azure.api_management.quota_by_period_keys
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND quota_counter_key = '{{ quota_counter_key }}' --required
AND quota_period_key = '{{ quota_period_key }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
counterKey,
periodEndTime,
periodKey,
periodStartTime,
value;
```
</TabItem>
</Tabs>
