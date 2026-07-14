--- 
title: check_aml_fs_subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - check_aml_fs_subnets
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>check_aml_fs_subnets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="check_aml_fs_subnets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.check_aml_fs_subnets" /></td></tr>
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
    <td><a href="#check_aml_fs_subnets"><CopyableCode code="check_aml_fs_subnets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check that subnets will be valid for AML file system create calls.</td>
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
    defaultValue="check_aml_fs_subnets"
    values={[
        { label: 'check_aml_fs_subnets', value: 'check_aml_fs_subnets' }
    ]}
>
<TabItem value="check_aml_fs_subnets">

Check that subnets will be valid for AML file system create calls.

```sql
EXEC azure.storage_cache.check_aml_fs_subnets.check_aml_fs_subnets 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"filesystemSubnet": "{{ filesystemSubnet }}", 
"storageCapacityTiB": {{ storageCapacityTiB }}, 
"sku": "{{ sku }}", 
"location": "{{ location }}"
}'
;
```
</TabItem>
</Tabs>
