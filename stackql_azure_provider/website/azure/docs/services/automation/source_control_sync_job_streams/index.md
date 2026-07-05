--- 
title: source_control_sync_job_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_job_streams
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

Creates, updates, deletes, gets or lists a <code>source_control_sync_job_streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="source_control_sync_job_streams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control_sync_job_streams" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sync_job', value: 'list_by_sync_job' }
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
    <td>Resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceControlSyncJobStreamId" /></td>
    <td><code>string</code></td>
    <td>The sync job stream id.</td>
</tr>
<tr>
    <td><CopyableCode code="streamText" /></td>
    <td><code>string</code></td>
    <td>The text of the sync job stream.</td>
</tr>
<tr>
    <td><CopyableCode code="streamType" /></td>
    <td><code>string</code></td>
    <td>The type of the sync job stream. Known values are: "Error" and "Output". (Error, Output)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>The summary of the sync job stream.</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the sync job stream.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>object</code></td>
    <td>The values of the job stream.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_sync_job">

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
    <td>Resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceControlSyncJobStreamId" /></td>
    <td><code>string</code></td>
    <td>The sync job stream id.</td>
</tr>
<tr>
    <td><CopyableCode code="streamType" /></td>
    <td><code>string</code></td>
    <td>The type of the sync job stream. Known values are: "Error" and "Output". (Error, Output)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>The summary of the sync job stream.</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the sync job stream.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-source_control_sync_job_id"><code>source_control_sync_job_id</code></a>, <a href="#parameter-stream_id"><code>stream_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a sync job stream identified by stream id.</td>
</tr>
<tr>
    <td><a href="#list_by_sync_job"><CopyableCode code="list_by_sync_job" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-source_control_sync_job_id"><code>source_control_sync_job_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieve a list of sync job streams identified by sync job id.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-source_control_name">
    <td><CopyableCode code="source_control_name" /></td>
    <td><code>string</code></td>
    <td>The name of source control. Required.</td>
</tr>
<tr id="parameter-source_control_sync_job_id">
    <td><CopyableCode code="source_control_sync_job_id" /></td>
    <td><code>string</code></td>
    <td>The source control sync job id. Required.</td>
</tr>
<tr id="parameter-stream_id">
    <td><CopyableCode code="stream_id" /></td>
    <td><code>string</code></td>
    <td>The id of the sync job stream. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sync_job', value: 'list_by_sync_job' }
    ]}
>
<TabItem value="get">

Retrieve a sync job stream identified by stream id.

```sql
SELECT
id,
sourceControlSyncJobStreamId,
streamText,
streamType,
summary,
time,
value
FROM azure.automation.source_control_sync_job_streams
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND source_control_name = '{{ source_control_name }}' -- required
AND source_control_sync_job_id = '{{ source_control_sync_job_id }}' -- required
AND stream_id = '{{ stream_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sync_job">

Retrieve a list of sync job streams identified by sync job id.

```sql
SELECT
id,
sourceControlSyncJobStreamId,
streamType,
summary,
time
FROM azure.automation.source_control_sync_job_streams
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND source_control_name = '{{ source_control_name }}' -- required
AND source_control_sync_job_id = '{{ source_control_sync_job_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
