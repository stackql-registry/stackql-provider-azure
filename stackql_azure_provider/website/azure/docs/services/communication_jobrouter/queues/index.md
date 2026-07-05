--- 
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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

Creates, updates, deletes, gets or lists a <code>queues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queues" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_jobrouter.queues" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_queue"
    values={[
        { label: 'get_queue', value: 'get_queue' },
        { label: 'list_queues', value: 'list_queues' }
    ]}
>
<TabItem value="get_queue">

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
    <td>Id of a queue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of this queue.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionPolicyId" /></td>
    <td><code>string</code></td>
    <td>Id of a distribution policy that will determine how a job is distributed to workers.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exceptionPolicyId" /></td>
    <td><code>string</code></td>
    <td>Id of an exception policy that determines various job escalation rules.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>A set of key/value pairs that are identifying attributes used by the rules engines to make decisions. Values must be primitive values - number, string, boolean.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_queues">

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
    <td>Id of a queue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Friendly name of this queue.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionPolicyId" /></td>
    <td><code>string</code></td>
    <td>Id of a distribution policy that will determine how a job is distributed to workers.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag for this resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exceptionPolicyId" /></td>
    <td><code>string</code></td>
    <td>Id of an exception policy that determines various job escalation rules.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>object</code></td>
    <td>A set of key/value pairs that are identifying attributes used by the rules engines to make decisions. Values must be primitive values - number, string, boolean.</td>
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
    <td><a href="#get_queue"><CopyableCode code="get_queue" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves an existing queue by Id. Retrieves an existing queue by Id.</td>
</tr>
<tr>
    <td><a href="#list_queues"><CopyableCode code="list_queues" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Retrieves existing queues. Retrieves existing queues.</td>
</tr>
<tr>
    <td><a href="#delete_queue"><CopyableCode code="delete_queue" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a queue by Id. Deletes a queue by Id.</td>
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
<tr id="parameter-queue_id">
    <td><CopyableCode code="queue_id" /></td>
    <td><code>string</code></td>
    <td>Id of a queue. Required.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_queue"
    values={[
        { label: 'get_queue', value: 'get_queue' },
        { label: 'list_queues', value: 'list_queues' }
    ]}
>
<TabItem value="get_queue">

Retrieves an existing queue by Id. Retrieves an existing queue by Id.

```sql
SELECT
id,
name,
distributionPolicyId,
etag,
exceptionPolicyId,
labels
FROM azure.communication_jobrouter.queues
WHERE queue_id = '{{ queue_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_queues">

Retrieves existing queues. Retrieves existing queues.

```sql
SELECT
id,
name,
distributionPolicyId,
etag,
exceptionPolicyId,
labels
FROM azure.communication_jobrouter.queues
WHERE endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_queue"
    values={[
        { label: 'delete_queue', value: 'delete_queue' }
    ]}
>
<TabItem value="delete_queue">

Deletes a queue by Id. Deletes a queue by Id.

```sql
DELETE FROM azure.communication_jobrouter.queues
WHERE queue_id = '{{ queue_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
