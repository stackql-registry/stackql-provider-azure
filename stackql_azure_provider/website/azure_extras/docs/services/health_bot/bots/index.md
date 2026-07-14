--- 
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - health_bot
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>bots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_bot.bots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="accessControlMethod" /></td>
    <td><code>string</code></td>
    <td>The access control method for the Azure Health Bot resource.</td>
</tr>
<tr>
    <td><CopyableCode code="botManagementPortalLink" /></td>
    <td><code>string</code></td>
    <td>The link.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Azure Health Bot.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>KeyVault properties for the resource encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Azure Health Bot resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the Azure Health Bot. Required.</td>
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
    <td><CopyableCode code="accessControlMethod" /></td>
    <td><code>string</code></td>
    <td>The access control method for the Azure Health Bot resource.</td>
</tr>
<tr>
    <td><CopyableCode code="botManagementPortalLink" /></td>
    <td><code>string</code></td>
    <td>The link.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Azure Health Bot.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>KeyVault properties for the resource encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Azure Health Bot resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the Azure Health Bot. Required.</td>
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
<TabItem value="list">

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
    <td><CopyableCode code="accessControlMethod" /></td>
    <td><code>string</code></td>
    <td>The access control method for the Azure Health Bot resource.</td>
</tr>
<tr>
    <td><CopyableCode code="botManagementPortalLink" /></td>
    <td><code>string</code></td>
    <td>The link.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Azure Health Bot.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>KeyVault properties for the resource encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Azure Health Bot resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the Azure Health Bot. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bot_name"><code>bot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a HealthBot.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bot_name"><code>bot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create a new Azure Health Bot.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bot_name"><code>bot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a HealthBot.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bot_name"><code>bot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a HealthBot.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bot_name"><code>bot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all secrets of a HealthBot.</td>
</tr>
<tr>
    <td><a href="#regenerate_api_jwt_secret"><CopyableCode code="regenerate_api_jwt_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bot_name"><code>bot_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerate the API JWT Secret of a HealthBot.</td>
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
<tr id="parameter-bot_name">
    <td><CopyableCode code="bot_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bot resource. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a HealthBot.

```sql
SELECT
id,
name,
accessControlMethod,
botManagementPortalLink,
identity,
keyVaultProperties,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure_extras.health_bot.bots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND bot_name = '{{ bot_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Returns all the resources of a particular type belonging to a resource group.

```sql
SELECT
id,
name,
accessControlMethod,
botManagementPortalLink,
identity,
keyVaultProperties,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure_extras.health_bot.bots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all the resources of a particular type belonging to a subscription.

```sql
SELECT
id,
name,
accessControlMethod,
botManagementPortalLink,
identity,
keyVaultProperties,
location,
provisioningState,
sku,
systemData,
tags,
type
FROM azure_extras.health_bot.bots
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

Create a new Azure Health Bot.

```sql
INSERT INTO azure_extras.health_bot.bots (
tags,
location,
properties,
sku,
identity,
resource_group_name,
bot_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ bot_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bots resource.
    - name: bot_name
      value: "{{ bot_name }}"
      description: Required parameter for the bots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bots resource.
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
        The set of properties specific to Azure Health Bot resource.
      value:
        provisioningState: "{{ provisioningState }}"
        botManagementPortalLink: "{{ botManagementPortalLink }}"
        keyVaultProperties:
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
          keyVaultUri: "{{ keyVaultUri }}"
          userIdentity: "{{ userIdentity }}"
        accessControlMethod: "{{ accessControlMethod }}"
    - name: sku
      description: |
        SKU of the Azure Health Bot. Required.
      value:
        name: "{{ name }}"
    - name: identity
      description: |
        The identity of the Azure Health Bot.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Patch a HealthBot.

```sql
UPDATE azure_extras.health_bot.bots
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bot_name = '{{ bot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Delete a HealthBot.

```sql
DELETE FROM azure_extras.health_bot.bots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND bot_name = '{{ bot_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_secrets"
    values={[
        { label: 'list_secrets', value: 'list_secrets' },
        { label: 'regenerate_api_jwt_secret', value: 'regenerate_api_jwt_secret' }
    ]}
>
<TabItem value="list_secrets">

List all secrets of a HealthBot.

```sql
EXEC azure_extras.health_bot.bots.list_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@bot_name='{{ bot_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_api_jwt_secret">

Regenerate the API JWT Secret of a HealthBot.

```sql
EXEC azure_extras.health_bot.bots.regenerate_api_jwt_secret 
@resource_group_name='{{ resource_group_name }}' --required, 
@bot_name='{{ bot_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
