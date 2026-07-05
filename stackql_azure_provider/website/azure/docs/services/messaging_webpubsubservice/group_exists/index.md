--- 
title: group_exists
hide_title: false
hide_table_of_contents: false
keywords:
  - group_exists
  - messaging_webpubsubservice
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

Creates, updates, deletes, gets or lists a <code>group_exists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="group_exists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.group_exists" /></td></tr>
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
    <td><a href="#group_exists"><CopyableCode code="group_exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group"><code>group</code></a>, <a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Check if there are any client connections inside the given group. Check if there are any client connections inside the given group.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-group">
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>Target group name, which length should be greater than 0 and less than 1025. Required.</td>
</tr>
<tr id="parameter-hub">
    <td><CopyableCode code="hub" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="group_exists"
    values={[
        { label: 'group_exists', value: 'group_exists' }
    ]}
>
<TabItem value="group_exists">

Check if there are any client connections inside the given group. Check if there are any client connections inside the given group.

```sql
EXEC azure.messaging_webpubsubservice.group_exists.group_exists 
@group='{{ group }}' --required, 
@hub='{{ hub }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
