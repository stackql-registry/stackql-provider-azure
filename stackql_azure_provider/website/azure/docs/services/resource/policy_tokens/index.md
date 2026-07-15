--- 
title: policy_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_tokens
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

Creates, updates, deletes, gets or lists a <code>policy_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_tokens" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.policy_tokens" /></td></tr>
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
    <td><a href="#acquire"><CopyableCode code="acquire" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-operation"><code>operation</code></a></td>
    <td></td>
    <td>Acquires a policy token. This operation acquires a policy token in the given subscription for the given request body.</td>
</tr>
<tr>
    <td><a href="#acquire_at_management_group"><CopyableCode code="acquire_at_management_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_name"><code>management_group_name</code></a>, <a href="#parameter-operation"><code>operation</code></a></td>
    <td></td>
    <td>Acquires a policy token at management group level. This operation acquires a policy token in the given management group for the given request body.</td>
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
    <td>The name of the management group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="acquire"
    values={[
        { label: 'acquire', value: 'acquire' },
        { label: 'acquire_at_management_group', value: 'acquire_at_management_group' }
    ]}
>
<TabItem value="acquire">

Acquires a policy token. This operation acquires a policy token in the given subscription for the given request body.

```sql
EXEC azure.resource.policy_tokens.acquire 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"operation": "{{ operation }}", 
"changeReference": "{{ changeReference }}"
}'
;
```
</TabItem>
<TabItem value="acquire_at_management_group">

Acquires a policy token at management group level. This operation acquires a policy token in the given management group for the given request body.

```sql
EXEC azure.resource.policy_tokens.acquire_at_management_group 
@management_group_name='{{ management_group_name }}' --required 
@@json=
'{
"operation": "{{ operation }}", 
"changeReference": "{{ changeReference }}"
}'
;
```
</TabItem>
</Tabs>
