--- 
title: sap_virtual_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_virtual_instances
  - workloads_sap_virtual_instance
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sap_virtual_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sap_virtual_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.workloads_sap_virtual_instance.sap_virtual_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_sizing_recommendations"
    values={[
        { label: 'get_sizing_recommendations', value: 'get_sizing_recommendations' },
        { label: 'get_disk_configurations', value: 'get_disk_configurations' },
        { label: 'get_sap_supported_sku', value: 'get_sap_supported_sku' },
        { label: 'get_availability_zone_details', value: 'get_availability_zone_details' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_sizing_recommendations">

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
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type. Eg: SingleServer/ThreeTier. Required. Known values are: "SingleServer" and "ThreeTier".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_disk_configurations">

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
    <td><CopyableCode code="volumeConfigurations" /></td>
    <td><code>object</code></td>
    <td>The disk configuration for the db volume. For HANA, Required volumes are: ['hana/data', 'hana/log', hana/shared', 'usr/sap', 'os'], Optional volume : ['backup'].</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_sap_supported_sku">

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
    <td><CopyableCode code="supportedSkus" /></td>
    <td><code>array</code></td>
    <td>Gets the list of SAP supported SKUs.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_availability_zone_details">

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
    <td><CopyableCode code="availabilityZonePairs" /></td>
    <td><code>array</code></td>
    <td>Gets the list of availability zone pairs.</td>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Defines if the SAP system is being created using Azure Center for SAP solutions (ACSS) or if an existing SAP system is being registered with ACSS. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Defines the environment type - Production/Non Production. Required. Known values are: "NonProd" and "Prod". (NonProd, Prod)</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Indicates any errors on the Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Defines the health of SAP Instances. Known values are: "Unknown", "Healthy", "Unhealthy", and "Degraded". (Unknown, Healthy, Unhealthy, Degraded)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourcesNetworkAccessType" /></td>
    <td><code>string</code></td>
    <td>Specifies the network access configuration for the resources that will be deployed in the Managed Resource Group. The options to choose from are Public and Private. If 'Private' is chosen, the Storage Account service tag should be enabled on the subnets in which the SAP VMs exist. This is required for establishing connectivity between VM extensions and the managed resource group storage account. This setting is currently applicable only to Storage Account. Learn more here `https://go.microsoft.com/fwlink/?linkid=2247228 `_. Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", "Failed", "Deleting", and "Canceled". (Succeeded, Updating, Creating, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sapProduct" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Product type. Required. Known values are: "ECC", "S4HANA", and "Other". (ECC, S4HANA, Other)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Defines the Virtual Instance for SAP state. Known values are: "InfrastructureDeploymentPending", "InfrastructureDeploymentInProgress", "InfrastructureDeploymentFailed", "SoftwareInstallationPending", "SoftwareInstallationInProgress", "SoftwareInstallationFailed", "SoftwareDetectionInProgress", "SoftwareDetectionFailed", "DiscoveryPending", "DiscoveryInProgress", "DiscoveryFailed", "RegistrationComplete", and "ACSSInstallationBlocked". (InfrastructureDeploymentPending, InfrastructureDeploymentInProgress, InfrastructureDeploymentFailed, SoftwareInstallationPending, SoftwareInstallationInProgress, SoftwareInstallationFailed, SoftwareDetectionInProgress, SoftwareDetectionFailed, DiscoveryPending, DiscoveryInProgress, DiscoveryFailed, RegistrationComplete, ACSSInstallationBlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Instance status. Known values are: "Starting", "Running", "Stopping", "Offline", "PartiallyRunning", "Unavailable", and "SoftShutdown". (Starting, Running, Stopping, Offline, PartiallyRunning, Unavailable, SoftShutdown)</td>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Defines if the SAP system is being created using Azure Center for SAP solutions (ACSS) or if an existing SAP system is being registered with ACSS. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Defines the environment type - Production/Non Production. Required. Known values are: "NonProd" and "Prod". (NonProd, Prod)</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Indicates any errors on the Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Defines the health of SAP Instances. Known values are: "Unknown", "Healthy", "Unhealthy", and "Degraded". (Unknown, Healthy, Unhealthy, Degraded)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourcesNetworkAccessType" /></td>
    <td><code>string</code></td>
    <td>Specifies the network access configuration for the resources that will be deployed in the Managed Resource Group. The options to choose from are Public and Private. If 'Private' is chosen, the Storage Account service tag should be enabled on the subnets in which the SAP VMs exist. This is required for establishing connectivity between VM extensions and the managed resource group storage account. This setting is currently applicable only to Storage Account. Learn more here `https://go.microsoft.com/fwlink/?linkid=2247228 `_. Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", "Failed", "Deleting", and "Canceled". (Succeeded, Updating, Creating, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sapProduct" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Product type. Required. Known values are: "ECC", "S4HANA", and "Other". (ECC, S4HANA, Other)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Defines the Virtual Instance for SAP state. Known values are: "InfrastructureDeploymentPending", "InfrastructureDeploymentInProgress", "InfrastructureDeploymentFailed", "SoftwareInstallationPending", "SoftwareInstallationInProgress", "SoftwareInstallationFailed", "SoftwareDetectionInProgress", "SoftwareDetectionFailed", "DiscoveryPending", "DiscoveryInProgress", "DiscoveryFailed", "RegistrationComplete", and "ACSSInstallationBlocked". (InfrastructureDeploymentPending, InfrastructureDeploymentInProgress, InfrastructureDeploymentFailed, SoftwareInstallationPending, SoftwareInstallationInProgress, SoftwareInstallationFailed, SoftwareDetectionInProgress, SoftwareDetectionFailed, DiscoveryPending, DiscoveryInProgress, DiscoveryFailed, RegistrationComplete, ACSSInstallationBlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Instance status. Known values are: "Starting", "Running", "Stopping", "Offline", "PartiallyRunning", "Unavailable", and "SoftShutdown". (Starting, Running, Stopping, Offline, PartiallyRunning, Unavailable, SoftShutdown)</td>
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
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>Defines if the SAP system is being created using Azure Center for SAP solutions (ACSS) or if an existing SAP system is being registered with ACSS. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Defines the environment type - Production/Non Production. Required. Known values are: "NonProd" and "Prod". (NonProd, Prod)</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Indicates any errors on the Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Defines the health of SAP Instances. Known values are: "Unknown", "Healthy", "Unhealthy", and "Degraded". (Unknown, Healthy, Unhealthy, Degraded)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourcesNetworkAccessType" /></td>
    <td><code>string</code></td>
    <td>Specifies the network access configuration for the resources that will be deployed in the Managed Resource Group. The options to choose from are Public and Private. If 'Private' is chosen, the Storage Account service tag should be enabled on the subnets in which the SAP VMs exist. This is required for establishing connectivity between VM extensions and the managed resource group storage account. This setting is currently applicable only to Storage Account. Learn more here `https://go.microsoft.com/fwlink/?linkid=2247228 `_. Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", "Failed", "Deleting", and "Canceled". (Succeeded, Updating, Creating, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sapProduct" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Product type. Required. Known values are: "ECC", "S4HANA", and "Other". (ECC, S4HANA, Other)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Defines the Virtual Instance for SAP state. Known values are: "InfrastructureDeploymentPending", "InfrastructureDeploymentInProgress", "InfrastructureDeploymentFailed", "SoftwareInstallationPending", "SoftwareInstallationInProgress", "SoftwareInstallationFailed", "SoftwareDetectionInProgress", "SoftwareDetectionFailed", "DiscoveryPending", "DiscoveryInProgress", "DiscoveryFailed", "RegistrationComplete", and "ACSSInstallationBlocked". (InfrastructureDeploymentPending, InfrastructureDeploymentInProgress, InfrastructureDeploymentFailed, SoftwareInstallationPending, SoftwareInstallationInProgress, SoftwareInstallationFailed, SoftwareDetectionInProgress, SoftwareDetectionFailed, DiscoveryPending, DiscoveryInProgress, DiscoveryFailed, RegistrationComplete, ACSSInstallationBlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Instance status. Known values are: "Starting", "Running", "Stopping", "Offline", "PartiallyRunning", "Unavailable", and "SoftShutdown". (Starting, Running, Stopping, Offline, PartiallyRunning, Unavailable, SoftShutdown)</td>
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
    <td><a href="#get_sizing_recommendations"><CopyableCode code="get_sizing_recommendations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the sizing recommendations.</td>
</tr>
<tr>
    <td><a href="#get_disk_configurations"><CopyableCode code="get_disk_configurations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the SAP Disk Configuration Layout prod/non-prod SAP System.</td>
</tr>
<tr>
    <td><a href="#get_sap_supported_sku"><CopyableCode code="get_sap_supported_sku" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of SAP supported SKUs for ASCS, Application and Database tier.</td>
</tr>
<tr>
    <td><a href="#get_availability_zone_details"><CopyableCode code="get_availability_zone_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the recommended SAP Availability Zone Pair Details for your region.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all Virtual Instances for SAP solutions resources in a Resource Group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all Virtual Instances for SAP solutions resources in a Subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a Virtual Instance for SAP solutions (VIS) resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Virtual Instance for SAP solutions resource and its child resources, that is the associated Central Services Instance, Application Server Instances and Database Instance.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts the SAP application, that is the Central Services instance and Application server instances.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops the SAP Application, that is the Application server instances and Central Services instance.</td>
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
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sap_virtual_instance_name">
    <td><CopyableCode code="sap_virtual_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Virtual Instances for SAP solutions resource. Required.</td>
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
    defaultValue="get_sizing_recommendations"
    values={[
        { label: 'get_sizing_recommendations', value: 'get_sizing_recommendations' },
        { label: 'get_disk_configurations', value: 'get_disk_configurations' },
        { label: 'get_sap_supported_sku', value: 'get_sap_supported_sku' },
        { label: 'get_availability_zone_details', value: 'get_availability_zone_details' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_sizing_recommendations">

Gets the sizing recommendations.

```sql
SELECT
deploymentType
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_disk_configurations">

Get the SAP Disk Configuration Layout prod/non-prod SAP System.

```sql
SELECT
volumeConfigurations
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_sap_supported_sku">

Get a list of SAP supported SKUs for ASCS, Application and Database tier.

```sql
SELECT
supportedSkus
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_availability_zone_details">

Get the recommended SAP Availability Zone Pair Details for your region.

```sql
SELECT
availabilityZonePairs
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a Virtual Instance for SAP solutions resource.

```sql
SELECT
id,
name,
configuration,
environment,
errors,
health,
identity,
location,
managedResourceGroupConfiguration,
managedResourcesNetworkAccessType,
provisioningState,
sapProduct,
state,
status,
systemData,
tags,
type
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all Virtual Instances for SAP solutions resources in a Resource Group.

```sql
SELECT
id,
name,
configuration,
environment,
errors,
health,
identity,
location,
managedResourceGroupConfiguration,
managedResourcesNetworkAccessType,
provisioningState,
sapProduct,
state,
status,
systemData,
tags,
type
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all Virtual Instances for SAP solutions resources in a Subscription.

```sql
SELECT
id,
name,
configuration,
environment,
errors,
health,
identity,
location,
managedResourceGroupConfiguration,
managedResourcesNetworkAccessType,
provisioningState,
sapProduct,
state,
status,
systemData,
tags,
type
FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates a Virtual Instance for SAP solutions (VIS) resource.

```sql
INSERT INTO azure_isv.workloads_sap_virtual_instance.sap_virtual_instances (
tags,
location,
properties,
identity,
resource_group_name,
sap_virtual_instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ sap_virtual_instance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: sap_virtual_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sap_virtual_instances resource.
    - name: sap_virtual_instance_name
      value: "{{ sap_virtual_instance_name }}"
      description: Required parameter for the sap_virtual_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sap_virtual_instances resource.
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
        The resource-specific properties for this resource.
      value:
        environment: "{{ environment }}"
        sapProduct: "{{ sapProduct }}"
        managedResourcesNetworkAccessType: "{{ managedResourcesNetworkAccessType }}"
        configuration:
          configurationType: "{{ configurationType }}"
        managedResourceGroupConfiguration:
          name: "{{ name }}"
        status: "{{ status }}"
        health: "{{ health }}"
        state: "{{ state }}"
        provisioningState: "{{ provisioningState }}"
        errors:
          properties:
            code: "{{ code }}"
            message: "{{ message }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                details: "{{ details }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
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

Updates a Virtual Instance for SAP solutions resource.

```sql
UPDATE azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Deletes a Virtual Instance for SAP solutions resource and its child resources, that is the associated Central Services Instance, Application Server Instances and Database Instance.

```sql
DELETE FROM azure_isv.workloads_sap_virtual_instance.sap_virtual_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Starts the SAP application, that is the Central Services instance and Application server instances.

```sql
EXEC azure_isv.workloads_sap_virtual_instance.sap_virtual_instances.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@sap_virtual_instance_name='{{ sap_virtual_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startVm": {{ startVm }}
}'
;
```
</TabItem>
<TabItem value="stop">

Stops the SAP Application, that is the Application server instances and Central Services instance.

```sql
EXEC azure_isv.workloads_sap_virtual_instance.sap_virtual_instances.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@sap_virtual_instance_name='{{ sap_virtual_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"softStopTimeoutSeconds": {{ softStopTimeoutSeconds }}, 
"deallocateVm": {{ deallocateVm }}
}'
;
```
</TabItem>
</Tabs>
