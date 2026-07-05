--- 
title: namespace_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace_topic_event_subscriptions
  - eventgrid
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

Creates, updates, deletes, gets or lists a <code>namespace_topic_event_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespace_topic_event_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid.namespace_topic_event_subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_namespace_topic', value: 'list_by_namespace_topic' }
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
    <td><CopyableCode code="deliveryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Information about the delivery configuration of the event subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="eventDeliverySchema" /></td>
    <td><code>string</code></td>
    <td>The event delivery schema for the event subscription. "CloudEventSchemaV1_0" (CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the event subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="filtersConfiguration" /></td>
    <td><code>object</code></td>
    <td>Information about the filter for the event subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the event subscription. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "AwaitingManualAction", "Deleted", "DeleteFailed", "CreateFailed", and "UpdatedFailed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, AwaitingManualAction, Deleted, DeleteFailed, CreateFailed, UpdatedFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags relating to Event Subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_namespace_topic">

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
    <td><CopyableCode code="deliveryConfiguration" /></td>
    <td><code>object</code></td>
    <td>Information about the delivery configuration of the event subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="eventDeliverySchema" /></td>
    <td><code>string</code></td>
    <td>The event delivery schema for the event subscription. "CloudEventSchemaV1_0" (CloudEventSchemaV1_0)</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the event subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="filtersConfiguration" /></td>
    <td><code>object</code></td>
    <td>Information about the filter for the event subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the event subscription. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "AwaitingManualAction", "Deleted", "DeleteFailed", "CreateFailed", and "UpdatedFailed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, AwaitingManualAction, Deleted, DeleteFailed, CreateFailed, UpdatedFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags relating to Event Subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an event subscription of a namespace topic. Get properties of an event subscription of a namespace topic.</td>
</tr>
<tr>
    <td><a href="#list_by_namespace_topic"><CopyableCode code="list_by_namespace_topic" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List event subscriptions of a namespace topic. List event subscriptions that belong to a specific namespace topic.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update an event subscription of a namespace topic. Asynchronously creates or updates an event subscription of a namespace topic with the specified parameters. Existing event subscriptions will be updated with this API.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update event subscription of a namespace topic. Update an existing event subscription of a namespace topic.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update an event subscription of a namespace topic. Asynchronously creates or updates an event subscription of a namespace topic with the specified parameters. Existing event subscriptions will be updated with this API.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an event subscription of a namespace topic. Delete an existing event subscription of a namespace topic.</td>
</tr>
<tr>
    <td><a href="#get_delivery_attributes"><CopyableCode code="get_delivery_attributes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get delivery attributes for an event subscription of a namespace topic. Get all delivery attributes for an event subscription of a namespace topic.</td>
</tr>
<tr>
    <td><a href="#get_full_url"><CopyableCode code="get_full_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-event_subscription_name"><code>event_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get full URL of an event subscription of a namespace topic. Get the full endpoint URL for an event subscription of a namespace topic.</td>
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
<tr id="parameter-event_subscription_name">
    <td><CopyableCode code="event_subscription_name" /></td>
    <td><code>string</code></td>
    <td>Name of the event subscription to be found. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the namespace. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-topic_name">
    <td><CopyableCode code="topic_name" /></td>
    <td><code>string</code></td>
    <td>Name of the namespace topic. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_namespace_topic', value: 'list_by_namespace_topic' }
    ]}
>
<TabItem value="get">

Get an event subscription of a namespace topic. Get properties of an event subscription of a namespace topic.

```sql
SELECT
id,
name,
deliveryConfiguration,
eventDeliverySchema,
expirationTimeUtc,
filtersConfiguration,
provisioningState,
systemData,
tags,
type
FROM azure.eventgrid.namespace_topic_event_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND event_subscription_name = '{{ event_subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_namespace_topic">

List event subscriptions of a namespace topic. List event subscriptions that belong to a specific namespace topic.

```sql
SELECT
id,
name,
deliveryConfiguration,
eventDeliverySchema,
expirationTimeUtc,
filtersConfiguration,
provisioningState,
systemData,
tags,
type
FROM azure.eventgrid.namespace_topic_event_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create or update an event subscription of a namespace topic. Asynchronously creates or updates an event subscription of a namespace topic with the specified parameters. Existing event subscriptions will be updated with this API.

```sql
INSERT INTO azure.eventgrid.namespace_topic_event_subscriptions (
properties,
resource_group_name,
namespace_name,
topic_name,
event_subscription_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ topic_name }}',
'{{ event_subscription_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: namespace_topic_event_subscriptions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the namespace_topic_event_subscriptions resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the namespace_topic_event_subscriptions resource.
    - name: topic_name
      value: "{{ topic_name }}"
      description: Required parameter for the namespace_topic_event_subscriptions resource.
    - name: event_subscription_name
      value: "{{ event_subscription_name }}"
      description: Required parameter for the namespace_topic_event_subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the namespace_topic_event_subscriptions resource.
    - name: properties
      description: |
        Properties of the event subscription.
      value:
        provisioningState: "{{ provisioningState }}"
        deliveryConfiguration:
          deliveryMode: "{{ deliveryMode }}"
          queue:
            receiveLockDurationInSeconds: {{ receiveLockDurationInSeconds }}
            maxDeliveryCount: {{ maxDeliveryCount }}
            deadLetterDestinationWithResourceIdentity:
              identity:
                type: "{{ type }}"
                userAssignedIdentity: "{{ userAssignedIdentity }}"
                federatedIdentityCredentialInfo: "{{ federatedIdentityCredentialInfo }}"
              deadLetterDestination:
                endpointType: "{{ endpointType }}"
            eventTimeToLive: "{{ eventTimeToLive }}"
          push:
            maxDeliveryCount: {{ maxDeliveryCount }}
            eventTimeToLive: "{{ eventTimeToLive }}"
            deadLetterDestinationWithResourceIdentity:
              identity:
                type: "{{ type }}"
                userAssignedIdentity: "{{ userAssignedIdentity }}"
                federatedIdentityCredentialInfo: "{{ federatedIdentityCredentialInfo }}"
              deadLetterDestination:
                endpointType: "{{ endpointType }}"
            deliveryWithResourceIdentity:
              identity:
                type: "{{ type }}"
                userAssignedIdentity: "{{ userAssignedIdentity }}"
                federatedIdentityCredentialInfo: "{{ federatedIdentityCredentialInfo }}"
              destination:
                endpointType: "{{ endpointType }}"
            destination:
              endpointType: "{{ endpointType }}"
        eventDeliverySchema: "{{ eventDeliverySchema }}"
        filtersConfiguration:
          includedEventTypes:
            - "{{ includedEventTypes }}"
          filters:
            - operatorType: "{{ operatorType }}"
              key: "{{ key }}"
        expirationTimeUtc: "{{ expirationTimeUtc }}"
        tags: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update event subscription of a namespace topic. Update an existing event subscription of a namespace topic.

```sql
UPDATE azure.eventgrid.namespace_topic_event_subscriptions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND event_subscription_name = '{{ event_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
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

Create or update an event subscription of a namespace topic. Asynchronously creates or updates an event subscription of a namespace topic with the specified parameters. Existing event subscriptions will be updated with this API.

```sql
REPLACE azure.eventgrid.namespace_topic_event_subscriptions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND event_subscription_name = '{{ event_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete an event subscription of a namespace topic. Delete an existing event subscription of a namespace topic.

```sql
DELETE FROM azure.eventgrid.namespace_topic_event_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND topic_name = '{{ topic_name }}' --required
AND event_subscription_name = '{{ event_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_delivery_attributes"
    values={[
        { label: 'get_delivery_attributes', value: 'get_delivery_attributes' },
        { label: 'get_full_url', value: 'get_full_url' }
    ]}
>
<TabItem value="get_delivery_attributes">

Get delivery attributes for an event subscription of a namespace topic. Get all delivery attributes for an event subscription of a namespace topic.

```sql
EXEC azure.eventgrid.namespace_topic_event_subscriptions.get_delivery_attributes 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@event_subscription_name='{{ event_subscription_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_full_url">

Get full URL of an event subscription of a namespace topic. Get the full endpoint URL for an event subscription of a namespace topic.

```sql
EXEC azure.eventgrid.namespace_topic_event_subscriptions.get_full_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@topic_name='{{ topic_name }}' --required, 
@event_subscription_name='{{ event_subscription_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
