--- 
title: db_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - db_systems
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

Creates, updates, deletes, gets or lists a <code>db_systems</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="db_systems" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.db_systems" /></td></tr>
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
    <td><CopyableCode code="adminPassword" /></td>
    <td><code>string</code></td>
    <td>A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of compute servers for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model for Base Database Service. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value. The ECPU compute model is the recommended model, and the OCPU compute model is legacy. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseEdition" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require EnterpriseEditionExtremePerformance. Required. Known values are: "StandardEdition", "EnterpriseEdition", "EnterpriseEditionHighPerformance", "EnterpriseEditionExtreme", and "EnterpriseEditionDeveloper". (StandardEdition, EnterpriseEdition, EnterpriseEditionHighPerformance, EnterpriseEditionExtreme, EnterpriseEditionDeveloper)</td>
</tr>
<tr>
    <td><CopyableCode code="dbSystemOptions" /></td>
    <td><code>object</code></td>
    <td>The DB system options.</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diskRedundancy" /></td>
    <td><code>string</code></td>
    <td>The type of redundancy configured for the DB system. NORMAL is 2-way redundancy. HIGH is 3-way redundancy. Known values are: "High" and "Normal". (High, Normal)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the DB system. The name does not have to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The domain name for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of a grid infrastructure software image. This is a database software image of the type GRID_IMAGE.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="initialDataStorageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>Size in GB of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to all the databases on the DB system. The default is LicenseIncluded. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the DB system. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "Failed", "Migrated", "MaintenanceInProgress", "NeedsAttention", and "Upgrading". (Provisioning, Available, Updating, Terminating, Terminated, Failed, Migrated, MaintenanceInProgress, NeedsAttention, Upgrading)</td>
</tr>
<tr>
    <td><CopyableCode code="listenerPort" /></td>
    <td><code>integer</code></td>
    <td>The port number configured for the listener on the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>Memory allocated to the DB system, in gigabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAnchorId" /></td>
    <td><code>string</code></td>
    <td>Azure Network Anchor ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="pdbName" /></td>
    <td><code>string</code></td>
    <td>The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>dbSystem provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAnchorId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Anchor ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIps" /></td>
    <td><code>array</code></td>
    <td>The list of Single Client Access Name (SCAN) IP addresses associated with the DB system. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. Note: For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the DB system. The shape determines resources to allocate to the DB system. For virtual machine shapes, the number of CPU cores and memory. For bare metal and Exadata shapes, the number of CPU cores, storage, and memory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source of the database for creating a new database. Required. for creating a new database.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageVolumePerformanceMode" /></td>
    <td><code>string</code></td>
    <td>The block storage volume performance level. Valid values are Balanced and HighPerformance. See `Block Volume Performance `_ for more information. Known values are: "Balanced" and "HighPerformance". (Balanced, HighPerformance)</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the DB system, e.g., UTC, to set the timeZone as UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database version of the DB system.</td>
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
    <td><CopyableCode code="adminPassword" /></td>
    <td><code>string</code></td>
    <td>A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of compute servers for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model for Base Database Service. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value. The ECPU compute model is the recommended model, and the OCPU compute model is legacy. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseEdition" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require EnterpriseEditionExtremePerformance. Required. Known values are: "StandardEdition", "EnterpriseEdition", "EnterpriseEditionHighPerformance", "EnterpriseEditionExtreme", and "EnterpriseEditionDeveloper". (StandardEdition, EnterpriseEdition, EnterpriseEditionHighPerformance, EnterpriseEditionExtreme, EnterpriseEditionDeveloper)</td>
</tr>
<tr>
    <td><CopyableCode code="dbSystemOptions" /></td>
    <td><code>object</code></td>
    <td>The DB system options.</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diskRedundancy" /></td>
    <td><code>string</code></td>
    <td>The type of redundancy configured for the DB system. NORMAL is 2-way redundancy. HIGH is 3-way redundancy. Known values are: "High" and "Normal". (High, Normal)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the DB system. The name does not have to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The domain name for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of a grid infrastructure software image. This is a database software image of the type GRID_IMAGE.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="initialDataStorageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>Size in GB of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to all the databases on the DB system. The default is LicenseIncluded. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the DB system. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "Failed", "Migrated", "MaintenanceInProgress", "NeedsAttention", and "Upgrading". (Provisioning, Available, Updating, Terminating, Terminated, Failed, Migrated, MaintenanceInProgress, NeedsAttention, Upgrading)</td>
</tr>
<tr>
    <td><CopyableCode code="listenerPort" /></td>
    <td><code>integer</code></td>
    <td>The port number configured for the listener on the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>Memory allocated to the DB system, in gigabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAnchorId" /></td>
    <td><code>string</code></td>
    <td>Azure Network Anchor ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="pdbName" /></td>
    <td><code>string</code></td>
    <td>The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>dbSystem provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAnchorId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Anchor ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIps" /></td>
    <td><code>array</code></td>
    <td>The list of Single Client Access Name (SCAN) IP addresses associated with the DB system. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. Note: For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the DB system. The shape determines resources to allocate to the DB system. For virtual machine shapes, the number of CPU cores and memory. For bare metal and Exadata shapes, the number of CPU cores, storage, and memory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source of the database for creating a new database. Required. for creating a new database.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageVolumePerformanceMode" /></td>
    <td><code>string</code></td>
    <td>The block storage volume performance level. Valid values are Balanced and HighPerformance. See `Block Volume Performance `_ for more information. Known values are: "Balanced" and "HighPerformance". (Balanced, HighPerformance)</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the DB system, e.g., UTC, to set the timeZone as UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database version of the DB system.</td>
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
    <td><CopyableCode code="adminPassword" /></td>
    <td><code>string</code></td>
    <td>A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterName" /></td>
    <td><code>string</code></td>
    <td>The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of compute servers for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model for Base Database Service. This is required if using the `computeCount` parameter. If using `cpuCoreCount` then it is an error to specify `computeModel` to a non-null value. The ECPU compute model is the recommended model, and the OCPU compute model is legacy. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseEdition" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require EnterpriseEditionExtremePerformance. Required. Known values are: "StandardEdition", "EnterpriseEdition", "EnterpriseEditionHighPerformance", "EnterpriseEditionExtreme", and "EnterpriseEditionDeveloper". (StandardEdition, EnterpriseEdition, EnterpriseEditionHighPerformance, EnterpriseEditionExtreme, EnterpriseEditionDeveloper)</td>
</tr>
<tr>
    <td><CopyableCode code="dbSystemOptions" /></td>
    <td><code>object</code></td>
    <td>The DB system options.</td>
</tr>
<tr>
    <td><CopyableCode code="dbVersion" /></td>
    <td><code>string</code></td>
    <td>A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diskRedundancy" /></td>
    <td><code>string</code></td>
    <td>The type of redundancy configured for the DB system. NORMAL is 2-way redundancy. HIGH is 3-way redundancy. Known values are: "High" and "Normal". (High, Normal)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The user-friendly name for the DB system. The name does not have to be unique.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The domain name for the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="gridImageOcid" /></td>
    <td><code>string</code></td>
    <td>The OCID of a grid infrastructure software image. This is a database software image of the type GRID_IMAGE.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname for the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="initialDataStorageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>Size in GB of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseModel" /></td>
    <td><code>string</code></td>
    <td>The Oracle license model that applies to all the databases on the DB system. The default is LicenseIncluded. Known values are: "LicenseIncluded" and "BringYourOwnLicense". (LicenseIncluded, BringYourOwnLicense)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the DB system. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "Failed", "Migrated", "MaintenanceInProgress", "NeedsAttention", and "Upgrading". (Provisioning, Available, Updating, Terminating, Terminated, Failed, Migrated, MaintenanceInProgress, NeedsAttention, Upgrading)</td>
</tr>
<tr>
    <td><CopyableCode code="listenerPort" /></td>
    <td><code>integer</code></td>
    <td>The port number configured for the listener on the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>Memory allocated to the DB system, in gigabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAnchorId" /></td>
    <td><code>string</code></td>
    <td>Azure Network Anchor ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="pdbName" /></td>
    <td><code>string</code></td>
    <td>The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>dbSystem provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAnchorId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Anchor ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scanDnsName" /></td>
    <td><code>string</code></td>
    <td>The FQDN of the DNS record for the SCAN IP addresses that are associated with the DB system.</td>
</tr>
<tr>
    <td><CopyableCode code="scanIps" /></td>
    <td><code>array</code></td>
    <td>The list of Single Client Access Name (SCAN) IP addresses associated with the DB system. SCAN IP addresses are typically used for load balancing and are not assigned to any interface. Oracle Clusterware directs the requests to the appropriate nodes in the cluster. Note: For a single-node DB system, this list is empty.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the DB system. The shape determines resources to allocate to the DB system. For virtual machine shapes, the number of CPU cores and memory. For bare metal and Exadata shapes, the number of CPU cores, storage, and memory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source of the database for creating a new database. Required. for creating a new database.</td>
</tr>
<tr>
    <td><CopyableCode code="sshPublicKeys" /></td>
    <td><code>array</code></td>
    <td>The public key portion of one or more key pairs used for SSH access to the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageVolumePerformanceMode" /></td>
    <td><code>string</code></td>
    <td>The block storage volume performance level. Valid values are Balanced and HighPerformance. See `Block Volume Performance `_ for more information. Known values are: "Balanced" and "HighPerformance". (Balanced, HighPerformance)</td>
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
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The time zone of the DB system, e.g., UTC, to set the timeZone as UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The Oracle Database version of the DB system.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-db_system_name"><code>db_system_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DbSystem.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DbSystem resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DbSystem resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-db_system_name"><code>db_system_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a DbSystem.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-db_system_name"><code>db_system_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a DbSystem.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-db_system_name"><code>db_system_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a DbSystem.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-db_system_name"><code>db_system_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DbSystem.</td>
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
<tr id="parameter-db_system_name">
    <td><CopyableCode code="db_system_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DbSystem. Required.</td>
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

Get a DbSystem.

```sql
SELECT
id,
name,
adminPassword,
clusterName,
computeCount,
computeModel,
dataStorageSizeInGbs,
databaseEdition,
dbSystemOptions,
dbVersion,
diskRedundancy,
displayName,
domain,
gridImageOcid,
hostname,
initialDataStorageSizeInGb,
licenseModel,
lifecycleDetails,
lifecycleState,
listenerPort,
location,
memorySizeInGbs,
networkAnchorId,
nodeCount,
ociUrl,
ocid,
pdbName,
provisioningState,
resourceAnchorId,
scanDnsName,
scanIps,
shape,
source,
sshPublicKeys,
storageVolumePerformanceMode,
systemData,
tags,
timeZone,
type,
version,
zones
FROM azure_isv.oracledatabase.db_systems
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND db_system_name = '{{ db_system_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List DbSystem resources by resource group.

```sql
SELECT
id,
name,
adminPassword,
clusterName,
computeCount,
computeModel,
dataStorageSizeInGbs,
databaseEdition,
dbSystemOptions,
dbVersion,
diskRedundancy,
displayName,
domain,
gridImageOcid,
hostname,
initialDataStorageSizeInGb,
licenseModel,
lifecycleDetails,
lifecycleState,
listenerPort,
location,
memorySizeInGbs,
networkAnchorId,
nodeCount,
ociUrl,
ocid,
pdbName,
provisioningState,
resourceAnchorId,
scanDnsName,
scanIps,
shape,
source,
sshPublicKeys,
storageVolumePerformanceMode,
systemData,
tags,
timeZone,
type,
version,
zones
FROM azure_isv.oracledatabase.db_systems
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List DbSystem resources by subscription ID.

```sql
SELECT
id,
name,
adminPassword,
clusterName,
computeCount,
computeModel,
dataStorageSizeInGbs,
databaseEdition,
dbSystemOptions,
dbVersion,
diskRedundancy,
displayName,
domain,
gridImageOcid,
hostname,
initialDataStorageSizeInGb,
licenseModel,
lifecycleDetails,
lifecycleState,
listenerPort,
location,
memorySizeInGbs,
networkAnchorId,
nodeCount,
ociUrl,
ocid,
pdbName,
provisioningState,
resourceAnchorId,
scanDnsName,
scanIps,
shape,
source,
sshPublicKeys,
storageVolumePerformanceMode,
systemData,
tags,
timeZone,
type,
version,
zones
FROM azure_isv.oracledatabase.db_systems
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

Create a DbSystem.

```sql
INSERT INTO azure_isv.oracledatabase.db_systems (
tags,
location,
properties,
zones,
resource_group_name,
db_system_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ db_system_name }}',
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
- name: db_systems
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the db_systems resource.
    - name: db_system_name
      value: "{{ db_system_name }}"
      description: Required parameter for the db_systems resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the db_systems resource.
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
        source: "{{ source }}"
        provisioningState: "{{ provisioningState }}"
        ociUrl: "{{ ociUrl }}"
        resourceAnchorId: "{{ resourceAnchorId }}"
        networkAnchorId: "{{ networkAnchorId }}"
        clusterName: "{{ clusterName }}"
        displayName: "{{ displayName }}"
        initialDataStorageSizeInGb: {{ initialDataStorageSizeInGb }}
        dataStorageSizeInGbs: {{ dataStorageSizeInGbs }}
        dbSystemOptions:
          storageManagement: "{{ storageManagement }}"
        diskRedundancy: "{{ diskRedundancy }}"
        domain: "{{ domain }}"
        gridImageOcid: "{{ gridImageOcid }}"
        hostname: "{{ hostname }}"
        ocid: "{{ ocid }}"
        licenseModel: "{{ licenseModel }}"
        lifecycleDetails: "{{ lifecycleDetails }}"
        lifecycleState: "{{ lifecycleState }}"
        listenerPort: {{ listenerPort }}
        memorySizeInGbs: {{ memorySizeInGbs }}
        nodeCount: {{ nodeCount }}
        scanDnsName: "{{ scanDnsName }}"
        scanIps:
          - "{{ scanIps }}"
        shape: "{{ shape }}"
        sshPublicKeys:
          - "{{ sshPublicKeys }}"
        storageVolumePerformanceMode: "{{ storageVolumePerformanceMode }}"
        timeZone: "{{ timeZone }}"
        version: "{{ version }}"
        computeModel: "{{ computeModel }}"
        computeCount: {{ computeCount }}
        databaseEdition: "{{ databaseEdition }}"
        adminPassword: "{{ adminPassword }}"
        dbVersion: "{{ dbVersion }}"
        pdbName: "{{ pdbName }}"
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

Update a DbSystem.

```sql
UPDATE azure_isv.oracledatabase.db_systems
SET 
zones = '{{ zones }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND db_system_name = '{{ db_system_name }}' --required
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

Create a DbSystem.

```sql
REPLACE azure_isv.oracledatabase.db_systems
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND db_system_name = '{{ db_system_name }}' --required
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

Delete a DbSystem.

```sql
DELETE FROM azure_isv.oracledatabase.db_systems
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND db_system_name = '{{ db_system_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
