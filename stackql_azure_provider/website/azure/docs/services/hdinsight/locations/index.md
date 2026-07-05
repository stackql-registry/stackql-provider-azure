--- 
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.locations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'list_usages', value: 'list_usages' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

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
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error message associated with the cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The async operation state. Known values are: "InProgress", "Succeeded", and "Failed". (InProgress, Succeeded, Failed)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_usages">

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
    <td><CopyableCode code="name" /></td>
    <td><code>object</code></td>
    <td>The details about the localizable name of the used resource.</td>
</tr>
<tr>
    <td><CopyableCode code="currentValue" /></td>
    <td><code>integer</code></td>
    <td>The current usage.</td>
</tr>
<tr>
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The maximum allowed usage.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>The type of measurement for usage.</td>
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
    <td><a href="#get_azure_async_operation_status"><CopyableCode code="get_azure_async_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the async operation status.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the usages for the specified location.</td>
</tr>
<tr>
    <td><a href="#list_billing_specs"><CopyableCode code="list_billing_specs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the billingSpecs for the specified subscription and location.</td>
</tr>
<tr>
    <td><a href="#get_capabilities"><CopyableCode code="get_capabilities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the capabilities for the specified location.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check the cluster name is available or not.</td>
</tr>
<tr>
    <td><a href="#validate_cluster_create_request"><CopyableCode code="validate_cluster_create_request" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validate the cluster create request spec is valid or not.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The long running operation id. Required.</td>
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
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'list_usages', value: 'list_usages' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

Get the async operation status.

```sql
SELECT
error,
status
FROM azure.hdinsight.locations
WHERE location = '{{ location }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_usages">

Lists the usages for the specified location.

```sql
SELECT
name,
currentValue,
limit,
unit
FROM azure.hdinsight.locations
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_billing_specs"
    values={[
        { label: 'list_billing_specs', value: 'list_billing_specs' },
        { label: 'get_capabilities', value: 'get_capabilities' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'validate_cluster_create_request', value: 'validate_cluster_create_request' }
    ]}
>
<TabItem value="list_billing_specs">

Lists the billingSpecs for the specified subscription and location.

```sql
EXEC azure.hdinsight.locations.list_billing_specs 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_capabilities">

Gets the capabilities for the specified location.

```sql
EXEC azure.hdinsight.locations.get_capabilities 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check the cluster name is available or not.

```sql
EXEC azure.hdinsight.locations.check_name_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
<TabItem value="validate_cluster_create_request">

Validate the cluster create request spec is valid or not.

```sql
EXEC azure.hdinsight.locations.validate_cluster_create_request 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"zones": "{{ zones }}", 
"properties": "{{ properties }}", 
"identity": "{{ identity }}", 
"name": "{{ name }}", 
"type": "{{ type }}", 
"tenantId": "{{ tenantId }}", 
"fetchAaddsResource": {{ fetchAaddsResource }}
}'
;
```
</TabItem>
</Tabs>
