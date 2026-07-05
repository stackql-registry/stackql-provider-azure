--- 
title: pool
hide_title: false
hide_table_of_contents: false
keywords:
  - pool
  - batch
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

Creates, updates, deletes, gets or lists a <code>pool</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pool" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.pool" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_batch_account', value: 'list_by_batch_account' }
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
    <td><CopyableCode code="allocationState" /></td>
    <td><code>string</code></td>
    <td>Whether the pool is resizing. Known values are: "Steady", "Resizing", and "Stopping". (Steady, Resizing, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="allocationStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the pool entered its current allocation state.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPackages" /></td>
    <td><code>array</code></td>
    <td>The list of application packages to be installed on each compute node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleRun" /></td>
    <td><code>object</code></td>
    <td>The results and errors from the last execution of the autoscale formula.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="currentDedicatedNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of dedicated compute nodes currently in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="currentLowPriorityNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of Spot/low-priority compute nodes currently in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentConfiguration" /></td>
    <td><code>object</code></td>
    <td>This property describes the virtual machines that the pool nodes will be deployed on.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the resource, used for concurrency statements.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The type of identity used for the Batch Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="interNodeCommunication" /></td>
    <td><code>string</code></td>
    <td>Whether the pool permits direct communication between nodes. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the pool as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="mountConfiguration" /></td>
    <td><code>array</code></td>
    <td>A list of file systems to mount on each node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the pool. Known values are: "Succeeded" and "Deleting". (Succeeded, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the pool entered its current state.</td>
</tr>
<tr>
    <td><CopyableCode code="resizeOperationStatus" /></td>
    <td><code>object</code></td>
    <td>Contains details about the current or last completed resize operation.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSettings" /></td>
    <td><code>object</code></td>
    <td>Settings which configure the number of nodes in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="startTask" /></td>
    <td><code>object</code></td>
    <td>A task specified to run on each compute node as it joins the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSchedulingPolicy" /></td>
    <td><code>object</code></td>
    <td>How tasks are distributed across compute nodes in a pool.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSlotsPerNode" /></td>
    <td><code>integer</code></td>
    <td>The number of task slots that can be used to run concurrent tasks on a single compute node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="userAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of user accounts to be created on each node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the pool. All VMs in a pool are the same size.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_batch_account">

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
    <td><CopyableCode code="allocationState" /></td>
    <td><code>string</code></td>
    <td>Whether the pool is resizing. Known values are: "Steady", "Resizing", and "Stopping". (Steady, Resizing, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="allocationStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the pool entered its current allocation state.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPackages" /></td>
    <td><code>array</code></td>
    <td>The list of application packages to be installed on each compute node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleRun" /></td>
    <td><code>object</code></td>
    <td>The results and errors from the last execution of the autoscale formula.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="currentDedicatedNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of dedicated compute nodes currently in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="currentLowPriorityNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of Spot/low-priority compute nodes currently in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentConfiguration" /></td>
    <td><code>object</code></td>
    <td>This property describes the virtual machines that the pool nodes will be deployed on.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the resource, used for concurrency statements.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The type of identity used for the Batch Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="interNodeCommunication" /></td>
    <td><code>string</code></td>
    <td>Whether the pool permits direct communication between nodes. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the pool as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="mountConfiguration" /></td>
    <td><code>array</code></td>
    <td>A list of file systems to mount on each node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the pool. Known values are: "Succeeded" and "Deleting". (Succeeded, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the pool entered its current state.</td>
</tr>
<tr>
    <td><CopyableCode code="resizeOperationStatus" /></td>
    <td><code>object</code></td>
    <td>Contains details about the current or last completed resize operation.</td>
</tr>
<tr>
    <td><CopyableCode code="scaleSettings" /></td>
    <td><code>object</code></td>
    <td>Settings which configure the number of nodes in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="startTask" /></td>
    <td><code>object</code></td>
    <td>A task specified to run on each compute node as it joins the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSchedulingPolicy" /></td>
    <td><code>object</code></td>
    <td>How tasks are distributed across compute nodes in a pool.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSlotsPerNode" /></td>
    <td><code>integer</code></td>
    <td>The number of task slots that can be used to run concurrent tasks on a single compute node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="userAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of user accounts to be created on each node in the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the pool. All VMs in a pool are the same size.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified pool.</td>
</tr>
<tr>
    <td><a href="#list_by_batch_account"><CopyableCode code="list_by_batch_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all of the pools in the specified account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new pool inside the specified account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the properties of an existing pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified pool.</td>
</tr>
<tr>
    <td><a href="#disable_auto_scale"><CopyableCode code="disable_auto_scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables automatic scaling for a pool.</td>
</tr>
<tr>
    <td><a href="#stop_resize"><CopyableCode code="stop_resize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops an ongoing resize operation on the pool. This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: `http://accountname.region.batch.azure.com/ `_. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The pool name. This must be unique within the account. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Valid properties for filtering are: name properties/allocationState properties/allocationStateTransitionTime properties/creationTime properties/provisioningState properties/provisioningStateTransitionTime properties/lastModified properties/vmSize properties/interNodeCommunication properties/scaleSettings/autoScale properties/scaleSettings/fixedScale. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of properties that should be returned. e.g. "properties/provisioningState". Only top level properties under properties/ are valid for selection. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_batch_account', value: 'list_by_batch_account' }
    ]}
>
<TabItem value="get">

Gets information about the specified pool.

```sql
SELECT
id,
name,
allocationState,
allocationStateTransitionTime,
applicationPackages,
autoScaleRun,
creationTime,
currentDedicatedNodes,
currentLowPriorityNodes,
deploymentConfiguration,
displayName,
etag,
identity,
interNodeCommunication,
lastModified,
metadata,
mountConfiguration,
networkConfiguration,
provisioningState,
provisioningStateTransitionTime,
resizeOperationStatus,
scaleSettings,
startTask,
systemData,
tags,
taskSchedulingPolicy,
taskSlotsPerNode,
type,
upgradePolicy,
userAccounts,
vmSize
FROM azure.batch.pool
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_batch_account">

Lists all of the pools in the specified account.

```sql
SELECT
id,
name,
allocationState,
allocationStateTransitionTime,
applicationPackages,
autoScaleRun,
creationTime,
currentDedicatedNodes,
currentLowPriorityNodes,
deploymentConfiguration,
displayName,
etag,
identity,
interNodeCommunication,
lastModified,
metadata,
mountConfiguration,
networkConfiguration,
provisioningState,
provisioningStateTransitionTime,
resizeOperationStatus,
scaleSettings,
startTask,
systemData,
tags,
taskSchedulingPolicy,
taskSlotsPerNode,
type,
upgradePolicy,
userAccounts,
vmSize
FROM azure.batch.pool
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND maxresults = '{{ maxresults }}'
AND $select = '{{ $select }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new pool inside the specified account.

```sql
INSERT INTO azure.batch.pool (
properties,
identity,
tags,
resource_group_name,
account_name,
pool_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: pool
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the pool resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the pool resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the pool resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the pool resource.
    - name: properties
      description: |
        The properties associated with the pool.
      value:
        displayName: "{{ displayName }}"
        lastModified: "{{ lastModified }}"
        creationTime: "{{ creationTime }}"
        provisioningState: "{{ provisioningState }}"
        provisioningStateTransitionTime: "{{ provisioningStateTransitionTime }}"
        allocationState: "{{ allocationState }}"
        allocationStateTransitionTime: "{{ allocationStateTransitionTime }}"
        vmSize: "{{ vmSize }}"
        deploymentConfiguration:
          virtualMachineConfiguration:
            imageReference:
              publisher: "{{ publisher }}"
              offer: "{{ offer }}"
              sku: "{{ sku }}"
              version: "{{ version }}"
              id: "{{ id }}"
              sharedGalleryImageId: "{{ sharedGalleryImageId }}"
              communityGalleryImageId: "{{ communityGalleryImageId }}"
            nodeAgentSkuId: "{{ nodeAgentSkuId }}"
            windowsConfiguration:
              enableAutomaticUpdates: {{ enableAutomaticUpdates }}
            dataDisks:
              - lun: {{ lun }}
                caching: "{{ caching }}"
                diskSizeGB: {{ diskSizeGB }}
                managedDisk:
                  storageAccountType: "{{ storageAccountType }}"
                  securityProfile: "{{ securityProfile }}"
                  diskEncryptionSet: "{{ diskEncryptionSet }}"
            licenseType: "{{ licenseType }}"
            containerConfiguration:
              type: "{{ type }}"
              containerImageNames:
                - "{{ containerImageNames }}"
              containerRegistries:
                - username: "{{ username }}"
                  password: "{{ password }}"
                  registryServer: "{{ registryServer }}"
                  identityReference:
                    resourceId: "{{ resourceId }}"
            diskEncryptionConfiguration:
              targets:
                - "{{ targets }}"
              customerManagedKey:
                keyUrl: "{{ keyUrl }}"
                rotationToLatestKeyVersionEnabled: {{ rotationToLatestKeyVersionEnabled }}
                identityReference: "{{ identityReference }}"
            nodePlacementConfiguration:
              policy: "{{ policy }}"
            extensions:
              - name: "{{ name }}"
                publisher: "{{ publisher }}"
                type: "{{ type }}"
                typeHandlerVersion: "{{ typeHandlerVersion }}"
                autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
                enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
                settings: "{{ settings }}"
                protectedSettings: "{{ protectedSettings }}"
                provisionAfterExtensions: "{{ provisionAfterExtensions }}"
            osDisk:
              ephemeralOSDiskSettings:
                placement: "{{ placement }}"
              caching: "{{ caching }}"
              managedDisk:
                storageAccountType: "{{ storageAccountType }}"
                securityProfile: "{{ securityProfile }}"
                diskEncryptionSet: "{{ diskEncryptionSet }}"
              diskSizeGB: {{ diskSizeGB }}
              writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
            securityProfile:
              securityType: "{{ securityType }}"
              encryptionAtHost: {{ encryptionAtHost }}
              uefiSettings:
                secureBootEnabled: {{ secureBootEnabled }}
                vTpmEnabled: {{ vTpmEnabled }}
              proxyAgentSettings:
                enabled: {{ enabled }}
                imds: "{{ imds }}"
                wireServer: "{{ wireServer }}"
            serviceArtifactReference:
              id: "{{ id }}"
        currentDedicatedNodes: {{ currentDedicatedNodes }}
        currentLowPriorityNodes: {{ currentLowPriorityNodes }}
        scaleSettings:
          fixedScale:
            resizeTimeout: "{{ resizeTimeout }}"
            targetDedicatedNodes: {{ targetDedicatedNodes }}
            targetLowPriorityNodes: {{ targetLowPriorityNodes }}
            nodeDeallocationOption: "{{ nodeDeallocationOption }}"
          autoScale:
            formula: "{{ formula }}"
            evaluationInterval: "{{ evaluationInterval }}"
        autoScaleRun:
          evaluationTime: "{{ evaluationTime }}"
          results: "{{ results }}"
          error:
            code: "{{ code }}"
            message: "{{ message }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                details: "{{ details }}"
        interNodeCommunication: "{{ interNodeCommunication }}"
        networkConfiguration:
          subnetId: "{{ subnetId }}"
          dynamicVnetAssignmentScope: "{{ dynamicVnetAssignmentScope }}"
          endpointConfiguration:
            inboundNatPools:
              - name: "{{ name }}"
                protocol: "{{ protocol }}"
                backendPort: {{ backendPort }}
                frontendPortRangeStart: {{ frontendPortRangeStart }}
                frontendPortRangeEnd: {{ frontendPortRangeEnd }}
                networkSecurityGroupRules: "{{ networkSecurityGroupRules }}"
          publicIPAddressConfiguration:
            provision: "{{ provision }}"
            ipAddressIds:
              - "{{ ipAddressIds }}"
            ipFamilies:
              - "{{ ipFamilies }}"
            ipTags:
              - ipTagType: "{{ ipTagType }}"
                tag: "{{ tag }}"
          enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
        taskSlotsPerNode: {{ taskSlotsPerNode }}
        taskSchedulingPolicy:
          jobDefaultOrder: "{{ jobDefaultOrder }}"
          nodeFillType: "{{ nodeFillType }}"
        userAccounts:
          - name: "{{ name }}"
            password: "{{ password }}"
            elevationLevel: "{{ elevationLevel }}"
            linuxUserConfiguration:
              uid: {{ uid }}
              gid: {{ gid }}
              sshPrivateKey: "{{ sshPrivateKey }}"
            windowsUserConfiguration:
              loginMode: "{{ loginMode }}"
        metadata:
          - name: "{{ name }}"
            value: "{{ value }}"
        startTask:
          commandLine: "{{ commandLine }}"
          resourceFiles:
            - autoStorageContainerName: "{{ autoStorageContainerName }}"
              storageContainerUrl: "{{ storageContainerUrl }}"
              httpUrl: "{{ httpUrl }}"
              blobPrefix: "{{ blobPrefix }}"
              filePath: "{{ filePath }}"
              fileMode: "{{ fileMode }}"
              identityReference:
                resourceId: "{{ resourceId }}"
          environmentSettings:
            - name: "{{ name }}"
              value: "{{ value }}"
          userIdentity:
            userName: "{{ userName }}"
            autoUser:
              scope: "{{ scope }}"
              elevationLevel: "{{ elevationLevel }}"
          maxTaskRetryCount: {{ maxTaskRetryCount }}
          waitForSuccess: {{ waitForSuccess }}
          containerSettings:
            containerRunOptions: "{{ containerRunOptions }}"
            imageName: "{{ imageName }}"
            registry:
              username: "{{ username }}"
              password: "{{ password }}"
              registryServer: "{{ registryServer }}"
              identityReference:
                resourceId: "{{ resourceId }}"
            workingDirectory: "{{ workingDirectory }}"
            containerHostBatchBindMounts:
              - source: "{{ source }}"
                isReadOnly: {{ isReadOnly }}
        applicationPackages:
          - id: "{{ id }}"
            version: "{{ version }}"
        resizeOperationStatus:
          targetDedicatedNodes: {{ targetDedicatedNodes }}
          targetLowPriorityNodes: {{ targetLowPriorityNodes }}
          resizeTimeout: "{{ resizeTimeout }}"
          nodeDeallocationOption: "{{ nodeDeallocationOption }}"
          startTime: "{{ startTime }}"
          errors:
            - code: "{{ code }}"
              message: "{{ message }}"
              details: "{{ details }}"
        mountConfiguration:
          - azureBlobFileSystemConfiguration:
              accountName: "{{ accountName }}"
              containerName: "{{ containerName }}"
              accountKey: "{{ accountKey }}"
              sasKey: "{{ sasKey }}"
              blobfuseOptions: "{{ blobfuseOptions }}"
              relativeMountPath: "{{ relativeMountPath }}"
              identityReference:
                resourceId: "{{ resourceId }}"
            nfsMountConfiguration:
              source: "{{ source }}"
              relativeMountPath: "{{ relativeMountPath }}"
              mountOptions: "{{ mountOptions }}"
            cifsMountConfiguration:
              userName: "{{ userName }}"
              source: "{{ source }}"
              relativeMountPath: "{{ relativeMountPath }}"
              mountOptions: "{{ mountOptions }}"
              password: "{{ password }}"
            azureFileShareConfiguration:
              accountName: "{{ accountName }}"
              azureFileUrl: "{{ azureFileUrl }}"
              accountKey: "{{ accountKey }}"
              relativeMountPath: "{{ relativeMountPath }}"
              mountOptions: "{{ mountOptions }}"
        upgradePolicy:
          mode: "{{ mode }}"
          automaticOSUpgradePolicy:
            disableAutomaticRollback: {{ disableAutomaticRollback }}
            enableAutomaticOSUpgrade: {{ enableAutomaticOSUpgrade }}
            useRollingUpgradePolicy: {{ useRollingUpgradePolicy }}
            osRollingUpgradeDeferral: {{ osRollingUpgradeDeferral }}
          rollingUpgradePolicy:
            enableCrossZoneUpgrade: {{ enableCrossZoneUpgrade }}
            maxBatchInstancePercent: {{ maxBatchInstancePercent }}
            maxUnhealthyInstancePercent: {{ maxUnhealthyInstancePercent }}
            maxUnhealthyUpgradedInstancePercent: {{ maxUnhealthyUpgradedInstancePercent }}
            pauseTimeBetweenBatches: "{{ pauseTimeBetweenBatches }}"
            prioritizeUnhealthyInstances: {{ prioritizeUnhealthyInstances }}
            rollbackFailedInstancesOnPolicyBreach: {{ rollbackFailedInstancesOnPolicyBreach }}
    - name: identity
      description: |
        The type of identity used for the Batch Pool.
      value:
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the resource.
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

Updates the properties of an existing pool.

```sql
UPDATE azure.batch.pool
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
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

Deletes the specified pool.

```sql
DELETE FROM azure.batch.pool
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disable_auto_scale"
    values={[
        { label: 'disable_auto_scale', value: 'disable_auto_scale' },
        { label: 'stop_resize', value: 'stop_resize' }
    ]}
>
<TabItem value="disable_auto_scale">

Disables automatic scaling for a pool.

```sql
EXEC azure.batch.pool.disable_auto_scale 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_resize">

Stops an ongoing resize operation on the pool. This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created.

```sql
EXEC azure.batch.pool.stop_resize 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
