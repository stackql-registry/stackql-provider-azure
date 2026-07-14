--- 
title: linked_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_subscriptions
  - azure_stack
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>linked_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="linked_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.linked_subscriptions" /></td></tr>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the remote management connection of the Azure Stack device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the Azure Stack device for remote management.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLinkState" /></td>
    <td><code>string</code></td>
    <td>The connection state of the Azure Stack device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceObjectId" /></td>
    <td><code>string</code></td>
    <td>The object identifier associated with the Azure Stack device connecting to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectedTime" /></td>
    <td><code>string</code></td>
    <td>The last remote management connection time for the Azure Stack device connected to the linked subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The identifier associated with the device subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the resource. Required. "global"</td>
</tr>
<tr>
    <td><CopyableCode code="registrationResourceId" /></td>
    <td><code>string</code></td>
    <td>The identifier associated with the device registration.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Custom tags for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the remote management connection of the Azure Stack device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the Azure Stack device for remote management.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLinkState" /></td>
    <td><code>string</code></td>
    <td>The connection state of the Azure Stack device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceObjectId" /></td>
    <td><code>string</code></td>
    <td>The object identifier associated with the Azure Stack device connecting to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectedTime" /></td>
    <td><code>string</code></td>
    <td>The last remote management connection time for the Azure Stack device connected to the linked subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The identifier associated with the device subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the resource. Required. "global"</td>
</tr>
<tr>
    <td><CopyableCode code="registrationResourceId" /></td>
    <td><code>string</code></td>
    <td>The identifier associated with the device registration.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Custom tags for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
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
    <td>ID of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceConnectionStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the remote management connection of the Azure Stack device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the Azure Stack device for remote management.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLinkState" /></td>
    <td><code>string</code></td>
    <td>The connection state of the Azure Stack device.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceObjectId" /></td>
    <td><code>string</code></td>
    <td>The object identifier associated with the Azure Stack device connecting to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag used for optimistic concurrency when modifying the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectedTime" /></td>
    <td><code>string</code></td>
    <td>The last remote management connection time for the Azure Stack device connected to the linked subscription resource.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The identifier associated with the device subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the resource. Required. "global"</td>
</tr>
<tr>
    <td><CopyableCode code="registrationResourceId" /></td>
    <td><code>string</code></td>
    <td>The identifier associated with the device registration.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Custom tags for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of Resource.</td>
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
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-linked_subscription_name"><code>linked_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the properties of a Linked Subscription resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of all linked subscriptions under current resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a list of all linked subscriptions under current subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-linked_subscription_name"><code>linked_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a linked subscription resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-linked_subscription_name"><code>linked_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Patch a Linked Subscription resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-linked_subscription_name"><code>linked_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update a linked subscription resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-linked_subscription_name"><code>linked_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the requested Linked Subscription resource.</td>
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
<tr id="parameter-linked_subscription_name">
    <td><CopyableCode code="linked_subscription_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Linked Subscription resource. Required.</td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Returns the properties of a Linked Subscription resource.

```sql
SELECT
id,
name,
deviceConnectionStatus,
deviceId,
deviceLinkState,
deviceObjectId,
etag,
kind,
lastConnectedTime,
linkedSubscriptionId,
location,
registrationResourceId,
systemData,
tags,
type
FROM azure_stack.azure_stack.linked_subscriptions
WHERE resource_group = '{{ resource_group }}' -- required
AND linked_subscription_name = '{{ linked_subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns a list of all linked subscriptions under current resource group.

```sql
SELECT
id,
name,
deviceConnectionStatus,
deviceId,
deviceLinkState,
deviceObjectId,
etag,
kind,
lastConnectedTime,
linkedSubscriptionId,
location,
registrationResourceId,
systemData,
tags,
type
FROM azure_stack.azure_stack.linked_subscriptions
WHERE resource_group = '{{ resource_group }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Returns a list of all linked subscriptions under current subscription.

```sql
SELECT
id,
name,
deviceConnectionStatus,
deviceId,
deviceLinkState,
deviceObjectId,
etag,
kind,
lastConnectedTime,
linkedSubscriptionId,
location,
registrationResourceId,
systemData,
tags,
type
FROM azure_stack.azure_stack.linked_subscriptions
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or update a linked subscription resource.

```sql
INSERT INTO azure_stack.azure_stack.linked_subscriptions (
location,
properties,
resource_group,
linked_subscription_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group }}',
'{{ linked_subscription_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
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
- name: linked_subscriptions
  props:
    - name: resource_group
      value: "{{ resource_group }}"
      description: Required parameter for the linked_subscriptions resource.
    - name: linked_subscription_name
      value: "{{ linked_subscription_name }}"
      description: Required parameter for the linked_subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the linked_subscriptions resource.
    - name: location
      value: "{{ location }}"
      description: |
        Location of the resource. Required. "global"
    - name: properties
      value:
        linkedSubscriptionId: "{{ linkedSubscriptionId }}"
        registrationResourceId: "{{ registrationResourceId }}"
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

Patch a Linked Subscription resource.

```sql
UPDATE azure_stack.azure_stack.linked_subscriptions
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group = '{{ resource_group }}' --required
AND linked_subscription_name = '{{ linked_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
kind,
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

Create or update a linked subscription resource.

```sql
REPLACE azure_stack.azure_stack.linked_subscriptions
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group = '{{ resource_group }}' --required
AND linked_subscription_name = '{{ linked_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
etag,
kind,
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

Delete the requested Linked Subscription resource.

```sql
DELETE FROM azure_stack.azure_stack.linked_subscriptions
WHERE resource_group = '{{ resource_group }}' --required
AND linked_subscription_name = '{{ linked_subscription_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
