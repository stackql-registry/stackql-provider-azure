--- 
title: consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_groups
  - event_hub
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

Creates, updates, deletes, gets or lists a <code>consumer_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="consumer_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hub.consumer_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_event_hub', value: 'list_by_event_hub' }
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
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the message was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
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
<tr>
    <td><CopyableCode code="userMetadata" /></td>
    <td><code>string</code></td>
    <td>User Metadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_event_hub">

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
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the message was created.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
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
<tr>
    <td><CopyableCode code="userMetadata" /></td>
    <td><code>string</code></td>
    <td>User Metadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-event_hub_name"><code>event_hub_name</code></a>, <a href="#parameter-consumer_group_name"><code>consumer_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a description for the specified consumer group.</td>
</tr>
<tr>
    <td><a href="#list_by_event_hub"><CopyableCode code="list_by_event_hub" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-event_hub_name"><code>event_hub_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-event_hub_name"><code>event_hub_name</code></a>, <a href="#parameter-consumer_group_name"><code>consumer_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-event_hub_name"><code>event_hub_name</code></a>, <a href="#parameter-consumer_group_name"><code>consumer_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-event_hub_name"><code>event_hub_name</code></a>, <a href="#parameter-consumer_group_name"><code>consumer_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a consumer group from the specified Event Hub and resource group.</td>
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
<tr id="parameter-consumer_group_name">
    <td><CopyableCode code="consumer_group_name" /></td>
    <td><code>string</code></td>
    <td>The consumer group name. Required.</td>
</tr>
<tr id="parameter-event_hub_name">
    <td><CopyableCode code="event_hub_name" /></td>
    <td><code>string</code></td>
    <td>The Event Hub name. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The Namespace name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group within the azure subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
        { label: 'list_by_event_hub', value: 'list_by_event_hub' }
    ]}
>
<TabItem value="get">

Gets a description for the specified consumer group.

```sql
SELECT
id,
name,
createdAt,
location,
systemData,
type,
updatedAt,
userMetadata
FROM azure.event_hub.consumer_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND event_hub_name = '{{ event_hub_name }}' -- required
AND consumer_group_name = '{{ consumer_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_event_hub">

Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace.

```sql
SELECT
id,
name,
createdAt,
location,
systemData,
type,
updatedAt,
userMetadata
FROM azure.event_hub.consumer_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND event_hub_name = '{{ event_hub_name }}' -- required
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

Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

```sql
INSERT INTO azure.event_hub.consumer_groups (
properties,
resource_group_name,
namespace_name,
event_hub_name,
consumer_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ event_hub_name }}',
'{{ consumer_group_name }}',
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
- name: consumer_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the consumer_groups resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the consumer_groups resource.
    - name: event_hub_name
      value: "{{ event_hub_name }}"
      description: Required parameter for the consumer_groups resource.
    - name: consumer_group_name
      value: "{{ consumer_group_name }}"
      description: Required parameter for the consumer_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the consumer_groups resource.
    - name: properties
      value:
        userMetadata: "{{ userMetadata }}"
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

Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

```sql
REPLACE azure.event_hub.consumer_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND event_hub_name = '{{ event_hub_name }}' --required
AND consumer_group_name = '{{ consumer_group_name }}' --required
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

Deletes a consumer group from the specified Event Hub and resource group.

```sql
DELETE FROM azure.event_hub.consumer_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND event_hub_name = '{{ event_hub_name }}' --required
AND consumer_group_name = '{{ consumer_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
