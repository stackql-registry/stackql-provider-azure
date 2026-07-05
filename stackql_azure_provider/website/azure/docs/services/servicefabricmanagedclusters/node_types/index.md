--- 
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
  - servicefabricmanagedclusters
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

Creates, updates, deletes, gets or lists a <code>node_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabricmanagedclusters.node_types" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_clusters', value: 'list_by_managed_clusters' }
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
    <td><CopyableCode code="additionalDataDisks" /></td>
    <td><code>array</code></td>
    <td>Additional managed data disks.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalNetworkInterfaceConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the settings for any additional secondary network interfaces to attach to the node type.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPorts" /></td>
    <td><code>object</code></td>
    <td>The range of ports from which cluster assigned port to Service Fabric applications.</td>
</tr>
<tr>
    <td><CopyableCode code="capacities" /></td>
    <td><code>object</code></td>
    <td>The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.</td>
</tr>
<tr>
    <td><CopyableCode code="computerNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Specifies the computer name prefix. Limited to 9 characters. If specified, allows for a longer name to be specified for the node type name.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskLetter" /></td>
    <td><code>string</code></td>
    <td>Managed data disk letter. It can not use the reserved letter C or D and it can not change after created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>Disk size for the managed disk attached to the vms on the node type in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskType" /></td>
    <td><code>string</code></td>
    <td>Managed data disk type. Specifies the storage account type for the managed disk. Known values are: "Standard_LRS", "StandardSSD_LRS", "Premium_LRS", "PremiumV2_LRS", "StandardSSD_ZRS", and "Premium_ZRS". (Standard_LRS, StandardSSD_LRS, Premium_LRS, PremiumV2_LRS, StandardSSD_ZRS, Premium_ZRS)</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource id of the DSCP configuration to apply to the node type network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the network interface is accelerated networking-enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableEncryptionAtHost" /></td>
    <td><code>boolean</code></td>
    <td>Enable or disable the Host Encryption for the virtual machines on the node type. This will enable the encryption for all the disks including Resource/Temp disk at host itself. Default: The Encryption at host will be disabled unless this property is set to true for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNodePublicIP" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether each node is allocated its own public IPv4 address. This is only supported on secondary node types with custom Load Balancers.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNodePublicIPv6" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether each node is allocated its own public IPv6 address. This is only supported on secondary node types with custom Load Balancers.</td>
</tr>
<tr>
    <td><CopyableCode code="enableOverProvisioning" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the node type should be overprovisioned. It is only allowed for stateless node types.</td>
</tr>
<tr>
    <td><CopyableCode code="enableResilientEphemeralOsDisk" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the node type should use a resilient ephemeral OS disk when using a supported SKU size. A resilient ephemeral OS disk provides improved reliability for ephemeral OS disks by enabling full caching.</td>
</tr>
<tr>
    <td><CopyableCode code="ephemeralPorts" /></td>
    <td><code>object</code></td>
    <td>The range of ephemeral ports that nodes in this node type should be configured with.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Specifies the eviction policy for virtual machines in a SPOT node type. Default is Delete. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="frontendConfigurations" /></td>
    <td><code>array</code></td>
    <td>Indicates the node type uses its own frontend configurations instead of the default one for the cluster. This setting can only be specified for non-primary node types and can not be added or removed after the node type is created.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroupId" /></td>
    <td><code>string</code></td>
    <td>Specifies the full host group resource Id. This property is used for deploying on azure dedicated hosts.</td>
</tr>
<tr>
    <td><CopyableCode code="isOutboundOnly" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the node type should be configured for only outbound traffic and not inbound traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrimary" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the Service Fabric system services for the cluster will run on this node type. This setting cannot be changed once the node type is created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isSpotVM" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the node type will be Spot Virtual Machines. Azure will allocate the VMs if there is capacity available and the VMs can be evicted at any time.</td>
</tr>
<tr>
    <td><CopyableCode code="isStateless" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the node type can only host Stateless workloads.</td>
</tr>
<tr>
    <td><CopyableCode code="multiplePlacementGroups" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if scale set associated with the node type can be composed of multiple placement groups.</td>
</tr>
<tr>
    <td><CopyableCode code="natConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the NAT configuration on default public Load Balancer for the node type. This is only supported for node types use the default public Load Balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="natGatewayId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource id of a NAT Gateway to attach to the subnet of this node type. Node type must use custom load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityRules" /></td>
    <td><code>array</code></td>
    <td>The Network Security Rules for this node type. This setting can only be specified for node types that are configured with frontend configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="placementProperties" /></td>
    <td><code>object</code></td>
    <td>The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the node type resource. Known values are: "None", "Creating", "Created", "Updating", "Succeeded", "Failed", "Canceled", "Deleting", "Deleted", and "Other". (None, Creating, Created, Updating, Succeeded, Failed, Canceled, Deleting, Deleted, Other)</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAgentSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies the settings for the proxy agent on the node type.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleInPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the scale in policy for the node type, which will be used when scale in happens on the cluster. If not specified, the default is Default which means the platform will decide which nodes to remove during scale in.</td>
</tr>
<tr>
    <td><CopyableCode code="secureBootEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether secure boot should be enabled on the nodeType. Can only be used with TrustedLaunch and ConfidentialVM SecurityType.</td>
</tr>
<tr>
    <td><CopyableCode code="securityEncryptionType" /></td>
    <td><code>string</code></td>
    <td>Specifies the EncryptionType of the managed disk. It is set to DiskWithVMGuestState for encryption of the managed disk along with VMGuestState blob and VMGuestStateOnly for encryption of just the VMGuestState blob. Note: It can be set for only Confidential VMs. Known values are: "DiskWithVMGuestState" and "VMGuestStateOnly". (DiskWithVMGuestState, VMGuestStateOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="securityType" /></td>
    <td><code>string</code></td>
    <td>Specifies the security type of the nodeType. Supported values include Standard, TrustedLaunch and ConfidentialVM. Known values are: "TrustedLaunch", "Standard", and "ConfidentialVM". (TrustedLaunch, Standard, ConfidentialVM)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceArtifactReferenceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the service artifact reference id used to set same image version for all virtual machines in the scale set when using 'latest' image version.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The node type sku.</td>
</tr>
<tr>
    <td><CopyableCode code="spotRestoreTimeout" /></td>
    <td><code>string</code></td>
    <td>Indicates the time duration after which the platform will not try to restore the VMSS SPOT instances specified as ISO 8601.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Indicates the resource id of the subnet for the node type.</td>
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
    <td><CopyableCode code="useDefaultPublicLoadBalancer" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the use public load balancer. If not specified and the node type doesn't have its own frontend configuration, it will be attached to the default load balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is true, then the frontend has to be an Internal Load Balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is false or not set, then the custom load balancer must include a public load balancer to provide outbound connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="useEphemeralOSDisk" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to use ephemeral os disk. The sku selected on the vmSize property needs to support this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="useTempDataDisk" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to use the temporary disk for the service fabric data root, in which case no managed data disk will be attached and the temporary disk will be used. It is only allowed for stateless node types.</td>
</tr>
<tr>
    <td><CopyableCode code="vmApplications" /></td>
    <td><code>array</code></td>
    <td>Specifies the gallery applications that should be made available to the underlying VMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="vmExtensions" /></td>
    <td><code>array</code></td>
    <td>Set of extensions that should be installed onto the virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageOffer" /></td>
    <td><code>string</code></td>
    <td>The offer type of the Azure Virtual Machines Marketplace image. For example, UbuntuServer or WindowsServer.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImagePlan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click Want to deploy programmatically, Get Started -&gt;. Enter any required information and then click Save.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImagePublisher" /></td>
    <td><code>string</code></td>
    <td>The publisher of the Azure Virtual Machines Marketplace image. For example, Canonical or MicrosoftWindowsServer.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageResourceId" /></td>
    <td><code>string</code></td>
    <td>Indicates the resource id of the vm image. This parameter is used for custom vm image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageSku" /></td>
    <td><code>string</code></td>
    <td>The SKU of the Azure Virtual Machines Marketplace image. For example, 14.04.0-LTS or 2012-R2-Datacenter.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Azure Virtual Machines Marketplace image. A value of 'latest' can be specified to select the latest version of an image. If omitted, the default is 'latest'.</td>
</tr>
<tr>
    <td><CopyableCode code="vmInstanceCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the node type. **Values:** -1 - Use when auto scale rules are configured or sku.capacity is defined 0 - Not supported &gt;0 - Use for manual scale. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmManagedIdentity" /></td>
    <td><code>object</code></td>
    <td>Identities to assign to the virtual machine scale set under the node type.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSecrets" /></td>
    <td><code>array</code></td>
    <td>The secrets to install in the virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSetupActions" /></td>
    <td><code>array</code></td>
    <td>Specifies the actions to be performed on the vms before bootstrapping the service fabric runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSharedGalleryImageId" /></td>
    <td><code>string</code></td>
    <td>Indicates the resource id of the vm shared galleries image. This parameter is used for custom vm image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the pool. All virtual machines in a pool are the same size. For example, Standard_D3.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneBalance" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true allows stateless node types to scale out without equal distribution across zones.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Specifies the availability zones where the node type would span across. If the cluster is not spanning across availability zones, initiates az migration for the cluster.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_managed_clusters">

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
    <td><CopyableCode code="additionalDataDisks" /></td>
    <td><code>array</code></td>
    <td>Additional managed data disks.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalNetworkInterfaceConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the settings for any additional secondary network interfaces to attach to the node type.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPorts" /></td>
    <td><code>object</code></td>
    <td>The range of ports from which cluster assigned port to Service Fabric applications.</td>
</tr>
<tr>
    <td><CopyableCode code="capacities" /></td>
    <td><code>object</code></td>
    <td>The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.</td>
</tr>
<tr>
    <td><CopyableCode code="computerNamePrefix" /></td>
    <td><code>string</code></td>
    <td>Specifies the computer name prefix. Limited to 9 characters. If specified, allows for a longer name to be specified for the node type name.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskLetter" /></td>
    <td><code>string</code></td>
    <td>Managed data disk letter. It can not use the reserved letter C or D and it can not change after created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>Disk size for the managed disk attached to the vms on the node type in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskType" /></td>
    <td><code>string</code></td>
    <td>Managed data disk type. Specifies the storage account type for the managed disk. Known values are: "Standard_LRS", "StandardSSD_LRS", "Premium_LRS", "PremiumV2_LRS", "StandardSSD_ZRS", and "Premium_ZRS". (Standard_LRS, StandardSSD_LRS, Premium_LRS, PremiumV2_LRS, StandardSSD_ZRS, Premium_ZRS)</td>
</tr>
<tr>
    <td><CopyableCode code="dscpConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource id of the DSCP configuration to apply to the node type network interface.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAcceleratedNetworking" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the network interface is accelerated networking-enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableEncryptionAtHost" /></td>
    <td><code>boolean</code></td>
    <td>Enable or disable the Host Encryption for the virtual machines on the node type. This will enable the encryption for all the disks including Resource/Temp disk at host itself. Default: The Encryption at host will be disabled unless this property is set to true for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNodePublicIP" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether each node is allocated its own public IPv4 address. This is only supported on secondary node types with custom Load Balancers.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNodePublicIPv6" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether each node is allocated its own public IPv6 address. This is only supported on secondary node types with custom Load Balancers.</td>
</tr>
<tr>
    <td><CopyableCode code="enableOverProvisioning" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the node type should be overprovisioned. It is only allowed for stateless node types.</td>
</tr>
<tr>
    <td><CopyableCode code="enableResilientEphemeralOsDisk" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the node type should use a resilient ephemeral OS disk when using a supported SKU size. A resilient ephemeral OS disk provides improved reliability for ephemeral OS disks by enabling full caching.</td>
</tr>
<tr>
    <td><CopyableCode code="ephemeralPorts" /></td>
    <td><code>object</code></td>
    <td>The range of ephemeral ports that nodes in this node type should be configured with.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Specifies the eviction policy for virtual machines in a SPOT node type. Default is Delete. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="frontendConfigurations" /></td>
    <td><code>array</code></td>
    <td>Indicates the node type uses its own frontend configurations instead of the default one for the cluster. This setting can only be specified for non-primary node types and can not be added or removed after the node type is created.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroupId" /></td>
    <td><code>string</code></td>
    <td>Specifies the full host group resource Id. This property is used for deploying on azure dedicated hosts.</td>
</tr>
<tr>
    <td><CopyableCode code="isOutboundOnly" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the node type should be configured for only outbound traffic and not inbound traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrimary" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the Service Fabric system services for the cluster will run on this node type. This setting cannot be changed once the node type is created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isSpotVM" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the node type will be Spot Virtual Machines. Azure will allocate the VMs if there is capacity available and the VMs can be evicted at any time.</td>
</tr>
<tr>
    <td><CopyableCode code="isStateless" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the node type can only host Stateless workloads.</td>
</tr>
<tr>
    <td><CopyableCode code="multiplePlacementGroups" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if scale set associated with the node type can be composed of multiple placement groups.</td>
</tr>
<tr>
    <td><CopyableCode code="natConfigurations" /></td>
    <td><code>array</code></td>
    <td>Specifies the NAT configuration on default public Load Balancer for the node type. This is only supported for node types use the default public Load Balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="natGatewayId" /></td>
    <td><code>string</code></td>
    <td>Specifies the resource id of a NAT Gateway to attach to the subnet of this node type. Node type must use custom load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityRules" /></td>
    <td><code>array</code></td>
    <td>The Network Security Rules for this node type. This setting can only be specified for node types that are configured with frontend configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="placementProperties" /></td>
    <td><code>object</code></td>
    <td>The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the node type resource. Known values are: "None", "Creating", "Created", "Updating", "Succeeded", "Failed", "Canceled", "Deleting", "Deleted", and "Other". (None, Creating, Created, Updating, Succeeded, Failed, Canceled, Deleting, Deleted, Other)</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAgentSettings" /></td>
    <td><code>object</code></td>
    <td>Specifies the settings for the proxy agent on the node type.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleInPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies the scale in policy for the node type, which will be used when scale in happens on the cluster. If not specified, the default is Default which means the platform will decide which nodes to remove during scale in.</td>
</tr>
<tr>
    <td><CopyableCode code="secureBootEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether secure boot should be enabled on the nodeType. Can only be used with TrustedLaunch and ConfidentialVM SecurityType.</td>
</tr>
<tr>
    <td><CopyableCode code="securityEncryptionType" /></td>
    <td><code>string</code></td>
    <td>Specifies the EncryptionType of the managed disk. It is set to DiskWithVMGuestState for encryption of the managed disk along with VMGuestState blob and VMGuestStateOnly for encryption of just the VMGuestState blob. Note: It can be set for only Confidential VMs. Known values are: "DiskWithVMGuestState" and "VMGuestStateOnly". (DiskWithVMGuestState, VMGuestStateOnly)</td>
</tr>
<tr>
    <td><CopyableCode code="securityType" /></td>
    <td><code>string</code></td>
    <td>Specifies the security type of the nodeType. Supported values include Standard, TrustedLaunch and ConfidentialVM. Known values are: "TrustedLaunch", "Standard", and "ConfidentialVM". (TrustedLaunch, Standard, ConfidentialVM)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceArtifactReferenceId" /></td>
    <td><code>string</code></td>
    <td>Specifies the service artifact reference id used to set same image version for all virtual machines in the scale set when using 'latest' image version.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The node type sku.</td>
</tr>
<tr>
    <td><CopyableCode code="spotRestoreTimeout" /></td>
    <td><code>string</code></td>
    <td>Indicates the time duration after which the platform will not try to restore the VMSS SPOT instances specified as ISO 8601.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Indicates the resource id of the subnet for the node type.</td>
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
    <td><CopyableCode code="useDefaultPublicLoadBalancer" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the use public load balancer. If not specified and the node type doesn't have its own frontend configuration, it will be attached to the default load balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is true, then the frontend has to be an Internal Load Balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is false or not set, then the custom load balancer must include a public load balancer to provide outbound connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="useEphemeralOSDisk" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether to use ephemeral os disk. The sku selected on the vmSize property needs to support this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="useTempDataDisk" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to use the temporary disk for the service fabric data root, in which case no managed data disk will be attached and the temporary disk will be used. It is only allowed for stateless node types.</td>
</tr>
<tr>
    <td><CopyableCode code="vmApplications" /></td>
    <td><code>array</code></td>
    <td>Specifies the gallery applications that should be made available to the underlying VMSS.</td>
</tr>
<tr>
    <td><CopyableCode code="vmExtensions" /></td>
    <td><code>array</code></td>
    <td>Set of extensions that should be installed onto the virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageOffer" /></td>
    <td><code>string</code></td>
    <td>The offer type of the Azure Virtual Machines Marketplace image. For example, UbuntuServer or WindowsServer.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImagePlan" /></td>
    <td><code>object</code></td>
    <td>Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use. In the Azure portal, find the marketplace image that you want to use and then click Want to deploy programmatically, Get Started -&gt;. Enter any required information and then click Save.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImagePublisher" /></td>
    <td><code>string</code></td>
    <td>The publisher of the Azure Virtual Machines Marketplace image. For example, Canonical or MicrosoftWindowsServer.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageResourceId" /></td>
    <td><code>string</code></td>
    <td>Indicates the resource id of the vm image. This parameter is used for custom vm image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageSku" /></td>
    <td><code>string</code></td>
    <td>The SKU of the Azure Virtual Machines Marketplace image. For example, 14.04.0-LTS or 2012-R2-Datacenter.</td>
</tr>
<tr>
    <td><CopyableCode code="vmImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the Azure Virtual Machines Marketplace image. A value of 'latest' can be specified to select the latest version of an image. If omitted, the default is 'latest'.</td>
</tr>
<tr>
    <td><CopyableCode code="vmInstanceCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the node type. **Values:** -1 - Use when auto scale rules are configured or sku.capacity is defined 0 - Not supported &gt;0 - Use for manual scale. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vmManagedIdentity" /></td>
    <td><code>object</code></td>
    <td>Identities to assign to the virtual machine scale set under the node type.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSecrets" /></td>
    <td><code>array</code></td>
    <td>The secrets to install in the virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSetupActions" /></td>
    <td><code>array</code></td>
    <td>Specifies the actions to be performed on the vms before bootstrapping the service fabric runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSharedGalleryImageId" /></td>
    <td><code>string</code></td>
    <td>Indicates the resource id of the vm shared galleries image. This parameter is used for custom vm image.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the pool. All virtual machines in a pool are the same size. For example, Standard_D3.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneBalance" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true allows stateless node types to scale out without equal distribution across zones.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>Specifies the availability zones where the node type would span across. If the cluster is not spanning across availability zones, initiates az migration for the cluster.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Service Fabric node type of a given managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_managed_clusters"><CopyableCode code="list_by_managed_clusters" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all Node types of the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Service Fabric node type of a given managed cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the configuration of a node type of a given managed cluster, only updating tags or capacity.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Service Fabric node type of a given managed cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Service Fabric node type of a given managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_fault_simulation"><CopyableCode code="list_fault_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of recent fault simulations for the node type.</td>
</tr>
<tr>
    <td><a href="#get_fault_simulation"><CopyableCode code="get_fault_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-simulationId"><code>simulationId</code></a></td>
    <td></td>
    <td>Gets a fault simulation by the simulationId.</td>
</tr>
<tr>
    <td><a href="#deallocate"><CopyableCode code="deallocate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deallocates one or more nodes on the node type. It will disable the fabric nodes, trigger a shutdown on the VMs and release them from the cluster.</td>
</tr>
<tr>
    <td><a href="#delete_node"><CopyableCode code="delete_node" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes one or more nodes on the node type. It will disable the fabric nodes, trigger a delete on the VMs and removes the state from the cluster.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Redeploys one or more nodes on the node type. It will disable the fabric nodes, trigger a shut down on the VMs, move them to a new node, and power them back on.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts one or more nodes on the node type. It will trigger an allocation of the fabric node if needed and activate them.</td>
</tr>
<tr>
    <td><a href="#start_fault_simulation"><CopyableCode code="start_fault_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-parameters"><code>parameters</code></a></td>
    <td></td>
    <td>Starts a fault simulation on the node type.</td>
</tr>
<tr>
    <td><a href="#stop_fault_simulation"><CopyableCode code="stop_fault_simulation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-node_type_name"><code>node_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-simulationId"><code>simulationId</code></a></td>
    <td></td>
    <td>Stops a fault simulation on the node type.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster resource. Required.</td>
</tr>
<tr id="parameter-node_type_name">
    <td><CopyableCode code="node_type_name" /></td>
    <td><code>string</code></td>
    <td>The name of the node type. Required.</td>
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
        { label: 'list_by_managed_clusters', value: 'list_by_managed_clusters' }
    ]}
>
<TabItem value="get">

Get a Service Fabric node type of a given managed cluster.

```sql
SELECT
id,
name,
additionalDataDisks,
additionalNetworkInterfaceConfigurations,
applicationPorts,
capacities,
computerNamePrefix,
dataDiskLetter,
dataDiskSizeGB,
dataDiskType,
dscpConfigurationId,
enableAcceleratedNetworking,
enableEncryptionAtHost,
enableNodePublicIP,
enableNodePublicIPv6,
enableOverProvisioning,
enableResilientEphemeralOsDisk,
ephemeralPorts,
evictionPolicy,
frontendConfigurations,
hostGroupId,
isOutboundOnly,
isPrimary,
isSpotVM,
isStateless,
multiplePlacementGroups,
natConfigurations,
natGatewayId,
networkSecurityRules,
placementProperties,
provisioningState,
proxyAgentSettings,
scaleInPolicy,
secureBootEnabled,
securityEncryptionType,
securityType,
serviceArtifactReferenceId,
sku,
spotRestoreTimeout,
subnetId,
systemData,
tags,
type,
useDefaultPublicLoadBalancer,
useEphemeralOSDisk,
useTempDataDisk,
vmApplications,
vmExtensions,
vmImageOffer,
vmImagePlan,
vmImagePublisher,
vmImageResourceId,
vmImageSku,
vmImageVersion,
vmInstanceCount,
vmManagedIdentity,
vmSecrets,
vmSetupActions,
vmSharedGalleryImageId,
vmSize,
zoneBalance,
zones
FROM azure.servicefabricmanagedclusters.node_types
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND node_type_name = '{{ node_type_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_managed_clusters">

Gets all Node types of the specified managed cluster.

```sql
SELECT
id,
name,
additionalDataDisks,
additionalNetworkInterfaceConfigurations,
applicationPorts,
capacities,
computerNamePrefix,
dataDiskLetter,
dataDiskSizeGB,
dataDiskType,
dscpConfigurationId,
enableAcceleratedNetworking,
enableEncryptionAtHost,
enableNodePublicIP,
enableNodePublicIPv6,
enableOverProvisioning,
enableResilientEphemeralOsDisk,
ephemeralPorts,
evictionPolicy,
frontendConfigurations,
hostGroupId,
isOutboundOnly,
isPrimary,
isSpotVM,
isStateless,
multiplePlacementGroups,
natConfigurations,
natGatewayId,
networkSecurityRules,
placementProperties,
provisioningState,
proxyAgentSettings,
scaleInPolicy,
secureBootEnabled,
securityEncryptionType,
securityType,
serviceArtifactReferenceId,
sku,
spotRestoreTimeout,
subnetId,
systemData,
tags,
type,
useDefaultPublicLoadBalancer,
useEphemeralOSDisk,
useTempDataDisk,
vmApplications,
vmExtensions,
vmImageOffer,
vmImagePlan,
vmImagePublisher,
vmImageResourceId,
vmImageSku,
vmImageVersion,
vmInstanceCount,
vmManagedIdentity,
vmSecrets,
vmSetupActions,
vmSharedGalleryImageId,
vmSize,
zoneBalance,
zones
FROM azure.servicefabricmanagedclusters.node_types
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
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

Create or update a Service Fabric node type of a given managed cluster.

```sql
INSERT INTO azure.servicefabricmanagedclusters.node_types (
properties,
tags,
sku,
resource_group_name,
cluster_name,
node_type_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ node_type_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: node_types
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the node_types resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the node_types resource.
    - name: node_type_name
      value: "{{ node_type_name }}"
      description: Required parameter for the node_types resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the node_types resource.
    - name: properties
      description: |
        The node type properties.
      value:
        isPrimary: {{ isPrimary }}
        vmInstanceCount: {{ vmInstanceCount }}
        dataDiskSizeGB: {{ dataDiskSizeGB }}
        dataDiskType: "{{ dataDiskType }}"
        dataDiskLetter: "{{ dataDiskLetter }}"
        placementProperties: "{{ placementProperties }}"
        capacities: "{{ capacities }}"
        applicationPorts:
          startPort: {{ startPort }}
          endPort: {{ endPort }}
        ephemeralPorts:
          startPort: {{ startPort }}
          endPort: {{ endPort }}
        vmSize: "{{ vmSize }}"
        vmImagePublisher: "{{ vmImagePublisher }}"
        vmImageOffer: "{{ vmImageOffer }}"
        vmImageSku: "{{ vmImageSku }}"
        vmImageVersion: "{{ vmImageVersion }}"
        vmSecrets:
          - sourceVault:
              id: "{{ id }}"
            vaultCertificates: "{{ vaultCertificates }}"
        vmExtensions:
          - name: "{{ name }}"
            properties:
              publisher: "{{ publisher }}"
              type: "{{ type }}"
              typeHandlerVersion: "{{ typeHandlerVersion }}"
              autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
              settings: "{{ settings }}"
              protectedSettings: "{{ protectedSettings }}"
              forceUpdateTag: "{{ forceUpdateTag }}"
              provisionAfterExtensions:
                - "{{ provisionAfterExtensions }}"
              provisioningState: "{{ provisioningState }}"
              enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
              setupOrder:
                - "{{ setupOrder }}"
        vmManagedIdentity:
          userAssignedIdentities:
            - "{{ userAssignedIdentities }}"
        isStateless: {{ isStateless }}
        multiplePlacementGroups: {{ multiplePlacementGroups }}
        frontendConfigurations:
          - ipAddressType: "{{ ipAddressType }}"
            loadBalancerBackendAddressPoolId: "{{ loadBalancerBackendAddressPoolId }}"
            loadBalancerInboundNatPoolId: "{{ loadBalancerInboundNatPoolId }}"
            applicationGatewayBackendAddressPoolId: "{{ applicationGatewayBackendAddressPoolId }}"
        networkSecurityRules:
          - name: "{{ name }}"
            description: "{{ description }}"
            protocol: "{{ protocol }}"
            sourceAddressPrefixes: "{{ sourceAddressPrefixes }}"
            destinationAddressPrefixes: "{{ destinationAddressPrefixes }}"
            sourcePortRanges: "{{ sourcePortRanges }}"
            destinationPortRanges: "{{ destinationPortRanges }}"
            sourceAddressPrefix: "{{ sourceAddressPrefix }}"
            destinationAddressPrefix: "{{ destinationAddressPrefix }}"
            sourcePortRange: "{{ sourcePortRange }}"
            destinationPortRange: "{{ destinationPortRange }}"
            access: "{{ access }}"
            priority: {{ priority }}
            direction: "{{ direction }}"
        additionalDataDisks:
          - lun: {{ lun }}
            diskSizeGB: {{ diskSizeGB }}
            diskType: "{{ diskType }}"
            diskLetter: "{{ diskLetter }}"
        enableEncryptionAtHost: {{ enableEncryptionAtHost }}
        provisioningState: "{{ provisioningState }}"
        enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
        useDefaultPublicLoadBalancer: {{ useDefaultPublicLoadBalancer }}
        useTempDataDisk: {{ useTempDataDisk }}
        enableOverProvisioning: {{ enableOverProvisioning }}
        zones:
          - "{{ zones }}"
        isSpotVM: {{ isSpotVM }}
        hostGroupId: "{{ hostGroupId }}"
        useEphemeralOSDisk: {{ useEphemeralOSDisk }}
        spotRestoreTimeout: "{{ spotRestoreTimeout }}"
        evictionPolicy: "{{ evictionPolicy }}"
        vmImageResourceId: "{{ vmImageResourceId }}"
        subnetId: "{{ subnetId }}"
        vmSetupActions:
          - "{{ vmSetupActions }}"
        securityType: "{{ securityType }}"
        securityEncryptionType: "{{ securityEncryptionType }}"
        secureBootEnabled: {{ secureBootEnabled }}
        enableNodePublicIP: {{ enableNodePublicIP }}
        enableNodePublicIPv6: {{ enableNodePublicIPv6 }}
        vmSharedGalleryImageId: "{{ vmSharedGalleryImageId }}"
        natGatewayId: "{{ natGatewayId }}"
        natConfigurations:
          - backendPort: {{ backendPort }}
            frontendPortRangeStart: {{ frontendPortRangeStart }}
            frontendPortRangeEnd: {{ frontendPortRangeEnd }}
        vmImagePlan:
          name: "{{ name }}"
          product: "{{ product }}"
          promotionCode: "{{ promotionCode }}"
          publisher: "{{ publisher }}"
        serviceArtifactReferenceId: "{{ serviceArtifactReferenceId }}"
        dscpConfigurationId: "{{ dscpConfigurationId }}"
        additionalNetworkInterfaceConfigurations:
          - name: "{{ name }}"
            enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
            dscpConfiguration:
              id: "{{ id }}"
            ipConfigurations: "{{ ipConfigurations }}"
        computerNamePrefix: "{{ computerNamePrefix }}"
        vmApplications:
          - configurationReference: "{{ configurationReference }}"
            enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
            order: {{ order }}
            packageReferenceId: "{{ packageReferenceId }}"
            vmGalleryTags: "{{ vmGalleryTags }}"
            treatFailureAsDeploymentFailure: {{ treatFailureAsDeploymentFailure }}
        zoneBalance: {{ zoneBalance }}
        isOutboundOnly: {{ isOutboundOnly }}
        enableResilientEphemeralOsDisk: {{ enableResilientEphemeralOsDisk }}
        scaleInPolicy:
          mode: "{{ mode }}"
        proxyAgentSettings:
          enabled: {{ enabled }}
          keyIncarnationId: {{ keyIncarnationId }}
          wireServer:
            mode: "{{ mode }}"
            inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
          imds:
            mode: "{{ mode }}"
            inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
          addProxyAgentExtension: {{ addProxyAgentExtension }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: sku
      description: |
        The node type sku.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Update the configuration of a node type of a given managed cluster, only updating tags or capacity.

```sql
UPDATE azure.servicefabricmanagedclusters.node_types
SET 
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND node_type_name = '{{ node_type_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a Service Fabric node type of a given managed cluster.

```sql
REPLACE azure.servicefabricmanagedclusters.node_types
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND node_type_name = '{{ node_type_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a Service Fabric node type of a given managed cluster.

```sql
DELETE FROM azure.servicefabricmanagedclusters.node_types
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND node_type_name = '{{ node_type_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_fault_simulation"
    values={[
        { label: 'list_fault_simulation', value: 'list_fault_simulation' },
        { label: 'get_fault_simulation', value: 'get_fault_simulation' },
        { label: 'deallocate', value: 'deallocate' },
        { label: 'delete_node', value: 'delete_node' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'reimage', value: 'reimage' },
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' },
        { label: 'start_fault_simulation', value: 'start_fault_simulation' },
        { label: 'stop_fault_simulation', value: 'stop_fault_simulation' }
    ]}
>
<TabItem value="list_fault_simulation">

Gets the list of recent fault simulations for the node type.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.list_fault_simulation 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_fault_simulation">

Gets a fault simulation by the simulationId.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.get_fault_simulation 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"simulationId": "{{ simulationId }}"
}'
;
```
</TabItem>
<TabItem value="deallocate">

Deallocates one or more nodes on the node type. It will disable the fabric nodes, trigger a shutdown on the VMs and release them from the cluster.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.deallocate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodes": "{{ nodes }}", 
"force": {{ force }}, 
"updateType": "{{ updateType }}"
}'
;
```
</TabItem>
<TabItem value="delete_node">

Deletes one or more nodes on the node type. It will disable the fabric nodes, trigger a delete on the VMs and removes the state from the cluster.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.delete_node 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodes": "{{ nodes }}", 
"force": {{ force }}, 
"updateType": "{{ updateType }}"
}'
;
```
</TabItem>
<TabItem value="redeploy">

Redeploys one or more nodes on the node type. It will disable the fabric nodes, trigger a shut down on the VMs, move them to a new node, and power them back on.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodes": "{{ nodes }}", 
"force": {{ force }}, 
"updateType": "{{ updateType }}"
}'
;
```
</TabItem>
<TabItem value="reimage">

Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodes": "{{ nodes }}", 
"force": {{ force }}, 
"updateType": "{{ updateType }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodes": "{{ nodes }}", 
"force": {{ force }}, 
"updateType": "{{ updateType }}"
}'
;
```
</TabItem>
<TabItem value="start">

Starts one or more nodes on the node type. It will trigger an allocation of the fabric node if needed and activate them.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"nodes": "{{ nodes }}", 
"force": {{ force }}, 
"updateType": "{{ updateType }}"
}'
;
```
</TabItem>
<TabItem value="start_fault_simulation">

Starts a fault simulation on the node type.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.start_fault_simulation 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"parameters": "{{ parameters }}"
}'
;
```
</TabItem>
<TabItem value="stop_fault_simulation">

Stops a fault simulation on the node type.

```sql
EXEC azure.servicefabricmanagedclusters.node_types.stop_fault_simulation 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@node_type_name='{{ node_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"simulationId": "{{ simulationId }}"
}'
;
```
</TabItem>
</Tabs>
