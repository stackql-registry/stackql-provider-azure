--- 
title: detect_univariate_change_points
hide_title: false
hide_table_of_contents: false
keywords:
  - detect_univariate_change_points
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

Creates, updates, deletes, gets or lists a <code>detect_univariate_change_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="detect_univariate_change_points" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_anomalydetector.detect_univariate_change_points" /></td></tr>
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
    <td><a href="#detect_univariate_change_point"><CopyableCode code="detect_univariate_change_point" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a>, <a href="#parameter-series"><code>series</code></a>, <a href="#parameter-granularity"><code>granularity</code></a></td>
    <td></td>
    <td>Detect change point for the entire series. Evaluate change point score of every series point.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="detect_univariate_change_point"
    values={[
        { label: 'detect_univariate_change_point', value: 'detect_univariate_change_point' }
    ]}
>
<TabItem value="detect_univariate_change_point">

Detect change point for the entire series. Evaluate change point score of every series point.

```sql
EXEC azure.ai_anomalydetector.detect_univariate_change_points.detect_univariate_change_point 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required 
@@json=
'{
"series": "{{ series }}", 
"granularity": "{{ granularity }}", 
"customInterval": {{ customInterval }}, 
"period": {{ period }}, 
"stableTrendWindow": {{ stableTrendWindow }}, 
"threshold": {{ threshold }}
}'
;
```
</TabItem>
</Tabs>
