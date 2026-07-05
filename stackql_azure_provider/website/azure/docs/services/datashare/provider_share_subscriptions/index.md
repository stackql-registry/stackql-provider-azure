--- 
title: provider_share_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_share_subscriptions
  - datashare
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

Creates, updates, deletes, gets or lists a <code>provider_share_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_share_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datashare.provider_share_subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_share"
    values={[
        { label: 'get_by_share', value: 'get_by_share' },
        { label: 'list_by_share', value: 'list_by_share' }
    ]}
>
<TabItem value="get_by_share">

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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="consumerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the consumer who created the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="consumerName" /></td>
    <td><code>string</code></td>
    <td>Name of the consumer who created the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="consumerTenantName" /></td>
    <td><code>string</code></td>
    <td>Tenant name of the consumer who created the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>created at.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of the share subscription in UTC format.</td>
</tr>
<tr>
    <td><CopyableCode code="providerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the provider who created the share.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the provider who created the share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareSubscriptionObjectId" /></td>
    <td><code>string</code></td>
    <td>share Subscription Object Id.</td>
</tr>
<tr>
    <td><CopyableCode code="shareSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets the status of share subscription. Known values are: "Active", "Revoked", "SourceDeleted", and "Revoking".</td>
</tr>
<tr>
    <td><CopyableCode code="sharedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shared at.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_share">

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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="consumerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the consumer who created the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="consumerName" /></td>
    <td><code>string</code></td>
    <td>Name of the consumer who created the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="consumerTenantName" /></td>
    <td><code>string</code></td>
    <td>Tenant name of the consumer who created the share subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>created at.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of the share subscription in UTC format.</td>
</tr>
<tr>
    <td><CopyableCode code="providerEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the provider who created the share.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>Name of the provider who created the share.</td>
</tr>
<tr>
    <td><CopyableCode code="shareSubscriptionObjectId" /></td>
    <td><code>string</code></td>
    <td>share Subscription Object Id.</td>
</tr>
<tr>
    <td><CopyableCode code="shareSubscriptionStatus" /></td>
    <td><code>string</code></td>
    <td>Gets the status of share subscription. Known values are: "Active", "Revoked", "SourceDeleted", and "Revoking".</td>
</tr>
<tr>
    <td><CopyableCode code="sharedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shared at.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
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
    <td><a href="#get_by_share"><CopyableCode code="get_by_share" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-provider_share_subscription_id"><code>provider_share_subscription_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get share subscription in a provider share. Get share subscription in a provider share.</td>
</tr>
<tr>
    <td><a href="#list_by_share"><CopyableCode code="list_by_share" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List of available share subscriptions to a provider share. List share subscriptions in a provider share.</td>
</tr>
<tr>
    <td><a href="#adjust"><CopyableCode code="adjust" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-provider_share_subscription_id"><code>provider_share_subscription_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adjust the expiration date of a share subscription in a provider share. Adjust a share subscription's expiration date in a provider share.</td>
</tr>
<tr>
    <td><a href="#reinstate"><CopyableCode code="reinstate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-provider_share_subscription_id"><code>provider_share_subscription_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reinstate share subscription in a provider share. Reinstate share subscription in a provider share.</td>
</tr>
<tr>
    <td><a href="#revoke"><CopyableCode code="revoke" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-provider_share_subscription_id"><code>provider_share_subscription_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Revoke share subscription in a provider share. Revoke share subscription in a provider share.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share account. Required.</td>
</tr>
<tr id="parameter-provider_share_subscription_id">
    <td><CopyableCode code="provider_share_subscription_id" /></td>
    <td><code>string</code></td>
    <td>To locate shareSubscription. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-share_name">
    <td><CopyableCode code="share_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Continuation Token. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_share"
    values={[
        { label: 'get_by_share', value: 'get_by_share' },
        { label: 'list_by_share', value: 'list_by_share' }
    ]}
>
<TabItem value="get_by_share">

Get share subscription in a provider share. Get share subscription in a provider share.

```sql
SELECT
id,
name,
consumerEmail,
consumerName,
consumerTenantName,
createdAt,
expirationDate,
providerEmail,
providerName,
shareSubscriptionObjectId,
shareSubscriptionStatus,
sharedAt,
systemData,
type
FROM azure.datashare.provider_share_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND provider_share_subscription_id = '{{ provider_share_subscription_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_share">

List of available share subscriptions to a provider share. List share subscriptions in a provider share.

```sql
SELECT
id,
name,
consumerEmail,
consumerName,
consumerTenantName,
createdAt,
expirationDate,
providerEmail,
providerName,
shareSubscriptionObjectId,
shareSubscriptionStatus,
sharedAt,
systemData,
type
FROM azure.datashare.provider_share_subscriptions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="adjust"
    values={[
        { label: 'adjust', value: 'adjust' },
        { label: 'reinstate', value: 'reinstate' },
        { label: 'revoke', value: 'revoke' }
    ]}
>
<TabItem value="adjust">

Adjust the expiration date of a share subscription in a provider share. Adjust a share subscription's expiration date in a provider share.

```sql
EXEC azure.datashare.provider_share_subscriptions.adjust 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_name='{{ share_name }}' --required, 
@provider_share_subscription_id='{{ provider_share_subscription_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="reinstate">

Reinstate share subscription in a provider share. Reinstate share subscription in a provider share.

```sql
EXEC azure.datashare.provider_share_subscriptions.reinstate 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_name='{{ share_name }}' --required, 
@provider_share_subscription_id='{{ provider_share_subscription_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="revoke">

Revoke share subscription in a provider share. Revoke share subscription in a provider share.

```sql
EXEC azure.datashare.provider_share_subscriptions.revoke 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@share_name='{{ share_name }}' --required, 
@provider_share_subscription_id='{{ provider_share_subscription_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
