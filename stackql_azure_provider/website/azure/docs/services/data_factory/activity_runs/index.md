--- 
title: activity_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - activity_runs
  - data_factory
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

Creates, updates, deletes, gets or lists an <code>activity_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="activity_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.activity_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="query_by_pipeline_run"
    values={[
        { label: 'query_by_pipeline_run', value: 'query_by_pipeline_run' }
    ]}
>
<TabItem value="query_by_pipeline_run">

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
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token for getting the next page of results, if any remaining results exist, null otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>List of activity runs. Required.</td>
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
    <td><a href="#query_by_pipeline_run"><CopyableCode code="query_by_pipeline_run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-run_id"><code>run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Query activity runs based on input filter conditions.</td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-run_id">
    <td><CopyableCode code="run_id" /></td>
    <td><code>string</code></td>
    <td>The pipeline run identifier. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="query_by_pipeline_run"
    values={[
        { label: 'query_by_pipeline_run', value: 'query_by_pipeline_run' }
    ]}
>
<TabItem value="query_by_pipeline_run">

Query activity runs based on input filter conditions.

```sql
SELECT
continuationToken,
value
FROM azure.data_factory.activity_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND factory_name = '{{ factory_name }}' -- required
AND run_id = '{{ run_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
