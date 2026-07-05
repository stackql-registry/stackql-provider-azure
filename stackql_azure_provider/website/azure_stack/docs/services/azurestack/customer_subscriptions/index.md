--- 
title: customer_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_subscriptions
  - azurestack
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>customer_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="customer_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azurestack.customer_subscriptions" /></td></tr>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-customer_subscription_name"><code>customer_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified product.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of products.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-customer_subscription_name"><code>customer_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new customer subscription under a registration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-registration_name"><code>registration_name</code></a>, <a href="#parameter-customer_subscription_name"><code>customer_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a customer subscription under a registration.</td>
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
<tr id="parameter-customer_subscription_name">
    <td><CopyableCode code="customer_subscription_name" /></td>
    <td><code>string</code></td>
    <td>Name of the product. Required.</td>
</tr>
<tr id="parameter-registration_name">
    <td><CopyableCode code="registration_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Stack registration. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns the specified product.

```sql
SELECT
id,
name,
etag,
systemData,
tenantId,
type
FROM azure_stack.azurestack.customer_subscriptions
WHERE resource_group = '{{ resource_group }}' -- required
AND registration_name = '{{ registration_name }}' -- required
AND customer_subscription_name = '{{ customer_subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of products.

```sql
SELECT
id,
name,
etag,
systemData,
tenantId,
type
FROM azure_stack.azurestack.customer_subscriptions
WHERE resource_group = '{{ resource_group }}' -- required
AND registration_name = '{{ registration_name }}' -- required
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

Creates a new customer subscription under a registration.

```sql
INSERT INTO azure_stack.azurestack.customer_subscriptions (
etag,
properties,
resource_group,
registration_name,
customer_subscription_name,
subscription_id
)
SELECT 
'{{ etag }}',
'{{ properties }}',
'{{ resource_group }}',
'{{ registration_name }}',
'{{ customer_subscription_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: customer_subscriptions
  props:
    - name: resource_group
      value: "{{ resource_group }}"
      description: Required parameter for the customer_subscriptions resource.
    - name: registration_name
      value: "{{ registration_name }}"
      description: Required parameter for the customer_subscriptions resource.
    - name: customer_subscription_name
      value: "{{ customer_subscription_name }}"
      description: Required parameter for the customer_subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the customer_subscriptions resource.
    - name: etag
      value: "{{ etag }}"
      description: |
        The entity tag used for optimistic concurrency when modifying the resource.
    - name: properties
      value:
        tenantId: "{{ tenantId }}"
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

Deletes a customer subscription under a registration.

```sql
DELETE FROM azure_stack.azurestack.customer_subscriptions
WHERE resource_group = '{{ resource_group }}' --required
AND registration_name = '{{ registration_name }}' --required
AND customer_subscription_name = '{{ customer_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
