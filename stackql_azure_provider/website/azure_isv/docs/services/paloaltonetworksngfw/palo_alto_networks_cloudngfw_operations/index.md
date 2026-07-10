--- 
title: palo_alto_networks_cloudngfw_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - palo_alto_networks_cloudngfw_operations
  - paloaltonetworksngfw
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>palo_alto_networks_cloudngfw_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="palo_alto_networks_cloudngfw_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworksngfw.palo_alto_networks_cloudngfw_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_cloud_manager_tenants"
    values={[
        { label: 'list_cloud_manager_tenants', value: 'list_cloud_manager_tenants' }
    ]}
>
<TabItem value="list_cloud_manager_tenants">

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
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>List of Cloud Manager Tenants. Required.</td>
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
    <td><a href="#list_cloud_manager_tenants"><CopyableCode code="list_cloud_manager_tenants" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>list_cloud_manager_tenants.</td>
</tr>
<tr>
    <td><a href="#list_product_serial_number_status"><CopyableCode code="list_product_serial_number_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>list_product_serial_number_status.</td>
</tr>
<tr>
    <td><a href="#list_support_info"><CopyableCode code="list_support_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>list_support_info.</td>
</tr>
<tr>
    <td><a href="#create_product_serial_number"><CopyableCode code="create_product_serial_number" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>create_product_serial_number.</td>
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
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_cloud_manager_tenants"
    values={[
        { label: 'list_cloud_manager_tenants', value: 'list_cloud_manager_tenants' }
    ]}
>
<TabItem value="list_cloud_manager_tenants">

list_cloud_manager_tenants.

```sql
SELECT
value
FROM azure_isv.paloaltonetworksngfw.palo_alto_networks_cloudngfw_operations
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_product_serial_number_status"
    values={[
        { label: 'list_product_serial_number_status', value: 'list_product_serial_number_status' },
        { label: 'list_support_info', value: 'list_support_info' },
        { label: 'create_product_serial_number', value: 'create_product_serial_number' }
    ]}
>
<TabItem value="list_product_serial_number_status">

list_product_serial_number_status.

```sql
EXEC azure_isv.paloaltonetworksngfw.palo_alto_networks_cloudngfw_operations.list_product_serial_number_status 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_support_info">

list_support_info.

```sql
EXEC azure_isv.paloaltonetworksngfw.palo_alto_networks_cloudngfw_operations.list_support_info 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_product_serial_number">

create_product_serial_number.

```sql
EXEC azure_isv.paloaltonetworksngfw.palo_alto_networks_cloudngfw_operations.create_product_serial_number 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
