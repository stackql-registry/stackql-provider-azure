--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - service_bus
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_topic', value: 'list_by_topic' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="accessedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time there was a receive request to this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteOnIdle" /></td>
    <td><code>string</code></td>
    <td>ISO 8061 timeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffineProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to client affine subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="countDetails" /></td>
    <td><code>object</code></td>
    <td>Message count details.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the message was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetteringOnFilterEvaluationExceptions" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether a subscription has dead letter support on filter evaluation exceptions.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetteringOnMessageExpiration" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether a subscription has dead letter support when a message expires.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMessageTimeToLive" /></td>
    <td><code>string</code></td>
    <td>ISO 8061 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</td>
</tr>
<tr>
    <td><CopyableCode code="duplicateDetectionHistoryTimeWindow" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBatchedOperations" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether server-side batched operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardDeadLetteredMessagesTo" /></td>
    <td><code>string</code></td>
    <td>Queue/Topic name to forward the Dead Letter message.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardTo" /></td>
    <td><code>string</code></td>
    <td>Queue/Topic name to forward the messages.</td>
</tr>
<tr>
    <td><CopyableCode code="isClientAffine" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether the subscription has an affinity to the client id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="lockDuration" /></td>
    <td><code>string</code></td>
    <td>ISO 8061 lock duration timespan for the subscription. The default value is 1 minute.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDeliveryCount" /></td>
    <td><code>integer</code></td>
    <td>Number of maximum deliveries.</td>
</tr>
<tr>
    <td><CopyableCode code="messageCount" /></td>
    <td><code>integer</code></td>
    <td>Number of messages.</td>
</tr>
<tr>
    <td><CopyableCode code="requiresSession" /></td>
    <td><code>boolean</code></td>
    <td>Value indicating if a subscription supports the concept of sessions.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Enumerates the possible values for the status of a messaging entity. Known values are: "Active", "Disabled", "Restoring", "SendDisabled", "ReceiveDisabled", "Creating", "Deleting", "Renaming", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The exact time the message was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_topic">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="accessedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time there was a receive request to this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteOnIdle" /></td>
    <td><code>string</code></td>
    <td>ISO 8061 timeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffineProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to client affine subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="countDetails" /></td>
    <td><code>object</code></td>
    <td>Message count details.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the message was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetteringOnFilterEvaluationExceptions" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether a subscription has dead letter support on filter evaluation exceptions.</td>
</tr>
<tr>
    <td><CopyableCode code="deadLetteringOnMessageExpiration" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether a subscription has dead letter support when a message expires.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultMessageTimeToLive" /></td>
    <td><code>string</code></td>
    <td>ISO 8061 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</td>
</tr>
<tr>
    <td><CopyableCode code="duplicateDetectionHistoryTimeWindow" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBatchedOperations" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether server-side batched operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardDeadLetteredMessagesTo" /></td>
    <td><code>string</code></td>
    <td>Queue/Topic name to forward the Dead Letter message.</td>
</tr>
<tr>
    <td><CopyableCode code="forwardTo" /></td>
    <td><code>string</code></td>
    <td>Queue/Topic name to forward the messages.</td>
</tr>
<tr>
    <td><CopyableCode code="isClientAffine" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether the subscription has an affinity to the client id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="lockDuration" /></td>
    <td><code>string</code></td>
    <td>ISO 8061 lock duration timespan for the subscription. The default value is 1 minute.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDeliveryCount" /></td>
    <td><code>integer</code></td>
    <td>Number of maximum deliveries.</td>
</tr>
<tr>
    <td><CopyableCode code="messageCount" /></td>
    <td><code>integer</code></td>
    <td>Number of messages.</td>
</tr>
<tr>
    <td><CopyableCode code="requiresSession" /></td>
    <td><code>boolean</code></td>
    <td>Value indicating if a subscription supports the concept of sessions.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Enumerates the possible values for the status of a messaging entity. Known values are: "Active", "Disabled", "Restoring", "SendDisabled", "ReceiveDisabled", "Creating", "Deleting", "Renaming", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The exact time the message was updated.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_name"><code>subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a subscription description for the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639402.aspx</td>
</tr>
<tr>
    <td><a href="#list_by_topic"><CopyableCode code="list_by_topic" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List all the subscriptions under a specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639400.aspx</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_name"><code>subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a topic subscription. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639385.aspx</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_name"><code>subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a topic subscription. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639385.aspx</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_name"><code>subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a subscription from the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639381.aspx</td>
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
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The namespace name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Resource group within the Azure subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-subscription_name">
    <td><CopyableCode code="subscription_name" /></td>
    <td><code>string</code></td>
    <td>The subscription name. Required.</td>
</tr>
<tr id="parameter-topic_name">
    <td><CopyableCode code="topic_name" /></td>
    <td><code>string</code></td>
    <td>The topic name. Required.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>May be used to limit the number of results to the most recent N usageDetails. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_topic', value: 'list_by_topic' }
    ]}
>
<TabItem value="get">

Returns a subscription description for the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639402.aspx

```sql
SELECT
id,
name,
accessedAt,
autoDeleteOnIdle,
clientAffineProperties,
countDetails,
createdAt,
deadLetteringOnFilterEvaluationExceptions,
deadLetteringOnMessageExpiration,
defaultMessageTimeToLive,
duplicateDetectionHistoryTimeWindow,
enableBatchedOperations,
forwardDeadLetteredMessagesTo,
forwardTo,
isClientAffine,
location,
lockDuration,
maxDeliveryCount,
messageCount,
requiresSession,
status,
systemData,
type,
updatedAt
FROM azure.service_bus.subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND subscription_name = '{{ subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_topic">

List all the subscriptions under a specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639400.aspx

```sql
SELECT
id,
name,
accessedAt,
autoDeleteOnIdle,
clientAffineProperties,
countDetails,
createdAt,
deadLetteringOnFilterEvaluationExceptions,
deadLetteringOnMessageExpiration,
defaultMessageTimeToLive,
duplicateDetectionHistoryTimeWindow,
enableBatchedOperations,
forwardDeadLetteredMessagesTo,
forwardTo,
isClientAffine,
location,
lockDuration,
maxDeliveryCount,
messageCount,
requiresSession,
status,
systemData,
type,
updatedAt
FROM azure.service_bus.subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates a topic subscription. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639385.aspx

```sql
INSERT INTO azure.service_bus.subscriptions (
properties,
resource_group_name,
namespace_name,
topic_name,
subscription_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ topic_name }}',
'{{ subscription_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: subscriptions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the subscriptions resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the subscriptions resource.
    - name: topic_name
      value: "{{ topic_name }}"
      description: Required parameter for the subscriptions resource.
    - name: subscription_name
      value: "{{ subscription_name }}"
      description: Required parameter for the subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the subscriptions resource.
    - name: properties
      value:
        lockDuration: "{{ lockDuration }}"
        requiresSession: {{ requiresSession }}
        defaultMessageTimeToLive: "{{ defaultMessageTimeToLive }}"
        deadLetteringOnFilterEvaluationExceptions: {{ deadLetteringOnFilterEvaluationExceptions }}
        deadLetteringOnMessageExpiration: {{ deadLetteringOnMessageExpiration }}
        duplicateDetectionHistoryTimeWindow: "{{ duplicateDetectionHistoryTimeWindow }}"
        maxDeliveryCount: {{ maxDeliveryCount }}
        status: "{{ status }}"
        enableBatchedOperations: {{ enableBatchedOperations }}
        autoDeleteOnIdle: "{{ autoDeleteOnIdle }}"
        forwardTo: "{{ forwardTo }}"
        forwardDeadLetteredMessagesTo: "{{ forwardDeadLetteredMessagesTo }}"
        isClientAffine: {{ isClientAffine }}
        clientAffineProperties:
          clientId: "{{ clientId }}"
          isDurable: {{ isDurable }}
          isShared: {{ isShared }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates a topic subscription. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639385.aspx

```sql
REPLACE azure.service_bus.subscriptions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_name = '{{ subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a subscription from the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639381.aspx

```sql
DELETE FROM azure.service_bus.subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_name = '{{ subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
