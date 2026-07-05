--- 
title: location
hide_title: false
hide_table_of_contents: false
keywords:
  - location
  - batch
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

Creates, updates, deletes, gets or lists a <code>location</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="location" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.location" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_supported_virtual_machine_skus"
    values={[
        { label: 'list_supported_virtual_machine_skus', value: 'list_supported_virtual_machine_skus' }
    ]}
>
<TabItem value="list_supported_virtual_machine_skus">

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
    <td><code>string</code></td>
    <td>The name of the SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="batchSupportEndOfLife" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when Azure Batch service will retire this SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>A collection of capabilities which this SKU supports.</td>
</tr>
<tr>
    <td><CopyableCode code="familyName" /></td>
    <td><code>string</code></td>
    <td>The family name of the SKU.</td>
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
    <td><a href="#list_supported_virtual_machine_skus"><CopyableCode code="list_supported_virtual_machine_skus" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the list of Batch supported Virtual Machine VM sizes available at the given location.</td>
</tr>
<tr>
    <td><a href="#get_quotas"><CopyableCode code="get_quotas" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Batch service quotas for the specified subscription at the given location.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks whether the Batch account name is available in the specified region.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The desired region for the name check. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Valid properties for filtering are "familyName". Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_supported_virtual_machine_skus"
    values={[
        { label: 'list_supported_virtual_machine_skus', value: 'list_supported_virtual_machine_skus' }
    ]}
>
<TabItem value="list_supported_virtual_machine_skus">

Gets the list of Batch supported Virtual Machine VM sizes available at the given location.

```sql
SELECT
name,
batchSupportEndOfLife,
capabilities,
familyName
FROM azure.batch.location
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_quotas"
    values={[
        { label: 'get_quotas', value: 'get_quotas' },
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="get_quotas">

Gets the Batch service quotas for the specified subscription at the given location.

```sql
EXEC azure.batch.location.get_quotas 
@location_name='{{ location_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks whether the Batch account name is available in the specified region.

```sql
EXEC azure.batch.location.check_name_availability 
@location_name='{{ location_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
