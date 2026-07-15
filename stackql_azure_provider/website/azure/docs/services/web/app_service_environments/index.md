--- 
title: app_service_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - app_service_environments
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

Creates, updates, deletes, gets or lists an <code>app_service_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_service_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.app_service_environments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_worker_pool_instance_metric_definitions"
    values={[
        { label: 'list_worker_pool_instance_metric_definitions', value: 'list_worker_pool_instance_metric_definitions' },
        { label: 'list_web_worker_metric_definitions', value: 'list_web_worker_metric_definitions' },
        { label: 'list_multi_role_pool_instance_metric_definitions', value: 'list_multi_role_pool_instance_metric_definitions' },
        { label: 'get_diagnostics_item', value: 'get_diagnostics_item' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_worker_pool_instance_metric_definitions">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metricAvailabilities" /></td>
    <td><code>array</code></td>
    <td>List of time grains supported for the metric together with retention period.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAggregationType" /></td>
    <td><code>string</code></td>
    <td>Primary aggregation type.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Resource metric definition properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUri" /></td>
    <td><code>string</code></td>
    <td>Resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>Unit of the metric.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_web_worker_metric_definitions">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metricAvailabilities" /></td>
    <td><code>array</code></td>
    <td>List of time grains supported for the metric together with retention period.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAggregationType" /></td>
    <td><code>string</code></td>
    <td>Primary aggregation type.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Resource metric definition properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUri" /></td>
    <td><code>string</code></td>
    <td>Resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>Unit of the metric.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_multi_role_pool_instance_metric_definitions">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metricAvailabilities" /></td>
    <td><code>array</code></td>
    <td>List of time grains supported for the metric together with retention period.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryAggregationType" /></td>
    <td><code>string</code></td>
    <td>Primary aggregation type.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Resource metric definition properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUri" /></td>
    <td><code>string</code></td>
    <td>Resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="unit" /></td>
    <td><code>string</code></td>
    <td>Unit of the metric.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_diagnostics_item">

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
    <td>Name/identifier of the diagnostics.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsOutput" /></td>
    <td><code>string</code></td>
    <td>Diagnostics output.</td>
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
    <td><CopyableCode code="ipAddresses" /></td>
    <td><code>array</code></td>
    <td>Private IPAddresses mapped to the remote private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>PrivateEndpoint of a remote private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>The state of a private link connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>:vartype provisioning_state: str</td>
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
    <td><CopyableCode code="clusterSettings" /></td>
    <td><code>array</code></td>
    <td>Custom settings for changing the behavior of the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsSuffixConfiguration" /></td>
    <td><code>object</code></td>
    <td>Full view of the custom domain suffix configuration for ASEv3.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedHostCount" /></td>
    <td><code>integer</code></td>
    <td>Dedicated Host Count.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSuffix" /></td>
    <td><code>string</code></td>
    <td>DNS suffix of the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="frontEndScaleFactor" /></td>
    <td><code>integer</code></td>
    <td>Scale factor for front-ends.</td>
</tr>
<tr>
    <td><CopyableCode code="hasLinuxWorkers" /></td>
    <td><code>boolean</code></td>
    <td>Flag that displays whether an ASE has linux workers or not.</td>
</tr>
<tr>
    <td><CopyableCode code="internalLoadBalancingMode" /></td>
    <td><code>string</code></td>
    <td>Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. Known values are: "None", "Web", "Publishing", and "Web, Publishing". (None, Web, Publishing, Web, Publishing)</td>
</tr>
<tr>
    <td><CopyableCode code="ipsslAddressCount" /></td>
    <td><code>integer</code></td>
    <td>Number of IP SSL addresses reserved for the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of VMs in the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="multiRoleCount" /></td>
    <td><code>integer</code></td>
    <td>Number of front-end instances.</td>
</tr>
<tr>
    <td><CopyableCode code="multiSize" /></td>
    <td><code>string</code></td>
    <td>Front-end VM size, e.g. "Medium", "Large".</td>
</tr>
<tr>
    <td><CopyableCode code="networkingConfiguration" /></td>
    <td><code>object</code></td>
    <td>Full view of networking configuration for an ASE.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App Service Environment. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the App Service Environment. Known values are: "Preparing", "Ready", "Scaling", and "Deleting". (Preparing, Ready, Scaling, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>true if the App Service Environment is suspended; otherwise, false. The environment can be suspended, e.g. when the management endpoint is no longer available (most likely because NSG blocked the incoming traffic).</td>
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
    <td><CopyableCode code="upgradeAvailability" /></td>
    <td><code>string</code></td>
    <td>Whether an upgrade is available for this App Service Environment. Known values are: "None" and "Ready". (None, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePreference" /></td>
    <td><code>string</code></td>
    <td>Upgrade Preference. Known values are: "None", "Early", "Late", and "Manual". (None, Early, Late, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="userWhitelistedIpRanges" /></td>
    <td><code>array</code></td>
    <td>User added ip ranges to whitelist on ASE db.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Description of the Virtual Network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this App Service Environment is zone-redundant.</td>
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
    <td><CopyableCode code="clusterSettings" /></td>
    <td><code>array</code></td>
    <td>Custom settings for changing the behavior of the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsSuffixConfiguration" /></td>
    <td><code>object</code></td>
    <td>Full view of the custom domain suffix configuration for ASEv3.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedHostCount" /></td>
    <td><code>integer</code></td>
    <td>Dedicated Host Count.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSuffix" /></td>
    <td><code>string</code></td>
    <td>DNS suffix of the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="frontEndScaleFactor" /></td>
    <td><code>integer</code></td>
    <td>Scale factor for front-ends.</td>
</tr>
<tr>
    <td><CopyableCode code="hasLinuxWorkers" /></td>
    <td><code>boolean</code></td>
    <td>Flag that displays whether an ASE has linux workers or not.</td>
</tr>
<tr>
    <td><CopyableCode code="internalLoadBalancingMode" /></td>
    <td><code>string</code></td>
    <td>Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. Known values are: "None", "Web", "Publishing", and "Web, Publishing". (None, Web, Publishing, Web, Publishing)</td>
</tr>
<tr>
    <td><CopyableCode code="ipsslAddressCount" /></td>
    <td><code>integer</code></td>
    <td>Number of IP SSL addresses reserved for the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of VMs in the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="multiRoleCount" /></td>
    <td><code>integer</code></td>
    <td>Number of front-end instances.</td>
</tr>
<tr>
    <td><CopyableCode code="multiSize" /></td>
    <td><code>string</code></td>
    <td>Front-end VM size, e.g. "Medium", "Large".</td>
</tr>
<tr>
    <td><CopyableCode code="networkingConfiguration" /></td>
    <td><code>object</code></td>
    <td>Full view of networking configuration for an ASE.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App Service Environment. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the App Service Environment. Known values are: "Preparing", "Ready", "Scaling", and "Deleting". (Preparing, Ready, Scaling, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>true if the App Service Environment is suspended; otherwise, false. The environment can be suspended, e.g. when the management endpoint is no longer available (most likely because NSG blocked the incoming traffic).</td>
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
    <td><CopyableCode code="upgradeAvailability" /></td>
    <td><code>string</code></td>
    <td>Whether an upgrade is available for this App Service Environment. Known values are: "None" and "Ready". (None, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePreference" /></td>
    <td><code>string</code></td>
    <td>Upgrade Preference. Known values are: "None", "Early", "Late", and "Manual". (None, Early, Late, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="userWhitelistedIpRanges" /></td>
    <td><code>array</code></td>
    <td>User added ip ranges to whitelist on ASE db.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Description of the Virtual Network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this App Service Environment is zone-redundant.</td>
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
    <td><CopyableCode code="clusterSettings" /></td>
    <td><code>array</code></td>
    <td>Custom settings for changing the behavior of the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="customDnsSuffixConfiguration" /></td>
    <td><code>object</code></td>
    <td>Full view of the custom domain suffix configuration for ASEv3.</td>
</tr>
<tr>
    <td><CopyableCode code="dedicatedHostCount" /></td>
    <td><code>integer</code></td>
    <td>Dedicated Host Count.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSuffix" /></td>
    <td><code>string</code></td>
    <td>DNS suffix of the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="frontEndScaleFactor" /></td>
    <td><code>integer</code></td>
    <td>Scale factor for front-ends.</td>
</tr>
<tr>
    <td><CopyableCode code="hasLinuxWorkers" /></td>
    <td><code>boolean</code></td>
    <td>Flag that displays whether an ASE has linux workers or not.</td>
</tr>
<tr>
    <td><CopyableCode code="internalLoadBalancingMode" /></td>
    <td><code>string</code></td>
    <td>Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. Known values are: "None", "Web", "Publishing", and "Web, Publishing". (None, Web, Publishing, Web, Publishing)</td>
</tr>
<tr>
    <td><CopyableCode code="ipsslAddressCount" /></td>
    <td><code>integer</code></td>
    <td>Number of IP SSL addresses reserved for the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maximumNumberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of VMs in the App Service Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="multiRoleCount" /></td>
    <td><code>integer</code></td>
    <td>Number of front-end instances.</td>
</tr>
<tr>
    <td><CopyableCode code="multiSize" /></td>
    <td><code>string</code></td>
    <td>Front-end VM size, e.g. "Medium", "Large".</td>
</tr>
<tr>
    <td><CopyableCode code="networkingConfiguration" /></td>
    <td><code>object</code></td>
    <td>Full view of networking configuration for an ASE.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App Service Environment. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the App Service Environment. Known values are: "Preparing", "Ready", "Scaling", and "Deleting". (Preparing, Ready, Scaling, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>true if the App Service Environment is suspended; otherwise, false. The environment can be suspended, e.g. when the management endpoint is no longer available (most likely because NSG blocked the incoming traffic).</td>
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
    <td><CopyableCode code="upgradeAvailability" /></td>
    <td><code>string</code></td>
    <td>Whether an upgrade is available for this App Service Environment. Known values are: "None" and "Ready". (None, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePreference" /></td>
    <td><code>string</code></td>
    <td>Upgrade Preference. Known values are: "None", "Early", "Late", and "Manual". (None, Early, Late, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="userWhitelistedIpRanges" /></td>
    <td><code>array</code></td>
    <td>User added ip ranges to whitelist on ASE db.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetwork" /></td>
    <td><code>object</code></td>
    <td>Description of the Virtual Network. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this App Service Environment is zone-redundant.</td>
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
    <td><a href="#list_worker_pool_instance_metric_definitions"><CopyableCode code="list_worker_pool_instance_metric_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-instance"><code>instance</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metric definitions for a specific instance of a worker pool of an App Service Environment. Description for Get metric definitions for a specific instance of a worker pool of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_web_worker_metric_definitions"><CopyableCode code="list_web_worker_metric_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metric definitions for a worker pool of an App Service Environment. Description for Get metric definitions for a worker pool of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_multi_role_pool_instance_metric_definitions"><CopyableCode code="list_multi_role_pool_instance_metric_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance"><code>instance</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metric definitions for a specific instance of a multi-role pool of an App Service Environment. Description for Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_diagnostics_item"><CopyableCode code="get_diagnostics_item" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-diagnostics_name"><code>diagnostics_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a diagnostics item for an App Service Environment. Description for Get a diagnostics item for an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection"><CopyableCode code="get_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a private endpoint connection. Description for Gets a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of an App Service Environment. Description for Get the properties of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all App Service Environments in a resource group. Description for Get all App Service Environments in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all App Service Environments for a subscription. Description for Get all App Service Environments for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an App Service Environment. Description for Create or update an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update an App Service Environment. Description for Create or update an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an App Service Environment. Description for Create or update an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDelete"><code>forceDelete</code></a></td>
    <td>Delete an App Service Environment. Description for Delete an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_worker_pools"><CopyableCode code="list_worker_pools" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all worker pools of an App Service Environment. Description for Get all worker pools of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_worker_pool_skus"><CopyableCode code="list_worker_pool_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get available SKUs for scaling a worker pool. Description for Get available SKUs for scaling a worker pool.</td>
</tr>
<tr>
    <td><a href="#list_web_worker_usages"><CopyableCode code="list_web_worker_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get usage metrics for a worker pool of an App Service Environment. Description for Get usage metrics for a worker pool of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_capacities"><CopyableCode code="list_capacities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the used, available, and total worker capacity an App Service Environment. Description for Get the used, available, and total worker capacity an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_diagnostics"><CopyableCode code="list_diagnostics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get diagnostic information for an App Service Environment. Description for Get diagnostic information for an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_operations"><CopyableCode code="list_operations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all currently running operations on the App Service Environment. Description for List all currently running operations on the App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_app_service_plans"><CopyableCode code="list_app_service_plans" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all App Service plans in an App Service Environment. Description for Get all App Service plans in an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_web_apps"><CopyableCode code="list_web_apps" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-propertiesToInclude"><code>propertiesToInclude</code></a></td>
    <td>Get all apps in an App Service Environment. Description for Get all apps in an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get global usage metrics of an App Service Environment. Description for Get global usage metrics of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_multi_role_pools"><CopyableCode code="list_multi_role_pools" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all multi-role pools. Description for Get all multi-role pools.</td>
</tr>
<tr>
    <td><a href="#list_multi_role_metric_definitions"><CopyableCode code="list_multi_role_metric_definitions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get metric definitions for a multi-role pool of an App Service Environment. Description for Get metric definitions for a multi-role pool of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#list_multi_role_pool_skus"><CopyableCode code="list_multi_role_pool_skus" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get available SKUs for scaling a multi-role pool. Description for Get available SKUs for scaling a multi-role pool.</td>
</tr>
<tr>
    <td><a href="#list_multi_role_usages"><CopyableCode code="list_multi_role_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get usage metrics for a multi-role pool of an App Service Environment. Description for Get usage metrics for a multi-role pool of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_worker_pool"><CopyableCode code="get_worker_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of a worker pool. Description for Get properties of a worker pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update_worker_pool"><CopyableCode code="create_or_update_worker_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a worker pool. Description for Create or update a worker pool.</td>
</tr>
<tr>
    <td><a href="#update_worker_pool"><CopyableCode code="update_worker_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-worker_pool_name"><code>worker_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a worker pool. Description for Create or update a worker pool.</td>
</tr>
<tr>
    <td><a href="#get_inbound_network_dependencies_endpoints"><CopyableCode code="get_inbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the network endpoints of all inbound dependencies of an App Service Environment. Description for Get the network endpoints of all inbound dependencies of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_outbound_network_dependencies_endpoints"><CopyableCode code="get_outbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the network endpoints of all outbound dependencies of an App Service Environment. Description for Get the network endpoints of all outbound dependencies of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_private_link_resources"><CopyableCode code="get_private_link_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the private link resources. Description for Gets the private link resources.</td>
</tr>
<tr>
    <td><a href="#get_vip_info"><CopyableCode code="get_vip_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get IP addresses assigned to an App Service Environment. Description for Get IP addresses assigned to an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_ase_custom_dns_suffix_configuration"><CopyableCode code="get_ase_custom_dns_suffix_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Custom Dns Suffix configuration of an App Service Environment. Get Custom Dns Suffix configuration of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#update_ase_custom_dns_suffix_configuration"><CopyableCode code="update_ase_custom_dns_suffix_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Custom Dns Suffix configuration of an App Service Environment. Update Custom Dns Suffix configuration of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#delete_ase_custom_dns_suffix_configuration"><CopyableCode code="delete_ase_custom_dns_suffix_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Custom Dns Suffix configuration of an App Service Environment. Delete Custom Dns Suffix configuration of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_ase_v3_networking_configuration"><CopyableCode code="get_ase_v3_networking_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get networking configuration of an App Service Environment. Description for Get networking configuration of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#update_ase_networking_configuration"><CopyableCode code="update_ase_networking_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update networking configuration of an App Service Environment. Description for Update networking configuration of an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#get_multi_role_pool"><CopyableCode code="get_multi_role_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get properties of a multi-role pool. Description for Get properties of a multi-role pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update_multi_role_pool"><CopyableCode code="create_or_update_multi_role_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a multi-role pool. Description for Create or update a multi-role pool.</td>
</tr>
<tr>
    <td><a href="#update_multi_role_pool"><CopyableCode code="update_multi_role_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a multi-role pool. Description for Create or update a multi-role pool.</td>
</tr>
<tr>
    <td><a href="#approve_or_reject_private_endpoint_connection"><CopyableCode code="approve_or_reject_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_connection"><CopyableCode code="delete_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a private endpoint connection. Description for Deletes a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection_list"><CopyableCode code="get_private_endpoint_connection_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of private endpoints associated with a hosting environment. Description for Gets the list of private endpoints associated with a hosting environment.</td>
</tr>
<tr>
    <td><a href="#change_vnet"><CopyableCode code="change_vnet" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Move an App Service Environment to a different VNET. Description for Move an App Service Environment to a different VNET.</td>
</tr>
<tr>
    <td><a href="#test_upgrade_available_notification"><CopyableCode code="test_upgrade_available_notification" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Send a test notification that an upgrade is available for this App Service Environment. Send a test notification that an upgrade is available for this App Service Environment.</td>
</tr>
<tr>
    <td><a href="#upgrade"><CopyableCode code="upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiate an upgrade of an App Service Environment if one is available. Description for Initiate an upgrade of an App Service Environment if one is available.</td>
</tr>
<tr>
    <td><a href="#reboot"><CopyableCode code="reboot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reboot all machines in an App Service Environment. Description for Reboot all machines in an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resume an App Service Environment. Description for Resume an App Service Environment.</td>
</tr>
<tr>
    <td><a href="#suspend"><CopyableCode code="suspend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Suspend an App Service Environment. Description for Suspend an App Service Environment.</td>
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
<tr id="parameter-diagnostics_name">
    <td><CopyableCode code="diagnostics_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-instance">
    <td><CopyableCode code="instance" /></td>
    <td><code>string</code></td>
    <td>Name of the instance in the multi-role pool. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the App Service Environment. Required.</td>
</tr>
<tr id="parameter-private_endpoint_connection_name">
    <td><CopyableCode code="private_endpoint_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private endpoint connection. Required.</td>
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
<tr id="parameter-worker_pool_name">
    <td><CopyableCode code="worker_pool_name" /></td>
    <td><code>string</code></td>
    <td>Name of the worker pool. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'. Default value is None.</td>
</tr>
<tr id="parameter-forceDelete">
    <td><CopyableCode code="forceDelete" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to force the deletion even if the App Service Environment contains resources. The default is false. Default value is None.</td>
</tr>
<tr id="parameter-propertiesToInclude">
    <td><CopyableCode code="propertiesToInclude" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of app properties to include. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_worker_pool_instance_metric_definitions"
    values={[
        { label: 'list_worker_pool_instance_metric_definitions', value: 'list_worker_pool_instance_metric_definitions' },
        { label: 'list_web_worker_metric_definitions', value: 'list_web_worker_metric_definitions' },
        { label: 'list_multi_role_pool_instance_metric_definitions', value: 'list_multi_role_pool_instance_metric_definitions' },
        { label: 'get_diagnostics_item', value: 'get_diagnostics_item' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_worker_pool_instance_metric_definitions">

Get metric definitions for a specific instance of a worker pool of an App Service Environment. Description for Get metric definitions for a specific instance of a worker pool of an App Service Environment.

```sql
SELECT
id,
name,
kind,
metricAvailabilities,
primaryAggregationType,
properties,
resourceUri,
type,
unit
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND worker_pool_name = '{{ worker_pool_name }}' -- required
AND instance = '{{ instance }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_web_worker_metric_definitions">

Get metric definitions for a worker pool of an App Service Environment. Description for Get metric definitions for a worker pool of an App Service Environment.

```sql
SELECT
id,
name,
kind,
metricAvailabilities,
primaryAggregationType,
properties,
resourceUri,
type,
unit
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND worker_pool_name = '{{ worker_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_multi_role_pool_instance_metric_definitions">

Get metric definitions for a specific instance of a multi-role pool of an App Service Environment. Description for Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

```sql
SELECT
id,
name,
kind,
metricAvailabilities,
primaryAggregationType,
properties,
resourceUri,
type,
unit
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND instance = '{{ instance }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_diagnostics_item">

Get a diagnostics item for an App Service Environment. Description for Get a diagnostics item for an App Service Environment.

```sql
SELECT
name,
diagnosticsOutput
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND diagnostics_name = '{{ diagnostics_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection">

Gets a private endpoint connection. Description for Gets a private endpoint connection.

```sql
SELECT
id,
name,
ipAddresses,
kind,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
systemData,
type
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get the properties of an App Service Environment. Description for Get the properties of an App Service Environment.

```sql
SELECT
id,
name,
clusterSettings,
customDnsSuffixConfiguration,
dedicatedHostCount,
dnsSuffix,
frontEndScaleFactor,
hasLinuxWorkers,
internalLoadBalancingMode,
ipsslAddressCount,
kind,
location,
maximumNumberOfMachines,
multiRoleCount,
multiSize,
networkingConfiguration,
provisioningState,
status,
suspended,
systemData,
tags,
type,
upgradeAvailability,
upgradePreference,
userWhitelistedIpRanges,
virtualNetwork,
zoneRedundant
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all App Service Environments in a resource group. Description for Get all App Service Environments in a resource group.

```sql
SELECT
id,
name,
clusterSettings,
customDnsSuffixConfiguration,
dedicatedHostCount,
dnsSuffix,
frontEndScaleFactor,
hasLinuxWorkers,
internalLoadBalancingMode,
ipsslAddressCount,
kind,
location,
maximumNumberOfMachines,
multiRoleCount,
multiSize,
networkingConfiguration,
provisioningState,
status,
suspended,
systemData,
tags,
type,
upgradeAvailability,
upgradePreference,
userWhitelistedIpRanges,
virtualNetwork,
zoneRedundant
FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all App Service Environments for a subscription. Description for Get all App Service Environments for a subscription.

```sql
SELECT
id,
name,
clusterSettings,
customDnsSuffixConfiguration,
dedicatedHostCount,
dnsSuffix,
frontEndScaleFactor,
hasLinuxWorkers,
internalLoadBalancingMode,
ipsslAddressCount,
kind,
location,
maximumNumberOfMachines,
multiRoleCount,
multiSize,
networkingConfiguration,
provisioningState,
status,
suspended,
systemData,
tags,
type,
upgradeAvailability,
upgradePreference,
userWhitelistedIpRanges,
virtualNetwork,
zoneRedundant
FROM azure.web.app_service_environments
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

Create or update an App Service Environment. Description for Create or update an App Service Environment.

```sql
INSERT INTO azure.web.app_service_environments (
tags,
location,
properties,
kind,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: app_service_environments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the app_service_environments resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the app_service_environments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the app_service_environments resource.
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
        Description of an App Service Environment.
      value:
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        virtualNetwork:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          subnet: "{{ subnet }}"
        internalLoadBalancingMode: "{{ internalLoadBalancingMode }}"
        multiSize: "{{ multiSize }}"
        multiRoleCount: {{ multiRoleCount }}
        ipsslAddressCount: {{ ipsslAddressCount }}
        dnsSuffix: "{{ dnsSuffix }}"
        maximumNumberOfMachines: {{ maximumNumberOfMachines }}
        frontEndScaleFactor: {{ frontEndScaleFactor }}
        suspended: {{ suspended }}
        clusterSettings:
          - name: "{{ name }}"
            value: "{{ value }}"
        userWhitelistedIpRanges:
          - "{{ userWhitelistedIpRanges }}"
        hasLinuxWorkers: {{ hasLinuxWorkers }}
        upgradePreference: "{{ upgradePreference }}"
        dedicatedHostCount: {{ dedicatedHostCount }}
        zoneRedundant: {{ zoneRedundant }}
        customDnsSuffixConfiguration:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          systemData:
            createdBy: "{{ createdBy }}"
            createdByType: "{{ createdByType }}"
            createdAt: "{{ createdAt }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedByType: "{{ lastModifiedByType }}"
            lastModifiedAt: "{{ lastModifiedAt }}"
          properties:
            provisioningState: "{{ provisioningState }}"
            provisioningDetails: "{{ provisioningDetails }}"
            dnsSuffix: "{{ dnsSuffix }}"
            certificateUrl: "{{ certificateUrl }}"
            keyVaultReferenceIdentity: "{{ keyVaultReferenceIdentity }}"
          kind: "{{ kind }}"
        networkingConfiguration:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          systemData:
            createdBy: "{{ createdBy }}"
            createdByType: "{{ createdByType }}"
            createdAt: "{{ createdAt }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedByType: "{{ lastModifiedByType }}"
            lastModifiedAt: "{{ lastModifiedAt }}"
          properties:
            windowsOutboundIpAddresses:
              - "{{ windowsOutboundIpAddresses }}"
            linuxOutboundIpAddresses:
              - "{{ linuxOutboundIpAddresses }}"
            externalInboundIpAddresses:
              - "{{ externalInboundIpAddresses }}"
            internalInboundIpAddresses:
              - "{{ internalInboundIpAddresses }}"
            allowNewPrivateEndpointConnections: {{ allowNewPrivateEndpointConnections }}
            ftpEnabled: {{ ftpEnabled }}
            remoteDebugEnabled: {{ remoteDebugEnabled }}
            inboundIpAddressOverride: "{{ inboundIpAddressOverride }}"
          kind: "{{ kind }}"
        upgradeAvailability: "{{ upgradeAvailability }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource. If the resource is an app, you can refer to \`https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference \`_ for details supported values for kind.
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

Create or update an App Service Environment. Description for Create or update an App Service Environment.

```sql
UPDATE azure.web.app_service_environments
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update an App Service Environment. Description for Create or update an App Service Environment.

```sql
REPLACE azure.web.app_service_environments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete an App Service Environment. Description for Delete an App Service Environment.

```sql
DELETE FROM azure.web.app_service_environments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDelete = '{{ forceDelete }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_worker_pools"
    values={[
        { label: 'list_worker_pools', value: 'list_worker_pools' },
        { label: 'list_worker_pool_skus', value: 'list_worker_pool_skus' },
        { label: 'list_web_worker_usages', value: 'list_web_worker_usages' },
        { label: 'list_capacities', value: 'list_capacities' },
        { label: 'list_diagnostics', value: 'list_diagnostics' },
        { label: 'list_operations', value: 'list_operations' },
        { label: 'list_app_service_plans', value: 'list_app_service_plans' },
        { label: 'list_web_apps', value: 'list_web_apps' },
        { label: 'list_usages', value: 'list_usages' },
        { label: 'list_multi_role_pools', value: 'list_multi_role_pools' },
        { label: 'list_multi_role_metric_definitions', value: 'list_multi_role_metric_definitions' },
        { label: 'list_multi_role_pool_skus', value: 'list_multi_role_pool_skus' },
        { label: 'list_multi_role_usages', value: 'list_multi_role_usages' },
        { label: 'get_worker_pool', value: 'get_worker_pool' },
        { label: 'create_or_update_worker_pool', value: 'create_or_update_worker_pool' },
        { label: 'update_worker_pool', value: 'update_worker_pool' },
        { label: 'get_inbound_network_dependencies_endpoints', value: 'get_inbound_network_dependencies_endpoints' },
        { label: 'get_outbound_network_dependencies_endpoints', value: 'get_outbound_network_dependencies_endpoints' },
        { label: 'get_private_link_resources', value: 'get_private_link_resources' },
        { label: 'get_vip_info', value: 'get_vip_info' },
        { label: 'get_ase_custom_dns_suffix_configuration', value: 'get_ase_custom_dns_suffix_configuration' },
        { label: 'update_ase_custom_dns_suffix_configuration', value: 'update_ase_custom_dns_suffix_configuration' },
        { label: 'delete_ase_custom_dns_suffix_configuration', value: 'delete_ase_custom_dns_suffix_configuration' },
        { label: 'get_ase_v3_networking_configuration', value: 'get_ase_v3_networking_configuration' },
        { label: 'update_ase_networking_configuration', value: 'update_ase_networking_configuration' },
        { label: 'get_multi_role_pool', value: 'get_multi_role_pool' },
        { label: 'create_or_update_multi_role_pool', value: 'create_or_update_multi_role_pool' },
        { label: 'update_multi_role_pool', value: 'update_multi_role_pool' },
        { label: 'approve_or_reject_private_endpoint_connection', value: 'approve_or_reject_private_endpoint_connection' },
        { label: 'delete_private_endpoint_connection', value: 'delete_private_endpoint_connection' },
        { label: 'get_private_endpoint_connection_list', value: 'get_private_endpoint_connection_list' },
        { label: 'change_vnet', value: 'change_vnet' },
        { label: 'test_upgrade_available_notification', value: 'test_upgrade_available_notification' },
        { label: 'upgrade', value: 'upgrade' },
        { label: 'reboot', value: 'reboot' },
        { label: 'resume', value: 'resume' },
        { label: 'suspend', value: 'suspend' }
    ]}
>
<TabItem value="list_worker_pools">

Get all worker pools of an App Service Environment. Description for Get all worker pools of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_worker_pools 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_worker_pool_skus">

Get available SKUs for scaling a worker pool. Description for Get available SKUs for scaling a worker pool.

```sql
EXEC azure.web.app_service_environments.list_worker_pool_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_pool_name='{{ worker_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_web_worker_usages">

Get usage metrics for a worker pool of an App Service Environment. Description for Get usage metrics for a worker pool of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_web_worker_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_pool_name='{{ worker_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_capacities">

Get the used, available, and total worker capacity an App Service Environment. Description for Get the used, available, and total worker capacity an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_capacities 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_diagnostics">

Get diagnostic information for an App Service Environment. Description for Get diagnostic information for an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_diagnostics 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_operations">

List all currently running operations on the App Service Environment. Description for List all currently running operations on the App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_operations 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_app_service_plans">

Get all App Service plans in an App Service Environment. Description for Get all App Service plans in an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_app_service_plans 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_web_apps">

Get all apps in an App Service Environment. Description for Get all apps in an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_web_apps 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@propertiesToInclude='{{ propertiesToInclude }}'
;
```
</TabItem>
<TabItem value="list_usages">

Get global usage metrics of an App Service Environment. Description for Get global usage metrics of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_multi_role_pools">

Get all multi-role pools. Description for Get all multi-role pools.

```sql
EXEC azure.web.app_service_environments.list_multi_role_pools 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_multi_role_metric_definitions">

Get metric definitions for a multi-role pool of an App Service Environment. Description for Get metric definitions for a multi-role pool of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_multi_role_metric_definitions 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_multi_role_pool_skus">

Get available SKUs for scaling a multi-role pool. Description for Get available SKUs for scaling a multi-role pool.

```sql
EXEC azure.web.app_service_environments.list_multi_role_pool_skus 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_multi_role_usages">

Get usage metrics for a multi-role pool of an App Service Environment. Description for Get usage metrics for a multi-role pool of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.list_multi_role_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_worker_pool">

Get properties of a worker pool. Description for Get properties of a worker pool.

```sql
EXEC azure.web.app_service_environments.get_worker_pool 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_pool_name='{{ worker_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_worker_pool">

Create or update a worker pool. Description for Create or update a worker pool.

```sql
EXEC azure.web.app_service_environments.create_or_update_worker_pool 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_pool_name='{{ worker_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"sku": "{{ sku }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_worker_pool">

Create or update a worker pool. Description for Create or update a worker pool.

```sql
EXEC azure.web.app_service_environments.update_worker_pool 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@worker_pool_name='{{ worker_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"sku": "{{ sku }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_inbound_network_dependencies_endpoints">

Get the network endpoints of all inbound dependencies of an App Service Environment. Description for Get the network endpoints of all inbound dependencies of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.get_inbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_outbound_network_dependencies_endpoints">

Get the network endpoints of all outbound dependencies of an App Service Environment. Description for Get the network endpoints of all outbound dependencies of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.get_outbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_link_resources">

Gets the private link resources. Description for Gets the private link resources.

```sql
EXEC azure.web.app_service_environments.get_private_link_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_vip_info">

Get IP addresses assigned to an App Service Environment. Description for Get IP addresses assigned to an App Service Environment.

```sql
EXEC azure.web.app_service_environments.get_vip_info 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_ase_custom_dns_suffix_configuration">

Get Custom Dns Suffix configuration of an App Service Environment. Get Custom Dns Suffix configuration of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.get_ase_custom_dns_suffix_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_ase_custom_dns_suffix_configuration">

Update Custom Dns Suffix configuration of an App Service Environment. Update Custom Dns Suffix configuration of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.update_ase_custom_dns_suffix_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_ase_custom_dns_suffix_configuration">

Delete Custom Dns Suffix configuration of an App Service Environment. Delete Custom Dns Suffix configuration of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.delete_ase_custom_dns_suffix_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_ase_v3_networking_configuration">

Get networking configuration of an App Service Environment. Description for Get networking configuration of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.get_ase_v3_networking_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_ase_networking_configuration">

Update networking configuration of an App Service Environment. Description for Update networking configuration of an App Service Environment.

```sql
EXEC azure.web.app_service_environments.update_ase_networking_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_multi_role_pool">

Get properties of a multi-role pool. Description for Get properties of a multi-role pool.

```sql
EXEC azure.web.app_service_environments.get_multi_role_pool 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_multi_role_pool">

Create or update a multi-role pool. Description for Create or update a multi-role pool.

```sql
EXEC azure.web.app_service_environments.create_or_update_multi_role_pool 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"sku": "{{ sku }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_multi_role_pool">

Create or update a multi-role pool. Description for Create or update a multi-role pool.

```sql
EXEC azure.web.app_service_environments.update_multi_role_pool 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"sku": "{{ sku }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="approve_or_reject_private_endpoint_connection">

Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.

```sql
EXEC azure.web.app_service_environments.approve_or_reject_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_private_endpoint_connection">

Deletes a private endpoint connection. Description for Deletes a private endpoint connection.

```sql
EXEC azure.web.app_service_environments.delete_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection_list">

Gets the list of private endpoints associated with a hosting environment. Description for Gets the list of private endpoints associated with a hosting environment.

```sql
EXEC azure.web.app_service_environments.get_private_endpoint_connection_list 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="change_vnet">

Move an App Service Environment to a different VNET. Description for Move an App Service Environment to a different VNET.

```sql
EXEC azure.web.app_service_environments.change_vnet 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"subnet": "{{ subnet }}"
}'
;
```
</TabItem>
<TabItem value="test_upgrade_available_notification">

Send a test notification that an upgrade is available for this App Service Environment. Send a test notification that an upgrade is available for this App Service Environment.

```sql
EXEC azure.web.app_service_environments.test_upgrade_available_notification 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="upgrade">

Initiate an upgrade of an App Service Environment if one is available. Description for Initiate an upgrade of an App Service Environment if one is available.

```sql
EXEC azure.web.app_service_environments.upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reboot">

Reboot all machines in an App Service Environment. Description for Reboot all machines in an App Service Environment.

```sql
EXEC azure.web.app_service_environments.reboot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resume an App Service Environment. Description for Resume an App Service Environment.

```sql
EXEC azure.web.app_service_environments.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="suspend">

Suspend an App Service Environment. Description for Suspend an App Service Environment.

```sql
EXEC azure.web.app_service_environments.suspend 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
