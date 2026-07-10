--- 
title: custom_models
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_models
  - ai_formrecognizer
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

Creates, updates, deletes, gets or lists a <code>custom_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_models" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_formrecognizer.custom_models" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_custom_model"
    values={[
        { label: 'get_custom_model', value: 'get_custom_model' },
        { label: 'list_custom_models', value: 'list_custom_models' }
    ]}
>
<TabItem value="get_custom_model">

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
    <td><CopyableCode code="keys" /></td>
    <td><code>object</code></td>
    <td>Keys extracted by the custom model.</td>
</tr>
<tr>
    <td><CopyableCode code="modelInfo" /></td>
    <td><code>object</code></td>
    <td>Basic custom model information. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="trainResult" /></td>
    <td><code>object</code></td>
    <td>Custom model training result. All required parameters must be populated in order to send to Azure.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_custom_models">

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
    <td><CopyableCode code="keys" /></td>
    <td><code>object</code></td>
    <td>Keys extracted by the custom model.</td>
</tr>
<tr>
    <td><CopyableCode code="modelInfo" /></td>
    <td><code>object</code></td>
    <td>Required. Basic custom model information.</td>
</tr>
<tr>
    <td><CopyableCode code="modelList" /></td>
    <td><code>array</code></td>
    <td>Collection of trained custom models.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>Link to the next page of custom models.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>object</code></td>
    <td>Summary of all trained custom models.</td>
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
    <td><a href="#get_custom_model"><CopyableCode code="get_custom_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-includeKeys"><code>includeKeys</code></a></td>
    <td>Get Custom Model. Get detailed information about a custom model.</td>
</tr>
<tr>
    <td><a href="#list_custom_models"><CopyableCode code="list_custom_models" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List Custom Models. Get information about all custom models.</td>
</tr>
<tr>
    <td><a href="#delete_custom_model"><CopyableCode code="delete_custom_model" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete Custom Model. Mark model for deletion. Model artifacts will be permanently removed within a predetermined period.</td>
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
<tr id="parameter-includeKeys">
    <td><CopyableCode code="includeKeys" /></td>
    <td><code>boolean</code></td>
    <td>Include list of extracted keys in model information. Default value is False.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_custom_model"
    values={[
        { label: 'get_custom_model', value: 'get_custom_model' },
        { label: 'list_custom_models', value: 'list_custom_models' }
    ]}
>
<TabItem value="get_custom_model">

Get Custom Model. Get detailed information about a custom model.

```sql
SELECT
composedTrainResults,
keys,
modelInfo,
trainResult
FROM azure.ai_formrecognizer.custom_models
WHERE model_id = '{{ model_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND includeKeys = '{{ includeKeys }}'
;
```
</TabItem>
<TabItem value="list_custom_models">

List Custom Models. Get information about all custom models.

```sql
SELECT
composedTrainResults,
keys,
modelInfo,
modelList,
nextLink,
summary,
trainResult
FROM azure.ai_formrecognizer.custom_models
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_custom_model"
    values={[
        { label: 'delete_custom_model', value: 'delete_custom_model' }
    ]}
>
<TabItem value="delete_custom_model">

Delete Custom Model. Mark model for deletion. Model artifacts will be permanently removed within a predetermined period.

```sql
DELETE FROM azure.ai_formrecognizer.custom_models
WHERE model_id = '{{ model_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
