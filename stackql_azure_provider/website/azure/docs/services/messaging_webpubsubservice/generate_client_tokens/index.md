--- 
title: generate_client_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_client_tokens
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

Creates, updates, deletes, gets or lists a <code>generate_client_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="generate_client_tokens" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.messaging_webpubsubservice.generate_client_tokens" /></td></tr>
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
    <td><a href="#generate_client_token"><CopyableCode code="generate_client_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-hub"><code>hub</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-userId"><code>userId</code></a>, <a href="#parameter-minutesToExpire"><code>minutesToExpire</code></a>, <a href="#parameter-clientType"><code>clientType</code></a></td>
    <td>Generate token for the client to connect Azure Web PubSub service. Generate token for the client to connect Azure Web PubSub service.</td>
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
<tr id="parameter-hub">
    <td><CopyableCode code="hub" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-clientType">
    <td><CopyableCode code="clientType" /></td>
    <td><code>string</code></td>
    <td>The type of client. Case-insensitive. If not set, it's "Default". For Web PubSub for Socket.IO, only the default value is supported. For Web PubSub, the valid values are 'Default' and 'MQTT'. Known values are: "Default" and "MQTT". Default value is None.</td>
</tr>
<tr id="parameter-minutesToExpire">
    <td><CopyableCode code="minutesToExpire" /></td>
    <td><code>integer</code></td>
    <td>The expire time of the generated token. Default value is None.</td>
</tr>
<tr id="parameter-userId">
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>User Id. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="generate_client_token"
    values={[
        { label: 'generate_client_token', value: 'generate_client_token' }
    ]}
>
<TabItem value="generate_client_token">

Generate token for the client to connect Azure Web PubSub service. Generate token for the client to connect Azure Web PubSub service.

```sql
EXEC azure.messaging_webpubsubservice.generate_client_tokens.generate_client_token 
@hub='{{ hub }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@userId='{{ userId }}', 
@minutesToExpire='{{ minutesToExpire }}', 
@clientType='{{ clientType }}'
;
```
</TabItem>
</Tabs>
