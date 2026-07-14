--- 
title: custom_model_copy_results
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_model_copy_results
  - ai_form_recognizer
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

Creates, updates, deletes, gets or lists a <code>custom_model_copy_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_model_copy_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_form_recognizer.custom_model_copy_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_custom_model_copy_result"
    values={[
        { label: 'get_custom_model_copy_result', value: 'get_custom_model_copy_result' }
    ]}
>
<TabItem value="get_custom_model_copy_result">

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
    <td><CopyableCode code="composedTrainResults" /></td>
    <td><code>array</code></td>
    <td>Training result for composed model.</td>
</tr>
<tr>
    <td><CopyableCode code="copyResult" /></td>
    <td><code>object</code></td>
    <td>Results of the copy operation.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Required. Date and time (UTC) when the copy operation was submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="keys" /></td>
    <td><code>object</code></td>
    <td>Keys extracted by the custom model.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Required. Date and time (UTC) when the status was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="modelInfo" /></td>
    <td><code>object</code></td>
    <td>Basic custom model information. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Required. Operation status. Known values are: "notStarted", "running", "succeeded", "failed".</td>
</tr>
<tr>
    <td><CopyableCode code="trainResult" /></td>
    <td><code>object</code></td>
    <td>Custom model training result. All required parameters must be populated in order to send to Azure.</td>
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
    <td><a href="#get_custom_model_copy_result"><CopyableCode code="get_custom_model_copy_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-result_id"><code>result_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Custom Model Copy Result. Obtain current status and the result of a custom model copy operation.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Model identifier.</td>
</tr>
<tr id="parameter-result_id">
    <td><CopyableCode code="result_id" /></td>
    <td><code>string</code></td>
    <td>Copy operation result identifier.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_custom_model_copy_result"
    values={[
        { label: 'get_custom_model_copy_result', value: 'get_custom_model_copy_result' }
    ]}
>
<TabItem value="get_custom_model_copy_result">

Get Custom Model Copy Result. Obtain current status and the result of a custom model copy operation.

```sql
SELECT
composedTrainResults,
copyResult,
createdDateTime,
keys,
lastUpdatedDateTime,
modelInfo,
status,
trainResult
FROM azure.ai_form_recognizer.custom_model_copy_results
WHERE model_id = '{{ model_id }}' -- required
AND result_id = '{{ result_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
