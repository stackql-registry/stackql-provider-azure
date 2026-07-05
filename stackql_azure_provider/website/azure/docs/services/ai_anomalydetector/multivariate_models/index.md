--- 
title: multivariate_models
hide_title: false
hide_table_of_contents: false
keywords:
  - multivariate_models
  - ai_anomalydetector
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

Creates, updates, deletes, gets or lists a <code>multivariate_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="multivariate_models" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_anomalydetector.multivariate_models" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_multivariate_model"
    values={[
        { label: 'get_multivariate_model', value: 'get_multivariate_model' },
        { label: 'list_multivariate_models', value: 'list_multivariate_models' }
    ]}
>
<TabItem value="get_multivariate_model">

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
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the model was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the model was last updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>Model identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelInfo" /></td>
    <td><code>object</code></td>
    <td>Training result of a model including its status, errors and diagnostics information.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_multivariate_models">

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
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the model was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the model was last updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>Model identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modelInfo" /></td>
    <td><code>object</code></td>
    <td>Training result of a model including its status, errors and diagnostics information.</td>
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
    <td><a href="#get_multivariate_model"><CopyableCode code="get_multivariate_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Get Multivariate Model. Get detailed information of multivariate model, including the training status and variables used in the model.</td>
</tr>
<tr>
    <td><a href="#list_multivariate_models"><CopyableCode code="list_multivariate_models" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List Multivariate Models. List models of a resource.</td>
</tr>
<tr>
    <td><a href="#delete_multivariate_model"><CopyableCode code="delete_multivariate_model" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Delete Multivariate Model. Delete an existing multivariate model according to the modelId.</td>
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
<tr id="parameter-api_version">
    <td><CopyableCode code="api_version" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `ApiVersion` parameter. (default: )</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Model identifier. Required.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>Skip indicates how many models will be skipped. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>Top indicates how many models will be fetched. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_multivariate_model"
    values={[
        { label: 'get_multivariate_model', value: 'get_multivariate_model' },
        { label: 'list_multivariate_models', value: 'list_multivariate_models' }
    ]}
>
<TabItem value="get_multivariate_model">

Get Multivariate Model. Get detailed information of multivariate model, including the training status and variables used in the model.

```sql
SELECT
createdTime,
lastUpdatedTime,
modelId,
modelInfo
FROM azure.ai_anomalydetector.multivariate_models
WHERE model_id = '{{ model_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
<TabItem value="list_multivariate_models">

List Multivariate Models. List models of a resource.

```sql
SELECT
createdTime,
lastUpdatedTime,
modelId,
modelInfo
FROM azure.ai_anomalydetector.multivariate_models
WHERE endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
AND skip = '{{ skip }}'
AND top = '{{ top }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_multivariate_model"
    values={[
        { label: 'delete_multivariate_model', value: 'delete_multivariate_model' }
    ]}
>
<TabItem value="delete_multivariate_model">

Delete Multivariate Model. Delete an existing multivariate model according to the modelId.

```sql
DELETE FROM azure.ai_anomalydetector.multivariate_models
WHERE model_id = '{{ model_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required
;
```
</TabItem>
</Tabs>
