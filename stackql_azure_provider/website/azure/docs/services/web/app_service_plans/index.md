--- 
title: app_service_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - app_service_plans
  - web
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

Creates, updates, deletes, gets or lists an <code>app_service_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_service_plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.app_service_plans" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_hybrid_connection"
    values={[
        { label: 'get_hybrid_connection', value: 'get_hybrid_connection' },
        { label: 'get_vnet_gateway', value: 'get_vnet_gateway' },
        { label: 'get_route_for_vnet', value: 'get_route_for_vnet' },
        { label: 'list_routes_for_vnet', value: 'list_routes_for_vnet' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_hybrid_connection">

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
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="relayArmUri" /></td>
    <td><code>string</code></td>
    <td>The ARM URI to the Service Bus relay.</td>
</tr>
<tr>
    <td><CopyableCode code="relayName" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus relay.</td>
</tr>
<tr>
    <td><CopyableCode code="sendKeyName" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus key which has Send permissions. This is used to authenticate to Service Bus.</td>
</tr>
<tr>
    <td><CopyableCode code="sendKeyValue" /></td>
    <td><code>string</code></td>
    <td>The value of the Service Bus key. This is used to authenticate to Service Bus. In ARM this key will not be returned normally, use the POST /listKeys API instead.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusNamespace" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusSuffix" /></td>
    <td><code>string</code></td>
    <td>The suffix for the service bus endpoint. By default this is .servicebus.windows.net.</td>
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
<TabItem value="get_vnet_gateway">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<tr>
    <td><CopyableCode code="vnetName" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network name.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnPackageUri" /></td>
    <td><code>string</code></td>
    <td>The URI where the VPN package can be downloaded. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_route_for_vnet">

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
    <td><CopyableCode code="endAddress" /></td>
    <td><code>string</code></td>
    <td>The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routeType" /></td>
    <td><code>string</code></td>
    <td>The type of route this is: DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918 INHERITED - Routes inherited from the real Virtual Network routes STATIC - Static route set on the app only These values will be used for syncing an app's routes with those from a Virtual Network. Known values are: "DEFAULT", "INHERITED", and "STATIC". (DEFAULT, INHERITED, STATIC)</td>
</tr>
<tr>
    <td><CopyableCode code="startAddress" /></td>
    <td><code>string</code></td>
    <td>The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.</td>
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
<TabItem value="list_routes_for_vnet">

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
    <td><CopyableCode code="endAddress" /></td>
    <td><code>string</code></td>
    <td>The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routeType" /></td>
    <td><code>string</code></td>
    <td>The type of route this is: DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918 INHERITED - Routes inherited from the real Virtual Network routes STATIC - Static route set on the app only These values will be used for syncing an app's routes with those from a Virtual Network. Known values are: "DEFAULT", "INHERITED", and "STATIC". (DEFAULT, INHERITED, STATIC)</td>
</tr>
<tr>
    <td><CopyableCode code="startAddress" /></td>
    <td><code>string</code></td>
    <td>The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.</td>
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
    <td><CopyableCode code="asyncScalingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan will attempt to scale asynchronously if there are insufficient workers to scale synchronously. If false, this App Service Plan will only attempt sync scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticScaleEnabled" /></td>
    <td><code>boolean</code></td>
    <td>ServerFarm supports ElasticScale. Apps in this plan will scale as if the ServerFarm was ElasticPremium sku.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="freeOfferExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the server farm free offer expires.</td>
</tr>
<tr>
    <td><CopyableCode code="geoRegion" /></td>
    <td><code>string</code></td>
    <td>Geographical location for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperV" /></td>
    <td><code>boolean</code></td>
    <td>If Hyper-V container app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="installScripts" /></td>
    <td><code>array</code></td>
    <td>Install scripts associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="isCustomMode" /></td>
    <td><code>boolean</code></td>
    <td>Whether this server farm is in custom mode.</td>
</tr>
<tr>
    <td><CopyableCode code="isSpot" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan owns spot instances.</td>
</tr>
<tr>
    <td><CopyableCode code="isXenon" /></td>
    <td><code>boolean</code></td>
    <td>Obsolete: If Hyper-V container app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the Kubernetes Environment to use for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumElasticWorkerCount" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of instances that can be assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>All network settings for the server farm.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSites" /></td>
    <td><code>integer</code></td>
    <td>Number of apps assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>The number of instances that are assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="perSiteScaling" /></td>
    <td><code>boolean</code></td>
    <td>If true, apps assigned to this App Service plan can be scaled independently. If false, apps assigned to this App Service plan will scale to all instances of the plan.</td>
</tr>
<tr>
    <td><CopyableCode code="planDefaultIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity to use by platform for various features and integrations using managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App Service Plan. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rdpEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, RDP access is enabled for this App Service plan. Only applicable for IsCustomMode ASPs. If false, RDP access is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="registryAdapters" /></td>
    <td><code>array</code></td>
    <td>Registry adapters associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="reserved" /></td>
    <td><code>boolean</code></td>
    <td>If Linux app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group of the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Description of a SKU for a scalable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="spotExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the server farm expires. Valid only if it is a spot server farm.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>App Service plan status. Known values are: "Ready", "Pending", and "Creating". (Ready, Pending, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="storageMounts" /></td>
    <td><code>array</code></td>
    <td>Storage mounts associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="subscription" /></td>
    <td><code>string</code></td>
    <td>App Service plan subscription.</td>
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
    <td><CopyableCode code="targetWorkerCount" /></td>
    <td><code>integer</code></td>
    <td>Scaling worker count.</td>
</tr>
<tr>
    <td><CopyableCode code="targetWorkerSizeId" /></td>
    <td><code>integer</code></td>
    <td>Scaling worker size ID.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workerTierName" /></td>
    <td><code>string</code></td>
    <td>Target worker tier assigned to the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan will perform availability zone balancing. If false, this App Service Plan will not perform availability zone balancing.</td>
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
    <td><CopyableCode code="asyncScalingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan will attempt to scale asynchronously if there are insufficient workers to scale synchronously. If false, this App Service Plan will only attempt sync scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticScaleEnabled" /></td>
    <td><code>boolean</code></td>
    <td>ServerFarm supports ElasticScale. Apps in this plan will scale as if the ServerFarm was ElasticPremium sku.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="freeOfferExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the server farm free offer expires.</td>
</tr>
<tr>
    <td><CopyableCode code="geoRegion" /></td>
    <td><code>string</code></td>
    <td>Geographical location for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperV" /></td>
    <td><code>boolean</code></td>
    <td>If Hyper-V container app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="installScripts" /></td>
    <td><code>array</code></td>
    <td>Install scripts associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="isCustomMode" /></td>
    <td><code>boolean</code></td>
    <td>Whether this server farm is in custom mode.</td>
</tr>
<tr>
    <td><CopyableCode code="isSpot" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan owns spot instances.</td>
</tr>
<tr>
    <td><CopyableCode code="isXenon" /></td>
    <td><code>boolean</code></td>
    <td>Obsolete: If Hyper-V container app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the Kubernetes Environment to use for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumElasticWorkerCount" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of instances that can be assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>All network settings for the server farm.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSites" /></td>
    <td><code>integer</code></td>
    <td>Number of apps assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>The number of instances that are assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="perSiteScaling" /></td>
    <td><code>boolean</code></td>
    <td>If true, apps assigned to this App Service plan can be scaled independently. If false, apps assigned to this App Service plan will scale to all instances of the plan.</td>
</tr>
<tr>
    <td><CopyableCode code="planDefaultIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity to use by platform for various features and integrations using managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App Service Plan. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rdpEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, RDP access is enabled for this App Service plan. Only applicable for IsCustomMode ASPs. If false, RDP access is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="registryAdapters" /></td>
    <td><code>array</code></td>
    <td>Registry adapters associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="reserved" /></td>
    <td><code>boolean</code></td>
    <td>If Linux app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group of the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Description of a SKU for a scalable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="spotExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the server farm expires. Valid only if it is a spot server farm.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>App Service plan status. Known values are: "Ready", "Pending", and "Creating". (Ready, Pending, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="storageMounts" /></td>
    <td><code>array</code></td>
    <td>Storage mounts associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="subscription" /></td>
    <td><code>string</code></td>
    <td>App Service plan subscription.</td>
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
    <td><CopyableCode code="targetWorkerCount" /></td>
    <td><code>integer</code></td>
    <td>Scaling worker count.</td>
</tr>
<tr>
    <td><CopyableCode code="targetWorkerSizeId" /></td>
    <td><code>integer</code></td>
    <td>Scaling worker size ID.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workerTierName" /></td>
    <td><code>string</code></td>
    <td>Target worker tier assigned to the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan will perform availability zone balancing. If false, this App Service Plan will not perform availability zone balancing.</td>
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
    <td><CopyableCode code="asyncScalingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan will attempt to scale asynchronously if there are insufficient workers to scale synchronously. If false, this App Service Plan will only attempt sync scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticScaleEnabled" /></td>
    <td><code>boolean</code></td>
    <td>ServerFarm supports ElasticScale. Apps in this plan will scale as if the ServerFarm was ElasticPremium sku.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="freeOfferExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the server farm free offer expires.</td>
</tr>
<tr>
    <td><CopyableCode code="geoRegion" /></td>
    <td><code>string</code></td>
    <td>Geographical location for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperV" /></td>
    <td><code>boolean</code></td>
    <td>If Hyper-V container app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="installScripts" /></td>
    <td><code>array</code></td>
    <td>Install scripts associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="isCustomMode" /></td>
    <td><code>boolean</code></td>
    <td>Whether this server farm is in custom mode.</td>
</tr>
<tr>
    <td><CopyableCode code="isSpot" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan owns spot instances.</td>
</tr>
<tr>
    <td><CopyableCode code="isXenon" /></td>
    <td><code>boolean</code></td>
    <td>Obsolete: If Hyper-V container app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the Kubernetes Environment to use for the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumElasticWorkerCount" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of instances that can be assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>All network settings for the server farm.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfSites" /></td>
    <td><code>integer</code></td>
    <td>Number of apps assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>The number of instances that are assigned to this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="perSiteScaling" /></td>
    <td><code>boolean</code></td>
    <td>If true, apps assigned to this App Service plan can be scaled independently. If false, apps assigned to this App Service plan will scale to all instances of the plan.</td>
</tr>
<tr>
    <td><CopyableCode code="planDefaultIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity to use by platform for various features and integrations using managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App Service Plan. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rdpEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, RDP access is enabled for this App Service plan. Only applicable for IsCustomMode ASPs. If false, RDP access is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="registryAdapters" /></td>
    <td><code>array</code></td>
    <td>Registry adapters associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="reserved" /></td>
    <td><code>boolean</code></td>
    <td>If Linux app service plan true, false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Resource group of the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Description of a SKU for a scalable resource.</td>
</tr>
<tr>
    <td><CopyableCode code="spotExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the server farm expires. Valid only if it is a spot server farm.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>App Service plan status. Known values are: "Ready", "Pending", and "Creating". (Ready, Pending, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="storageMounts" /></td>
    <td><code>array</code></td>
    <td>Storage mounts associated with this App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="subscription" /></td>
    <td><code>string</code></td>
    <td>App Service plan subscription.</td>
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
    <td><CopyableCode code="targetWorkerCount" /></td>
    <td><code>integer</code></td>
    <td>Scaling worker count.</td>
</tr>
<tr>
    <td><CopyableCode code="targetWorkerSizeId" /></td>
    <td><code>integer</code></td>
    <td>Scaling worker size ID.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workerTierName" /></td>
    <td><code>string</code></td>
    <td>Target worker tier assigned to the App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>If true, this App Service Plan will perform availability zone balancing. If false, this App Service Plan will not perform availability zone balancing.</td>
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
    <td><a href="#get_hybrid_connection"><CopyableCode code="get_hybrid_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve a Hybrid Connection in use in an App Service plan. Description for Retrieve a Hybrid Connection in use in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#get_vnet_gateway"><CopyableCode code="get_vnet_gateway" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Virtual Network gateway. Description for Get a Virtual Network gateway.</td>
</tr>
<tr>
    <td><a href="#get_route_for_vnet"><CopyableCode code="get_route_for_vnet" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Virtual Network route in an App Service plan. Description for Get a Virtual Network route in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#list_routes_for_vnet"><CopyableCode code="list_routes_for_vnet" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all routes that are associated with a Virtual Network in an App Service plan. Description for Get all routes that are associated with a Virtual Network in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an App Service plan. Description for Get an App Service plan.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all App Service plans in a resource group. Description for Get all App Service plans in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-detailed"><code>detailed</code></a></td>
    <td>Get all App Service plans for a subscription. Description for Get all App Service plans for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update_vnet_route"><CopyableCode code="create_or_update_vnet_route" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Virtual Network route in an App Service plan. Description for Create or update a Virtual Network route in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an App Service Plan. Description for Creates or updates an App Service Plan.</td>
</tr>
<tr>
    <td><a href="#update_vnet_gateway"><CopyableCode code="update_vnet_gateway" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Virtual Network gateway. Description for Update a Virtual Network gateway.</td>
</tr>
<tr>
    <td><a href="#update_vnet_route"><CopyableCode code="update_vnet_route" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Virtual Network route in an App Service plan. Description for Create or update a Virtual Network route in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an App Service Plan. Description for Creates or updates an App Service Plan.</td>
</tr>
<tr>
    <td><a href="#create_or_update_vnet_route"><CopyableCode code="create_or_update_vnet_route" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Virtual Network route in an App Service plan. Description for Create or update a Virtual Network route in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an App Service Plan. Description for Creates or updates an App Service Plan.</td>
</tr>
<tr>
    <td><a href="#delete_hybrid_connection"><CopyableCode code="delete_hybrid_connection" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Hybrid Connection in use in an App Service plan. Description for Delete a Hybrid Connection in use in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#delete_vnet_route"><CopyableCode code="delete_vnet_route" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-route_name"><code>route_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Virtual Network route in an App Service plan. Description for Delete a Virtual Network route in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an App Service plan. Description for Delete an App Service plan.</td>
</tr>
<tr>
    <td><a href="#list_capabilities"><CopyableCode code="list_capabilities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all capabilities of an App Service plan. Description for List all capabilities of an App Service plan.</td>
</tr>
<tr>
    <td><a href="#list_hybrid_connections"><CopyableCode code="list_hybrid_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve all Hybrid Connections in use in an App Service plan. Description for Retrieve all Hybrid Connections in use in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#list_web_apps"><CopyableCode code="list_web_apps" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all apps associated with an App Service plan. Description for Get all apps associated with an App Service plan.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets server farm usage information. Description for Gets server farm usage information.</td>
</tr>
<tr>
    <td><a href="#list_hybrid_connection_keys"><CopyableCode code="list_hybrid_connection_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the send key name and value of a Hybrid Connection. Description for Get the send key name and value of a Hybrid Connection.</td>
</tr>
<tr>
    <td><a href="#list_web_apps_by_hybrid_connection"><CopyableCode code="list_web_apps_by_hybrid_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all apps that use a Hybrid Connection in an App Service Plan. Description for Get all apps that use a Hybrid Connection in an App Service Plan.</td>
</tr>
<tr>
    <td><a href="#list_vnets"><CopyableCode code="list_vnets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Virtual Networks associated with an App Service plan. Description for Get all Virtual Networks associated with an App Service plan.</td>
</tr>
<tr>
    <td><a href="#get_server_farm_rdp_password"><CopyableCode code="get_server_farm_rdp_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the RDP password for an IsCustomMode ServerFarm. Description for Get the RDP password for an IsCustomMode ServerFarm.</td>
</tr>
<tr>
    <td><a href="#get_server_farm_instance_details"><CopyableCode code="get_server_farm_instance_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the instance details for an app service plan. Description for Get the instance details for an app service plan.</td>
</tr>
<tr>
    <td><a href="#get_server_farm_skus"><CopyableCode code="get_server_farm_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all selectable SKUs for a given App Service Plan. Description for Gets all selectable SKUs for a given App Service Plan.</td>
</tr>
<tr>
    <td><a href="#get_hybrid_connection_plan_limit"><CopyableCode code="get_hybrid_connection_plan_limit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the maximum number of Hybrid Connections allowed in an App Service plan. Description for Get the maximum number of Hybrid Connections allowed in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#get_vnet_from_server_farm"><CopyableCode code="get_vnet_from_server_farm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Virtual Network associated with an App Service plan. Description for Get a Virtual Network associated with an App Service plan.</td>
</tr>
<tr>
    <td><a href="#recycle_managed_instance_worker"><CopyableCode code="recycle_managed_instance_worker" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_name"><code>worker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Recycles a managed instance worker machine. Description for Recycles a managed instance worker machine.</td>
</tr>
<tr>
    <td><a href="#restart_web_apps"><CopyableCode code="restart_web_apps" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-softRestart"><code>softRestart</code></a></td>
    <td>Restart all apps in an App Service plan. Description for Restart all apps in an App Service plan.</td>
</tr>
<tr>
    <td><a href="#reboot_worker"><CopyableCode code="reboot_worker" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_name"><code>worker_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reboot a worker machine in an App Service plan. Description for Reboot a worker machine in an App Service plan.</td>
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
<tr id="parameter-gateway_name">
    <td><CopyableCode code="gateway_name" /></td>
    <td><code>string</code></td>
    <td>Name of the gateway. Only the 'primary' gateway is supported. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>App Service plan. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Service Bus namespace. Required.</td>
</tr>
<tr id="parameter-relay_name">
    <td><CopyableCode code="relay_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Service Bus relay. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-route_name">
    <td><CopyableCode code="route_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Virtual Network route. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vnet_name">
    <td><CopyableCode code="vnet_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Virtual Network. Required.</td>
</tr>
<tr id="parameter-worker_name">
    <td><CopyableCode code="worker_name" /></td>
    <td><code>string</code></td>
    <td>Name of worker machine, which typically starts with RD. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2'). Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting from (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>string</code></td>
    <td>List page size. If specified, results are paged. Default value is None.</td>
</tr>
<tr id="parameter-detailed">
    <td><CopyableCode code="detailed" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to return all App Service plan properties. The default is false, which returns a subset of the properties. Retrieval of all properties may increase the API latency. Default value is None.</td>
</tr>
<tr id="parameter-softRestart">
    <td><CopyableCode code="softRestart" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to perform a soft restart, applies the configuration settings and restarts the apps if necessary. The default is false, which always restarts and reprovisions the apps. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_hybrid_connection"
    values={[
        { label: 'get_hybrid_connection', value: 'get_hybrid_connection' },
        { label: 'get_vnet_gateway', value: 'get_vnet_gateway' },
        { label: 'get_route_for_vnet', value: 'get_route_for_vnet' },
        { label: 'list_routes_for_vnet', value: 'list_routes_for_vnet' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_hybrid_connection">

Retrieve a Hybrid Connection in use in an App Service plan. Description for Retrieve a Hybrid Connection in use in an App Service plan.

```sql
SELECT
id,
name,
hostname,
kind,
port,
relayArmUri,
relayName,
sendKeyName,
sendKeyValue,
serviceBusNamespace,
serviceBusSuffix,
systemData,
type
FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND relay_name = '{{ relay_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_vnet_gateway">

Get a Virtual Network gateway. Description for Get a Virtual Network gateway.

```sql
SELECT
id,
name,
kind,
systemData,
type,
vnetName,
vpnPackageUri
FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_route_for_vnet">

Get a Virtual Network route in an App Service plan. Description for Get a Virtual Network route in an App Service plan.

```sql
SELECT
id,
name,
endAddress,
kind,
routeType,
startAddress,
systemData,
type
FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND route_name = '{{ route_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_routes_for_vnet">

Get all routes that are associated with a Virtual Network in an App Service plan. Description for Get all routes that are associated with a Virtual Network in an App Service plan.

```sql
SELECT
id,
name,
endAddress,
kind,
routeType,
startAddress,
systemData,
type
FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get an App Service plan. Description for Get an App Service plan.

```sql
SELECT
id,
name,
asyncScalingEnabled,
elasticScaleEnabled,
extendedLocation,
freeOfferExpirationTime,
geoRegion,
hostingEnvironmentProfile,
hyperV,
identity,
installScripts,
isCustomMode,
isSpot,
isXenon,
kind,
kubeEnvironmentProfile,
location,
maximumElasticWorkerCount,
maximumNumberOfWorkers,
network,
numberOfSites,
numberOfWorkers,
perSiteScaling,
planDefaultIdentity,
provisioningState,
rdpEnabled,
registryAdapters,
reserved,
resourceGroup,
sku,
spotExpirationTime,
status,
storageMounts,
subscription,
systemData,
tags,
targetWorkerCount,
targetWorkerSizeId,
type,
workerTierName,
zoneRedundant
FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all App Service plans in a resource group. Description for Get all App Service plans in a resource group.

```sql
SELECT
id,
name,
asyncScalingEnabled,
elasticScaleEnabled,
extendedLocation,
freeOfferExpirationTime,
geoRegion,
hostingEnvironmentProfile,
hyperV,
identity,
installScripts,
isCustomMode,
isSpot,
isXenon,
kind,
kubeEnvironmentProfile,
location,
maximumElasticWorkerCount,
maximumNumberOfWorkers,
network,
numberOfSites,
numberOfWorkers,
perSiteScaling,
planDefaultIdentity,
provisioningState,
rdpEnabled,
registryAdapters,
reserved,
resourceGroup,
sku,
spotExpirationTime,
status,
storageMounts,
subscription,
systemData,
tags,
targetWorkerCount,
targetWorkerSizeId,
type,
workerTierName,
zoneRedundant
FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all App Service plans for a subscription. Description for Get all App Service plans for a subscription.

```sql
SELECT
id,
name,
asyncScalingEnabled,
elasticScaleEnabled,
extendedLocation,
freeOfferExpirationTime,
geoRegion,
hostingEnvironmentProfile,
hyperV,
identity,
installScripts,
isCustomMode,
isSpot,
isXenon,
kind,
kubeEnvironmentProfile,
location,
maximumElasticWorkerCount,
maximumNumberOfWorkers,
network,
numberOfSites,
numberOfWorkers,
perSiteScaling,
planDefaultIdentity,
provisioningState,
rdpEnabled,
registryAdapters,
reserved,
resourceGroup,
sku,
spotExpirationTime,
status,
storageMounts,
subscription,
systemData,
tags,
targetWorkerCount,
targetWorkerSizeId,
type,
workerTierName,
zoneRedundant
FROM azure.web.app_service_plans
WHERE subscription_id = '{{ subscription_id }}' -- required
AND detailed = '{{ detailed }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_vnet_route"
    values={[
        { label: 'create_or_update_vnet_route', value: 'create_or_update_vnet_route' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_vnet_route">

Create or update a Virtual Network route in an App Service plan. Description for Create or update a Virtual Network route in an App Service plan.

```sql
INSERT INTO azure.web.app_service_plans (
properties,
kind,
resource_group_name,
name,
vnet_name,
route_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ vnet_name }}',
'{{ route_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_or_update">

Creates or updates an App Service Plan. Description for Creates or updates an App Service Plan.

```sql
INSERT INTO azure.web.app_service_plans (
tags,
location,
properties,
sku,
extendedLocation,
kind,
identity,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ extendedLocation }}',
'{{ kind }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
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
- name: app_service_plans
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the app_service_plans resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the app_service_plans resource.
    - name: vnet_name
      value: "{{ vnet_name }}"
      description: Required parameter for the app_service_plans resource.
    - name: route_name
      value: "{{ route_name }}"
      description: Required parameter for the app_service_plans resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the app_service_plans resource.
    - name: properties
      description: |
        AppServicePlan resource specific properties.
      value:
        workerTierName: "{{ workerTierName }}"
        status: "{{ status }}"
        subscription: "{{ subscription }}"
        hostingEnvironmentProfile:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
        maximumNumberOfWorkers: {{ maximumNumberOfWorkers }}
        numberOfWorkers: {{ numberOfWorkers }}
        geoRegion: "{{ geoRegion }}"
        perSiteScaling: {{ perSiteScaling }}
        elasticScaleEnabled: {{ elasticScaleEnabled }}
        maximumElasticWorkerCount: {{ maximumElasticWorkerCount }}
        numberOfSites: {{ numberOfSites }}
        isSpot: {{ isSpot }}
        spotExpirationTime: "{{ spotExpirationTime }}"
        freeOfferExpirationTime: "{{ freeOfferExpirationTime }}"
        resourceGroup: "{{ resourceGroup }}"
        reserved: {{ reserved }}
        isXenon: {{ isXenon }}
        hyperV: {{ hyperV }}
        targetWorkerCount: {{ targetWorkerCount }}
        targetWorkerSizeId: {{ targetWorkerSizeId }}
        provisioningState: "{{ provisioningState }}"
        kubeEnvironmentProfile:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
        zoneRedundant: {{ zoneRedundant }}
        asyncScalingEnabled: {{ asyncScalingEnabled }}
        planDefaultIdentity:
          identityType: "{{ identityType }}"
          userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
        isCustomMode: {{ isCustomMode }}
        registryAdapters:
          - registryKey: "{{ registryKey }}"
            type: "{{ type }}"
            keyVaultSecretReference:
              secretUri: "{{ secretUri }}"
              referenceStatus: "{{ referenceStatus }}"
        installScripts:
          - name: "{{ name }}"
            source:
              sourceUri: "{{ sourceUri }}"
              type: "{{ type }}"
        network:
          virtualNetworkSubnetId: "{{ virtualNetworkSubnetId }}"
        storageMounts:
          - name: "{{ name }}"
            type: "{{ type }}"
            source: "{{ source }}"
            destinationPath: "{{ destinationPath }}"
            credentialsKeyVaultReference:
              secretUri: "{{ secretUri }}"
              referenceStatus: "{{ referenceStatus }}"
        rdpEnabled: {{ rdpEnabled }}
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource. If the resource is an app, you can refer to \`https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference \`_ for details supported values for kind.
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
        Description of a SKU for a scalable resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
        skuCapacity:
          minimum: {{ minimum }}
          maximum: {{ maximum }}
          elasticMaximum: {{ elasticMaximum }}
          default: {{ default }}
          scaleType: "{{ scaleType }}"
        locations:
          - "{{ locations }}"
        capabilities:
          - name: "{{ name }}"
            value: "{{ value }}"
            reason: "{{ reason }}"
    - name: extendedLocation
      description: |
        Extended Location.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        Managed service identity.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_vnet_gateway"
    values={[
        { label: 'update_vnet_gateway', value: 'update_vnet_gateway' },
        { label: 'update_vnet_route', value: 'update_vnet_route' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_vnet_gateway">

Update a Virtual Network gateway. Description for Update a Virtual Network gateway.

```sql
UPDATE azure.web.app_service_plans
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND vnet_name = '{{ vnet_name }}' --required
AND gateway_name = '{{ gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_vnet_route">

Create or update a Virtual Network route in an App Service plan. Description for Create or update a Virtual Network route in an App Service plan.

```sql
UPDATE azure.web.app_service_plans
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND vnet_name = '{{ vnet_name }}' --required
AND route_name = '{{ route_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update">

Creates or updates an App Service Plan. Description for Creates or updates an App Service Plan.

```sql
UPDATE azure.web.app_service_plans
SET 
kind = '{{ kind }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
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
    defaultValue="create_or_update_vnet_route"
    values={[
        { label: 'create_or_update_vnet_route', value: 'create_or_update_vnet_route' },
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update_vnet_route">

Create or update a Virtual Network route in an App Service plan. Description for Create or update a Virtual Network route in an App Service plan.

```sql
REPLACE azure.web.app_service_plans
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND vnet_name = '{{ vnet_name }}' --required
AND route_name = '{{ route_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update">

Creates or updates an App Service Plan. Description for Creates or updates an App Service Plan.

```sql
REPLACE azure.web.app_service_plans
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
extendedLocation = '{{ extendedLocation }}',
kind = '{{ kind }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
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
    defaultValue="delete_hybrid_connection"
    values={[
        { label: 'delete_hybrid_connection', value: 'delete_hybrid_connection' },
        { label: 'delete_vnet_route', value: 'delete_vnet_route' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_hybrid_connection">

Delete a Hybrid Connection in use in an App Service plan. Description for Delete a Hybrid Connection in use in an App Service plan.

```sql
DELETE FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND relay_name = '{{ relay_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_vnet_route">

Delete a Virtual Network route in an App Service plan. Description for Delete a Virtual Network route in an App Service plan.

```sql
DELETE FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND vnet_name = '{{ vnet_name }}' --required
AND route_name = '{{ route_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete an App Service plan. Description for Delete an App Service plan.

```sql
DELETE FROM azure.web.app_service_plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_capabilities"
    values={[
        { label: 'list_capabilities', value: 'list_capabilities' },
        { label: 'list_hybrid_connections', value: 'list_hybrid_connections' },
        { label: 'list_web_apps', value: 'list_web_apps' },
        { label: 'list_usages', value: 'list_usages' },
        { label: 'list_hybrid_connection_keys', value: 'list_hybrid_connection_keys' },
        { label: 'list_web_apps_by_hybrid_connection', value: 'list_web_apps_by_hybrid_connection' },
        { label: 'list_vnets', value: 'list_vnets' },
        { label: 'get_server_farm_rdp_password', value: 'get_server_farm_rdp_password' },
        { label: 'get_server_farm_instance_details', value: 'get_server_farm_instance_details' },
        { label: 'get_server_farm_skus', value: 'get_server_farm_skus' },
        { label: 'get_hybrid_connection_plan_limit', value: 'get_hybrid_connection_plan_limit' },
        { label: 'get_vnet_from_server_farm', value: 'get_vnet_from_server_farm' },
        { label: 'recycle_managed_instance_worker', value: 'recycle_managed_instance_worker' },
        { label: 'restart_web_apps', value: 'restart_web_apps' },
        { label: 'reboot_worker', value: 'reboot_worker' }
    ]}
>
<TabItem value="list_capabilities">

List all capabilities of an App Service plan. Description for List all capabilities of an App Service plan.

```sql
EXEC azure.web.app_service_plans.list_capabilities 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_hybrid_connections">

Retrieve all Hybrid Connections in use in an App Service plan. Description for Retrieve all Hybrid Connections in use in an App Service plan.

```sql
EXEC azure.web.app_service_plans.list_hybrid_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_web_apps">

Get all apps associated with an App Service plan. Description for Get all apps associated with an App Service plan.

```sql
EXEC azure.web.app_service_plans.list_web_apps 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$skipToken='{{ $skipToken }}', 
@$filter='{{ $filter }}', 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="list_usages">

Gets server farm usage information. Description for Gets server farm usage information.

```sql
EXEC azure.web.app_service_plans.list_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_hybrid_connection_keys">

Get the send key name and value of a Hybrid Connection. Description for Get the send key name and value of a Hybrid Connection.

```sql
EXEC azure.web.app_service_plans.list_hybrid_connection_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_web_apps_by_hybrid_connection">

Get all apps that use a Hybrid Connection in an App Service Plan. Description for Get all apps that use a Hybrid Connection in an App Service Plan.

```sql
EXEC azure.web.app_service_plans.list_web_apps_by_hybrid_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_vnets">

Get all Virtual Networks associated with an App Service plan. Description for Get all Virtual Networks associated with an App Service plan.

```sql
EXEC azure.web.app_service_plans.list_vnets 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_server_farm_rdp_password">

Get the RDP password for an IsCustomMode ServerFarm. Description for Get the RDP password for an IsCustomMode ServerFarm.

```sql
EXEC azure.web.app_service_plans.get_server_farm_rdp_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_server_farm_instance_details">

Get the instance details for an app service plan. Description for Get the instance details for an app service plan.

```sql
EXEC azure.web.app_service_plans.get_server_farm_instance_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_server_farm_skus">

Gets all selectable SKUs for a given App Service Plan. Description for Gets all selectable SKUs for a given App Service Plan.

```sql
EXEC azure.web.app_service_plans.get_server_farm_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_hybrid_connection_plan_limit">

Get the maximum number of Hybrid Connections allowed in an App Service plan. Description for Get the maximum number of Hybrid Connections allowed in an App Service plan.

```sql
EXEC azure.web.app_service_plans.get_hybrid_connection_plan_limit 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_vnet_from_server_farm">

Get a Virtual Network associated with an App Service plan. Description for Get a Virtual Network associated with an App Service plan.

```sql
EXEC azure.web.app_service_plans.get_vnet_from_server_farm 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="recycle_managed_instance_worker">

Recycles a managed instance worker machine. Description for Recycles a managed instance worker machine.

```sql
EXEC azure.web.app_service_plans.recycle_managed_instance_worker 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_name='{{ worker_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart_web_apps">

Restart all apps in an App Service plan. Description for Restart all apps in an App Service plan.

```sql
EXEC azure.web.app_service_plans.restart_web_apps 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@softRestart={{ softRestart }}
;
```
</TabItem>
<TabItem value="reboot_worker">

Reboot a worker machine in an App Service plan. Description for Reboot a worker machine in an App Service plan.

```sql
EXEC azure.web.app_service_plans.reboot_worker 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_name='{{ worker_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
