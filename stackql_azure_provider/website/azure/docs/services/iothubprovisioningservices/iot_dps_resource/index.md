--- 
title: iot_dps_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource
  - iothubprovisioningservices
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

Creates, updates, deletes, gets or lists an <code>iot_dps_resource</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iot_dps_resource" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iothubprovisioningservices.iot_dps_resource" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_result"
    values={[
        { label: 'get_operation_result', value: 'get_operation_result' },
        { label: 'get_private_link_resources', value: 'get_private_link_resources' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'list_private_link_resources', value: 'list_private_link_resources' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_operation_result">

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
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error message containing code, description and details.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>current status of a long running operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_private_link_resources">

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
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredMembers" /></td>
    <td><code>array</code></td>
    <td>The required members for a specific group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredZoneNames" /></td>
    <td><code>array</code></td>
    <td>The required DNS zones for a specific group id.</td>
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
<TabItem value="get_private_endpoint_connection">

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
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>The private endpoint property of a private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>The current state of a private endpoint connection. Required.</td>
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
<TabItem value="list_private_link_resources">

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
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredMembers" /></td>
    <td><code>array</code></td>
    <td>The required members for a specific group id.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredZoneNames" /></td>
    <td><code>array</code></td>
    <td>The required DNS zones for a specific group id.</td>
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
    <td><CopyableCode code="allocationPolicy" /></td>
    <td><code>string</code></td>
    <td>Allocation policy to be used by this provisioning service. Known values are: "Hashed", "GeoLatency", and "Static". (Hashed, GeoLatency, Static)</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>array</code></td>
    <td>List of authorization keys for a provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceProvisioningHostName" /></td>
    <td><code>string</code></td>
    <td>Device endpoint for this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistryNamespace" /></td>
    <td><code>object</code></td>
    <td>The Device Registry namespace that is linked to the provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDataResidency" /></td>
    <td><code>boolean</code></td>
    <td>Optional. Indicates if the DPS instance has Data Residency enabled, removing the cross geo-pair disaster recovery.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="idScope" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubs" /></td>
    <td><code>array</code></td>
    <td>List of IoT hubs associated with this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="ipFilterRules" /></td>
    <td><code>array</code></td>
    <td>The IP filter rules.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="portalOperationsHostName" /></td>
    <td><code>string</code></td>
    <td>Portal endpoint to enable CORS for this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on this IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The ARM provisioning state of the provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourcegroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceOperationsHostName" /></td>
    <td><code>string</code></td>
    <td>Service endpoint for provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku info for a provisioning Service. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the provisioning service. Known values are: "Activating", "Active", "Deleting", "Deleted", "ActivationFailed", "DeletionFailed", "Transitioning", "Suspending", "Suspended", "Resuming", "FailingOver", and "FailoverFailed". (Activating, Active, Deleting, Deleted, ActivationFailed, DeletionFailed, Transitioning, Suspending, Suspended, Resuming, FailingOver, FailoverFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionid" /></td>
    <td><code>string</code></td>
    <td>The subscription id of the resource.</td>
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
    <td><CopyableCode code="allocationPolicy" /></td>
    <td><code>string</code></td>
    <td>Allocation policy to be used by this provisioning service. Known values are: "Hashed", "GeoLatency", and "Static". (Hashed, GeoLatency, Static)</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>array</code></td>
    <td>List of authorization keys for a provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceProvisioningHostName" /></td>
    <td><code>string</code></td>
    <td>Device endpoint for this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistryNamespace" /></td>
    <td><code>object</code></td>
    <td>The Device Registry namespace that is linked to the provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDataResidency" /></td>
    <td><code>boolean</code></td>
    <td>Optional. Indicates if the DPS instance has Data Residency enabled, removing the cross geo-pair disaster recovery.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="idScope" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubs" /></td>
    <td><code>array</code></td>
    <td>List of IoT hubs associated with this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="ipFilterRules" /></td>
    <td><code>array</code></td>
    <td>The IP filter rules.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="portalOperationsHostName" /></td>
    <td><code>string</code></td>
    <td>Portal endpoint to enable CORS for this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on this IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The ARM provisioning state of the provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourcegroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceOperationsHostName" /></td>
    <td><code>string</code></td>
    <td>Service endpoint for provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku info for a provisioning Service. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the provisioning service. Known values are: "Activating", "Active", "Deleting", "Deleted", "ActivationFailed", "DeletionFailed", "Transitioning", "Suspending", "Suspended", "Resuming", "FailingOver", and "FailoverFailed". (Activating, Active, Deleting, Deleted, ActivationFailed, DeletionFailed, Transitioning, Suspending, Suspended, Resuming, FailingOver, FailoverFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionid" /></td>
    <td><code>string</code></td>
    <td>The subscription id of the resource.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allocationPolicy" /></td>
    <td><code>string</code></td>
    <td>Allocation policy to be used by this provisioning service. Known values are: "Hashed", "GeoLatency", and "Static". (Hashed, GeoLatency, Static)</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicies" /></td>
    <td><code>array</code></td>
    <td>List of authorization keys for a provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceProvisioningHostName" /></td>
    <td><code>string</code></td>
    <td>Device endpoint for this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistryNamespace" /></td>
    <td><code>object</code></td>
    <td>The Device Registry namespace that is linked to the provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDataResidency" /></td>
    <td><code>boolean</code></td>
    <td>Optional. Indicates if the DPS instance has Data Residency enabled, removing the cross geo-pair disaster recovery.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="idScope" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="iotHubs" /></td>
    <td><code>array</code></td>
    <td>List of IoT hubs associated with this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="ipFilterRules" /></td>
    <td><code>array</code></td>
    <td>The IP filter rules.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="portalOperationsHostName" /></td>
    <td><code>string</code></td>
    <td>Portal endpoint to enable CORS for this provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections created on this IotHub.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The ARM provisioning state of the provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether requests from Public Network are allowed. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourcegroup" /></td>
    <td><code>string</code></td>
    <td>The resource group of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceOperationsHostName" /></td>
    <td><code>string</code></td>
    <td>Service endpoint for provisioning service.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku info for a provisioning Service. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the provisioning service. Known values are: "Activating", "Active", "Deleting", "Deleted", "ActivationFailed", "DeletionFailed", "Transitioning", "Suspending", "Suspended", "Resuming", "FailingOver", and "FailoverFailed". (Activating, Active, Deleting, Deleted, ActivationFailed, DeletionFailed, Transitioning, Suspending, Suspended, Resuming, FailingOver, FailoverFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionid" /></td>
    <td><code>string</code></td>
    <td>The subscription id of the resource.</td>
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
    <td><a href="#get_operation_result"><CopyableCode code="get_operation_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-asyncinfo"><code>asyncinfo</code></a></td>
    <td></td>
    <td>Gets the status of a long running operation, such as create, update or delete a provisioning service.</td>
</tr>
<tr>
    <td><a href="#get_private_link_resources"><CopyableCode code="get_private_link_resources" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified private link resource for the given provisioning service.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection"><CopyableCode code="get_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get private endpoint connection properties.</td>
</tr>
<tr>
    <td><a href="#list_private_link_resources"><CopyableCode code="list_private_link_resources" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List private link resources for the given provisioning service.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a></td>
    <td></td>
    <td>Get the metadata of the provisioning service without SAS keys.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all provisioning services in the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the provisioning services for a given subscription id.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.</td>
</tr>
<tr>
    <td><a href="#create_or_update_private_endpoint_connection"><CopyableCode code="create_or_update_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the status of a private endpoint connection with the specified name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing provisioning service's tags. to update other fields use the CreateOrUpdate method.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.</td>
</tr>
<tr>
    <td><a href="#create_or_update_private_endpoint_connection"><CopyableCode code="create_or_update_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update the status of a private endpoint connection with the specified name.</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_connection"><CopyableCode code="delete_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete private endpoint connection with the specified name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a></td>
    <td></td>
    <td>Deletes the Provisioning Service.</td>
</tr>
<tr>
    <td><a href="#list_valid_skus"><CopyableCode code="list_valid_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a></td>
    <td></td>
    <td>Gets the list of valid SKUs and tiers for a provisioning service.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a></td>
    <td></td>
    <td>List the primary and secondary keys for a provisioning service.</td>
</tr>
<tr>
    <td><a href="#list_keys_for_key_name"><CopyableCode code="list_keys_for_key_name" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a></td>
    <td></td>
    <td>List primary and secondary keys for a specific key name.</td>
</tr>
<tr>
    <td><a href="#list_private_endpoint_connections"><CopyableCode code="list_private_endpoint_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List private endpoint connection properties.</td>
</tr>
<tr>
    <td><a href="#check_provisioning_service_name_availability"><CopyableCode code="check_provisioning_service_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Check if a provisioning service name is available. Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable.</td>
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
<tr id="parameter-asyncinfo">
    <td><CopyableCode code="asyncinfo" /></td>
    <td><code>string</code></td>
    <td>Async header used to poll on the status of the operation, obtained while creating the long running operation. Required.</td>
</tr>
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The name of the private link resource. Required.</td>
</tr>
<tr id="parameter-key_name">
    <td><CopyableCode code="key_name" /></td>
    <td><code>string</code></td>
    <td>Logical key name to get key-values for. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation id corresponding to long running operation. Use this to poll for the status. Required.</td>
</tr>
<tr id="parameter-private_endpoint_connection_name">
    <td><CopyableCode code="private_endpoint_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the private endpoint connection. Required.</td>
</tr>
<tr id="parameter-provisioning_service_name">
    <td><CopyableCode code="provisioning_service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the provisioning service to retrieve. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Name of the provisioning service to retrieve. Required.</td>
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
    defaultValue="get_operation_result"
    values={[
        { label: 'get_operation_result', value: 'get_operation_result' },
        { label: 'get_private_link_resources', value: 'get_private_link_resources' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'list_private_link_resources', value: 'list_private_link_resources' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_operation_result">

Gets the status of a long running operation, such as create, update or delete a provisioning service.

```sql
SELECT
error,
status
FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE operation_id = '{{ operation_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND provisioning_service_name = '{{ provisioning_service_name }}' -- required
AND asyncinfo = '{{ asyncinfo }}' -- required
;
```
</TabItem>
<TabItem value="get_private_link_resources">

Get the specified private link resource for the given provisioning service.

```sql
SELECT
id,
name,
groupId,
requiredMembers,
requiredZoneNames,
systemData,
type
FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND group_id = '{{ group_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection">

Get private endpoint connection properties.

```sql
SELECT
id,
name,
privateEndpoint,
privateLinkServiceConnectionState,
systemData,
type
FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_private_link_resources">

List private link resources for the given provisioning service.

```sql
SELECT
id,
name,
groupId,
requiredMembers,
requiredZoneNames,
systemData,
type
FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the metadata of the provisioning service without SAS keys.

```sql
SELECT
id,
name,
allocationPolicy,
authorizationPolicies,
deviceProvisioningHostName,
deviceRegistryNamespace,
enableDataResidency,
etag,
idScope,
identity,
iotHubs,
ipFilterRules,
location,
portalOperationsHostName,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
resourcegroup,
serviceOperationsHostName,
sku,
state,
subscriptionid,
systemData,
tags,
type
FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE provisioning_service_name = '{{ provisioning_service_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of all provisioning services in the given resource group.

```sql
SELECT
id,
name,
allocationPolicy,
authorizationPolicies,
deviceProvisioningHostName,
deviceRegistryNamespace,
enableDataResidency,
etag,
idScope,
identity,
iotHubs,
ipFilterRules,
location,
portalOperationsHostName,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
resourcegroup,
serviceOperationsHostName,
sku,
state,
subscriptionid,
systemData,
tags,
type
FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all the provisioning services for a given subscription id.

```sql
SELECT
id,
name,
allocationPolicy,
authorizationPolicies,
deviceProvisioningHostName,
deviceRegistryNamespace,
enableDataResidency,
etag,
idScope,
identity,
iotHubs,
ipFilterRules,
location,
portalOperationsHostName,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
resourcegroup,
serviceOperationsHostName,
sku,
state,
subscriptionid,
systemData,
tags,
type
FROM azure.iothubprovisioningservices.iot_dps_resource
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
        { label: 'create_or_update_private_endpoint_connection', value: 'create_or_update_private_endpoint_connection' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.

```sql
INSERT INTO azure.iothubprovisioningservices.iot_dps_resource (
tags,
location,
etag,
resourcegroup,
subscriptionid,
properties,
sku,
identity,
resource_group_name,
provisioning_service_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ etag }}',
'{{ resourcegroup }}',
'{{ subscriptionid }}',
'{{ properties }}' /* required */,
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ provisioning_service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
resourcegroup,
sku,
subscriptionid,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_private_endpoint_connection">

Create or update the status of a private endpoint connection with the specified name.

```sql
INSERT INTO azure.iothubprovisioningservices.iot_dps_resource (
properties,
resource_group_name,
resource_name,
private_endpoint_connection_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ private_endpoint_connection_name }}',
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
- name: iot_dps_resource
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the iot_dps_resource resource.
    - name: provisioning_service_name
      value: "{{ provisioning_service_name }}"
      description: Required parameter for the iot_dps_resource resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the iot_dps_resource resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the iot_dps_resource resource.
    - name: private_endpoint_connection_name
      value: "{{ private_endpoint_connection_name }}"
      description: Required parameter for the iot_dps_resource resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: etag
      value: "{{ etag }}"
      description: |
        The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
    - name: resourcegroup
      value: "{{ resourcegroup }}"
      description: |
        The resource group of the resource.
    - name: subscriptionid
      value: "{{ subscriptionid }}"
      description: |
        The subscription id of the resource.
    - name: properties
      description: |
        The properties of a private endpoint connection. Required.
      value:
        privateEndpoint:
          id: "{{ id }}"
        privateLinkServiceConnectionState:
          status: "{{ status }}"
          description: "{{ description }}"
          actionsRequired: "{{ actionsRequired }}"
    - name: sku
      description: |
        Sku info for a provisioning Service. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        The managed service identities assigned to this resource.
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

Update an existing provisioning service's tags. to update other fields use the CreateOrUpdate method.

```sql
UPDATE azure.iothubprovisioningservices.iot_dps_resource
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provisioning_service_name = '{{ provisioning_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
resourcegroup,
sku,
subscriptionid,
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
        { label: 'create_or_update_private_endpoint_connection', value: 'create_or_update_private_endpoint_connection' }
    ]}
>
<TabItem value="create_or_update">

Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.

```sql
REPLACE azure.iothubprovisioningservices.iot_dps_resource
SET 
tags = '{{ tags }}',
location = '{{ location }}',
etag = '{{ etag }}',
resourcegroup = '{{ resourcegroup }}',
subscriptionid = '{{ subscriptionid }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provisioning_service_name = '{{ provisioning_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
resourcegroup,
sku,
subscriptionid,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_private_endpoint_connection">

Create or update the status of a private endpoint connection with the specified name.

```sql
REPLACE azure.iothubprovisioningservices.iot_dps_resource
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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
    defaultValue="delete_private_endpoint_connection"
    values={[
        { label: 'delete_private_endpoint_connection', value: 'delete_private_endpoint_connection' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_private_endpoint_connection">

Delete private endpoint connection with the specified name.

```sql
DELETE FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes the Provisioning Service.

```sql
DELETE FROM azure.iothubprovisioningservices.iot_dps_resource
WHERE provisioning_service_name = '{{ provisioning_service_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_valid_skus"
    values={[
        { label: 'list_valid_skus', value: 'list_valid_skus' },
        { label: 'list_keys', value: 'list_keys' },
        { label: 'list_keys_for_key_name', value: 'list_keys_for_key_name' },
        { label: 'list_private_endpoint_connections', value: 'list_private_endpoint_connections' },
        { label: 'check_provisioning_service_name_availability', value: 'check_provisioning_service_name_availability' }
    ]}
>
<TabItem value="list_valid_skus">

Gets the list of valid SKUs and tiers for a provisioning service.

```sql
EXEC azure.iothubprovisioningservices.iot_dps_resource.list_valid_skus 
@provisioning_service_name='{{ provisioning_service_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required
;
```
</TabItem>
<TabItem value="list_keys">

List the primary and secondary keys for a provisioning service.

```sql
EXEC azure.iothubprovisioningservices.iot_dps_resource.list_keys 
@provisioning_service_name='{{ provisioning_service_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required
;
```
</TabItem>
<TabItem value="list_keys_for_key_name">

List primary and secondary keys for a specific key name.

```sql
EXEC azure.iothubprovisioningservices.iot_dps_resource.list_keys_for_key_name 
@provisioning_service_name='{{ provisioning_service_name }}' --required, 
@key_name='{{ key_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required
;
```
</TabItem>
<TabItem value="list_private_endpoint_connections">

List private endpoint connection properties.

```sql
EXEC azure.iothubprovisioningservices.iot_dps_resource.list_private_endpoint_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_provisioning_service_name_availability">

Check if a provisioning service name is available. Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable.

```sql
EXEC azure.iothubprovisioningservices.iot_dps_resource.check_provisioning_service_name_availability 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}"
}'
;
```
</TabItem>
</Tabs>
