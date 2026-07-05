--- 
title: public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses
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

Creates, updates, deletes, gets or lists a <code>public_ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="public_ip_addresses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_addresses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cloud_service_public_ip_address"
    values={[
        { label: 'get_cloud_service_public_ip_address', value: 'get_cloud_service_public_ip_address' },
        { label: 'get_virtual_machine_scale_set_public_ip_address', value: 'get_virtual_machine_scale_set_public_ip_address' },
        { label: 'list_cloud_service_role_instance_public_ip_addresses', value: 'list_cloud_service_role_instance_public_ip_addresses' },
        { label: 'list_virtual_machine_scale_set_vm_public_ip_addresses', value: 'list_virtual_machine_scale_set_vm_public_ip_addresses' },
        { label: 'get', value: 'get' },
        { label: 'list_cloud_service_public_ip_addresses', value: 'list_cloud_service_public_ip_addresses' },
        { label: 'list_virtual_machine_scale_set_public_ip_addresses', value: 'list_virtual_machine_scale_set_public_ip_addresses' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_cloud_service_public_ip_address">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_virtual_machine_scale_set_public_ip_address">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_cloud_service_role_instance_public_ip_addresses">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_virtual_machine_scale_set_vm_public_ip_addresses">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_cloud_service_public_ip_addresses">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_virtual_machine_scale_set_public_ip_addresses">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td><CopyableCode code="ddosSettings" /></td>
    <td><code>object</code></td>
    <td>The DDoS protection custom policy associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>Specify what happens to the public IP address when the VM using it is deleted. Known values are: "Delete" and "Detach". (Delete, Detach)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>The FQDN of the DNS record associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the public ip address.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The idle timeout of the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address associated with the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfiguration" /></td>
    <td><code>object</code></td>
    <td>IP configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="ipTags" /></td>
    <td><code>array</code></td>
    <td>The list of tags associated with the public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedPublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The linked public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationPhase" /></td>
    <td><code>string</code></td>
    <td>Migration phase of Public IP Address. Known values are: "None", "Prepare", "Commit", "Abort", and "Committed". (None, Prepare, Commit, Abort, Committed)</td>
</tr>
<tr>
    <td><CopyableCode code="natGateway" /></td>
    <td><code>object</code></td>
    <td>The NatGateway for the Public IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the public IP address resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAddressVersion" /></td>
    <td><code>string</code></td>
    <td>The public IP address version. Known values are: "IPv4" and "IPv6". (IPv4, IPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPAllocationMethod" /></td>
    <td><code>string</code></td>
    <td>The public IP address allocation method. Known values are: "Static" and "Dynamic". (Static, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPPrefix" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePublicIPAddress" /></td>
    <td><code>object</code></td>
    <td>The service public IP address of the public IP address resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The public IP address SKU.</td>
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
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting the IP allocated for the resource needs to come from.</td>
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
    <td><a href="#get_cloud_service_public_ip_address"><CopyableCode code="get_cloud_service_public_ip_address" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_service_name"><code>cloud_service_name</code></a>, <a href="#parameter-role_instance_name"><code>role_instance_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-ip_configuration_name"><code>ip_configuration_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specified public IP address in a cloud service.</td>
</tr>
<tr>
    <td><a href="#get_virtual_machine_scale_set_public_ip_address"><CopyableCode code="get_virtual_machine_scale_set_public_ip_address" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-virtualmachine_index"><code>virtualmachine_index</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-ip_configuration_name"><code>ip_configuration_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the specified public IP address in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#list_cloud_service_role_instance_public_ip_addresses"><CopyableCode code="list_cloud_service_role_instance_public_ip_addresses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_service_name"><code>cloud_service_name</code></a>, <a href="#parameter-role_instance_name"><code>role_instance_name</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-ip_configuration_name"><code>ip_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about all public IP addresses in a role instance IP configuration in a cloud service.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machine_scale_set_vm_public_ip_addresses"><CopyableCode code="list_virtual_machine_scale_set_vm_public_ip_addresses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-virtualmachine_index"><code>virtualmachine_index</code></a>, <a href="#parameter-network_interface_name"><code>network_interface_name</code></a>, <a href="#parameter-ip_configuration_name"><code>ip_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified public IP address in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_cloud_service_public_ip_addresses"><CopyableCode code="list_cloud_service_public_ip_addresses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_service_name"><code>cloud_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about all public IP addresses on a cloud service level.</td>
</tr>
<tr>
    <td><a href="#list_virtual_machine_scale_set_public_ip_addresses"><CopyableCode code="list_virtual_machine_scale_set_public_ip_addresses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_machine_scale_set_name"><code>virtual_machine_scale_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about all public IP addresses on a virtual machine scale set level.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all public IP addresses in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the public IP addresses in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a static or dynamic public IP address.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates public IP address tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a static or dynamic public IP address.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified public IP address.</td>
</tr>
<tr>
    <td><a href="#ddos_protection_status"><CopyableCode code="ddos_protection_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Ddos Protection Status of a Public IP Address.</td>
</tr>
<tr>
    <td><a href="#reserve_cloud_service_public_ip_address"><CopyableCode code="reserve_cloud_service_public_ip_address" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-isRollback"><code>isRollback</code></a></td>
    <td></td>
    <td>Reserves the specified Cloud Service Public IP by switching its allocation method to Static. If rollback is requested, reverts the allocation method to Dynamic.</td>
</tr>
<tr>
    <td><a href="#disassociate_cloud_service_reserved_public_ip"><CopyableCode code="disassociate_cloud_service_reserved_public_ip" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-public_ip_address_name"><code>public_ip_address_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-publicIpArmId"><code>publicIpArmId</code></a></td>
    <td></td>
    <td>Disassociates the Cloud Service reserved Public IP and associates the specified Standalone Public IP to the same Cloud Service frontend.</td>
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
<tr id="parameter-cloud_service_name">
    <td><CopyableCode code="cloud_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cloud service. Required.</td>
</tr>
<tr id="parameter-ip_configuration_name">
    <td><CopyableCode code="ip_configuration_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-network_interface_name">
    <td><CopyableCode code="network_interface_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-public_ip_address_name">
    <td><CopyableCode code="public_ip_address_name" /></td>
    <td><code>string</code></td>
    <td>The name of the public IP address. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-role_instance_name">
    <td><CopyableCode code="role_instance_name" /></td>
    <td><code>string</code></td>
    <td>The role instance name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_machine_scale_set_name">
    <td><CopyableCode code="virtual_machine_scale_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual machine scale set. Required.</td>
</tr>
<tr id="parameter-virtualmachine_index">
    <td><CopyableCode code="virtualmachine_index" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
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
    defaultValue="get_cloud_service_public_ip_address"
    values={[
        { label: 'get_cloud_service_public_ip_address', value: 'get_cloud_service_public_ip_address' },
        { label: 'get_virtual_machine_scale_set_public_ip_address', value: 'get_virtual_machine_scale_set_public_ip_address' },
        { label: 'list_cloud_service_role_instance_public_ip_addresses', value: 'list_cloud_service_role_instance_public_ip_addresses' },
        { label: 'list_virtual_machine_scale_set_vm_public_ip_addresses', value: 'list_virtual_machine_scale_set_vm_public_ip_addresses' },
        { label: 'get', value: 'get' },
        { label: 'list_cloud_service_public_ip_addresses', value: 'list_cloud_service_public_ip_addresses' },
        { label: 'list_virtual_machine_scale_set_public_ip_addresses', value: 'list_virtual_machine_scale_set_public_ip_addresses' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get_cloud_service_public_ip_address">

Get the specified public IP address in a cloud service.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_service_name = '{{ cloud_service_name }}' -- required
AND role_instance_name = '{{ role_instance_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND ip_configuration_name = '{{ ip_configuration_name }}' -- required
AND public_ip_address_name = '{{ public_ip_address_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_virtual_machine_scale_set_public_ip_address">

Get the specified public IP address in a virtual machine scale set.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND virtualmachine_index = '{{ virtualmachine_index }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND ip_configuration_name = '{{ ip_configuration_name }}' -- required
AND public_ip_address_name = '{{ public_ip_address_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_cloud_service_role_instance_public_ip_addresses">

Gets information about all public IP addresses in a role instance IP configuration in a cloud service.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_service_name = '{{ cloud_service_name }}' -- required
AND role_instance_name = '{{ role_instance_name }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND ip_configuration_name = '{{ ip_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_virtual_machine_scale_set_vm_public_ip_addresses">

Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND virtualmachine_index = '{{ virtualmachine_index }}' -- required
AND network_interface_name = '{{ network_interface_name }}' -- required
AND ip_configuration_name = '{{ ip_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the specified public IP address in a specified resource group.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND public_ip_address_name = '{{ public_ip_address_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_cloud_service_public_ip_addresses">

Gets information about all public IP addresses on a cloud service level.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_service_name = '{{ cloud_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_virtual_machine_scale_set_public_ip_addresses">

Gets information about all public IP addresses on a virtual machine scale set level.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_machine_scale_set_name = '{{ virtual_machine_scale_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all public IP addresses in a resource group.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the public IP addresses in a subscription.

```sql
SELECT
id,
name,
ddosSettings,
deleteOption,
dnsSettings,
etag,
extendedLocation,
idleTimeoutInMinutes,
ipAddress,
ipConfiguration,
ipTags,
linkedPublicIPAddress,
location,
migrationPhase,
natGateway,
provisioningState,
publicIPAddressVersion,
publicIPAllocationMethod,
publicIPPrefix,
resourceGuid,
servicePublicIPAddress,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
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

Creates or updates a static or dynamic public IP address.

```sql
INSERT INTO azure.network.public_ip_addresses (
id,
location,
tags,
properties,
extendedLocation,
sku,
zones,
resource_group_name,
public_ip_address_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ sku }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ public_ip_address_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: public_ip_addresses
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the public_ip_addresses resource.
    - name: public_ip_address_name
      value: "{{ public_ip_address_name }}"
      description: Required parameter for the public_ip_addresses resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the public_ip_addresses resource.
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
        Public IP address properties.
      value:
        publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
        publicIPAddressVersion: "{{ publicIPAddressVersion }}"
        ipConfiguration:
          id: "{{ id }}"
          properties:
            privateIPAddress: "{{ privateIPAddress }}"
            privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
            subnet:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              properties:
                addressPrefix: "{{ addressPrefix }}"
                addressPrefixes: "{{ addressPrefixes }}"
                networkSecurityGroup: "{{ networkSecurityGroup }}"
                routeTable: "{{ routeTable }}"
                natGateway: "{{ natGateway }}"
                serviceEndpoints: "{{ serviceEndpoints }}"
                serviceEndpointPolicies: "{{ serviceEndpointPolicies }}"
                privateEndpoints: "{{ privateEndpoints }}"
                ipConfigurations: "{{ ipConfigurations }}"
                ipConfigurationProfiles: "{{ ipConfigurationProfiles }}"
                ipAllocations: "{{ ipAllocations }}"
                resourceNavigationLinks: "{{ resourceNavigationLinks }}"
                serviceAssociationLinks: "{{ serviceAssociationLinks }}"
                delegations: "{{ delegations }}"
                purpose: "{{ purpose }}"
                provisioningState: "{{ provisioningState }}"
                privateEndpointNetworkPolicies: "{{ privateEndpointNetworkPolicies }}"
                privateLinkServiceNetworkPolicies: "{{ privateLinkServiceNetworkPolicies }}"
                applicationGatewayIPConfigurations: "{{ applicationGatewayIPConfigurations }}"
                sharingScope: "{{ sharingScope }}"
                defaultOutboundAccess: {{ defaultOutboundAccess }}
                ipamPoolPrefixAllocations: "{{ ipamPoolPrefixAllocations }}"
                serviceGateway: "{{ serviceGateway }}"
              etag: "{{ etag }}"
            publicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            provisioningState: "{{ provisioningState }}"
          name: "{{ name }}"
          etag: "{{ etag }}"
        dnsSettings:
          domainNameLabel: "{{ domainNameLabel }}"
          domainNameLabelScope: "{{ domainNameLabelScope }}"
          fqdn: "{{ fqdn }}"
          reverseFqdn: "{{ reverseFqdn }}"
        ddosSettings:
          protectionMode: "{{ protectionMode }}"
          ddosCustomPolicy:
            id: "{{ id }}"
          ddosProtectionPlan:
            id: "{{ id }}"
        ipTags:
          - ipTagType: "{{ ipTagType }}"
            tag: "{{ tag }}"
        ipAddress: "{{ ipAddress }}"
        publicIPPrefix:
          id: "{{ id }}"
        idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        servicePublicIPAddress:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
            publicIPAddressVersion: "{{ publicIPAddressVersion }}"
            ipConfiguration:
              id: "{{ id }}"
              properties:
                privateIPAddress: "{{ privateIPAddress }}"
                privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                subnet: "{{ subnet }}"
                publicIPAddress: "{{ publicIPAddress }}"
                provisioningState: "{{ provisioningState }}"
              name: "{{ name }}"
              etag: "{{ etag }}"
            dnsSettings:
              domainNameLabel: "{{ domainNameLabel }}"
              domainNameLabelScope: "{{ domainNameLabelScope }}"
              fqdn: "{{ fqdn }}"
              reverseFqdn: "{{ reverseFqdn }}"
            ddosSettings:
              protectionMode: "{{ protectionMode }}"
              ddosCustomPolicy:
                id: "{{ id }}"
              ddosProtectionPlan:
                id: "{{ id }}"
            ipTags:
              - ipTagType: "{{ ipTagType }}"
                tag: "{{ tag }}"
            ipAddress: "{{ ipAddress }}"
            publicIPPrefix:
              id: "{{ id }}"
            idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
            servicePublicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            natGateway:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                publicIpAddresses: "{{ publicIpAddresses }}"
                publicIpAddressesV6: "{{ publicIpAddressesV6 }}"
                publicIpPrefixes: "{{ publicIpPrefixes }}"
                publicIpPrefixesV6: "{{ publicIpPrefixesV6 }}"
                subnets: "{{ subnets }}"
                sourceVirtualNetwork: "{{ sourceVirtualNetwork }}"
                serviceGateway: "{{ serviceGateway }}"
                nat64: "{{ nat64 }}"
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
              sku:
                name: "{{ name }}"
              zones:
                - "{{ zones }}"
              etag: "{{ etag }}"
            migrationPhase: "{{ migrationPhase }}"
            linkedPublicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            deleteOption: "{{ deleteOption }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          sku:
            name: "{{ name }}"
            tier: "{{ tier }}"
          etag: "{{ etag }}"
          zones:
            - "{{ zones }}"
        natGateway:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
            publicIpAddresses:
              - id: "{{ id }}"
            publicIpAddressesV6:
              - id: "{{ id }}"
            publicIpPrefixes:
              - id: "{{ id }}"
            publicIpPrefixesV6:
              - id: "{{ id }}"
            subnets:
              - id: "{{ id }}"
            sourceVirtualNetwork:
              id: "{{ id }}"
            serviceGateway:
              id: "{{ id }}"
            nat64: "{{ nat64 }}"
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
          sku:
            name: "{{ name }}"
          zones:
            - "{{ zones }}"
          etag: "{{ etag }}"
        migrationPhase: "{{ migrationPhase }}"
        linkedPublicIPAddress:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
            publicIPAddressVersion: "{{ publicIPAddressVersion }}"
            ipConfiguration:
              id: "{{ id }}"
              properties:
                privateIPAddress: "{{ privateIPAddress }}"
                privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                subnet: "{{ subnet }}"
                publicIPAddress: "{{ publicIPAddress }}"
                provisioningState: "{{ provisioningState }}"
              name: "{{ name }}"
              etag: "{{ etag }}"
            dnsSettings:
              domainNameLabel: "{{ domainNameLabel }}"
              domainNameLabelScope: "{{ domainNameLabelScope }}"
              fqdn: "{{ fqdn }}"
              reverseFqdn: "{{ reverseFqdn }}"
            ddosSettings:
              protectionMode: "{{ protectionMode }}"
              ddosCustomPolicy:
                id: "{{ id }}"
              ddosProtectionPlan:
                id: "{{ id }}"
            ipTags:
              - ipTagType: "{{ ipTagType }}"
                tag: "{{ tag }}"
            ipAddress: "{{ ipAddress }}"
            publicIPPrefix:
              id: "{{ id }}"
            idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
            resourceGuid: "{{ resourceGuid }}"
            provisioningState: "{{ provisioningState }}"
            servicePublicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            natGateway:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                publicIpAddresses: "{{ publicIpAddresses }}"
                publicIpAddressesV6: "{{ publicIpAddressesV6 }}"
                publicIpPrefixes: "{{ publicIpPrefixes }}"
                publicIpPrefixesV6: "{{ publicIpPrefixesV6 }}"
                subnets: "{{ subnets }}"
                sourceVirtualNetwork: "{{ sourceVirtualNetwork }}"
                serviceGateway: "{{ serviceGateway }}"
                nat64: "{{ nat64 }}"
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
              sku:
                name: "{{ name }}"
              zones:
                - "{{ zones }}"
              etag: "{{ etag }}"
            migrationPhase: "{{ migrationPhase }}"
            linkedPublicIPAddress:
              id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              location: "{{ location }}"
              tags: "{{ tags }}"
              properties:
                publicIPAllocationMethod: "{{ publicIPAllocationMethod }}"
                publicIPAddressVersion: "{{ publicIPAddressVersion }}"
                ipConfiguration: "{{ ipConfiguration }}"
                dnsSettings: "{{ dnsSettings }}"
                ddosSettings: "{{ ddosSettings }}"
                ipTags: "{{ ipTags }}"
                ipAddress: "{{ ipAddress }}"
                publicIPPrefix: "{{ publicIPPrefix }}"
                idleTimeoutInMinutes: {{ idleTimeoutInMinutes }}
                resourceGuid: "{{ resourceGuid }}"
                provisioningState: "{{ provisioningState }}"
                servicePublicIPAddress: "{{ servicePublicIPAddress }}"
                natGateway: "{{ natGateway }}"
                migrationPhase: "{{ migrationPhase }}"
                linkedPublicIPAddress: "{{ linkedPublicIPAddress }}"
                deleteOption: "{{ deleteOption }}"
              extendedLocation:
                name: "{{ name }}"
                type: "{{ type }}"
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
              etag: "{{ etag }}"
              zones:
                - "{{ zones }}"
            deleteOption: "{{ deleteOption }}"
          extendedLocation:
            name: "{{ name }}"
            type: "{{ type }}"
          sku:
            name: "{{ name }}"
            tier: "{{ tier }}"
          etag: "{{ etag }}"
          zones:
            - "{{ zones }}"
        deleteOption: "{{ deleteOption }}"
    - name: extendedLocation
      description: |
        The extended location of the public ip address.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: sku
      description: |
        The public IP address SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting the IP allocated for the resource needs to come from.
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

Updates public IP address tags.

```sql
UPDATE azure.network.public_ip_addresses
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_address_name = '{{ public_ip_address_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
tags,
type,
zones;
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

Creates or updates a static or dynamic public IP address.

```sql
REPLACE azure.network.public_ip_addresses
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
sku = '{{ sku }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_address_name = '{{ public_ip_address_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
tags,
type,
zones;
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

Deletes the specified public IP address.

```sql
DELETE FROM azure.network.public_ip_addresses
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND public_ip_address_name = '{{ public_ip_address_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="ddos_protection_status"
    values={[
        { label: 'ddos_protection_status', value: 'ddos_protection_status' },
        { label: 'reserve_cloud_service_public_ip_address', value: 'reserve_cloud_service_public_ip_address' },
        { label: 'disassociate_cloud_service_reserved_public_ip', value: 'disassociate_cloud_service_reserved_public_ip' }
    ]}
>
<TabItem value="ddos_protection_status">

Gets the Ddos Protection Status of a Public IP Address.

```sql
EXEC azure.network.public_ip_addresses.ddos_protection_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@public_ip_address_name='{{ public_ip_address_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reserve_cloud_service_public_ip_address">

Reserves the specified Cloud Service Public IP by switching its allocation method to Static. If rollback is requested, reverts the allocation method to Dynamic.

```sql
EXEC azure.network.public_ip_addresses.reserve_cloud_service_public_ip_address 
@resource_group_name='{{ resource_group_name }}' --required, 
@public_ip_address_name='{{ public_ip_address_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"isRollback": "{{ isRollback }}"
}'
;
```
</TabItem>
<TabItem value="disassociate_cloud_service_reserved_public_ip">

Disassociates the Cloud Service reserved Public IP and associates the specified Standalone Public IP to the same Cloud Service frontend.

```sql
EXEC azure.network.public_ip_addresses.disassociate_cloud_service_reserved_public_ip 
@resource_group_name='{{ resource_group_name }}' --required, 
@public_ip_address_name='{{ public_ip_address_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"publicIpArmId": "{{ publicIpArmId }}"
}'
;
```
</TabItem>
</Tabs>
