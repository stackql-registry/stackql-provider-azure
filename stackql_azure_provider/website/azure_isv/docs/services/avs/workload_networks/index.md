--- 
title: workload_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_networks
  - avs
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

Creates, updates, deletes, gets or lists a <code>workload_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workload_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.avs.workload_networks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_dhcp"
    values={[
        { label: 'get_dhcp', value: 'get_dhcp' },
        { label: 'get_dns_service', value: 'get_dns_service' },
        { label: 'get_dns_zone', value: 'get_dns_zone' },
        { label: 'get_gateway', value: 'get_gateway' },
        { label: 'get_port_mirroring', value: 'get_port_mirroring' },
        { label: 'get_public_ip', value: 'get_public_ip' },
        { label: 'get_segment', value: 'get_segment' },
        { label: 'get_virtual_machine', value: 'get_virtual_machine' },
        { label: 'get_vm_group', value: 'get_vm_group' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_dhcp">

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
    <td><CopyableCode code="dhcpType" /></td>
    <td><code>string</code></td>
    <td>Type of DHCP: SERVER or RELAY. Required. Known values are: "SERVER" and "RELAY".</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the DHCP entity.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>NSX revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="segments" /></td>
    <td><code>array</code></td>
    <td>NSX Segments consuming DHCP.</td>
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
<TabItem value="get_dns_service">

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
    <td><CopyableCode code="defaultDnsZone" /></td>
    <td><code>string</code></td>
    <td>Default DNS zone of the DNS Service.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the DNS Service.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServiceIp" /></td>
    <td><code>string</code></td>
    <td>DNS service IP of the DNS Service.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdnZones" /></td>
    <td><code>array</code></td>
    <td>FQDN zones of the DNS Service.</td>
</tr>
<tr>
    <td><CopyableCode code="logLevel" /></td>
    <td><code>string</code></td>
    <td>DNS Service log level. Known values are: "DEBUG", "INFO", "WARNING", "ERROR", and "FATAL". (DEBUG, INFO, WARNING, ERROR, FATAL)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>NSX revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>DNS Service status. Known values are: "SUCCESS" and "FAILURE". (SUCCESS, FAILURE)</td>
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
<TabItem value="get_dns_zone">

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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the DNS Zone.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServerIps" /></td>
    <td><code>array</code></td>
    <td>DNS Server IP array of the DNS Zone.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServices" /></td>
    <td><code>integer</code></td>
    <td>Number of DNS Services using the DNS zone.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>array</code></td>
    <td>Domain names of the DNS Zone.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>NSX revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceIp" /></td>
    <td><code>string</code></td>
    <td>Source IP of the DNS Zone.</td>
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
<TabItem value="get_gateway">

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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the DHCP entity.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>NSX Gateway Path.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
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
<TabItem value="get_port_mirroring">

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
    <td><CopyableCode code="destination" /></td>
    <td><code>string</code></td>
    <td>Destination VM Group.</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Direction of port mirroring profile. Known values are: "INGRESS", "EGRESS", and "BIDIRECTIONAL". (INGRESS, EGRESS, BIDIRECTIONAL)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the port mirroring profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>NSX revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source VM Group.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Port Mirroring Status. Known values are: "SUCCESS" and "FAILURE". (SUCCESS, FAILURE)</td>
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
<TabItem value="get_public_ip">

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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the Public IP Block.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfPublicIPs" /></td>
    <td><code>integer</code></td>
    <td>Number of Public IPs requested.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPBlock" /></td>
    <td><code>string</code></td>
    <td>CIDR Block of the Public IP Block.</td>
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
<TabItem value="get_segment">

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
    <td><CopyableCode code="connectedGateway" /></td>
    <td><code>string</code></td>
    <td>Gateway which to connect segment to.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the segment.</td>
</tr>
<tr>
    <td><CopyableCode code="portVif" /></td>
    <td><code>array</code></td>
    <td>Port Vif which segment is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>NSX revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Segment status. Known values are: "SUCCESS" and "FAILURE". (SUCCESS, FAILURE)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>object</code></td>
    <td>Subnet which to connect segment to.</td>
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
<TabItem value="get_virtual_machine">

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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
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
    <td><CopyableCode code="vmType" /></td>
    <td><code>string</code></td>
    <td>Virtual machine type. Known values are: "REGULAR", "EDGE", and "SERVICE". (REGULAR, EDGE, SERVICE)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_vm_group">

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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the VM group.</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td>Virtual machine members of this group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>NSX revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>VM Group status. Known values are: "SUCCESS" and "FAILURE". (SUCCESS, FAILURE)</td>
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Building, Deleting, Updating)</td>
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
    <td><a href="#get_dhcp"><CopyableCode code="get_dhcp" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dhcp_id"><code>dhcp_id</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkDhcp.</td>
</tr>
<tr>
    <td><a href="#get_dns_service"><CopyableCode code="get_dns_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dns_service_id"><code>dns_service_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkDnsService.</td>
</tr>
<tr>
    <td><a href="#get_dns_zone"><CopyableCode code="get_dns_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dns_zone_id"><code>dns_zone_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkDnsZone.</td>
</tr>
<tr>
    <td><a href="#get_gateway"><CopyableCode code="get_gateway" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkGateway.</td>
</tr>
<tr>
    <td><a href="#get_port_mirroring"><CopyableCode code="get_port_mirroring" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-port_mirroring_id"><code>port_mirroring_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkPortMirroring.</td>
</tr>
<tr>
    <td><a href="#get_public_ip"><CopyableCode code="get_public_ip" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-public_ip_id"><code>public_ip_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkPublicIP.</td>
</tr>
<tr>
    <td><a href="#get_segment"><CopyableCode code="get_segment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-segment_id"><code>segment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkSegment.</td>
</tr>
<tr>
    <td><a href="#get_virtual_machine"><CopyableCode code="get_virtual_machine" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-virtual_machine_id"><code>virtual_machine_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkVirtualMachine.</td>
</tr>
<tr>
    <td><a href="#get_vm_group"><CopyableCode code="get_vm_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-vm_group_id"><code>vm_group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetworkVMGroup.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#create_dhcp"><CopyableCode code="create_dhcp" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dhcp_id"><code>dhcp_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkDhcp.</td>
</tr>
<tr>
    <td><a href="#create_dns_service"><CopyableCode code="create_dns_service" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dns_service_id"><code>dns_service_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkDnsService.</td>
</tr>
<tr>
    <td><a href="#create_dns_zone"><CopyableCode code="create_dns_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dns_zone_id"><code>dns_zone_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkDnsZone.</td>
</tr>
<tr>
    <td><a href="#create_port_mirroring"><CopyableCode code="create_port_mirroring" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-port_mirroring_id"><code>port_mirroring_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkPortMirroring.</td>
</tr>
<tr>
    <td><a href="#create_public_ip"><CopyableCode code="create_public_ip" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-public_ip_id"><code>public_ip_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkPublicIP.</td>
</tr>
<tr>
    <td><a href="#create_segments"><CopyableCode code="create_segments" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-segment_id"><code>segment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkSegment.</td>
</tr>
<tr>
    <td><a href="#create_vm_group"><CopyableCode code="create_vm_group" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-vm_group_id"><code>vm_group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a WorkloadNetworkVMGroup.</td>
</tr>
<tr>
    <td><a href="#update_dhcp"><CopyableCode code="update_dhcp" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dhcp_id"><code>dhcp_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a WorkloadNetworkDhcp.</td>
</tr>
<tr>
    <td><a href="#update_dns_service"><CopyableCode code="update_dns_service" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dns_service_id"><code>dns_service_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a WorkloadNetworkDnsService.</td>
</tr>
<tr>
    <td><a href="#update_dns_zone"><CopyableCode code="update_dns_zone" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dns_zone_id"><code>dns_zone_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a WorkloadNetworkDnsZone.</td>
</tr>
<tr>
    <td><a href="#update_port_mirroring"><CopyableCode code="update_port_mirroring" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-port_mirroring_id"><code>port_mirroring_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a WorkloadNetworkPortMirroring.</td>
</tr>
<tr>
    <td><a href="#update_segments"><CopyableCode code="update_segments" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-segment_id"><code>segment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a WorkloadNetworkSegment.</td>
</tr>
<tr>
    <td><a href="#update_vm_group"><CopyableCode code="update_vm_group" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-vm_group_id"><code>vm_group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a WorkloadNetworkVMGroup.</td>
</tr>
<tr>
    <td><a href="#delete_dhcp"><CopyableCode code="delete_dhcp" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-dhcp_id"><code>dhcp_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkDhcp.</td>
</tr>
<tr>
    <td><a href="#delete_dns_service"><CopyableCode code="delete_dns_service" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dns_service_id"><code>dns_service_id</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkDnsService.</td>
</tr>
<tr>
    <td><a href="#delete_dns_zone"><CopyableCode code="delete_dns_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dns_zone_id"><code>dns_zone_id</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkDnsZone.</td>
</tr>
<tr>
    <td><a href="#delete_port_mirroring"><CopyableCode code="delete_port_mirroring" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-port_mirroring_id"><code>port_mirroring_id</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkPortMirroring.</td>
</tr>
<tr>
    <td><a href="#delete_public_ip"><CopyableCode code="delete_public_ip" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_id"><code>public_ip_id</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkPublicIP.</td>
</tr>
<tr>
    <td><a href="#delete_segment"><CopyableCode code="delete_segment" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-segment_id"><code>segment_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkSegment.</td>
</tr>
<tr>
    <td><a href="#delete_vm_group"><CopyableCode code="delete_vm_group" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_group_id"><code>vm_group_id</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a WorkloadNetworkVMGroup.</td>
</tr>
<tr>
    <td><a href="#list_dhcp"><CopyableCode code="list_dhcp" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkDhcp resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_dns_services"><CopyableCode code="list_dns_services" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkDnsService resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_dns_zones"><CopyableCode code="list_dns_zones" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkDnsZone resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_gateways"><CopyableCode code="list_gateways" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkGateway resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_port_mirroring"><CopyableCode code="list_port_mirroring" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkPortMirroring resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_public_ips"><CopyableCode code="list_public_ips" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkPublicIP resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_segments"><CopyableCode code="list_segments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkSegment resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machines"><CopyableCode code="list_virtual_machines" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkVirtualMachine resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_vm_groups"><CopyableCode code="list_vm_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetworkVMGroup resources by WorkloadNetwork.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List WorkloadNetwork resources by PrivateCloud.</td>
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
<tr id="parameter-dhcp_id">
    <td><CopyableCode code="dhcp_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the DHCP configuration. Required.</td>
</tr>
<tr id="parameter-dns_service_id">
    <td><CopyableCode code="dns_service_id" /></td>
    <td><code>string</code></td>
    <td>ID of the DNS service. Required.</td>
</tr>
<tr id="parameter-dns_zone_id">
    <td><CopyableCode code="dns_zone_id" /></td>
    <td><code>string</code></td>
    <td>ID of the DNS zone. Required.</td>
</tr>
<tr id="parameter-gateway_id">
    <td><CopyableCode code="gateway_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the NSX Gateway. Required.</td>
</tr>
<tr id="parameter-port_mirroring_id">
    <td><CopyableCode code="port_mirroring_id" /></td>
    <td><code>string</code></td>
    <td>ID of the NSX port mirroring profile. Required.</td>
</tr>
<tr id="parameter-private_cloud_name">
    <td><CopyableCode code="private_cloud_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private cloud. Required.</td>
</tr>
<tr id="parameter-public_ip_id">
    <td><CopyableCode code="public_ip_id" /></td>
    <td><code>string</code></td>
    <td>ID of the DNS zone. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-segment_id">
    <td><CopyableCode code="segment_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the NSX Segment. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_machine_id">
    <td><CopyableCode code="virtual_machine_id" /></td>
    <td><code>string</code></td>
    <td>ID of the virtual machine. Required.</td>
</tr>
<tr id="parameter-vm_group_id">
    <td><CopyableCode code="vm_group_id" /></td>
    <td><code>string</code></td>
    <td>ID of the VM group. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_dhcp"
    values={[
        { label: 'get_dhcp', value: 'get_dhcp' },
        { label: 'get_dns_service', value: 'get_dns_service' },
        { label: 'get_dns_zone', value: 'get_dns_zone' },
        { label: 'get_gateway', value: 'get_gateway' },
        { label: 'get_port_mirroring', value: 'get_port_mirroring' },
        { label: 'get_public_ip', value: 'get_public_ip' },
        { label: 'get_segment', value: 'get_segment' },
        { label: 'get_virtual_machine', value: 'get_virtual_machine' },
        { label: 'get_vm_group', value: 'get_vm_group' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_dhcp">

Get a WorkloadNetworkDhcp.

```sql
SELECT
id,
name,
dhcpType,
displayName,
provisioningState,
revision,
segments,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dhcp_id = '{{ dhcp_id }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_dns_service">

Get a WorkloadNetworkDnsService.

```sql
SELECT
id,
name,
defaultDnsZone,
displayName,
dnsServiceIp,
fqdnZones,
logLevel,
provisioningState,
revision,
status,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND dns_service_id = '{{ dns_service_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_dns_zone">

Get a WorkloadNetworkDnsZone.

```sql
SELECT
id,
name,
displayName,
dnsServerIps,
dnsServices,
domain,
provisioningState,
revision,
sourceIp,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND dns_zone_id = '{{ dns_zone_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_gateway">

Get a WorkloadNetworkGateway.

```sql
SELECT
id,
name,
displayName,
path,
provisioningState,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_port_mirroring">

Get a WorkloadNetworkPortMirroring.

```sql
SELECT
id,
name,
destination,
direction,
displayName,
provisioningState,
revision,
source,
status,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND port_mirroring_id = '{{ port_mirroring_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_public_ip">

Get a WorkloadNetworkPublicIP.

```sql
SELECT
id,
name,
displayName,
numberOfPublicIPs,
provisioningState,
publicIPBlock,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND public_ip_id = '{{ public_ip_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_segment">

Get a WorkloadNetworkSegment.

```sql
SELECT
id,
name,
connectedGateway,
displayName,
portVif,
provisioningState,
revision,
status,
subnet,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND segment_id = '{{ segment_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_virtual_machine">

Get a WorkloadNetworkVirtualMachine.

```sql
SELECT
id,
name,
displayName,
provisioningState,
systemData,
type,
vmType
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND virtual_machine_id = '{{ virtual_machine_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_vm_group">

Get a WorkloadNetworkVMGroup.

```sql
SELECT
id,
name,
displayName,
members,
provisioningState,
revision,
status,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND vm_group_id = '{{ vm_group_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a WorkloadNetwork.

```sql
SELECT
id,
name,
provisioningState,
systemData,
type
FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_dhcp"
    values={[
        { label: 'create_dhcp', value: 'create_dhcp' },
        { label: 'create_dns_service', value: 'create_dns_service' },
        { label: 'create_dns_zone', value: 'create_dns_zone' },
        { label: 'create_port_mirroring', value: 'create_port_mirroring' },
        { label: 'create_public_ip', value: 'create_public_ip' },
        { label: 'create_segments', value: 'create_segments' },
        { label: 'create_vm_group', value: 'create_vm_group' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_dhcp">

Create a WorkloadNetworkDhcp.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
dhcp_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ dhcp_id }}',
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
<TabItem value="create_dns_service">

Create a WorkloadNetworkDnsService.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
dns_service_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ dns_service_id }}',
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
<TabItem value="create_dns_zone">

Create a WorkloadNetworkDnsZone.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
dns_zone_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ dns_zone_id }}',
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
<TabItem value="create_port_mirroring">

Create a WorkloadNetworkPortMirroring.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
port_mirroring_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ port_mirroring_id }}',
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
<TabItem value="create_public_ip">

Create a WorkloadNetworkPublicIP.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
public_ip_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ public_ip_id }}',
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
<TabItem value="create_segments">

Create a WorkloadNetworkSegment.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
segment_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ segment_id }}',
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
<TabItem value="create_vm_group">

Create a WorkloadNetworkVMGroup.

```sql
INSERT INTO azure_isv.avs.workload_networks (
properties,
resource_group_name,
private_cloud_name,
vm_group_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ vm_group_id }}',
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
- name: workload_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workload_networks resource.
    - name: private_cloud_name
      value: "{{ private_cloud_name }}"
      description: Required parameter for the workload_networks resource.
    - name: dhcp_id
      value: "{{ dhcp_id }}"
      description: Required parameter for the workload_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workload_networks resource.
    - name: dns_service_id
      value: "{{ dns_service_id }}"
      description: Required parameter for the workload_networks resource.
    - name: dns_zone_id
      value: "{{ dns_zone_id }}"
      description: Required parameter for the workload_networks resource.
    - name: port_mirroring_id
      value: "{{ port_mirroring_id }}"
      description: Required parameter for the workload_networks resource.
    - name: public_ip_id
      value: "{{ public_ip_id }}"
      description: Required parameter for the workload_networks resource.
    - name: segment_id
      value: "{{ segment_id }}"
      description: Required parameter for the workload_networks resource.
    - name: vm_group_id
      value: "{{ vm_group_id }}"
      description: Required parameter for the workload_networks resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        displayName: "{{ displayName }}"
        members:
          - "{{ members }}"
        status: "{{ status }}"
        provisioningState: "{{ provisioningState }}"
        revision: {{ revision }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_dhcp"
    values={[
        { label: 'update_dhcp', value: 'update_dhcp' },
        { label: 'update_dns_service', value: 'update_dns_service' },
        { label: 'update_dns_zone', value: 'update_dns_zone' },
        { label: 'update_port_mirroring', value: 'update_port_mirroring' },
        { label: 'update_segments', value: 'update_segments' },
        { label: 'update_vm_group', value: 'update_vm_group' }
    ]}
>
<TabItem value="update_dhcp">

Update a WorkloadNetworkDhcp.

```sql
UPDATE azure_isv.avs.workload_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND dhcp_id = '{{ dhcp_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_dns_service">

Update a WorkloadNetworkDnsService.

```sql
UPDATE azure_isv.avs.workload_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND dns_service_id = '{{ dns_service_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_dns_zone">

Update a WorkloadNetworkDnsZone.

```sql
UPDATE azure_isv.avs.workload_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND dns_zone_id = '{{ dns_zone_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_port_mirroring">

Update a WorkloadNetworkPortMirroring.

```sql
UPDATE azure_isv.avs.workload_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND port_mirroring_id = '{{ port_mirroring_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_segments">

Update a WorkloadNetworkSegment.

```sql
UPDATE azure_isv.avs.workload_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND segment_id = '{{ segment_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update_vm_group">

Update a WorkloadNetworkVMGroup.

```sql
UPDATE azure_isv.avs.workload_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND vm_group_id = '{{ vm_group_id }}' --required
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
    defaultValue="delete_dhcp"
    values={[
        { label: 'delete_dhcp', value: 'delete_dhcp' },
        { label: 'delete_dns_service', value: 'delete_dns_service' },
        { label: 'delete_dns_zone', value: 'delete_dns_zone' },
        { label: 'delete_port_mirroring', value: 'delete_port_mirroring' },
        { label: 'delete_public_ip', value: 'delete_public_ip' },
        { label: 'delete_segment', value: 'delete_segment' },
        { label: 'delete_vm_group', value: 'delete_vm_group' }
    ]}
>
<TabItem value="delete_dhcp">

Delete a WorkloadNetworkDhcp.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND dhcp_id = '{{ dhcp_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_dns_service">

Delete a WorkloadNetworkDnsService.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dns_service_id = '{{ dns_service_id }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_dns_zone">

Delete a WorkloadNetworkDnsZone.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dns_zone_id = '{{ dns_zone_id }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_port_mirroring">

Delete a WorkloadNetworkPortMirroring.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND port_mirroring_id = '{{ port_mirroring_id }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_public_ip">

Delete a WorkloadNetworkPublicIP.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_id = '{{ public_ip_id }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_segment">

Delete a WorkloadNetworkSegment.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND segment_id = '{{ segment_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_vm_group">

Delete a WorkloadNetworkVMGroup.

```sql
DELETE FROM azure_isv.avs.workload_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vm_group_id = '{{ vm_group_id }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_dhcp"
    values={[
        { label: 'list_dhcp', value: 'list_dhcp' },
        { label: 'list_dns_services', value: 'list_dns_services' },
        { label: 'list_dns_zones', value: 'list_dns_zones' },
        { label: 'list_gateways', value: 'list_gateways' },
        { label: 'list_port_mirroring', value: 'list_port_mirroring' },
        { label: 'list_public_ips', value: 'list_public_ips' },
        { label: 'list_segments', value: 'list_segments' },
        { label: 'list_virtual_machines', value: 'list_virtual_machines' },
        { label: 'list_vm_groups', value: 'list_vm_groups' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_dhcp">

List WorkloadNetworkDhcp resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_dhcp 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_dns_services">

List WorkloadNetworkDnsService resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_dns_services 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_dns_zones">

List WorkloadNetworkDnsZone resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_dns_zones 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_gateways">

List WorkloadNetworkGateway resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_gateways 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_port_mirroring">

List WorkloadNetworkPortMirroring resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_port_mirroring 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_public_ips">

List WorkloadNetworkPublicIP resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_public_ips 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_segments">

List WorkloadNetworkSegment resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_segments 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_virtual_machines">

List WorkloadNetworkVirtualMachine resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_virtual_machines 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_vm_groups">

List WorkloadNetworkVMGroup resources by WorkloadNetwork.

```sql
EXEC azure_isv.avs.workload_networks.list_vm_groups 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

List WorkloadNetwork resources by PrivateCloud.

```sql
EXEC azure_isv.avs.workload_networks.list_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
