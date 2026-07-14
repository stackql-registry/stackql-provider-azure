--- 
title: analyze_result_figures
hide_title: false
hide_table_of_contents: false
keywords:
  - analyze_result_figures
  - ai_document_intelligence
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

Creates, updates, deletes, gets or lists an <code>analyze_result_figures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyze_result_figures" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.analyze_result_figures" /></td></tr>
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
    <td><a href="#get_analyze_result_figure"><CopyableCode code="get_analyze_result_figure" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-result_id"><code>result_id</code></a>, <a href="#parameter-figure_id"><code>figure_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the generated cropped image of specified figure from document analysis.</td>
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
<tr id="parameter-figure_id">
    <td><CopyableCode code="figure_id" /></td>
    <td><code>string</code></td>
    <td>Figure ID. Required.</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
<tr id="parameter-result_id">
    <td><CopyableCode code="result_id" /></td>
    <td><code>string</code></td>
    <td>Analyze operation result ID. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_analyze_result_figure"
    values={[
        { label: 'get_analyze_result_figure', value: 'get_analyze_result_figure' }
    ]}
>
<TabItem value="get_analyze_result_figure">

Gets the generated cropped image of specified figure from document analysis.

```sql
EXEC azure.ai_document_intelligence.analyze_result_figures.get_analyze_result_figure 
@model_id='{{ model_id }}' --required, 
@result_id='{{ result_id }}' --required, 
@figure_id='{{ figure_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
