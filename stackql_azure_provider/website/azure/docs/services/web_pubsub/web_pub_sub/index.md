--- 
title: web_pub_sub
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub
  - web_pubsub
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

Creates, updates, deletes, gets or lists a <code>web_pub_sub</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="web_pub_sub" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_replica_skus"
    values={[
        { label: 'list_replica_skus', value: 'list_replica_skus' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_replica_skus">

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
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>Describes scaling information of a sku.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The resource type that this object applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The billing information of the resource.</td>
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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The message of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the name is available or not.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason of the availability. Required if name is not available.</td>
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
    <td><CopyableCode code="disableAadAuth" /></td>
    <td><code>boolean</code></td>
    <td>DisableLocalAuth Enable or disable aad auth When set as true, connection with AuthType=aad won't work.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>DisableLocalAuth Enable or disable local auth with AccessKey When set as true, connection with AccessKey=xxx won't work.</td>
</tr>
<tr>
    <td><CopyableCode code="externalIP" /></td>
    <td><code>string</code></td>
    <td>The publicly accessible IP of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>FQDN of the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>A class represent managed identities used for request and response.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the service. Known values are: "WebPubSub" and "SocketIO".</td>
</tr>
<tr>
    <td><CopyableCode code="liveTraceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Live trace configuration of a Microsoft.SignalRService resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkACLs" /></td>
    <td><code>object</code></td>
    <td>Network ACLs for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enable or disable public network access. Default to "Enabled". When it's Enabled, network ACLs still apply. When it's Disabled, public network access is always disabled no matter what you set in network ACLs.</td>
</tr>
<tr>
    <td><CopyableCode code="publicPort" /></td>
    <td><code>integer</code></td>
    <td>The publicly accessible port of the resource which is designed for browser/client side usage.</td>
</tr>
<tr>
    <td><CopyableCode code="regionEndpointEnabled" /></td>
    <td><code>string</code></td>
    <td>Enable or disable the regional endpoint. Default to "Enabled". When it's Disabled, new connections will not be routed to this endpoint, however existing connections will not be affected. This property is replica specific. Disable the regional endpoint without replica is not allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLogConfiguration" /></td>
    <td><code>object</code></td>
    <td>Resource log configuration of a Microsoft.SignalRService resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceStopped" /></td>
    <td><code>string</code></td>
    <td>Stop or start the resource. Default to "False". When it's true, the data plane of the resource is shutdown. When it's false, the data plane of the resource is started.</td>
</tr>
<tr>
    <td><CopyableCode code="serverPort" /></td>
    <td><code>integer</code></td>
    <td>The publicly accessible port of the resource which is designed for customer server side usage.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The billing information of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="socketIO" /></td>
    <td><code>object</code></td>
    <td>SocketIO settings for the resource.</td>
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
    <td><CopyableCode code="tls" /></td>
    <td><code>object</code></td>
    <td>TLS settings for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the resource. Probably you need the same or higher version of client SDKs.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="disableAadAuth" /></td>
    <td><code>boolean</code></td>
    <td>DisableLocalAuth Enable or disable aad auth When set as true, connection with AuthType=aad won't work.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>DisableLocalAuth Enable or disable local auth with AccessKey When set as true, connection with AccessKey=xxx won't work.</td>
</tr>
<tr>
    <td><CopyableCode code="externalIP" /></td>
    <td><code>string</code></td>
    <td>The publicly accessible IP of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>FQDN of the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>A class represent managed identities used for request and response.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the service. Known values are: "WebPubSub" and "SocketIO".</td>
</tr>
<tr>
    <td><CopyableCode code="liveTraceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Live trace configuration of a Microsoft.SignalRService resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkACLs" /></td>
    <td><code>object</code></td>
    <td>Network ACLs for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enable or disable public network access. Default to "Enabled". When it's Enabled, network ACLs still apply. When it's Disabled, public network access is always disabled no matter what you set in network ACLs.</td>
</tr>
<tr>
    <td><CopyableCode code="publicPort" /></td>
    <td><code>integer</code></td>
    <td>The publicly accessible port of the resource which is designed for browser/client side usage.</td>
</tr>
<tr>
    <td><CopyableCode code="regionEndpointEnabled" /></td>
    <td><code>string</code></td>
    <td>Enable or disable the regional endpoint. Default to "Enabled". When it's Disabled, new connections will not be routed to this endpoint, however existing connections will not be affected. This property is replica specific. Disable the regional endpoint without replica is not allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLogConfiguration" /></td>
    <td><code>object</code></td>
    <td>Resource log configuration of a Microsoft.SignalRService resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceStopped" /></td>
    <td><code>string</code></td>
    <td>Stop or start the resource. Default to "False". When it's true, the data plane of the resource is shutdown. When it's false, the data plane of the resource is started.</td>
</tr>
<tr>
    <td><CopyableCode code="serverPort" /></td>
    <td><code>integer</code></td>
    <td>The publicly accessible port of the resource which is designed for customer server side usage.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The billing information of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="socketIO" /></td>
    <td><code>object</code></td>
    <td>SocketIO settings for the resource.</td>
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
    <td><CopyableCode code="tls" /></td>
    <td><code>object</code></td>
    <td>TLS settings for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the resource. Probably you need the same or higher version of client SDKs.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="disableAadAuth" /></td>
    <td><code>boolean</code></td>
    <td>DisableLocalAuth Enable or disable aad auth When set as true, connection with AuthType=aad won't work.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAuth" /></td>
    <td><code>boolean</code></td>
    <td>DisableLocalAuth Enable or disable local auth with AccessKey When set as true, connection with AccessKey=xxx won't work.</td>
</tr>
<tr>
    <td><CopyableCode code="externalIP" /></td>
    <td><code>string</code></td>
    <td>The publicly accessible IP of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>FQDN of the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>A class represent managed identities used for request and response.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the service. Known values are: "WebPubSub" and "SocketIO".</td>
</tr>
<tr>
    <td><CopyableCode code="liveTraceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Live trace configuration of a Microsoft.SignalRService resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkACLs" /></td>
    <td><code>object</code></td>
    <td>Network ACLs for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Enable or disable public network access. Default to "Enabled". When it's Enabled, network ACLs still apply. When it's Disabled, public network access is always disabled no matter what you set in network ACLs.</td>
</tr>
<tr>
    <td><CopyableCode code="publicPort" /></td>
    <td><code>integer</code></td>
    <td>The publicly accessible port of the resource which is designed for browser/client side usage.</td>
</tr>
<tr>
    <td><CopyableCode code="regionEndpointEnabled" /></td>
    <td><code>string</code></td>
    <td>Enable or disable the regional endpoint. Default to "Enabled". When it's Disabled, new connections will not be routed to this endpoint, however existing connections will not be affected. This property is replica specific. Disable the regional endpoint without replica is not allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLogConfiguration" /></td>
    <td><code>object</code></td>
    <td>Resource log configuration of a Microsoft.SignalRService resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceStopped" /></td>
    <td><code>string</code></td>
    <td>Stop or start the resource. Default to "False". When it's true, the data plane of the resource is shutdown. When it's false, the data plane of the resource is started.</td>
</tr>
<tr>
    <td><CopyableCode code="serverPort" /></td>
    <td><code>integer</code></td>
    <td>The publicly accessible port of the resource which is designed for customer server side usage.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResources" /></td>
    <td><code>array</code></td>
    <td>The list of shared private link resources.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The billing information of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="socketIO" /></td>
    <td><code>object</code></td>
    <td>SocketIO settings for the resource.</td>
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
    <td><CopyableCode code="tls" /></td>
    <td><code>object</code></td>
    <td>TLS settings for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the resource. Probably you need the same or higher version of client SDKs.</td>
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
    <td><a href="#list_replica_skus"><CopyableCode code="list_replica_skus" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-replica_name"><code>replica_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all available skus of the replica resource.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks that the resource name is valid and is not already in use.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the resource and its properties.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Operation to update an exiting resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to delete a resource.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the access keys of the resource.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all available skus of the resource.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to restart a resource.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>the region. Required.</td>
</tr>
<tr id="parameter-replica_name">
    <td><CopyableCode code="replica_name" /></td>
    <td><code>string</code></td>
    <td>The name of the replica. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
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
    defaultValue="list_replica_skus"
    values={[
        { label: 'list_replica_skus', value: 'list_replica_skus' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_replica_skus">

List all available skus of the replica resource.

```sql
SELECT
capacity,
resourceType,
sku
FROM azure.web_pubsub.web_pub_sub
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND replica_name = '{{ replica_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Checks that the resource name is valid and is not already in use.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.web_pubsub.web_pub_sub
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the resource and its properties.

```sql
SELECT
id,
name,
disableAadAuth,
disableLocalAuth,
externalIP,
hostName,
hostNamePrefix,
identity,
kind,
liveTraceConfiguration,
location,
networkACLs,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
publicPort,
regionEndpointEnabled,
resourceLogConfiguration,
resourceStopped,
serverPort,
sharedPrivateLinkResources,
sku,
socketIO,
systemData,
tags,
tls,
type,
version
FROM azure.web_pubsub.web_pub_sub
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Handles requests to list all resources in a resource group.

```sql
SELECT
id,
name,
disableAadAuth,
disableLocalAuth,
externalIP,
hostName,
hostNamePrefix,
identity,
kind,
liveTraceConfiguration,
location,
networkACLs,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
publicPort,
regionEndpointEnabled,
resourceLogConfiguration,
resourceStopped,
serverPort,
sharedPrivateLinkResources,
sku,
socketIO,
systemData,
tags,
tls,
type,
version
FROM azure.web_pubsub.web_pub_sub
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Handles requests to list all resources in a subscription.

```sql
SELECT
id,
name,
disableAadAuth,
disableLocalAuth,
externalIP,
hostName,
hostNamePrefix,
identity,
kind,
liveTraceConfiguration,
location,
networkACLs,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
publicPort,
regionEndpointEnabled,
resourceLogConfiguration,
resourceStopped,
serverPort,
sharedPrivateLinkResources,
sku,
socketIO,
systemData,
tags,
tls,
type,
version
FROM azure.web_pubsub.web_pub_sub
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or update a resource.

```sql
INSERT INTO azure.web_pubsub.web_pub_sub (
tags,
location,
sku,
kind,
identity,
properties,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ sku }}',
'{{ kind }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
kind,
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
- name: web_pub_sub
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the web_pub_sub resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the web_pub_sub resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the web_pub_sub resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: sku
      description: |
        The billing information of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the service. Known values are: "WebPubSub" and "SocketIO".
    - name: identity
      description: |
        A class represent managed identities used for request and response.
      value:
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
    - name: properties
      value:
        tls:
          clientCertEnabled: {{ clientCertEnabled }}
        liveTraceConfiguration:
          enabled: "{{ enabled }}"
          categories:
            - name: "{{ name }}"
              enabled: "{{ enabled }}"
        resourceLogConfiguration:
          categories:
            - name: "{{ name }}"
              enabled: "{{ enabled }}"
        networkACLs:
          defaultAction: "{{ defaultAction }}"
          publicNetwork:
            allow:
              - "{{ allow }}"
            deny:
              - "{{ deny }}"
          privateEndpoints:
            - allow: "{{ allow }}"
              deny: "{{ deny }}"
              name: "{{ name }}"
          ipRules:
            - value: "{{ value }}"
              action: "{{ action }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        disableLocalAuth: {{ disableLocalAuth }}
        disableAadAuth: {{ disableAadAuth }}
        regionEndpointEnabled: "{{ regionEndpointEnabled }}"
        resourceStopped: "{{ resourceStopped }}"
        socketIO:
          serviceMode: "{{ serviceMode }}"
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

Operation to update an exiting resource.

```sql
UPDATE azure.web_pubsub.web_pub_sub
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
kind,
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
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update a resource.

```sql
REPLACE azure.web_pubsub.web_pub_sub
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
kind,
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

Operation to delete a resource.

```sql
DELETE FROM azure.web_pubsub.web_pub_sub
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'list_skus', value: 'list_skus' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'restart', value: 'restart' }
    ]}
>
<TabItem value="list_keys">

Get the access keys of the resource.

```sql
EXEC azure.web_pubsub.web_pub_sub.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_skus">

List all available skus of the resource.

```sql
EXEC azure.web_pubsub.web_pub_sub.list_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time.

```sql
EXEC azure.web_pubsub.web_pub_sub.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Operation to restart a resource.

```sql
EXEC azure.web_pubsub.web_pub_sub.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
