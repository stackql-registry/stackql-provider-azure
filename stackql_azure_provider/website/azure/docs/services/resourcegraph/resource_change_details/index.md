--- 
title: resource_change_details
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_change_details
  - resourcegraph
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

Creates, updates, deletes, gets or lists a <code>resource_change_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_change_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resourcegraph.resource_change_details" /></td></tr>
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
    <td><a href="#resource_change_details"><CopyableCode code="resource_change_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resourceIds"><code>resourceIds</code></a>, <a href="#parameter-changeIds"><code>changeIds</code></a></td>
    <td></td>
    <td>Get resource change details.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="resource_change_details"
    values={[
        { label: 'resource_change_details', value: 'resource_change_details' }
    ]}
>
<TabItem value="resource_change_details">

Get resource change details.

```sql
EXEC azure.resourcegraph.resource_change_details.resource_change_details 
@@json=
'{
"resourceIds": "{{ resourceIds }}", 
"changeIds": "{{ changeIds }}"
}'
;
```
</TabItem>
</Tabs>
