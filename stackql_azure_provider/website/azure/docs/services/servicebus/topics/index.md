--- 
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - servicebus
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

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="topics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicebus.topics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_authorization_rule"
    values={[
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'get', value: 'get' },
        { label: 'list_by_namespace', value: 'list_by_namespace' }
    ]}
>
<TabItem value="get_authorization_rule">

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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="rights" /></td>
    <td><code>array</code></td>
    <td>The rights associated with the rule.</td>
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
</tbody>
</table>
</TabItem>
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
    <td>Last time the message was sent, or a request was received, for this topic.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteOnIdle" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.</td>
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
    <td><CopyableCode code="defaultMessageTimeToLive" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</td>
</tr>
<tr>
    <td><CopyableCode code="duplicateDetectionHistoryTimeWindow" /></td>
    <td><code>string</code></td>
    <td>ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBatchedOperations" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether server-side batched operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableExpress" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePartitioning" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMessageSizeInKilobytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeInMegabytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="requiresDuplicateDetection" /></td>
    <td><code>boolean</code></td>
    <td>Value indicating if this topic requires duplicate detection.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of the topic, in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Enumerates the possible values for the status of a messaging entity. Known values are: "Active", "Disabled", "Restoring", "SendDisabled", "ReceiveDisabled", "Creating", "Deleting", "Renaming", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionCount" /></td>
    <td><code>integer</code></td>
    <td>Number of subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="supportOrdering" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether the topic supports ordering.</td>
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
<TabItem value="list_by_namespace">

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
    <td>Last time the message was sent, or a request was received, for this topic.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDeleteOnIdle" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.</td>
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
    <td><CopyableCode code="defaultMessageTimeToLive" /></td>
    <td><code>string</code></td>
    <td>ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.</td>
</tr>
<tr>
    <td><CopyableCode code="duplicateDetectionHistoryTimeWindow" /></td>
    <td><code>string</code></td>
    <td>ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="enableBatchedOperations" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether server-side batched operations are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableExpress" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.</td>
</tr>
<tr>
    <td><CopyableCode code="enablePartitioning" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMessageSizeInKilobytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeInMegabytes" /></td>
    <td><code>integer</code></td>
    <td>Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="requiresDuplicateDetection" /></td>
    <td><code>boolean</code></td>
    <td>Value indicating if this topic requires duplicate detection.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of the topic, in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Enumerates the possible values for the status of a messaging entity. Known values are: "Active", "Disabled", "Restoring", "SendDisabled", "ReceiveDisabled", "Creating", "Deleting", "Renaming", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionCount" /></td>
    <td><code>integer</code></td>
    <td>Number of subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="supportOrdering" /></td>
    <td><code>boolean</code></td>
    <td>Value that indicates whether the topic supports ordering.</td>
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
    <td><a href="#get_authorization_rule"><CopyableCode code="get_authorization_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified authorization rule. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720676.aspx</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a description for the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639399.aspx</td>
</tr>
<tr>
    <td><a href="#list_by_namespace"><CopyableCode code="list_by_namespace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all the topics in a namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639388.aspx</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a topic in the specified namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639409.aspx</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a topic in the specified namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639409.aspx</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a topic from the specified namespace and resource group. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639404.aspx</td>
</tr>
<tr>
    <td><a href="#list_authorization_rules"><CopyableCode code="list_authorization_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets authorization rules for a topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720681.aspx</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the primary and secondary connection strings for the topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720677.aspx</td>
</tr>
<tr>
    <td><a href="#create_or_update_authorization_rule"><CopyableCode code="create_or_update_authorization_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an authorization rule for the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720678.aspx</td>
</tr>
<tr>
    <td><a href="#delete_authorization_rule"><CopyableCode code="delete_authorization_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a topic authorization rule. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720681.aspx</td>
</tr>
<tr>
    <td><a href="#regenerate_keys"><CopyableCode code="regenerate_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyType"><code>keyType</code></a></td>
    <td></td>
    <td>Regenerates primary or secondary connection strings for the topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720679.aspx</td>
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
<tr id="parameter-authorization_rule_name">
    <td><CopyableCode code="authorization_rule_name" /></td>
    <td><code>string</code></td>
    <td>The authorization rule name. Required.</td>
</tr>
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
    defaultValue="get_authorization_rule"
    values={[
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'get', value: 'get' },
        { label: 'list_by_namespace', value: 'list_by_namespace' }
    ]}
>
<TabItem value="get_authorization_rule">

Returns the specified authorization rule. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720676.aspx

```sql
SELECT
id,
name,
location,
rights,
systemData,
type
FROM azure.servicebus.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND authorization_rule_name = '{{ authorization_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Returns a description for the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639399.aspx

```sql
SELECT
id,
name,
accessedAt,
autoDeleteOnIdle,
countDetails,
createdAt,
defaultMessageTimeToLive,
duplicateDetectionHistoryTimeWindow,
enableBatchedOperations,
enableExpress,
enablePartitioning,
location,
maxMessageSizeInKilobytes,
maxSizeInMegabytes,
requiresDuplicateDetection,
sizeInBytes,
status,
subscriptionCount,
supportOrdering,
systemData,
type,
updatedAt
FROM azure.servicebus.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_namespace">

Gets all the topics in a namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639388.aspx

```sql
SELECT
id,
name,
accessedAt,
autoDeleteOnIdle,
countDetails,
createdAt,
defaultMessageTimeToLive,
duplicateDetectionHistoryTimeWindow,
enableBatchedOperations,
enableExpress,
enablePartitioning,
location,
maxMessageSizeInKilobytes,
maxSizeInMegabytes,
requiresDuplicateDetection,
sizeInBytes,
status,
subscriptionCount,
supportOrdering,
systemData,
type,
updatedAt
FROM azure.servicebus.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
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

Creates a topic in the specified namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639409.aspx

```sql
INSERT INTO azure.servicebus.topics (
properties,
resource_group_name,
namespace_name,
topic_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ topic_name }}',
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
- name: topics
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the topics resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the topics resource.
    - name: topic_name
      value: "{{ topic_name }}"
      description: Required parameter for the topics resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the topics resource.
    - name: properties
      value:
        defaultMessageTimeToLive: "{{ defaultMessageTimeToLive }}"
        maxSizeInMegabytes: {{ maxSizeInMegabytes }}
        maxMessageSizeInKilobytes: {{ maxMessageSizeInKilobytes }}
        requiresDuplicateDetection: {{ requiresDuplicateDetection }}
        duplicateDetectionHistoryTimeWindow: "{{ duplicateDetectionHistoryTimeWindow }}"
        enableBatchedOperations: {{ enableBatchedOperations }}
        status: "{{ status }}"
        supportOrdering: {{ supportOrdering }}
        autoDeleteOnIdle: "{{ autoDeleteOnIdle }}"
        enablePartitioning: {{ enablePartitioning }}
        enableExpress: {{ enableExpress }}
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

Creates a topic in the specified namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639409.aspx

```sql
REPLACE azure.servicebus.topics
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
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

Deletes a topic from the specified namespace and resource group. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639404.aspx

```sql
DELETE FROM azure.servicebus.topics
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_authorization_rules"
    values={[
        { label: 'list_authorization_rules', value: 'list_authorization_rules' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'create_or_update_authorization_rule', value: 'create_or_update_authorization_rule' },
        { label: 'delete_authorization_rule', value: 'delete_authorization_rule' },
        { label: 'regenerate_keys', value: 'regenerate_keys' }
    ]}
>
<TabItem value="list_authorization_rules">

Gets authorization rules for a topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720681.aspx

```sql
EXEC azure.servicebus.topics.list_authorization_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_keys">

Gets the primary and secondary connection strings for the topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720677.aspx

```sql
EXEC azure.servicebus.topics.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_authorization_rule">

Creates an authorization rule for the specified topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720678.aspx

```sql
EXEC azure.servicebus.topics.create_or_update_authorization_rule 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_authorization_rule">

Deletes a topic authorization rule. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720681.aspx

```sql
EXEC azure.servicebus.topics.delete_authorization_rule 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_keys">

Regenerates primary or secondary connection strings for the topic. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt720679.aspx

```sql
EXEC azure.servicebus.topics.regenerate_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}", 
"key": "{{ key }}"
}'
;
```
</TabItem>
</Tabs>
