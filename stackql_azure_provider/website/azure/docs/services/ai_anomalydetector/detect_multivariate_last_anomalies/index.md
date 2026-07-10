--- 
title: detect_multivariate_last_anomalies
hide_title: false
hide_table_of_contents: false
keywords:
  - detect_multivariate_last_anomalies
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

Creates, updates, deletes, gets or lists a <code>detect_multivariate_last_anomalies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="detect_multivariate_last_anomalies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_anomalydetector.detect_multivariate_last_anomalies" /></td></tr>
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
    <td><a href="#detect_multivariate_last_anomaly"><CopyableCode code="detect_multivariate_last_anomaly" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a>, <a href="#parameter-variables"><code>variables</code></a>, <a href="#parameter-topContributorCount"><code>topContributorCount</code></a></td>
    <td></td>
    <td>Detect anomalies in the last point of the request body. Submit multivariate anomaly detection task with the modelId of trained model and inference data, and the inference data should be put into request body in a JSON format. The request will complete synchronously and return the detection immediately in the response body.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `ApiVersion` parameter. (default: )</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Model identifier. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="detect_multivariate_last_anomaly"
    values={[
        { label: 'detect_multivariate_last_anomaly', value: 'detect_multivariate_last_anomaly' }
    ]}
>
<TabItem value="detect_multivariate_last_anomaly">

Detect anomalies in the last point of the request body. Submit multivariate anomaly detection task with the modelId of trained model and inference data, and the inference data should be put into request body in a JSON format. The request will complete synchronously and return the detection immediately in the response body.

```sql
EXEC azure.ai_anomalydetector.detect_multivariate_last_anomalies.detect_multivariate_last_anomaly 
@model_id='{{ model_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required 
@@json=
'{
"variables": "{{ variables }}", 
"topContributorCount": {{ topContributorCount }}
}'
;
```
</TabItem>
</Tabs>
