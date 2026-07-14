--- 
title: cloud_exadata_infrastructures
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_exadata_infrastructures
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

Creates, updates, deletes, gets or lists a <code>cloud_exadata_infrastructures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_exadata_infrastructures" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle_database.cloud_exadata_infrastructures" /></td></tr>
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
    <td><CopyableCode code="activatedStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The requested number of additional storage servers activated for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The requested number of additional storage servers for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="availableStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of compute servers for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores allocated.</td>
</tr>
<tr>
    <td><CopyableCode code="customerContacts" /></td>
    <td><code>array</code></td>
    <td>The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource. Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators. Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The quantity of data in the database, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseServerType" /></td>
    <td><code>string</code></td>
    <td>The database server model type of the cloud Exadata infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The local node storage to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerVersion" /></td>
    <td><code>string</code></td>
    <td>The software version of the database servers (dom0) in the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="definedFileSystemConfiguration" /></td>
    <td><code>array</code></td>
    <td>Defined file system configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name for the Exadata infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedPatchingTime" /></td>
    <td><code>object</code></td>
    <td>The estimated total time required in minutes for all patching operations (database server, storage server, and network switch patching).</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleConfig" /></td>
    <td><code>object</code></td>
    <td>The exascale config details for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMaintenanceRunId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the last maintenance run.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "MaintenanceInProgress", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, MaintenanceInProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>maintenanceWindow property.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores available.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDataStorageInTbs" /></td>
    <td><code>number</code></td>
    <td>The total available DATA disk group size.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total local node storage available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyDbServerVersion" /></td>
    <td><code>string</code></td>
    <td>Monthly Db Server version.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyStorageServerVersion" /></td>
    <td><code>string</code></td>
    <td>Monthly Storage Server version.</td>
</tr>
<tr>
    <td><CopyableCode code="nextMaintenanceRunId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the next maintenance run.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Exadata infra ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The model name of the cloud Exadata infrastructure resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageCount" /></td>
    <td><code>integer</code></td>
    <td>The number of storage servers for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="storageServerType" /></td>
    <td><code>string</code></td>
    <td>The storage server model type of the cloud Exadata infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageServerVersion" /></td>
    <td><code>string</code></td>
    <td>The software version of the storage servers (cells) in the Exadata infrastructure.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string</code></td>
    <td>The date and time the cloud Exadata infrastructure resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>CloudExadataInfrastructure zones. Required.</td>
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
    <td><CopyableCode code="activatedStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The requested number of additional storage servers activated for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The requested number of additional storage servers for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="availableStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of compute servers for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores allocated.</td>
</tr>
<tr>
    <td><CopyableCode code="customerContacts" /></td>
    <td><code>array</code></td>
    <td>The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource. Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators. Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The quantity of data in the database, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseServerType" /></td>
    <td><code>string</code></td>
    <td>The database server model type of the cloud Exadata infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The local node storage to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerVersion" /></td>
    <td><code>string</code></td>
    <td>The software version of the database servers (dom0) in the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="definedFileSystemConfiguration" /></td>
    <td><code>array</code></td>
    <td>Defined file system configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name for the Exadata infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedPatchingTime" /></td>
    <td><code>object</code></td>
    <td>The estimated total time required in minutes for all patching operations (database server, storage server, and network switch patching).</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleConfig" /></td>
    <td><code>object</code></td>
    <td>The exascale config details for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMaintenanceRunId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the last maintenance run.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "MaintenanceInProgress", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, MaintenanceInProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>maintenanceWindow property.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores available.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDataStorageInTbs" /></td>
    <td><code>number</code></td>
    <td>The total available DATA disk group size.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total local node storage available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyDbServerVersion" /></td>
    <td><code>string</code></td>
    <td>Monthly Db Server version.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyStorageServerVersion" /></td>
    <td><code>string</code></td>
    <td>Monthly Storage Server version.</td>
</tr>
<tr>
    <td><CopyableCode code="nextMaintenanceRunId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the next maintenance run.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Exadata infra ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The model name of the cloud Exadata infrastructure resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageCount" /></td>
    <td><code>integer</code></td>
    <td>The number of storage servers for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="storageServerType" /></td>
    <td><code>string</code></td>
    <td>The storage server model type of the cloud Exadata infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageServerVersion" /></td>
    <td><code>string</code></td>
    <td>The software version of the storage servers (cells) in the Exadata infrastructure.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string</code></td>
    <td>The date and time the cloud Exadata infrastructure resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>CloudExadataInfrastructure zones. Required.</td>
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
    <td><CopyableCode code="activatedStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The requested number of additional storage servers activated for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalStorageCount" /></td>
    <td><code>integer</code></td>
    <td>The requested number of additional storage servers for the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="availableStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).</td>
</tr>
<tr>
    <td><CopyableCode code="computeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of compute servers for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores allocated.</td>
</tr>
<tr>
    <td><CopyableCode code="customerContacts" /></td>
    <td><code>array</code></td>
    <td>The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource. Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators. Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.</td>
</tr>
<tr>
    <td><CopyableCode code="dataStorageSizeInTbs" /></td>
    <td><code>number</code></td>
    <td>The quantity of data in the database, in terabytes.</td>
</tr>
<tr>
    <td><CopyableCode code="databaseServerType" /></td>
    <td><code>string</code></td>
    <td>The database server model type of the cloud Exadata infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The local node storage to be allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerVersion" /></td>
    <td><code>string</code></td>
    <td>The software version of the database servers (dom0) in the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="definedFileSystemConfiguration" /></td>
    <td><code>array</code></td>
    <td>Defined file system configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name for the Exadata infrastructure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedPatchingTime" /></td>
    <td><code>object</code></td>
    <td>The estimated total time required in minutes for all patching operations (database server, storage server, and network switch patching).</td>
</tr>
<tr>
    <td><CopyableCode code="exascaleConfig" /></td>
    <td><code>object</code></td>
    <td>The exascale config details for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMaintenanceRunId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the last maintenance run.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the current lifecycle state.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure lifecycle state. Known values are: "Provisioning", "Available", "Updating", "Terminating", "Terminated", "MaintenanceInProgress", and "Failed". (Provisioning, Available, Updating, Terminating, Terminated, MaintenanceInProgress, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceWindow" /></td>
    <td><code>object</code></td>
    <td>maintenanceWindow property.</td>
</tr>
<tr>
    <td><CopyableCode code="maxCpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores available.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDataStorageInTbs" /></td>
    <td><code>number</code></td>
    <td>The total available DATA disk group size.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total local node storage available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The memory allocated in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyDbServerVersion" /></td>
    <td><code>string</code></td>
    <td>Monthly Db Server version.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyStorageServerVersion" /></td>
    <td><code>string</code></td>
    <td>Monthly Storage Server version.</td>
</tr>
<tr>
    <td><CopyableCode code="nextMaintenanceRunId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the next maintenance run.</td>
</tr>
<tr>
    <td><CopyableCode code="ociUrl" /></td>
    <td><code>string</code></td>
    <td>HTTPS link to OCI resources exposed to Azure Customer via Azure Interface.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Exadata infra ocid.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure provisioning state. Known values are: "Succeeded", "Failed", "Canceled", and "Provisioning". (Succeeded, Failed, Canceled, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The model name of the cloud Exadata infrastructure resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="storageCount" /></td>
    <td><code>integer</code></td>
    <td>The number of storage servers for the cloud Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="storageServerType" /></td>
    <td><code>string</code></td>
    <td>The storage server model type of the cloud Exadata infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageServerVersion" /></td>
    <td><code>string</code></td>
    <td>The software version of the storage servers (cells) in the Exadata infrastructure.</td>
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
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string</code></td>
    <td>The date and time the cloud Exadata infrastructure resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>CloudExadataInfrastructure zones. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a CloudExadataInfrastructure.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List CloudExadataInfrastructure resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List CloudExadataInfrastructure resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-zones"><code>zones</code></a></td>
    <td></td>
    <td>Create a CloudExadataInfrastructure.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a CloudExadataInfrastructure.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-zones"><code>zones</code></a></td>
    <td></td>
    <td>Create a CloudExadataInfrastructure.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a CloudExadataInfrastructure.</td>
</tr>
<tr>
    <td><a href="#add_storage_capacity"><CopyableCode code="add_storage_capacity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Perform add storage capacity on exadata infra.</td>
</tr>
<tr>
    <td><a href="#configure_exascale"><CopyableCode code="configure_exascale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-totalStorageInGbs"><code>totalStorageInGbs</code></a></td>
    <td></td>
    <td>Configures Exascale on Cloud exadata infrastructure resource.</td>
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
<tr id="parameter-cloudexadatainfrastructurename">
    <td><CopyableCode code="cloudexadatainfrastructurename" /></td>
    <td><code>string</code></td>
    <td>CloudExadataInfrastructure name. Required.</td>
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

Get a CloudExadataInfrastructure.

```sql
SELECT
id,
name,
activatedStorageCount,
additionalStorageCount,
availableStorageSizeInGbs,
computeCount,
computeModel,
cpuCount,
customerContacts,
dataStorageSizeInTbs,
databaseServerType,
dbNodeStorageSizeInGbs,
dbServerVersion,
definedFileSystemConfiguration,
displayName,
estimatedPatchingTime,
exascaleConfig,
lastMaintenanceRunId,
lifecycleDetails,
lifecycleState,
location,
maintenanceWindow,
maxCpuCount,
maxDataStorageInTbs,
maxDbNodeStorageSizeInGbs,
maxMemoryInGbs,
memorySizeInGbs,
monthlyDbServerVersion,
monthlyStorageServerVersion,
nextMaintenanceRunId,
ociUrl,
ocid,
provisioningState,
shape,
storageCount,
storageServerType,
storageServerVersion,
systemData,
tags,
timeCreated,
totalStorageSizeInGbs,
type,
zones
FROM azure_isv.oracle_database.cloud_exadata_infrastructures
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List CloudExadataInfrastructure resources by resource group.

```sql
SELECT
id,
name,
activatedStorageCount,
additionalStorageCount,
availableStorageSizeInGbs,
computeCount,
computeModel,
cpuCount,
customerContacts,
dataStorageSizeInTbs,
databaseServerType,
dbNodeStorageSizeInGbs,
dbServerVersion,
definedFileSystemConfiguration,
displayName,
estimatedPatchingTime,
exascaleConfig,
lastMaintenanceRunId,
lifecycleDetails,
lifecycleState,
location,
maintenanceWindow,
maxCpuCount,
maxDataStorageInTbs,
maxDbNodeStorageSizeInGbs,
maxMemoryInGbs,
memorySizeInGbs,
monthlyDbServerVersion,
monthlyStorageServerVersion,
nextMaintenanceRunId,
ociUrl,
ocid,
provisioningState,
shape,
storageCount,
storageServerType,
storageServerVersion,
systemData,
tags,
timeCreated,
totalStorageSizeInGbs,
type,
zones
FROM azure_isv.oracle_database.cloud_exadata_infrastructures
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List CloudExadataInfrastructure resources by subscription ID.

```sql
SELECT
id,
name,
activatedStorageCount,
additionalStorageCount,
availableStorageSizeInGbs,
computeCount,
computeModel,
cpuCount,
customerContacts,
dataStorageSizeInTbs,
databaseServerType,
dbNodeStorageSizeInGbs,
dbServerVersion,
definedFileSystemConfiguration,
displayName,
estimatedPatchingTime,
exascaleConfig,
lastMaintenanceRunId,
lifecycleDetails,
lifecycleState,
location,
maintenanceWindow,
maxCpuCount,
maxDataStorageInTbs,
maxDbNodeStorageSizeInGbs,
maxMemoryInGbs,
memorySizeInGbs,
monthlyDbServerVersion,
monthlyStorageServerVersion,
nextMaintenanceRunId,
ociUrl,
ocid,
provisioningState,
shape,
storageCount,
storageServerType,
storageServerVersion,
systemData,
tags,
timeCreated,
totalStorageSizeInGbs,
type,
zones
FROM azure_isv.oracle_database.cloud_exadata_infrastructures
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

Create a CloudExadataInfrastructure.

```sql
INSERT INTO azure_isv.oracle_database.cloud_exadata_infrastructures (
tags,
location,
properties,
zones,
resource_group_name,
cloudexadatainfrastructurename,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ zones }}' /* required */,
'{{ resource_group_name }}',
'{{ cloudexadatainfrastructurename }}',
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
- name: cloud_exadata_infrastructures
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cloud_exadata_infrastructures resource.
    - name: cloudexadatainfrastructurename
      value: "{{ cloudexadatainfrastructurename }}"
      description: Required parameter for the cloud_exadata_infrastructures resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cloud_exadata_infrastructures resource.
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
        definedFileSystemConfiguration:
          - isBackupPartition: {{ isBackupPartition }}
            isResizable: {{ isResizable }}
            minSizeGb: {{ minSizeGb }}
            mountPoint: "{{ mountPoint }}"
        ocid: "{{ ocid }}"
        computeCount: {{ computeCount }}
        storageCount: {{ storageCount }}
        totalStorageSizeInGbs: {{ totalStorageSizeInGbs }}
        availableStorageSizeInGbs: {{ availableStorageSizeInGbs }}
        timeCreated: "{{ timeCreated }}"
        lifecycleDetails: "{{ lifecycleDetails }}"
        maintenanceWindow:
          preference: "{{ preference }}"
          months:
            - name: "{{ name }}"
          weeksOfMonth:
            - {{ weeksOfMonth }}
          daysOfWeek:
            - name: "{{ name }}"
          hoursOfDay:
            - {{ hoursOfDay }}
          leadTimeInWeeks: {{ leadTimeInWeeks }}
          patchingMode: "{{ patchingMode }}"
          customActionTimeoutInMins: {{ customActionTimeoutInMins }}
          isCustomActionTimeoutEnabled: {{ isCustomActionTimeoutEnabled }}
          isMonthlyPatchingEnabled: {{ isMonthlyPatchingEnabled }}
        estimatedPatchingTime:
          estimatedDbServerPatchingTime: {{ estimatedDbServerPatchingTime }}
          estimatedNetworkSwitchesPatchingTime: {{ estimatedNetworkSwitchesPatchingTime }}
          estimatedStorageServerPatchingTime: {{ estimatedStorageServerPatchingTime }}
          totalEstimatedPatchingTime: {{ totalEstimatedPatchingTime }}
        customerContacts:
          - email: "{{ email }}"
        provisioningState: "{{ provisioningState }}"
        lifecycleState: "{{ lifecycleState }}"
        shape: "{{ shape }}"
        ociUrl: "{{ ociUrl }}"
        cpuCount: {{ cpuCount }}
        maxCpuCount: {{ maxCpuCount }}
        memorySizeInGbs: {{ memorySizeInGbs }}
        maxMemoryInGbs: {{ maxMemoryInGbs }}
        dbNodeStorageSizeInGbs: {{ dbNodeStorageSizeInGbs }}
        maxDbNodeStorageSizeInGbs: {{ maxDbNodeStorageSizeInGbs }}
        dataStorageSizeInTbs: {{ dataStorageSizeInTbs }}
        maxDataStorageInTbs: {{ maxDataStorageInTbs }}
        dbServerVersion: "{{ dbServerVersion }}"
        storageServerVersion: "{{ storageServerVersion }}"
        activatedStorageCount: {{ activatedStorageCount }}
        additionalStorageCount: {{ additionalStorageCount }}
        displayName: "{{ displayName }}"
        lastMaintenanceRunId: "{{ lastMaintenanceRunId }}"
        nextMaintenanceRunId: "{{ nextMaintenanceRunId }}"
        monthlyDbServerVersion: "{{ monthlyDbServerVersion }}"
        monthlyStorageServerVersion: "{{ monthlyStorageServerVersion }}"
        databaseServerType: "{{ databaseServerType }}"
        storageServerType: "{{ storageServerType }}"
        computeModel: "{{ computeModel }}"
        exascaleConfig:
          totalStorageInGbs: {{ totalStorageInGbs }}
          availableStorageInGbs: {{ availableStorageInGbs }}
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        CloudExadataInfrastructure zones. Required.
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

Update a CloudExadataInfrastructure.

```sql
UPDATE azure_isv.oracle_database.cloud_exadata_infrastructures
SET 
zones = '{{ zones }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}' --required
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

Create a CloudExadataInfrastructure.

```sql
REPLACE azure_isv.oracle_database.cloud_exadata_infrastructures
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND zones = '{{ zones }}' --required
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

Delete a CloudExadataInfrastructure.

```sql
DELETE FROM azure_isv.oracle_database.cloud_exadata_infrastructures
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_storage_capacity"
    values={[
        { label: 'add_storage_capacity', value: 'add_storage_capacity' },
        { label: 'configure_exascale', value: 'configure_exascale' }
    ]}
>
<TabItem value="add_storage_capacity">

Perform add storage capacity on exadata infra.

```sql
EXEC azure_isv.oracle_database.cloud_exadata_infrastructures.add_storage_capacity 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloudexadatainfrastructurename='{{ cloudexadatainfrastructurename }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="configure_exascale">

Configures Exascale on Cloud exadata infrastructure resource.

```sql
EXEC azure_isv.oracle_database.cloud_exadata_infrastructures.configure_exascale 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloudexadatainfrastructurename='{{ cloudexadatainfrastructurename }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"totalStorageInGbs": {{ totalStorageInGbs }}
}'
;
```
</TabItem>
</Tabs>
