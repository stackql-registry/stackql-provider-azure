--- 
title: sender_usernames
hide_title: false
hide_table_of_contents: false
keywords:
  - sender_usernames
  - communication
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

Creates, updates, deletes, gets or lists a <code>sender_usernames</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sender_usernames" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.sender_usernames" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_domains', value: 'list_by_domains' }
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
    <td><CopyableCode code="dataLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the SenderUsername resource data is stored at rest.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the senderUsername.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Unknown is the default state for Communication Services. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving". (Unknown, Succeeded, Failed, Canceled, Running, Creating, Updating, Deleting, Moving)</td>
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
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>A sender senderUsername to be used when sending emails. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_domains">

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
    <td><CopyableCode code="dataLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the SenderUsername resource data is stored at rest.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the senderUsername.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Unknown is the default state for Communication Services. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving". (Unknown, Succeeded, Failed, Canceled, Running, Creating, Updating, Deleting, Moving)</td>
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
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>A sender senderUsername to be used when sending emails. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-sender_username"><code>sender_username</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get. Get a valid sender username for a domains resource.</td>
</tr>
<tr>
    <td><a href="#list_by_domains"><CopyableCode code="list_by_domains" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>ListBy_Domains. List all valid sender usernames for a domains resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-sender_username"><code>sender_username</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Or Update. Add a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-sender_username"><code>sender_username</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Or Update. Add a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-sender_username"><code>sender_username</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete. Operation to delete a SenderUsernames resource.</td>
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
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Domains resource. Required.</td>
</tr>
<tr id="parameter-email_service_name">
    <td><CopyableCode code="email_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the EmailService resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sender_username">
    <td><CopyableCode code="sender_username" /></td>
    <td><code>string</code></td>
    <td>The valid sender Username. Required.</td>
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
        { label: 'list_by_domains', value: 'list_by_domains' }
    ]}
>
<TabItem value="get">

Get. Get a valid sender username for a domains resource.

```sql
SELECT
id,
name,
dataLocation,
displayName,
provisioningState,
systemData,
type,
username
FROM azure.communication.sender_usernames
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND email_service_name = '{{ email_service_name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
AND sender_username = '{{ sender_username }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_domains">

ListBy_Domains. List all valid sender usernames for a domains resource.

```sql
SELECT
id,
name,
dataLocation,
displayName,
provisioningState,
systemData,
type,
username
FROM azure.communication.sender_usernames
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND email_service_name = '{{ email_service_name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
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

Create Or Update. Add a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource.

```sql
INSERT INTO azure.communication.sender_usernames (
properties,
resource_group_name,
email_service_name,
domain_name,
sender_username,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ email_service_name }}',
'{{ domain_name }}',
'{{ sender_username }}',
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
- name: sender_usernames
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sender_usernames resource.
    - name: email_service_name
      value: "{{ email_service_name }}"
      description: Required parameter for the sender_usernames resource.
    - name: domain_name
      value: "{{ domain_name }}"
      description: Required parameter for the sender_usernames resource.
    - name: sender_username
      value: "{{ sender_username }}"
      description: Required parameter for the sender_usernames resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sender_usernames resource.
    - name: properties
      description: |
        The properties of a SenderUsername resource.
      value:
        dataLocation: "{{ dataLocation }}"
        username: "{{ username }}"
        displayName: "{{ displayName }}"
        provisioningState: "{{ provisioningState }}"
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

Create Or Update. Add a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource.

```sql
REPLACE azure.communication.sender_usernames
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND email_service_name = '{{ email_service_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND sender_username = '{{ sender_username }}' --required
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

Delete. Operation to delete a SenderUsernames resource.

```sql
DELETE FROM azure.communication.sender_usernames
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND email_service_name = '{{ email_service_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND sender_username = '{{ sender_username }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
