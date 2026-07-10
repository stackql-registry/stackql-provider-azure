--- 
title: detect_univariate_last_points
hide_title: false
hide_table_of_contents: false
keywords:
  - detect_univariate_last_points
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

Creates, updates, deletes, gets or lists a <code>detect_univariate_last_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="detect_univariate_last_points" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_anomalydetector.detect_univariate_last_points" /></td></tr>
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
    <td><a href="#detect_univariate_last_point"><CopyableCode code="detect_univariate_last_point" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a>, <a href="#parameter-series"><code>series</code></a></td>
    <td></td>
    <td>Detect anomaly status of the latest point in time series. This operation generates a model using the points that you sent into the API, and based on all data to determine whether the last point is anomalous.</td>
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
    defaultValue="detect_univariate_last_point"
    values={[
        { label: 'detect_univariate_last_point', value: 'detect_univariate_last_point' }
    ]}
>
<TabItem value="detect_univariate_last_point">

Detect anomaly status of the latest point in time series. This operation generates a model using the points that you sent into the API, and based on all data to determine whether the last point is anomalous.

```sql
EXEC azure.ai_anomalydetector.detect_univariate_last_points.detect_univariate_last_point 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required 
@@json=
'{
"series": "{{ series }}", 
"granularity": "{{ granularity }}", 
"customInterval": {{ customInterval }}, 
"period": {{ period }}, 
"maxAnomalyRatio": {{ maxAnomalyRatio }}, 
"sensitivity": {{ sensitivity }}, 
"imputeMode": "{{ imputeMode }}", 
"imputeFixedValue": {{ imputeFixedValue }}
}'
;
```
</TabItem>
</Tabs>
