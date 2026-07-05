--- 
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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

Creates, updates, deletes, gets or lists a <code>channels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="channels" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.eventgrid.channels" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_partner_namespace', value: 'list_by_partner_namespace' }
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
    <td><CopyableCode code="channelType" /></td>
    <td><code>string</code></td>
    <td>The type of the event channel which represents the direction flow of events. Known values are: "PartnerTopic" and "PartnerDestination". (PartnerTopic, PartnerDestination)</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeIfNotActivatedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated, the channel and corresponding partner topic are deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="messageForActivation" /></td>
    <td><code>string</code></td>
    <td>Context or helpful message that can be used during the approval process by the subscriber.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDestinationInfo" /></td>
    <td><code>object</code></td>
    <td>This property should be populated when channelType is PartnerDestination and represents information about the partner destination resource corresponding to the channel.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicInfo" /></td>
    <td><code>object</code></td>
    <td>This property should be populated when channelType is PartnerTopic and represents information about the partner topic resource corresponding to the channel.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the channel. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "IdleDueToMirroredPartnerTopicDeletion", and "IdleDueToMirroredPartnerDestinationDeletion". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, IdleDueToMirroredPartnerTopicDeletion, IdleDueToMirroredPartnerDestinationDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="readinessState" /></td>
    <td><code>string</code></td>
    <td>The readiness state of the corresponding partner topic. Known values are: "NeverActivated" and "Activated". (NeverActivated, Activated)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_partner_namespace">

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
    <td><CopyableCode code="channelType" /></td>
    <td><code>string</code></td>
    <td>The type of the event channel which represents the direction flow of events. Known values are: "PartnerTopic" and "PartnerDestination". (PartnerTopic, PartnerDestination)</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeIfNotActivatedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the channel. If this timer expires while the corresponding partner topic is never activated, the channel and corresponding partner topic are deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="messageForActivation" /></td>
    <td><code>string</code></td>
    <td>Context or helpful message that can be used during the approval process by the subscriber.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerDestinationInfo" /></td>
    <td><code>object</code></td>
    <td>This property should be populated when channelType is PartnerDestination and represents information about the partner destination resource corresponding to the channel.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicInfo" /></td>
    <td><code>object</code></td>
    <td>This property should be populated when channelType is PartnerTopic and represents information about the partner topic resource corresponding to the channel.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the channel. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "IdleDueToMirroredPartnerTopicDeletion", and "IdleDueToMirroredPartnerDestinationDeletion". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, IdleDueToMirroredPartnerTopicDeletion, IdleDueToMirroredPartnerDestinationDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="readinessState" /></td>
    <td><code>string</code></td>
    <td>The readiness state of the corresponding partner topic. Known values are: "NeverActivated" and "Activated". (NeverActivated, Activated)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a channel. Get properties of a channel.</td>
</tr>
<tr>
    <td><a href="#list_by_partner_namespace"><CopyableCode code="list_by_partner_namespace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List channels. List all the channels in a partner namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a channel. Synchronously creates or updates a new channel with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Channel. Synchronously updates a channel with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a channel. Synchronously creates or updates a new channel with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a channel. Delete an existing channel.</td>
</tr>
<tr>
    <td><a href="#get_full_url"><CopyableCode code="get_full_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_namespace_name"><code>partner_namespace_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get full URL of partner destination channel. Get the full endpoint URL of a partner destination channel.</td>
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
<tr id="parameter-channel_name">
    <td><CopyableCode code="channel_name" /></td>
    <td><code>string</code></td>
    <td>Name of the channel. Required.</td>
</tr>
<tr id="parameter-partner_namespace_name">
    <td><CopyableCode code="partner_namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the partner namespace. Required.</td>
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
        { label: 'list_by_partner_namespace', value: 'list_by_partner_namespace' }
    ]}
>
<TabItem value="get">

Get a channel. Get properties of a channel.

```sql
SELECT
id,
name,
channelType,
expirationTimeIfNotActivatedUtc,
messageForActivation,
partnerDestinationInfo,
partnerTopicInfo,
provisioningState,
readinessState,
systemData,
type
FROM azure.eventgrid.channels
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND partner_namespace_name = '{{ partner_namespace_name }}' -- required
AND channel_name = '{{ channel_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_partner_namespace">

List channels. List all the channels in a partner namespace.

```sql
SELECT
id,
name,
channelType,
expirationTimeIfNotActivatedUtc,
messageForActivation,
partnerDestinationInfo,
partnerTopicInfo,
provisioningState,
readinessState,
systemData,
type
FROM azure.eventgrid.channels
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND partner_namespace_name = '{{ partner_namespace_name }}' -- required
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

Create or update a channel. Synchronously creates or updates a new channel with the specified parameters.

```sql
INSERT INTO azure.eventgrid.channels (
properties,
resource_group_name,
partner_namespace_name,
channel_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ partner_namespace_name }}',
'{{ channel_name }}',
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
- name: channels
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the channels resource.
    - name: partner_namespace_name
      value: "{{ partner_namespace_name }}"
      description: Required parameter for the channels resource.
    - name: channel_name
      value: "{{ channel_name }}"
      description: Required parameter for the channels resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the channels resource.
    - name: properties
      description: |
        Properties of the Channel.
      value:
        channelType: "{{ channelType }}"
        partnerTopicInfo:
          azureSubscriptionId: "{{ azureSubscriptionId }}"
          resourceGroupName: "{{ resourceGroupName }}"
          name: "{{ name }}"
          eventTypeInfo:
            kind: "{{ kind }}"
            inlineEventTypes: "{{ inlineEventTypes }}"
          source: "{{ source }}"
        partnerDestinationInfo:
          azureSubscriptionId: "{{ azureSubscriptionId }}"
          resourceGroupName: "{{ resourceGroupName }}"
          name: "{{ name }}"
          endpointType: "{{ endpointType }}"
          endpointServiceContext: "{{ endpointServiceContext }}"
          resourceMoveChangeHistory:
            - azureSubscriptionId: "{{ azureSubscriptionId }}"
              resourceGroupName: "{{ resourceGroupName }}"
              changedTimeUtc: "{{ changedTimeUtc }}"
        messageForActivation: "{{ messageForActivation }}"
        provisioningState: "{{ provisioningState }}"
        readinessState: "{{ readinessState }}"
        expirationTimeIfNotActivatedUtc: "{{ expirationTimeIfNotActivatedUtc }}"
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

Update a Channel. Synchronously updates a channel with the specified parameters.

```sql
UPDATE azure.eventgrid.channels
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND partner_namespace_name = '{{ partner_namespace_name }}' --required
AND channel_name = '{{ channel_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required;
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

Create or update a channel. Synchronously creates or updates a new channel with the specified parameters.

```sql
REPLACE azure.eventgrid.channels
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND partner_namespace_name = '{{ partner_namespace_name }}' --required
AND channel_name = '{{ channel_name }}' --required
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

Delete a channel. Delete an existing channel.

```sql
DELETE FROM azure.eventgrid.channels
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND partner_namespace_name = '{{ partner_namespace_name }}' --required
AND channel_name = '{{ channel_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_full_url"
    values={[
        { label: 'get_full_url', value: 'get_full_url' }
    ]}
>
<TabItem value="get_full_url">

Get full URL of partner destination channel. Get the full endpoint URL of a partner destination channel.

```sql
EXEC azure.eventgrid.channels.get_full_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@partner_namespace_name='{{ partner_namespace_name }}' --required, 
@channel_name='{{ channel_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
