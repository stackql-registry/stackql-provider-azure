--- 
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - notificationhubs
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notificationhubs.namespaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_authorization_rule"
    values={[
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_authorization_rule">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="claimType" /></td>
    <td><code>string</code></td>
    <td>Gets a string that describes the claim type.</td>
</tr>
<tr>
    <td><CopyableCode code="claimValue" /></td>
    <td><code>string</code></td>
    <td>Gets a string that describes the claim value.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the created time for this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="keyName" /></td>
    <td><code>string</code></td>
    <td>Gets a string that describes the authorization rule.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Deprecated - only for compatibility.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the last modified time for this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryKey" /></td>
    <td><code>string</code></td>
    <td>Gets a base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>Gets the revision number for the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="rights" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the rights associated with the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryKey" /></td>
    <td><code>string</code></td>
    <td>Gets a base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Deprecated - only for compatibility.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the namespace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="critical" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets whether or not the namespace is set as Critical.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCenter" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets whether or not the namespace is currently enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricId" /></td>
    <td><code>string</code></td>
    <td>Azure Insights Metrics id.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaceType" /></td>
    <td><code>string</code></td>
    <td>Defines values for NamespaceType. Known values are: "Messaging" and "NotificationHub".</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of network authorization rules.</td>
</tr>
<tr>
    <td><CopyableCode code="pnsCredentials" /></td>
    <td><code>object</code></td>
    <td>Collection of Notification Hub or Notification Hub Namespace PNS credentials.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private Endpoint Connections for namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines values for OperationProvisioningState. Known values are: "Unknown", "InProgress", "Succeeded", "Failed", "Canceled", "Pending", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Type of public network access. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Region. The value is always set to the same value as Namespace.Location, so we are deprecating this property.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRegion" /></td>
    <td><code>string</code></td>
    <td>Allowed replication region. Known values are: "Default", "WestUs2", "NorthEurope", "AustraliaEast", "BrazilSouth", "SouthEastAsia", "SouthAfricaNorth", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnit" /></td>
    <td><code>string</code></td>
    <td>Gets or sets scaleUnit where the namespace gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusEndpoint" /></td>
    <td><code>string</code></td>
    <td>Gets or sets endpoint you can use to perform NotificationHub operations.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku description for a namespace. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Namespace status. Known values are: "Created", "Creating", "Suspended", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Namespace subscription id.</td>
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
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the namespace was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundancy" /></td>
    <td><code>string</code></td>
    <td>Namespace SKU name. Known values are: "Disabled" and "Enabled".</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the namespace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="critical" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets whether or not the namespace is set as Critical.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCenter" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets whether or not the namespace is currently enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricId" /></td>
    <td><code>string</code></td>
    <td>Azure Insights Metrics id.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaceType" /></td>
    <td><code>string</code></td>
    <td>Defines values for NamespaceType. Known values are: "Messaging" and "NotificationHub".</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of network authorization rules.</td>
</tr>
<tr>
    <td><CopyableCode code="pnsCredentials" /></td>
    <td><code>object</code></td>
    <td>Collection of Notification Hub or Notification Hub Namespace PNS credentials.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private Endpoint Connections for namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines values for OperationProvisioningState. Known values are: "Unknown", "InProgress", "Succeeded", "Failed", "Canceled", "Pending", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Type of public network access. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Region. The value is always set to the same value as Namespace.Location, so we are deprecating this property.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRegion" /></td>
    <td><code>string</code></td>
    <td>Allowed replication region. Known values are: "Default", "WestUs2", "NorthEurope", "AustraliaEast", "BrazilSouth", "SouthEastAsia", "SouthAfricaNorth", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnit" /></td>
    <td><code>string</code></td>
    <td>Gets or sets scaleUnit where the namespace gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusEndpoint" /></td>
    <td><code>string</code></td>
    <td>Gets or sets endpoint you can use to perform NotificationHub operations.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku description for a namespace. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Namespace status. Known values are: "Created", "Creating", "Suspended", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Namespace subscription id.</td>
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
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the namespace was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundancy" /></td>
    <td><code>string</code></td>
    <td>Namespace SKU name. Known values are: "Disabled" and "Enabled".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the namespace was created.</td>
</tr>
<tr>
    <td><CopyableCode code="critical" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets whether or not the namespace is set as Critical.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCenter" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets whether or not the namespace is currently enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metricId" /></td>
    <td><code>string</code></td>
    <td>Azure Insights Metrics id.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaceType" /></td>
    <td><code>string</code></td>
    <td>Defines values for NamespaceType. Known values are: "Messaging" and "NotificationHub".</td>
</tr>
<tr>
    <td><CopyableCode code="networkAcls" /></td>
    <td><code>object</code></td>
    <td>A collection of network authorization rules.</td>
</tr>
<tr>
    <td><CopyableCode code="pnsCredentials" /></td>
    <td><code>object</code></td>
    <td>Collection of Notification Hub or Notification Hub Namespace PNS credentials.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private Endpoint Connections for namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines values for OperationProvisioningState. Known values are: "Unknown", "InProgress", "Succeeded", "Failed", "Canceled", "Pending", and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Type of public network access. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Region. The value is always set to the same value as Namespace.Location, so we are deprecating this property.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRegion" /></td>
    <td><code>string</code></td>
    <td>Allowed replication region. Known values are: "Default", "WestUs2", "NorthEurope", "AustraliaEast", "BrazilSouth", "SouthEastAsia", "SouthAfricaNorth", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="scaleUnit" /></td>
    <td><code>string</code></td>
    <td>Gets or sets scaleUnit where the namespace gets created.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusEndpoint" /></td>
    <td><code>string</code></td>
    <td>Gets or sets endpoint you can use to perform NotificationHub operations.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku description for a namespace. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Namespace status. Known values are: "Created", "Creating", "Suspended", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Namespace subscription id.</td>
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
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the namespace was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundancy" /></td>
    <td><code>string</code></td>
    <td>Namespace SKU name. Known values are: "Disabled" and "Enabled".</td>
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
    <td><a href="#get_authorization_rule"><CopyableCode code="get_authorization_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an authorization rule for a namespace by name. Gets an authorization rule for a namespace by name.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the given namespace. Returns the given namespace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the available namespaces within a resource group. Lists the available namespaces within a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists all the available namespaces within the subscription. Lists all the available namespaces within the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates / Updates a Notification Hub namespace. This operation is idempotent. Creates / Updates a Notification Hub namespace. This operation is idempotent.</td>
</tr>
<tr>
    <td><a href="#create_or_update_authorization_rule"><CopyableCode code="create_or_update_authorization_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an authorization rule for a namespace. Creates an authorization rule for a namespace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patches the existing namespace. Patches the existing namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates / Updates a Notification Hub namespace. This operation is idempotent. Creates / Updates a Notification Hub namespace. This operation is idempotent.</td>
</tr>
<tr>
    <td><a href="#create_or_update_authorization_rule"><CopyableCode code="create_or_update_authorization_rule" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an authorization rule for a namespace. Creates an authorization rule for a namespace.</td>
</tr>
<tr>
    <td><a href="#delete_authorization_rule"><CopyableCode code="delete_authorization_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a namespace authorization rule. Deletes a namespace authorization rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace. Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace.</td>
</tr>
<tr>
    <td><a href="#list_authorization_rules"><CopyableCode code="list_authorization_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the authorization rules for a namespace. Gets the authorization rules for a namespace.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Primary and Secondary ConnectionStrings to the namespace. Gets the Primary and Secondary ConnectionStrings to the namespace.</td>
</tr>
<tr>
    <td><a href="#get_pns_credentials"><CopyableCode code="get_pns_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the PNS credentials associated with a namespace. Lists the PNS credentials associated with a namespace.</td>
</tr>
<tr>
    <td><a href="#check_availability"><CopyableCode code="check_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name. Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name.</td>
</tr>
<tr>
    <td><a href="#regenerate_keys"><CopyableCode code="regenerate_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-policyKey"><code>policyKey</code></a></td>
    <td></td>
    <td>Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule. Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule.</td>
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
<tr id="parameter-authorization_rule_name">
    <td><CopyableCode code="authorization_rule_name" /></td>
    <td><code>string</code></td>
    <td>Authorization Rule Name. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Namespace name. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for subsequent requests. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results to return. Default value is 100.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_authorization_rule"
    values={[
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_authorization_rule">

Gets an authorization rule for a namespace by name. Gets an authorization rule for a namespace by name.

```sql
SELECT
id,
name,
claimType,
claimValue,
createdTime,
keyName,
location,
modifiedTime,
primaryKey,
revision,
rights,
secondaryKey,
systemData,
tags,
type
FROM azure.notificationhubs.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND authorization_rule_name = '{{ authorization_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Returns the given namespace. Returns the given namespace.

```sql
SELECT
id,
name,
createdAt,
critical,
dataCenter,
enabled,
location,
metricId,
namespaceType,
networkAcls,
pnsCredentials,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
region,
replicationRegion,
scaleUnit,
serviceBusEndpoint,
sku,
status,
subscriptionId,
systemData,
tags,
type,
updatedAt,
zoneRedundancy
FROM azure.notificationhubs.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the available namespaces within a resource group. Lists the available namespaces within a resource group.

```sql
SELECT
id,
name,
createdAt,
critical,
dataCenter,
enabled,
location,
metricId,
namespaceType,
networkAcls,
pnsCredentials,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
region,
replicationRegion,
scaleUnit,
serviceBusEndpoint,
sku,
status,
subscriptionId,
systemData,
tags,
type,
updatedAt,
zoneRedundancy
FROM azure.notificationhubs.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_all">

Lists all the available namespaces within the subscription. Lists all the available namespaces within the subscription.

```sql
SELECT
id,
name,
createdAt,
critical,
dataCenter,
enabled,
location,
metricId,
namespaceType,
networkAcls,
pnsCredentials,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
region,
replicationRegion,
scaleUnit,
serviceBusEndpoint,
sku,
status,
subscriptionId,
systemData,
tags,
type,
updatedAt,
zoneRedundancy
FROM azure.notificationhubs.namespaces
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_authorization_rule', value: 'create_or_update_authorization_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates / Updates a Notification Hub namespace. This operation is idempotent. Creates / Updates a Notification Hub namespace. This operation is idempotent.

```sql
INSERT INTO azure.notificationhubs.namespaces (
tags,
location,
sku,
properties,
resource_group_name,
namespace_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_authorization_rule">

Creates an authorization rule for a namespace. Creates an authorization rule for a namespace.

```sql
INSERT INTO azure.notificationhubs.namespaces (
location,
tags,
properties,
resource_group_name,
namespace_name,
authorization_rule_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ authorization_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: namespaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the namespaces resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the namespaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the namespaces resource.
    - name: authorization_rule_name
      value: "{{ authorization_rule_name }}"
      description: Required parameter for the namespaces resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Deprecated - only for compatibility.
    - name: location
      value: "{{ location }}"
      description: |
        Deprecated - only for compatibility.
    - name: sku
      description: |
        The Sku description for a namespace. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        rights:
          - "{{ rights }}"
        primaryKey: "{{ primaryKey }}"
        secondaryKey: "{{ secondaryKey }}"
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

Patches the existing namespace. Patches the existing namespace.

```sql
UPDATE azure.notificationhubs.namespaces
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_authorization_rule', value: 'create_or_update_authorization_rule' }
    ]}
>
<TabItem value="create_or_update">

Creates / Updates a Notification Hub namespace. This operation is idempotent. Creates / Updates a Notification Hub namespace. This operation is idempotent.

```sql
REPLACE azure.notificationhubs.namespaces
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_authorization_rule">

Creates an authorization rule for a namespace. Creates an authorization rule for a namespace.

```sql
REPLACE azure.notificationhubs.namespaces
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND authorization_rule_name = '{{ authorization_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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
    defaultValue="delete_authorization_rule"
    values={[
        { label: 'delete_authorization_rule', value: 'delete_authorization_rule' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_authorization_rule">

Deletes a namespace authorization rule. Deletes a namespace authorization rule.

```sql
DELETE FROM azure.notificationhubs.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND authorization_rule_name = '{{ authorization_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace. Deletes an existing namespace. This operation also removes all associated notificationHubs under the namespace.

```sql
DELETE FROM azure.notificationhubs.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_authorization_rules"
    values={[
        { label: 'list_authorization_rules', value: 'list_authorization_rules' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get_pns_credentials', value: 'get_pns_credentials' },
        { label: 'check_availability', value: 'check_availability' },
        { label: 'regenerate_keys', value: 'regenerate_keys' }
    ]}
>
<TabItem value="list_authorization_rules">

Gets the authorization rules for a namespace. Gets the authorization rules for a namespace.

```sql
EXEC azure.notificationhubs.namespaces.list_authorization_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_keys">

Gets the Primary and Secondary ConnectionStrings to the namespace. Gets the Primary and Secondary ConnectionStrings to the namespace.

```sql
EXEC azure.notificationhubs.namespaces.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_pns_credentials">

Lists the PNS credentials associated with a namespace. Lists the PNS credentials associated with a namespace.

```sql
EXEC azure.notificationhubs.namespaces.get_pns_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_availability">

Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name. Checks the availability of the given service namespace across all Azure subscriptions. This is useful because the domain name is created based on the service namespace name.

```sql
EXEC azure.notificationhubs.namespaces.check_availability 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"location": "{{ location }}", 
"tags": "{{ tags }}", 
"isAvailiable": {{ isAvailiable }}, 
"sku": "{{ sku }}"
}'
;
```
</TabItem>
<TabItem value="regenerate_keys">

Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule. Regenerates the Primary/Secondary Keys to the Namespace Authorization Rule.

```sql
EXEC azure.notificationhubs.namespaces.regenerate_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"policyKey": "{{ policyKey }}"
}'
;
```
</TabItem>
</Tabs>
