--- 
title: sms
hide_title: false
hide_table_of_contents: false
keywords:
  - sms
  - communication_sms
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

Creates, updates, deletes, gets or lists a <code>sms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sms" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_sms.sms" /></td></tr>
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
    <td><a href="#send"><CopyableCode code="send" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-smsRecipients"><code>smsRecipients</code></a>, <a href="#parameter-message"><code>message</code></a></td>
    <td></td>
    <td>Sends a SMS message from a phone number that belongs to the authenticated account. Sends a SMS message from a phone number that belongs to the authenticated account.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="send"
    values={[
        { label: 'send', value: 'send' }
    ]}
>
<TabItem value="send">

Sends a SMS message from a phone number that belongs to the authenticated account. Sends a SMS message from a phone number that belongs to the authenticated account.

```sql
EXEC azure.communication_sms.sms.send 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"from": "{{ from }}", 
"smsRecipients": "{{ smsRecipients }}", 
"message": "{{ message }}", 
"smsSendOptions": "{{ smsSendOptions }}"
}'
;
```
</TabItem>
</Tabs>
