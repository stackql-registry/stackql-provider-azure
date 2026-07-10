--- 
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - sql
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="servers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.servers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the server. Once created it cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for server creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during server creation and for server updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Create mode for server, only valid values for this are Normal and Restore. Known values are: "Normal" and "Restore". (Normal, Restore)</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>The Client id used for cross tenant CMK scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="isIPv6Enabled" /></td>
    <td><code>string</code></td>
    <td>Whether or not to enable IPv6 support for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of sql server. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', 1.0', '1.1', '1.2', '1.3'. Known values are: "None", "1.0", "1.1", "1.2", and "1.3". (None, 1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a server.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' or 'SecuredByPerimeter'. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not to restrict outbound network access for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Number of days this server will stay soft-deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the server.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceFeature" /></td>
    <td><code>string</code></td>
    <td>Whether or not existing server has a workspace created and if it allows connection from workspace. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name whose availability was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="available" /></td>
    <td><code>boolean</code></td>
    <td>True if the name is available, otherwise false.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>A message explaining why the name is unavailable. Will be undefined if the name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason code explaining why the name is unavailable. Will be undefined if the name is available. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the server. Once created it cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for server creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during server creation and for server updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Create mode for server, only valid values for this are Normal and Restore. Known values are: "Normal" and "Restore". (Normal, Restore)</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>The Client id used for cross tenant CMK scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="isIPv6Enabled" /></td>
    <td><code>string</code></td>
    <td>Whether or not to enable IPv6 support for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of sql server. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', 1.0', '1.1', '1.2', '1.3'. Known values are: "None", "1.0", "1.1", "1.2", and "1.3". (None, 1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a server.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' or 'SecuredByPerimeter'. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not to restrict outbound network access for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Number of days this server will stay soft-deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the server.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceFeature" /></td>
    <td><code>string</code></td>
    <td>Whether or not existing server has a workspace created and if it allows connection from workspace. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>Administrator username for the server. Once created it cannot be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password (required for server creation).</td>
</tr>
<tr>
    <td><CopyableCode code="administrators" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory administrator can be utilized during server creation and for server updates, except for the azureADOnlyAuthentication property. To update the azureADOnlyAuthentication property, individual API must be used.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Create mode for server, only valid values for this are Normal and Restore. Known values are: "Normal" and "Restore". (Normal, Restore)</td>
</tr>
<tr>
    <td><CopyableCode code="externalGovernanceStatus" /></td>
    <td><code>string</code></td>
    <td>Status of external governance. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="federatedClientId" /></td>
    <td><code>string</code></td>
    <td>The Client id used for cross tenant CMK scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="isIPv6Enabled" /></td>
    <td><code>string</code></td>
    <td>Whether or not to enable IPv6 support for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="keyId" /></td>
    <td><code>string</code></td>
    <td>A CMK URI of the key to use for encryption.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of sql server. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimalTlsVersion" /></td>
    <td><code>string</code></td>
    <td>Minimal TLS version. Allowed values: 'None', 1.0', '1.1', '1.2', '1.3'. Known values are: "None", "1.0", "1.1", "1.2", and "1.3". (None, 1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="primaryUserAssignedIdentityId" /></td>
    <td><code>string</code></td>
    <td>The resource id of a user assigned identity to be used by default.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections on a server.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' or 'SecuredByPerimeter'. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="restrictOutboundNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not to restrict outbound network access for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Number of days this server will stay soft-deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the server.</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="workspaceFeature" /></td>
    <td><code>string</code></td>
    <td>Whether or not existing server has a workspace created and if it allows connection from workspace. Known values are: "Connected" and "Disconnected". (Connected, Disconnected)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a server.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Determines whether a resource can be created with the specified name.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a list of servers in a resource groups.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a list of all servers in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a server.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a server.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a server.</td>
</tr>
<tr>
    <td><a href="#import_database"><CopyableCode code="import_database" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-storageKeyType"><code>storageKeyType</code></a>, <a href="#parameter-storageKey"><code>storageKey</code></a>, <a href="#parameter-storageUri"><code>storageUri</code></a>, <a href="#parameter-administratorLogin"><code>administratorLogin</code></a></td>
    <td></td>
    <td>Imports a bacpac into a new database.</td>
</tr>
<tr>
    <td><a href="#refresh_status"><CopyableCode code="refresh_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh external governance enablement status.</td>
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
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The child resources to include in the response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a server.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
createMode,
externalGovernanceStatus,
federatedClientId,
fullyQualifiedDomainName,
identity,
isIPv6Enabled,
keyId,
kind,
location,
minimalTlsVersion,
primaryUserAssignedIdentityId,
privateEndpointConnections,
publicNetworkAccess,
restrictOutboundNetworkAccess,
retentionDays,
state,
systemData,
tags,
type,
version,
workspaceFeature
FROM azure.sql.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="check_name_availability">

Determines whether a resource can be created with the specified name.

```sql
SELECT
name,
available,
message,
reason
FROM azure.sql.servers
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of servers in a resource groups.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
createMode,
externalGovernanceStatus,
federatedClientId,
fullyQualifiedDomainName,
identity,
isIPv6Enabled,
keyId,
kind,
location,
minimalTlsVersion,
primaryUserAssignedIdentityId,
privateEndpointConnections,
publicNetworkAccess,
restrictOutboundNetworkAccess,
retentionDays,
state,
systemData,
tags,
type,
version,
workspaceFeature
FROM azure.sql.servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of all servers in the subscription.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
administrators,
createMode,
externalGovernanceStatus,
federatedClientId,
fullyQualifiedDomainName,
identity,
isIPv6Enabled,
keyId,
kind,
location,
minimalTlsVersion,
primaryUserAssignedIdentityId,
privateEndpointConnections,
publicNetworkAccess,
restrictOutboundNetworkAccess,
retentionDays,
state,
systemData,
tags,
type,
version,
workspaceFeature
FROM azure.sql.servers
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

Creates or updates a server.

```sql
INSERT INTO azure.sql.servers (
tags,
location,
properties,
identity,
resource_group_name,
server_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
kind,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: servers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the servers resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the servers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the servers resource.
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
        Resource properties.
      value:
        administratorLogin: "{{ administratorLogin }}"
        administratorLoginPassword: "{{ administratorLoginPassword }}"
        version: "{{ version }}"
        state: "{{ state }}"
        fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              groupIds:
                - "{{ groupIds }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        minimalTlsVersion: "{{ minimalTlsVersion }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        workspaceFeature: "{{ workspaceFeature }}"
        primaryUserAssignedIdentityId: "{{ primaryUserAssignedIdentityId }}"
        federatedClientId: "{{ federatedClientId }}"
        keyId: "{{ keyId }}"
        administrators:
          administratorType: "{{ administratorType }}"
          principalType: "{{ principalType }}"
          login: "{{ login }}"
          sid: "{{ sid }}"
          tenantId: "{{ tenantId }}"
          azureADOnlyAuthentication: {{ azureADOnlyAuthentication }}
        restrictOutboundNetworkAccess: "{{ restrictOutboundNetworkAccess }}"
        isIPv6Enabled: "{{ isIPv6Enabled }}"
        externalGovernanceStatus: "{{ externalGovernanceStatus }}"
        retentionDays: {{ retentionDays }}
        createMode: "{{ createMode }}"
    - name: identity
      description: |
        The Azure Active Directory identity of the server.
      value:
        userAssignedIdentities: "{{ userAssignedIdentities }}"
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
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

Updates a server.

```sql
UPDATE azure.sql.servers
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
kind,
location,
properties,
systemData,
tags,
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

Creates or updates a server.

```sql
REPLACE azure.sql.servers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
kind,
location,
properties,
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

Deletes a server.

```sql
DELETE FROM azure.sql.servers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="import_database"
    values={[
        { label: 'import_database', value: 'import_database' },
        { label: 'refresh_status', value: 'refresh_status' }
    ]}
>
<TabItem value="import_database">

Imports a bacpac into a new database.

```sql
EXEC azure.sql.servers.import_database 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"databaseName": "{{ databaseName }}", 
"edition": "{{ edition }}", 
"serviceObjectiveName": "{{ serviceObjectiveName }}", 
"maxSizeBytes": "{{ maxSizeBytes }}", 
"storageKeyType": "{{ storageKeyType }}", 
"storageKey": "{{ storageKey }}", 
"storageUri": "{{ storageUri }}", 
"administratorLogin": "{{ administratorLogin }}", 
"administratorLoginPassword": "{{ administratorLoginPassword }}", 
"authenticationType": "{{ authenticationType }}", 
"networkIsolation": "{{ networkIsolation }}"
}'
;
```
</TabItem>
<TabItem value="refresh_status">

Refresh external governance enablement status.

```sql
EXEC azure.sql.servers.refresh_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
