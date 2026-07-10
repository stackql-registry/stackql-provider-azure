--- 
title: add_connections_to_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - add_connections_to_groups
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

Creates, updates, deletes, gets or lists an <code>add_connections_to_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="add_connections_to_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.add_connections_to_groups" /></td></tr>
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
    <td><a href="#add_connections_to_groups"><CopyableCode code="add_connections_to_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-groups"><code>groups</code></a></td>
    <td></td>
    <td>Add filtered connections to multiple groups. Add filtered connections to multiple groups.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
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
    defaultValue="add_connections_to_groups"
    values={[
        { label: 'add_connections_to_groups', value: 'add_connections_to_groups' }
    ]}
>
<TabItem value="add_connections_to_groups">

Add filtered connections to multiple groups. Add filtered connections to multiple groups.

```sql
EXEC azure.messaging_webpubsubservice.add_connections_to_groups.add_connections_to_groups 
@hub='{{ hub }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"groups": "{{ groups }}", 
"filter": "{{ filter }}"
}'
;
```
</TabItem>
</Tabs>
