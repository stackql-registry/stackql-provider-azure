--- 
title: remove_blocklist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - remove_blocklist_items
  - ai_contentsafety
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

Creates, updates, deletes, gets or lists a <code>remove_blocklist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="remove_blocklist_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_contentsafety.remove_blocklist_items" /></td></tr>
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
    <td><a href="#remove_blocklist_items"><CopyableCode code="remove_blocklist_items" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-blocklistItemIds"><code>blocklistItemIds</code></a></td>
    <td></td>
    <td>Remove BlocklistItems From Text Blocklist. Remove blocklistItems from a text blocklist. You can remove at most 100 BlocklistItems in one request.</td>
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
<tr id="parameter-blocklist_name">
    <td><CopyableCode code="blocklist_name" /></td>
    <td><code>string</code></td>
    <td>Text blocklist name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="remove_blocklist_items"
    values={[
        { label: 'remove_blocklist_items', value: 'remove_blocklist_items' }
    ]}
>
<TabItem value="remove_blocklist_items">

Remove BlocklistItems From Text Blocklist. Remove blocklistItems from a text blocklist. You can remove at most 100 BlocklistItems in one request.

```sql
EXEC azure.ai_contentsafety.remove_blocklist_items.remove_blocklist_items 
@blocklist_name='{{ blocklist_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"blocklistItemIds": "{{ blocklistItemIds }}"
}'
;
```
</TabItem>
</Tabs>
