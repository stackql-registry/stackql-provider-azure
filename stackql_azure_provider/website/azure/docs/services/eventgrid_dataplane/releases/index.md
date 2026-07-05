--- 
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
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

Creates, updates, deletes, gets or lists a <code>releases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="releases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid_dataplane.releases" /></td></tr>
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
    <td><a href="#release"><CopyableCode code="release" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-releaseDelayInSeconds"><code>releaseDelayInSeconds</code></a></td>
    <td>Release a batch of Cloud Events. The response will include the set of successfully released lock tokens, along with other failed lock tokens with their corresponding error information. Successfully released events can be received by consumers.</td>
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
<tr id="parameter-releaseDelayInSeconds">
    <td><CopyableCode code="releaseDelayInSeconds" /></td>
    <td><code>string</code></td>
    <td>Release cloud events with the specified delay in seconds. Known values are: "0", "10", "60", "600", and "3600". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="release"
    values={[
        { label: 'release', value: 'release' }
    ]}
>
<TabItem value="release">

Release a batch of Cloud Events. The response will include the set of successfully released lock tokens, along with other failed lock tokens with their corresponding error information. Successfully released events can be received by consumers.

```sql
EXEC azure.eventgrid_dataplane.releases.release 
@topic_name='{{ topic_name }}' --required, 
@event_subscription_name='{{ event_subscription_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@releaseDelayInSeconds='{{ releaseDelayInSeconds }}'
;
```
</TabItem>
</Tabs>
