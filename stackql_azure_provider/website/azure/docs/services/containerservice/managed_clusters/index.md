--- 
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - containerservice
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

Creates, updates, deletes, gets or lists a <code>managed_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerservice.managed_clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_command_result"
    values={[
        { label: 'get_command_result', value: 'get_command_result' },
        { label: 'get_mesh_upgrade_profile', value: 'get_mesh_upgrade_profile' },
        { label: 'get', value: 'get' },
        { label: 'get_guardrails_versions', value: 'get_guardrails_versions' },
        { label: 'get_mesh_revision_profile', value: 'get_mesh_revision_profile' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_guardrails_versions', value: 'list_guardrails_versions' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_command_result">

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
    <td>The command id.</td>
</tr>
<tr>
    <td><CopyableCode code="exitCode" /></td>
    <td><code>integer</code></td>
    <td>The exit code of the command.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the command finished.</td>
</tr>
<tr>
    <td><CopyableCode code="logs" /></td>
    <td><code>string</code></td>
    <td>The command output.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>provisioning State.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>An explanation of why provisioningState is set to failed (if so).</td>
</tr>
<tr>
    <td><CopyableCode code="startedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the command started.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_mesh_upgrade_profile">

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
    <td><CopyableCode code="compatibleWith" /></td>
    <td><code>array</code></td>
    <td>List of items this revision of service mesh is compatible with, and their associated versions.</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>string</code></td>
    <td>The revision of the mesh release.</td>
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
    <td><CopyableCode code="upgrades" /></td>
    <td><code>array</code></td>
    <td>List of revisions available for upgrade of a specific mesh revision.</td>
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
    <td><CopyableCode code="aadProfile" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="addonProfiles" /></td>
    <td><code>object</code></td>
    <td>The profile of managed cluster add-on.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolProfiles" /></td>
    <td><code>array</code></td>
    <td>The agent pool properties.</td>
</tr>
<tr>
    <td><CopyableCode code="aiToolchainOperatorProfile" /></td>
    <td><code>object</code></td>
    <td>AI toolchain operator settings that apply to the whole cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="apiServerAccessProfile" /></td>
    <td><code>object</code></td>
    <td>The access profile for managed cluster API server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Parameters to be applied to the cluster-autoscaler when enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="autoUpgradeProfile" /></td>
    <td><code>object</code></td>
    <td>The auto upgrade configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="azureMonitorProfile" /></td>
    <td><code>object</code></td>
    <td>Azure Monitor addon profiles for monitoring the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePortalFQDN" /></td>
    <td><code>string</code></td>
    <td>The special FQDN used by the Azure Portal to access the Managed Cluster. This FQDN is for use only by the Azure Portal and should not be used by other clients. The Azure Portal requires certain Cross-Origin Resource Sharing (CORS) headers to be sent in some responses, which Kubernetes APIServer doesn't handle by default. This special FQDN supports CORS, allowing the Azure Portal to function properly.</td>
</tr>
<tr>
    <td><CopyableCode code="bootstrapProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the cluster bootstrap configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneScalingProfile" /></td>
    <td><code>object</code></td>
    <td>Profile for providing scaled and performance guaranteed control plane capacity to deliver consistent performance under high workload. Requires Kubernetes version 1.33.0 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source Snapshot ID if the cluster will be created/upgraded using a snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="currentKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes the Managed Cluster is running. If kubernetesVersion was a fully specified version , this field will be exactly equal to it. If kubernetesVersion was , this field will contain the full version being used.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAccounts" /></td>
    <td><code>boolean</code></td>
    <td>If local accounts should be disabled on the Managed Cluster. If set to true, getting static credentials will be disabled for this cluster. This must only be used on Managed Clusters that are AAD enabled. For more details see `disable local accounts `_.</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetID" /></td>
    <td><code>string</code></td>
    <td>The Resource ID of the disk encryption set to use for enabling encryption at rest. This is of the form: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/diskEncryptionSets/&#123;encryptionSetName&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsPrefix" /></td>
    <td><code>string</code></td>
    <td>The DNS prefix of the Managed Cluster. This cannot be updated once the Managed Cluster has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable FIPS mode at the cluster level. When enabled, this setting enforces FIPS compliance for all AKS-managed components, such as the node operating system, addons, and `managed containerized components `_. See `Enable cluster-wide FIPS `_ for more details. When this property is enabled, all node pools in the cluster must also be FIPS-enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNamespaceResources" /></td>
    <td><code>boolean</code></td>
    <td>Enable namespace as Azure resource. The default value is false. It can be enabled/disabled on creation and updating of the managed cluster. See `https://aka.ms/NamespaceARMResource `_ for more details on Namespace as a ARM Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRBAC" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable Kubernetes Role-Based Access Control.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the master pool.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnSubdomain" /></td>
    <td><code>string</code></td>
    <td>The FQDN subdomain of the private cluster with custom private dns zone. This cannot be updated once the Managed Cluster has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="healthMonitorProfile" /></td>
    <td><code>object</code></td>
    <td>Health monitor profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedSystemProfile" /></td>
    <td><code>object</code></td>
    <td>Settings for hosted system addons. For more information, see `https://aka.ms/aks/automatic/systemcomponents `_.</td>
</tr>
<tr>
    <td><CopyableCode code="httpProxyConfig" /></td>
    <td><code>object</code></td>
    <td>Configurations for provisioning the cluster with HTTP proxy servers.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the managed cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProfile" /></td>
    <td><code>object</code></td>
    <td>The user identity associated with the managed cluster. This identity will be used by the kubelet. Only one user assigned identity is allowed. The only accepted key is "kubeletidentity", with value of "resourceId": "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identityName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="ingressProfile" /></td>
    <td><code>object</code></td>
    <td>Ingress profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>This is primarily used to expose different UI experiences in the portal for different kinds.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes specified by the user. Both patch version (e.g. 1.20.13) and (e.g. 1.20) are supported. When is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. When you upgrade a supported AKS cluster, Kubernetes minor versions cannot be skipped. All upgrades must be performed sequentially by major version number. For example, upgrades between 1.14.x -&gt; 1.15.x or 1.15.x -&gt; 1.16.x are allowed, however 1.14.x -&gt; 1.16.x is not allowed. See `upgrading an AKS cluster `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="linuxProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Linux VMs in the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxAgentPools" /></td>
    <td><code>integer</code></td>
    <td>The max number of agent pools for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsProfile" /></td>
    <td><code>object</code></td>
    <td>Optional cluster metrics configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network configuration profile.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeDisruptionProfile" /></td>
    <td><code>object</code></td>
    <td>Node disruption profile for a managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeProvisioningProfile" /></td>
    <td><code>object</code></td>
    <td>Node provisioning settings that apply to the whole cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group containing agent pool nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeResourceGroupProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the node resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="oidcIssuerProfile" /></td>
    <td><code>object</code></td>
    <td>The OIDC issuer profile of the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="podIdentityProfile" /></td>
    <td><code>object</code></td>
    <td>The pod identity profile of the Managed Cluster. See `use AAD pod identity `_ for more details on AAD pod identity integration.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>object</code></td>
    <td>The Power State of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateFQDN" /></td>
    <td><code>string</code></td>
    <td>The FQDN of private cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResources" /></td>
    <td><code>array</code></td>
    <td>Private link resources associated with the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>PublicNetworkAccess of the managedCluster. Allow or deny public network access for AKS. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUID" /></td>
    <td><code>string</code></td>
    <td>The resourceUID uniquely identifies ManagedClusters that reuse ARM ResourceIds (i.e: create, delete, create sequence).</td>
</tr>
<tr>
    <td><CopyableCode code="schedulerProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the pod scheduler configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Security profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceMeshProfile" /></td>
    <td><code>object</code></td>
    <td>Service mesh profile for a managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalProfile" /></td>
    <td><code>object</code></td>
    <td>Information about a service principal identity for the cluster to use for manipulating Azure APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The managed cluster SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlan" /></td>
    <td><code>string</code></td>
    <td>The support plan for the Managed Cluster. If unspecified, the default is 'KubernetesOfficial'. Known values are: "KubernetesOfficial" and "AKSLongTermSupport". (KubernetesOfficial, AKSLongTermSupport)</td>
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
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for upgrading a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Windows VMs in the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadAutoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Workload Auto-scaler profile for the managed cluster.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_guardrails_versions">

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
    <td><CopyableCode code="isDefaultVersion" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is the default version.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>string</code></td>
    <td>Whether the version is preview or stable. Known values are: "Preview" and "Stable". (Preview, Stable)</td>
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
<TabItem value="get_mesh_revision_profile">

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
    <td><CopyableCode code="meshRevisions" /></td>
    <td><code>array</code></td>
    <td>Available mesh revisions.</td>
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
    <td><CopyableCode code="aadProfile" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="addonProfiles" /></td>
    <td><code>object</code></td>
    <td>The profile of managed cluster add-on.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolProfiles" /></td>
    <td><code>array</code></td>
    <td>The agent pool properties.</td>
</tr>
<tr>
    <td><CopyableCode code="aiToolchainOperatorProfile" /></td>
    <td><code>object</code></td>
    <td>AI toolchain operator settings that apply to the whole cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="apiServerAccessProfile" /></td>
    <td><code>object</code></td>
    <td>The access profile for managed cluster API server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Parameters to be applied to the cluster-autoscaler when enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="autoUpgradeProfile" /></td>
    <td><code>object</code></td>
    <td>The auto upgrade configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="azureMonitorProfile" /></td>
    <td><code>object</code></td>
    <td>Azure Monitor addon profiles for monitoring the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePortalFQDN" /></td>
    <td><code>string</code></td>
    <td>The special FQDN used by the Azure Portal to access the Managed Cluster. This FQDN is for use only by the Azure Portal and should not be used by other clients. The Azure Portal requires certain Cross-Origin Resource Sharing (CORS) headers to be sent in some responses, which Kubernetes APIServer doesn't handle by default. This special FQDN supports CORS, allowing the Azure Portal to function properly.</td>
</tr>
<tr>
    <td><CopyableCode code="bootstrapProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the cluster bootstrap configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneScalingProfile" /></td>
    <td><code>object</code></td>
    <td>Profile for providing scaled and performance guaranteed control plane capacity to deliver consistent performance under high workload. Requires Kubernetes version 1.33.0 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source Snapshot ID if the cluster will be created/upgraded using a snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="currentKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes the Managed Cluster is running. If kubernetesVersion was a fully specified version , this field will be exactly equal to it. If kubernetesVersion was , this field will contain the full version being used.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAccounts" /></td>
    <td><code>boolean</code></td>
    <td>If local accounts should be disabled on the Managed Cluster. If set to true, getting static credentials will be disabled for this cluster. This must only be used on Managed Clusters that are AAD enabled. For more details see `disable local accounts `_.</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetID" /></td>
    <td><code>string</code></td>
    <td>The Resource ID of the disk encryption set to use for enabling encryption at rest. This is of the form: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/diskEncryptionSets/&#123;encryptionSetName&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsPrefix" /></td>
    <td><code>string</code></td>
    <td>The DNS prefix of the Managed Cluster. This cannot be updated once the Managed Cluster has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable FIPS mode at the cluster level. When enabled, this setting enforces FIPS compliance for all AKS-managed components, such as the node operating system, addons, and `managed containerized components `_. See `Enable cluster-wide FIPS `_ for more details. When this property is enabled, all node pools in the cluster must also be FIPS-enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNamespaceResources" /></td>
    <td><code>boolean</code></td>
    <td>Enable namespace as Azure resource. The default value is false. It can be enabled/disabled on creation and updating of the managed cluster. See `https://aka.ms/NamespaceARMResource `_ for more details on Namespace as a ARM Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRBAC" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable Kubernetes Role-Based Access Control.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the master pool.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnSubdomain" /></td>
    <td><code>string</code></td>
    <td>The FQDN subdomain of the private cluster with custom private dns zone. This cannot be updated once the Managed Cluster has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="healthMonitorProfile" /></td>
    <td><code>object</code></td>
    <td>Health monitor profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedSystemProfile" /></td>
    <td><code>object</code></td>
    <td>Settings for hosted system addons. For more information, see `https://aka.ms/aks/automatic/systemcomponents `_.</td>
</tr>
<tr>
    <td><CopyableCode code="httpProxyConfig" /></td>
    <td><code>object</code></td>
    <td>Configurations for provisioning the cluster with HTTP proxy servers.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the managed cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProfile" /></td>
    <td><code>object</code></td>
    <td>The user identity associated with the managed cluster. This identity will be used by the kubelet. Only one user assigned identity is allowed. The only accepted key is "kubeletidentity", with value of "resourceId": "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identityName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="ingressProfile" /></td>
    <td><code>object</code></td>
    <td>Ingress profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>This is primarily used to expose different UI experiences in the portal for different kinds.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes specified by the user. Both patch version (e.g. 1.20.13) and (e.g. 1.20) are supported. When is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. When you upgrade a supported AKS cluster, Kubernetes minor versions cannot be skipped. All upgrades must be performed sequentially by major version number. For example, upgrades between 1.14.x -&gt; 1.15.x or 1.15.x -&gt; 1.16.x are allowed, however 1.14.x -&gt; 1.16.x is not allowed. See `upgrading an AKS cluster `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="linuxProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Linux VMs in the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxAgentPools" /></td>
    <td><code>integer</code></td>
    <td>The max number of agent pools for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsProfile" /></td>
    <td><code>object</code></td>
    <td>Optional cluster metrics configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network configuration profile.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeDisruptionProfile" /></td>
    <td><code>object</code></td>
    <td>Node disruption profile for a managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeProvisioningProfile" /></td>
    <td><code>object</code></td>
    <td>Node provisioning settings that apply to the whole cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group containing agent pool nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeResourceGroupProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the node resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="oidcIssuerProfile" /></td>
    <td><code>object</code></td>
    <td>The OIDC issuer profile of the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="podIdentityProfile" /></td>
    <td><code>object</code></td>
    <td>The pod identity profile of the Managed Cluster. See `use AAD pod identity `_ for more details on AAD pod identity integration.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>object</code></td>
    <td>The Power State of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateFQDN" /></td>
    <td><code>string</code></td>
    <td>The FQDN of private cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResources" /></td>
    <td><code>array</code></td>
    <td>Private link resources associated with the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>PublicNetworkAccess of the managedCluster. Allow or deny public network access for AKS. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUID" /></td>
    <td><code>string</code></td>
    <td>The resourceUID uniquely identifies ManagedClusters that reuse ARM ResourceIds (i.e: create, delete, create sequence).</td>
</tr>
<tr>
    <td><CopyableCode code="schedulerProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the pod scheduler configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Security profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceMeshProfile" /></td>
    <td><code>object</code></td>
    <td>Service mesh profile for a managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalProfile" /></td>
    <td><code>object</code></td>
    <td>Information about a service principal identity for the cluster to use for manipulating Azure APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The managed cluster SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlan" /></td>
    <td><code>string</code></td>
    <td>The support plan for the Managed Cluster. If unspecified, the default is 'KubernetesOfficial'. Known values are: "KubernetesOfficial" and "AKSLongTermSupport". (KubernetesOfficial, AKSLongTermSupport)</td>
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
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for upgrading a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Windows VMs in the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadAutoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Workload Auto-scaler profile for the managed cluster.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_guardrails_versions">

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
    <td><CopyableCode code="isDefaultVersion" /></td>
    <td><code>boolean</code></td>
    <td>Whether this is the default version.</td>
</tr>
<tr>
    <td><CopyableCode code="support" /></td>
    <td><code>string</code></td>
    <td>Whether the version is preview or stable. Known values are: "Preview" and "Stable". (Preview, Stable)</td>
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
    <td><CopyableCode code="aadProfile" /></td>
    <td><code>object</code></td>
    <td>The Azure Active Directory configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="addonProfiles" /></td>
    <td><code>object</code></td>
    <td>The profile of managed cluster add-on.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPoolProfiles" /></td>
    <td><code>array</code></td>
    <td>The agent pool properties.</td>
</tr>
<tr>
    <td><CopyableCode code="aiToolchainOperatorProfile" /></td>
    <td><code>object</code></td>
    <td>AI toolchain operator settings that apply to the whole cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="apiServerAccessProfile" /></td>
    <td><code>object</code></td>
    <td>The access profile for managed cluster API server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Parameters to be applied to the cluster-autoscaler when enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="autoUpgradeProfile" /></td>
    <td><code>object</code></td>
    <td>The auto upgrade configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="azureMonitorProfile" /></td>
    <td><code>object</code></td>
    <td>Azure Monitor addon profiles for monitoring the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azurePortalFQDN" /></td>
    <td><code>string</code></td>
    <td>The special FQDN used by the Azure Portal to access the Managed Cluster. This FQDN is for use only by the Azure Portal and should not be used by other clients. The Azure Portal requires certain Cross-Origin Resource Sharing (CORS) headers to be sent in some responses, which Kubernetes APIServer doesn't handle by default. This special FQDN supports CORS, allowing the Azure Portal to function properly.</td>
</tr>
<tr>
    <td><CopyableCode code="bootstrapProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the cluster bootstrap configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlaneScalingProfile" /></td>
    <td><code>object</code></td>
    <td>Profile for providing scaled and performance guaranteed control plane capacity to deliver consistent performance under high workload. Requires Kubernetes version 1.33.0 or later.</td>
</tr>
<tr>
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source Snapshot ID if the cluster will be created/upgraded using a snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="currentKubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes the Managed Cluster is running. If kubernetesVersion was a fully specified version , this field will be exactly equal to it. If kubernetesVersion was , this field will contain the full version being used.</td>
</tr>
<tr>
    <td><CopyableCode code="disableLocalAccounts" /></td>
    <td><code>boolean</code></td>
    <td>If local accounts should be disabled on the Managed Cluster. If set to true, getting static credentials will be disabled for this cluster. This must only be used on Managed Clusters that are AAD enabled. For more details see `disable local accounts `_.</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetID" /></td>
    <td><code>string</code></td>
    <td>The Resource ID of the disk encryption set to use for enabling encryption at rest. This is of the form: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Compute/diskEncryptionSets/&#123;encryptionSetName&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsPrefix" /></td>
    <td><code>string</code></td>
    <td>The DNS prefix of the Managed Cluster. This cannot be updated once the Managed Cluster has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable FIPS mode at the cluster level. When enabled, this setting enforces FIPS compliance for all AKS-managed components, such as the node operating system, addons, and `managed containerized components `_. See `Enable cluster-wide FIPS `_ for more details. When this property is enabled, all node pools in the cluster must also be FIPS-enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enableNamespaceResources" /></td>
    <td><code>boolean</code></td>
    <td>Enable namespace as Azure resource. The default value is false. It can be enabled/disabled on creation and updating of the managed cluster. See `https://aka.ms/NamespaceARMResource `_ for more details on Namespace as a ARM Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableRBAC" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable Kubernetes Role-Based Access Control.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the master pool.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnSubdomain" /></td>
    <td><code>string</code></td>
    <td>The FQDN subdomain of the private cluster with custom private dns zone. This cannot be updated once the Managed Cluster has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="healthMonitorProfile" /></td>
    <td><code>object</code></td>
    <td>Health monitor profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="hostedSystemProfile" /></td>
    <td><code>object</code></td>
    <td>Settings for hosted system addons. For more information, see `https://aka.ms/aks/automatic/systemcomponents `_.</td>
</tr>
<tr>
    <td><CopyableCode code="httpProxyConfig" /></td>
    <td><code>object</code></td>
    <td>Configurations for provisioning the cluster with HTTP proxy servers.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the managed cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProfile" /></td>
    <td><code>object</code></td>
    <td>The user identity associated with the managed cluster. This identity will be used by the kubelet. Only one user assigned identity is allowed. The only accepted key is "kubeletidentity", with value of "resourceId": "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identityName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="ingressProfile" /></td>
    <td><code>object</code></td>
    <td>Ingress profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>This is primarily used to expose different UI experiences in the portal for different kinds.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes specified by the user. Both patch version (e.g. 1.20.13) and (e.g. 1.20) are supported. When is specified, the latest supported GA patch version is chosen automatically. Updating the cluster with the same once it has been created (e.g. 1.14.x -&gt; 1.14) will not trigger an upgrade, even if a newer patch version is available. When you upgrade a supported AKS cluster, Kubernetes minor versions cannot be skipped. All upgrades must be performed sequentially by major version number. For example, upgrades between 1.14.x -&gt; 1.15.x or 1.15.x -&gt; 1.16.x are allowed, however 1.14.x -&gt; 1.16.x is not allowed. See `upgrading an AKS cluster `_ for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="linuxProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Linux VMs in the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maxAgentPools" /></td>
    <td><code>integer</code></td>
    <td>The max number of agent pools for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsProfile" /></td>
    <td><code>object</code></td>
    <td>Optional cluster metrics configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network configuration profile.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeDisruptionProfile" /></td>
    <td><code>object</code></td>
    <td>Node disruption profile for a managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeProvisioningProfile" /></td>
    <td><code>object</code></td>
    <td>Node provisioning settings that apply to the whole cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group containing agent pool nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeResourceGroupProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the node resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="oidcIssuerProfile" /></td>
    <td><code>object</code></td>
    <td>The OIDC issuer profile of the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="podIdentityProfile" /></td>
    <td><code>object</code></td>
    <td>The pod identity profile of the Managed Cluster. See `use AAD pod identity `_ for more details on AAD pod identity integration.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>object</code></td>
    <td>The Power State of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateFQDN" /></td>
    <td><code>string</code></td>
    <td>The FQDN of private cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResources" /></td>
    <td><code>array</code></td>
    <td>Private link resources associated with the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>PublicNetworkAccess of the managedCluster. Allow or deny public network access for AKS. Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUID" /></td>
    <td><code>string</code></td>
    <td>The resourceUID uniquely identifies ManagedClusters that reuse ARM ResourceIds (i.e: create, delete, create sequence).</td>
</tr>
<tr>
    <td><CopyableCode code="schedulerProfile" /></td>
    <td><code>object</code></td>
    <td>Profile of the pod scheduler configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Security profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceMeshProfile" /></td>
    <td><code>object</code></td>
    <td>Service mesh profile for a managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalProfile" /></td>
    <td><code>object</code></td>
    <td>Information about a service principal identity for the cluster to use for manipulating Azure APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The managed cluster SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage profile for the managed cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlan" /></td>
    <td><code>string</code></td>
    <td>The support plan for the Managed Cluster. If unspecified, the default is 'KubernetesOfficial'. Known values are: "KubernetesOfficial" and "AKSLongTermSupport". (KubernetesOfficial, AKSLongTermSupport)</td>
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
    <td><CopyableCode code="upgradeSettings" /></td>
    <td><code>object</code></td>
    <td>Settings for upgrading a cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Windows VMs in the Managed Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadAutoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Workload Auto-scaler profile for the managed cluster.</td>
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
    <td><a href="#get_command_result"><CopyableCode code="get_command_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-command_id"><code>command_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the results of a command which has been run on the Managed Cluster.</td>
</tr>
<tr>
    <td><a href="#get_mesh_upgrade_profile"><CopyableCode code="get_mesh_upgrade_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets available upgrades for a service mesh in a cluster.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a managed cluster.</td>
</tr>
<tr>
    <td><a href="#get_guardrails_versions"><CopyableCode code="get_guardrails_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets supported Guardrails version in the specified subscription and location. Contains Guardrails version along with its support info and whether it is a default version.</td>
</tr>
<tr>
    <td><a href="#get_mesh_revision_profile"><CopyableCode code="get_mesh_revision_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a mesh revision profile for a specified mesh in the specified location. Contains extra metadata on the revision, including supported revisions, cluster compatibility and available upgrades.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists managed clusters in the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_guardrails_versions"><CopyableCode code="list_guardrails_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of supported Guardrails versions in the specified subscription and location. Contains list of Guardrails version along with its support info and whether it is a default version.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of managed clusters in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a managed cluster.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags on a managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a managed cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-ignore-pod-disruption-budget"><code>ignore-pod-disruption-budget</code></a></td>
    <td>Deletes a managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_cluster_admin_credentials"><CopyableCode code="list_cluster_admin_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-server-fqdn"><code>server-fqdn</code></a></td>
    <td>Lists the admin credentials of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_cluster_user_credentials"><CopyableCode code="list_cluster_user_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-server-fqdn"><code>server-fqdn</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Lists the user credentials of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_cluster_monitoring_user_credentials"><CopyableCode code="list_cluster_monitoring_user_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-server-fqdn"><code>server-fqdn</code></a></td>
    <td>Lists the cluster monitoring user credentials of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_outbound_network_dependencies_endpoints"><CopyableCode code="list_outbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. The operation returns properties of each egress endpoint.</td>
</tr>
<tr>
    <td><a href="#list_safeguards_versions"><CopyableCode code="list_safeguards_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of supported Safeguards versions in the specified subscription and location. Contains list of Safeguards version along with its support info and whether it is a default version.</td>
</tr>
<tr>
    <td><a href="#list_mesh_revision_profiles"><CopyableCode code="list_mesh_revision_profiles" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists mesh revision profiles for all meshes in the specified location. Contains extra metadata on each revision, including supported revisions, cluster compatibility and available upgrades.</td>
</tr>
<tr>
    <td><a href="#list_mesh_upgrade_profiles"><CopyableCode code="list_mesh_upgrade_profiles" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists available upgrades for all service meshes in a specific cluster.</td>
</tr>
<tr>
    <td><a href="#list_kubernetes_versions"><CopyableCode code="list_kubernetes_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of supported Kubernetes versions in the specified subscription. Contains extra metadata on the version, including supported patch versions, capabilities, available upgrades, and details on preview status of the version.</td>
</tr>
<tr>
    <td><a href="#get_access_profile"><CopyableCode code="get_access_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-role_name"><code>role_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an access profile of a managed cluster. **WARNING**: This API will be deprecated. Instead use `ListClusterUserCredentials `_ or `ListClusterAdminCredentials `_ .</td>
</tr>
<tr>
    <td><a href="#get_upgrade_profile"><CopyableCode code="get_upgrade_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the upgrade profile of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#get_safeguards_versions"><CopyableCode code="get_safeguards_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets supported Safeguards version in the specified subscription and location. Contains Safeguards version along with its support info and whether it is a default version.</td>
</tr>
<tr>
    <td><a href="#reset_service_principal_profile"><CopyableCode code="reset_service_principal_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-clientId"><code>clientId</code></a></td>
    <td></td>
    <td>Reset the Service Principal Profile of a managed cluster. This action cannot be performed on a cluster that is not using a service principal.</td>
</tr>
<tr>
    <td><a href="#reset_aad_profile"><CopyableCode code="reset_aad_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reset the AAD Profile of a managed cluster. **WARNING**: This API will be deprecated. Please see `AKS-managed Azure Active Directory integration `_ to update your cluster with AKS-managed Azure AD.</td>
</tr>
<tr>
    <td><a href="#rotate_cluster_certificates"><CopyableCode code="rotate_cluster_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotates the certificates of a managed cluster. See `Certificate rotation `_ for more details about rotating managed cluster certificates.</td>
</tr>
<tr>
    <td><a href="#abort_latest_operation"><CopyableCode code="abort_latest_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Aborts last operation running on managed cluster. Aborts the currently running operation on the managed cluster. The Managed Cluster will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned.</td>
</tr>
<tr>
    <td><a href="#rotate_service_account_signing_keys"><CopyableCode code="rotate_service_account_signing_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotates the service account signing keys of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops a Managed Cluster. This can only be performed on Azure Virtual Machine Scale set backed clusters. Stopping a cluster stops the control plane and agent nodes entirely, while maintaining all object and cluster state. A cluster does not accrue charges while it is stopped. See `stopping a cluster `_ for more details about stopping a cluster.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a previously stopped Managed Cluster. See `starting a cluster `_ for more details about starting a cluster.</td>
</tr>
<tr>
    <td><a href="#run_command"><CopyableCode code="run_command" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-command"><code>command</code></a></td>
    <td></td>
    <td>Submits a command to run against the Managed Cluster. AKS will create a pod to run the command. This is primarily useful for private clusters. For more information see `AKS Run Command `_.</td>
</tr>
<tr>
    <td><a href="#rebalance_load_balancers"><CopyableCode code="rebalance_load_balancers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rebalance nodes across specific load balancers.</td>
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
<tr id="parameter-command_id">
    <td><CopyableCode code="command_id" /></td>
    <td><code>string</code></td>
    <td>Id of the command. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-mode">
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode of the mesh. Required.</td>
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
<tr id="parameter-role_name">
    <td><CopyableCode code="role_name" /></td>
    <td><code>string</code></td>
    <td>The name of the role for managed cluster accessProfile resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Safeguards version. Required.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Only apply to AAD clusters, specifies the format of returned kubeconfig. Format 'azure' will return azure auth-provider kubeconfig; format 'exec' will return exec format kubeconfig, which requires kubelogin binary in the path. Known values are: "azure" and "exec". Default value is None.</td>
</tr>
<tr id="parameter-ignore-pod-disruption-budget">
    <td><CopyableCode code="ignore-pod-disruption-budget" /></td>
    <td><code>boolean</code></td>
    <td>ignore-pod-disruption-budget=true to delete those pods on a node without considering Pod Disruption Budget. Default value is None.</td>
</tr>
<tr id="parameter-server-fqdn">
    <td><CopyableCode code="server-fqdn" /></td>
    <td><code>string</code></td>
    <td>server fqdn type for credentials to be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_command_result"
    values={[
        { label: 'get_command_result', value: 'get_command_result' },
        { label: 'get_mesh_upgrade_profile', value: 'get_mesh_upgrade_profile' },
        { label: 'get', value: 'get' },
        { label: 'get_guardrails_versions', value: 'get_guardrails_versions' },
        { label: 'get_mesh_revision_profile', value: 'get_mesh_revision_profile' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_guardrails_versions', value: 'list_guardrails_versions' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_command_result">

Gets the results of a command which has been run on the Managed Cluster.

```sql
SELECT
id,
exitCode,
finishedAt,
logs,
provisioningState,
reason,
startedAt
FROM azure.containerservice.managed_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND command_id = '{{ command_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_mesh_upgrade_profile">

Gets available upgrades for a service mesh in a cluster.

```sql
SELECT
id,
name,
compatibleWith,
revision,
systemData,
type,
upgrades
FROM azure.containerservice.managed_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND mode = '{{ mode }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a managed cluster.

```sql
SELECT
id,
name,
aadProfile,
addonProfiles,
agentPoolProfiles,
aiToolchainOperatorProfile,
apiServerAccessProfile,
autoScalerProfile,
autoUpgradeProfile,
azureMonitorProfile,
azurePortalFQDN,
bootstrapProfile,
controlPlaneScalingProfile,
creationData,
currentKubernetesVersion,
disableLocalAccounts,
diskEncryptionSetID,
dnsPrefix,
eTag,
enableFIPS,
enableNamespaceResources,
enableRBAC,
extendedLocation,
fqdn,
fqdnSubdomain,
healthMonitorProfile,
hostedSystemProfile,
httpProxyConfig,
identity,
identityProfile,
ingressProfile,
kind,
kubernetesVersion,
linuxProfile,
location,
maxAgentPools,
metricsProfile,
networkProfile,
nodeDisruptionProfile,
nodeProvisioningProfile,
nodeResourceGroup,
nodeResourceGroupProfile,
oidcIssuerProfile,
podIdentityProfile,
powerState,
privateFQDN,
privateLinkResources,
provisioningState,
publicNetworkAccess,
resourceUID,
schedulerProfile,
securityProfile,
serviceMeshProfile,
servicePrincipalProfile,
sku,
status,
storageProfile,
supportPlan,
systemData,
tags,
type,
upgradeSettings,
windowsProfile,
workloadAutoScalerProfile
FROM azure.containerservice.managed_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_guardrails_versions">

Gets supported Guardrails version in the specified subscription and location. Contains Guardrails version along with its support info and whether it is a default version.

```sql
SELECT
id,
name,
isDefaultVersion,
support,
systemData,
type
FROM azure.containerservice.managed_clusters
WHERE location = '{{ location }}' -- required
AND version = '{{ version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_mesh_revision_profile">

Gets a mesh revision profile for a specified mesh in the specified location. Contains extra metadata on the revision, including supported revisions, cluster compatibility and available upgrades.

```sql
SELECT
id,
name,
meshRevisions,
systemData,
type
FROM azure.containerservice.managed_clusters
WHERE location = '{{ location }}' -- required
AND mode = '{{ mode }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists managed clusters in the specified subscription and resource group.

```sql
SELECT
id,
name,
aadProfile,
addonProfiles,
agentPoolProfiles,
aiToolchainOperatorProfile,
apiServerAccessProfile,
autoScalerProfile,
autoUpgradeProfile,
azureMonitorProfile,
azurePortalFQDN,
bootstrapProfile,
controlPlaneScalingProfile,
creationData,
currentKubernetesVersion,
disableLocalAccounts,
diskEncryptionSetID,
dnsPrefix,
eTag,
enableFIPS,
enableNamespaceResources,
enableRBAC,
extendedLocation,
fqdn,
fqdnSubdomain,
healthMonitorProfile,
hostedSystemProfile,
httpProxyConfig,
identity,
identityProfile,
ingressProfile,
kind,
kubernetesVersion,
linuxProfile,
location,
maxAgentPools,
metricsProfile,
networkProfile,
nodeDisruptionProfile,
nodeProvisioningProfile,
nodeResourceGroup,
nodeResourceGroupProfile,
oidcIssuerProfile,
podIdentityProfile,
powerState,
privateFQDN,
privateLinkResources,
provisioningState,
publicNetworkAccess,
resourceUID,
schedulerProfile,
securityProfile,
serviceMeshProfile,
servicePrincipalProfile,
sku,
status,
storageProfile,
supportPlan,
systemData,
tags,
type,
upgradeSettings,
windowsProfile,
workloadAutoScalerProfile
FROM azure.containerservice.managed_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_guardrails_versions">

Gets a list of supported Guardrails versions in the specified subscription and location. Contains list of Guardrails version along with its support info and whether it is a default version.

```sql
SELECT
id,
name,
isDefaultVersion,
support,
systemData,
type
FROM azure.containerservice.managed_clusters
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of managed clusters in the specified subscription.

```sql
SELECT
id,
name,
aadProfile,
addonProfiles,
agentPoolProfiles,
aiToolchainOperatorProfile,
apiServerAccessProfile,
autoScalerProfile,
autoUpgradeProfile,
azureMonitorProfile,
azurePortalFQDN,
bootstrapProfile,
controlPlaneScalingProfile,
creationData,
currentKubernetesVersion,
disableLocalAccounts,
diskEncryptionSetID,
dnsPrefix,
eTag,
enableFIPS,
enableNamespaceResources,
enableRBAC,
extendedLocation,
fqdn,
fqdnSubdomain,
healthMonitorProfile,
hostedSystemProfile,
httpProxyConfig,
identity,
identityProfile,
ingressProfile,
kind,
kubernetesVersion,
linuxProfile,
location,
maxAgentPools,
metricsProfile,
networkProfile,
nodeDisruptionProfile,
nodeProvisioningProfile,
nodeResourceGroup,
nodeResourceGroupProfile,
oidcIssuerProfile,
podIdentityProfile,
powerState,
privateFQDN,
privateLinkResources,
provisioningState,
publicNetworkAccess,
resourceUID,
schedulerProfile,
securityProfile,
serviceMeshProfile,
servicePrincipalProfile,
sku,
status,
storageProfile,
supportPlan,
systemData,
tags,
type,
upgradeSettings,
windowsProfile,
workloadAutoScalerProfile
FROM azure.containerservice.managed_clusters
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

Creates or updates a managed cluster.

```sql
INSERT INTO azure.containerservice.managed_clusters (
tags,
location,
properties,
sku,
extendedLocation,
identity,
kind,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ extendedLocation }}',
'{{ identity }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
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
- name: managed_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_clusters resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the managed_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_clusters resource.
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
        Properties of a managed cluster.
      value:
        provisioningState: "{{ provisioningState }}"
        powerState:
          code: "{{ code }}"
        creationData:
          sourceResourceId: "{{ sourceResourceId }}"
        maxAgentPools: {{ maxAgentPools }}
        kubernetesVersion: "{{ kubernetesVersion }}"
        currentKubernetesVersion: "{{ currentKubernetesVersion }}"
        dnsPrefix: "{{ dnsPrefix }}"
        fqdnSubdomain: "{{ fqdnSubdomain }}"
        fqdn: "{{ fqdn }}"
        privateFQDN: "{{ privateFQDN }}"
        azurePortalFQDN: "{{ azurePortalFQDN }}"
        agentPoolProfiles:
          - eTag: "{{ eTag }}"
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
            availabilityZones: "{{ availabilityZones }}"
            enableNodePublicIP: {{ enableNodePublicIP }}
            nodePublicIPPrefixID: "{{ nodePublicIPPrefixID }}"
            scaleSetPriority: "{{ scaleSetPriority }}"
            scaleSetEvictionPolicy: "{{ scaleSetEvictionPolicy }}"
            spotMaxPrice: {{ spotMaxPrice }}
            tags: "{{ tags }}"
            nodeLabels: "{{ nodeLabels }}"
            nodeTaints: "{{ nodeTaints }}"
            nodeInitializationTaints: "{{ nodeInitializationTaints }}"
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
            virtualMachineNodesStatus: "{{ virtualMachineNodesStatus }}"
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
            name: "{{ name }}"
        linuxProfile:
          adminUsername: "{{ adminUsername }}"
          ssh:
            publicKeys:
              - keyData: "{{ keyData }}"
        windowsProfile:
          adminUsername: "{{ adminUsername }}"
          adminPassword: "{{ adminPassword }}"
          licenseType: "{{ licenseType }}"
          enableCSIProxy: {{ enableCSIProxy }}
          gmsaProfile:
            enabled: {{ enabled }}
            dnsServer: "{{ dnsServer }}"
            rootDomainName: "{{ rootDomainName }}"
        servicePrincipalProfile:
          clientId: "{{ clientId }}"
          secret: "{{ secret }}"
        addonProfiles: "{{ addonProfiles }}"
        podIdentityProfile:
          enabled: {{ enabled }}
          allowNetworkPluginKubenet: {{ allowNetworkPluginKubenet }}
          userAssignedIdentities:
            - name: "{{ name }}"
              namespace: "{{ namespace }}"
              bindingSelector: "{{ bindingSelector }}"
              identity:
                resourceId: "{{ resourceId }}"
                clientId: "{{ clientId }}"
                objectId: "{{ objectId }}"
              provisioningState: "{{ provisioningState }}"
              provisioningInfo:
                error:
                  error: "{{ error }}"
          userAssignedIdentityExceptions:
            - name: "{{ name }}"
              namespace: "{{ namespace }}"
              podLabels: "{{ podLabels }}"
        oidcIssuerProfile:
          issuerURL: "{{ issuerURL }}"
          enabled: {{ enabled }}
        nodeResourceGroup: "{{ nodeResourceGroup }}"
        nodeResourceGroupProfile:
          restrictionLevel: "{{ restrictionLevel }}"
        enableRBAC: {{ enableRBAC }}
        supportPlan: "{{ supportPlan }}"
        enableFIPS: {{ enableFIPS }}
        enableNamespaceResources: {{ enableNamespaceResources }}
        networkProfile:
          networkPlugin: "{{ networkPlugin }}"
          networkPluginMode: "{{ networkPluginMode }}"
          networkPolicy: "{{ networkPolicy }}"
          networkMode: "{{ networkMode }}"
          networkDataplane: "{{ networkDataplane }}"
          advancedNetworking:
            enabled: {{ enabled }}
            observability:
              enabled: {{ enabled }}
            security:
              enabled: {{ enabled }}
              advancedNetworkPolicies: "{{ advancedNetworkPolicies }}"
              transitEncryption:
                type: "{{ type }}"
            performance:
              accelerationMode: "{{ accelerationMode }}"
          podCidr: "{{ podCidr }}"
          serviceCidr: "{{ serviceCidr }}"
          dnsServiceIP: "{{ dnsServiceIP }}"
          outboundType: "{{ outboundType }}"
          loadBalancerSku: "{{ loadBalancerSku }}"
          loadBalancerProfile:
            managedOutboundIPs:
              count: {{ count }}
              countIPv6: {{ countIPv6 }}
            outboundIPPrefixes:
              publicIPPrefixes:
                - id: "{{ id }}"
            outboundIPs:
              publicIPs:
                - id: "{{ id }}"
            effectiveOutboundIPs:
              - id: "{{ id }}"
            allocatedOutboundPorts: {{ allocatedOutboundPorts }}
            idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
            enableMultipleStandardLoadBalancers: {{ enableMultipleStandardLoadBalancers }}
            backendPoolType: "{{ backendPoolType }}"
            clusterServiceLoadBalancerHealthProbeMode: "{{ clusterServiceLoadBalancerHealthProbeMode }}"
          bastionProfile:
            enabled: {{ enabled }}
            bastionId: "{{ bastionId }}"
            sku: "{{ sku }}"
            scaleUnits: {{ scaleUnits }}
            publicIpAddressId: "{{ publicIpAddressId }}"
          natGatewayProfile:
            managedOutboundIPProfile:
              count: {{ count }}
              countIPv6: {{ countIPv6 }}
            effectiveOutboundIPs:
              - id: "{{ id }}"
            outboundIPPrefixes:
              publicIPPrefixes:
                - "{{ publicIPPrefixes }}"
            outboundIPs:
              publicIPs:
                - "{{ publicIPs }}"
            idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
          staticEgressGatewayProfile:
            enabled: {{ enabled }}
          podCidrs:
            - "{{ podCidrs }}"
          serviceCidrs:
            - "{{ serviceCidrs }}"
          ipFamilies:
            - "{{ ipFamilies }}"
          podLinkLocalAccess: "{{ podLinkLocalAccess }}"
          kubeProxyConfig:
            enabled: {{ enabled }}
            mode: "{{ mode }}"
            ipvsConfig:
              scheduler: "{{ scheduler }}"
              tcpTimeoutSeconds: {{ tcpTimeoutSeconds }}
              tcpFinTimeoutSeconds: {{ tcpFinTimeoutSeconds }}
              udpTimeoutSeconds: {{ udpTimeoutSeconds }}
        aadProfile:
          managed: {{ managed }}
          enableAzureRBAC: {{ enableAzureRBAC }}
          adminGroupObjectIDs:
            - "{{ adminGroupObjectIDs }}"
          clientAppID: "{{ clientAppID }}"
          serverAppID: "{{ serverAppID }}"
          serverAppSecret: "{{ serverAppSecret }}"
          tenantID: "{{ tenantID }}"
        autoUpgradeProfile:
          upgradeChannel: "{{ upgradeChannel }}"
          nodeOSUpgradeChannel: "{{ nodeOSUpgradeChannel }}"
        upgradeSettings:
          overrideSettings:
            forceUpgrade: {{ forceUpgrade }}
            until: "{{ until }}"
        autoScalerProfile:
          balance-similar-node-groups: "{{ balance-similar-node-groups }}"
          daemonset-eviction-for-empty-nodes: {{ daemonset-eviction-for-empty-nodes }}
          daemonset-eviction-for-occupied-nodes: {{ daemonset-eviction-for-occupied-nodes }}
          ignore-daemonsets-utilization: {{ ignore-daemonsets-utilization }}
          expander: "{{ expander }}"
          max-empty-bulk-delete: "{{ max-empty-bulk-delete }}"
          max-graceful-termination-sec: "{{ max-graceful-termination-sec }}"
          max-node-provision-time: "{{ max-node-provision-time }}"
          max-total-unready-percentage: "{{ max-total-unready-percentage }}"
          new-pod-scale-up-delay: "{{ new-pod-scale-up-delay }}"
          ok-total-unready-count: "{{ ok-total-unready-count }}"
          scan-interval: "{{ scan-interval }}"
          scale-down-delay-after-add: "{{ scale-down-delay-after-add }}"
          scale-down-delay-after-delete: "{{ scale-down-delay-after-delete }}"
          scale-down-delay-after-failure: "{{ scale-down-delay-after-failure }}"
          scale-down-unneeded-time: "{{ scale-down-unneeded-time }}"
          scale-down-unready-time: "{{ scale-down-unready-time }}"
          scale-down-utilization-threshold: "{{ scale-down-utilization-threshold }}"
          skip-nodes-with-local-storage: "{{ skip-nodes-with-local-storage }}"
          skip-nodes-with-system-pods: "{{ skip-nodes-with-system-pods }}"
        apiServerAccessProfile:
          authorizedIPRanges:
            - "{{ authorizedIPRanges }}"
          enablePrivateCluster: {{ enablePrivateCluster }}
          privateDNSZone: "{{ privateDNSZone }}"
          enablePrivateClusterPublicFQDN: {{ enablePrivateClusterPublicFQDN }}
          disableRunCommand: {{ disableRunCommand }}
          enableVnetIntegration: {{ enableVnetIntegration }}
          subnetId: "{{ subnetId }}"
        diskEncryptionSetID: "{{ diskEncryptionSetID }}"
        identityProfile: "{{ identityProfile }}"
        privateLinkResources:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            groupId: "{{ groupId }}"
            requiredMembers: "{{ requiredMembers }}"
            privateLinkServiceID: "{{ privateLinkServiceID }}"
        disableLocalAccounts: {{ disableLocalAccounts }}
        httpProxyConfig:
          httpProxy: "{{ httpProxy }}"
          httpsProxy: "{{ httpsProxy }}"
          noProxy:
            - "{{ noProxy }}"
          effectiveNoProxy:
            - "{{ effectiveNoProxy }}"
          trustedCa: "{{ trustedCa }}"
          enabled: {{ enabled }}
        securityProfile:
          defender:
            logAnalyticsWorkspaceResourceId: "{{ logAnalyticsWorkspaceResourceId }}"
            securityMonitoring:
              enabled: {{ enabled }}
            securityGating:
              enabled: {{ enabled }}
              identities:
                - azureContainerRegistry: "{{ azureContainerRegistry }}"
                  identity:
                    resourceId: "{{ resourceId }}"
                    clientId: "{{ clientId }}"
                    objectId: "{{ objectId }}"
              allowSecretAccess: {{ allowSecretAccess }}
          azureKeyVaultKms:
            enabled: {{ enabled }}
            keyId: "{{ keyId }}"
            keyVaultNetworkAccess: "{{ keyVaultNetworkAccess }}"
            keyVaultResourceId: "{{ keyVaultResourceId }}"
          kubernetesResourceObjectEncryptionProfile:
            infrastructureEncryption: "{{ infrastructureEncryption }}"
          workloadIdentity:
            enabled: {{ enabled }}
          imageCleaner:
            enabled: {{ enabled }}
            intervalHours: {{ intervalHours }}
          imageIntegrity:
            enabled: {{ enabled }}
          nodeRestriction:
            enabled: {{ enabled }}
          customCATrustCertificates:
            - "{{ customCATrustCertificates }}"
          serviceAccountImagePullProfile:
            enabled: {{ enabled }}
            defaultManagedIdentityId: "{{ defaultManagedIdentityId }}"
        storageProfile:
          diskCSIDriver:
            enabled: {{ enabled }}
          fileCSIDriver:
            enabled: {{ enabled }}
          snapshotController:
            enabled: {{ enabled }}
          blobCSIDriver:
            enabled: {{ enabled }}
        ingressProfile:
          webAppRouting:
            enabled: {{ enabled }}
            gatewayAPIImplementations:
              appRoutingIstio:
                mode: "{{ mode }}"
            dnsZoneResourceIds:
              - "{{ dnsZoneResourceIds }}"
            nginx:
              defaultIngressControllerType: "{{ defaultIngressControllerType }}"
            identity:
              resourceId: "{{ resourceId }}"
              clientId: "{{ clientId }}"
              objectId: "{{ objectId }}"
            defaultDomain:
              enabled: {{ enabled }}
              domainName: "{{ domainName }}"
          gatewayAPI:
            installation: "{{ installation }}"
          applicationLoadBalancer:
            enabled: {{ enabled }}
            identity:
              resourceId: "{{ resourceId }}"
              clientId: "{{ clientId }}"
              objectId: "{{ objectId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        workloadAutoScalerProfile:
          keda:
            enabled: {{ enabled }}
          verticalPodAutoscaler:
            enabled: {{ enabled }}
            addonAutoscaling: "{{ addonAutoscaling }}"
        azureMonitorProfile:
          metrics:
            enabled: {{ enabled }}
            kubeStateMetrics:
              metricLabelsAllowlist: "{{ metricLabelsAllowlist }}"
              metricAnnotationsAllowList: "{{ metricAnnotationsAllowList }}"
            controlPlane:
              enabled: {{ enabled }}
          containerInsights:
            enabled: {{ enabled }}
            logAnalyticsWorkspaceResourceId: "{{ logAnalyticsWorkspaceResourceId }}"
            syslogPort: {{ syslogPort }}
            disableCustomMetrics: {{ disableCustomMetrics }}
            disablePrometheusMetricsScraping: {{ disablePrometheusMetricsScraping }}
            containerNetworkLogs: "{{ containerNetworkLogs }}"
          appMonitoring:
            autoInstrumentation:
              enabled: {{ enabled }}
            openTelemetryMetrics:
              enabled: {{ enabled }}
              httpPort: {{ httpPort }}
              grpcPort: {{ grpcPort }}
            openTelemetryLogsAndTraces:
              enabled: {{ enabled }}
              httpPort: {{ httpPort }}
              grpcPort: {{ grpcPort }}
        serviceMeshProfile:
          mode: "{{ mode }}"
          istio:
            components:
              ingressGateways:
                - mode: "{{ mode }}"
                  enabled: {{ enabled }}
              egressGateways:
                - enabled: {{ enabled }}
                  name: "{{ name }}"
                  namespace: "{{ namespace }}"
                  gatewayConfigurationName: "{{ gatewayConfigurationName }}"
              proxyRedirectionMechanism: "{{ proxyRedirectionMechanism }}"
            certificateAuthority:
              plugin:
                keyVaultId: "{{ keyVaultId }}"
                certObjectName: "{{ certObjectName }}"
                keyObjectName: "{{ keyObjectName }}"
                rootCertObjectName: "{{ rootCertObjectName }}"
                certChainObjectName: "{{ certChainObjectName }}"
            revisions:
              - "{{ revisions }}"
        resourceUID: "{{ resourceUID }}"
        metricsProfile:
          costAnalysis:
            enabled: {{ enabled }}
        nodeProvisioningProfile:
          mode: "{{ mode }}"
          defaultNodePools: "{{ defaultNodePools }}"
        bootstrapProfile:
          artifactSource: "{{ artifactSource }}"
          containerRegistryId: "{{ containerRegistryId }}"
        aiToolchainOperatorProfile:
          enabled: {{ enabled }}
        schedulerProfile:
          schedulerInstanceProfiles:
            upstream:
              schedulerConfigMode: "{{ schedulerConfigMode }}"
        hostedSystemProfile:
          enabled: {{ enabled }}
          systemNodeSubnetID: "{{ systemNodeSubnetID }}"
          nodeSubnetID: "{{ nodeSubnetID }}"
        healthMonitorProfile:
          enableContinuousControlPlaneAndAddonMonitor: {{ enableContinuousControlPlaneAndAddonMonitor }}
          enableOnDemandMonitor: {{ enableOnDemandMonitor }}
        controlPlaneScalingProfile:
          scalingSize: "{{ scalingSize }}"
        nodeDisruptionProfile:
          nodeDisruptionPolicy: "{{ nodeDisruptionPolicy }}"
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
    - name: sku
      description: |
        The managed cluster SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: extendedLocation
      description: |
        The extended location of the Virtual Machine.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: identity
      description: |
        The identity of the managed cluster, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        delegatedResources: "{{ delegatedResources }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        This is primarily used to expose different UI experiences in the portal for different kinds.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates tags on a managed cluster.

```sql
UPDATE azure.containerservice.managed_clusters
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
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
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a managed cluster.

```sql
REPLACE azure.containerservice.managed_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
eTag,
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a managed cluster.

```sql
DELETE FROM azure.containerservice.managed_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND ignore-pod-disruption-budget = '{{ ignore-pod-disruption-budget }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_cluster_admin_credentials"
    values={[
        { label: 'list_cluster_admin_credentials', value: 'list_cluster_admin_credentials' },
        { label: 'list_cluster_user_credentials', value: 'list_cluster_user_credentials' },
        { label: 'list_cluster_monitoring_user_credentials', value: 'list_cluster_monitoring_user_credentials' },
        { label: 'list_outbound_network_dependencies_endpoints', value: 'list_outbound_network_dependencies_endpoints' },
        { label: 'list_safeguards_versions', value: 'list_safeguards_versions' },
        { label: 'list_mesh_revision_profiles', value: 'list_mesh_revision_profiles' },
        { label: 'list_mesh_upgrade_profiles', value: 'list_mesh_upgrade_profiles' },
        { label: 'list_kubernetes_versions', value: 'list_kubernetes_versions' },
        { label: 'get_access_profile', value: 'get_access_profile' },
        { label: 'get_upgrade_profile', value: 'get_upgrade_profile' },
        { label: 'get_safeguards_versions', value: 'get_safeguards_versions' },
        { label: 'reset_service_principal_profile', value: 'reset_service_principal_profile' },
        { label: 'reset_aad_profile', value: 'reset_aad_profile' },
        { label: 'rotate_cluster_certificates', value: 'rotate_cluster_certificates' },
        { label: 'abort_latest_operation', value: 'abort_latest_operation' },
        { label: 'rotate_service_account_signing_keys', value: 'rotate_service_account_signing_keys' },
        { label: 'stop', value: 'stop' },
        { label: 'start', value: 'start' },
        { label: 'run_command', value: 'run_command' },
        { label: 'rebalance_load_balancers', value: 'rebalance_load_balancers' }
    ]}
>
<TabItem value="list_cluster_admin_credentials">

Lists the admin credentials of a managed cluster.

```sql
EXEC azure.containerservice.managed_clusters.list_cluster_admin_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@server-fqdn='{{ server-fqdn }}'
;
```
</TabItem>
<TabItem value="list_cluster_user_credentials">

Lists the user credentials of a managed cluster.

```sql
EXEC azure.containerservice.managed_clusters.list_cluster_user_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@server-fqdn='{{ server-fqdn }}', 
@format='{{ format }}'
;
```
</TabItem>
<TabItem value="list_cluster_monitoring_user_credentials">

Lists the cluster monitoring user credentials of a managed cluster.

```sql
EXEC azure.containerservice.managed_clusters.list_cluster_monitoring_user_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@server-fqdn='{{ server-fqdn }}'
;
```
</TabItem>
<TabItem value="list_outbound_network_dependencies_endpoints">

Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. The operation returns properties of each egress endpoint.

```sql
EXEC azure.containerservice.managed_clusters.list_outbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_safeguards_versions">

Gets a list of supported Safeguards versions in the specified subscription and location. Contains list of Safeguards version along with its support info and whether it is a default version.

```sql
EXEC azure.containerservice.managed_clusters.list_safeguards_versions 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_mesh_revision_profiles">

Lists mesh revision profiles for all meshes in the specified location. Contains extra metadata on each revision, including supported revisions, cluster compatibility and available upgrades.

```sql
EXEC azure.containerservice.managed_clusters.list_mesh_revision_profiles 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_mesh_upgrade_profiles">

Lists available upgrades for all service meshes in a specific cluster.

```sql
EXEC azure.containerservice.managed_clusters.list_mesh_upgrade_profiles 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_kubernetes_versions">

Gets a list of supported Kubernetes versions in the specified subscription. Contains extra metadata on the version, including supported patch versions, capabilities, available upgrades, and details on preview status of the version.

```sql
EXEC azure.containerservice.managed_clusters.list_kubernetes_versions 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_access_profile">

Gets an access profile of a managed cluster. **WARNING**: This API will be deprecated. Instead use `ListClusterUserCredentials `_ or `ListClusterAdminCredentials `_ .

```sql
EXEC azure.containerservice.managed_clusters.get_access_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@role_name='{{ role_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_upgrade_profile">

Gets the upgrade profile of a managed cluster.

```sql
EXEC azure.containerservice.managed_clusters.get_upgrade_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_safeguards_versions">

Gets supported Safeguards version in the specified subscription and location. Contains Safeguards version along with its support info and whether it is a default version.

```sql
EXEC azure.containerservice.managed_clusters.get_safeguards_versions 
@location='{{ location }}' --required, 
@version='{{ version }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_service_principal_profile">

Reset the Service Principal Profile of a managed cluster. This action cannot be performed on a cluster that is not using a service principal.

```sql
EXEC azure.containerservice.managed_clusters.reset_service_principal_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"clientId": "{{ clientId }}", 
"secret": "{{ secret }}"
}'
;
```
</TabItem>
<TabItem value="reset_aad_profile">

Reset the AAD Profile of a managed cluster. **WARNING**: This API will be deprecated. Please see `AKS-managed Azure Active Directory integration `_ to update your cluster with AKS-managed Azure AD.

```sql
EXEC azure.containerservice.managed_clusters.reset_aad_profile 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"managed": {{ managed }}, 
"enableAzureRBAC": {{ enableAzureRBAC }}, 
"adminGroupObjectIDs": "{{ adminGroupObjectIDs }}", 
"clientAppID": "{{ clientAppID }}", 
"serverAppID": "{{ serverAppID }}", 
"serverAppSecret": "{{ serverAppSecret }}", 
"tenantID": "{{ tenantID }}"
}'
;
```
</TabItem>
<TabItem value="rotate_cluster_certificates">

Rotates the certificates of a managed cluster. See `Certificate rotation `_ for more details about rotating managed cluster certificates.

```sql
EXEC azure.containerservice.managed_clusters.rotate_cluster_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="abort_latest_operation">

Aborts last operation running on managed cluster. Aborts the currently running operation on the managed cluster. The Managed Cluster will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned.

```sql
EXEC azure.containerservice.managed_clusters.abort_latest_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rotate_service_account_signing_keys">

Rotates the service account signing keys of a managed cluster.

```sql
EXEC azure.containerservice.managed_clusters.rotate_service_account_signing_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a Managed Cluster. This can only be performed on Azure Virtual Machine Scale set backed clusters. Stopping a cluster stops the control plane and agent nodes entirely, while maintaining all object and cluster state. A cluster does not accrue charges while it is stopped. See `stopping a cluster `_ for more details about stopping a cluster.

```sql
EXEC azure.containerservice.managed_clusters.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts a previously stopped Managed Cluster. See `starting a cluster `_ for more details about starting a cluster.

```sql
EXEC azure.containerservice.managed_clusters.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_command">

Submits a command to run against the Managed Cluster. AKS will create a pod to run the command. This is primarily useful for private clusters. For more information see `AKS Run Command `_.

```sql
EXEC azure.containerservice.managed_clusters.run_command 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"command": "{{ command }}", 
"context": "{{ context }}", 
"clusterToken": "{{ clusterToken }}"
}'
;
```
</TabItem>
<TabItem value="rebalance_load_balancers">

Rebalance nodes across specific load balancers.

```sql
EXEC azure.containerservice.managed_clusters.rebalance_load_balancers 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"loadBalancerNames": "{{ loadBalancerNames }}"
}'
;
```
</TabItem>
</Tabs>
