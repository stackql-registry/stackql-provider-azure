--- 
title: authorization_server
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server
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

Creates, updates, deletes, gets or lists an <code>authorization_server</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authorization_server" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_server" /></td></tr>
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
    <td><CopyableCode code="authorizationEndpoint" /></td>
    <td><code>string</code></td>
    <td>OAuth authorization endpoint. See `http://tools.ietf.org/html/rfc6749#section-3.2 `_. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationMethods" /></td>
    <td><code>array</code></td>
    <td>HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.</td>
</tr>
<tr>
    <td><CopyableCode code="bearerTokenSendingMethods" /></td>
    <td><code>array</code></td>
    <td>Specifies the mechanism by which access token is passed to the API.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAuthenticationMethod" /></td>
    <td><code>array</code></td>
    <td>Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>Client or app id registered with this authorization server. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientRegistrationEndpoint" /></td>
    <td><code>string</code></td>
    <td>Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>Client or app secret registered with this authorization server. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultScope" /></td>
    <td><code>string</code></td>
    <td>Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the authorization server. Can contain HTML formatting tags.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User-friendly authorization server name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="grantTypes" /></td>
    <td><code>array</code></td>
    <td>Form of an authorization grant, which the client uses to request the access token. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceOwnerPassword" /></td>
    <td><code>string</code></td>
    <td>Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceOwnerUsername" /></td>
    <td><code>string</code></td>
    <td>Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.</td>
</tr>
<tr>
    <td><CopyableCode code="supportState" /></td>
    <td><code>boolean</code></td>
    <td>If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenBodyParameters" /></td>
    <td><code>array</code></td>
    <td>Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. &#123;"name" : "name value", "value": "a value"&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEndpoint" /></td>
    <td><code>string</code></td>
    <td>OAuth token endpoint. Contains absolute URI to entity being referenced.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useInApiDocumentation" /></td>
    <td><code>boolean</code></td>
    <td>If true, the authorization server will be used in the API documentation in the developer portal. False by default if no value is provided.</td>
</tr>
<tr>
    <td><CopyableCode code="useInTestConsole" /></td>
    <td><code>boolean</code></td>
    <td>If true, the authorization server may be used in the developer portal test console. True by default if no value is provided.</td>
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
    <td><CopyableCode code="authorizationEndpoint" /></td>
    <td><code>string</code></td>
    <td>OAuth authorization endpoint. See `http://tools.ietf.org/html/rfc6749#section-3.2 `_. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationMethods" /></td>
    <td><code>array</code></td>
    <td>HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.</td>
</tr>
<tr>
    <td><CopyableCode code="bearerTokenSendingMethods" /></td>
    <td><code>array</code></td>
    <td>Specifies the mechanism by which access token is passed to the API.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAuthenticationMethod" /></td>
    <td><code>array</code></td>
    <td>Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>Client or app id registered with this authorization server. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientRegistrationEndpoint" /></td>
    <td><code>string</code></td>
    <td>Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>Client or app secret registered with this authorization server. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultScope" /></td>
    <td><code>string</code></td>
    <td>Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the authorization server. Can contain HTML formatting tags.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User-friendly authorization server name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="grantTypes" /></td>
    <td><code>array</code></td>
    <td>Form of an authorization grant, which the client uses to request the access token. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceOwnerPassword" /></td>
    <td><code>string</code></td>
    <td>Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceOwnerUsername" /></td>
    <td><code>string</code></td>
    <td>Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.</td>
</tr>
<tr>
    <td><CopyableCode code="supportState" /></td>
    <td><code>boolean</code></td>
    <td>If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenBodyParameters" /></td>
    <td><code>array</code></td>
    <td>Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. &#123;"name" : "name value", "value": "a value"&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEndpoint" /></td>
    <td><code>string</code></td>
    <td>OAuth token endpoint. Contains absolute URI to entity being referenced.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useInApiDocumentation" /></td>
    <td><code>boolean</code></td>
    <td>If true, the authorization server will be used in the API documentation in the developer portal. False by default if no value is provided.</td>
</tr>
<tr>
    <td><CopyableCode code="useInTestConsole" /></td>
    <td><code>boolean</code></td>
    <td>If true, the authorization server may be used in the developer portal test console. True by default if no value is provided.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the authorization server specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_service"><CopyableCode code="list_by_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Lists a collection of authorization servers defined within a service instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates new authorization server or updates an existing authorization server.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the details of the authorization server specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates new authorization server or updates an existing authorization server.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes specific authorization server instance.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the entity state (Etag) version of the authorizationServer specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_secrets"><CopyableCode code="list_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-authsid"><code>authsid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the client secret details of the authorization server.</td>
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
<tr id="parameter-authsid">
    <td><CopyableCode code="authsid" /></td>
    <td><code>string</code></td>
    <td>Identifier of the authorization server. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Usage | Supported operators | Supported functions ||-------------|-------------|-------------|-------------|| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith || displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of records to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of records to return. Default value is None.</td>
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

Gets the details of the authorization server specified by its identifier.

```sql
SELECT
id,
name,
authorizationEndpoint,
authorizationMethods,
bearerTokenSendingMethods,
clientAuthenticationMethod,
clientId,
clientRegistrationEndpoint,
clientSecret,
defaultScope,
description,
displayName,
grantTypes,
resourceOwnerPassword,
resourceOwnerUsername,
supportState,
systemData,
tokenBodyParameters,
tokenEndpoint,
type,
useInApiDocumentation,
useInTestConsole
FROM azure.api_management.authorization_server
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND authsid = '{{ authsid }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_service">

Lists a collection of authorization servers defined within a service instance.

```sql
SELECT
id,
name,
authorizationEndpoint,
authorizationMethods,
bearerTokenSendingMethods,
clientAuthenticationMethod,
clientId,
clientRegistrationEndpoint,
clientSecret,
defaultScope,
description,
displayName,
grantTypes,
resourceOwnerPassword,
resourceOwnerUsername,
supportState,
systemData,
tokenBodyParameters,
tokenEndpoint,
type,
useInApiDocumentation,
useInTestConsole
FROM azure.api_management.authorization_server
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
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

Creates new authorization server or updates an existing authorization server.

```sql
INSERT INTO azure.api_management.authorization_server (
properties,
resource_group_name,
service_name,
authsid,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ authsid }}',
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
- name: authorization_server
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the authorization_server resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the authorization_server resource.
    - name: authsid
      value: "{{ authsid }}"
      description: Required parameter for the authorization_server resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the authorization_server resource.
    - name: properties
      description: |
        Properties of the External OAuth authorization server Contract.
      value:
        description: "{{ description }}"
        authorizationMethods:
          - "{{ authorizationMethods }}"
        clientAuthenticationMethod:
          - "{{ clientAuthenticationMethod }}"
        tokenBodyParameters:
          - name: "{{ name }}"
            value: "{{ value }}"
        tokenEndpoint: "{{ tokenEndpoint }}"
        supportState: {{ supportState }}
        defaultScope: "{{ defaultScope }}"
        bearerTokenSendingMethods:
          - "{{ bearerTokenSendingMethods }}"
        resourceOwnerUsername: "{{ resourceOwnerUsername }}"
        resourceOwnerPassword: "{{ resourceOwnerPassword }}"
        displayName: "{{ displayName }}"
        useInTestConsole: {{ useInTestConsole }}
        useInApiDocumentation: {{ useInApiDocumentation }}
        clientRegistrationEndpoint: "{{ clientRegistrationEndpoint }}"
        authorizationEndpoint: "{{ authorizationEndpoint }}"
        grantTypes:
          - "{{ grantTypes }}"
        clientId: "{{ clientId }}"
        clientSecret: "{{ clientSecret }}"
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

Updates the details of the authorization server specified by its identifier.

```sql
UPDATE azure.api_management.authorization_server
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND authsid = '{{ authsid }}' --required
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

Creates new authorization server or updates an existing authorization server.

```sql
REPLACE azure.api_management.authorization_server
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND authsid = '{{ authsid }}' --required
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

Deletes specific authorization server instance.

```sql
DELETE FROM azure.api_management.authorization_server
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND authsid = '{{ authsid }}' --required
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

Gets the entity state (Etag) version of the authorizationServer specified by its identifier.

```sql
EXEC azure.api_management.authorization_server.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@authsid='{{ authsid }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_secrets">

Gets the client secret details of the authorization server.

```sql
EXEC azure.api_management.authorization_server.list_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@authsid='{{ authsid }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
