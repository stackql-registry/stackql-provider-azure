--- 
title: multivariate_batch_detection_results
hide_title: false
hide_table_of_contents: false
keywords:
  - multivariate_batch_detection_results
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

Creates, updates, deletes, gets or lists a <code>multivariate_batch_detection_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="multivariate_batch_detection_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_anomalydetector.multivariate_batch_detection_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_multivariate_batch_detection_result"
    values={[
        { label: 'get_multivariate_batch_detection_result', value: 'get_multivariate_batch_detection_result' }
    ]}
>
<TabItem value="get_multivariate_batch_detection_result">

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
    <td><CopyableCode code="resultId" /></td>
    <td><code>string</code></td>
    <td>Result identifier, which is used to fetch the results of an inference call. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="results" /></td>
    <td><code>array</code></td>
    <td>Detection result for each timestamp. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>object</code></td>
    <td>Multivariate anomaly detection status. Required.</td>
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
    <td><a href="#get_multivariate_batch_detection_result"><CopyableCode code="get_multivariate_batch_detection_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-result_id"><code>result_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Get Multivariate Anomaly Detection Result. For asynchronous inference, get multivariate anomaly detection result based on resultId returned by the BatchDetectAnomaly api.</td>
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
<tr id="parameter-result_id">
    <td><CopyableCode code="result_id" /></td>
    <td><code>string</code></td>
    <td>ID of a batch detection result. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_multivariate_batch_detection_result"
    values={[
        { label: 'get_multivariate_batch_detection_result', value: 'get_multivariate_batch_detection_result' }
    ]}
>
<TabItem value="get_multivariate_batch_detection_result">

Get Multivariate Anomaly Detection Result. For asynchronous inference, get multivariate anomaly detection result based on resultId returned by the BatchDetectAnomaly api.

```sql
SELECT
resultId,
results,
summary
FROM azure.ai_anomalydetector.multivariate_batch_detection_results
WHERE result_id = '{{ result_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
</Tabs>
