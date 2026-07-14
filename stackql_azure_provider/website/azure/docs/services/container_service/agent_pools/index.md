--- 
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - container_service
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

Creates, updates, deletes, gets or lists an <code>agent_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agent_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.agent_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="artifactStreamingProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration for using artifact streaming on AKS.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is 'VirtualMachineScaleSets'.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityReservationGroupID" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Capacity Reservation Group to provide virtual machines from a reserved group of Virtual Machines. This is of the form: '/subscriptions/&#123;subscriptionId&#125;/resourcegroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/capacityreservationgroups/&#123;capacityReservationGroupName&#125;' Customers use it to create an agentpool with a specified CRG. For more information see `Capacity Reservation `_.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source Snapshot ID if the node pool will be created/upgraded using a snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="currentOrchestratorVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes the Agent Pool is running. If orchestratorVersion is a fully specified version , this field will be exactly equal to it. If orchestratorVersion is , this field will contain the full version being used.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Unique read-only string used to implement optimistic concurrency. The eTag value will change when the resource is updated. Specify an if-match or if-none-match header with the eTag value for a subsequent request to enable optimistic concurrency per the normal eTag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoScaling" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable auto-scaler.</td>
</tr>
<tr>
    <td><CopyableCode code="enableEncryptionAtHost" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable host based OS and data drive encryption. This is only supported on certain VM sizes and in certain Azure regions. For more information, see: `https://docs.microsoft.com/azure/aks/enable-host-encryption `_.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use a FIPS-enabled OS. See `Add a FIPS-enabled node pool `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNodePublicIP" /></td>
    <td><code>boolean</code></td>
    <td>Whether each node is allocated its own public IP. Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see `assigning a public IP per node `_. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableOSDiskFullCaching" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable the full-cache ephemeral OS disk feature. When this feature is enabled, the entire operating system will be locally cached on the ephemeral OS disk, preventing E17 events caused by network failures.</td>
</tr>
<tr>
    <td><CopyableCode code="enableUltraSSD" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable UltraSSD.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayProfile" /></td>
    <td><code>object</code></td>
    <td>Profile specific to a managed agent pool in Gateway mode. This field cannot be set if agent pool mode is not Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="gpuInstanceProfile" /></td>
    <td><code>string</code></td>
    <td>GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU. Known values are: "MIG1g", "MIG2g", "MIG3g", "MIG4g", and "MIG7g". (MIG1g, MIG2g, MIG3g, MIG4g, MIG7g)</td>
</tr>
<tr>
    <td><CopyableCode code="gpuProfile" /></td>
    <td><code>object</code></td>
    <td>GPU settings for the Agent Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroupID" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Dedicated Host Group to provision virtual machines from, used only in creation scenario and not allowed to changed once set. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/hostGroups/&#123;hostGroupName&#125;. For more information see `Azure dedicated hosts `_.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeletConfig" /></td>
    <td><code>object</code></td>
    <td>The Kubelet configuration on the agent pool nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeletDiskType" /></td>
    <td><code>string</code></td>
    <td>Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage. Known values are: "OS" and "Temporary". (OS, Temporary)</td>
</tr>
<tr>
    <td><CopyableCode code="linuxOSConfig" /></td>
    <td><code>object</code></td>
    <td>The OS configuration of Linux agent nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="localDNSProfile" /></td>
    <td><code>object</code></td>
    <td>Configures the per-node local DNS, with VnetDNS and KubeDNS overrides. LocalDNS helps improve performance and reliability of DNS resolution in an AKS cluster. For more details see aka.ms/aks/localdns.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="maxPods" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of pods that can run on a node.</td>
</tr>
<tr>
    <td><CopyableCode code="messageOfTheDay" /></td>
    <td><code>string</code></td>
    <td>Message of the day for Linux nodes, base64-encoded. A base64-encoded string which will be written to /etc/motd after decoding. This allows customization of the message of the day for Linux nodes. It must not be specified for Windows nodes. It must be a static string (i.e., will be printed raw and not be executed as a script).</td>
</tr>
<tr>
    <td><CopyableCode code="minCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode of an agent pool. A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions and best practices, see: `https://docs.microsoft.com/azure/aks/use-system-pools `_. Known values are: "System", "User", "Gateway", "ManagedSystem", and "Machines". (System, User, Gateway, ManagedSystem, Machines)</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network-related settings of an agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the node image. Setting this value triggers an agentPool rollback. Only values from `recentlyUsedVersions` are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeInitializationTaints" /></td>
    <td><code>array</code></td>
    <td>Taints added on the nodes during creation that will not be reconciled by AKS. These taints will not be reconciled by AKS and can be removed with a kubectl call. This field can be modified after node pool is created, but nodes will not be recreated with new taints until another operation that requires recreation (e.g. node image upgrade) happens. These taints allow for required configuration to run before the node is ready to accept workloads, for example 'key1=value1:NoSchedule' that then can be removed with `kubectl taint nodes node1 key1=value1:NoSchedule-`.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeLabels" /></td>
    <td><code>object</code></td>
    <td>The node labels to be persisted across all nodes in agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodePublicIPPrefixID" /></td>
    <td><code>string</code></td>
    <td>The public IP prefix ID which VM nodes should use IPs from. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/publicIPPrefixes/&#123;publicIPPrefixName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTaints" /></td>
    <td><code>array</code></td>
    <td>The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestratorVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes specified by the user. Both patch version (e.g. 1.20.13) and (e.g. 1.20) are supported. When is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see `upgrading a node pool `_.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>OS Disk Size in GB to be used to specify the disk size for every machine in the master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskType" /></td>
    <td><code>string</code></td>
    <td>The OS disk type to be used for machines in the agent pool. The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more information see `Ephemeral OS `_. Known values are: "Managed" and "Ephemeral". (Managed, Ephemeral)</td>
</tr>
<tr>
    <td><CopyableCode code="osSKU" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes &lt;= 1.24 or Windows2022 when Kubernetes &gt;= 1.25 if OSType is Windows. Known values are: "Ubuntu", "AzureLinux", "AzureLinux3", "Mariner", "Flatcar", "CBLMariner", "Windows2019", "Windows2022", "Ubuntu2204", "Windows2025", "WindowsAnnual", "Ubuntu2404", and "AzureContainerLinux". (Ubuntu, AzureLinux, AzureLinux3, Mariner, Flatcar, CBLMariner, Windows2019, Windows2022, Ubuntu2204, Windows2025, WindowsAnnual, Ubuntu2404, AzureContainerLinux)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type. The default is Linux. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="podIPAllocationMode" /></td>
    <td><code>string</code></td>
    <td>Pod IP Allocation Mode. The IP allocation mode for pods in the agent pool. Must be used with podSubnetId. The default is 'DynamicIndividual'. Known values are: "DynamicIndividual" and "StaticBlock". (DynamicIndividual, StaticBlock)</td>
</tr>
<tr>
    <td><CopyableCode code="podSubnetID" /></td>
    <td><code>string</code></td>
    <td>The ID of the subnet which pods will join when launched. If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;virtualNetworkName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>object</code></td>
    <td>Whether the Agent Pool is running or stopped. When an Agent Pool is first created it is initially Running. The Agent Pool can be stopped by setting this field to Stopped. A stopped Agent Pool stops all of its VMs and does not accrue billing charges. An Agent Pool can only be stopped if it is Running and provisioning state is Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="preparedImageSpecificationProfile" /></td>
    <td><code>object</code></td>
    <td>Settings to determine the prepared image specification used to provision nodes in a pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroupID" /></td>
    <td><code>string</code></td>
    <td>The ID for Proximity Placement Group.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleDownMode" /></td>
    <td><code>string</code></td>
    <td>The scale down mode to use when scaling the Agent Pool. This also effects the cluster autoscaler behavior. If not specified, it defaults to Delete. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSetEvictionPolicy" /></td>
    <td><code>string</code></td>
    <td>The Virtual Machine Scale Set eviction policy. The eviction policy specifies what to do with the VM when it is evicted. The default is Delete. For more information about eviction see `spot VMs `_. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSetPriority" /></td>
    <td><code>string</code></td>
    <td>The Virtual Machine Scale Set priority. Known values are: "Spot" and "Regular". (Spot, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The security settings of an agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="spotMaxPrice" /></td>
    <td><code>number</code></td>
    <td>The max price (in US Dollars) you are willing to pay for spot instances. Possible values are any decimal value greater than zero or -1 which indicates default price to be up-to on-demand. Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see `spot VMs pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the Agent Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags to be persisted on the agent pool virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for upgrading the agentpool.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeSettingsBlueGreen" /></td>
    <td><code>object</code></td>
    <td>Settings for Blue-Green upgrade on the agentpool. Applies when upgrade strategy is set to BlueGreen.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeStrategy" /></td>
    <td><code>string</code></td>
    <td>Defines the upgrade strategy for the agent pool. The default is Rolling. Known values are: "Rolling" and "BlueGreen". (Rolling, BlueGreen)</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineNodesStatus" /></td>
    <td><code>array</code></td>
    <td>The status of nodes in a VirtualMachines agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesProfile" /></td>
    <td><code>object</code></td>
    <td>Specifications on VirtualMachines agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the agent pool VMs. VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: `https://docs.microsoft.com/azure/aks/quotas-skus-regions `_.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetSubnetID" /></td>
    <td><code>string</code></td>
    <td>The ID of the subnet which agent pool nodes and optionally pods will join on startup. If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;virtualNetworkName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsProfile" /></td>
    <td><code>object</code></td>
    <td>The Windows agent pool's specific profile.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadRuntime" /></td>
    <td><code>string</code></td>
    <td>Determines the type of workload a node can run. Known values are: "OCIContainer", "WasmWasi", "KataMshvVmIsolation", and "KataVmIsolation". (OCIContainer, WasmWasi, KataMshvVmIsolation, KataVmIsolation)</td>
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
    <td><CopyableCode code="artifactStreamingProfile" /></td>
    <td><code>object</code></td>
    <td>Configuration for using artifact streaming on AKS.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZones" /></td>
    <td><code>array</code></td>
    <td>The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is 'VirtualMachineScaleSets'.</td>
</tr>
<tr>
    <td><CopyableCode code="capacityReservationGroupID" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Capacity Reservation Group to provide virtual machines from a reserved group of Virtual Machines. This is of the form: '/subscriptions/&#123;subscriptionId&#125;/resourcegroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/capacityreservationgroups/&#123;capacityReservationGroupName&#125;' Customers use it to create an agentpool with a specified CRG. For more information see `Capacity Reservation `_.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source Snapshot ID if the node pool will be created/upgraded using a snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="currentOrchestratorVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes the Agent Pool is running. If orchestratorVersion is a fully specified version , this field will be exactly equal to it. If orchestratorVersion is , this field will contain the full version being used.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Unique read-only string used to implement optimistic concurrency. The eTag value will change when the resource is updated. Specify an if-match or if-none-match header with the eTag value for a subsequent request to enable optimistic concurrency per the normal eTag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoScaling" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable auto-scaler.</td>
</tr>
<tr>
    <td><CopyableCode code="enableEncryptionAtHost" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable host based OS and data drive encryption. This is only supported on certain VM sizes and in certain Azure regions. For more information, see: `https://docs.microsoft.com/azure/aks/enable-host-encryption `_.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use a FIPS-enabled OS. See `Add a FIPS-enabled node pool `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNodePublicIP" /></td>
    <td><code>boolean</code></td>
    <td>Whether each node is allocated its own public IP. Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see `assigning a public IP per node `_. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableOSDiskFullCaching" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable the full-cache ephemeral OS disk feature. When this feature is enabled, the entire operating system will be locally cached on the ephemeral OS disk, preventing E17 events caused by network failures.</td>
</tr>
<tr>
    <td><CopyableCode code="enableUltraSSD" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable UltraSSD.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayProfile" /></td>
    <td><code>object</code></td>
    <td>Profile specific to a managed agent pool in Gateway mode. This field cannot be set if agent pool mode is not Gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="gpuInstanceProfile" /></td>
    <td><code>string</code></td>
    <td>GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU. Known values are: "MIG1g", "MIG2g", "MIG3g", "MIG4g", and "MIG7g". (MIG1g, MIG2g, MIG3g, MIG4g, MIG7g)</td>
</tr>
<tr>
    <td><CopyableCode code="gpuProfile" /></td>
    <td><code>object</code></td>
    <td>GPU settings for the Agent Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="hostGroupID" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the Dedicated Host Group to provision virtual machines from, used only in creation scenario and not allowed to changed once set. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/hostGroups/&#123;hostGroupName&#125;. For more information see `Azure dedicated hosts `_.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeletConfig" /></td>
    <td><code>object</code></td>
    <td>The Kubelet configuration on the agent pool nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="kubeletDiskType" /></td>
    <td><code>string</code></td>
    <td>Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage. Known values are: "OS" and "Temporary". (OS, Temporary)</td>
</tr>
<tr>
    <td><CopyableCode code="linuxOSConfig" /></td>
    <td><code>object</code></td>
    <td>The OS configuration of Linux agent nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="localDNSProfile" /></td>
    <td><code>object</code></td>
    <td>Configures the per-node local DNS, with VnetDNS and KubeDNS overrides. LocalDNS helps improve performance and reliability of DNS resolution in an AKS cluster. For more details see aka.ms/aks/localdns.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCount" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="maxPods" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of pods that can run on a node.</td>
</tr>
<tr>
    <td><CopyableCode code="messageOfTheDay" /></td>
    <td><code>string</code></td>
    <td>Message of the day for Linux nodes, base64-encoded. A base64-encoded string which will be written to /etc/motd after decoding. This allows customization of the message of the day for Linux nodes. It must not be specified for Windows nodes. It must be a static string (i.e., will be printed raw and not be executed as a script).</td>
</tr>
<tr>
    <td><CopyableCode code="minCount" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of nodes for auto-scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode of an agent pool. A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions and best practices, see: `https://docs.microsoft.com/azure/aks/use-system-pools `_. Known values are: "System", "User", "Gateway", "ManagedSystem", and "Machines". (System, User, Gateway, ManagedSystem, Machines)</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network-related settings of an agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the node image. Setting this value triggers an agentPool rollback. Only values from `recentlyUsedVersions` are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeInitializationTaints" /></td>
    <td><code>array</code></td>
    <td>Taints added on the nodes during creation that will not be reconciled by AKS. These taints will not be reconciled by AKS and can be removed with a kubectl call. This field can be modified after node pool is created, but nodes will not be recreated with new taints until another operation that requires recreation (e.g. node image upgrade) happens. These taints allow for required configuration to run before the node is ready to accept workloads, for example 'key1=value1:NoSchedule' that then can be removed with `kubectl taint nodes node1 key1=value1:NoSchedule-`.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeLabels" /></td>
    <td><code>object</code></td>
    <td>The node labels to be persisted across all nodes in agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodePublicIPPrefixID" /></td>
    <td><code>string</code></td>
    <td>The public IP prefix ID which VM nodes should use IPs from. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/publicIPPrefixes/&#123;publicIPPrefixName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTaints" /></td>
    <td><code>array</code></td>
    <td>The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestratorVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes specified by the user. Both patch version (e.g. 1.20.13) and (e.g. 1.20) are supported. When is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see `upgrading a node pool `_.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskSizeGB" /></td>
    <td><code>integer</code></td>
    <td>OS Disk Size in GB to be used to specify the disk size for every machine in the master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskType" /></td>
    <td><code>string</code></td>
    <td>The OS disk type to be used for machines in the agent pool. The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more information see `Ephemeral OS `_. Known values are: "Managed" and "Ephemeral". (Managed, Ephemeral)</td>
</tr>
<tr>
    <td><CopyableCode code="osSKU" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes &lt;= 1.24 or Windows2022 when Kubernetes &gt;= 1.25 if OSType is Windows. Known values are: "Ubuntu", "AzureLinux", "AzureLinux3", "Mariner", "Flatcar", "CBLMariner", "Windows2019", "Windows2022", "Ubuntu2204", "Windows2025", "WindowsAnnual", "Ubuntu2404", and "AzureContainerLinux". (Ubuntu, AzureLinux, AzureLinux3, Mariner, Flatcar, CBLMariner, Windows2019, Windows2022, Ubuntu2204, Windows2025, WindowsAnnual, Ubuntu2404, AzureContainerLinux)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type. The default is Linux. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="podIPAllocationMode" /></td>
    <td><code>string</code></td>
    <td>Pod IP Allocation Mode. The IP allocation mode for pods in the agent pool. Must be used with podSubnetId. The default is 'DynamicIndividual'. Known values are: "DynamicIndividual" and "StaticBlock". (DynamicIndividual, StaticBlock)</td>
</tr>
<tr>
    <td><CopyableCode code="podSubnetID" /></td>
    <td><code>string</code></td>
    <td>The ID of the subnet which pods will join when launched. If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;virtualNetworkName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>object</code></td>
    <td>Whether the Agent Pool is running or stopped. When an Agent Pool is first created it is initially Running. The Agent Pool can be stopped by setting this field to Stopped. A stopped Agent Pool stops all of its VMs and does not accrue billing charges. An Agent Pool can only be stopped if it is Running and provisioning state is Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="preparedImageSpecificationProfile" /></td>
    <td><code>object</code></td>
    <td>Settings to determine the prepared image specification used to provision nodes in a pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroupID" /></td>
    <td><code>string</code></td>
    <td>The ID for Proximity Placement Group.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleDownMode" /></td>
    <td><code>string</code></td>
    <td>The scale down mode to use when scaling the Agent Pool. This also effects the cluster autoscaler behavior. If not specified, it defaults to Delete. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSetEvictionPolicy" /></td>
    <td><code>string</code></td>
    <td>The Virtual Machine Scale Set eviction policy. The eviction policy specifies what to do with the VM when it is evicted. The default is Delete. For more information about eviction see `spot VMs `_. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSetPriority" /></td>
    <td><code>string</code></td>
    <td>The Virtual Machine Scale Set priority. Known values are: "Spot" and "Regular". (Spot, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The security settings of an agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="spotMaxPrice" /></td>
    <td><code>number</code></td>
    <td>The max price (in US Dollars) you are willing to pay for spot instances. Possible values are any decimal value greater than zero or -1 which indicates default price to be up-to on-demand. Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see `spot VMs pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the Agent Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags to be persisted on the agent pool virtual machine scale set.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for upgrading the agentpool.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeSettingsBlueGreen" /></td>
    <td><code>object</code></td>
    <td>Settings for Blue-Green upgrade on the agentpool. Applies when upgrade strategy is set to BlueGreen.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeStrategy" /></td>
    <td><code>string</code></td>
    <td>Defines the upgrade strategy for the agent pool. The default is Rolling. Known values are: "Rolling" and "BlueGreen". (Rolling, BlueGreen)</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineNodesStatus" /></td>
    <td><code>array</code></td>
    <td>The status of nodes in a VirtualMachines agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachinesProfile" /></td>
    <td><code>object</code></td>
    <td>Specifications on VirtualMachines agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the agent pool VMs. VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: `https://docs.microsoft.com/azure/aks/quotas-skus-regions `_.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetSubnetID" /></td>
    <td><code>string</code></td>
    <td>The ID of the subnet which agent pool nodes and optionally pods will join on startup. If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;virtualNetworkName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsProfile" /></td>
    <td><code>object</code></td>
    <td>The Windows agent pool's specific profile.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadRuntime" /></td>
    <td><code>string</code></td>
    <td>Determines the type of workload a node can run. Known values are: "OCIContainer", "WasmWasi", "KataMshvVmIsolation", and "KataVmIsolation". (OCIContainer, WasmWasi, KataMshvVmIsolation, KataVmIsolation)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified managed cluster agent pool.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of agent pools in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an agent pool in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an agent pool in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-ignore-pod-disruption-budget"><code>ignore-pod-disruption-budget</code></a></td>
    <td>Deletes an agent pool in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#get_available_agent_pool_versions"><CopyableCode code="get_available_agent_pool_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of supported Kubernetes versions for the specified agent pool. See `supported Kubernetes versions `_ for more details about the version lifecycle.</td>
</tr>
<tr>
    <td><a href="#get_upgrade_profile"><CopyableCode code="get_upgrade_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the upgrade profile for an agent pool.</td>
</tr>
<tr>
    <td><a href="#abort_latest_operation"><CopyableCode code="abort_latest_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Aborts last operation running on agent pool. Aborts the currently running operation on the agent pool. The Agent Pool will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned.</td>
</tr>
<tr>
    <td><a href="#complete_upgrade"><CopyableCode code="complete_upgrade" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Completes the upgrade of an agent pool. Completes the upgrade operation for the specified agent pool.</td>
</tr>
<tr>
    <td><a href="#delete_machines"><CopyableCode code="delete_machines" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-machineNames"><code>machineNames</code></a></td>
    <td></td>
    <td>Deletes specific machines in an agent pool.</td>
</tr>
<tr>
    <td><a href="#upgrade_node_image_version"><CopyableCode code="upgrade_node_image_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades the node image version of an agent pool to the latest. Upgrading the node image version of an agent pool applies the newest OS and runtime updates to the nodes. AKS provides one new image per week with the latest updates. For more details on node image versions, see: `https://docs.microsoft.com/azure/aks/node-image-upgrade `_.</td>
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
<tr id="parameter-agent_pool_name">
    <td><CopyableCode code="agent_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent pool. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed cluster resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-ignore-pod-disruption-budget">
    <td><CopyableCode code="ignore-pod-disruption-budget" /></td>
    <td><code>boolean</code></td>
    <td>ignore-pod-disruption-budget=true to delete those pods on a node without considering Pod Disruption Budget. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified managed cluster agent pool.

```sql
SELECT
id,
name,
artifactStreamingProfile,
availabilityZones,
capacityReservationGroupID,
count,
creationData,
currentOrchestratorVersion,
eTag,
enableAutoScaling,
enableEncryptionAtHost,
enableFIPS,
enableNodePublicIP,
enableOSDiskFullCaching,
enableUltraSSD,
gatewayProfile,
gpuInstanceProfile,
gpuProfile,
hostGroupID,
kubeletConfig,
kubeletDiskType,
linuxOSConfig,
localDNSProfile,
maxCount,
maxPods,
messageOfTheDay,
minCount,
mode,
networkProfile,
nodeImageVersion,
nodeInitializationTaints,
nodeLabels,
nodePublicIPPrefixID,
nodeTaints,
orchestratorVersion,
osDiskSizeGB,
osDiskType,
osSKU,
osType,
podIPAllocationMode,
podSubnetID,
powerState,
preparedImageSpecificationProfile,
provisioningState,
proximityPlacementGroupID,
scaleDownMode,
scaleSetEvictionPolicy,
scaleSetPriority,
securityProfile,
spotMaxPrice,
status,
systemData,
tags,
type,
upgradeSettings,
upgradeSettingsBlueGreen,
upgradeStrategy,
virtualMachineNodesStatus,
virtualMachinesProfile,
vmSize,
vnetSubnetID,
windowsProfile,
workloadRuntime
FROM azure.container_service.agent_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND agent_pool_name = '{{ agent_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of agent pools in the specified managed cluster.

```sql
SELECT
id,
name,
artifactStreamingProfile,
availabilityZones,
capacityReservationGroupID,
count,
creationData,
currentOrchestratorVersion,
eTag,
enableAutoScaling,
enableEncryptionAtHost,
enableFIPS,
enableNodePublicIP,
enableOSDiskFullCaching,
enableUltraSSD,
gatewayProfile,
gpuInstanceProfile,
gpuProfile,
hostGroupID,
kubeletConfig,
kubeletDiskType,
linuxOSConfig,
localDNSProfile,
maxCount,
maxPods,
messageOfTheDay,
minCount,
mode,
networkProfile,
nodeImageVersion,
nodeInitializationTaints,
nodeLabels,
nodePublicIPPrefixID,
nodeTaints,
orchestratorVersion,
osDiskSizeGB,
osDiskType,
osSKU,
osType,
podIPAllocationMode,
podSubnetID,
powerState,
preparedImageSpecificationProfile,
provisioningState,
proximityPlacementGroupID,
scaleDownMode,
scaleSetEvictionPolicy,
scaleSetPriority,
securityProfile,
spotMaxPrice,
status,
systemData,
tags,
type,
upgradeSettings,
upgradeSettingsBlueGreen,
upgradeStrategy,
virtualMachineNodesStatus,
virtualMachinesProfile,
vmSize,
vnetSubnetID,
windowsProfile,
workloadRuntime
FROM azure.container_service.agent_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Creates or updates an agent pool in the specified managed cluster.

```sql
INSERT INTO azure.container_service.agent_pools (
properties,
resource_group_name,
resource_name,
agent_pool_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ agent_pool_name }}',
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
- name: agent_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the agent_pools resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the agent_pools resource.
    - name: agent_pool_name
      value: "{{ agent_pool_name }}"
      description: Required parameter for the agent_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the agent_pools resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        eTag: "{{ eTag }}"
        count: {{ count }}
        vmSize: "{{ vmSize }}"
        osDiskSizeGB: {{ osDiskSizeGB }}
        osDiskType: "{{ osDiskType }}"
        kubeletDiskType: "{{ kubeletDiskType }}"
        workloadRuntime: "{{ workloadRuntime }}"
        messageOfTheDay: "{{ messageOfTheDay }}"
        vnetSubnetID: "{{ vnetSubnetID }}"
        podSubnetID: "{{ podSubnetID }}"
        podIPAllocationMode: "{{ podIPAllocationMode }}"
        maxPods: {{ maxPods }}
        osType: "{{ osType }}"
        osSKU: "{{ osSKU }}"
        maxCount: {{ maxCount }}
        minCount: {{ minCount }}
        enableAutoScaling: {{ enableAutoScaling }}
        scaleDownMode: "{{ scaleDownMode }}"
        type: "{{ type }}"
        mode: "{{ mode }}"
        orchestratorVersion: "{{ orchestratorVersion }}"
        currentOrchestratorVersion: "{{ currentOrchestratorVersion }}"
        nodeImageVersion: "{{ nodeImageVersion }}"
        upgradeStrategy: "{{ upgradeStrategy }}"
        enableOSDiskFullCaching: {{ enableOSDiskFullCaching }}
        upgradeSettings:
          maxSurge: "{{ maxSurge }}"
          maxUnavailable: "{{ maxUnavailable }}"
          maxBlockedNodes: "{{ maxBlockedNodes }}"
          drainTimeoutInMinutes: {{ drainTimeoutInMinutes }}
          nodeSoakDurationInMinutes: {{ nodeSoakDurationInMinutes }}
          undrainableNodeBehavior: "{{ undrainableNodeBehavior }}"
        upgradeSettingsBlueGreen:
          drainBatchSize: "{{ drainBatchSize }}"
          drainTimeoutInMinutes: {{ drainTimeoutInMinutes }}
          batchSoakDurationInMinutes: {{ batchSoakDurationInMinutes }}
          finalSoakDurationInMinutes: {{ finalSoakDurationInMinutes }}
        provisioningState: "{{ provisioningState }}"
        powerState:
          code: "{{ code }}"
        availabilityZones:
          - "{{ availabilityZones }}"
        enableNodePublicIP: {{ enableNodePublicIP }}
        nodePublicIPPrefixID: "{{ nodePublicIPPrefixID }}"
        scaleSetPriority: "{{ scaleSetPriority }}"
        scaleSetEvictionPolicy: "{{ scaleSetEvictionPolicy }}"
        spotMaxPrice: {{ spotMaxPrice }}
        tags: "{{ tags }}"
        nodeLabels: "{{ nodeLabels }}"
        nodeTaints:
          - "{{ nodeTaints }}"
        nodeInitializationTaints:
          - "{{ nodeInitializationTaints }}"
        proximityPlacementGroupID: "{{ proximityPlacementGroupID }}"
        kubeletConfig:
          cpuManagerPolicy: "{{ cpuManagerPolicy }}"
          cpuCfsQuota: {{ cpuCfsQuota }}
          cpuCfsQuotaPeriod: "{{ cpuCfsQuotaPeriod }}"
          imageGcHighThreshold: {{ imageGcHighThreshold }}
          imageGcLowThreshold: {{ imageGcLowThreshold }}
          topologyManagerPolicy: "{{ topologyManagerPolicy }}"
          allowedUnsafeSysctls:
            - "{{ allowedUnsafeSysctls }}"
          failSwapOn: {{ failSwapOn }}
          containerLogMaxSizeMB: {{ containerLogMaxSizeMB }}
          containerLogMaxFiles: {{ containerLogMaxFiles }}
          podMaxPids: {{ podMaxPids }}
          seccompDefault: "{{ seccompDefault }}"
          kubeReserved:
            cpuMillicores: {{ cpuMillicores }}
            memoryMB: {{ memoryMB }}
          hardEvictionThreshold:
            memoryAvailable: "{{ memoryAvailable }}"
            nodeFsAvailable: "{{ nodeFsAvailable }}"
            nodeFsInodesFree: "{{ nodeFsInodesFree }}"
        linuxOSConfig:
          sysctls:
            netCoreSomaxconn: {{ netCoreSomaxconn }}
            netCoreNetdevMaxBacklog: {{ netCoreNetdevMaxBacklog }}
            netCoreRmemDefault: {{ netCoreRmemDefault }}
            netCoreRmemMax: {{ netCoreRmemMax }}
            netCoreWmemDefault: {{ netCoreWmemDefault }}
            netCoreWmemMax: {{ netCoreWmemMax }}
            netCoreOptmemMax: {{ netCoreOptmemMax }}
            netIpv4TcpMaxSynBacklog: {{ netIpv4TcpMaxSynBacklog }}
            netIpv4TcpMaxTwBuckets: {{ netIpv4TcpMaxTwBuckets }}
            netIpv4TcpFinTimeout: {{ netIpv4TcpFinTimeout }}
            netIpv4TcpKeepaliveTime: {{ netIpv4TcpKeepaliveTime }}
            netIpv4TcpKeepaliveProbes: {{ netIpv4TcpKeepaliveProbes }}
            netIpv4TcpkeepaliveIntvl: {{ netIpv4TcpkeepaliveIntvl }}
            netIpv4TcpTwReuse: {{ netIpv4TcpTwReuse }}
            netIpv4IpLocalPortRange: "{{ netIpv4IpLocalPortRange }}"
            netIpv4NeighDefaultGcThresh1: {{ netIpv4NeighDefaultGcThresh1 }}
            netIpv4NeighDefaultGcThresh2: {{ netIpv4NeighDefaultGcThresh2 }}
            netIpv4NeighDefaultGcThresh3: {{ netIpv4NeighDefaultGcThresh3 }}
            netNetfilterNfConntrackMax: {{ netNetfilterNfConntrackMax }}
            netNetfilterNfConntrackBuckets: {{ netNetfilterNfConntrackBuckets }}
            fsInotifyMaxUserWatches: {{ fsInotifyMaxUserWatches }}
            fsFileMax: {{ fsFileMax }}
            fsAioMaxNr: {{ fsAioMaxNr }}
            fsNrOpen: {{ fsNrOpen }}
            kernelThreadsMax: {{ kernelThreadsMax }}
            vmMaxMapCount: {{ vmMaxMapCount }}
            vmSwappiness: {{ vmSwappiness }}
            vmVfsCachePressure: {{ vmVfsCachePressure }}
          transparentHugePageEnabled: "{{ transparentHugePageEnabled }}"
          transparentHugePageDefrag: "{{ transparentHugePageDefrag }}"
          swapFileSizeMB: {{ swapFileSizeMB }}
        enableEncryptionAtHost: {{ enableEncryptionAtHost }}
        enableUltraSSD: {{ enableUltraSSD }}
        enableFIPS: {{ enableFIPS }}
        gpuInstanceProfile: "{{ gpuInstanceProfile }}"
        creationData:
          sourceResourceId: "{{ sourceResourceId }}"
        capacityReservationGroupID: "{{ capacityReservationGroupID }}"
        hostGroupID: "{{ hostGroupID }}"
        networkProfile:
          nodePublicIPTags:
            - ipTagType: "{{ ipTagType }}"
              tag: "{{ tag }}"
          nodePublicIPPrefixIDs:
            - "{{ nodePublicIPPrefixIDs }}"
          allowedHostPorts:
            - portStart: {{ portStart }}
              portEnd: {{ portEnd }}
              protocol: "{{ protocol }}"
          applicationSecurityGroups:
            - "{{ applicationSecurityGroups }}"
          secondaryNetworkInterfaces:
            - type: "{{ type }}"
              vnetSubnetId: "{{ vnetSubnetId }}"
              enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
        windowsProfile:
          disableOutboundNat: {{ disableOutboundNat }}
        securityProfile:
          enableVTPM: {{ enableVTPM }}
          enableSecureBoot: {{ enableSecureBoot }}
          sshAccess: "{{ sshAccess }}"
        gpuProfile:
          driver: "{{ driver }}"
          driverType: "{{ driverType }}"
          nvidia:
            managementMode: "{{ managementMode }}"
            migStrategy: "{{ migStrategy }}"
        gatewayProfile:
          publicIPPrefixSize: {{ publicIPPrefixSize }}
        artifactStreamingProfile:
          enabled: {{ enabled }}
        virtualMachinesProfile:
          scale:
            manual:
              - size: "{{ size }}"
                count: {{ count }}
            autoscale:
              - size: "{{ size }}"
                minCount: {{ minCount }}
                maxCount: {{ maxCount }}
        virtualMachineNodesStatus:
          - size: "{{ size }}"
            count: {{ count }}
        status:
          provisioningError:
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                target: "{{ target }}"
                details: "{{ details }}"
                additionalInfo: "{{ additionalInfo }}"
            additionalInfo:
              - type: "{{ type }}"
                info: "{{ info }}"
        localDNSProfile:
          mode: "{{ mode }}"
          state: "{{ state }}"
          vnetDNSOverrides: "{{ vnetDNSOverrides }}"
          kubeDNSOverrides: "{{ kubeDNSOverrides }}"
        preparedImageSpecificationProfile:
          preparedImageSpecificationId: "{{ preparedImageSpecificationId }}"
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

Creates or updates an agent pool in the specified managed cluster.

```sql
REPLACE azure.container_service.agent_pools
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
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

Deletes an agent pool in the specified managed cluster.

```sql
DELETE FROM azure.container_service.agent_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND ignore-pod-disruption-budget = '{{ ignore-pod-disruption-budget }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_available_agent_pool_versions"
    values={[
        { label: 'get_available_agent_pool_versions', value: 'get_available_agent_pool_versions' },
        { label: 'get_upgrade_profile', value: 'get_upgrade_profile' },
        { label: 'abort_latest_operation', value: 'abort_latest_operation' },
        { label: 'complete_upgrade', value: 'complete_upgrade' },
        { label: 'delete_machines', value: 'delete_machines' },
        { label: 'upgrade_node_image_version', value: 'upgrade_node_image_version' }
    ]}
>
<TabItem value="get_available_agent_pool_versions">

Gets a list of supported Kubernetes versions for the specified agent pool. See `supported Kubernetes versions `_ for more details about the version lifecycle.

```sql
EXEC azure.container_service.agent_pools.get_available_agent_pool_versions 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_upgrade_profile">

Gets the upgrade profile for an agent pool.

```sql
EXEC azure.container_service.agent_pools.get_upgrade_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@agent_pool_name='{{ agent_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="abort_latest_operation">

Aborts last operation running on agent pool. Aborts the currently running operation on the agent pool. The Agent Pool will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned.

```sql
EXEC azure.container_service.agent_pools.abort_latest_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@agent_pool_name='{{ agent_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="complete_upgrade">

Completes the upgrade of an agent pool. Completes the upgrade operation for the specified agent pool.

```sql
EXEC azure.container_service.agent_pools.complete_upgrade 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@agent_pool_name='{{ agent_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_machines">

Deletes specific machines in an agent pool.

```sql
EXEC azure.container_service.agent_pools.delete_machines 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@agent_pool_name='{{ agent_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"machineNames": "{{ machineNames }}"
}'
;
```
</TabItem>
<TabItem value="upgrade_node_image_version">

Upgrades the node image version of an agent pool to the latest. Upgrading the node image version of an agent pool applies the newest OS and runtime updates to the nodes. AKS provides one new image per week with the latest updates. For more details on node image versions, see: `https://docs.microsoft.com/azure/aks/node-image-upgrade `_.

```sql
EXEC azure.container_service.agent_pools.upgrade_node_image_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@agent_pool_name='{{ agent_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
