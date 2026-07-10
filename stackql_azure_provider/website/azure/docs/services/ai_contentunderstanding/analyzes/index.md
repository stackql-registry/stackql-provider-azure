--- 
title: analyzes
hide_title: false
hide_table_of_contents: false
keywords:
  - analyzes
  - ai_contentunderstanding
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

Creates, updates, deletes, gets or lists an <code>analyzes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyzes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_contentunderstanding.analyzes" /></td></tr>
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
    <td><a href="#analyze"><CopyableCode code="analyze" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-analyzer_id"><code>analyzer_id</code></a>, <a href="#parameter-stringEncoding"><code>stringEncoding</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-processingLocation"><code>processingLocation</code></a></td>
    <td>Extract content and fields from input.</td>
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
<tr id="parameter-analyzer_id">
    <td><CopyableCode code="analyzer_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the analyzer. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-stringEncoding">
    <td><CopyableCode code="stringEncoding" /></td>
    <td><code>string</code></td>
    <td>The string encoding format for content spans in the response. Possible values are 'codePoint', 'utf16', and `utf8`. Default is `codePoint`."). Required.</td>
</tr>
<tr id="parameter-processingLocation">
    <td><CopyableCode code="processingLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the data may be processed. Defaults to global. Known values are: "geography", "dataZone", and "global". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="analyze"
    values={[
        { label: 'analyze', value: 'analyze' }
    ]}
>
<TabItem value="analyze">

Extract content and fields from input.

```sql
EXEC azure.ai_contentunderstanding.analyzes.analyze 
@analyzer_id='{{ analyzer_id }}' --required, 
@stringEncoding='{{ stringEncoding }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@processingLocation='{{ processingLocation }}'
;
```
</TabItem>
</Tabs>
