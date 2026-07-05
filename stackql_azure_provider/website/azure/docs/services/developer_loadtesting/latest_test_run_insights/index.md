--- 
title: latest_test_run_insights
hide_title: false
hide_table_of_contents: false
keywords:
  - latest_test_run_insights
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists a <code>latest_test_run_insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="latest_test_run_insights" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.latest_test_run_insights" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_latest_test_run_insights"
    values={[
        { label: 'get_latest_test_run_insights', value: 'get_latest_test_run_insights' }
    ]}
>
<TabItem value="get_latest_test_run_insights">

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
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td>The columns of the insights.</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>object</code></td>
    <td>The rows of the insights.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the insights. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The version of the insights.</td>
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
    <td><a href="#get_latest_test_run_insights"><CopyableCode code="get_latest_test_run_insights" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the latest insights for the test run. Get the latest insights for the test run.</td>
</tr>
<tr>
    <td><a href="#update_latest_test_run_insights"><CopyableCode code="update_latest_test_run_insights" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-test_run_id"><code>test_run_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update the latest insights for the test run. Update the latest insights for the test run.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-test_run_id">
    <td><CopyableCode code="test_run_id" /></td>
    <td><code>string</code></td>
    <td>Unique name for the load test run, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_latest_test_run_insights"
    values={[
        { label: 'get_latest_test_run_insights', value: 'get_latest_test_run_insights' }
    ]}
>
<TabItem value="get_latest_test_run_insights">

Get the latest insights for the test run. Get the latest insights for the test run.

```sql
SELECT
columns,
rows,
status,
version
FROM azure.developer_loadtesting.latest_test_run_insights
WHERE test_run_id = '{{ test_run_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_latest_test_run_insights"
    values={[
        { label: 'update_latest_test_run_insights', value: 'update_latest_test_run_insights' }
    ]}
>
<TabItem value="update_latest_test_run_insights">

Update the latest insights for the test run. Update the latest insights for the test run.

```sql
UPDATE azure.developer_loadtesting.latest_test_run_insights
SET 
rows = '{{ rows }}'
WHERE 
test_run_id = '{{ test_run_id }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
columns,
rows,
status,
version;
```
</TabItem>
</Tabs>
