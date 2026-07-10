--- 
title: text_blocklist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - text_blocklist_items
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

Creates, updates, deletes, gets or lists a <code>text_blocklist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="text_blocklist_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_contentsafety.text_blocklist_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_text_blocklist_item"
    values={[
        { label: 'get_text_blocklist_item', value: 'get_text_blocklist_item' },
        { label: 'list_text_blocklist_items', value: 'list_text_blocklist_items' }
    ]}
>
<TabItem value="get_text_blocklist_item">

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
    <td><CopyableCode code="blocklistItemId" /></td>
    <td><code>string</code></td>
    <td>The service will generate a BlocklistItemId, which will be a UUID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>BlocklistItem description.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>BlocklistItem content. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_text_blocklist_items">

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
    <td><CopyableCode code="blocklistItemId" /></td>
    <td><code>string</code></td>
    <td>The service will generate a BlocklistItemId, which will be a UUID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>BlocklistItem description.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>BlocklistItem content. Required.</td>
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
    <td><a href="#get_text_blocklist_item"><CopyableCode code="get_text_blocklist_item" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-blocklist_item_id"><code>blocklist_item_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get BlocklistItem By blocklistName And blocklistItemId. Get blocklistItem by blocklistName and blocklistItemId from a text blocklist.</td>
</tr>
<tr>
    <td><a href="#list_text_blocklist_items"><CopyableCode code="list_text_blocklist_items" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Get All BlocklistItems By blocklistName. Get all blocklistItems in a text blocklist.</td>
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
<tr id="parameter-blocklist_item_id">
    <td><CopyableCode code="blocklist_item_id" /></td>
    <td><code>string</code></td>
    <td>The service will generate a BlocklistItemId, which will be a UUID. Required.</td>
</tr>
<tr id="parameter-blocklist_name">
    <td><CopyableCode code="blocklist_name" /></td>
    <td><code>string</code></td>
    <td>Text blocklist name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_text_blocklist_item"
    values={[
        { label: 'get_text_blocklist_item', value: 'get_text_blocklist_item' },
        { label: 'list_text_blocklist_items', value: 'list_text_blocklist_items' }
    ]}
>
<TabItem value="get_text_blocklist_item">

Get BlocklistItem By blocklistName And blocklistItemId. Get blocklistItem by blocklistName and blocklistItemId from a text blocklist.

```sql
SELECT
blocklistItemId,
description,
text
FROM azure.ai_contentsafety.text_blocklist_items
WHERE blocklist_name = '{{ blocklist_name }}' -- required
AND blocklist_item_id = '{{ blocklist_item_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_text_blocklist_items">

Get All BlocklistItems By blocklistName. Get all blocklistItems in a text blocklist.

```sql
SELECT
blocklistItemId,
description,
text
FROM azure.ai_contentsafety.text_blocklist_items
WHERE blocklist_name = '{{ blocklist_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>
