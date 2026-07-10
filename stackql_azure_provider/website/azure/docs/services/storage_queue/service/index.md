--- 
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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

Creates, updates, deletes, gets or lists a <code>service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_queue.service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' }
    ]}
>
<TabItem value="get_properties">

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
    <td><CopyableCode code="cors" /></td>
    <td><code>array</code></td>
    <td>The CORS properties.</td>
</tr>
<tr>
    <td><CopyableCode code="hourMetrics" /></td>
    <td><code>object</code></td>
    <td>The hour metrics properties.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>The logging properties.</td>
</tr>
<tr>
    <td><CopyableCode code="minuteMetrics" /></td>
    <td><code>object</code></td>
    <td>The minute metrics properties.</td>
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
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves properties of a storage account's Queue service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.</td>
</tr>
<tr>
    <td><a href="#set_properties"><CopyableCode code="set_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Sets properties for a storage account's Queue service endpoint, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.</td>
</tr>
<tr>
    <td><a href="#get_statistics"><CopyableCode code="get_statistics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves statistics related to replication for the Queue service. It is only available on the secondary location endpoint when read-access geo-redundant replication is enabled for the storage account.</td>
</tr>
<tr>
    <td><a href="#get_user_delegation_key"><CopyableCode code="get_user_delegation_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account"><code>account</code></a>, <a href="#parameter-expiry"><code>expiry</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves a user delegation key for the Queue service. This is only a valid operation when using bearer token authentication.</td>
</tr>
<tr>
    <td><a href="#get_queues"><CopyableCode code="get_queues" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-marker"><code>marker</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td>Returns a list of queues.</td>
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
<tr id="parameter-account">
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Storage account name. (default: )</td>
</tr>
<tr id="parameter-include">
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Specify to include additional, optional information. Default value is None.</td>
</tr>
<tr id="parameter-marker">
    <td><CopyableCode code="marker" /></td>
    <td><code>string</code></td>
    <td>Identifies the portion of the list of queues to be returned with the next listing operation. The operation returns the marker value if the listing operation did not return all queues remaining. The marker value can be used as the value for the marker parameter in a subsequent call to request the next page of list items. The marker value is opaque to the client. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of queues to return. If the request does not specify maxresults, or specifies a value greater than 5000, the server will return up to 5000 items. Default value is None.</td>
</tr>
<tr id="parameter-prefix">
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td>Filters the results to return only queues whose name begins with the specified prefix. Default value is None.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. For more information, see Setting Timeouts for Queue Service Operations.. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' }
    ]}
>
<TabItem value="get_properties">

Retrieves properties of a storage account's Queue service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

```sql
SELECT
cors,
hourMetrics,
logging,
minuteMetrics
FROM azure.storage_queue.service
WHERE account = '{{ account }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="set_properties"
    values={[
        { label: 'set_properties', value: 'set_properties' },
        { label: 'get_statistics', value: 'get_statistics' },
        { label: 'get_user_delegation_key', value: 'get_user_delegation_key' },
        { label: 'get_queues', value: 'get_queues' }
    ]}
>
<TabItem value="set_properties">

Sets properties for a storage account's Queue service endpoint, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

```sql
EXEC azure.storage_queue.service.set_properties 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"logging": "{{ logging }}", 
"hourMetrics": "{{ hourMetrics }}", 
"minuteMetrics": "{{ minuteMetrics }}", 
"cors": "{{ cors }}"
}'
;
```
</TabItem>
<TabItem value="get_statistics">

Retrieves statistics related to replication for the Queue service. It is only available on the secondary location endpoint when read-access geo-redundant replication is enabled for the storage account.

```sql
EXEC azure.storage_queue.service.get_statistics 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="get_user_delegation_key">

Retrieves a user delegation key for the Queue service. This is only a valid operation when using bearer token authentication.

```sql
EXEC azure.storage_queue.service.get_user_delegation_key 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"start": "{{ start }}", 
"expiry": "{{ expiry }}", 
"delegatedUserTid": "{{ delegatedUserTid }}"
}'
;
```
</TabItem>
<TabItem value="get_queues">

Returns a list of queues.

```sql
EXEC azure.storage_queue.service.get_queues 
@account='{{ account }}' --required, 
@prefix='{{ prefix }}', 
@marker='{{ marker }}', 
@maxresults='{{ maxresults }}', 
@timeout='{{ timeout }}', 
@include='{{ include }}'
;
```
</TabItem>
</Tabs>
