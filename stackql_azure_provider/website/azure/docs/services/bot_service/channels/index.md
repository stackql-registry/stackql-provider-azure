--- 
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - bot_service
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.channels" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="channelName" /></td>
    <td><code>string</code></td>
    <td>The channel name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity Tag.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Required. Gets or sets the Kind of the resource. Known values are: "sdk", "designer", "bot", "function", and "azurebot".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Entity zones.</td>
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="channelName" /></td>
    <td><code>string</code></td>
    <td>The channel name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity Tag.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Required. Gets or sets the Kind of the resource. Known values are: "sdk", "designer", "bot", "function", and "azurebot".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Entity zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a BotService Channel registration specified by the parameters.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the Channel registrations of a particular BotService resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a Channel registration for a Bot Service.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Updates a Channel registration for a Bot Service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Channel registration from a Bot Service.</td>
</tr>
<tr>
    <td><a href="#list_with_keys"><CopyableCode code="list_with_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-channel_name"><code>channel_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists a Channel registration for a Bot Service including secrets.</td>
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
    <td>The name of the Channel resource. Known values are: "AlexaChannel", "FacebookChannel", "EmailChannel", "KikChannel", "TelegramChannel", "SlackChannel", "MsTeamsChannel", "SkypeChannel", "WebChatChannel", "DirectLineChannel", "SmsChannel", "LineChannel", "DirectLineSpeechChannel", "OutlookChannel", "Omnichannel", "TelephonyChannel", "AcsChatChannel", "SearchAssistant", and "M365Extensions". Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bot resource group in the user subscription. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bot resource. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="get">

Returns a BotService Channel registration specified by the parameters.

```sql
SELECT
id,
name,
channelName,
etag,
kind,
location,
provisioningState,
sku,
tags,
type,
zones
FROM azure.bot_service.channels
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND channel_name = '{{ channel_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns all the Channel registrations of a particular BotService resource.

```sql
SELECT
id,
name,
channelName,
etag,
kind,
location,
provisioningState,
sku,
tags,
type,
zones
FROM azure.bot_service.channels
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a Channel registration for a Bot Service.

```sql
INSERT INTO azure.bot_service.channels (
location,
tags,
sku,
kind,
etag,
properties,
resource_group_name,
resource_name,
channel_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ kind }}',
'{{ etag }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ channel_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
tags,
type,
zones
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
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the channels resource.
    - name: channel_name
      value: "{{ channel_name }}"
      description: Required parameter for the channels resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the channels resource.
    - name: location
      value: "{{ location }}"
      description: |
        Specifies the location of the resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Contains resource tags defined as key/value pairs.
    - name: sku
      description: |
        Gets or sets the SKU of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Required. Gets or sets the Kind of the resource. Known values are: "sdk", "designer", "bot", "function", and "azurebot".
    - name: etag
      value: "{{ etag }}"
      description: |
        Entity Tag.
    - name: properties
      description: |
        The set of properties specific to bot channel resource.
      value:
        channelName: "{{ channelName }}"
        etag: "{{ etag }}"
        provisioningState: "{{ provisioningState }}"
        location: "{{ location }}"
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

Updates a Channel registration for a Bot Service.

```sql
UPDATE azure.bot_service.channels
SET 
name = '{{ name }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND channel_name = '{{ channel_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND name = '{{ name }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
tags,
type,
zones;
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

Deletes a Channel registration from a Bot Service.

```sql
DELETE FROM azure.bot_service.channels
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND channel_name = '{{ channel_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_with_keys"
    values={[
        { label: 'list_with_keys', value: 'list_with_keys' }
    ]}
>
<TabItem value="list_with_keys">

Lists a Channel registration for a Bot Service including secrets.

```sql
EXEC azure.bot_service.channels.list_with_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@channel_name='{{ channel_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
