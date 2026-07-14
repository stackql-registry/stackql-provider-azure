--- 
title: train_multivariate_models
hide_title: false
hide_table_of_contents: false
keywords:
  - train_multivariate_models
  - ai_anomaly_detector
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

Creates, updates, deletes, gets or lists a <code>train_multivariate_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="train_multivariate_models" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_anomaly_detector.train_multivariate_models" /></td></tr>
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
    <td><a href="#train_multivariate_model"><CopyableCode code="train_multivariate_model" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a>, <a href="#parameter-dataSource"><code>dataSource</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a></td>
    <td></td>
    <td>Train a Multivariate Anomaly Detection Model. Create and train a multivariate anomaly detection model. The request must include a source parameter to indicate an externally accessible Azure blob storage URI.There are two types of data input: An URI pointed to an Azure blob storage folder which contains multiple CSV files, and each CSV file contains two columns, timestamp and variable. Another type of input is an URI pointed to a CSV file in Azure blob storage, which contains all the variables and a timestamp column.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="train_multivariate_model"
    values={[
        { label: 'train_multivariate_model', value: 'train_multivariate_model' }
    ]}
>
<TabItem value="train_multivariate_model">

Train a Multivariate Anomaly Detection Model. Create and train a multivariate anomaly detection model. The request must include a source parameter to indicate an externally accessible Azure blob storage URI.There are two types of data input: An URI pointed to an Azure blob storage folder which contains multiple CSV files, and each CSV file contains two columns, timestamp and variable. Another type of input is an URI pointed to a CSV file in Azure blob storage, which contains all the variables and a timestamp column.

```sql
EXEC azure.ai_anomaly_detector.train_multivariate_models.train_multivariate_model 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required 
@@json=
'{
"dataSource": "{{ dataSource }}", 
"dataSchema": "{{ dataSchema }}", 
"startTime": "{{ startTime }}", 
"endTime": "{{ endTime }}", 
"displayName": "{{ displayName }}", 
"slidingWindow": {{ slidingWindow }}, 
"alignPolicy": "{{ alignPolicy }}", 
"status": "{{ status }}", 
"errors": "{{ errors }}", 
"diagnosticsInfo": "{{ diagnosticsInfo }}"
}'
;
```
</TabItem>
</Tabs>
