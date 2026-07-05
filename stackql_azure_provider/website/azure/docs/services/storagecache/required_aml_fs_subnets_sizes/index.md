--- 
title: required_aml_fs_subnets_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - required_aml_fs_subnets_sizes
  - storagecache
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

Creates, updates, deletes, gets or lists a <code>required_aml_fs_subnets_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="required_aml_fs_subnets_sizes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagecache.required_aml_fs_subnets_sizes" /></td></tr>
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
    <td><a href="#get_required_aml_fs_subnets_size"><CopyableCode code="get_required_aml_fs_subnets_size" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the number of available IP addresses needed for the AML file system information provided.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="get_required_aml_fs_subnets_size"
    values={[
        { label: 'get_required_aml_fs_subnets_size', value: 'get_required_aml_fs_subnets_size' }
    ]}
>
<TabItem value="get_required_aml_fs_subnets_size">

Get the number of available IP addresses needed for the AML file system information provided.

```sql
EXEC azure.storagecache.required_aml_fs_subnets_sizes.get_required_aml_fs_subnets_size 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"storageCapacityTiB": {{ storageCapacityTiB }}, 
"sku": "{{ sku }}"
}'
;
```
</TabItem>
</Tabs>
