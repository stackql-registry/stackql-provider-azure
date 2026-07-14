--- 
title: partner_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topics
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>partner_topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="partner_topics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_topics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="activationState" /></td>
    <td><code>string</code></td>
    <td>Activation state of the partner topic. Known values are: "NeverActivated", "Activated", and "Deactivated". (NeverActivated, Activated, Deactivated)</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type information from the corresponding event channel.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeIfNotActivatedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the partner topic. If this timer expires while the partner topic is still never activated, the partner topic and corresponding event channel are deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Partner Topic resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="messageForActivation" /></td>
    <td><code>string</code></td>
    <td>Context or helpful message that can be used during the approval process by the subscriber.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegistrationImmutableId" /></td>
    <td><code>string</code></td>
    <td>The immutableId of the corresponding partner registration.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicFriendlyDescription" /></td>
    <td><code>string</code></td>
    <td>Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic. This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the partner topic. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", and "IdleDueToMirroredChannelResourceDeletion". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, IdleDueToMirroredChannelResourceDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source associated with this partner topic. This represents a unique partner resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="activationState" /></td>
    <td><code>string</code></td>
    <td>Activation state of the partner topic. Known values are: "NeverActivated", "Activated", and "Deactivated". (NeverActivated, Activated, Deactivated)</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type information from the corresponding event channel.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeIfNotActivatedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the partner topic. If this timer expires while the partner topic is still never activated, the partner topic and corresponding event channel are deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Partner Topic resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="messageForActivation" /></td>
    <td><code>string</code></td>
    <td>Context or helpful message that can be used during the approval process by the subscriber.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegistrationImmutableId" /></td>
    <td><code>string</code></td>
    <td>The immutableId of the corresponding partner registration.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicFriendlyDescription" /></td>
    <td><code>string</code></td>
    <td>Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic. This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the partner topic. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", and "IdleDueToMirroredChannelResourceDeletion". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, IdleDueToMirroredChannelResourceDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source associated with this partner topic. This represents a unique partner resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="activationState" /></td>
    <td><code>string</code></td>
    <td>Activation state of the partner topic. Known values are: "NeverActivated", "Activated", and "Deactivated". (NeverActivated, Activated, Deactivated)</td>
</tr>
<tr>
    <td><CopyableCode code="eventTypeInfo" /></td>
    <td><code>object</code></td>
    <td>Event Type information from the corresponding event channel.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTimeIfNotActivatedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the partner topic. If this timer expires while the partner topic is still never activated, the partner topic and corresponding event channel are deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Partner Topic resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="messageForActivation" /></td>
    <td><code>string</code></td>
    <td>Context or helpful message that can be used during the approval process by the subscriber.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegistrationImmutableId" /></td>
    <td><code>string</code></td>
    <td>The immutableId of the corresponding partner registration.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTopicFriendlyDescription" /></td>
    <td><code>string</code></td>
    <td>Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic. This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the partner topic. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", and "IdleDueToMirroredChannelResourceDeletion". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, IdleDueToMirroredChannelResourceDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source associated with this partner topic. This represents a unique partner resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a partner topic. Get properties of a partner topic.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List partner topics under a resource group. List all the partner topics under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List partner topics under an Azure subscription. List all the partner topics under an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a partner topic. Asynchronously creates a new partner topic with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a partner topic. Asynchronously updates a partner topic with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a partner topic. Asynchronously creates a new partner topic with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a partner topic. Delete existing partner topic.</td>
</tr>
<tr>
    <td><a href="#activate"><CopyableCode code="activate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Activate a partner topic. Activate a newly created partner topic.</td>
</tr>
<tr>
    <td><a href="#deactivate"><CopyableCode code="deactivate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-partner_topic_name"><code>partner_topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deactivate a partner topic. Deactivate specific partner topic.</td>
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
<tr id="parameter-partner_topic_name">
    <td><CopyableCode code="partner_topic_name" /></td>
    <td><code>string</code></td>
    <td>Name of the partner topic. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a partner topic. Get properties of a partner topic.

```sql
SELECT
id,
name,
activationState,
eventTypeInfo,
expirationTimeIfNotActivatedUtc,
identity,
location,
messageForActivation,
partnerRegistrationImmutableId,
partnerTopicFriendlyDescription,
provisioningState,
source,
systemData,
tags,
type
FROM azure.event_grid.partner_topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND partner_topic_name = '{{ partner_topic_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List partner topics under a resource group. List all the partner topics under a resource group.

```sql
SELECT
id,
name,
activationState,
eventTypeInfo,
expirationTimeIfNotActivatedUtc,
identity,
location,
messageForActivation,
partnerRegistrationImmutableId,
partnerTopicFriendlyDescription,
provisioningState,
source,
systemData,
tags,
type
FROM azure.event_grid.partner_topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List partner topics under an Azure subscription. List all the partner topics under an Azure subscription.

```sql
SELECT
id,
name,
activationState,
eventTypeInfo,
expirationTimeIfNotActivatedUtc,
identity,
location,
messageForActivation,
partnerRegistrationImmutableId,
partnerTopicFriendlyDescription,
provisioningState,
source,
systemData,
tags,
type
FROM azure.event_grid.partner_topics
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a partner topic. Asynchronously creates a new partner topic with the specified parameters.

```sql
INSERT INTO azure.event_grid.partner_topics (
tags,
location,
properties,
identity,
resource_group_name,
partner_topic_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ partner_topic_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: partner_topics
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the partner_topics resource.
    - name: partner_topic_name
      value: "{{ partner_topic_name }}"
      description: Required parameter for the partner_topics resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the partner_topics resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of the Partner Topic.
      value:
        partnerRegistrationImmutableId: "{{ partnerRegistrationImmutableId }}"
        source: "{{ source }}"
        eventTypeInfo:
          kind: "{{ kind }}"
          inlineEventTypes: "{{ inlineEventTypes }}"
        expirationTimeIfNotActivatedUtc: "{{ expirationTimeIfNotActivatedUtc }}"
        provisioningState: "{{ provisioningState }}"
        activationState: "{{ activationState }}"
        partnerTopicFriendlyDescription: "{{ partnerTopicFriendlyDescription }}"
        messageForActivation: "{{ messageForActivation }}"
    - name: identity
      description: |
        Identity information for the Partner Topic resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update a partner topic. Asynchronously updates a partner topic with the specified parameters.

```sql
UPDATE azure.event_grid.partner_topics
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND partner_topic_name = '{{ partner_topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
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

Create a partner topic. Asynchronously creates a new partner topic with the specified parameters.

```sql
REPLACE azure.event_grid.partner_topics
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND partner_topic_name = '{{ partner_topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
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

Delete a partner topic. Delete existing partner topic.

```sql
DELETE FROM azure.event_grid.partner_topics
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND partner_topic_name = '{{ partner_topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="activate"
    values={[
        { label: 'activate', value: 'activate' },
        { label: 'deactivate', value: 'deactivate' }
    ]}
>
<TabItem value="activate">

Activate a partner topic. Activate a newly created partner topic.

```sql
EXEC azure.event_grid.partner_topics.activate 
@resource_group_name='{{ resource_group_name }}' --required, 
@partner_topic_name='{{ partner_topic_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deactivate">

Deactivate a partner topic. Deactivate specific partner topic.

```sql
EXEC azure.event_grid.partner_topics.deactivate 
@resource_group_name='{{ resource_group_name }}' --required, 
@partner_topic_name='{{ partner_topic_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
