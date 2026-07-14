--- 
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
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

Creates, updates, deletes, gets or lists a <code>bots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'get_check_name_availability', value: 'get_check_name_availability' }
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
    <td><CopyableCode code="allSettings" /></td>
    <td><code>object</code></td>
    <td>Contains resource all settings defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="appPasswordHint" /></td>
    <td><code>string</code></td>
    <td>The hint (e.g. keyVault secret resourceId) on how to fetch the app secret.</td>
</tr>
<tr>
    <td><CopyableCode code="cmekEncryptionStatus" /></td>
    <td><code>string</code></td>
    <td>The CMK encryption status.</td>
</tr>
<tr>
    <td><CopyableCode code="cmekKeyVaultUrl" /></td>
    <td><code>string</code></td>
    <td>The CMK Url.</td>
</tr>
<tr>
    <td><CopyableCode code="configuredChannels" /></td>
    <td><code>array</code></td>
    <td>Collection of channels for which the bot is configured.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightKey" /></td>
    <td><code>string</code></td>
    <td>The Application Insights key.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightsApiKey" /></td>
    <td><code>string</code></td>
    <td>The Application Insights Api Key.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightsApplicationId" /></td>
    <td><code>string</code></td>
    <td>The Application Insights App Id.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The Name of the bot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledChannels" /></td>
    <td><code>array</code></td>
    <td>Collection of channels for which the bot is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The bot's endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointVersion" /></td>
    <td><code>string</code></td>
    <td>The bot's endpoint version.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity Tag.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>The Icon Url of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="isCmekEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cmek is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeveloperAppInsightsApiKeySet" /></td>
    <td><code>boolean</code></td>
    <td>Whether the bot is developerAppInsightsApiKey set.</td>
</tr>
<tr>
    <td><CopyableCode code="isStreamingSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the bot is streaming supported.</td>
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
    <td><CopyableCode code="luisAppIds" /></td>
    <td><code>array</code></td>
    <td>Collection of LUIS App Ids.</td>
</tr>
<tr>
    <td><CopyableCode code="luisKey" /></td>
    <td><code>string</code></td>
    <td>The LUIS Key.</td>
</tr>
<tr>
    <td><CopyableCode code="manifestUrl" /></td>
    <td><code>string</code></td>
    <td>The bot's manifest url.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationToken" /></td>
    <td><code>string</code></td>
    <td>Token used to migrate non Azure bot to azure subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Id for the bot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppMSIResourceId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Managed Identity Resource Id for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppTenantId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Tenant Id for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppType" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Type for the bot. Known values are: "UserAssignedMSI", "SingleTenant", and "MultiTenant".</td>
</tr>
<tr>
    <td><CopyableCode code="openWithHint" /></td>
    <td><code>string</code></td>
    <td>The hint to browser (e.g. protocol handler) on how to open the bot for authoring.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Contains resource parameters defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections configured for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether the bot is in an isolated network. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publishingCredentials" /></td>
    <td><code>string</code></td>
    <td>Publishing credentials of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaTransformationVersion" /></td>
    <td><code>string</code></td>
    <td>The channel schema transformation version for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageResourceId" /></td>
    <td><code>string</code></td>
    <td>The storage resourceId for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Tenant Id for the bot.</td>
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
    <td><CopyableCode code="allSettings" /></td>
    <td><code>object</code></td>
    <td>Contains resource all settings defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="appPasswordHint" /></td>
    <td><code>string</code></td>
    <td>The hint (e.g. keyVault secret resourceId) on how to fetch the app secret.</td>
</tr>
<tr>
    <td><CopyableCode code="cmekEncryptionStatus" /></td>
    <td><code>string</code></td>
    <td>The CMK encryption status.</td>
</tr>
<tr>
    <td><CopyableCode code="cmekKeyVaultUrl" /></td>
    <td><code>string</code></td>
    <td>The CMK Url.</td>
</tr>
<tr>
    <td><CopyableCode code="configuredChannels" /></td>
    <td><code>array</code></td>
    <td>Collection of channels for which the bot is configured.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightKey" /></td>
    <td><code>string</code></td>
    <td>The Application Insights key.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightsApiKey" /></td>
    <td><code>string</code></td>
    <td>The Application Insights Api Key.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightsApplicationId" /></td>
    <td><code>string</code></td>
    <td>The Application Insights App Id.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The Name of the bot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledChannels" /></td>
    <td><code>array</code></td>
    <td>Collection of channels for which the bot is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The bot's endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointVersion" /></td>
    <td><code>string</code></td>
    <td>The bot's endpoint version.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity Tag.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>The Icon Url of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="isCmekEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cmek is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeveloperAppInsightsApiKeySet" /></td>
    <td><code>boolean</code></td>
    <td>Whether the bot is developerAppInsightsApiKey set.</td>
</tr>
<tr>
    <td><CopyableCode code="isStreamingSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the bot is streaming supported.</td>
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
    <td><CopyableCode code="luisAppIds" /></td>
    <td><code>array</code></td>
    <td>Collection of LUIS App Ids.</td>
</tr>
<tr>
    <td><CopyableCode code="luisKey" /></td>
    <td><code>string</code></td>
    <td>The LUIS Key.</td>
</tr>
<tr>
    <td><CopyableCode code="manifestUrl" /></td>
    <td><code>string</code></td>
    <td>The bot's manifest url.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationToken" /></td>
    <td><code>string</code></td>
    <td>Token used to migrate non Azure bot to azure subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Id for the bot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppMSIResourceId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Managed Identity Resource Id for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppTenantId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Tenant Id for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppType" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Type for the bot. Known values are: "UserAssignedMSI", "SingleTenant", and "MultiTenant".</td>
</tr>
<tr>
    <td><CopyableCode code="openWithHint" /></td>
    <td><code>string</code></td>
    <td>The hint to browser (e.g. protocol handler) on how to open the bot for authoring.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Contains resource parameters defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections configured for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether the bot is in an isolated network. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publishingCredentials" /></td>
    <td><code>string</code></td>
    <td>Publishing credentials of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaTransformationVersion" /></td>
    <td><code>string</code></td>
    <td>The channel schema transformation version for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageResourceId" /></td>
    <td><code>string</code></td>
    <td>The storage resourceId for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Tenant Id for the bot.</td>
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allSettings" /></td>
    <td><code>object</code></td>
    <td>Contains resource all settings defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="appPasswordHint" /></td>
    <td><code>string</code></td>
    <td>The hint (e.g. keyVault secret resourceId) on how to fetch the app secret.</td>
</tr>
<tr>
    <td><CopyableCode code="cmekEncryptionStatus" /></td>
    <td><code>string</code></td>
    <td>The CMK encryption status.</td>
</tr>
<tr>
    <td><CopyableCode code="cmekKeyVaultUrl" /></td>
    <td><code>string</code></td>
    <td>The CMK Url.</td>
</tr>
<tr>
    <td><CopyableCode code="configuredChannels" /></td>
    <td><code>array</code></td>
    <td>Collection of channels for which the bot is configured.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightKey" /></td>
    <td><code>string</code></td>
    <td>The Application Insights key.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightsApiKey" /></td>
    <td><code>string</code></td>
    <td>The Application Insights Api Key.</td>
</tr>
<tr>
    <td><CopyableCode code="developerAppInsightsApplicationId" /></td>
    <td><code>string</code></td>
    <td>The Application Insights App Id.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The Name of the bot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledChannels" /></td>
    <td><code>array</code></td>
    <td>Collection of channels for which the bot is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The bot's endpoint. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointVersion" /></td>
    <td><code>string</code></td>
    <td>The bot's endpoint version.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Entity Tag.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>The Icon Url of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="isCmekEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cmek is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeveloperAppInsightsApiKeySet" /></td>
    <td><code>boolean</code></td>
    <td>Whether the bot is developerAppInsightsApiKey set.</td>
</tr>
<tr>
    <td><CopyableCode code="isStreamingSupported" /></td>
    <td><code>boolean</code></td>
    <td>Whether the bot is streaming supported.</td>
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
    <td><CopyableCode code="luisAppIds" /></td>
    <td><code>array</code></td>
    <td>Collection of LUIS App Ids.</td>
</tr>
<tr>
    <td><CopyableCode code="luisKey" /></td>
    <td><code>string</code></td>
    <td>The LUIS Key.</td>
</tr>
<tr>
    <td><CopyableCode code="manifestUrl" /></td>
    <td><code>string</code></td>
    <td>The bot's manifest url.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationToken" /></td>
    <td><code>string</code></td>
    <td>Token used to migrate non Azure bot to azure subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Id for the bot. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppMSIResourceId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Managed Identity Resource Id for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppTenantId" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Tenant Id for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="msaAppType" /></td>
    <td><code>string</code></td>
    <td>Microsoft App Type for the bot. Known values are: "UserAssignedMSI", "SingleTenant", and "MultiTenant".</td>
</tr>
<tr>
    <td><CopyableCode code="openWithHint" /></td>
    <td><code>string</code></td>
    <td>The hint to browser (e.g. protocol handler) on how to open the bot for authoring.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Contains resource parameters defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of Private Endpoint Connections configured for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether the bot is in an isolated network. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publishingCredentials" /></td>
    <td><code>string</code></td>
    <td>Publishing credentials of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaTransformationVersion" /></td>
    <td><code>string</code></td>
    <td>The channel schema transformation version for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageResourceId" /></td>
    <td><code>string</code></td>
    <td>The storage resourceId for the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Tenant Id for the bot.</td>
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
<TabItem value="get_check_name_availability">

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
    <td><CopyableCode code="absCode" /></td>
    <td><code>string</code></td>
    <td>response code from ABS.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>additional message from the bot management api showing why a bot name is not available.</td>
</tr>
<tr>
    <td><CopyableCode code="valid" /></td>
    <td><code>boolean</code></td>
    <td>indicates if the bot name is valid.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a BotService specified by the parameters.</td>
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
    <td><a href="#get_check_name_availability"><CopyableCode code="get_check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Check whether a bot name is available.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a Bot Service. Bot Service is a resource group wide resource type.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Updates a Bot Service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Bot Service from the resource group.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'get_check_name_availability', value: 'get_check_name_availability' }
    ]}
>
<TabItem value="get">

Returns a BotService specified by the parameters.

```sql
SELECT
id,
name,
allSettings,
appPasswordHint,
cmekEncryptionStatus,
cmekKeyVaultUrl,
configuredChannels,
description,
developerAppInsightKey,
developerAppInsightsApiKey,
developerAppInsightsApplicationId,
disableLocalAuth,
displayName,
enabledChannels,
endpoint,
endpointVersion,
etag,
iconUrl,
isCmekEnabled,
isDeveloperAppInsightsApiKeySet,
isStreamingSupported,
kind,
location,
luisAppIds,
luisKey,
manifestUrl,
migrationToken,
msaAppId,
msaAppMSIResourceId,
msaAppTenantId,
msaAppType,
openWithHint,
parameters,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
publishingCredentials,
schemaTransformationVersion,
sku,
storageResourceId,
tags,
tenantId,
type,
zones
FROM azure.bot_service.bots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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
allSettings,
appPasswordHint,
cmekEncryptionStatus,
cmekKeyVaultUrl,
configuredChannels,
description,
developerAppInsightKey,
developerAppInsightsApiKey,
developerAppInsightsApplicationId,
disableLocalAuth,
displayName,
enabledChannels,
endpoint,
endpointVersion,
etag,
iconUrl,
isCmekEnabled,
isDeveloperAppInsightsApiKeySet,
isStreamingSupported,
kind,
location,
luisAppIds,
luisKey,
manifestUrl,
migrationToken,
msaAppId,
msaAppMSIResourceId,
msaAppTenantId,
msaAppType,
openWithHint,
parameters,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
publishingCredentials,
schemaTransformationVersion,
sku,
storageResourceId,
tags,
tenantId,
type,
zones
FROM azure.bot_service.bots
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
allSettings,
appPasswordHint,
cmekEncryptionStatus,
cmekKeyVaultUrl,
configuredChannels,
description,
developerAppInsightKey,
developerAppInsightsApiKey,
developerAppInsightsApplicationId,
disableLocalAuth,
displayName,
enabledChannels,
endpoint,
endpointVersion,
etag,
iconUrl,
isCmekEnabled,
isDeveloperAppInsightsApiKeySet,
isStreamingSupported,
kind,
location,
luisAppIds,
luisKey,
manifestUrl,
migrationToken,
msaAppId,
msaAppMSIResourceId,
msaAppTenantId,
msaAppType,
openWithHint,
parameters,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
publishingCredentials,
schemaTransformationVersion,
sku,
storageResourceId,
tags,
tenantId,
type,
zones
FROM azure.bot_service.bots
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_check_name_availability">

Check whether a bot name is available.

```sql
SELECT
absCode,
message,
valid
FROM azure.bot_service.bots
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

Creates a Bot Service. Bot Service is a resource group wide resource type.

```sql
INSERT INTO azure.bot_service.bots (
location,
tags,
sku,
kind,
etag,
properties,
resource_group_name,
resource_name,
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
- name: bots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bots resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the bots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bots resource.
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
        The set of properties specific to bot resource.
      value:
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        iconUrl: "{{ iconUrl }}"
        endpoint: "{{ endpoint }}"
        endpointVersion: "{{ endpointVersion }}"
        allSettings: "{{ allSettings }}"
        parameters: "{{ parameters }}"
        manifestUrl: "{{ manifestUrl }}"
        msaAppType: "{{ msaAppType }}"
        msaAppId: "{{ msaAppId }}"
        msaAppTenantId: "{{ msaAppTenantId }}"
        msaAppMSIResourceId: "{{ msaAppMSIResourceId }}"
        configuredChannels:
          - "{{ configuredChannels }}"
        enabledChannels:
          - "{{ enabledChannels }}"
        developerAppInsightKey: "{{ developerAppInsightKey }}"
        developerAppInsightsApiKey: "{{ developerAppInsightsApiKey }}"
        developerAppInsightsApplicationId: "{{ developerAppInsightsApplicationId }}"
        luisAppIds:
          - "{{ luisAppIds }}"
        luisKey: "{{ luisKey }}"
        isCmekEnabled: {{ isCmekEnabled }}
        cmekKeyVaultUrl: "{{ cmekKeyVaultUrl }}"
        cmekEncryptionStatus: "{{ cmekEncryptionStatus }}"
        tenantId: "{{ tenantId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        isStreamingSupported: {{ isStreamingSupported }}
        isDeveloperAppInsightsApiKeySet: {{ isDeveloperAppInsightsApiKeySet }}
        migrationToken: "{{ migrationToken }}"
        disableLocalAuth: {{ disableLocalAuth }}
        schemaTransformationVersion: "{{ schemaTransformationVersion }}"
        storageResourceId: "{{ storageResourceId }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
              groupIds:
                - "{{ groupIds }}"
        openWithHint: "{{ openWithHint }}"
        appPasswordHint: "{{ appPasswordHint }}"
        provisioningState: "{{ provisioningState }}"
        publishingCredentials: "{{ publishingCredentials }}"
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

Updates a Bot Service.

```sql
UPDATE azure.bot_service.bots
SET 
name = '{{ name }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
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

Deletes a Bot Service from the resource group.

```sql
DELETE FROM azure.bot_service.bots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
