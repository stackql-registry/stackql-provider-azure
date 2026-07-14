--- 
title: analyze_results
hide_title: false
hide_table_of_contents: false
keywords:
  - analyze_results
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

Creates, updates, deletes, gets or lists an <code>analyze_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyze_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.analyze_results" /></td></tr>
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
    <td><a href="#delete_analyze_result"><CopyableCode code="delete_analyze_result" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-result_id"><code>result_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Mark the result of document analysis for deletion.</td>
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

## `DELETE` examples

<Tabs
    defaultValue="delete_analyze_result"
    values={[
        { label: 'delete_analyze_result', value: 'delete_analyze_result' }
    ]}
>
<TabItem value="delete_analyze_result">

Mark the result of document analysis for deletion.

```sql
DELETE FROM azure.ai_document_intelligence.analyze_results
WHERE model_id = '{{ model_id }}' --required
AND result_id = '{{ result_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
