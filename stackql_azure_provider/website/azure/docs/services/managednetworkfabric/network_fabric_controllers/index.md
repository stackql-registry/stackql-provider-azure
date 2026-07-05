--- 
title: network_fabric_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabric_controllers
  - managednetworkfabric
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

Creates, updates, deletes, gets or lists a <code>network_fabric_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_fabric_controllers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managednetworkfabric.network_fabric_controllers" /></td></tr>
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
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureExpressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute).</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureServices" /></td>
    <td><code>object</code></td>
    <td>InfrastructureServices IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4AddressSpace" /></td>
    <td><code>string</code></td>
    <td>IPv4 Network Fabric Controller Address Space.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6AddressSpace" /></td>
    <td><code>string</code></td>
    <td>IPv6 Network Fabric Controller Address Space.</td>
</tr>
<tr>
    <td><CopyableCode code="isWorkloadManagementNetworkEnabled" /></td>
    <td><code>string</code></td>
    <td>A workload management network is required for all the tenant (workload) traffic. This traffic is only dedicated for Tenant workloads which are required to access internet or any other MSFT/Public endpoints. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed Resource Group configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricIds" /></td>
    <td><code>array</code></td>
    <td>The NF-ID will be an input parameter used by the NF to link and get associated with the parent NFC Service.</td>
</tr>
<tr>
    <td><CopyableCode code="nfcSku" /></td>
    <td><code>string</code></td>
    <td>Network Fabric Controller SKU. Known values are: "Basic", "Standard", and "HighPerformance". (Basic, Standard, HighPerformance)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
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
    <td><CopyableCode code="tenantInternetGatewayIds" /></td>
    <td><code>array</code></td>
    <td>List of tenant InternetGateway resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadExpressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).</td>
</tr>
<tr>
    <td><CopyableCode code="workloadServices" /></td>
    <td><code>object</code></td>
    <td>WorkloadServices IP ranges.</td>
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
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureExpressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute).</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureServices" /></td>
    <td><code>object</code></td>
    <td>InfrastructureServices IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4AddressSpace" /></td>
    <td><code>string</code></td>
    <td>IPv4 Network Fabric Controller Address Space.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6AddressSpace" /></td>
    <td><code>string</code></td>
    <td>IPv6 Network Fabric Controller Address Space.</td>
</tr>
<tr>
    <td><CopyableCode code="isWorkloadManagementNetworkEnabled" /></td>
    <td><code>string</code></td>
    <td>A workload management network is required for all the tenant (workload) traffic. This traffic is only dedicated for Tenant workloads which are required to access internet or any other MSFT/Public endpoints. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed Resource Group configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricIds" /></td>
    <td><code>array</code></td>
    <td>The NF-ID will be an input parameter used by the NF to link and get associated with the parent NFC Service.</td>
</tr>
<tr>
    <td><CopyableCode code="nfcSku" /></td>
    <td><code>string</code></td>
    <td>Network Fabric Controller SKU. Known values are: "Basic", "Standard", and "HighPerformance". (Basic, Standard, HighPerformance)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
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
    <td><CopyableCode code="tenantInternetGatewayIds" /></td>
    <td><code>array</code></td>
    <td>List of tenant InternetGateway resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadExpressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).</td>
</tr>
<tr>
    <td><CopyableCode code="workloadServices" /></td>
    <td><code>object</code></td>
    <td>WorkloadServices IP ranges.</td>
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
    <td><CopyableCode code="annotation" /></td>
    <td><code>string</code></td>
    <td>Switch configuration description.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureExpressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute).</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureServices" /></td>
    <td><code>object</code></td>
    <td>InfrastructureServices IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4AddressSpace" /></td>
    <td><code>string</code></td>
    <td>IPv4 Network Fabric Controller Address Space.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6AddressSpace" /></td>
    <td><code>string</code></td>
    <td>IPv6 Network Fabric Controller Address Space.</td>
</tr>
<tr>
    <td><CopyableCode code="isWorkloadManagementNetworkEnabled" /></td>
    <td><code>string</code></td>
    <td>A workload management network is required for all the tenant (workload) traffic. This traffic is only dedicated for Tenant workloads which are required to access internet or any other MSFT/Public endpoints. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperation" /></td>
    <td><code>object</code></td>
    <td>Details of the last operation performed on the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed Resource Group configuration properties.</td>
</tr>
<tr>
    <td><CopyableCode code="networkFabricIds" /></td>
    <td><code>array</code></td>
    <td>The NF-ID will be an input parameter used by the NF to link and get associated with the parent NFC Service.</td>
</tr>
<tr>
    <td><CopyableCode code="nfcSku" /></td>
    <td><code>string</code></td>
    <td>Network Fabric Controller SKU. Known values are: "Basic", "Standard", and "HighPerformance". (Basic, Standard, HighPerformance)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning. Known values are: "Accepted", "Succeeded", "Updating", "Deleting", "Failed", and "Canceled". (Accepted, Succeeded, Updating, Deleting, Failed, Canceled)</td>
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
    <td><CopyableCode code="tenantInternetGatewayIds" /></td>
    <td><code>array</code></td>
    <td>List of tenant InternetGateway resource IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadExpressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).</td>
</tr>
<tr>
    <td><CopyableCode code="workloadServices" /></td>
    <td><code>object</code></td>
    <td>WorkloadServices IP ranges.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_controller_name"><code>network_fabric_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Shows the provisioning status of Network Fabric Controller.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the NetworkFabricControllers thats available in the resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the NetworkFabricControllers by subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_controller_name"><code>network_fabric_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a Network Fabric Controller.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_controller_name"><code>network_fabric_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates are currently not supported for the Network Fabric Controller resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_fabric_controller_name"><code>network_fabric_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the Network Fabric Controller resource.</td>
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
<tr id="parameter-network_fabric_controller_name">
    <td><CopyableCode code="network_fabric_controller_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Fabric Controller. Required.</td>
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

Shows the provisioning status of Network Fabric Controller.

```sql
SELECT
id,
name,
annotation,
identity,
infrastructureExpressRouteConnections,
infrastructureServices,
ipv4AddressSpace,
ipv6AddressSpace,
isWorkloadManagementNetworkEnabled,
lastOperation,
location,
managedResourceGroupConfiguration,
networkFabricIds,
nfcSku,
provisioningState,
systemData,
tags,
tenantInternetGatewayIds,
type,
workloadExpressRouteConnections,
workloadServices
FROM azure.managednetworkfabric.network_fabric_controllers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_fabric_controller_name = '{{ network_fabric_controller_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all the NetworkFabricControllers thats available in the resource group.

```sql
SELECT
id,
name,
annotation,
identity,
infrastructureExpressRouteConnections,
infrastructureServices,
ipv4AddressSpace,
ipv6AddressSpace,
isWorkloadManagementNetworkEnabled,
lastOperation,
location,
managedResourceGroupConfiguration,
networkFabricIds,
nfcSku,
provisioningState,
systemData,
tags,
tenantInternetGatewayIds,
type,
workloadExpressRouteConnections,
workloadServices
FROM azure.managednetworkfabric.network_fabric_controllers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all the NetworkFabricControllers by subscription.

```sql
SELECT
id,
name,
annotation,
identity,
infrastructureExpressRouteConnections,
infrastructureServices,
ipv4AddressSpace,
ipv6AddressSpace,
isWorkloadManagementNetworkEnabled,
lastOperation,
location,
managedResourceGroupConfiguration,
networkFabricIds,
nfcSku,
provisioningState,
systemData,
tags,
tenantInternetGatewayIds,
type,
workloadExpressRouteConnections,
workloadServices
FROM azure.managednetworkfabric.network_fabric_controllers
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

Creates a Network Fabric Controller.

```sql
INSERT INTO azure.managednetworkfabric.network_fabric_controllers (
tags,
location,
properties,
identity,
resource_group_name,
network_fabric_controller_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_fabric_controller_name }}',
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
- name: network_fabric_controllers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_fabric_controllers resource.
    - name: network_fabric_controller_name
      value: "{{ network_fabric_controller_name }}"
      description: Required parameter for the network_fabric_controllers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_fabric_controllers resource.
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
        The NetworkFabricController Properties. Required.
      value:
        annotation: "{{ annotation }}"
        infrastructureExpressRouteConnections:
          - expressRouteCircuitId: "{{ expressRouteCircuitId }}"
            expressRouteAuthorizationKey: "{{ expressRouteAuthorizationKey }}"
        workloadExpressRouteConnections:
          - expressRouteCircuitId: "{{ expressRouteCircuitId }}"
            expressRouteAuthorizationKey: "{{ expressRouteAuthorizationKey }}"
        infrastructureServices:
          ipv4AddressSpaces:
            - "{{ ipv4AddressSpaces }}"
          ipv6AddressSpaces:
            - "{{ ipv6AddressSpaces }}"
        workloadServices:
          ipv4AddressSpaces:
            - "{{ ipv4AddressSpaces }}"
          ipv6AddressSpaces:
            - "{{ ipv6AddressSpaces }}"
        managedResourceGroupConfiguration:
          name: "{{ name }}"
          location: "{{ location }}"
        networkFabricIds:
          - "{{ networkFabricIds }}"
        isWorkloadManagementNetworkEnabled: "{{ isWorkloadManagementNetworkEnabled }}"
        tenantInternetGatewayIds:
          - "{{ tenantInternetGatewayIds }}"
        ipv4AddressSpace: "{{ ipv4AddressSpace }}"
        ipv6AddressSpace: "{{ ipv6AddressSpace }}"
        nfcSku: "{{ nfcSku }}"
        lastOperation:
          details: "{{ details }}"
        provisioningState: "{{ provisioningState }}"
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

Updates are currently not supported for the Network Fabric Controller resource.

```sql
UPDATE azure.managednetworkfabric.network_fabric_controllers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_fabric_controller_name = '{{ network_fabric_controller_name }}' --required
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

Deletes the Network Fabric Controller resource.

```sql
DELETE FROM azure.managednetworkfabric.network_fabric_controllers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_fabric_controller_name = '{{ network_fabric_controller_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
