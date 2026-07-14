--- 
title: exadb_vm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - exadb_vm_clusters
  - oracle_database
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

Creates, updates, deletes, gets or lists an <code>exadb_vm_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exadb_vm_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.exadb_vm_clusters" /></td></tr>
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
    <td><CopyableCode code="backupSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Client OCI backup subnet CIDR, default is 192.168.252.0/22.</td>
</tr>
<tr>
    <td><CopyableCode code="backupSubnetOcid" /></td>
    <td><code>string</code></td>
    <td>Cluster backup subnet ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for Exadata VM cluster on Exascale Infrastructure. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionOptions" /></td>
    <td><code>object</code></td>
    <td>Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>A domain name used for the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledEcpuCount" /></td>
    <td><code>integer</code></td>
    <td>The number of ECPUs to enable for an Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleDbStorageVaultId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource ID of the Exadata Database Storage Vault. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="giVersion" /></td>
    <td><code>string</code></td>
    <td>Oracle Grid Infrastructure (GI) software version.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageOcid" /></td>
    <td><code>string</code></td>
    <td>Grid Setup will be done using this Grid Image OCID. Can be obtained using giMinorVersions API.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageType" /></td>
    <td><code>string</code></td>
    <td>The type of Grid Image. Known values are: "ReleaseUpdate" and "CustomImage". (ReleaseUpdate, CustomImage)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iormConfigCache" /></td>
    <td><code>object</code></td>
    <td>iormConfigCache details for Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the Exadata VM cluster on Exascale Infrastructure. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "MaintenanceInProgress", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, MaintenanceInProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="listenerPort" /></td>
    <td><code>integer</code></td>
    <td>The port number configured for the listener on the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory that you want to be allocated in GBs. Memory is calculated based on 11 GB per VM core reserved.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nsgCidrs" /></td>
    <td><code>array</code></td>
    <td>CIDR blocks for additional NSG ingress rules. The VNET CIDRs used to provision the VM Cluster will be added by default.</td>
</tr>
<tr>
    <td><CopyableCode code="nsgUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI Network Security Group exposed to Azure Customer via the Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>ExadbVmCluster ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="privateZoneOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the Exadata VM cluster on Exascale Infrastructure is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Exadata VM cluster on Exascale Infrastructure provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsRecordId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DNS record for the SCAN IP addresses that are associated with the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIpIds" /></td>
    <td><code>array</code></td>
    <td>The Single Client Access Name (SCAN) IP addresses associated with the Exadata VM cluster on Exascale Infrastructure. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="scanListenerPortTcp" /></td>
    <td><code>integer</code></td>
    <td>The TCP Single Client Access Name (SCAN) port. The default port is 1521.</td>
</tr>
<tr>
    <td><CopyableCode code="scanListenerPortTcpSsl" /></td>
    <td><code>integer</code></td>
    <td>The TCPS Single Client Access Name (SCAN) port. The default port is 2484.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the Exadata VM cluster on Exascale Infrastructure resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeAttribute" /></td>
    <td><code>string</code></td>
    <td>The type of Exascale storage used for Exadata VM cluster. Known values are: "SMART_STORAGE" and "BLOCK_STORAGE". (SMART_STORAGE, BLOCK_STORAGE)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Snapshot filesystem storage details.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetOcid" /></td>
    <td><code>string</code></td>
    <td>Cluster subnet ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the Exadata VM cluster on Exascale Infrastructure. For details, see `Exadata Infrastructure Time Zones `_.</td>
</tr>
<tr>
    <td><CopyableCode code="totalEcpuCount" /></td>
    <td><code>integer</code></td>
    <td>The number of Total ECPUs for an Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Total file system storage details.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipIds" /></td>
    <td><code>array</code></td>
    <td>The virtual IP (VIP) addresses associated with the Exadata VM cluster on Exascale Infrastructure. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="vmFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Filesystem storage details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the Exadata VM cluster on Exascale Infrastructure is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="backupSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Client OCI backup subnet CIDR, default is 192.168.252.0/22.</td>
</tr>
<tr>
    <td><CopyableCode code="backupSubnetOcid" /></td>
    <td><code>string</code></td>
    <td>Cluster backup subnet ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for Exadata VM cluster on Exascale Infrastructure. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionOptions" /></td>
    <td><code>object</code></td>
    <td>Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>A domain name used for the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledEcpuCount" /></td>
    <td><code>integer</code></td>
    <td>The number of ECPUs to enable for an Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleDbStorageVaultId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource ID of the Exadata Database Storage Vault. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="giVersion" /></td>
    <td><code>string</code></td>
    <td>Oracle Grid Infrastructure (GI) software version.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageOcid" /></td>
    <td><code>string</code></td>
    <td>Grid Setup will be done using this Grid Image OCID. Can be obtained using giMinorVersions API.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageType" /></td>
    <td><code>string</code></td>
    <td>The type of Grid Image. Known values are: "ReleaseUpdate" and "CustomImage". (ReleaseUpdate, CustomImage)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iormConfigCache" /></td>
    <td><code>object</code></td>
    <td>iormConfigCache details for Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the Exadata VM cluster on Exascale Infrastructure. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "MaintenanceInProgress", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, MaintenanceInProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="listenerPort" /></td>
    <td><code>integer</code></td>
    <td>The port number configured for the listener on the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory that you want to be allocated in GBs. Memory is calculated based on 11 GB per VM core reserved.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nsgCidrs" /></td>
    <td><code>array</code></td>
    <td>CIDR blocks for additional NSG ingress rules. The VNET CIDRs used to provision the VM Cluster will be added by default.</td>
</tr>
<tr>
    <td><CopyableCode code="nsgUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI Network Security Group exposed to Azure Customer via the Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>ExadbVmCluster ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="privateZoneOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the Exadata VM cluster on Exascale Infrastructure is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Exadata VM cluster on Exascale Infrastructure provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsRecordId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DNS record for the SCAN IP addresses that are associated with the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIpIds" /></td>
    <td><code>array</code></td>
    <td>The Single Client Access Name (SCAN) IP addresses associated with the Exadata VM cluster on Exascale Infrastructure. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="scanListenerPortTcp" /></td>
    <td><code>integer</code></td>
    <td>The TCP Single Client Access Name (SCAN) port. The default port is 1521.</td>
</tr>
<tr>
    <td><CopyableCode code="scanListenerPortTcpSsl" /></td>
    <td><code>integer</code></td>
    <td>The TCPS Single Client Access Name (SCAN) port. The default port is 2484.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the Exadata VM cluster on Exascale Infrastructure resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeAttribute" /></td>
    <td><code>string</code></td>
    <td>The type of Exascale storage used for Exadata VM cluster. Known values are: "SMART_STORAGE" and "BLOCK_STORAGE". (SMART_STORAGE, BLOCK_STORAGE)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Snapshot filesystem storage details.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetOcid" /></td>
    <td><code>string</code></td>
    <td>Cluster subnet ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the Exadata VM cluster on Exascale Infrastructure. For details, see `Exadata Infrastructure Time Zones `_.</td>
</tr>
<tr>
    <td><CopyableCode code="totalEcpuCount" /></td>
    <td><code>integer</code></td>
    <td>The number of Total ECPUs for an Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Total file system storage details.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipIds" /></td>
    <td><code>array</code></td>
    <td>The virtual IP (VIP) addresses associated with the Exadata VM cluster on Exascale Infrastructure. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="vmFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Filesystem storage details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the Exadata VM cluster on Exascale Infrastructure is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="backupSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Client OCI backup subnet CIDR, default is 192.168.252.0/22.</td>
</tr>
<tr>
    <td><CopyableCode code="backupSubnetOcid" /></td>
    <td><code>string</code></td>
    <td>Cluster backup subnet ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for Exadata VM cluster on Exascale Infrastructure. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionOptions" /></td>
    <td><code>object</code></td>
    <td>Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>A domain name used for the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="enabledEcpuCount" /></td>
    <td><code>integer</code></td>
    <td>The number of ECPUs to enable for an Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleDbStorageVaultId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource ID of the Exadata Database Storage Vault. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="giVersion" /></td>
    <td><code>string</code></td>
    <td>Oracle Grid Infrastructure (GI) software version.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageOcid" /></td>
    <td><code>string</code></td>
    <td>Grid Setup will be done using this Grid Image OCID. Can be obtained using giMinorVersions API.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageType" /></td>
    <td><code>string</code></td>
    <td>The type of Grid Image. Known values are: "ReleaseUpdate" and "CustomImage". (ReleaseUpdate, CustomImage)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iormConfigCache" /></td>
    <td><code>object</code></td>
    <td>iormConfigCache details for Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the Exadata VM cluster on Exascale Infrastructure. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "MaintenanceInProgress", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, MaintenanceInProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="listenerPort" /></td>
    <td><code>integer</code></td>
    <td>The port number configured for the listener on the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory that you want to be allocated in GBs. Memory is calculated based on 11 GB per VM core reserved.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nsgCidrs" /></td>
    <td><code>array</code></td>
    <td>CIDR blocks for additional NSG ingress rules. The VNET CIDRs used to provision the VM Cluster will be added by default.</td>
</tr>
<tr>
    <td><CopyableCode code="nsgUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI Network Security Group exposed to Azure Customer via the Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>ExadbVmCluster ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="privateZoneOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the Exadata VM cluster on Exascale Infrastructure is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Exadata VM cluster on Exascale Infrastructure provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsRecordId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DNS record for the SCAN IP addresses that are associated with the Exadata VM cluster on Exascale Infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIpIds" /></td>
    <td><code>array</code></td>
    <td>The Single Client Access Name (SCAN) IP addresses associated with the Exadata VM cluster on Exascale Infrastructure. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="scanListenerPortTcp" /></td>
    <td><code>integer</code></td>
    <td>The TCP Single Client Access Name (SCAN) port. The default port is 1521.</td>
</tr>
<tr>
    <td><CopyableCode code="scanListenerPortTcpSsl" /></td>
    <td><code>integer</code></td>
    <td>The TCPS Single Client Access Name (SCAN) port. The default port is 2484.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the Exadata VM cluster on Exascale Infrastructure resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="shapeAttribute" /></td>
    <td><code>string</code></td>
    <td>The type of Exascale storage used for Exadata VM cluster. Known values are: "SMART_STORAGE" and "BLOCK_STORAGE". (SMART_STORAGE, BLOCK_STORAGE)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Snapshot filesystem storage details.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Client subnet. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetOcid" /></td>
    <td><code>string</code></td>
    <td>Cluster subnet ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the Exadata VM cluster on Exascale Infrastructure. For details, see `Exadata Infrastructure Time Zones `_.</td>
</tr>
<tr>
    <td><CopyableCode code="totalEcpuCount" /></td>
    <td><code>integer</code></td>
    <td>The number of Total ECPUs for an Exadata VM cluster on Exascale Infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="totalFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Total file system storage details.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipIds" /></td>
    <td><code>array</code></td>
    <td>The virtual IP (VIP) addresses associated with the Exadata VM cluster on Exascale Infrastructure. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="vmFileSystemStorage" /></td>
    <td><code>object</code></td>
    <td>Filesystem storage details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the Exadata VM cluster on Exascale Infrastructure is associated with.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exadb_vm_cluster_name"><code>exadb_vm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ExadbVmCluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ExadbVmCluster resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ExadbVmCluster resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exadb_vm_cluster_name"><code>exadb_vm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ExadbVmCluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exadb_vm_cluster_name"><code>exadb_vm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a ExadbVmCluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exadb_vm_cluster_name"><code>exadb_vm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ExadbVmCluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exadb_vm_cluster_name"><code>exadb_vm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ExadbVmCluster.</td>
</tr>
<tr>
    <td><a href="#remove_vms"><CopyableCode code="remove_vms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-exadb_vm_cluster_name"><code>exadb_vm_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-dbNodes"><code>dbNodes</code></a></td>
    <td></td>
    <td>Remove VMs from the VM Cluster.</td>
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
<tr id="parameter-exadb_vm_cluster_name">
    <td><CopyableCode code="exadb_vm_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ExadbVmCluster. Required.</td>
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

Get a ExadbVmCluster.

```sql
SELECT
id,
name,
backupSubnetCidr,
backupSubnetOcid,
clusterName,
dataCollectionOptions,
displayName,
domain,
enabledEcpuCount,
exascaleDbStorageVaultId,
giVersion,
gridImageOcid,
gridImageType,
hostname,
iormConfigCache,
licenseModel,
lifecycleDetails,
lifecycleState,
listenerPort,
location,
memorySizeInGbs,
nodeCount,
nsgCidrs,
nsgUrl,
ociUrl,
ocid,
privateZoneOcid,
provisioningState,
scanDnsName,
scanDnsRecordId,
scanIpIds,
scanListenerPortTcp,
scanListenerPortTcpSsl,
shape,
shapeAttribute,
snapshotFileSystemStorage,
sshPublicKeys,
subnetId,
subnetOcid,
systemData,
systemVersion,
tags,
timeZone,
totalEcpuCount,
totalFileSystemStorage,
type,
vipIds,
vmFileSystemStorage,
vnetId,
zoneOcid,
zones
FROM azure_isv.oracle_database.exadb_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND exadb_vm_cluster_name = '{{ exadb_vm_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List ExadbVmCluster resources by resource group.

```sql
SELECT
id,
name,
backupSubnetCidr,
backupSubnetOcid,
clusterName,
dataCollectionOptions,
displayName,
domain,
enabledEcpuCount,
exascaleDbStorageVaultId,
giVersion,
gridImageOcid,
gridImageType,
hostname,
iormConfigCache,
licenseModel,
lifecycleDetails,
lifecycleState,
listenerPort,
location,
memorySizeInGbs,
nodeCount,
nsgCidrs,
nsgUrl,
ociUrl,
ocid,
privateZoneOcid,
provisioningState,
scanDnsName,
scanDnsRecordId,
scanIpIds,
scanListenerPortTcp,
scanListenerPortTcpSsl,
shape,
shapeAttribute,
snapshotFileSystemStorage,
sshPublicKeys,
subnetId,
subnetOcid,
systemData,
systemVersion,
tags,
timeZone,
totalEcpuCount,
totalFileSystemStorage,
type,
vipIds,
vmFileSystemStorage,
vnetId,
zoneOcid,
zones
FROM azure_isv.oracle_database.exadb_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List ExadbVmCluster resources by subscription ID.

```sql
SELECT
id,
name,
backupSubnetCidr,
backupSubnetOcid,
clusterName,
dataCollectionOptions,
displayName,
domain,
enabledEcpuCount,
exascaleDbStorageVaultId,
giVersion,
gridImageOcid,
gridImageType,
hostname,
iormConfigCache,
licenseModel,
lifecycleDetails,
lifecycleState,
listenerPort,
location,
memorySizeInGbs,
nodeCount,
nsgCidrs,
nsgUrl,
ociUrl,
ocid,
privateZoneOcid,
provisioningState,
scanDnsName,
scanDnsRecordId,
scanIpIds,
scanListenerPortTcp,
scanListenerPortTcpSsl,
shape,
shapeAttribute,
snapshotFileSystemStorage,
sshPublicKeys,
subnetId,
subnetOcid,
systemData,
systemVersion,
tags,
timeZone,
totalEcpuCount,
totalFileSystemStorage,
type,
vipIds,
vmFileSystemStorage,
vnetId,
zoneOcid,
zones
FROM azure_isv.oracle_database.exadb_vm_clusters
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

Create a ExadbVmCluster.

```sql
INSERT INTO azure_isv.oracle_database.exadb_vm_clusters (
tags,
location,
properties,
zones,
resource_group_name,
exadb_vm_cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ exadb_vm_cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: exadb_vm_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the exadb_vm_clusters resource.
    - name: exadb_vm_cluster_name
      value: "{{ exadb_vm_cluster_name }}"
      description: Required parameter for the exadb_vm_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the exadb_vm_clusters resource.
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
        ocid: "{{ ocid }}"
        clusterName: "{{ clusterName }}"
        backupSubnetCidr: "{{ backupSubnetCidr }}"
        nsgUrl: "{{ nsgUrl }}"
        provisioningState: "{{ provisioningState }}"
        lifecycleState: "{{ lifecycleState }}"
        vnetId: "{{ vnetId }}"
        subnetId: "{{ subnetId }}"
        dataCollectionOptions:
          isDiagnosticsEventsEnabled: {{ isDiagnosticsEventsEnabled }}
          isHealthMonitoringEnabled: {{ isHealthMonitoringEnabled }}
          isIncidentLogsEnabled: {{ isIncidentLogsEnabled }}
        displayName: "{{ displayName }}"
        domain: "{{ domain }}"
        enabledEcpuCount: {{ enabledEcpuCount }}
        exascaleDbStorageVaultId: "{{ exascaleDbStorageVaultId }}"
        gridImageOcid: "{{ gridImageOcid }}"
        gridImageType: "{{ gridImageType }}"
        giVersion: "{{ giVersion }}"
        hostname: "{{ hostname }}"
        licenseModel: "{{ licenseModel }}"
        memorySizeInGbs: {{ memorySizeInGbs }}
        nodeCount: {{ nodeCount }}
        nsgCidrs:
          - source: "{{ source }}"
            destinationPortRange:
              min: {{ min }}
              max: {{ max }}
        zoneOcid: "{{ zoneOcid }}"
        privateZoneOcid: "{{ privateZoneOcid }}"
        scanListenerPortTcp: {{ scanListenerPortTcp }}
        scanListenerPortTcpSsl: {{ scanListenerPortTcpSsl }}
        listenerPort: {{ listenerPort }}
        shape: "{{ shape }}"
        sshPublicKeys:
          - "{{ sshPublicKeys }}"
        systemVersion: "{{ systemVersion }}"
        timeZone: "{{ timeZone }}"
        totalEcpuCount: {{ totalEcpuCount }}
        vmFileSystemStorage:
          totalSizeInGbs: {{ totalSizeInGbs }}
        lifecycleDetails: "{{ lifecycleDetails }}"
        scanDnsName: "{{ scanDnsName }}"
        scanIpIds:
          - "{{ scanIpIds }}"
        scanDnsRecordId: "{{ scanDnsRecordId }}"
        snapshotFileSystemStorage:
          totalSizeInGbs: {{ totalSizeInGbs }}
        totalFileSystemStorage:
          totalSizeInGbs: {{ totalSizeInGbs }}
        vipIds:
          - "{{ vipIds }}"
        ociUrl: "{{ ociUrl }}"
        iormConfigCache:
          dbPlans:
            - dbName: "{{ dbName }}"
              flashCacheLimit: "{{ flashCacheLimit }}"
              share: {{ share }}
          lifecycleDetails: "{{ lifecycleDetails }}"
          lifecycleState: "{{ lifecycleState }}"
          objective: "{{ objective }}"
        backupSubnetOcid: "{{ backupSubnetOcid }}"
        subnetOcid: "{{ subnetOcid }}"
        shapeAttribute: "{{ shapeAttribute }}"
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

Update a ExadbVmCluster.

```sql
UPDATE azure_isv.oracle_database.exadb_vm_clusters
SET 
zones = '{{ zones }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND exadb_vm_cluster_name = '{{ exadb_vm_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Create a ExadbVmCluster.

```sql
REPLACE azure_isv.oracle_database.exadb_vm_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND exadb_vm_cluster_name = '{{ exadb_vm_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
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

Delete a ExadbVmCluster.

```sql
DELETE FROM azure_isv.oracle_database.exadb_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND exadb_vm_cluster_name = '{{ exadb_vm_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="remove_vms"
    values={[
        { label: 'remove_vms', value: 'remove_vms' }
    ]}
>
<TabItem value="remove_vms">

Remove VMs from the VM Cluster.

```sql
EXEC azure_isv.oracle_database.exadb_vm_clusters.remove_vms 
@resource_group_name='{{ resource_group_name }}' --required, 
@exadb_vm_cluster_name='{{ exadb_vm_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"dbNodes": "{{ dbNodes }}"
}'
;
```
</TabItem>
</Tabs>
