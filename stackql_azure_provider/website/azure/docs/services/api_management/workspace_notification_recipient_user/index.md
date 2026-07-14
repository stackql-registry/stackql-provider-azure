--- 
title: workspace_notification_recipient_user
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_notification_recipient_user
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_notification_recipient_user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_notification_recipient_user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_notification_recipient_user" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_notification"
    values={[
        { label: 'list_by_notification', value: 'list_by_notification' }
    ]}
>
<TabItem value="list_by_notification">

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
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>API Management UserId subscribed to notification.</td>
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
    <td><a href="#list_by_notification"><CopyableCode code="list_by_notification" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-notification_name"><code>notification_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of the Notification Recipient User subscribed to the notification.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-notification_name"><code>notification_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds the API Management User to the list of Recipients for the Notification.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-notification_name"><code>notification_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds the API Management User to the list of Recipients for the Notification.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-notification_name"><code>notification_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes the API Management user from the list of Notification.</td>
</tr>
<tr>
    <td><a href="#check_entity_exists"><CopyableCode code="check_entity_exists" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-workspace_id"><code>workspace_id</code></a>, <a href="#parameter-notification_name"><code>notification_name</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Determine if the Notification Recipient User is subscribed to the notification.</td>
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
<tr id="parameter-notification_name">
    <td><CopyableCode code="notification_name" /></td>
    <td><code>string</code></td>
    <td>Workspace identifier. Must be unique in the current API Management service instance. Known values are: "RequestPublisherNotificationMessage", "PurchasePublisherNotificationMessage", "NewApplicationNotificationMessage", "BCC", "NewIssuePublisherNotificationMessage", "AccountClosedPublisher", and "QuotaLimitApproachingPublisherNotificationMessage". Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>User identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-workspace_id">
    <td><CopyableCode code="workspace_id" /></td>
    <td><code>string</code></td>
    <td>Workspace identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_notification"
    values={[
        { label: 'list_by_notification', value: 'list_by_notification' }
    ]}
>
<TabItem value="list_by_notification">

Gets the list of the Notification Recipient User subscribed to the notification.

```sql
SELECT
id,
name,
systemData,
type,
userId
FROM azure.api_management.workspace_notification_recipient_user
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND workspace_id = '{{ workspace_id }}' -- required
AND notification_name = '{{ notification_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Adds the API Management User to the list of Recipients for the Notification.

```sql
INSERT INTO azure.api_management.workspace_notification_recipient_user (
resource_group_name,
service_name,
workspace_id,
notification_name,
user_id,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ workspace_id }}',
'{{ notification_name }}',
'{{ user_id }}',
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
- name: workspace_notification_recipient_user
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_notification_recipient_user resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the workspace_notification_recipient_user resource.
    - name: workspace_id
      value: "{{ workspace_id }}"
      description: Required parameter for the workspace_notification_recipient_user resource.
    - name: notification_name
      value: "{{ notification_name }}"
      description: Required parameter for the workspace_notification_recipient_user resource.
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the workspace_notification_recipient_user resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_notification_recipient_user resource.
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

Adds the API Management User to the list of Recipients for the Notification.

```sql
REPLACE azure.api_management.workspace_notification_recipient_user
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND notification_name = '{{ notification_name }}' --required
AND user_id = '{{ user_id }}' --required
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

Removes the API Management user from the list of Notification.

```sql
DELETE FROM azure.api_management.workspace_notification_recipient_user
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND workspace_id = '{{ workspace_id }}' --required
AND notification_name = '{{ notification_name }}' --required
AND user_id = '{{ user_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_entity_exists"
    values={[
        { label: 'check_entity_exists', value: 'check_entity_exists' }
    ]}
>
<TabItem value="check_entity_exists">

Determine if the Notification Recipient User is subscribed to the notification.

```sql
EXEC azure.api_management.workspace_notification_recipient_user.check_entity_exists 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@workspace_id='{{ workspace_id }}' --required, 
@notification_name='{{ notification_name }}' --required, 
@user_id='{{ user_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
