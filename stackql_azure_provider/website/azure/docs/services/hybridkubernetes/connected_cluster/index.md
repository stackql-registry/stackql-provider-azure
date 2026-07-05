--- 
title: connected_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_cluster
  - hybridkubernetes
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

Creates, updates, deletes, gets or lists a <code>connected_cluster</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connected_cluster" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridkubernetes.connected_cluster" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="aadProfile" /></td>
    <td><code>object</code></td>
    <td>AAD profile for the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPublicKeyCertificate" /></td>
    <td><code>string</code></td>
    <td>Base64 encoded public certificate used by the agent to do the initial handshake to the backend services in Azure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the agent running on the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="arcAgentProfile" /></td>
    <td><code>object</code></td>
    <td>Arc agentry configuration for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="arcAgentryConfigurations" /></td>
    <td><code>array</code></td>
    <td>Configuration settings for customizing the behavior of the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azureHybridBenefit" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Azure Hybrid Benefit is opted in. Known values are: "True", "False", and "NotApplicable". (True, False, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>Represents the connectivity status of the connected cluster. Known values are: "Connecting", "Connected", "Offline", "Expired", and "AgentNotInstalled". (Connecting, Connected, Offline, Expired, AgentNotInstalled)</td>
</tr>
<tr>
    <td><CopyableCode code="distribution" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes distribution running on this connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes distribution version on this connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>object</code></td>
    <td>Details of the gateway used by the Arc router for connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the connected cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructure" /></td>
    <td><code>string</code></td>
    <td>The infrastructure on which the Kubernetes cluster represented by this connected cluster is running on.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of connected cluster. "ProvisionedCluster" (ProvisionedCluster)</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version of the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectivityTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time representing the last instance when heart beat was received from the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityCertificateExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the managed identity certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="miscellaneousProperties" /></td>
    <td><code>object</code></td>
    <td>More properties related to the Connected Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="offering" /></td>
    <td><code>string</code></td>
    <td>Connected cluster offering.</td>
</tr>
<tr>
    <td><CopyableCode code="oidcIssuerProfile" /></td>
    <td><code>object</code></td>
    <td>Open ID Connect (OIDC) Issuer Profile for the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>This is populated only if privateLinkState is enabled. The resource id of the private link scope this connected cluster is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkState" /></td>
    <td><code>string</code></td>
    <td>Property which describes the state of private link on a connected cluster resource. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the connected cluster resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Security profile for the connected cluster.</td>
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
    <td><CopyableCode code="totalCoreCount" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores present in the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="totalNodeCount" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes present in the connected cluster resource.</td>
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
    <td>AAD profile for the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPublicKeyCertificate" /></td>
    <td><code>string</code></td>
    <td>Base64 encoded public certificate used by the agent to do the initial handshake to the backend services in Azure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the agent running on the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="arcAgentProfile" /></td>
    <td><code>object</code></td>
    <td>Arc agentry configuration for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="arcAgentryConfigurations" /></td>
    <td><code>array</code></td>
    <td>Configuration settings for customizing the behavior of the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azureHybridBenefit" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Azure Hybrid Benefit is opted in. Known values are: "True", "False", and "NotApplicable". (True, False, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>Represents the connectivity status of the connected cluster. Known values are: "Connecting", "Connected", "Offline", "Expired", and "AgentNotInstalled". (Connecting, Connected, Offline, Expired, AgentNotInstalled)</td>
</tr>
<tr>
    <td><CopyableCode code="distribution" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes distribution running on this connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes distribution version on this connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>object</code></td>
    <td>Details of the gateway used by the Arc router for connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the connected cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructure" /></td>
    <td><code>string</code></td>
    <td>The infrastructure on which the Kubernetes cluster represented by this connected cluster is running on.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of connected cluster. "ProvisionedCluster" (ProvisionedCluster)</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version of the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectivityTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time representing the last instance when heart beat was received from the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityCertificateExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the managed identity certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="miscellaneousProperties" /></td>
    <td><code>object</code></td>
    <td>More properties related to the Connected Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="offering" /></td>
    <td><code>string</code></td>
    <td>Connected cluster offering.</td>
</tr>
<tr>
    <td><CopyableCode code="oidcIssuerProfile" /></td>
    <td><code>object</code></td>
    <td>Open ID Connect (OIDC) Issuer Profile for the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>This is populated only if privateLinkState is enabled. The resource id of the private link scope this connected cluster is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkState" /></td>
    <td><code>string</code></td>
    <td>Property which describes the state of private link on a connected cluster resource. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the connected cluster resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Security profile for the connected cluster.</td>
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
    <td><CopyableCode code="totalCoreCount" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores present in the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="totalNodeCount" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes present in the connected cluster resource.</td>
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
    <td><CopyableCode code="aadProfile" /></td>
    <td><code>object</code></td>
    <td>AAD profile for the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPublicKeyCertificate" /></td>
    <td><code>string</code></td>
    <td>Base64 encoded public certificate used by the agent to do the initial handshake to the backend services in Azure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agentVersion" /></td>
    <td><code>string</code></td>
    <td>Version of the agent running on the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="arcAgentProfile" /></td>
    <td><code>object</code></td>
    <td>Arc agentry configuration for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="arcAgentryConfigurations" /></td>
    <td><code>array</code></td>
    <td>Configuration settings for customizing the behavior of the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="azureHybridBenefit" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Azure Hybrid Benefit is opted in. Known values are: "True", "False", and "NotApplicable". (True, False, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityStatus" /></td>
    <td><code>string</code></td>
    <td>Represents the connectivity status of the connected cluster. Known values are: "Connecting", "Connected", "Offline", "Expired", and "AgentNotInstalled". (Connecting, Connected, Offline, Expired, AgentNotInstalled)</td>
</tr>
<tr>
    <td><CopyableCode code="distribution" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes distribution running on this connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="distributionVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes distribution version on this connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>object</code></td>
    <td>Details of the gateway used by the Arc router for connectivity.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the connected cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructure" /></td>
    <td><code>string</code></td>
    <td>The infrastructure on which the Kubernetes cluster represented by this connected cluster is running on.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of connected cluster. "ProvisionedCluster" (ProvisionedCluster)</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes version of the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectivityTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time representing the last instance when heart beat was received from the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentityCertificateExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration time of the managed identity certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="miscellaneousProperties" /></td>
    <td><code>object</code></td>
    <td>More properties related to the Connected Cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="offering" /></td>
    <td><code>string</code></td>
    <td>Connected cluster offering.</td>
</tr>
<tr>
    <td><CopyableCode code="oidcIssuerProfile" /></td>
    <td><code>object</code></td>
    <td>Open ID Connect (OIDC) Issuer Profile for the connected cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkScopeResourceId" /></td>
    <td><code>string</code></td>
    <td>This is populated only if privateLinkState is enabled. The resource id of the private link scope this connected cluster is assigned to, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkState" /></td>
    <td><code>string</code></td>
    <td>Property which describes the state of private link on a connected cluster resource. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the connected cluster resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Security profile for the connected cluster.</td>
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
    <td><CopyableCode code="totalCoreCount" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores present in the connected cluster resource.</td>
</tr>
<tr>
    <td><CopyableCode code="totalNodeCount" /></td>
    <td><code>integer</code></td>
    <td>Number of nodes present in the connected cluster resource.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of the specified connected cluster. Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all connected clusters in the given Resource Group. API to enumerate registered connected K8s clusters under a Resource Group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all connected clusters in the given Subscription. API to enumerate registered connected K8s clusters under a Subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-identity"><code>identity</code></a></td>
    <td></td>
    <td>Register a new Kubernetes cluster with Azure Resource Manager. API to register a new Kubernetes cluster and create or replace a connected cluster tracked resource in Azure Resource Manager (ARM).</td>
</tr>
<tr>
    <td><a href="#update_async"><CopyableCode code="update_async" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a connected cluster. API to update certain properties of the connected cluster resource.</td>
</tr>
<tr>
    <td><a href="#create_or_replace"><CopyableCode code="create_or_replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a>, <a href="#parameter-identity"><code>identity</code></a></td>
    <td></td>
    <td>Register a new Kubernetes cluster with Azure Resource Manager. API to register a new Kubernetes cluster and create or replace a connected cluster tracked resource in Azure Resource Manager (ARM).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a connected cluster. Delete a connected cluster, removing the tracked resource in Azure Resource Manager (ARM).</td>
</tr>
<tr>
    <td><a href="#list_cluster_user_credential"><CopyableCode code="list_cluster_user_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-authenticationMethod"><code>authenticationMethod</code></a>, <a href="#parameter-clientProxy"><code>clientProxy</code></a></td>
    <td></td>
    <td>Gets cluster user credentials of a connected cluster. Gets cluster user credentials of the connected cluster with a specified resource group and name.</td>
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
    <td>The name of the Kubernetes cluster on which get is called. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get the properties of the specified connected cluster. Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details.

```sql
SELECT
id,
name,
aadProfile,
agentPublicKeyCertificate,
agentVersion,
arcAgentProfile,
arcAgentryConfigurations,
azureHybridBenefit,
connectivityStatus,
distribution,
distributionVersion,
gateway,
identity,
infrastructure,
kind,
kubernetesVersion,
lastConnectivityTime,
location,
managedIdentityCertificateExpirationTime,
miscellaneousProperties,
offering,
oidcIssuerProfile,
privateLinkScopeResourceId,
privateLinkState,
provisioningState,
securityProfile,
systemData,
tags,
totalCoreCount,
totalNodeCount,
type
FROM azure.hybridkubernetes.connected_cluster
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all connected clusters in the given Resource Group. API to enumerate registered connected K8s clusters under a Resource Group.

```sql
SELECT
id,
name,
aadProfile,
agentPublicKeyCertificate,
agentVersion,
arcAgentProfile,
arcAgentryConfigurations,
azureHybridBenefit,
connectivityStatus,
distribution,
distributionVersion,
gateway,
identity,
infrastructure,
kind,
kubernetesVersion,
lastConnectivityTime,
location,
managedIdentityCertificateExpirationTime,
miscellaneousProperties,
offering,
oidcIssuerProfile,
privateLinkScopeResourceId,
privateLinkState,
provisioningState,
securityProfile,
systemData,
tags,
totalCoreCount,
totalNodeCount,
type
FROM azure.hybridkubernetes.connected_cluster
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all connected clusters in the given Subscription. API to enumerate registered connected K8s clusters under a Subscription.

```sql
SELECT
id,
name,
aadProfile,
agentPublicKeyCertificate,
agentVersion,
arcAgentProfile,
arcAgentryConfigurations,
azureHybridBenefit,
connectivityStatus,
distribution,
distributionVersion,
gateway,
identity,
infrastructure,
kind,
kubernetesVersion,
lastConnectivityTime,
location,
managedIdentityCertificateExpirationTime,
miscellaneousProperties,
offering,
oidcIssuerProfile,
privateLinkScopeResourceId,
privateLinkState,
provisioningState,
securityProfile,
systemData,
tags,
totalCoreCount,
totalNodeCount,
type
FROM azure.hybridkubernetes.connected_cluster
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_replace">

Register a new Kubernetes cluster with Azure Resource Manager. API to register a new Kubernetes cluster and create or replace a connected cluster tracked resource in Azure Resource Manager (ARM).

```sql
INSERT INTO azure.hybridkubernetes.connected_cluster (
tags,
location,
properties,
identity,
kind,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}' /* required */,
'{{ kind }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: connected_cluster
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connected_cluster resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the connected_cluster resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connected_cluster resource.
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
        Describes the connected cluster resource properties. Required.
      value:
        agentPublicKeyCertificate: "{{ agentPublicKeyCertificate }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        totalNodeCount: {{ totalNodeCount }}
        totalCoreCount: {{ totalCoreCount }}
        agentVersion: "{{ agentVersion }}"
        provisioningState: "{{ provisioningState }}"
        distribution: "{{ distribution }}"
        distributionVersion: "{{ distributionVersion }}"
        infrastructure: "{{ infrastructure }}"
        offering: "{{ offering }}"
        managedIdentityCertificateExpirationTime: "{{ managedIdentityCertificateExpirationTime }}"
        lastConnectivityTime: "{{ lastConnectivityTime }}"
        connectivityStatus: "{{ connectivityStatus }}"
        privateLinkState: "{{ privateLinkState }}"
        privateLinkScopeResourceId: "{{ privateLinkScopeResourceId }}"
        azureHybridBenefit: "{{ azureHybridBenefit }}"
        aadProfile:
          enableAzureRBAC: {{ enableAzureRBAC }}
          adminGroupObjectIDs:
            - "{{ adminGroupObjectIDs }}"
          tenantID: "{{ tenantID }}"
        arcAgentProfile:
          desiredAgentVersion: "{{ desiredAgentVersion }}"
          agentAutoUpgrade: "{{ agentAutoUpgrade }}"
          systemComponents:
            - type: "{{ type }}"
              userSpecifiedVersion: "{{ userSpecifiedVersion }}"
              majorVersion: {{ majorVersion }}
              currentVersion: "{{ currentVersion }}"
          agentErrors:
            - message: "{{ message }}"
              severity: "{{ severity }}"
              component: "{{ component }}"
              time: "{{ time }}"
          agentState: "{{ agentState }}"
        securityProfile:
          workloadIdentity:
            enabled: {{ enabled }}
        oidcIssuerProfile:
          enabled: {{ enabled }}
          issuerUrl: "{{ issuerUrl }}"
          selfHostedIssuerUrl: "{{ selfHostedIssuerUrl }}"
        gateway:
          enabled: {{ enabled }}
        arcAgentryConfigurations:
          - feature: "{{ feature }}"
            settings: "{{ settings }}"
            protectedSettings: "{{ protectedSettings }}"
        miscellaneousProperties: "{{ miscellaneousProperties }}"
    - name: identity
      description: |
        The identity of the connected cluster. Required.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of connected cluster. "ProvisionedCluster"
      valid_values: ['ProvisionedCluster']
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_async"
    values={[
        { label: 'update_async', value: 'update_async' }
    ]}
>
<TabItem value="update_async">

Updates a connected cluster. API to update certain properties of the connected cluster resource.

```sql
UPDATE azure.hybridkubernetes.connected_cluster
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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
    defaultValue="create_or_replace"
    values={[
        { label: 'create_or_replace', value: 'create_or_replace' }
    ]}
>
<TabItem value="create_or_replace">

Register a new Kubernetes cluster with Azure Resource Manager. API to register a new Kubernetes cluster and create or replace a connected cluster tracked resource in Azure Resource Manager (ARM).

```sql
REPLACE azure.hybridkubernetes.connected_cluster
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
AND identity = '{{ identity }}' --required
RETURNING
id,
name,
identity,
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

Delete a connected cluster. Delete a connected cluster, removing the tracked resource in Azure Resource Manager (ARM).

```sql
DELETE FROM azure.hybridkubernetes.connected_cluster
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_cluster_user_credential"
    values={[
        { label: 'list_cluster_user_credential', value: 'list_cluster_user_credential' }
    ]}
>
<TabItem value="list_cluster_user_credential">

Gets cluster user credentials of a connected cluster. Gets cluster user credentials of the connected cluster with a specified resource group and name.

```sql
EXEC azure.hybridkubernetes.connected_cluster.list_cluster_user_credential 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"authenticationMethod": "{{ authenticationMethod }}", 
"clientProxy": {{ clientProxy }}
}'
;
```
</TabItem>
</Tabs>
