--- 
title: translates
hide_title: false
hide_table_of_contents: false
keywords:
  - translates
  - ai_translation_text
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

Creates, updates, deletes, gets or lists a <code>translates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="translates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_translation_text.translates" /></td></tr>
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
    <td><a href="#translate"><CopyableCode code="translate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-inputs"><code>inputs</code></a></td>
    <td><a href="#parameter-X-ClientTraceId"><code>X-ClientTraceId</code></a></td>
    <td>Translate Text. Translate Text.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-X-ClientTraceId">
    <td><CopyableCode code="X-ClientTraceId" /></td>
    <td><code>string</code></td>
    <td>A client-generated GUID to uniquely identify the request. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="translate"
    values={[
        { label: 'translate', value: 'translate' }
    ]}
>
<TabItem value="translate">

Translate Text. Translate Text.

```sql
EXEC azure.ai_translation_text.translates.translate 
@endpoint='{{ endpoint }}' --required, 
@X-ClientTraceId='{{ X-ClientTraceId }}' 
@@json=
'{
"inputs": "{{ inputs }}"
}'
;
```
</TabItem>
</Tabs>
