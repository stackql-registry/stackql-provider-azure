--- 
title: deidentify_texts
hide_title: false
hide_table_of_contents: false
keywords:
  - deidentify_texts
  - health_deidentification
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

Creates, updates, deletes, gets or lists a <code>deidentify_texts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deidentify_texts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.health_deidentification.deidentify_texts" /></td></tr>
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
    <td><a href="#deidentify_text"><CopyableCode code="deidentify_text" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-inputText"><code>inputText</code></a></td>
    <td></td>
    <td>De-identify text. A remote procedure call (RPC) operation.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="deidentify_text"
    values={[
        { label: 'deidentify_text', value: 'deidentify_text' }
    ]}
>
<TabItem value="deidentify_text">

De-identify text. A remote procedure call (RPC) operation.

```sql
EXEC azure.health_deidentification.deidentify_texts.deidentify_text 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"inputText": "{{ inputText }}", 
"operation": "{{ operation }}", 
"taggedEntities": "{{ taggedEntities }}", 
"customizations": "{{ customizations }}"
}'
;
```
</TabItem>
</Tabs>
