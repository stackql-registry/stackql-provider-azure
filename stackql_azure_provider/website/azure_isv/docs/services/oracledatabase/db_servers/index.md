--- 
title: db_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - db_servers
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

Creates, updates, deletes, gets or lists a <code>db_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="db_servers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracledatabase.db_servers" /></td></tr>
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
    <td><CopyableCode code="autonomousVirtualMachineIds" /></td>
    <td><code>array</code></td>
    <td>The list of OCIDs of the Autonomous Virtual Machines associated with the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousVmClusterIds" /></td>
    <td><code>array</code></td>
    <td>The list of OCIDs of the Autonomous VM Clusters associated with the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="compartmentId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the compartment.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeIds" /></td>
    <td><code>array</code></td>
    <td>The OCID of the Db nodes associated with the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The allocated local node storage in GBs on the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerPatchingDetails" /></td>
    <td><code>object</code></td>
    <td>dbServerPatching details of the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name for the Db Server.</td>
</tr>
<tr>
    <td><CopyableCode code="exadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Lifecycle details of dbServer.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>DbServer provisioning state. Known values are: "Creating", "Available", "Unavailable", "Deleting", "Deleted", and "MaintenanceInProgress". (Creating, Available, Unavailable, Deleting, Deleted, MaintenanceInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="maxCpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores available.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDbNodeStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total max dbNode storage in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory size in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Db server name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the Db server. The shape determines the amount of CPU, storage, and memory resources available.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the Db Server was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmClusterIds" /></td>
    <td><code>array</code></td>
    <td>The OCID of the VM Clusters associated with the Db server.</td>
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
    <td><CopyableCode code="autonomousVirtualMachineIds" /></td>
    <td><code>array</code></td>
    <td>The list of OCIDs of the Autonomous Virtual Machines associated with the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="autonomousVmClusterIds" /></td>
    <td><code>array</code></td>
    <td>The list of OCIDs of the Autonomous VM Clusters associated with the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="compartmentId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the compartment.</td>
</tr>
<tr>
    <td><CopyableCode code="computeModel" /></td>
    <td><code>string</code></td>
    <td>The compute model of the Exadata Infrastructure. Known values are: "ECPU" and "OCPU". (ECPU, OCPU)</td>
</tr>
<tr>
    <td><CopyableCode code="cpuCoreCount" /></td>
    <td><code>integer</code></td>
    <td>The number of CPU cores enabled on the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeIds" /></td>
    <td><code>array</code></td>
    <td>The OCID of the Db nodes associated with the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="dbNodeStorageSizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The allocated local node storage in GBs on the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="dbServerPatchingDetails" /></td>
    <td><code>object</code></td>
    <td>dbServerPatching details of the Db server.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name for the Db Server.</td>
</tr>
<tr>
    <td><CopyableCode code="exadataInfrastructureId" /></td>
    <td><code>string</code></td>
    <td>The OCID of the Exadata infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleDetails" /></td>
    <td><code>string</code></td>
    <td>Lifecycle details of dbServer.</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleState" /></td>
    <td><code>string</code></td>
    <td>DbServer provisioning state. Known values are: "Creating", "Available", "Unavailable", "Deleting", "Deleted", and "MaintenanceInProgress". (Creating, Available, Unavailable, Deleting, Deleted, MaintenanceInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="maxCpuCount" /></td>
    <td><code>integer</code></td>
    <td>The total number of CPU cores available.</td>
</tr>
<tr>
    <td><CopyableCode code="maxDbNodeStorageInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total max dbNode storage in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMemoryInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory available in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="memorySizeInGbs" /></td>
    <td><code>integer</code></td>
    <td>The total memory size in GBs.</td>
</tr>
<tr>
    <td><CopyableCode code="ocid" /></td>
    <td><code>string</code></td>
    <td>Db server name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>string</code></td>
    <td>The shape of the Db server. The shape determines the amount of CPU, storage, and memory resources available.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the Db Server was created.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmClusterIds" /></td>
    <td><code>array</code></td>
    <td>The OCID of the VM Clusters associated with the Db server.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-dbserverocid"><code>dbserverocid</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DbServer.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloudexadatainfrastructurename"><code>cloudexadatainfrastructurename</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DbServer resources by CloudExadataInfrastructure.</td>
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
<tr id="parameter-dbserverocid">
    <td><CopyableCode code="dbserverocid" /></td>
    <td><code>string</code></td>
    <td>DbServer OCID. Required.</td>
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

Get a DbServer.

```sql
SELECT
id,
name,
autonomousVirtualMachineIds,
autonomousVmClusterIds,
compartmentId,
computeModel,
cpuCoreCount,
dbNodeIds,
dbNodeStorageSizeInGbs,
dbServerPatchingDetails,
displayName,
exadataInfrastructureId,
lifecycleDetails,
lifecycleState,
maxCpuCount,
maxDbNodeStorageInGbs,
maxMemoryInGbs,
memorySizeInGbs,
ocid,
provisioningState,
shape,
systemData,
timeCreated,
type,
vmClusterIds
FROM azure_isv.oracledatabase.db_servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}' -- required
AND dbserverocid = '{{ dbserverocid }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

List DbServer resources by CloudExadataInfrastructure.

```sql
SELECT
id,
name,
autonomousVirtualMachineIds,
autonomousVmClusterIds,
compartmentId,
computeModel,
cpuCoreCount,
dbNodeIds,
dbNodeStorageSizeInGbs,
dbServerPatchingDetails,
displayName,
exadataInfrastructureId,
lifecycleDetails,
lifecycleState,
maxCpuCount,
maxDbNodeStorageInGbs,
maxMemoryInGbs,
memorySizeInGbs,
ocid,
provisioningState,
shape,
systemData,
timeCreated,
type,
vmClusterIds
FROM azure_isv.oracledatabase.db_servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
