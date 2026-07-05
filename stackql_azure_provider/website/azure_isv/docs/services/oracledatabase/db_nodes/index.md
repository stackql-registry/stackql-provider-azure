--- 
title: db_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_nodes
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

Creates, updates, deletes, gets or lists a <code>db_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="db_nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.db_nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
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
    <td><CopyableCode code="additionalDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the planned maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="backupIpId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the backup IP address associated with the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="backupVnic2Id" /></td>
    <td><code>string</code></td>
    <td>The OCID of the second backup VNIC.</td>
</tr>
<tr>
    <td><CopyableCode code="backupVnicId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the backup VNIC.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the Db node.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The allocated local node storage in GBs on the Db node.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exacc Db server associated with the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="dbSystemId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="faultDomain" /></td>
    <td><code>string</code></td>
    <td>The name of the Fault Domain the instance is contained in.</td>
</tr>
<tr>
    <td><CopyableCode code="hostIpId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the host IP address associated with the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The host name for the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Lifecycle details of Db Node.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the database node. Required. Known values are: "Provisioning", "Available", "Updating", "Stopping", "Stopped", "Starting", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Updating, Stopping, Stopped, Starting, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceType" /></td>
    <td><code>string</code></td>
    <td>The type of database node maintenance. "VmdbRebootMigration" (VmdbRebootMigration)</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The allocated memory in GBs on the Db node.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>DbNode OCID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="softwareStorageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the database node was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceWindowEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date and time of maintenance window.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceWindowStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date and time of maintenance window.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vnic2Id" /></td>
    <td><code>string</code></td>
    <td>The OCID of the second VNIC.</td>
</tr>
<tr>
    <td><CopyableCode code="vnicId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the VNIC. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_parent">

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
    <td><CopyableCode code="additionalDetails" /></td>
    <td><code>string</code></td>
    <td>Additional information about the planned maintenance.</td>
</tr>
<tr>
    <td><CopyableCode code="backupIpId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the backup IP address associated with the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="backupVnic2Id" /></td>
    <td><code>string</code></td>
    <td>The OCID of the second backup VNIC.</td>
</tr>
<tr>
    <td><CopyableCode code="backupVnicId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the backup VNIC.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the Db node.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The allocated local node storage in GBs on the Db node.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exacc Db server associated with the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="dbSystemId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the DB system. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="faultDomain" /></td>
    <td><code>string</code></td>
    <td>The name of the Fault Domain the instance is contained in.</td>
</tr>
<tr>
    <td><CopyableCode code="hostIpId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the host IP address associated with the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The host name for the database node.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Lifecycle details of Db Node.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>The current state of the database node. Required. Known values are: "Provisioning", "Available", "Updating", "Stopping", "Stopped", "Starting", "Terminating", "Terminated", and "Failed". (Provisioning, Available, Updating, Stopping, Stopped, Starting, Terminating, Terminated, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceType" /></td>
    <td><code>string</code></td>
    <td>The type of database node maintenance. "VmdbRebootMigration" (VmdbRebootMigration)</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The allocated memory in GBs on the Db node.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>DbNode OCID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="softwareStorageSizeInGb" /></td>
    <td><code>integer</code></td>
    <td>The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the database node was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceWindowEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>End date and time of maintenance window.</td>
</tr>
<tr>
    <td><CopyableCode code="timeMaintenanceWindowStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start date and time of maintenance window.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vnic2Id" /></td>
    <td><code>string</code></td>
    <td>The OCID of the second VNIC.</td>
</tr>
<tr>
    <td><CopyableCode code="vnicId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the VNIC. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-dbnodeocid"><code>dbnodeocid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DbNode.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DbNode resources by CloudVmCluster.</td>
</tr>
<tr>
    <td><a href="#action"><CopyableCode code="action" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudvmclustername"><code>cloudvmclustername</code></a>, <a href="#parameter-dbnodeocid"><code>dbnodeocid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>VM actions on DbNode of VM Cluster by the provided filter.</td>
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
<tr id="parameter-dbnodeocid">
    <td><CopyableCode code="dbnodeocid" /></td>
    <td><code>string</code></td>
    <td>DbNode OCID. Required.</td>
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
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="get">

Get a DbNode.

```sql
SELECT
id,
name,
additionalDetails,
backupIpId,
backupVnic2Id,
backupVnicId,
cpuCoreCount,
dbNodeStorageSizeInGbs,
dbServerId,
dbSystemId,
faultDomain,
hostIpId,
hostname,
lifecycleDetails,
lifecycleState,
maintenanceType,
memorySizeInGbs,
ocid,
provisioningState,
softwareStorageSizeInGb,
systemData,
timeCreated,
timeMaintenanceWindowEnd,
timeMaintenanceWindowStart,
type,
vnic2Id,
vnicId
FROM azure_isv.oracledatabase.db_nodes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudvmclustername = '{{ cloudvmclustername }}' -- required
AND dbnodeocid = '{{ dbnodeocid }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List DbNode resources by CloudVmCluster.

```sql
SELECT
id,
name,
additionalDetails,
backupIpId,
backupVnic2Id,
backupVnicId,
cpuCoreCount,
dbNodeStorageSizeInGbs,
dbServerId,
dbSystemId,
faultDomain,
hostIpId,
hostname,
lifecycleDetails,
lifecycleState,
maintenanceType,
memorySizeInGbs,
ocid,
provisioningState,
softwareStorageSizeInGb,
systemData,
timeCreated,
timeMaintenanceWindowEnd,
timeMaintenanceWindowStart,
type,
vnic2Id,
vnicId
FROM azure_isv.oracledatabase.db_nodes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudvmclustername = '{{ cloudvmclustername }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="action"
    values={[
        { label: 'action', value: 'action' }
    ]}
>
<TabItem value="action">

VM actions on DbNode of VM Cluster by the provided filter.

```sql
EXEC azure_isv.oracledatabase.db_nodes.action 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloudvmclustername='{{ cloudvmclustername }}' --required, 
@dbnodeocid='{{ dbnodeocid }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"action": "{{ action }}"
}'
;
```
</TabItem>
</Tabs>
