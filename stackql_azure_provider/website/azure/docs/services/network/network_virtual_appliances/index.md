--- 
title: network_virtual_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - network_virtual_appliances
  - network
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

Creates, updates, deletes, gets or lists a <code>network_virtual_appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_virtual_appliances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_virtual_appliances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalNics" /></td>
    <td><code>array</code></td>
    <td>Details required for Additional Network Interface. This property is not compatible with the NVA deployed in VNets.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>Address Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="bootStrapConfigurationBlobs" /></td>
    <td><code>array</code></td>
    <td>BootStrapConfigurationBlobs storage URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudInitConfiguration" /></td>
    <td><code>string</code></td>
    <td>CloudInitConfiguration string in plain text.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudInitConfigurationBlobs" /></td>
    <td><code>array</code></td>
    <td>CloudInitConfigurationBlob storage URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="delegation" /></td>
    <td><code>object</code></td>
    <td>The delegation for the Virtual Appliance. Only appliable for SaaS NVA.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type. PartnerManaged for the SaaS NVA.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The service principal that has read access to cloud-init and config blob.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundSecurityRules" /></td>
    <td><code>array</code></td>
    <td>List of references to InboundSecurityRules.</td>
</tr>
<tr>
    <td><CopyableCode code="internetIngressPublicIps" /></td>
    <td><code>array</code></td>
    <td>List of Resource Uri of Public IPs for Internet Ingress Scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network Profile containing configurations for Public and Private NIC.</td>
</tr>
<tr>
    <td><CopyableCode code="nvaInterfaceConfigurations" /></td>
    <td><code>array</code></td>
    <td>The NVA in VNet interface configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="nvaSku" /></td>
    <td><code>object</code></td>
    <td>Network Virtual Appliance SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerManagedResource" /></td>
    <td><code>object</code></td>
    <td>The delegation for the Virtual Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIpAddress" /></td>
    <td><code>string</code></td>
    <td>A Internal Load Balancer's HA port frontend IP address. Can be used to set routes & UDR to load balance traffic between NVA instances.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public key for SSH login.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceAsn" /></td>
    <td><code>integer</code></td>
    <td>VirtualAppliance ASN. Microsoft private, public and IANA reserved ASN are not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceConnections" /></td>
    <td><code>array</code></td>
    <td>List of references to VirtualApplianceConnections.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceNics" /></td>
    <td><code>array</code></td>
    <td>List of Virtual Appliance Network Interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceSites" /></td>
    <td><code>array</code></td>
    <td>List of references to VirtualApplianceSite.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalNics" /></td>
    <td><code>array</code></td>
    <td>Details required for Additional Network Interface. This property is not compatible with the NVA deployed in VNets.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>Address Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="bootStrapConfigurationBlobs" /></td>
    <td><code>array</code></td>
    <td>BootStrapConfigurationBlobs storage URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudInitConfiguration" /></td>
    <td><code>string</code></td>
    <td>CloudInitConfiguration string in plain text.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudInitConfigurationBlobs" /></td>
    <td><code>array</code></td>
    <td>CloudInitConfigurationBlob storage URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="delegation" /></td>
    <td><code>object</code></td>
    <td>The delegation for the Virtual Appliance. Only appliable for SaaS NVA.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type. PartnerManaged for the SaaS NVA.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The service principal that has read access to cloud-init and config blob.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundSecurityRules" /></td>
    <td><code>array</code></td>
    <td>List of references to InboundSecurityRules.</td>
</tr>
<tr>
    <td><CopyableCode code="internetIngressPublicIps" /></td>
    <td><code>array</code></td>
    <td>List of Resource Uri of Public IPs for Internet Ingress Scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network Profile containing configurations for Public and Private NIC.</td>
</tr>
<tr>
    <td><CopyableCode code="nvaInterfaceConfigurations" /></td>
    <td><code>array</code></td>
    <td>The NVA in VNet interface configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="nvaSku" /></td>
    <td><code>object</code></td>
    <td>Network Virtual Appliance SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerManagedResource" /></td>
    <td><code>object</code></td>
    <td>The delegation for the Virtual Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIpAddress" /></td>
    <td><code>string</code></td>
    <td>A Internal Load Balancer's HA port frontend IP address. Can be used to set routes & UDR to load balance traffic between NVA instances.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public key for SSH login.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceAsn" /></td>
    <td><code>integer</code></td>
    <td>VirtualAppliance ASN. Microsoft private, public and IANA reserved ASN are not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceConnections" /></td>
    <td><code>array</code></td>
    <td>List of references to VirtualApplianceConnections.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceNics" /></td>
    <td><code>array</code></td>
    <td>List of Virtual Appliance Network Interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceSites" /></td>
    <td><code>array</code></td>
    <td>List of references to VirtualApplianceSite.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalNics" /></td>
    <td><code>array</code></td>
    <td>Details required for Additional Network Interface. This property is not compatible with the NVA deployed in VNets.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefix" /></td>
    <td><code>string</code></td>
    <td>Address Prefix.</td>
</tr>
<tr>
    <td><CopyableCode code="bootStrapConfigurationBlobs" /></td>
    <td><code>array</code></td>
    <td>BootStrapConfigurationBlobs storage URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudInitConfiguration" /></td>
    <td><code>string</code></td>
    <td>CloudInitConfiguration string in plain text.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudInitConfigurationBlobs" /></td>
    <td><code>array</code></td>
    <td>CloudInitConfigurationBlob storage URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="delegation" /></td>
    <td><code>object</code></td>
    <td>The delegation for the Virtual Appliance. Only appliable for SaaS NVA.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentType" /></td>
    <td><code>string</code></td>
    <td>The deployment type. PartnerManaged for the SaaS NVA.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The service principal that has read access to cloud-init and config blob.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundSecurityRules" /></td>
    <td><code>array</code></td>
    <td>List of references to InboundSecurityRules.</td>
</tr>
<tr>
    <td><CopyableCode code="internetIngressPublicIps" /></td>
    <td><code>array</code></td>
    <td>List of Resource Uri of Public IPs for Internet Ingress Scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network Profile containing configurations for Public and Private NIC.</td>
</tr>
<tr>
    <td><CopyableCode code="nvaInterfaceConfigurations" /></td>
    <td><code>array</code></td>
    <td>The NVA in VNet interface configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="nvaSku" /></td>
    <td><code>object</code></td>
    <td>Network Virtual Appliance SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerManagedResource" /></td>
    <td><code>object</code></td>
    <td>The delegation for the Virtual Appliance.</td>
</tr>
<tr>
    <td><CopyableCode code="privateIpAddress" /></td>
    <td><code>string</code></td>
    <td>A Internal Load Balancer's HA port frontend IP address. Can be used to set routes & UDR to load balance traffic between NVA instances.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public key for SSH login.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceAsn" /></td>
    <td><code>integer</code></td>
    <td>VirtualAppliance ASN. Microsoft private, public and IANA reserved ASN are not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceConnections" /></td>
    <td><code>array</code></td>
    <td>List of references to VirtualApplianceConnections.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceNics" /></td>
    <td><code>array</code></td>
    <td>List of Virtual Appliance Network Interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplianceSites" /></td>
    <td><code>array</code></td>
    <td>List of references to VirtualApplianceSite.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Network Virtual Appliances in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all Network Virtual Appliances in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#get_boot_diagnostic_logs"><CopyableCode code="get_boot_diagnostic_logs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the boot diagnostic logs for a VM instance belonging to the specified Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts one or more VMs belonging to the specified Network Virtual Appliance.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reimages one VM belonging to the specified Network Virtual Appliance.</td>
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
<tr id="parameter-network_virtual_appliance_name">
    <td><CopyableCode code="network_virtual_appliance_name" /></td>
    <td><code>string</code></td>
    <td>The name of Network Virtual Appliance. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified Network Virtual Appliance.

```sql
SELECT
id,
name,
additionalNics,
addressPrefix,
bootStrapConfigurationBlobs,
cloudInitConfiguration,
cloudInitConfigurationBlobs,
delegation,
deploymentType,
etag,
identity,
inboundSecurityRules,
internetIngressPublicIps,
location,
networkProfile,
nvaInterfaceConfigurations,
nvaSku,
partnerManagedResource,
privateIpAddress,
provisioningState,
sshPublicKey,
tags,
type,
virtualApplianceAsn,
virtualApplianceConnections,
virtualApplianceNics,
virtualApplianceSites,
virtualHub
FROM azure.network.network_virtual_appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all Network Virtual Appliances in a resource group.

```sql
SELECT
id,
name,
additionalNics,
addressPrefix,
bootStrapConfigurationBlobs,
cloudInitConfiguration,
cloudInitConfigurationBlobs,
delegation,
deploymentType,
etag,
identity,
inboundSecurityRules,
internetIngressPublicIps,
location,
networkProfile,
nvaInterfaceConfigurations,
nvaSku,
partnerManagedResource,
privateIpAddress,
provisioningState,
sshPublicKey,
tags,
type,
virtualApplianceAsn,
virtualApplianceConnections,
virtualApplianceNics,
virtualApplianceSites,
virtualHub
FROM azure.network.network_virtual_appliances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all Network Virtual Appliances in a subscription.

```sql
SELECT
id,
name,
additionalNics,
addressPrefix,
bootStrapConfigurationBlobs,
cloudInitConfiguration,
cloudInitConfigurationBlobs,
delegation,
deploymentType,
etag,
identity,
inboundSecurityRules,
internetIngressPublicIps,
location,
networkProfile,
nvaInterfaceConfigurations,
nvaSku,
partnerManagedResource,
privateIpAddress,
provisioningState,
sshPublicKey,
tags,
type,
virtualApplianceAsn,
virtualApplianceConnections,
virtualApplianceNics,
virtualApplianceSites,
virtualHub
FROM azure.network.network_virtual_appliances
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

Creates or updates the specified Network Virtual Appliance.

```sql
INSERT INTO azure.network.network_virtual_appliances (
id,
location,
tags,
properties,
identity,
resource_group_name,
network_virtual_appliance_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ network_virtual_appliance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_virtual_appliances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_virtual_appliances resource.
    - name: network_virtual_appliance_name
      value: "{{ network_virtual_appliance_name }}"
      description: Required parameter for the network_virtual_appliances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_virtual_appliances resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the Network Virtual Appliance.
      value:
        nvaSku:
          vendor: "{{ vendor }}"
          bundledScaleUnit: "{{ bundledScaleUnit }}"
          marketPlaceVersion: "{{ marketPlaceVersion }}"
        addressPrefix: "{{ addressPrefix }}"
        bootStrapConfigurationBlobs:
          - "{{ bootStrapConfigurationBlobs }}"
        virtualHub:
          id: "{{ id }}"
        cloudInitConfigurationBlobs:
          - "{{ cloudInitConfigurationBlobs }}"
        cloudInitConfiguration: "{{ cloudInitConfiguration }}"
        virtualApplianceAsn: {{ virtualApplianceAsn }}
        sshPublicKey: "{{ sshPublicKey }}"
        virtualApplianceNics:
          - nicType: "{{ nicType }}"
            name: "{{ name }}"
            publicIpAddress: "{{ publicIpAddress }}"
            privateIpAddress: "{{ privateIpAddress }}"
            instanceName: "{{ instanceName }}"
        networkProfile:
          networkInterfaceConfigurations:
            - type: "{{ type }}"
              properties:
                ipConfigurations:
                  - name: "{{ name }}"
                    properties:
                      primary: {{ primary }}
        additionalNics:
          - name: "{{ name }}"
            hasPublicIp: {{ hasPublicIp }}
        internetIngressPublicIps:
          - id: "{{ id }}"
        virtualApplianceSites:
          - id: "{{ id }}"
        virtualApplianceConnections:
          - id: "{{ id }}"
        inboundSecurityRules:
          - id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        deploymentType: "{{ deploymentType }}"
        delegation:
          serviceName: "{{ serviceName }}"
          provisioningState: "{{ provisioningState }}"
        partnerManagedResource:
          id: "{{ id }}"
          internalLoadBalancerId: "{{ internalLoadBalancerId }}"
          standardLoadBalancerId: "{{ standardLoadBalancerId }}"
        nvaInterfaceConfigurations:
          - subnet:
              id: "{{ id }}"
            type: "{{ type }}"
            name: "{{ name }}"
        privateIpAddress: "{{ privateIpAddress }}"
    - name: identity
      description: |
        The service principal that has read access to cloud-init and config blob.
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
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates a Network Virtual Appliance.

```sql
UPDATE azure.network.network_virtual_appliances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
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

Creates or updates the specified Network Virtual Appliance.

```sql
REPLACE azure.network.network_virtual_appliances
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
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

Deletes the specified Network Virtual Appliance.

```sql
DELETE FROM azure.network.network_virtual_appliances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_boot_diagnostic_logs"
    values={[
        { label: 'get_boot_diagnostic_logs', value: 'get_boot_diagnostic_logs' },
        { label: 'restart', value: 'restart' },
        { label: 'reimage', value: 'reimage' }
    ]}
>
<TabItem value="get_boot_diagnostic_logs">

Retrieves the boot diagnostic logs for a VM instance belonging to the specified Network Virtual Appliance.

```sql
EXEC azure.network.network_virtual_appliances.get_boot_diagnostic_logs 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_virtual_appliance_name='{{ network_virtual_appliance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceId": {{ instanceId }}, 
"serialConsoleStorageSasUrl": "{{ serialConsoleStorageSasUrl }}", 
"consoleScreenshotStorageSasUrl": "{{ consoleScreenshotStorageSasUrl }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Restarts one or more VMs belonging to the specified Network Virtual Appliance.

```sql
EXEC azure.network.network_virtual_appliances.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_virtual_appliance_name='{{ network_virtual_appliance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
<TabItem value="reimage">

Reimages one VM belonging to the specified Network Virtual Appliance.

```sql
EXEC azure.network.network_virtual_appliances.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_virtual_appliance_name='{{ network_virtual_appliance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceIds": "{{ instanceIds }}"
}'
;
```
</TabItem>
</Tabs>
