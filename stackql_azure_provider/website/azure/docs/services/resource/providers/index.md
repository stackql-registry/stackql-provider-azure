--- 
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - resource
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

Creates, updates, deletes, gets or lists a <code>providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.providers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_at_tenant_scope', value: 'get_at_tenant_scope' },
        { label: 'list_at_tenant_scope', value: 'list_at_tenant_scope' }
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
    <td>The provider ID.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerAuthorizationConsentState" /></td>
    <td><code>string</code></td>
    <td>The provider authorization consent state. Known values are: "NotSpecified", "Required", "NotRequired", and "Consented". (NotSpecified, Required, NotRequired, Consented)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationPolicy" /></td>
    <td><code>string</code></td>
    <td>The registration policy of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationState" /></td>
    <td><code>string</code></td>
    <td>The registration state of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTypes" /></td>
    <td><code>array</code></td>
    <td>The collection of provider resource types.</td>
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
    <td>The provider ID.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerAuthorizationConsentState" /></td>
    <td><code>string</code></td>
    <td>The provider authorization consent state. Known values are: "NotSpecified", "Required", "NotRequired", and "Consented". (NotSpecified, Required, NotRequired, Consented)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationPolicy" /></td>
    <td><code>string</code></td>
    <td>The registration policy of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationState" /></td>
    <td><code>string</code></td>
    <td>The registration state of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTypes" /></td>
    <td><code>array</code></td>
    <td>The collection of provider resource types.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_tenant_scope">

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
    <td>The provider ID.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerAuthorizationConsentState" /></td>
    <td><code>string</code></td>
    <td>The provider authorization consent state. Known values are: "NotSpecified", "Required", "NotRequired", and "Consented". (NotSpecified, Required, NotRequired, Consented)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationPolicy" /></td>
    <td><code>string</code></td>
    <td>The registration policy of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationState" /></td>
    <td><code>string</code></td>
    <td>The registration state of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTypes" /></td>
    <td><code>array</code></td>
    <td>The collection of provider resource types.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_tenant_scope">

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
    <td>The provider ID.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerAuthorizationConsentState" /></td>
    <td><code>string</code></td>
    <td>The provider authorization consent state. Known values are: "NotSpecified", "Required", "NotRequired", and "Consented". (NotSpecified, Required, NotRequired, Consented)</td>
</tr>
<tr>
    <td><CopyableCode code="registrationPolicy" /></td>
    <td><code>string</code></td>
    <td>The registration policy of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationState" /></td>
    <td><code>string</code></td>
    <td>The registration state of the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceTypes" /></td>
    <td><code>array</code></td>
    <td>The collection of provider resource types.</td>
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
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified resource provider.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets all resource providers for a subscription.</td>
</tr>
<tr>
    <td><a href="#get_at_tenant_scope"><CopyableCode code="get_at_tenant_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified resource provider at the tenant level.</td>
</tr>
<tr>
    <td><a href="#list_at_tenant_scope"><CopyableCode code="list_at_tenant_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets all resource providers for the tenant.</td>
</tr>
<tr>
    <td><a href="#unregister"><CopyableCode code="unregister" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Unregisters a subscription from a resource provider.</td>
</tr>
<tr>
    <td><a href="#register_at_management_group_scope"><CopyableCode code="register_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Registers a management group with a resource provider. Use this operation to register a resource provider with resource types that can be deployed at the management group scope. It does not recursively register subscriptions within the management group. Instead, you must register subscriptions individually.</td>
</tr>
<tr>
    <td><a href="#provider_permissions"><CopyableCode code="provider_permissions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the provider permissions.</td>
</tr>
<tr>
    <td><a href="#register"><CopyableCode code="register" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Registers a subscription with a resource provider.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider to register. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The properties to include in the results. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_at_tenant_scope', value: 'get_at_tenant_scope' },
        { label: 'list_at_tenant_scope', value: 'list_at_tenant_scope' }
    ]}
>
<TabItem value="get">

Gets the specified resource provider.

```sql
SELECT
id,
namespace,
providerAuthorizationConsentState,
registrationPolicy,
registrationState,
resourceTypes
FROM azure.resource.providers
WHERE resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets all resource providers for a subscription.

```sql
SELECT
id,
namespace,
providerAuthorizationConsentState,
registrationPolicy,
registrationState,
resourceTypes
FROM azure.resource.providers
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_at_tenant_scope">

Gets the specified resource provider at the tenant level.

```sql
SELECT
id,
namespace,
providerAuthorizationConsentState,
registrationPolicy,
registrationState,
resourceTypes
FROM azure.resource.providers
WHERE resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_at_tenant_scope">

Gets all resource providers for the tenant.

```sql
SELECT
id,
namespace,
providerAuthorizationConsentState,
registrationPolicy,
registrationState,
resourceTypes
FROM azure.resource.providers
WHERE $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="unregister"
    values={[
        { label: 'unregister', value: 'unregister' },
        { label: 'register_at_management_group_scope', value: 'register_at_management_group_scope' },
        { label: 'provider_permissions', value: 'provider_permissions' },
        { label: 'register', value: 'register' }
    ]}
>
<TabItem value="unregister">

Unregisters a subscription from a resource provider.

```sql
EXEC azure.resource.providers.unregister 
@resource_provider_namespace='{{ resource_provider_namespace }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="register_at_management_group_scope">

Registers a management group with a resource provider. Use this operation to register a resource provider with resource types that can be deployed at the management group scope. It does not recursively register subscriptions within the management group. Instead, you must register subscriptions individually.

```sql
EXEC azure.resource.providers.register_at_management_group_scope 
@resource_provider_namespace='{{ resource_provider_namespace }}' --required, 
@group_id='{{ group_id }}' --required
;
```
</TabItem>
<TabItem value="provider_permissions">

Get the provider permissions.

```sql
EXEC azure.resource.providers.provider_permissions 
@resource_provider_namespace='{{ resource_provider_namespace }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="register">

Registers a subscription with a resource provider.

```sql
EXEC azure.resource.providers.register 
@resource_provider_namespace='{{ resource_provider_namespace }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"thirdPartyProviderConsent": "{{ thirdPartyProviderConsent }}"
}'
;
```
</TabItem>
</Tabs>
