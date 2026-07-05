--- 
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
  - subscription
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

Creates, updates, deletes, gets or lists a <code>subscription</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscription" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.subscription" /></td></tr>
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
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to cancel a subscription.</td>
</tr>
<tr>
    <td><a href="#rename"><CopyableCode code="rename" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to rename a subscription.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to enable a subscription.</td>
</tr>
<tr>
    <td><a href="#accept_ownership"><CopyableCode code="accept_ownership" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Accept subscription ownership.</td>
</tr>
<tr>
    <td><a href="#accept_ownership_status"><CopyableCode code="accept_ownership_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Accept subscription ownership status.</td>
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
    <td>Subscription Id. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'rename', value: 'rename' },
        { label: 'enable', value: 'enable' },
        { label: 'accept_ownership', value: 'accept_ownership' },
        { label: 'accept_ownership_status', value: 'accept_ownership_status' }
    ]}
>
<TabItem value="cancel">

The operation to cancel a subscription.

```sql
EXEC azure.subscription.subscription.cancel 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rename">

The operation to rename a subscription.

```sql
EXEC azure.subscription.subscription.rename 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"subscriptionName": "{{ subscriptionName }}"
}'
;
```
</TabItem>
<TabItem value="enable">

The operation to enable a subscription.

```sql
EXEC azure.subscription.subscription.enable 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="accept_ownership">

Accept subscription ownership.

```sql
EXEC azure.subscription.subscription.accept_ownership 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="accept_ownership_status">

Accept subscription ownership status.

```sql
EXEC azure.subscription.subscription.accept_ownership_status 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
