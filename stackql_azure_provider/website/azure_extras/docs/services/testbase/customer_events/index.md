--- 
title: customer_events
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_events
  - testbase
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>customer_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="customer_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.testbase.customer_events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_test_base_account', value: 'list_by_test_base_account' }
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
    <td><CopyableCode code="eventName" /></td>
    <td><code>string</code></td>
    <td>The name of the event subscribed to.</td>
</tr>
<tr>
    <td><CopyableCode code="receivers" /></td>
    <td><code>array</code></td>
    <td>The notification event receivers.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_test_base_account">

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
    <td><CopyableCode code="eventName" /></td>
    <td><code>string</code></td>
    <td>The name of the event subscribed to.</td>
</tr>
<tr>
    <td><CopyableCode code="receivers" /></td>
    <td><code>array</code></td>
    <td>The notification event receivers.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-customer_event_name"><code>customer_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Test Base CustomerEvent.</td>
</tr>
<tr>
    <td><a href="#list_by_test_base_account"><CopyableCode code="list_by_test_base_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all notification events subscribed under a Test Base Account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-customer_event_name"><code>customer_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace a Test Base Customer Event.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-test_base_account_name"><code>test_base_account_name</code></a>, <a href="#parameter-customer_event_name"><code>customer_event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Test Base Customer Event.</td>
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
<tr id="parameter-customer_event_name">
    <td><CopyableCode code="customer_event_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Customer event. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-test_base_account_name">
    <td><CopyableCode code="test_base_account_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the Test Base Account. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_test_base_account', value: 'list_by_test_base_account' }
    ]}
>
<TabItem value="get">

Gets a Test Base CustomerEvent.

```sql
SELECT
id,
name,
eventName,
receivers,
systemData,
type
FROM azure_extras.testbase.customer_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND customer_event_name = '{{ customer_event_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_test_base_account">

Lists all notification events subscribed under a Test Base Account.

```sql
SELECT
id,
name,
eventName,
receivers,
systemData,
type
FROM azure_extras.testbase.customer_events
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND test_base_account_name = '{{ test_base_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create or replace a Test Base Customer Event.

```sql
INSERT INTO azure_extras.testbase.customer_events (
properties,
resource_group_name,
test_base_account_name,
customer_event_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ test_base_account_name }}',
'{{ customer_event_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: customer_events
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the customer_events resource.
    - name: test_base_account_name
      value: "{{ test_base_account_name }}"
      description: Required parameter for the customer_events resource.
    - name: customer_event_name
      value: "{{ customer_event_name }}"
      description: Required parameter for the customer_events resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the customer_events resource.
    - name: properties
      value:
        eventName: "{{ eventName }}"
        receivers:
          - receiverType: "{{ receiverType }}"
            receiverValue:
              userObjectReceiverValue:
                userObjectIds:
                  - "{{ userObjectIds }}"
              subscriptionReceiverValue:
                subscriptionId: "{{ subscriptionId }}"
                subscriptionName: "{{ subscriptionName }}"
                role: "{{ role }}"
              distributionGroupListReceiverValue:
                distributionGroups:
                  - "{{ distributionGroups }}"
`}</CodeBlock>

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

Deletes a Test Base Customer Event.

```sql
DELETE FROM azure_extras.testbase.customer_events
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND test_base_account_name = '{{ test_base_account_name }}' --required
AND customer_event_name = '{{ customer_event_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
