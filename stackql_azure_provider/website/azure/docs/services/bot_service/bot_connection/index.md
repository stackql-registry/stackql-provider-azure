--- 
title: bot_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_connection
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

Creates, updates, deletes, gets or lists a <code>bot_connection</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bot_connection" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bot_connection" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_bot_service', value: 'list_by_bot_service' },
        { label: 'list_service_providers', value: 'list_service_providers' }
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
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>Client Id associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>Client Secret associated with the Connection Setting.</td>
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
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>Service Provider Parameters associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>string</code></td>
    <td>Scopes associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderDisplayName" /></td>
    <td><code>string</code></td>
    <td>Service Provider Display Name associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderId" /></td>
    <td><code>string</code></td>
    <td>Service Provider Id associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="settingId" /></td>
    <td><code>string</code></td>
    <td>Setting Id set by the service for the Connection Setting.</td>
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
<TabItem value="list_by_bot_service">

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
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>Client Id associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>Client Secret associated with the Connection Setting.</td>
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
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>Service Provider Parameters associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>string</code></td>
    <td>Scopes associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderDisplayName" /></td>
    <td><code>string</code></td>
    <td>Service Provider Display Name associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderId" /></td>
    <td><code>string</code></td>
    <td>Service Provider Id associated with the Connection Setting.</td>
</tr>
<tr>
    <td><CopyableCode code="settingId" /></td>
    <td><code>string</code></td>
    <td>Setting Id set by the service for the Connection Setting.</td>
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
<TabItem value="list_service_providers">

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
    <td>Id for Service Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="devPortalUrl" /></td>
    <td><code>string</code></td>
    <td>URL of Dev Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name of the Service Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of icon.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>The list of parameters for the Service Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProviderName" /></td>
    <td><code>string</code></td>
    <td>Name of the Service Provider.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Connection Setting registration for a Bot Service.</td>
</tr>
<tr>
    <td><a href="#list_by_bot_service"><CopyableCode code="list_by_bot_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the Connection Settings registered to a particular BotService resource.</td>
</tr>
<tr>
    <td><a href="#list_service_providers"><CopyableCode code="list_service_providers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the available Service Providers for creating Connection Settings.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Register a new Auth Connection for a Bot Service.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Connection Setting registration for a Bot Service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Connection Setting registration for a Bot Service.</td>
</tr>
<tr>
    <td><a href="#list_with_secrets"><CopyableCode code="list_with_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Connection Setting registration for a Bot Service.</td>
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
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bot Service Connection Setting resource. Required.</td>
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
        { label: 'list_by_bot_service', value: 'list_by_bot_service' },
        { label: 'list_service_providers', value: 'list_service_providers' }
    ]}
>
<TabItem value="get">

Get a Connection Setting registration for a Bot Service.

```sql
SELECT
id,
name,
clientId,
clientSecret,
etag,
kind,
location,
parameters,
provisioningState,
scopes,
serviceProviderDisplayName,
serviceProviderId,
settingId,
sku,
tags,
type,
zones
FROM azure.bot_service.bot_connection
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_bot_service">

Returns all the Connection Settings registered to a particular BotService resource.

```sql
SELECT
id,
name,
clientId,
clientSecret,
etag,
kind,
location,
parameters,
provisioningState,
scopes,
serviceProviderDisplayName,
serviceProviderId,
settingId,
sku,
tags,
type,
zones
FROM azure.bot_service.bot_connection
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_service_providers">

Lists the available Service Providers for creating Connection Settings.

```sql
SELECT
id,
devPortalUrl,
displayName,
iconUrl,
parameters,
serviceProviderName
FROM azure.bot_service.bot_connection
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Register a new Auth Connection for a Bot Service.

```sql
INSERT INTO azure.bot_service.bot_connection (
location,
tags,
sku,
kind,
etag,
properties,
resource_group_name,
resource_name,
connection_name,
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
'{{ connection_name }}',
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
- name: bot_connection
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bot_connection resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the bot_connection resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the bot_connection resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bot_connection resource.
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
        clientId: "{{ clientId }}"
        settingId: "{{ settingId }}"
        clientSecret: "{{ clientSecret }}"
        scopes: "{{ scopes }}"
        serviceProviderId: "{{ serviceProviderId }}"
        serviceProviderDisplayName: "{{ serviceProviderDisplayName }}"
        parameters:
          - key: "{{ key }}"
            value: "{{ value }}"
        provisioningState: "{{ provisioningState }}"
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

Updates a Connection Setting registration for a Bot Service.

```sql
UPDATE azure.bot_service.bot_connection
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Deletes a Connection Setting registration for a Bot Service.

```sql
DELETE FROM azure.bot_service.bot_connection
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_with_secrets"
    values={[
        { label: 'list_with_secrets', value: 'list_with_secrets' }
    ]}
>
<TabItem value="list_with_secrets">

Get a Connection Setting registration for a Bot Service.

```sql
EXEC azure.bot_service.bot_connection.list_with_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@connection_name='{{ connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
