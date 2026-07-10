--- 
title: text_blocklists
hide_title: false
hide_table_of_contents: false
keywords:
  - text_blocklists
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

Creates, updates, deletes, gets or lists a <code>text_blocklists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="text_blocklists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_contentsafety.text_blocklists" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_text_blocklist"
    values={[
        { label: 'get_text_blocklist', value: 'get_text_blocklist' },
        { label: 'list_text_blocklists', value: 'list_text_blocklists' }
    ]}
>
<TabItem value="get_text_blocklist">

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
    <td><CopyableCode code="blocklistName" /></td>
    <td><code>string</code></td>
    <td>Text blocklist name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text blocklist description.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_text_blocklists">

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
    <td><CopyableCode code="blocklistName" /></td>
    <td><code>string</code></td>
    <td>Text blocklist name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Text blocklist description.</td>
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
    <td><a href="#get_text_blocklist"><CopyableCode code="get_text_blocklist" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Text Blocklist By blocklistName. Returns text blocklist details.</td>
</tr>
<tr>
    <td><a href="#list_text_blocklists"><CopyableCode code="list_text_blocklists" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get All Text Blocklists. Get all text blocklists details.</td>
</tr>
<tr>
    <td><a href="#create_or_update_text_blocklist"><CopyableCode code="create_or_update_text_blocklist" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-blocklistName"><code>blocklistName</code></a></td>
    <td></td>
    <td>Create Or Update Text Blocklist. Updates a text blocklist. If the blocklistName does not exist, a new blocklist will be created.</td>
</tr>
<tr>
    <td><a href="#create_or_update_text_blocklist"><CopyableCode code="create_or_update_text_blocklist" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-blocklistName"><code>blocklistName</code></a></td>
    <td></td>
    <td>Create Or Update Text Blocklist. Updates a text blocklist. If the blocklistName does not exist, a new blocklist will be created.</td>
</tr>
<tr>
    <td><a href="#delete_text_blocklist"><CopyableCode code="delete_text_blocklist" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-blocklist_name"><code>blocklist_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Text Blocklist By blocklistName. Deletes a text blocklist.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_text_blocklist"
    values={[
        { label: 'get_text_blocklist', value: 'get_text_blocklist' },
        { label: 'list_text_blocklists', value: 'list_text_blocklists' }
    ]}
>
<TabItem value="get_text_blocklist">

Get Text Blocklist By blocklistName. Returns text blocklist details.

```sql
SELECT
blocklistName,
description
FROM azure.ai_contentsafety.text_blocklists
WHERE blocklist_name = '{{ blocklist_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_text_blocklists">

Get All Text Blocklists. Get all text blocklists details.

```sql
SELECT
blocklistName,
description
FROM azure.ai_contentsafety.text_blocklists
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_text_blocklist"
    values={[
        { label: 'create_or_update_text_blocklist', value: 'create_or_update_text_blocklist' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_text_blocklist">

Create Or Update Text Blocklist. Updates a text blocklist. If the blocklistName does not exist, a new blocklist will be created.

```sql
INSERT INTO azure.ai_contentsafety.text_blocklists (
blocklistName,
description,
blocklist_name,
endpoint
)
SELECT 
'{{ blocklistName }}' /* required */,
'{{ description }}',
'{{ blocklist_name }}',
'{{ endpoint }}'
RETURNING
blocklistName,
description
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: text_blocklists
  props:
    - name: blocklist_name
      value: "{{ blocklist_name }}"
      description: Required parameter for the text_blocklists resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the text_blocklists resource.
    - name: blocklistName
      value: "{{ blocklistName }}"
      description: |
        Text blocklist name. Required.
    - name: description
      value: "{{ description }}"
      description: |
        Text blocklist description.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_text_blocklist"
    values={[
        { label: 'create_or_update_text_blocklist', value: 'create_or_update_text_blocklist' }
    ]}
>
<TabItem value="create_or_update_text_blocklist">

Create Or Update Text Blocklist. Updates a text blocklist. If the blocklistName does not exist, a new blocklist will be created.

```sql
REPLACE azure.ai_contentsafety.text_blocklists
SET 
blocklistName = '{{ blocklistName }}',
description = '{{ description }}'
WHERE 
blocklist_name = '{{ blocklist_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND blocklistName = '{{ blocklistName }}' --required
RETURNING
blocklistName,
description;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_text_blocklist"
    values={[
        { label: 'delete_text_blocklist', value: 'delete_text_blocklist' }
    ]}
>
<TabItem value="delete_text_blocklist">

Delete Text Blocklist By blocklistName. Deletes a text blocklist.

```sql
DELETE FROM azure.ai_contentsafety.text_blocklists
WHERE blocklist_name = '{{ blocklist_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
