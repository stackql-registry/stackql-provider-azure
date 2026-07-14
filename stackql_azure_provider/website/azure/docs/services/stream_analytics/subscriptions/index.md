--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_quotas"
    values={[
        { label: 'list_quotas', value: 'list_quotas' }
    ]}
>
<TabItem value="list_quotas">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="currentCount" /></td>
    <td><code>integer</code></td>
    <td>The current usage of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCount" /></td>
    <td><code>integer</code></td>
    <td>The max permitted usage of this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#list_quotas"><CopyableCode code="list_quotas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the subscription's current quota information in a particular region.</td>
</tr>
<tr>
    <td><a href="#test_query"><CopyableCode code="test_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-streamingJob"><code>streamingJob</code></a></td>
    <td></td>
    <td>Test the Stream Analytics query on a sample input.</td>
</tr>
<tr>
    <td><a href="#compile_query"><CopyableCode code="compile_query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-jobType"><code>jobType</code></a></td>
    <td></td>
    <td>Compile the Stream Analytics query.</td>
</tr>
<tr>
    <td><a href="#sample_input"><CopyableCode code="sample_input" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sample the Stream Analytics input data.</td>
</tr>
<tr>
    <td><a href="#test_input"><CopyableCode code="test_input" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-input"><code>input</code></a></td>
    <td></td>
    <td>Test the Stream Analytics input.</td>
</tr>
<tr>
    <td><a href="#test_output"><CopyableCode code="test_output" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-output"><code>output</code></a></td>
    <td></td>
    <td>Test the Stream Analytics output.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The region to which the request is sent. You can find out which regions Azure Stream Analytics is supported in here: https://azure.microsoft.com/en-us/regions/. Required.</td>
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
    defaultValue="list_quotas"
    values={[
        { label: 'list_quotas', value: 'list_quotas' }
    ]}
>
<TabItem value="list_quotas">

Retrieves the subscription's current quota information in a particular region.

```sql
SELECT
id,
name,
currentCount,
maxCount,
type
FROM azure.stream_analytics.subscriptions
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="test_query"
    values={[
        { label: 'test_query', value: 'test_query' },
        { label: 'compile_query', value: 'compile_query' },
        { label: 'sample_input', value: 'sample_input' },
        { label: 'test_input', value: 'test_input' },
        { label: 'test_output', value: 'test_output' }
    ]}
>
<TabItem value="test_query">

Test the Stream Analytics query on a sample input.

```sql
EXEC azure.stream_analytics.subscriptions.test_query 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"diagnostics": "{{ diagnostics }}", 
"streamingJob": "{{ streamingJob }}"
}'
;
```
</TabItem>
<TabItem value="compile_query">

Compile the Stream Analytics query.

```sql
EXEC azure.stream_analytics.subscriptions.compile_query 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"query": "{{ query }}", 
"inputs": "{{ inputs }}", 
"functions": "{{ functions }}", 
"jobType": "{{ jobType }}", 
"compatibilityLevel": "{{ compatibilityLevel }}"
}'
;
```
</TabItem>
<TabItem value="sample_input">

Sample the Stream Analytics input data.

```sql
EXEC azure.stream_analytics.subscriptions.sample_input 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"input": "{{ input }}", 
"compatibilityLevel": "{{ compatibilityLevel }}", 
"eventsUri": "{{ eventsUri }}", 
"dataLocale": "{{ dataLocale }}"
}'
;
```
</TabItem>
<TabItem value="test_input">

Test the Stream Analytics input.

```sql
EXEC azure.stream_analytics.subscriptions.test_input 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"input": "{{ input }}"
}'
;
```
</TabItem>
<TabItem value="test_output">

Test the Stream Analytics output.

```sql
EXEC azure.stream_analytics.subscriptions.test_output 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"output": "{{ output }}"
}'
;
```
</TabItem>
</Tabs>
