--- 
title: communications
hide_title: false
hide_table_of_contents: false
keywords:
  - communications
  - support
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

Creates, updates, deletes, gets or lists a <code>communications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="communications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.communications" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>Body of the communication. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="communicationDirection" /></td>
    <td><code>string</code></td>
    <td>Direction of communication. Known values are: "inbound" and "outbound".</td>
</tr>
<tr>
    <td><CopyableCode code="communicationType" /></td>
    <td><code>string</code></td>
    <td>Communication type. Known values are: "web" and "phone".</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the communication was created.</td>
</tr>
<tr>
    <td><CopyableCode code="sender" /></td>
    <td><code>string</code></td>
    <td>Email address of the sender. This property is required if called by a service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>Subject of the communication. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the resource 'Microsoft.Support/communications'.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>Body of the communication. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="communicationDirection" /></td>
    <td><code>string</code></td>
    <td>Direction of communication. Known values are: "inbound" and "outbound".</td>
</tr>
<tr>
    <td><CopyableCode code="communicationType" /></td>
    <td><code>string</code></td>
    <td>Communication type. Known values are: "web" and "phone".</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the communication was created.</td>
</tr>
<tr>
    <td><CopyableCode code="sender" /></td>
    <td><code>string</code></td>
    <td>Email address of the sender. This property is required if called by a service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>Subject of the communication. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the resource 'Microsoft.Support/communications'.</td>
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
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a>, <a href="#parameter-communication_name"><code>communication_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns communication details for a support ticket.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all communications (attachments not included) for a support ticket. You can also filter support ticket communications by *CreatedDate* or *CommunicationType* using the $filter parameter. The only type of communication supported today is *Web*. Output will be a paged result with *nextLink*\ , using which you can retrieve the next set of Communication results. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a>, <a href="#parameter-communication_name"><code>communication_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Adds a new customer communication to an Azure support ticket.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Check the availability of a resource name. This API should be used to check the uniqueness of the name for adding a new communication to the support ticket.</td>
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
<tr id="parameter-communication_name">
    <td><CopyableCode code="communication_name" /></td>
    <td><code>string</code></td>
    <td>Communication name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-support_ticket_name">
    <td><CopyableCode code="support_ticket_name" /></td>
    <td><code>string</code></td>
    <td>Support ticket name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. You can filter by communicationType and createdDate properties. CommunicationType supports Equals ('eq') operator and createdDate supports Greater Than ('gt') and Greater Than or Equals ('ge') operators. You may combine the CommunicationType and CreatedDate filters by Logical And ('and') operator. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of values to return in the collection. Default is 10 and max is 10. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns communication details for a support ticket.

```sql
SELECT
id,
name,
body,
communicationDirection,
communicationType,
createdDate,
sender,
subject,
type
FROM azure.support.communications
WHERE support_ticket_name = '{{ support_ticket_name }}' -- required
AND communication_name = '{{ communication_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all communications (attachments not included) for a support ticket. You can also filter support ticket communications by *CreatedDate* or *CommunicationType* using the $filter parameter. The only type of communication supported today is *Web*. Output will be a paged result with *nextLink*\ , using which you can retrieve the next set of Communication results. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.

```sql
SELECT
id,
name,
body,
communicationDirection,
communicationType,
createdDate,
sender,
subject,
type
FROM azure.support.communications
WHERE support_ticket_name = '{{ support_ticket_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Adds a new customer communication to an Azure support ticket.

```sql
INSERT INTO azure.support.communications (
properties,
support_ticket_name,
communication_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ support_ticket_name }}',
'{{ communication_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: communications
  props:
    - name: support_ticket_name
      value: "{{ support_ticket_name }}"
      description: Required parameter for the communications resource.
    - name: communication_name
      value: "{{ communication_name }}"
      description: Required parameter for the communications resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the communications resource.
    - name: properties
      value:
        sender: "{{ sender }}"
        subject: "{{ subject }}"
        body: "{{ body }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Check the availability of a resource name. This API should be used to check the uniqueness of the name for adding a new communication to the support ticket.

```sql
EXEC azure.support.communications.check_name_availability 
@support_ticket_name='{{ support_ticket_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
