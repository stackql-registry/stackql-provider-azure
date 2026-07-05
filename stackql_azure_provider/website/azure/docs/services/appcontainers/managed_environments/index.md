--- 
title: managed_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>managed_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.managed_environments" /></td></tr>
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
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to configured destination.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainConfiguration" /></td>
    <td><code>object</code></td>
    <td>Custom domain configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights connection string used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIInstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="daprConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of Dapr component.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDomain" /></td>
    <td><code>string</code></td>
    <td>Default Domain Name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressConfiguration" /></td>
    <td><code>object</code></td>
    <td>Ingress configuration for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="kedaConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of Keda component.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peerAuthentication" /></td>
    <td><code>object</code></td>
    <td>Peer authentication settings for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="peerTrafficConfiguration" /></td>
    <td><code>object</code></td>
    <td>Peer traffic settings for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", and "UpgradeFailed". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete, UpgradeRequested, UpgradeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the Environment.</td>
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
    <td><CopyableCode code="vnetConfiguration" /></td>
    <td><code>object</code></td>
    <td>Vnet configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfiles" /></td>
    <td><code>array</code></td>
    <td>Workload profiles configured for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this Managed Environment is zone-redundant.</td>
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
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to configured destination.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainConfiguration" /></td>
    <td><code>object</code></td>
    <td>Custom domain configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights connection string used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIInstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="daprConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of Dapr component.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDomain" /></td>
    <td><code>string</code></td>
    <td>Default Domain Name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressConfiguration" /></td>
    <td><code>object</code></td>
    <td>Ingress configuration for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="kedaConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of Keda component.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peerAuthentication" /></td>
    <td><code>object</code></td>
    <td>Peer authentication settings for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="peerTrafficConfiguration" /></td>
    <td><code>object</code></td>
    <td>Peer traffic settings for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", and "UpgradeFailed". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete, UpgradeRequested, UpgradeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the Environment.</td>
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
    <td><CopyableCode code="vnetConfiguration" /></td>
    <td><code>object</code></td>
    <td>Vnet configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfiles" /></td>
    <td><code>array</code></td>
    <td>Workload profiles configured for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this Managed Environment is zone-redundant.</td>
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
    <td><CopyableCode code="appLogsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Cluster configuration which enables the log daemon to export app logs to configured destination.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainConfiguration" /></td>
    <td><code>object</code></td>
    <td>Custom domain configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIConnectionString" /></td>
    <td><code>string</code></td>
    <td>Application Insights connection string used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="daprAIInstrumentationKey" /></td>
    <td><code>string</code></td>
    <td>Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry.</td>
</tr>
<tr>
    <td><CopyableCode code="daprConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of Dapr component.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDomain" /></td>
    <td><code>string</code></td>
    <td>Default Domain Name for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentErrors" /></td>
    <td><code>string</code></td>
    <td>Any errors that occurred during deployment or deployment validation.</td>
</tr>
<tr>
    <td><CopyableCode code="eventStreamEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint of the eventstream of the Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressConfiguration" /></td>
    <td><code>object</code></td>
    <td>Ingress configuration for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="kedaConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration of Keda component.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="peerAuthentication" /></td>
    <td><code>object</code></td>
    <td>Peer authentication settings for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="peerTrafficConfiguration" /></td>
    <td><code>object</code></td>
    <td>Peer traffic settings for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private endpoint connections to the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Environment. Known values are: "Succeeded", "Failed", "Canceled", "Waiting", "InitializationInProgress", "InfrastructureSetupInProgress", "InfrastructureSetupComplete", "ScheduledForDelete", "UpgradeRequested", and "UpgradeFailed". (Succeeded, Failed, Canceled, Waiting, InitializationInProgress, InfrastructureSetupInProgress, InfrastructureSetupComplete, ScheduledForDelete, UpgradeRequested, UpgradeFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="staticIp" /></td>
    <td><code>string</code></td>
    <td>Static IP of the Environment.</td>
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
    <td><CopyableCode code="vnetConfiguration" /></td>
    <td><code>object</code></td>
    <td>Vnet configuration for the environment.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfiles" /></td>
    <td><code>array</code></td>
    <td>Workload profiles configured for the Managed Environment.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this Managed Environment is zone-redundant.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Managed Environment. Get the properties of a Managed Environment used to host container apps.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all the Environments in a resource group. Get all the Managed Environments in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Environments for a subscription. Get all Managed Environments for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Managed Environment. Creates or updates a Managed Environment used to host container apps.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Update Managed Environment's properties. Patches a Managed Environment using JSON Merge Patch.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Managed Environment. Creates or updates a Managed Environment used to host container apps.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Managed Environment. Delete a Managed Environment if it does not have any container apps.</td>
</tr>
<tr>
    <td><a href="#list_workload_profile_states"><CopyableCode code="list_workload_profile_states" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all workload Profile States for a Managed Environment.. Get all workload Profile States for a Managed Environment.</td>
</tr>
<tr>
    <td><a href="#get_auth_token"><CopyableCode code="get_auth_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get auth token for a managed environment. Checks if resource name is available.</td>
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
<tr id="parameter-environment_name">
    <td><CopyableCode code="environment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Environment. Required.</td>
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

Get the properties of a Managed Environment. Get the properties of a Managed Environment used to host container apps.

```sql
SELECT
id,
name,
appLogsConfiguration,
customDomainConfiguration,
daprAIConnectionString,
daprAIInstrumentationKey,
daprConfiguration,
defaultDomain,
deploymentErrors,
eventStreamEndpoint,
identity,
infrastructureResourceGroup,
ingressConfiguration,
kedaConfiguration,
kind,
location,
peerAuthentication,
peerTrafficConfiguration,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
staticIp,
systemData,
tags,
type,
vnetConfiguration,
workloadProfiles,
zoneRedundant
FROM azure.appcontainers.managed_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all the Environments in a resource group. Get all the Managed Environments in a resource group.

```sql
SELECT
id,
name,
appLogsConfiguration,
customDomainConfiguration,
daprAIConnectionString,
daprAIInstrumentationKey,
daprConfiguration,
defaultDomain,
deploymentErrors,
eventStreamEndpoint,
identity,
infrastructureResourceGroup,
ingressConfiguration,
kedaConfiguration,
kind,
location,
peerAuthentication,
peerTrafficConfiguration,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
staticIp,
systemData,
tags,
type,
vnetConfiguration,
workloadProfiles,
zoneRedundant
FROM azure.appcontainers.managed_environments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get all Environments for a subscription. Get all Managed Environments for a subscription.

```sql
SELECT
id,
name,
appLogsConfiguration,
customDomainConfiguration,
daprAIConnectionString,
daprAIInstrumentationKey,
daprConfiguration,
defaultDomain,
deploymentErrors,
eventStreamEndpoint,
identity,
infrastructureResourceGroup,
ingressConfiguration,
kedaConfiguration,
kind,
location,
peerAuthentication,
peerTrafficConfiguration,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
staticIp,
systemData,
tags,
type,
vnetConfiguration,
workloadProfiles,
zoneRedundant
FROM azure.appcontainers.managed_environments
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

Creates or updates a Managed Environment. Creates or updates a Managed Environment used to host container apps.

```sql
INSERT INTO azure.appcontainers.managed_environments (
tags,
location,
properties,
kind,
identity,
resource_group_name,
environment_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ environment_name }}',
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
- name: managed_environments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_environments resource.
    - name: environment_name
      value: "{{ environment_name }}"
      description: Required parameter for the managed_environments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_environments resource.
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
        Managed environment resource specific properties.
      value:
        provisioningState: "{{ provisioningState }}"
        daprAIInstrumentationKey: "{{ daprAIInstrumentationKey }}"
        daprAIConnectionString: "{{ daprAIConnectionString }}"
        vnetConfiguration:
          internal: {{ internal }}
          infrastructureSubnetId: "{{ infrastructureSubnetId }}"
          dockerBridgeCidr: "{{ dockerBridgeCidr }}"
          platformReservedCidr: "{{ platformReservedCidr }}"
          platformReservedDnsIP: "{{ platformReservedDnsIP }}"
        deploymentErrors: "{{ deploymentErrors }}"
        defaultDomain: "{{ defaultDomain }}"
        staticIp: "{{ staticIp }}"
        appLogsConfiguration:
          destination: "{{ destination }}"
          logAnalyticsConfiguration:
            customerId: "{{ customerId }}"
            sharedKey: "{{ sharedKey }}"
        zoneRedundant: {{ zoneRedundant }}
        customDomainConfiguration:
          customDomainVerificationId: "{{ customDomainVerificationId }}"
          dnsSuffix: "{{ dnsSuffix }}"
          certificateKeyVaultProperties:
            identity: "{{ identity }}"
            keyVaultUrl: "{{ keyVaultUrl }}"
          certificateValue: "{{ certificateValue }}"
          certificatePassword: "{{ certificatePassword }}"
          expirationDate: "{{ expirationDate }}"
          thumbprint: "{{ thumbprint }}"
          subjectName: "{{ subjectName }}"
        eventStreamEndpoint: "{{ eventStreamEndpoint }}"
        workloadProfiles:
          - name: "{{ name }}"
            workloadProfileType: "{{ workloadProfileType }}"
            minimumCount: {{ minimumCount }}
            maximumCount: {{ maximumCount }}
        kedaConfiguration:
          version: "{{ version }}"
        daprConfiguration:
          version: "{{ version }}"
        infrastructureResourceGroup: "{{ infrastructureResourceGroup }}"
        peerAuthentication:
          mtls:
            enabled: {{ enabled }}
        peerTrafficConfiguration:
          encryption:
            enabled: {{ enabled }}
        ingressConfiguration:
          workloadProfileName: "{{ workloadProfileName }}"
          terminationGracePeriodSeconds: {{ terminationGracePeriodSeconds }}
          headerCountLimit: {{ headerCountLimit }}
          requestIdleTimeout: {{ requestIdleTimeout }}
        privateEndpointConnections:
          - id: "{{ id }}"
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
              groupIds:
                - "{{ groupIds }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of the Environment.
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

Update Managed Environment's properties. Patches a Managed Environment using JSON Merge Patch.

```sql
UPDATE azure.appcontainers.managed_environments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a Managed Environment. Creates or updates a Managed Environment used to host container apps.

```sql
REPLACE azure.appcontainers.managed_environments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Delete a Managed Environment. Delete a Managed Environment if it does not have any container apps.

```sql
DELETE FROM azure.appcontainers.managed_environments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_workload_profile_states"
    values={[
        { label: 'list_workload_profile_states', value: 'list_workload_profile_states' },
        { label: 'get_auth_token', value: 'get_auth_token' }
    ]}
>
<TabItem value="list_workload_profile_states">

Get all workload Profile States for a Managed Environment.. Get all workload Profile States for a Managed Environment.

```sql
EXEC azure.appcontainers.managed_environments.list_workload_profile_states 
@resource_group_name='{{ resource_group_name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_auth_token">

Get auth token for a managed environment. Checks if resource name is available.

```sql
EXEC azure.appcontainers.managed_environments.get_auth_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@environment_name='{{ environment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
