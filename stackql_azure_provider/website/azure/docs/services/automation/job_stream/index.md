--- 
title: job_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - job_stream
  - automation
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

Creates, updates, deletes, gets or lists a <code>job_stream</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_stream" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.job_stream" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_job', value: 'list_by_job' }
    ]}
>
<TabItem value="get">

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
    <td>Gets or sets the id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="jobStreamId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the id of the job stream.</td>
</tr>
<tr>
    <td><CopyableCode code="streamText" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the stream text.</td>
</tr>
<tr>
    <td><CopyableCode code="streamType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the stream type. Known values are: "Progress", "Output", "Warning", "Error", "Debug", "Verbose", and "Any". (Progress, Output, Warning, Error, Debug, Verbose, Any)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the summary.</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the creation time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the values of the job stream.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_job">

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
    <td>Gets or sets the id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="jobStreamId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the id of the job stream.</td>
</tr>
<tr>
    <td><CopyableCode code="streamText" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the stream text.</td>
</tr>
<tr>
    <td><CopyableCode code="streamType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the stream type. Known values are: "Progress", "Output", "Warning", "Error", "Debug", "Verbose", and "Any". (Progress, Output, Warning, Error, Debug, Verbose, Any)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the summary.</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the creation time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the values of the job stream.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-job_stream_id"><code>job_stream_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Retrieve the job stream identified by job stream id.</td>
</tr>
<tr>
    <td><a href="#list_by_job"><CopyableCode code="list_by_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-job_name"><code>job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Retrieve a list of jobs streams identified by job name.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-job_name">
    <td><CopyableCode code="job_name" /></td>
    <td><code>string</code></td>
    <td>The job name. Required.</td>
</tr>
<tr id="parameter-job_stream_id">
    <td><CopyableCode code="job_stream_id" /></td>
    <td><code>string</code></td>
    <td>The job stream id. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-clientRequestId">
    <td><CopyableCode code="clientRequestId" /></td>
    <td><code>string</code></td>
    <td>Identifies this specific client request. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_job', value: 'list_by_job' }
    ]}
>
<TabItem value="get">

Retrieve the job stream identified by job stream id.

```sql
SELECT
id,
jobStreamId,
streamText,
streamType,
summary,
time,
value
FROM azure.automation.job_stream
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND job_stream_id = '{{ job_stream_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND clientRequestId = '{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="list_by_job">

Retrieve a list of jobs streams identified by job name.

```sql
SELECT
id,
jobStreamId,
streamText,
streamType,
summary,
time,
value
FROM azure.automation.job_stream
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND job_name = '{{ job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND clientRequestId = '{{ clientRequestId }}'
;
```
</TabItem>
</Tabs>
