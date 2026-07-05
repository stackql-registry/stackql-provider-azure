--- 
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
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

Creates, updates, deletes, gets or lists a <code>private_clouds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_clouds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.avs.private_clouds" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_in_subscription', value: 'list_in_subscription' }
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
    <td><CopyableCode code="availability" /></td>
    <td><code>object</code></td>
    <td>Properties describing how the cloud is distributed across availability zones.</td>
</tr>
<tr>
    <td><CopyableCode code="circuit" /></td>
    <td><code>object</code></td>
    <td>An ExpressRoute Circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZoneType" /></td>
    <td><code>string</code></td>
    <td>The type of DNS zone to use. Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer managed key encryption, can be enabled or disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>The endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedNetworkBlocks" /></td>
    <td><code>array</code></td>
    <td>Array of additional networks noncontiguous with networkBlock. Networks must be unique and non-overlapping across VNet in your subscription, on-premise, and this privateCloud networkBlock attribute. Make sure the CIDR format conforms to (A.B.C.D/X).</td>
</tr>
<tr>
    <td><CopyableCode code="externalCloudLinks" /></td>
    <td><code>array</code></td>
    <td>Array of cloud link IDs from other clouds that connect to this one.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySources" /></td>
    <td><code>array</code></td>
    <td>vCenter Single Sign On Identity Sources.</td>
</tr>
<tr>
    <td><CopyableCode code="internet" /></td>
    <td><code>string</code></td>
    <td>Connectivity to internet is enabled or disabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementCluster" /></td>
    <td><code>object</code></td>
    <td>The default cluster used for management. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementNetwork" /></td>
    <td><code>string</code></td>
    <td>Network used to access vCenter Server and NSX-T Manager.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBlock" /></td>
    <td><code>string</code></td>
    <td>The block of addresses should be unique across VNet in your subscription as well as on-premise. Make sure the CIDR format is conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is between 0 and 22. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nsxPublicIpQuotaRaised" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate whether the private cloud has the quota for provisioned NSX Public IP count raised from 64 to 1024. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nsxtCertificateThumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the NSX-T Manager SSL certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="nsxtPassword" /></td>
    <td><code>string</code></td>
    <td>Optionally, set the NSX-T Manager password when the private cloud is created.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningNetwork" /></td>
    <td><code>string</code></td>
    <td>Used for virtual machine cold migration, cloning, and snapshot migration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Cancelled", "Pending", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Cancelled, Pending, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryCircuit" /></td>
    <td><code>object</code></td>
    <td>A secondary expressRoute circuit from a separate AZ. Only present in a stretched private cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (Stock Keeping Unit) assigned to this resource. Required.</td>
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
    <td><CopyableCode code="vcenterCertificateThumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the vCenter Server SSL certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterPassword" /></td>
    <td><code>string</code></td>
    <td>Optionally, set the vCenter admin password when the private cloud is created.</td>
</tr>
<tr>
    <td><CopyableCode code="vcfLicense" /></td>
    <td><code>object</code></td>
    <td>The private cloud license.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="vmotionNetwork" /></td>
    <td><code>string</code></td>
    <td>Used for live migration of virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="availability" /></td>
    <td><code>object</code></td>
    <td>Properties describing how the cloud is distributed across availability zones.</td>
</tr>
<tr>
    <td><CopyableCode code="circuit" /></td>
    <td><code>object</code></td>
    <td>An ExpressRoute Circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZoneType" /></td>
    <td><code>string</code></td>
    <td>The type of DNS zone to use. Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer managed key encryption, can be enabled or disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>The endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedNetworkBlocks" /></td>
    <td><code>array</code></td>
    <td>Array of additional networks noncontiguous with networkBlock. Networks must be unique and non-overlapping across VNet in your subscription, on-premise, and this privateCloud networkBlock attribute. Make sure the CIDR format conforms to (A.B.C.D/X).</td>
</tr>
<tr>
    <td><CopyableCode code="externalCloudLinks" /></td>
    <td><code>array</code></td>
    <td>Array of cloud link IDs from other clouds that connect to this one.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySources" /></td>
    <td><code>array</code></td>
    <td>vCenter Single Sign On Identity Sources.</td>
</tr>
<tr>
    <td><CopyableCode code="internet" /></td>
    <td><code>string</code></td>
    <td>Connectivity to internet is enabled or disabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementCluster" /></td>
    <td><code>object</code></td>
    <td>The default cluster used for management. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementNetwork" /></td>
    <td><code>string</code></td>
    <td>Network used to access vCenter Server and NSX-T Manager.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBlock" /></td>
    <td><code>string</code></td>
    <td>The block of addresses should be unique across VNet in your subscription as well as on-premise. Make sure the CIDR format is conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is between 0 and 22. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nsxPublicIpQuotaRaised" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate whether the private cloud has the quota for provisioned NSX Public IP count raised from 64 to 1024. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nsxtCertificateThumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the NSX-T Manager SSL certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="nsxtPassword" /></td>
    <td><code>string</code></td>
    <td>Optionally, set the NSX-T Manager password when the private cloud is created.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningNetwork" /></td>
    <td><code>string</code></td>
    <td>Used for virtual machine cold migration, cloning, and snapshot migration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Cancelled", "Pending", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Cancelled, Pending, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryCircuit" /></td>
    <td><code>object</code></td>
    <td>A secondary expressRoute circuit from a separate AZ. Only present in a stretched private cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (Stock Keeping Unit) assigned to this resource. Required.</td>
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
    <td><CopyableCode code="vcenterCertificateThumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the vCenter Server SSL certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterPassword" /></td>
    <td><code>string</code></td>
    <td>Optionally, set the vCenter admin password when the private cloud is created.</td>
</tr>
<tr>
    <td><CopyableCode code="vcfLicense" /></td>
    <td><code>object</code></td>
    <td>The private cloud license.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="vmotionNetwork" /></td>
    <td><code>string</code></td>
    <td>Used for live migration of virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_in_subscription">

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
    <td><CopyableCode code="availability" /></td>
    <td><code>object</code></td>
    <td>Properties describing how the cloud is distributed across availability zones.</td>
</tr>
<tr>
    <td><CopyableCode code="circuit" /></td>
    <td><code>object</code></td>
    <td>An ExpressRoute Circuit.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZoneType" /></td>
    <td><code>string</code></td>
    <td>The type of DNS zone to use. Known values are: "Public" and "Private". (Public, Private)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>Customer managed key encryption, can be enabled or disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>The endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedNetworkBlocks" /></td>
    <td><code>array</code></td>
    <td>Array of additional networks noncontiguous with networkBlock. Networks must be unique and non-overlapping across VNet in your subscription, on-premise, and this privateCloud networkBlock attribute. Make sure the CIDR format conforms to (A.B.C.D/X).</td>
</tr>
<tr>
    <td><CopyableCode code="externalCloudLinks" /></td>
    <td><code>array</code></td>
    <td>Array of cloud link IDs from other clouds that connect to this one.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySources" /></td>
    <td><code>array</code></td>
    <td>vCenter Single Sign On Identity Sources.</td>
</tr>
<tr>
    <td><CopyableCode code="internet" /></td>
    <td><code>string</code></td>
    <td>Connectivity to internet is enabled or disabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementCluster" /></td>
    <td><code>object</code></td>
    <td>The default cluster used for management. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managementNetwork" /></td>
    <td><code>string</code></td>
    <td>Network used to access vCenter Server and NSX-T Manager.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBlock" /></td>
    <td><code>string</code></td>
    <td>The block of addresses should be unique across VNet in your subscription as well as on-premise. Make sure the CIDR format is conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is between 0 and 22. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nsxPublicIpQuotaRaised" /></td>
    <td><code>string</code></td>
    <td>Flag to indicate whether the private cloud has the quota for provisioned NSX Public IP count raised from 64 to 1024. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="nsxtCertificateThumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the NSX-T Manager SSL certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="nsxtPassword" /></td>
    <td><code>string</code></td>
    <td>Optionally, set the NSX-T Manager password when the private cloud is created.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningNetwork" /></td>
    <td><code>string</code></td>
    <td>Used for virtual machine cold migration, cloning, and snapshot migration.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Cancelled", "Pending", "Building", "Deleting", and "Updating". (Succeeded, Failed, Canceled, Cancelled, Pending, Building, Deleting, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryCircuit" /></td>
    <td><code>object</code></td>
    <td>A secondary expressRoute circuit from a separate AZ. Only present in a stretched private cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU (Stock Keeping Unit) assigned to this resource. Required.</td>
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
    <td><CopyableCode code="vcenterCertificateThumbprint" /></td>
    <td><code>string</code></td>
    <td>Thumbprint of the vCenter Server SSL certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="vcenterPassword" /></td>
    <td><code>string</code></td>
    <td>Optionally, set the vCenter admin password when the private cloud is created.</td>
</tr>
<tr>
    <td><CopyableCode code="vcfLicense" /></td>
    <td><code>object</code></td>
    <td>The private cloud license.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkId" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the virtual network.</td>
</tr>
<tr>
    <td><CopyableCode code="vmotionNetwork" /></td>
    <td><code>string</code></td>
    <td>Used for live migration of virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List PrivateCloud resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_in_subscription"><CopyableCode code="list_in_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List PrivateCloud resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create a PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create a PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a PrivateCloud.</td>
</tr>
<tr>
    <td><a href="#list_admin_credentials"><CopyableCode code="list_admin_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the admin credentials for the private cloud.</td>
</tr>
<tr>
    <td><a href="#get_vcf_license"><CopyableCode code="get_vcf_license" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the license for the private cloud.</td>
</tr>
<tr>
    <td><a href="#rotate_vcenter_password"><CopyableCode code="rotate_vcenter_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotate the vCenter password.</td>
</tr>
<tr>
    <td><a href="#rotate_nsxt_password"><CopyableCode code="rotate_nsxt_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-private_cloud_name"><code>private_cloud_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotate the NSX-T Manager password.</td>
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
<tr id="parameter-private_cloud_name">
    <td><CopyableCode code="private_cloud_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private cloud. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_in_subscription', value: 'list_in_subscription' }
    ]}
>
<TabItem value="get">

Get a PrivateCloud.

```sql
SELECT
id,
name,
availability,
circuit,
dnsZoneType,
encryption,
endpoints,
extendedNetworkBlocks,
externalCloudLinks,
identity,
identitySources,
internet,
location,
managementCluster,
managementNetwork,
networkBlock,
nsxPublicIpQuotaRaised,
nsxtCertificateThumbprint,
nsxtPassword,
provisioningNetwork,
provisioningState,
secondaryCircuit,
sku,
systemData,
tags,
type,
vcenterCertificateThumbprint,
vcenterPassword,
vcfLicense,
virtualNetworkId,
vmotionNetwork,
zones
FROM azure_isv.avs.private_clouds
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND private_cloud_name = '{{ private_cloud_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List PrivateCloud resources by resource group.

```sql
SELECT
id,
name,
availability,
circuit,
dnsZoneType,
encryption,
endpoints,
extendedNetworkBlocks,
externalCloudLinks,
identity,
identitySources,
internet,
location,
managementCluster,
managementNetwork,
networkBlock,
nsxPublicIpQuotaRaised,
nsxtCertificateThumbprint,
nsxtPassword,
provisioningNetwork,
provisioningState,
secondaryCircuit,
sku,
systemData,
tags,
type,
vcenterCertificateThumbprint,
vcenterPassword,
vcfLicense,
virtualNetworkId,
vmotionNetwork,
zones
FROM azure_isv.avs.private_clouds
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_in_subscription">

List PrivateCloud resources by subscription ID.

```sql
SELECT
id,
name,
availability,
circuit,
dnsZoneType,
encryption,
endpoints,
extendedNetworkBlocks,
externalCloudLinks,
identity,
identitySources,
internet,
location,
managementCluster,
managementNetwork,
networkBlock,
nsxPublicIpQuotaRaised,
nsxtCertificateThumbprint,
nsxtPassword,
provisioningNetwork,
provisioningState,
secondaryCircuit,
sku,
systemData,
tags,
type,
vcenterCertificateThumbprint,
vcenterPassword,
vcfLicense,
virtualNetworkId,
vmotionNetwork,
zones
FROM azure_isv.avs.private_clouds
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

Create a PrivateCloud.

```sql
INSERT INTO azure_isv.avs.private_clouds (
tags,
location,
properties,
sku,
identity,
zones,
resource_group_name,
private_cloud_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ private_cloud_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: private_clouds
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the private_clouds resource.
    - name: private_cloud_name
      value: "{{ private_cloud_name }}"
      description: Required parameter for the private_clouds resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the private_clouds resource.
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
        The resource-specific properties for this resource.
      value:
        managementCluster:
          clusterSize: {{ clusterSize }}
          provisioningState: "{{ provisioningState }}"
          clusterId: {{ clusterId }}
          hosts:
            - "{{ hosts }}"
          vsanDatastoreName: "{{ vsanDatastoreName }}"
        internet: "{{ internet }}"
        identitySources:
          - name: "{{ name }}"
            alias: "{{ alias }}"
            domain: "{{ domain }}"
            baseUserDN: "{{ baseUserDN }}"
            baseGroupDN: "{{ baseGroupDN }}"
            primaryServer: "{{ primaryServer }}"
            secondaryServer: "{{ secondaryServer }}"
            ssl: "{{ ssl }}"
            username: "{{ username }}"
            password: "{{ password }}"
        availability:
          strategy: "{{ strategy }}"
          zone: {{ zone }}
          secondaryZone: {{ secondaryZone }}
        encryption:
          status: "{{ status }}"
          keyVaultProperties:
            keyName: "{{ keyName }}"
            keyVersion: "{{ keyVersion }}"
            autoDetectedKeyVersion: "{{ autoDetectedKeyVersion }}"
            keyVaultUrl: "{{ keyVaultUrl }}"
            keyState: "{{ keyState }}"
            versionType: "{{ versionType }}"
        extendedNetworkBlocks:
          - "{{ extendedNetworkBlocks }}"
        provisioningState: "{{ provisioningState }}"
        circuit:
          primarySubnet: "{{ primarySubnet }}"
          secondarySubnet: "{{ secondarySubnet }}"
          expressRouteID: "{{ expressRouteID }}"
          expressRoutePrivatePeeringID: "{{ expressRoutePrivatePeeringID }}"
        endpoints:
          nsxtManager: "{{ nsxtManager }}"
          vcsa: "{{ vcsa }}"
          hcxCloudManager: "{{ hcxCloudManager }}"
          nsxtManagerIp: "{{ nsxtManagerIp }}"
          vcenterIp: "{{ vcenterIp }}"
          hcxCloudManagerIp: "{{ hcxCloudManagerIp }}"
        networkBlock: "{{ networkBlock }}"
        managementNetwork: "{{ managementNetwork }}"
        provisioningNetwork: "{{ provisioningNetwork }}"
        vmotionNetwork: "{{ vmotionNetwork }}"
        vcenterPassword: "{{ vcenterPassword }}"
        nsxtPassword: "{{ nsxtPassword }}"
        vcenterCertificateThumbprint: "{{ vcenterCertificateThumbprint }}"
        nsxtCertificateThumbprint: "{{ nsxtCertificateThumbprint }}"
        externalCloudLinks:
          - "{{ externalCloudLinks }}"
        secondaryCircuit:
          primarySubnet: "{{ primarySubnet }}"
          secondarySubnet: "{{ secondarySubnet }}"
          expressRouteID: "{{ expressRouteID }}"
          expressRoutePrivatePeeringID: "{{ expressRoutePrivatePeeringID }}"
        nsxPublicIpQuotaRaised: "{{ nsxPublicIpQuotaRaised }}"
        virtualNetworkId: "{{ virtualNetworkId }}"
        dnsZoneType: "{{ dnsZoneType }}"
        vcfLicense:
          kind: "{{ kind }}"
          provisioningState: "{{ provisioningState }}"
    - name: sku
      description: |
        The SKU (Stock Keeping Unit) assigned to this resource. Required.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

Update a PrivateCloud.

```sql
UPDATE azure_isv.avs.private_clouds
SET 
tags = '{{ tags }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
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

Create a PrivateCloud.

```sql
REPLACE azure_isv.avs.private_clouds
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
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

Delete a PrivateCloud.

```sql
DELETE FROM azure_isv.avs.private_clouds
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND private_cloud_name = '{{ private_cloud_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_admin_credentials"
    values={[
        { label: 'list_admin_credentials', value: 'list_admin_credentials' },
        { label: 'get_vcf_license', value: 'get_vcf_license' },
        { label: 'rotate_vcenter_password', value: 'rotate_vcenter_password' },
        { label: 'rotate_nsxt_password', value: 'rotate_nsxt_password' }
    ]}
>
<TabItem value="list_admin_credentials">

List the admin credentials for the private cloud.

```sql
EXEC azure_isv.avs.private_clouds.list_admin_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_vcf_license">

Get the license for the private cloud.

```sql
EXEC azure_isv.avs.private_clouds.get_vcf_license 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rotate_vcenter_password">

Rotate the vCenter password.

```sql
EXEC azure_isv.avs.private_clouds.rotate_vcenter_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="rotate_nsxt_password">

Rotate the NSX-T Manager password.

```sql
EXEC azure_isv.avs.private_clouds.rotate_nsxt_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@private_cloud_name='{{ private_cloud_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
