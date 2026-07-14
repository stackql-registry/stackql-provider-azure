--- 
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - app_configuration
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

Creates, updates, deletes, gets or lists an <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>If any, the error message that provides more detail for the reason that the name is not available.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether the resource name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>If any, the reason that the name is not available.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="display" /></td>
    <td><code>object</code></td>
    <td>The display information for the configuration store operation.</td>
</tr>
<tr>
    <td><CopyableCode code="isDataAction" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the operation is a data action.</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>Origin of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceSpecification" /></td>
    <td><code>object</code></td>
    <td>Service specifications of the operation.</td>
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
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether the configuration store name is available for use.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List the operations for the provider.</td>
</tr>
<tr>
    <td><a href="#regional_check_name_availability"><CopyableCode code="regional_check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Checks whether the configuration store name is available for use.</td>
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
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="check_name_availability">

Checks whether the configuration store name is available for use.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.app_configuration.operations
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the operations for the provider.

```sql
SELECT
name,
display,
isDataAction,
origin,
serviceSpecification
FROM azure.app_configuration.operations
WHERE $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="regional_check_name_availability"
    values={[
        { label: 'regional_check_name_availability', value: 'regional_check_name_availability' }
    ]}
>
<TabItem value="regional_check_name_availability">

Checks whether the configuration store name is available for use.

```sql
EXEC azure.app_configuration.operations.regional_check_name_availability 
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
</Tabs>
