--- 
title: queue
hide_title: false
hide_table_of_contents: false
keywords:
  - queue
  - storage_queue
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

Creates, updates, deletes, gets or lists a <code>queue</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queue" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_queue.queue" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_access_policy"
    values={[
        { label: 'get_access_policy', value: 'get_access_policy' }
    ]}
>
<TabItem value="get_access_policy">

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
    <td><CopyableCode code="items_" /></td>
    <td><code>array</code></td>
    <td>The list of signed identifiers. Required.</td>
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
    <td><a href="#get_access_policy"><CopyableCode code="get_access_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the access policy for the specified queue.</td>
</tr>
<tr>
    <td><a href="#update_message"><CopyableCode code="update_message" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-popreceipt"><code>popreceipt</code></a>, <a href="#parameter-visibilitytimeout"><code>visibilitytimeout</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-messageText"><code>messageText</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Updates the visibility timeout of a message. This operation can also be used to update the contents of a message.</td>
</tr>
<tr>
    <td><a href="#set_access_policy"><CopyableCode code="set_access_policy" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-url"><code>url</code></a>, <a href="#parameter-items_"><code>items_</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Sets the permissions for the specified queue.</td>
</tr>
<tr>
    <td><a href="#set_metadata"><CopyableCode code="set_metadata" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-x-ms-meta"><code>x-ms-meta</code></a></td>
    <td>Sets user-defined metadata for the specified queue.</td>
</tr>
<tr>
    <td><a href="#delete_message"><CopyableCode code="delete_message" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-popreceipt"><code>popreceipt</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes the specified message.</td>
</tr>
<tr>
    <td><a href="#clear"><CopyableCode code="clear" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes all messages from the specified queue.</td>
</tr>
<tr>
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Returns all user-defined metadata and system properties for the specified queue.</td>
</tr>
<tr>
    <td><a href="#receive_messages"><CopyableCode code="receive_messages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-numofmessages"><code>numofmessages</code></a>, <a href="#parameter-visibilitytimeout"><code>visibilitytimeout</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves one or more messages from the front of the queue.</td>
</tr>
<tr>
    <td><a href="#send_message"><CopyableCode code="send_message" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-url"><code>url</code></a>, <a href="#parameter-messageText"><code>messageText</code></a></td>
    <td><a href="#parameter-visibilitytimeout"><code>visibilitytimeout</code></a>, <a href="#parameter-messagettl"><code>messagettl</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Adds a new message to the back of the message queue. A visibility timeout can also be specified to make the message invisible until the visibility timeout expires.</td>
</tr>
<tr>
    <td><a href="#peek_messages"><CopyableCode code="peek_messages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-numofmessages"><code>numofmessages</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves one or more messages from the front of the queue, but does not alter the visibility of the message.</td>
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
<tr id="parameter-message_id">
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the queue message. Required.</td>
</tr>
<tr id="parameter-popreceipt">
    <td><CopyableCode code="popreceipt" /></td>
    <td><code>string</code></td>
    <td>An opaque value required to delete the message. If deletion fails using this PopReceipt then the message has been dequeued by another client. Required.</td>
</tr>
<tr id="parameter-url">
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `url` parameter. (default: )</td>
</tr>
<tr id="parameter-visibilitytimeout">
    <td><CopyableCode code="visibilitytimeout" /></td>
    <td><code>integer</code></td>
    <td>Specifies the new visibility timeout value, in seconds, relative to server time. A specified value must be larger than or equal to 1 second, and cannot be larger than 7 days. The visibility timeout of a message can be set to a value later than the expiry time. Required.</td>
</tr>
<tr id="parameter-messagettl">
    <td><CopyableCode code="messagettl" /></td>
    <td><code>integer</code></td>
    <td>Specifies the time-to-live interval for the message, in seconds. Prior to version 2017-07-29, the maximum time-to-live allowed is 7 days. For version 2017-07-29 or later, the maximum time-to-live can be any positive number, as well as -1 indicating that the message does not expire. If this parameter is omitted, the default time-to-live is 7 days. Default value is None.</td>
</tr>
<tr id="parameter-numofmessages">
    <td><CopyableCode code="numofmessages" /></td>
    <td><code>integer</code></td>
    <td>A nonzero integer value that specifies the number of messages to retrieve from the queue, up to a maximum of 32. If fewer are visible, the visible messages are returned. By default, a single message is retrieved from the queue with this operation. Default value is None.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see Setting Timeouts for Queue Service Operations.. Default value is None.</td>
</tr>
<tr id="parameter-visibilitytimeout">
    <td><CopyableCode code="visibilitytimeout" /></td>
    <td><code>integer</code></td>
    <td>Specifies the new visibility timeout value, in seconds, relative to server time. A specified value must be larger than or equal to 1 second, and cannot be larger than 7 days. The visibility timeout of a message can be set to a value later than the expiry time. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-meta">
    <td><CopyableCode code="x-ms-meta" /></td>
    <td><code>string</code></td>
    <td>The metadata headers. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_access_policy"
    values={[
        { label: 'get_access_policy', value: 'get_access_policy' }
    ]}
>
<TabItem value="get_access_policy">

Gets the access policy for the specified queue.

```sql
SELECT
items_
FROM azure.storage_queue.queue
WHERE url = '{{ url }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_message"
    values={[
        { label: 'update_message', value: 'update_message' }
    ]}
>
<TabItem value="update_message">

Updates the visibility timeout of a message. This operation can also be used to update the contents of a message.

```sql
UPDATE azure.storage_queue.queue
SET 
messageText = '{{ messageText }}'
WHERE 
message_id = '{{ message_id }}' --required
AND popreceipt = '{{ popreceipt }}' --required
AND visibilitytimeout = '{{ visibilitytimeout }}' --required
AND url = '{{ url }}' --required
AND messageText = '{{ messageText }}' --required
AND timeout = '{{ timeout}}';
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_access_policy"
    values={[
        { label: 'set_access_policy', value: 'set_access_policy' },
        { label: 'set_metadata', value: 'set_metadata' }
    ]}
>
<TabItem value="set_access_policy">

Sets the permissions for the specified queue.

```sql
REPLACE azure.storage_queue.queue
SET 
items_ = '{{ items_ }}'
WHERE 
url = '{{ url }}' --required
AND items_ = '{{ items_ }}' --required
AND timeout = '{{ timeout}}';
```
</TabItem>
<TabItem value="set_metadata">

Sets user-defined metadata for the specified queue.

```sql
REPLACE azure.storage_queue.queue
SET 
-- No updatable properties
WHERE 
url = '{{ url }}' --required
AND timeout = '{{ timeout}}'
AND x-ms-meta = '{{ x-ms-meta}}';
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_message"
    values={[
        { label: 'delete_message', value: 'delete_message' },
        { label: 'clear', value: 'clear' }
    ]}
>
<TabItem value="delete_message">

Deletes the specified message.

```sql
DELETE FROM azure.storage_queue.queue
WHERE message_id = '{{ message_id }}' --required
AND popreceipt = '{{ popreceipt }}' --required
AND url = '{{ url }}' --required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
<TabItem value="clear">

Deletes all messages from the specified queue.

```sql
DELETE FROM azure.storage_queue.queue
WHERE url = '{{ url }}' --required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' },
        { label: 'receive_messages', value: 'receive_messages' },
        { label: 'send_message', value: 'send_message' },
        { label: 'peek_messages', value: 'peek_messages' }
    ]}
>
<TabItem value="get_properties">

Returns all user-defined metadata and system properties for the specified queue.

```sql
EXEC azure.storage_queue.queue.get_properties 
@url='{{ url }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="receive_messages">

Retrieves one or more messages from the front of the queue.

```sql
EXEC azure.storage_queue.queue.receive_messages 
@url='{{ url }}' --required, 
@numofmessages='{{ numofmessages }}', 
@visibilitytimeout='{{ visibilitytimeout }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="send_message">

Adds a new message to the back of the message queue. A visibility timeout can also be specified to make the message invisible until the visibility timeout expires.

```sql
EXEC azure.storage_queue.queue.send_message 
@url='{{ url }}' --required, 
@visibilitytimeout='{{ visibilitytimeout }}', 
@messagettl='{{ messagettl }}', 
@timeout='{{ timeout }}' 
@@json=
'{
"messageText": "{{ messageText }}"
}'
;
```
</TabItem>
<TabItem value="peek_messages">

Retrieves one or more messages from the front of the queue, but does not alter the visibility of the message.

```sql
EXEC azure.storage_queue.queue.peek_messages 
@url='{{ url }}' --required, 
@numofmessages='{{ numofmessages }}', 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
