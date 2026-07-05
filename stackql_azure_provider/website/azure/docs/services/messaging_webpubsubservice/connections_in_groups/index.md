--- 
title: connections_in_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - connections_in_groups
  - messaging_webpubsubservice
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

Creates, updates, deletes, gets or lists a <code>connections_in_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connections_in_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.connections_in_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_connections_in_group"
    values={[
        { label: 'list_connections_in_group', value: 'list_connections_in_group' }
    ]}
>
<TabItem value="list_connections_in_group">

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
    <td><CopyableCode code="connectionId" /></td>
    <td><code>string</code></td>
    <td>Connection Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>User Id.</td>
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
    <td><a href="#list_connections_in_group"><CopyableCode code="list_connections_in_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group"><code>group</code></a>, <a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a></td>
    <td>List connections in a group. List connections in a group.</td>
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
<tr id="parameter-group">
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>Target group name, whose length should be greater than 0 and less than 1025. Required.</td>
</tr>
<tr id="parameter-hub">
    <td><CopyableCode code="hub" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>A token that allows the client to retrieve the next page of results. This parameter is provided by the service in the response of a previous request when there are additional results to be fetched. Clients should include the continuationToken in the next request to receive the subsequent page of data. If this parameter is omitted, the server will return the first page of results. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of connections to return. If the value is not set, then all the connections in a group are returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_connections_in_group"
    values={[
        { label: 'list_connections_in_group', value: 'list_connections_in_group' }
    ]}
>
<TabItem value="list_connections_in_group">

List connections in a group. List connections in a group.

```sql
SELECT
connectionId,
userId
FROM azure.messaging_webpubsubservice.connections_in_groups
WHERE group = '{{ group }}' -- required
AND hub = '{{ hub }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND maxpagesize = '{{ maxpagesize }}'
AND top = '{{ top }}'
AND continuationToken = '{{ continuationToken }}'
;
```
</TabItem>
</Tabs>
