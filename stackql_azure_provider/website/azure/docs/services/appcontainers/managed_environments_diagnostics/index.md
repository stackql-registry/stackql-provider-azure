--- 
title: managed_environments_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments_diagnostics
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

Creates, updates, deletes, gets or lists a <code>managed_environments_diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_environments_diagnostics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.managed_environments_diagnostics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_root"
    values={[
        { label: 'get_root', value: 'get_root' }
    ]}
>
<TabItem value="get_root">

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
    <td><a href="#get_root"><CopyableCode code="get_root" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a Managed Environment. Get the properties of a Managed Environment used to host container apps.</td>
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
    defaultValue="get_root"
    values={[
        { label: 'get_root', value: 'get_root' }
    ]}
>
<TabItem value="get_root">

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
FROM azure.appcontainers.managed_environments_diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
