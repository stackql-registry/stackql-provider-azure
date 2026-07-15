--- 
title: identity_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider
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

Creates, updates, deletes, gets or lists an <code>identity_provider</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="identity_provider" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.identity_provider" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
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
    <td><CopyableCode code="allowedTenants" /></td>
    <td><code>array</code></td>
    <td>List of Allowed Tenants when configuring Azure Active Directory login.</td>
</tr>
<tr>
    <td><CopyableCode code="authority" /></td>
    <td><code>string</code></td>
    <td>OpenID Connect discovery endpoint hostname for AAD or AAD B2C.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateId" /></td>
    <td><code>string</code></td>
    <td>Certificate full resource ID used in external Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientLibrary" /></td>
    <td><code>string</code></td>
    <td>The client library to be used in the developer portal. Only applies to AAD and AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordResetPolicyName" /></td>
    <td><code>string</code></td>
    <td>Password Reset Policy Name. Only applies to AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="profileEditingPolicyName" /></td>
    <td><code>string</code></td>
    <td>Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="signinPolicyName" /></td>
    <td><code>string</code></td>
    <td>Signin Policy Name. Only applies to AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="signinTenant" /></td>
    <td><code>string</code></td>
    <td>The TenantId to use instead of Common when logging into Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="signupPolicyName" /></td>
    <td><code>string</code></td>
    <td>Signup Policy Name. Only applies to AAD B2C Identity Provider.</td>
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
<TabItem value="list_by_service">

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
    <td><CopyableCode code="allowedTenants" /></td>
    <td><code>array</code></td>
    <td>List of Allowed Tenants when configuring Azure Active Directory login.</td>
</tr>
<tr>
    <td><CopyableCode code="authority" /></td>
    <td><code>string</code></td>
    <td>OpenID Connect discovery endpoint hostname for AAD or AAD B2C.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateId" /></td>
    <td><code>string</code></td>
    <td>Certificate full resource ID used in external Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientLibrary" /></td>
    <td><code>string</code></td>
    <td>The client library to be used in the developer portal. Only applies to AAD and AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordResetPolicyName" /></td>
    <td><code>string</code></td>
    <td>Password Reset Policy Name. Only applies to AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="profileEditingPolicyName" /></td>
    <td><code>string</code></td>
    <td>Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="signinPolicyName" /></td>
    <td><code>string</code></td>
    <td>Signin Policy Name. Only applies to AAD B2C Identity Provider.</td>
</tr>
<tr>
    <td><CopyableCode code="signinTenant" /></td>
    <td><code>string</code></td>
    <td>The TenantId to use instead of Common when logging into Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="signupPolicyName" /></td>
    <td><code>string</code></td>
    <td>Signup Policy Name. Only applies to AAD B2C Identity Provider.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the configuration details of the identity Provider configured in specified service instance.</td>
</tr>
<tr>
    <td><a href="#list_by_service"><CopyableCode code="list_by_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists a collection of Identity Provider configured in the specified service instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates the IdentityProvider configuration.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing IdentityProvider configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates the IdentityProvider configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified identity provider configuration.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the identityProvider specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-identity_provider_name"><code>identity_provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the client secret details of the Identity Provider.</td>
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
<tr id="parameter-identity_provider_name">
    <td><CopyableCode code="identity_provider_name" /></td>
    <td><code>string</code></td>
    <td>Identity Provider Type identifier. Known values are: "facebook", "google", "microsoft", "twitter", "aad", and "aadB2C". Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
    ]}
>
<TabItem value="get">

Gets the configuration details of the identity Provider configured in specified service instance.

```sql
SELECT
id,
name,
allowedTenants,
authority,
certificateId,
clientId,
clientLibrary,
clientSecret,
passwordResetPolicyName,
profileEditingPolicyName,
signinPolicyName,
signinTenant,
signupPolicyName,
systemData,
type
FROM azure.api_management.identity_provider
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND identity_provider_name = '{{ identity_provider_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_service">

Lists a collection of Identity Provider configured in the specified service instance.

```sql
SELECT
id,
name,
allowedTenants,
authority,
certificateId,
clientId,
clientLibrary,
clientSecret,
passwordResetPolicyName,
profileEditingPolicyName,
signinPolicyName,
signinTenant,
signupPolicyName,
systemData,
type
FROM azure.api_management.identity_provider
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
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

Creates or Updates the IdentityProvider configuration.

```sql
INSERT INTO azure.api_management.identity_provider (
properties,
resource_group_name,
service_name,
identity_provider_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ identity_provider_name }}',
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
- name: identity_provider
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the identity_provider resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the identity_provider resource.
    - name: identity_provider_name
      value: "{{ identity_provider_name }}"
      description: Required parameter for the identity_provider resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the identity_provider resource.
    - name: properties
      description: |
        Identity Provider contract properties.
      value:
        type: "{{ type }}"
        signinTenant: "{{ signinTenant }}"
        allowedTenants:
          - "{{ allowedTenants }}"
        authority: "{{ authority }}"
        signupPolicyName: "{{ signupPolicyName }}"
        signinPolicyName: "{{ signinPolicyName }}"
        profileEditingPolicyName: "{{ profileEditingPolicyName }}"
        passwordResetPolicyName: "{{ passwordResetPolicyName }}"
        clientLibrary: "{{ clientLibrary }}"
        clientId: "{{ clientId }}"
        clientSecret: "{{ clientSecret }}"
        certificateId: "{{ certificateId }}"
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

Updates an existing IdentityProvider configuration.

```sql
UPDATE azure.api_management.identity_provider
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND identity_provider_name = '{{ identity_provider_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or Updates the IdentityProvider configuration.

```sql
REPLACE azure.api_management.identity_provider
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND identity_provider_name = '{{ identity_provider_name }}' --required
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

Deletes the specified identity provider configuration.

```sql
DELETE FROM azure.api_management.identity_provider
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND identity_provider_name = '{{ identity_provider_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_entity_tag"
    values={[
        { label: 'get_entity_tag', value: 'get_entity_tag' },
        { label: 'list_secrets', value: 'list_secrets' }
    ]}
>
<TabItem value="get_entity_tag">

Gets the entity state (Etag) version of the identityProvider specified by its identifier.

```sql
EXEC azure.api_management.identity_provider.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@identity_provider_name='{{ identity_provider_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_secrets">

Gets the client secret details of the Identity Provider.

```sql
EXEC azure.api_management.identity_provider.list_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@identity_provider_name='{{ identity_provider_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
