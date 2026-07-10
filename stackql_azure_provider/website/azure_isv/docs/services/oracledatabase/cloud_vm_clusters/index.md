--- 
title: cloud_vm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_vm_clusters
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>cloud_vm_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_vm_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.cloud_vm_clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_private_ip_addresses"
    values={[
        { label: 'list_private_ip_addresses', value: 'list_private_ip_addresses' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_private_ip_addresses">

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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>PrivateIpAddresses displayName. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnameLabel" /></td>
    <td><code>string</code></td>
    <td>PrivateIpAddresses hostnameLabel. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>PrivateIpAddresses ipAddress. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>PrivateIpAddresses Id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>PrivateIpAddresses subnetId. Required.</td>
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
    <td><CopyableCode code="backupSubnetCidr" /></td>
    <td><code>string</code></td>
    <td>Client OCI backup subnet CIDR, default is 192.168.252.0/22.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudExadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>Cloud Exadata Infrastructure ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="compartmentId" /></td>
    <td><code>string</code></td>
    <td>Cluster compartmentId.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the VM Cluster. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="computeNodes" /></td>
    <td><code>array</code></td>
    <td>The list of compute servers to be added to the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionOptions" /></td>
    <td><code>object</code></td>
    <td>Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStoragePercentage" /></td>
    <td><code>integer</code></td>
    <td>The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration `_ in the Exadata documentation for details on the impact of the configuration settings on storage.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The data disk group size to be allocated in TBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The local node storage to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServers" /></td>
    <td><code>array</code></td>
    <td>The list of DB servers.</td>
</tr>
<tr>
    <td><CopyableCode code="diskRedundancy" /></td>
    <td><code>string</code></td>
    <td>The type of redundancy configured for the cloud Vm cluster. NORMAL is 2-way redundancy. HIGH is 3-way redundancy. Known values are: "High" and "Normal". (High, Normal)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The domain name for the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleDbStorageVaultId" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault ID.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemConfigurationDetails" /></td>
    <td><code>array</code></td>
    <td>Array of mount path and size.</td>
</tr>
<tr>
    <td><CopyableCode code="giVersion" /></td>
    <td><code>string</code></td>
    <td>Oracle Grid Infrastructure (GI) software version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iormConfigCache" /></td>
    <td><code>object</code></td>
    <td>iormConfigCache details for cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalBackupEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isSparseDiskgroupEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateHistoryEntryId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the last maintenance update history entry.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
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
    <td>The port number configured for the listener on the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the cloud VM cluster.</td>
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
    <td>Cloud VM Cluster ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="ocpuCount" /></td>
    <td><code>number</code></td>
    <td>The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsRecordId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIpIds" /></td>
    <td><code>array</code></td>
    <td>The Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
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
    <td>The model name of the Exadata hardware running the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageManagementType" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the type of storage management for the VM cluster is ASM or Exascale. Known values are: "ASM" and "Exascale". (ASM, Exascale)</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The data disk group size to be allocated in GBs per VM.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the cloud VM cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the cloud VM cluster. For details, see `Exadata Infrastructure Time Zones `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipIds" /></td>
    <td><code>array</code></td>
    <td>The virtual IP (VIP) addresses associated with the cloud VM cluster. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the cloud VM cluster is associated with.</td>
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
    <td><CopyableCode code="cloudExadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>Cloud Exadata Infrastructure ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="compartmentId" /></td>
    <td><code>string</code></td>
    <td>Cluster compartmentId.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the VM Cluster. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="computeNodes" /></td>
    <td><code>array</code></td>
    <td>The list of compute servers to be added to the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionOptions" /></td>
    <td><code>object</code></td>
    <td>Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStoragePercentage" /></td>
    <td><code>integer</code></td>
    <td>The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration `_ in the Exadata documentation for details on the impact of the configuration settings on storage.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The data disk group size to be allocated in TBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The local node storage to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServers" /></td>
    <td><code>array</code></td>
    <td>The list of DB servers.</td>
</tr>
<tr>
    <td><CopyableCode code="diskRedundancy" /></td>
    <td><code>string</code></td>
    <td>The type of redundancy configured for the cloud Vm cluster. NORMAL is 2-way redundancy. HIGH is 3-way redundancy. Known values are: "High" and "Normal". (High, Normal)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The domain name for the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleDbStorageVaultId" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault ID.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemConfigurationDetails" /></td>
    <td><code>array</code></td>
    <td>Array of mount path and size.</td>
</tr>
<tr>
    <td><CopyableCode code="giVersion" /></td>
    <td><code>string</code></td>
    <td>Oracle Grid Infrastructure (GI) software version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iormConfigCache" /></td>
    <td><code>object</code></td>
    <td>iormConfigCache details for cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalBackupEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isSparseDiskgroupEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateHistoryEntryId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the last maintenance update history entry.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
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
    <td>The port number configured for the listener on the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the cloud VM cluster.</td>
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
    <td>Cloud VM Cluster ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="ocpuCount" /></td>
    <td><code>number</code></td>
    <td>The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsRecordId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIpIds" /></td>
    <td><code>array</code></td>
    <td>The Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
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
    <td>The model name of the Exadata hardware running the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageManagementType" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the type of storage management for the VM cluster is ASM or Exascale. Known values are: "ASM" and "Exascale". (ASM, Exascale)</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The data disk group size to be allocated in GBs per VM.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the cloud VM cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the cloud VM cluster. For details, see `Exadata Infrastructure Time Zones `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipIds" /></td>
    <td><code>array</code></td>
    <td>The virtual IP (VIP) addresses associated with the cloud VM cluster. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the cloud VM cluster is associated with.</td>
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
    <td><CopyableCode code="cloudExadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>Cloud Exadata Infrastructure ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="compartmentId" /></td>
    <td><code>string</code></td>
    <td>Cluster compartmentId.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the VM Cluster. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="computeNodes" /></td>
    <td><code>array</code></td>
    <td>The list of compute servers to be added to the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionOptions" /></td>
    <td><code>object</code></td>
    <td>Indicates user preferences for the various diagnostic collection options for the VM cluster/Cloud VM cluster/VMBM DBCS.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStoragePercentage" /></td>
    <td><code>integer</code></td>
    <td>The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See `Storage Configuration `_ in the Exadata documentation for details on the impact of the configuration settings on storage.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The data disk group size to be allocated in TBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The local node storage to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServers" /></td>
    <td><code>array</code></td>
    <td>The list of DB servers.</td>
</tr>
<tr>
    <td><CopyableCode code="diskRedundancy" /></td>
    <td><code>string</code></td>
    <td>The type of redundancy configured for the cloud Vm cluster. NORMAL is 2-way redundancy. HIGH is 3-way redundancy. Known values are: "High" and "Normal". (High, Normal)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The domain name for the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleDbStorageVaultId" /></td>
    <td><code>string</code></td>
    <td>Exadata Database Storage Vault ID.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemConfigurationDetails" /></td>
    <td><code>array</code></td>
    <td>Array of mount path and size.</td>
</tr>
<tr>
    <td><CopyableCode code="giVersion" /></td>
    <td><code>string</code></td>
    <td>Oracle Grid Infrastructure (GI) software version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iormConfigCache" /></td>
    <td><code>object</code></td>
    <td>iormConfigCache details for cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isLocalBackupEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="isSparseDiskgroupEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateHistoryEntryId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the last maintenance update history entry.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
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
    <td>The port number configured for the listener on the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the cloud VM cluster.</td>
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
    <td>Cloud VM Cluster ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="ocpuCount" /></td>
    <td><code>number</code></td>
    <td>The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsRecordId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIpIds" /></td>
    <td><code>array</code></td>
    <td>The Single Client Access Name (SCAN) IP addresses associated with the cloud VM cluster. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
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
    <td>The model name of the Exadata hardware running the cloud VM cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the cloud VM cluster. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageManagementType" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the type of storage management for the VM cluster is ASM or Exascale. Known values are: "ASM" and "Exascale". (ASM, Exascale)</td>
</tr>
<tr>
    <td><CopyableCode code="storageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The data disk group size to be allocated in GBs per VM.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the cloud VM cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the cloud VM cluster. For details, see `Exadata Infrastructure Time Zones `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vipIds" /></td>
    <td><code>array</code></td>
    <td>The virtual IP (VIP) addresses associated with the cloud VM cluster. The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster. **Note:** For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetId" /></td>
    <td><code>string</code></td>
    <td>VNET for network connectivity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the zone the cloud VM cluster is associated with.</td>
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
    <td><a href="#list_private_ip_addresses"><CopyableCode code="list_private_ip_addresses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Private IP Addresses by the provided filter.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List CloudVmCluster resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List CloudVmCluster resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#add_vms"><CopyableCode code="add_vms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-dbServers"><code>dbServers</code></a></td>
    <td></td>
    <td>Add VMs to the VM Cluster.</td>
</tr>
<tr>
    <td><a href="#remove_vms"><CopyableCode code="remove_vms" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-dbServers"><code>dbServers</code></a></td>
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
<tr id="parameter-cloudvmclustername">
    <td><CopyableCode code="cloudvmclustername" /></td>
    <td><code>string</code></td>
    <td>CloudVmCluster name. Required.</td>
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
    defaultValue="list_private_ip_addresses"
    values={[
        { label: 'list_private_ip_addresses', value: 'list_private_ip_addresses' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_private_ip_addresses">

List Private IP Addresses by the provided filter.

```sql
SELECT
displayName,
hostnameLabel,
ipAddress,
ocid,
subnetId
FROM azure_isv.oracledatabase.cloud_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudvmclustername = '{{ cloudvmclustername }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a CloudVmCluster.

```sql
SELECT
id,
name,
backupSubnetCidr,
cloudExadataInfrastructureId,
clusterName,
compartmentId,
computeModel,
computeNodes,
cpuCoreCount,
dataCollectionOptions,
dataStoragePercentage,
dataStorageSizeInTbs,
dbNodeStorageSizeInGbs,
dbServers,
diskRedundancy,
displayName,
domain,
exascaleDbStorageVaultId,
fileSystemConfigurationDetails,
giVersion,
hostname,
iormConfigCache,
isLocalBackupEnabled,
isSparseDiskgroupEnabled,
lastUpdateHistoryEntryId,
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
ocpuCount,
provisioningState,
scanDnsName,
scanDnsRecordId,
scanIpIds,
scanListenerPortTcp,
scanListenerPortTcpSsl,
shape,
sshPublicKeys,
storageManagementType,
storageSizeInGbs,
subnetId,
subnetOcid,
systemData,
systemVersion,
tags,
timeCreated,
timeZone,
type,
vipIds,
vnetId,
zoneId
FROM azure_isv.oracledatabase.cloud_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudvmclustername = '{{ cloudvmclustername }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List CloudVmCluster resources by resource group.

```sql
SELECT
id,
name,
backupSubnetCidr,
cloudExadataInfrastructureId,
clusterName,
compartmentId,
computeModel,
computeNodes,
cpuCoreCount,
dataCollectionOptions,
dataStoragePercentage,
dataStorageSizeInTbs,
dbNodeStorageSizeInGbs,
dbServers,
diskRedundancy,
displayName,
domain,
exascaleDbStorageVaultId,
fileSystemConfigurationDetails,
giVersion,
hostname,
iormConfigCache,
isLocalBackupEnabled,
isSparseDiskgroupEnabled,
lastUpdateHistoryEntryId,
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
ocpuCount,
provisioningState,
scanDnsName,
scanDnsRecordId,
scanIpIds,
scanListenerPortTcp,
scanListenerPortTcpSsl,
shape,
sshPublicKeys,
storageManagementType,
storageSizeInGbs,
subnetId,
subnetOcid,
systemData,
systemVersion,
tags,
timeCreated,
timeZone,
type,
vipIds,
vnetId,
zoneId
FROM azure_isv.oracledatabase.cloud_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List CloudVmCluster resources by subscription ID.

```sql
SELECT
id,
name,
backupSubnetCidr,
cloudExadataInfrastructureId,
clusterName,
compartmentId,
computeModel,
computeNodes,
cpuCoreCount,
dataCollectionOptions,
dataStoragePercentage,
dataStorageSizeInTbs,
dbNodeStorageSizeInGbs,
dbServers,
diskRedundancy,
displayName,
domain,
exascaleDbStorageVaultId,
fileSystemConfigurationDetails,
giVersion,
hostname,
iormConfigCache,
isLocalBackupEnabled,
isSparseDiskgroupEnabled,
lastUpdateHistoryEntryId,
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
ocpuCount,
provisioningState,
scanDnsName,
scanDnsRecordId,
scanIpIds,
scanListenerPortTcp,
scanListenerPortTcpSsl,
shape,
sshPublicKeys,
storageManagementType,
storageSizeInGbs,
subnetId,
subnetOcid,
systemData,
systemVersion,
tags,
timeCreated,
timeZone,
type,
vipIds,
vnetId,
zoneId
FROM azure_isv.oracledatabase.cloud_vm_clusters
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

Create a CloudVmCluster.

```sql
INSERT INTO azure_isv.oracledatabase.cloud_vm_clusters (
tags,
location,
properties,
resource_group_name,
cloudvmclustername,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cloudvmclustername }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: cloud_vm_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cloud_vm_clusters resource.
    - name: cloudvmclustername
      value: "{{ cloudvmclustername }}"
      description: Required parameter for the cloud_vm_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cloud_vm_clusters resource.
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
        listenerPort: {{ listenerPort }}
        nodeCount: {{ nodeCount }}
        storageSizeInGbs: {{ storageSizeInGbs }}
        fileSystemConfigurationDetails:
          - mountPoint: "{{ mountPoint }}"
            fileSystemSizeGb: {{ fileSystemSizeGb }}
        dataStorageSizeInTbs: {{ dataStorageSizeInTbs }}
        dbNodeStorageSizeInGbs: {{ dbNodeStorageSizeInGbs }}
        memorySizeInGbs: {{ memorySizeInGbs }}
        timeCreated: "{{ timeCreated }}"
        lifecycleDetails: "{{ lifecycleDetails }}"
        timeZone: "{{ timeZone }}"
        zoneId: "{{ zoneId }}"
        hostname: "{{ hostname }}"
        domain: "{{ domain }}"
        cpuCoreCount: {{ cpuCoreCount }}
        ocpuCount: {{ ocpuCount }}
        clusterName: "{{ clusterName }}"
        dataStoragePercentage: {{ dataStoragePercentage }}
        isLocalBackupEnabled: {{ isLocalBackupEnabled }}
        cloudExadataInfrastructureId: "{{ cloudExadataInfrastructureId }}"
        isSparseDiskgroupEnabled: {{ isSparseDiskgroupEnabled }}
        systemVersion: "{{ systemVersion }}"
        sshPublicKeys:
          - "{{ sshPublicKeys }}"
        licenseModel: "{{ licenseModel }}"
        diskRedundancy: "{{ diskRedundancy }}"
        scanIpIds:
          - "{{ scanIpIds }}"
        vipIds:
          - "{{ vipIds }}"
        scanDnsName: "{{ scanDnsName }}"
        scanListenerPortTcp: {{ scanListenerPortTcp }}
        scanListenerPortTcpSsl: {{ scanListenerPortTcpSsl }}
        scanDnsRecordId: "{{ scanDnsRecordId }}"
        shape: "{{ shape }}"
        provisioningState: "{{ provisioningState }}"
        lifecycleState: "{{ lifecycleState }}"
        vnetId: "{{ vnetId }}"
        giVersion: "{{ giVersion }}"
        ociUrl: "{{ ociUrl }}"
        nsgUrl: "{{ nsgUrl }}"
        subnetId: "{{ subnetId }}"
        backupSubnetCidr: "{{ backupSubnetCidr }}"
        nsgCidrs:
          - source: "{{ source }}"
            destinationPortRange:
              min: {{ min }}
              max: {{ max }}
        dataCollectionOptions:
          isDiagnosticsEventsEnabled: {{ isDiagnosticsEventsEnabled }}
          isHealthMonitoringEnabled: {{ isHealthMonitoringEnabled }}
          isIncidentLogsEnabled: {{ isIncidentLogsEnabled }}
        displayName: "{{ displayName }}"
        computeNodes:
          - "{{ computeNodes }}"
        iormConfigCache:
          dbPlans:
            - dbName: "{{ dbName }}"
              flashCacheLimit: "{{ flashCacheLimit }}"
              share: {{ share }}
          lifecycleDetails: "{{ lifecycleDetails }}"
          lifecycleState: "{{ lifecycleState }}"
          objective: "{{ objective }}"
        lastUpdateHistoryEntryId: "{{ lastUpdateHistoryEntryId }}"
        dbServers:
          - "{{ dbServers }}"
        compartmentId: "{{ compartmentId }}"
        subnetOcid: "{{ subnetOcid }}"
        computeModel: "{{ computeModel }}"
        exascaleDbStorageVaultId: "{{ exascaleDbStorageVaultId }}"
        storageManagementType: "{{ storageManagementType }}"
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

Update a CloudVmCluster.

```sql
UPDATE azure_isv.oracledatabase.cloud_vm_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cloudvmclustername = '{{ cloudvmclustername }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create a CloudVmCluster.

```sql
REPLACE azure_isv.oracledatabase.cloud_vm_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cloudvmclustername = '{{ cloudvmclustername }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete a CloudVmCluster.

```sql
DELETE FROM azure_isv.oracledatabase.cloud_vm_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cloudvmclustername = '{{ cloudvmclustername }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_vms"
    values={[
        { label: 'add_vms', value: 'add_vms' },
        { label: 'remove_vms', value: 'remove_vms' }
    ]}
>
<TabItem value="add_vms">

Add VMs to the VM Cluster.

```sql
EXEC azure_isv.oracledatabase.cloud_vm_clusters.add_vms 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloudvmclustername='{{ cloudvmclustername }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"dbServers": "{{ dbServers }}"
}'
;
```
</TabItem>
<TabItem value="remove_vms">

Remove VMs from the VM Cluster.

```sql
EXEC azure_isv.oracledatabase.cloud_vm_clusters.remove_vms 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloudvmclustername='{{ cloudvmclustername }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"dbServers": "{{ dbServers }}"
}'
;
```
</TabItem>
</Tabs>
