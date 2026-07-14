--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - service_fabric
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_upgradable_versions"
    values={[
        { label: 'list_upgradable_versions', value: 'list_upgradable_versions' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_upgradable_versions">

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
    <td><CopyableCode code="supportedPath" /></td>
    <td><code>array</code></td>
    <td>The list of intermediate cluster code versions for an upgrade or downgrade.</td>
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
    <td><CopyableCode code="addOnFeatures" /></td>
    <td><code>array</code></td>
    <td>The list of add-on features to enable in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTypeVersionsCleanupPolicy" /></td>
    <td><code>object</code></td>
    <td>The policy used to clean up unused versions.</td>
</tr>
<tr>
    <td><CopyableCode code="availableClusterVersions" /></td>
    <td><code>array</code></td>
    <td>The Service Fabric runtime versions available for this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azureActiveDirectory" /></td>
    <td><code>object</code></td>
    <td>The AAD authentication settings of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>The certificate to use for securing the cluster. The certificate provided will be used for node to node security within the cluster, SSL certificate for cluster management endpoint and default admin client.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateCommonNames" /></td>
    <td><code>object</code></td>
    <td>Describes a list of server certificates referenced by common name that are used to secure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificateCommonNames" /></td>
    <td><code>array</code></td>
    <td>The list of client certificates referenced by common name that are allowed to manage the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificateThumbprints" /></td>
    <td><code>array</code></td>
    <td>The list of client certificates referenced by thumbprint that are allowed to manage the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to 'Manual'. To get list of available Service Fabric versions for new clusters use `ClusterVersion API `_. To get the list of available version for existing clusters use **availableClusterVersions**.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterEndpoint" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource Provider endpoint. A system service in the cluster connects to this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>A service generated unique identifier for the cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterState" /></td>
    <td><code>string</code></td>
    <td>The current state of the cluster. * WaitingForNodes - Indicates that the cluster resource is created and the resource provider is waiting for Service Fabric VM extension to boot up and report to it. * Deploying - Indicates that the Service Fabric runtime is being installed on the VMs. Cluster resource will be in this state until the cluster boots up and system services are up. * BaselineUpgrade - Indicates that the cluster is upgrading to establishes the cluster version. This upgrade is automatically initiated when the cluster boots up for the first time. * UpdatingUserConfiguration - Indicates that the cluster is being upgraded with the user provided configuration. * UpdatingUserCertificate - Indicates that the cluster is being upgraded with the user provided certificate. * UpdatingInfrastructure - Indicates that the cluster is being upgraded with the latest Service Fabric runtime version. This happens only when the **upgradeMode** is set to 'Automatic'. * EnforcingClusterVersion - Indicates that cluster is on a different version than expected and the cluster is being upgraded to the expected version. * UpgradeServiceUnreachable - Indicates that the system service in the cluster is no longer polling the Resource Provider. Clusters in this state cannot be managed by the Resource Provider. * AutoScale - Indicates that the ReliabilityLevel of the cluster is being adjusted. * Ready - Indicates that the cluster is in a stable state. Known values are: "WaitingForNodes", "Deploying", "BaselineUpgrade", "UpdatingUserConfiguration", "UpdatingUserCertificate", "UpdatingInfrastructure", "EnforcingClusterVersion", "UpgradeServiceUnreachable", "AutoScale", and "Ready". (WaitingForNodes, Deploying, BaselineUpgrade, UpdatingUserConfiguration, UpdatingUserCertificate, UpdatingInfrastructure, EnforcingClusterVersion, UpgradeServiceUnreachable, AutoScale, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsStorageAccountConfig" /></td>
    <td><code>object</code></td>
    <td>The storage account information for storing Service Fabric diagnostic logs.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHttpGatewayExclusiveAuthMode" /></td>
    <td><code>boolean</code></td>
    <td>If true, token-based authentication is not allowed on the HttpGatewayEndpoint. This is required to support TLS versions 1.3 and above. If token-based authentication is used, HttpGatewayTokenAuthEndpointPort must be defined.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Azure resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStoreServiceEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the event store service is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricSettings" /></td>
    <td><code>array</code></td>
    <td>The list of custom fabric settings to configure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureServiceManager" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if infrastructure service manager is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The http management endpoint of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTypes" /></td>
    <td><code>array</code></td>
    <td>The list of node types in the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>array</code></td>
    <td>Indicates a list of notification channels for cluster events.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster resource. Known values are: "Updating", "Succeeded", "Failed", and "Canceled". (Updating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="reliabilityLevel" /></td>
    <td><code>string</code></td>
    <td>The reliability level sets the replica set size of system services. Learn about `ReliabilityLevel `_. * None - Run the System services with a target replica set count of 1. This should only be used for test clusters. * Bronze - Run the System services with a target replica set count of 3. This should only be used for test clusters. * Silver - Run the System services with a target replica set count of 5. * Gold - Run the System services with a target replica set count of 7. * Platinum - Run the System services with a target replica set count of 9. Known values are: "None", "Bronze", "Silver", "Gold", and "Platinum". (None, Bronze, Silver, Gold, Platinum)</td>
</tr>
<tr>
    <td><CopyableCode code="reverseProxyCertificate" /></td>
    <td><code>object</code></td>
    <td>The server certificate used by reverse proxy.</td>
</tr>
<tr>
    <td><CopyableCode code="reverseProxyCertificateCommonNames" /></td>
    <td><code>object</code></td>
    <td>Describes a list of server certificates referenced by common name that are used to secure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sfZonalUpgradeMode" /></td>
    <td><code>string</code></td>
    <td>This property controls the logical grouping of VMs in upgrade domains (UDs). This property can't be modified if a node type with multiple Availability Zones is already present in the cluster. Known values are: "Parallel" and "Hierarchical". (Parallel, Hierarchical)</td>
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
    <td><CopyableCode code="upgradeDescription" /></td>
    <td><code>object</code></td>
    <td>The policy to use when upgrading the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeMode" /></td>
    <td><code>string</code></td>
    <td>The upgrade mode of the cluster when new Service Fabric runtime version is available. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePauseEndTimestampUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the end date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePauseStartTimestampUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the start date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeWave" /></td>
    <td><code>string</code></td>
    <td>Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. Only applies when **upgradeMode** is set to 'Automatic'. Known values are: "Wave0", "Wave1", and "Wave2". (Wave0, Wave1, Wave2)</td>
</tr>
<tr>
    <td><CopyableCode code="vmImage" /></td>
    <td><code>string</code></td>
    <td>The VM image VMSS has been configured with. Generic names such as Windows or Linux can be used.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssZonalUpgradeMode" /></td>
    <td><code>string</code></td>
    <td>This property defines the upgrade mode for the virtual machine scale set, it is mandatory if a node type with multiple Availability Zones is added. Known values are: "Parallel" and "Hierarchical". (Parallel, Hierarchical)</td>
</tr>
<tr>
    <td><CopyableCode code="waveUpgradePaused" /></td>
    <td><code>boolean</code></td>
    <td>Boolean to pause automatic runtime version upgrades to the cluster.</td>
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
    <td><CopyableCode code="addOnFeatures" /></td>
    <td><code>array</code></td>
    <td>The list of add-on features to enable in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTypeVersionsCleanupPolicy" /></td>
    <td><code>object</code></td>
    <td>The policy used to clean up unused versions.</td>
</tr>
<tr>
    <td><CopyableCode code="availableClusterVersions" /></td>
    <td><code>array</code></td>
    <td>The Service Fabric runtime versions available for this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azureActiveDirectory" /></td>
    <td><code>object</code></td>
    <td>The AAD authentication settings of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>The certificate to use for securing the cluster. The certificate provided will be used for node to node security within the cluster, SSL certificate for cluster management endpoint and default admin client.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateCommonNames" /></td>
    <td><code>object</code></td>
    <td>Describes a list of server certificates referenced by common name that are used to secure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificateCommonNames" /></td>
    <td><code>array</code></td>
    <td>The list of client certificates referenced by common name that are allowed to manage the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificateThumbprints" /></td>
    <td><code>array</code></td>
    <td>The list of client certificates referenced by thumbprint that are allowed to manage the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to 'Manual'. To get list of available Service Fabric versions for new clusters use `ClusterVersion API `_. To get the list of available version for existing clusters use **availableClusterVersions**.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterEndpoint" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource Provider endpoint. A system service in the cluster connects to this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>A service generated unique identifier for the cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterState" /></td>
    <td><code>string</code></td>
    <td>The current state of the cluster. * WaitingForNodes - Indicates that the cluster resource is created and the resource provider is waiting for Service Fabric VM extension to boot up and report to it. * Deploying - Indicates that the Service Fabric runtime is being installed on the VMs. Cluster resource will be in this state until the cluster boots up and system services are up. * BaselineUpgrade - Indicates that the cluster is upgrading to establishes the cluster version. This upgrade is automatically initiated when the cluster boots up for the first time. * UpdatingUserConfiguration - Indicates that the cluster is being upgraded with the user provided configuration. * UpdatingUserCertificate - Indicates that the cluster is being upgraded with the user provided certificate. * UpdatingInfrastructure - Indicates that the cluster is being upgraded with the latest Service Fabric runtime version. This happens only when the **upgradeMode** is set to 'Automatic'. * EnforcingClusterVersion - Indicates that cluster is on a different version than expected and the cluster is being upgraded to the expected version. * UpgradeServiceUnreachable - Indicates that the system service in the cluster is no longer polling the Resource Provider. Clusters in this state cannot be managed by the Resource Provider. * AutoScale - Indicates that the ReliabilityLevel of the cluster is being adjusted. * Ready - Indicates that the cluster is in a stable state. Known values are: "WaitingForNodes", "Deploying", "BaselineUpgrade", "UpdatingUserConfiguration", "UpdatingUserCertificate", "UpdatingInfrastructure", "EnforcingClusterVersion", "UpgradeServiceUnreachable", "AutoScale", and "Ready". (WaitingForNodes, Deploying, BaselineUpgrade, UpdatingUserConfiguration, UpdatingUserCertificate, UpdatingInfrastructure, EnforcingClusterVersion, UpgradeServiceUnreachable, AutoScale, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsStorageAccountConfig" /></td>
    <td><code>object</code></td>
    <td>The storage account information for storing Service Fabric diagnostic logs.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHttpGatewayExclusiveAuthMode" /></td>
    <td><code>boolean</code></td>
    <td>If true, token-based authentication is not allowed on the HttpGatewayEndpoint. This is required to support TLS versions 1.3 and above. If token-based authentication is used, HttpGatewayTokenAuthEndpointPort must be defined.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Azure resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStoreServiceEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the event store service is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricSettings" /></td>
    <td><code>array</code></td>
    <td>The list of custom fabric settings to configure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureServiceManager" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if infrastructure service manager is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The http management endpoint of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTypes" /></td>
    <td><code>array</code></td>
    <td>The list of node types in the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>array</code></td>
    <td>Indicates a list of notification channels for cluster events.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster resource. Known values are: "Updating", "Succeeded", "Failed", and "Canceled". (Updating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="reliabilityLevel" /></td>
    <td><code>string</code></td>
    <td>The reliability level sets the replica set size of system services. Learn about `ReliabilityLevel `_. * None - Run the System services with a target replica set count of 1. This should only be used for test clusters. * Bronze - Run the System services with a target replica set count of 3. This should only be used for test clusters. * Silver - Run the System services with a target replica set count of 5. * Gold - Run the System services with a target replica set count of 7. * Platinum - Run the System services with a target replica set count of 9. Known values are: "None", "Bronze", "Silver", "Gold", and "Platinum". (None, Bronze, Silver, Gold, Platinum)</td>
</tr>
<tr>
    <td><CopyableCode code="reverseProxyCertificate" /></td>
    <td><code>object</code></td>
    <td>The server certificate used by reverse proxy.</td>
</tr>
<tr>
    <td><CopyableCode code="reverseProxyCertificateCommonNames" /></td>
    <td><code>object</code></td>
    <td>Describes a list of server certificates referenced by common name that are used to secure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sfZonalUpgradeMode" /></td>
    <td><code>string</code></td>
    <td>This property controls the logical grouping of VMs in upgrade domains (UDs). This property can't be modified if a node type with multiple Availability Zones is already present in the cluster. Known values are: "Parallel" and "Hierarchical". (Parallel, Hierarchical)</td>
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
    <td><CopyableCode code="upgradeDescription" /></td>
    <td><code>object</code></td>
    <td>The policy to use when upgrading the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeMode" /></td>
    <td><code>string</code></td>
    <td>The upgrade mode of the cluster when new Service Fabric runtime version is available. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePauseEndTimestampUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the end date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePauseStartTimestampUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the start date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeWave" /></td>
    <td><code>string</code></td>
    <td>Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. Only applies when **upgradeMode** is set to 'Automatic'. Known values are: "Wave0", "Wave1", and "Wave2". (Wave0, Wave1, Wave2)</td>
</tr>
<tr>
    <td><CopyableCode code="vmImage" /></td>
    <td><code>string</code></td>
    <td>The VM image VMSS has been configured with. Generic names such as Windows or Linux can be used.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssZonalUpgradeMode" /></td>
    <td><code>string</code></td>
    <td>This property defines the upgrade mode for the virtual machine scale set, it is mandatory if a node type with multiple Availability Zones is added. Known values are: "Parallel" and "Hierarchical". (Parallel, Hierarchical)</td>
</tr>
<tr>
    <td><CopyableCode code="waveUpgradePaused" /></td>
    <td><code>boolean</code></td>
    <td>Boolean to pause automatic runtime version upgrades to the cluster.</td>
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
    <td><CopyableCode code="addOnFeatures" /></td>
    <td><code>array</code></td>
    <td>The list of add-on features to enable in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTypeVersionsCleanupPolicy" /></td>
    <td><code>object</code></td>
    <td>The policy used to clean up unused versions.</td>
</tr>
<tr>
    <td><CopyableCode code="availableClusterVersions" /></td>
    <td><code>array</code></td>
    <td>The Service Fabric runtime versions available for this cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azureActiveDirectory" /></td>
    <td><code>object</code></td>
    <td>The AAD authentication settings of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>The certificate to use for securing the cluster. The certificate provided will be used for node to node security within the cluster, SSL certificate for cluster management endpoint and default admin client.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateCommonNames" /></td>
    <td><code>object</code></td>
    <td>Describes a list of server certificates referenced by common name that are used to secure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificateCommonNames" /></td>
    <td><code>array</code></td>
    <td>The list of client certificates referenced by common name that are allowed to manage the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertificateThumbprints" /></td>
    <td><code>array</code></td>
    <td>The list of client certificates referenced by thumbprint that are allowed to manage the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to 'Manual'. To get list of available Service Fabric versions for new clusters use `ClusterVersion API `_. To get the list of available version for existing clusters use **availableClusterVersions**.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterEndpoint" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource Provider endpoint. A system service in the cluster connects to this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>A service generated unique identifier for the cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterState" /></td>
    <td><code>string</code></td>
    <td>The current state of the cluster. * WaitingForNodes - Indicates that the cluster resource is created and the resource provider is waiting for Service Fabric VM extension to boot up and report to it. * Deploying - Indicates that the Service Fabric runtime is being installed on the VMs. Cluster resource will be in this state until the cluster boots up and system services are up. * BaselineUpgrade - Indicates that the cluster is upgrading to establishes the cluster version. This upgrade is automatically initiated when the cluster boots up for the first time. * UpdatingUserConfiguration - Indicates that the cluster is being upgraded with the user provided configuration. * UpdatingUserCertificate - Indicates that the cluster is being upgraded with the user provided certificate. * UpdatingInfrastructure - Indicates that the cluster is being upgraded with the latest Service Fabric runtime version. This happens only when the **upgradeMode** is set to 'Automatic'. * EnforcingClusterVersion - Indicates that cluster is on a different version than expected and the cluster is being upgraded to the expected version. * UpgradeServiceUnreachable - Indicates that the system service in the cluster is no longer polling the Resource Provider. Clusters in this state cannot be managed by the Resource Provider. * AutoScale - Indicates that the ReliabilityLevel of the cluster is being adjusted. * Ready - Indicates that the cluster is in a stable state. Known values are: "WaitingForNodes", "Deploying", "BaselineUpgrade", "UpdatingUserConfiguration", "UpdatingUserCertificate", "UpdatingInfrastructure", "EnforcingClusterVersion", "UpgradeServiceUnreachable", "AutoScale", and "Ready". (WaitingForNodes, Deploying, BaselineUpgrade, UpdatingUserConfiguration, UpdatingUserCertificate, UpdatingInfrastructure, EnforcingClusterVersion, UpgradeServiceUnreachable, AutoScale, Ready)</td>
</tr>
<tr>
    <td><CopyableCode code="diagnosticsStorageAccountConfig" /></td>
    <td><code>object</code></td>
    <td>The storage account information for storing Service Fabric diagnostic logs.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHttpGatewayExclusiveAuthMode" /></td>
    <td><code>boolean</code></td>
    <td>If true, token-based authentication is not allowed on the HttpGatewayEndpoint. This is required to support TLS versions 1.3 and above. If token-based authentication is used, HttpGatewayTokenAuthEndpointPort must be defined.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Azure resource etag.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStoreServiceEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the event store service is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricSettings" /></td>
    <td><code>array</code></td>
    <td>The list of custom fabric settings to configure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureServiceManager" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if infrastructure service manager is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The http management endpoint of the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeTypes" /></td>
    <td><code>array</code></td>
    <td>The list of node types in the cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>array</code></td>
    <td>Indicates a list of notification channels for cluster events.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster resource. Known values are: "Updating", "Succeeded", "Failed", and "Canceled". (Updating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="reliabilityLevel" /></td>
    <td><code>string</code></td>
    <td>The reliability level sets the replica set size of system services. Learn about `ReliabilityLevel `_. * None - Run the System services with a target replica set count of 1. This should only be used for test clusters. * Bronze - Run the System services with a target replica set count of 3. This should only be used for test clusters. * Silver - Run the System services with a target replica set count of 5. * Gold - Run the System services with a target replica set count of 7. * Platinum - Run the System services with a target replica set count of 9. Known values are: "None", "Bronze", "Silver", "Gold", and "Platinum". (None, Bronze, Silver, Gold, Platinum)</td>
</tr>
<tr>
    <td><CopyableCode code="reverseProxyCertificate" /></td>
    <td><code>object</code></td>
    <td>The server certificate used by reverse proxy.</td>
</tr>
<tr>
    <td><CopyableCode code="reverseProxyCertificateCommonNames" /></td>
    <td><code>object</code></td>
    <td>Describes a list of server certificates referenced by common name that are used to secure the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sfZonalUpgradeMode" /></td>
    <td><code>string</code></td>
    <td>This property controls the logical grouping of VMs in upgrade domains (UDs). This property can't be modified if a node type with multiple Availability Zones is already present in the cluster. Known values are: "Parallel" and "Hierarchical". (Parallel, Hierarchical)</td>
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
    <td><CopyableCode code="upgradeDescription" /></td>
    <td><code>object</code></td>
    <td>The policy to use when upgrading the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeMode" /></td>
    <td><code>string</code></td>
    <td>The upgrade mode of the cluster when new Service Fabric runtime version is available. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePauseEndTimestampUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the end date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePauseStartTimestampUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the start date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="upgradeWave" /></td>
    <td><code>string</code></td>
    <td>Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. Only applies when **upgradeMode** is set to 'Automatic'. Known values are: "Wave0", "Wave1", and "Wave2". (Wave0, Wave1, Wave2)</td>
</tr>
<tr>
    <td><CopyableCode code="vmImage" /></td>
    <td><code>string</code></td>
    <td>The VM image VMSS has been configured with. Generic names such as Windows or Linux can be used.</td>
</tr>
<tr>
    <td><CopyableCode code="vmssZonalUpgradeMode" /></td>
    <td><code>string</code></td>
    <td>This property defines the upgrade mode for the virtual machine scale set, it is mandatory if a node type with multiple Availability Zones is added. Known values are: "Parallel" and "Hierarchical". (Parallel, Hierarchical)</td>
</tr>
<tr>
    <td><CopyableCode code="waveUpgradePaused" /></td>
    <td><code>boolean</code></td>
    <td>Boolean to pause automatic runtime version upgrades to the cluster.</td>
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
    <td><a href="#list_upgradable_versions"><CopyableCode code="list_upgradable_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to get the minimum and maximum upgradable version from the current cluster version, or the required path to get to the an specific target version. If a target is not provided, it will get the minimum and maximum versions available from the current cluster version. If a target is given, it will provide the required path to get from the current cluster version to the target version.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Service Fabric cluster resource. Get a Service Fabric cluster resource created or in the process of being created in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of Service Fabric cluster resources created in the specified resource group. Gets all Service Fabric cluster resources created or in the process of being created in the resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of Service Fabric cluster resources created in the specified subscription. Gets all Service Fabric cluster resources created or in the process of being created in the subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Service Fabric cluster resource. Create or update a Service Fabric cluster resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the configuration of a Service Fabric cluster resource. Update the configuration of a Service Fabric cluster resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Service Fabric cluster resource. Create or update a Service Fabric cluster resource with the specified name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Service Fabric cluster resource. Delete a Service Fabric cluster resource with the specified name.</td>
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
    defaultValue="list_upgradable_versions"
    values={[
        { label: 'list_upgradable_versions', value: 'list_upgradable_versions' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_upgradable_versions">

Operation to get the minimum and maximum upgradable version from the current cluster version, or the required path to get to the an specific target version. If a target is not provided, it will get the minimum and maximum versions available from the current cluster version. If a target is given, it will provide the required path to get from the current cluster version to the target version.

```sql
SELECT
supportedPath
FROM azure.service_fabric.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a Service Fabric cluster resource. Get a Service Fabric cluster resource created or in the process of being created in the specified resource group.

```sql
SELECT
id,
name,
addOnFeatures,
applicationTypeVersionsCleanupPolicy,
availableClusterVersions,
azureActiveDirectory,
certificate,
certificateCommonNames,
clientCertificateCommonNames,
clientCertificateThumbprints,
clusterCodeVersion,
clusterEndpoint,
clusterId,
clusterState,
diagnosticsStorageAccountConfig,
enableHttpGatewayExclusiveAuthMode,
etag,
eventStoreServiceEnabled,
fabricSettings,
infrastructureServiceManager,
location,
managementEndpoint,
nodeTypes,
notifications,
provisioningState,
reliabilityLevel,
reverseProxyCertificate,
reverseProxyCertificateCommonNames,
sfZonalUpgradeMode,
systemData,
tags,
type,
upgradeDescription,
upgradeMode,
upgradePauseEndTimestampUtc,
upgradePauseStartTimestampUtc,
upgradeWave,
vmImage,
vmssZonalUpgradeMode,
waveUpgradePaused
FROM azure.service_fabric.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets the list of Service Fabric cluster resources created in the specified resource group. Gets all Service Fabric cluster resources created or in the process of being created in the resource group.

```sql
SELECT
id,
name,
addOnFeatures,
applicationTypeVersionsCleanupPolicy,
availableClusterVersions,
azureActiveDirectory,
certificate,
certificateCommonNames,
clientCertificateCommonNames,
clientCertificateThumbprints,
clusterCodeVersion,
clusterEndpoint,
clusterId,
clusterState,
diagnosticsStorageAccountConfig,
enableHttpGatewayExclusiveAuthMode,
etag,
eventStoreServiceEnabled,
fabricSettings,
infrastructureServiceManager,
location,
managementEndpoint,
nodeTypes,
notifications,
provisioningState,
reliabilityLevel,
reverseProxyCertificate,
reverseProxyCertificateCommonNames,
sfZonalUpgradeMode,
systemData,
tags,
type,
upgradeDescription,
upgradeMode,
upgradePauseEndTimestampUtc,
upgradePauseStartTimestampUtc,
upgradeWave,
vmImage,
vmssZonalUpgradeMode,
waveUpgradePaused
FROM azure.service_fabric.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of Service Fabric cluster resources created in the specified subscription. Gets all Service Fabric cluster resources created or in the process of being created in the subscription.

```sql
SELECT
id,
name,
addOnFeatures,
applicationTypeVersionsCleanupPolicy,
availableClusterVersions,
azureActiveDirectory,
certificate,
certificateCommonNames,
clientCertificateCommonNames,
clientCertificateThumbprints,
clusterCodeVersion,
clusterEndpoint,
clusterId,
clusterState,
diagnosticsStorageAccountConfig,
enableHttpGatewayExclusiveAuthMode,
etag,
eventStoreServiceEnabled,
fabricSettings,
infrastructureServiceManager,
location,
managementEndpoint,
nodeTypes,
notifications,
provisioningState,
reliabilityLevel,
reverseProxyCertificate,
reverseProxyCertificateCommonNames,
sfZonalUpgradeMode,
systemData,
tags,
type,
upgradeDescription,
upgradeMode,
upgradePauseEndTimestampUtc,
upgradePauseStartTimestampUtc,
upgradeWave,
vmImage,
vmssZonalUpgradeMode,
waveUpgradePaused
FROM azure.service_fabric.clusters
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

Creates or updates a Service Fabric cluster resource. Create or update a Service Fabric cluster resource with the specified name.

```sql
INSERT INTO azure.service_fabric.clusters (
tags,
location,
properties,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the clusters resource.
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
        The cluster resource properties.
      value:
        addOnFeatures:
          - "{{ addOnFeatures }}"
        availableClusterVersions:
          - codeVersion: "{{ codeVersion }}"
            supportExpiryUtc: "{{ supportExpiryUtc }}"
            environment: "{{ environment }}"
        azureActiveDirectory:
          tenantId: "{{ tenantId }}"
          clusterApplication: "{{ clusterApplication }}"
          clientApplication: "{{ clientApplication }}"
        certificate:
          thumbprint: "{{ thumbprint }}"
          thumbprintSecondary: "{{ thumbprintSecondary }}"
          x509StoreName: "{{ x509StoreName }}"
        certificateCommonNames:
          commonNames:
            - certificateCommonName: "{{ certificateCommonName }}"
              certificateIssuerThumbprint: "{{ certificateIssuerThumbprint }}"
          x509StoreName: "{{ x509StoreName }}"
        clientCertificateCommonNames:
          - isAdmin: {{ isAdmin }}
            certificateCommonName: "{{ certificateCommonName }}"
            certificateIssuerThumbprint: "{{ certificateIssuerThumbprint }}"
        clientCertificateThumbprints:
          - isAdmin: {{ isAdmin }}
            certificateThumbprint: "{{ certificateThumbprint }}"
        clusterCodeVersion: "{{ clusterCodeVersion }}"
        clusterEndpoint: "{{ clusterEndpoint }}"
        clusterId: "{{ clusterId }}"
        clusterState: "{{ clusterState }}"
        diagnosticsStorageAccountConfig:
          storageAccountName: "{{ storageAccountName }}"
          protectedAccountKeyName: "{{ protectedAccountKeyName }}"
          protectedAccountKeyName2: "{{ protectedAccountKeyName2 }}"
          blobEndpoint: "{{ blobEndpoint }}"
          queueEndpoint: "{{ queueEndpoint }}"
          tableEndpoint: "{{ tableEndpoint }}"
        eventStoreServiceEnabled: {{ eventStoreServiceEnabled }}
        fabricSettings:
          - name: "{{ name }}"
            parameters: "{{ parameters }}"
        managementEndpoint: "{{ managementEndpoint }}"
        nodeTypes:
          - name: "{{ name }}"
            placementProperties: "{{ placementProperties }}"
            capacities: "{{ capacities }}"
            clientConnectionEndpointPort: {{ clientConnectionEndpointPort }}
            httpGatewayEndpointPort: {{ httpGatewayEndpointPort }}
            durabilityLevel: "{{ durabilityLevel }}"
            applicationPorts:
              startPort: {{ startPort }}
              endPort: {{ endPort }}
            ephemeralPorts:
              startPort: {{ startPort }}
              endPort: {{ endPort }}
            isPrimary: {{ isPrimary }}
            vmInstanceCount: {{ vmInstanceCount }}
            reverseProxyEndpointPort: {{ reverseProxyEndpointPort }}
            isStateless: {{ isStateless }}
            multipleAvailabilityZones: {{ multipleAvailabilityZones }}
            httpGatewayTokenAuthEndpointPort: {{ httpGatewayTokenAuthEndpointPort }}
        provisioningState: "{{ provisioningState }}"
        reliabilityLevel: "{{ reliabilityLevel }}"
        reverseProxyCertificate:
          thumbprint: "{{ thumbprint }}"
          thumbprintSecondary: "{{ thumbprintSecondary }}"
          x509StoreName: "{{ x509StoreName }}"
        reverseProxyCertificateCommonNames:
          commonNames:
            - certificateCommonName: "{{ certificateCommonName }}"
              certificateIssuerThumbprint: "{{ certificateIssuerThumbprint }}"
          x509StoreName: "{{ x509StoreName }}"
        upgradeDescription:
          forceRestart: {{ forceRestart }}
          upgradeReplicaSetCheckTimeout: "{{ upgradeReplicaSetCheckTimeout }}"
          healthCheckWaitDuration: "{{ healthCheckWaitDuration }}"
          healthCheckStableDuration: "{{ healthCheckStableDuration }}"
          healthCheckRetryTimeout: "{{ healthCheckRetryTimeout }}"
          upgradeTimeout: "{{ upgradeTimeout }}"
          upgradeDomainTimeout: "{{ upgradeDomainTimeout }}"
          healthPolicy:
            maxPercentUnhealthyNodes: {{ maxPercentUnhealthyNodes }}
            maxPercentUnhealthyApplications: {{ maxPercentUnhealthyApplications }}
            applicationHealthPolicies: "{{ applicationHealthPolicies }}"
          deltaHealthPolicy:
            maxPercentDeltaUnhealthyNodes: {{ maxPercentDeltaUnhealthyNodes }}
            maxPercentUpgradeDomainDeltaUnhealthyNodes: {{ maxPercentUpgradeDomainDeltaUnhealthyNodes }}
            maxPercentDeltaUnhealthyApplications: {{ maxPercentDeltaUnhealthyApplications }}
            applicationDeltaHealthPolicies: "{{ applicationDeltaHealthPolicies }}"
        upgradeMode: "{{ upgradeMode }}"
        applicationTypeVersionsCleanupPolicy:
          maxUnusedVersionsToKeep: {{ maxUnusedVersionsToKeep }}
        vmImage: "{{ vmImage }}"
        sfZonalUpgradeMode: "{{ sfZonalUpgradeMode }}"
        vmssZonalUpgradeMode: "{{ vmssZonalUpgradeMode }}"
        infrastructureServiceManager: {{ infrastructureServiceManager }}
        upgradeWave: "{{ upgradeWave }}"
        upgradePauseStartTimestampUtc: "{{ upgradePauseStartTimestampUtc }}"
        upgradePauseEndTimestampUtc: "{{ upgradePauseEndTimestampUtc }}"
        waveUpgradePaused: {{ waveUpgradePaused }}
        notifications:
          - isEnabled: {{ isEnabled }}
            notificationCategory: "{{ notificationCategory }}"
            notificationLevel: "{{ notificationLevel }}"
            notificationTargets: "{{ notificationTargets }}"
        enableHttpGatewayExclusiveAuthMode: {{ enableHttpGatewayExclusiveAuthMode }}
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

Updates the configuration of a Service Fabric cluster resource. Update the configuration of a Service Fabric cluster resource with the specified name.

```sql
UPDATE azure.service_fabric.clusters
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Creates or updates a Service Fabric cluster resource. Create or update a Service Fabric cluster resource with the specified name.

```sql
REPLACE azure.service_fabric.clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
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

Deletes a Service Fabric cluster resource. Delete a Service Fabric cluster resource with the specified name.

```sql
DELETE FROM azure.service_fabric.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
