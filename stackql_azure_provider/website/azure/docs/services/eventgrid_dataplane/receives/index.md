--- 
title: receives
hide_title: false
hide_table_of_contents: false
keywords:
  - receives
  - eventgrid_dataplane
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

Creates, updates, deletes, gets or lists a <code>receives</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="receives" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid_dataplane.receives" /></td></tr>
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
    <td><a href="#receive"><CopyableCode code="receive" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxEvents"><code>maxEvents</code></a>, <a href="#parameter-maxWaitTime"><code>maxWaitTime</code></a></td>
    <td>Receive a batch of Cloud Events from a subscription.</td>
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
<tr id="parameter-event_subscription_name">
    <td><CopyableCode code="event_subscription_name" /></td>
    <td><code>string</code></td>
    <td>Event Subscription Name. Required.</td>
</tr>
<tr id="parameter-topic_name">
    <td><CopyableCode code="topic_name" /></td>
    <td><code>string</code></td>
    <td>Topic Name. Required.</td>
</tr>
<tr id="parameter-maxEvents">
    <td><CopyableCode code="maxEvents" /></td>
    <td><code>integer</code></td>
    <td>Max Events count to be received. Minimum value is 1, while maximum value is 100 events. If not specified, the default value is 1. Default value is None.</td>
</tr>
<tr id="parameter-maxWaitTime">
    <td><CopyableCode code="maxWaitTime" /></td>
    <td><code>integer</code></td>
    <td>Max wait time value for receive operation in Seconds. It is the time in seconds that the server approximately waits for the availability of an event and responds to the request. If an event is available, the broker responds immediately to the client. Minimum value is 10 seconds, while maximum value is 120 seconds. If not specified, the default value is 60 seconds. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="receive"
    values={[
        { label: 'receive', value: 'receive' }
    ]}
>
<TabItem value="receive">

Receive a batch of Cloud Events from a subscription.

```sql
EXEC azure.eventgrid_dataplane.receives.receive 
@topic_name='{{ topic_name }}' --required, 
@event_subscription_name='{{ event_subscription_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@maxEvents='{{ maxEvents }}', 
@maxWaitTime='{{ maxWaitTime }}'
;
```
</TabItem>
</Tabs>
