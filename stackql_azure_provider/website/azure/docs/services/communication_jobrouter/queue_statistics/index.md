--- 
title: queue_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_statistics
  - communication_jobrouter
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

Creates, updates, deletes, gets or lists a <code>queue_statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queue_statistics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_jobrouter.queue_statistics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_queue_statistics"
    values={[
        { label: 'get_queue_statistics', value: 'get_queue_statistics' }
    ]}
>
<TabItem value="get_queue_statistics">

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
    <td><CopyableCode code="estimatedWaitTimeMinutes" /></td>
    <td><code>object</code></td>
    <td>The estimated wait time of this queue rounded up to the nearest minute, grouped by job priority.</td>
</tr>
<tr>
    <td><CopyableCode code="length" /></td>
    <td><code>integer</code></td>
    <td>Length of the queue: total number of enqueued jobs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longestJobWaitTimeMinutes" /></td>
    <td><code>number</code></td>
    <td>The wait time of the job that has been enqueued in this queue for the longest.</td>
</tr>
<tr>
    <td><CopyableCode code="queueId" /></td>
    <td><code>string</code></td>
    <td>Id of the queue these details are about. Required.</td>
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
    <td><a href="#get_queue_statistics"><CopyableCode code="get_queue_statistics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves a queue's statistics. Retrieves a queue's statistics.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-queue_id">
    <td><CopyableCode code="queue_id" /></td>
    <td><code>string</code></td>
    <td>Id of the queue to retrieve statistics. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_queue_statistics"
    values={[
        { label: 'get_queue_statistics', value: 'get_queue_statistics' }
    ]}
>
<TabItem value="get_queue_statistics">

Retrieves a queue's statistics. Retrieves a queue's statistics.

```sql
SELECT
estimatedWaitTimeMinutes,
length,
longestJobWaitTimeMinutes,
queueId
FROM azure.communication_jobrouter.queue_statistics
WHERE queue_id = '{{ queue_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
