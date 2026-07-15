--- 
title: workers
hide_title: false
hide_table_of_contents: false
keywords:
  - workers
  - communication_job_router
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

Creates, updates, deletes, gets or lists a <code>workers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_job_router.workers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_worker"
    values={[
        { label: 'get_worker', value: 'get_worker' },
        { label: 'list_workers', value: 'list_workers' }
    ]}
>
<TabItem value="get_worker">

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
    <td>Id of a worker. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedJobs" /></td>
    <td><code>array</code></td>
    <td>A list of assigned jobs attached to this worker.</td>
</tr>
<tr>
    <td><CopyableCode code="availableForOffers" /></td>
    <td><code>boolean</code></td>
    <td>A flag indicating this worker is open to receive offers or not.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>The total capacity score this worker has to manage multiple concurrent jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>array</code></td>
    <td>Collection of channel(s) this worker can handle and their impact on the workers capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>A set of key/value pairs that are identifying attributes used by the rules engines to make decisions. Values must be primitive values - number, string, boolean.</td>
</tr>
<tr>
    <td><CopyableCode code="loadRatio" /></td>
    <td><code>number</code></td>
    <td>A value indicating the workers capacity. A value of '1' means all capacity is consumed. A value of '0' means no capacity is currently consumed.</td>
</tr>
<tr>
    <td><CopyableCode code="maxConcurrentOffers" /></td>
    <td><code>integer</code></td>
    <td>If this is set, the worker will only receive up to this many new offers at a time.</td>
</tr>
<tr>
    <td><CopyableCode code="offers" /></td>
    <td><code>array</code></td>
    <td>A list of active offers issued to this worker.</td>
</tr>
<tr>
    <td><CopyableCode code="queues" /></td>
    <td><code>array</code></td>
    <td>Collection of queue(s) that this worker can receive work from.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of a worker. Known values are: "active", "draining", and "inactive". (active, draining, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>A set of non-identifying attributes attached to this worker. Values must be primitive values - number, string, boolean.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_workers">

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
    <td>Id of a worker. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedJobs" /></td>
    <td><code>array</code></td>
    <td>A list of assigned jobs attached to this worker.</td>
</tr>
<tr>
    <td><CopyableCode code="availableForOffers" /></td>
    <td><code>boolean</code></td>
    <td>A flag indicating this worker is open to receive offers or not.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>integer</code></td>
    <td>The total capacity score this worker has to manage multiple concurrent jobs.</td>
</tr>
<tr>
    <td><CopyableCode code="channels" /></td>
    <td><code>array</code></td>
    <td>Collection of channel(s) this worker can handle and their impact on the workers capacity.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>A set of key/value pairs that are identifying attributes used by the rules engines to make decisions. Values must be primitive values - number, string, boolean.</td>
</tr>
<tr>
    <td><CopyableCode code="loadRatio" /></td>
    <td><code>number</code></td>
    <td>A value indicating the workers capacity. A value of '1' means all capacity is consumed. A value of '0' means no capacity is currently consumed.</td>
</tr>
<tr>
    <td><CopyableCode code="maxConcurrentOffers" /></td>
    <td><code>integer</code></td>
    <td>If this is set, the worker will only receive up to this many new offers at a time.</td>
</tr>
<tr>
    <td><CopyableCode code="offers" /></td>
    <td><code>array</code></td>
    <td>A list of active offers issued to this worker.</td>
</tr>
<tr>
    <td><CopyableCode code="queues" /></td>
    <td><code>array</code></td>
    <td>Collection of queue(s) that this worker can receive work from.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of a worker. Known values are: "active", "draining", and "inactive". (active, draining, inactive)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>A set of non-identifying attributes attached to this worker. Values must be primitive values - number, string, boolean.</td>
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
    <td><a href="#get_worker"><CopyableCode code="get_worker" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing worker by Id. Retrieves an existing worker by Id.</td>
</tr>
<tr>
    <td><a href="#list_workers"><CopyableCode code="list_workers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-state"><code>state</code></a>, <a href="#parameter-channelId"><code>channelId</code></a>, <a href="#parameter-queueId"><code>queueId</code></a>, <a href="#parameter-hasCapacity"><code>hasCapacity</code></a></td>
    <td>Retrieves existing workers. Retrieves existing workers.</td>
</tr>
<tr>
    <td><a href="#delete_worker"><CopyableCode code="delete_worker" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a worker and all of its traces. Deletes a worker and all of its traces.</td>
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
<tr id="parameter-worker_id">
    <td><CopyableCode code="worker_id" /></td>
    <td><code>string</code></td>
    <td>Id of a worker. Required.</td>
</tr>
<tr id="parameter-channelId">
    <td><CopyableCode code="channelId" /></td>
    <td><code>string</code></td>
    <td>If specified, select workers who have a channel configuration with this channel. Default value is None.</td>
</tr>
<tr id="parameter-hasCapacity">
    <td><CopyableCode code="hasCapacity" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, select only workers who have capacity for the channel specified by `channelId` or for any channel if `channelId` not specified. If set to false, then will return all workers including workers without any capacity for jobs. Defaults to false. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-queueId">
    <td><CopyableCode code="queueId" /></td>
    <td><code>string</code></td>
    <td>If specified, select workers who are assigned to this queue. Default value is None.</td>
</tr>
<tr id="parameter-state">
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>If specified, select workers by worker state. Known values are: "active", "draining", "inactive", and "all". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_worker"
    values={[
        { label: 'get_worker', value: 'get_worker' },
        { label: 'list_workers', value: 'list_workers' }
    ]}
>
<TabItem value="get_worker">

Retrieves an existing worker by Id. Retrieves an existing worker by Id.

```sql
SELECT
id,
assignedJobs,
availableForOffers,
capacity,
channels,
etag,
labels,
loadRatio,
maxConcurrentOffers,
offers,
queues,
state,
tags
FROM azure.communication_job_router.workers
WHERE worker_id = '{{ worker_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_workers">

Retrieves existing workers. Retrieves existing workers.

```sql
SELECT
id,
assignedJobs,
availableForOffers,
capacity,
channels,
etag,
labels,
loadRatio,
maxConcurrentOffers,
offers,
queues,
state,
tags
FROM azure.communication_job_router.workers
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
AND state = '{{ state }}'
AND channelId = '{{ channelId }}'
AND queueId = '{{ queueId }}'
AND hasCapacity = '{{ hasCapacity }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_worker"
    values={[
        { label: 'delete_worker', value: 'delete_worker' }
    ]}
>
<TabItem value="delete_worker">

Deletes a worker and all of its traces. Deletes a worker and all of its traces.

```sql
DELETE FROM azure.communication_job_router.workers
WHERE worker_id = '{{ worker_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
