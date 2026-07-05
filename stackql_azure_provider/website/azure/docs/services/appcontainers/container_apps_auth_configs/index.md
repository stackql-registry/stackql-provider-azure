--- 
title: container_apps_auth_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_auth_configs
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>container_apps_auth_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_auth_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.container_apps_auth_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_container_app', value: 'list_by_container_app' }
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
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the secrets references of encryption key and signing key for ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="globalValidation" /></td>
    <td><code>object</code></td>
    <td>The configuration settings that determines the validation flow of users using Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="httpSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProviders" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="login" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the platform of ContainerApp Service Authentication/Authorization.</td>
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
<TabItem value="list_by_container_app">

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
    <td><CopyableCode code="encryptionSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the secrets references of encryption key and signing key for ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="globalValidation" /></td>
    <td><code>object</code></td>
    <td>The configuration settings that determines the validation flow of users using Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="httpSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProviders" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="login" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>object</code></td>
    <td>The configuration settings of the platform of ContainerApp Service Authentication/Authorization.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-auth_config_name"><code>auth_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AuthConfig of a Container App. Get a AuthConfig of a Container App.</td>
</tr>
<tr>
    <td><a href="#list_by_container_app"><CopyableCode code="list_by_container_app" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Container App AuthConfigs in a given resource group. Get the Container App AuthConfigs in a given resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-auth_config_name"><code>auth_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the AuthConfig for a Container App. Create or update the AuthConfig for a Container App.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-auth_config_name"><code>auth_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the AuthConfig for a Container App. Create or update the AuthConfig for a Container App.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-auth_config_name"><code>auth_config_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Container App AuthConfig. Delete a Container App AuthConfig.</td>
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
<tr id="parameter-auth_config_name">
    <td><CopyableCode code="auth_config_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App AuthConfig. Required.</td>
</tr>
<tr id="parameter-container_app_name">
    <td><CopyableCode code="container_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App. Required.</td>
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
        { label: 'list_by_container_app', value: 'list_by_container_app' }
    ]}
>
<TabItem value="get">

Get a AuthConfig of a Container App. Get a AuthConfig of a Container App.

```sql
SELECT
id,
name,
encryptionSettings,
globalValidation,
httpSettings,
identityProviders,
login,
platform,
systemData,
type
FROM azure.appcontainers.container_apps_auth_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND auth_config_name = '{{ auth_config_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_container_app">

Get the Container App AuthConfigs in a given resource group. Get the Container App AuthConfigs in a given resource group.

```sql
SELECT
id,
name,
encryptionSettings,
globalValidation,
httpSettings,
identityProviders,
login,
platform,
systemData,
type
FROM azure.appcontainers.container_apps_auth_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
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

Create or update the AuthConfig for a Container App. Create or update the AuthConfig for a Container App.

```sql
INSERT INTO azure.appcontainers.container_apps_auth_configs (
properties,
resource_group_name,
container_app_name,
auth_config_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ container_app_name }}',
'{{ auth_config_name }}',
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
- name: container_apps_auth_configs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the container_apps_auth_configs resource.
    - name: container_app_name
      value: "{{ container_app_name }}"
      description: Required parameter for the container_apps_auth_configs resource.
    - name: auth_config_name
      value: "{{ auth_config_name }}"
      description: Required parameter for the container_apps_auth_configs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the container_apps_auth_configs resource.
    - name: properties
      description: |
        AuthConfig resource specific properties.
      value:
        platform:
          enabled: {{ enabled }}
          runtimeVersion: "{{ runtimeVersion }}"
        globalValidation:
          unauthenticatedClientAction: "{{ unauthenticatedClientAction }}"
          redirectToProvider: "{{ redirectToProvider }}"
          excludedPaths:
            - "{{ excludedPaths }}"
        identityProviders:
          azureActiveDirectory:
            enabled: {{ enabled }}
            registration:
              openIdIssuer: "{{ openIdIssuer }}"
              clientId: "{{ clientId }}"
              clientSecretSettingName: "{{ clientSecretSettingName }}"
              clientSecretCertificateThumbprint: "{{ clientSecretCertificateThumbprint }}"
              clientSecretCertificateSubjectAlternativeName: "{{ clientSecretCertificateSubjectAlternativeName }}"
              clientSecretCertificateIssuer: "{{ clientSecretCertificateIssuer }}"
            login:
              loginParameters:
                - "{{ loginParameters }}"
              disableWWWAuthenticate: {{ disableWWWAuthenticate }}
            validation:
              jwtClaimChecks:
                allowedGroups: "{{ allowedGroups }}"
                allowedClientApplications: "{{ allowedClientApplications }}"
              allowedAudiences:
                - "{{ allowedAudiences }}"
              defaultAuthorizationPolicy:
                allowedPrincipals: "{{ allowedPrincipals }}"
                allowedApplications: "{{ allowedApplications }}"
            isAutoProvisioned: {{ isAutoProvisioned }}
          facebook:
            enabled: {{ enabled }}
            registration:
              appId: "{{ appId }}"
              appSecretSettingName: "{{ appSecretSettingName }}"
            graphApiVersion: "{{ graphApiVersion }}"
            login:
              scopes:
                - "{{ scopes }}"
          gitHub:
            enabled: {{ enabled }}
            registration:
              clientId: "{{ clientId }}"
              clientSecretSettingName: "{{ clientSecretSettingName }}"
            login:
              scopes:
                - "{{ scopes }}"
          google:
            enabled: {{ enabled }}
            registration:
              clientId: "{{ clientId }}"
              clientSecretSettingName: "{{ clientSecretSettingName }}"
            login:
              scopes:
                - "{{ scopes }}"
            validation:
              allowedAudiences:
                - "{{ allowedAudiences }}"
          twitter:
            enabled: {{ enabled }}
            registration:
              consumerKey: "{{ consumerKey }}"
              consumerSecretSettingName: "{{ consumerSecretSettingName }}"
          apple:
            enabled: {{ enabled }}
            registration:
              clientId: "{{ clientId }}"
              clientSecretSettingName: "{{ clientSecretSettingName }}"
            login:
              scopes:
                - "{{ scopes }}"
          azureStaticWebApps:
            enabled: {{ enabled }}
            registration:
              clientId: "{{ clientId }}"
          customOpenIdConnectProviders: "{{ customOpenIdConnectProviders }}"
        login:
          routes:
            logoutEndpoint: "{{ logoutEndpoint }}"
          tokenStore:
            enabled: {{ enabled }}
            tokenRefreshExtensionHours: {{ tokenRefreshExtensionHours }}
            azureBlobStorage:
              sasUrlSettingName: "{{ sasUrlSettingName }}"
          preserveUrlFragmentsForLogins: {{ preserveUrlFragmentsForLogins }}
          allowedExternalRedirectUrls:
            - "{{ allowedExternalRedirectUrls }}"
          cookieExpiration:
            convention: "{{ convention }}"
            timeToExpiration: "{{ timeToExpiration }}"
          nonce:
            validateNonce: {{ validateNonce }}
            nonceExpirationInterval: "{{ nonceExpirationInterval }}"
        httpSettings:
          requireHttps: {{ requireHttps }}
          routes:
            apiPrefix: "{{ apiPrefix }}"
          forwardProxy:
            convention: "{{ convention }}"
            customHostHeaderName: "{{ customHostHeaderName }}"
            customProtoHeaderName: "{{ customProtoHeaderName }}"
        encryptionSettings:
          containerAppAuthEncryptionSecretName: "{{ containerAppAuthEncryptionSecretName }}"
          containerAppAuthSigningSecretName: "{{ containerAppAuthSigningSecretName }}"
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

Create or update the AuthConfig for a Container App. Create or update the AuthConfig for a Container App.

```sql
REPLACE azure.appcontainers.container_apps_auth_configs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND auth_config_name = '{{ auth_config_name }}' --required
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

Delete a Container App AuthConfig. Delete a Container App AuthConfig.

```sql
DELETE FROM azure.appcontainers.container_apps_auth_configs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND auth_config_name = '{{ auth_config_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
