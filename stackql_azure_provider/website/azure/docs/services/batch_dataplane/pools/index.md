--- 
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - batch_dataplane
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_pool"
    values={[
        { label: 'get_pool', value: 'get_pool' },
        { label: 'list_pools', value: 'list_pools' }
    ]}
>
<TabItem value="get_pool">

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
    <td>A string that uniquely identifies the Pool within the Account. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="allocationState" /></td>
    <td><code>string</code></td>
    <td>Whether the Pool is resizing. Known values are: "steady", "resizing", and "stopping". (steady, resizing, stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="allocationStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Pool entered its current allocation state.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPackageReferences" /></td>
    <td><code>array</code></td>
    <td>The list of Packages to be installed on each Compute Node in the Pool. Changes to Package references affect all new Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. There is a maximum of 10 Package references on any given Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleEvaluationInterval" /></td>
    <td><code>string</code></td>
    <td>The time interval at which to automatically adjust the Pool size according to the autoscale formula. This property is set only if the Pool automatically scales, i.e. enableAutoScale is true. The time duration is specified in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleFormula" /></td>
    <td><code>string</code></td>
    <td>A formula for the desired number of Compute Nodes in the Pool. This property is set only if the Pool automatically scales, i.e. enableAutoScale is true.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleRun" /></td>
    <td><code>object</code></td>
    <td>The results and errors from the last execution of the autoscale formula. This property is set only if the Pool automatically scales, i.e. enableAutoScale is true.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="currentDedicatedNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of dedicated Compute Nodes currently in the Pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="currentLowPriorityNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of Spot/Low-priority Compute Nodes currently in the Pool. Spot/Low-priority Compute Nodes which have been preempted are included in this count. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Pool. This is an opaque string. You can use it to detect whether the Pool has changed between requests. In particular, you can be pass the ETag when updating a Pool to specify that your changes should take effect only if nobody else has modified the Pool in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoScale" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Pool size should automatically adjust over time. If false, at least one of targetDedicatedNodes and targetLowPriorityNodes must be specified. If true, the autoScaleFormula property is required and the Pool automatically resizes according to the formula. The default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInterNodeCommunication" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Pool permits direct communication between Compute Nodes. Enabling inter-node communication limits the maximum size of the Pool due to deployment restrictions on the Compute Nodes of the Pool. This may result in the Pool not reaching its desired size. The default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Batch pool, if configured. The list of user identities associated with the Batch pool. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identityName&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Pool. This is the last time at which the Pool level data, such as the targetDedicatedNodes or enableAutoscale settings, changed. It does not factor in node-level changes such as a Compute Node changing state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the Pool as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="mountConfiguration" /></td>
    <td><code>array</code></td>
    <td>Mount storage using specified file system for the entire lifetime of the pool. Mount the storage using Azure fileshare, NFS, CIFS or Blobfuse based file system.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration for the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="resizeErrors" /></td>
    <td><code>array</code></td>
    <td>A list of errors encountered while performing the last resize on the Pool. This property is set only if one or more errors occurred during the last Pool resize, and only when the Pool allocationState is Steady.</td>
</tr>
<tr>
    <td><CopyableCode code="resizeTimeout" /></td>
    <td><code>string</code></td>
    <td>The timeout for allocation of Compute Nodes to the Pool. This is the timeout for the most recent resize operation. (The initial sizing when the Pool is created counts as a resize.) The default value is 15 minutes. The time duration is specified in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="startTask" /></td>
    <td><code>object</code></td>
    <td>A Task specified to run on each Compute Node as it joins the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Pool. Required. Known values are: "active" and "deleting". (active, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Pool entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>Utilization and resource usage statistics for the entire lifetime of the Pool. This property is populated only if the BatchPool was retrieved with an expand clause including the 'stats' attribute; otherwise it is null. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDedicatedNodes" /></td>
    <td><code>integer</code></td>
    <td>The desired number of dedicated Compute Nodes in the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="targetLowPriorityNodes" /></td>
    <td><code>integer</code></td>
    <td>The desired number of Spot/Low-priority Compute Nodes in the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSchedulingPolicy" /></td>
    <td><code>object</code></td>
    <td>How Tasks are distributed across Compute Nodes in a Pool. If not specified, the default is spread.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSlotsPerNode" /></td>
    <td><code>integer</code></td>
    <td>The number of task slots that can be used to run concurrent tasks on a single compute node in the pool. The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the pool or 256.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy for the Pool. Describes an upgrade policy - automatic, manual, or rolling.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of user Accounts to be created on each Compute Node in the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineConfiguration" /></td>
    <td><code>object</code></td>
    <td>The virtual machine configuration for the Pool. This property must be specified.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the Pool. All virtual machines in a Pool are the same size. For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (`https://learn.microsoft.com/azure/batch/batch-pool-vm-sizes `_). Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_pools">

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
    <td>A string that uniquely identifies the Pool within the Account. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="allocationState" /></td>
    <td><code>string</code></td>
    <td>Whether the Pool is resizing. Known values are: "steady", "resizing", and "stopping". (steady, resizing, stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="allocationStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Pool entered its current allocation state.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationPackageReferences" /></td>
    <td><code>array</code></td>
    <td>The list of Packages to be installed on each Compute Node in the Pool. Changes to Package references affect all new Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. There is a maximum of 10 Package references on any given Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleEvaluationInterval" /></td>
    <td><code>string</code></td>
    <td>The time interval at which to automatically adjust the Pool size according to the autoscale formula. This property is set only if the Pool automatically scales, i.e. enableAutoScale is true. The time duration is specified in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleFormula" /></td>
    <td><code>string</code></td>
    <td>A formula for the desired number of Compute Nodes in the Pool. This property is set only if the Pool automatically scales, i.e. enableAutoScale is true.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleRun" /></td>
    <td><code>object</code></td>
    <td>The results and errors from the last execution of the autoscale formula. This property is set only if the Pool automatically scales, i.e. enableAutoScale is true.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="currentDedicatedNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of dedicated Compute Nodes currently in the Pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="currentLowPriorityNodes" /></td>
    <td><code>integer</code></td>
    <td>The number of Spot/Low-priority Compute Nodes currently in the Pool. Spot/Low-priority Compute Nodes which have been preempted are included in this count. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Pool. This is an opaque string. You can use it to detect whether the Pool has changed between requests. In particular, you can be pass the ETag when updating a Pool to specify that your changes should take effect only if nobody else has modified the Pool in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutoScale" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Pool size should automatically adjust over time. If false, at least one of targetDedicatedNodes and targetLowPriorityNodes must be specified. If true, the autoScaleFormula property is required and the Pool automatically resizes according to the formula. The default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="enableInterNodeCommunication" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Pool permits direct communication between Compute Nodes. Enabling inter-node communication limits the maximum size of the Pool due to deployment restrictions on the Compute Nodes of the Pool. This may result in the Pool not reaching its desired size. The default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the Batch pool, if configured. The list of user identities associated with the Batch pool. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&#123;identityName&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Pool. This is the last time at which the Pool level data, such as the targetDedicatedNodes or enableAutoscale settings, changed. It does not factor in node-level changes such as a Compute Node changing state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the Pool as metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="mountConfiguration" /></td>
    <td><code>array</code></td>
    <td>Mount storage using specified file system for the entire lifetime of the pool. Mount the storage using Azure fileshare, NFS, CIFS or Blobfuse based file system.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration for the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="resizeErrors" /></td>
    <td><code>array</code></td>
    <td>A list of errors encountered while performing the last resize on the Pool. This property is set only if one or more errors occurred during the last Pool resize, and only when the Pool allocationState is Steady.</td>
</tr>
<tr>
    <td><CopyableCode code="resizeTimeout" /></td>
    <td><code>string</code></td>
    <td>The timeout for allocation of Compute Nodes to the Pool. This is the timeout for the most recent resize operation. (The initial sizing when the Pool is created counts as a resize.) The default value is 15 minutes. The time duration is specified in ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="startTask" /></td>
    <td><code>object</code></td>
    <td>A Task specified to run on each Compute Node as it joins the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Pool. Required. Known values are: "active" and "deleting". (active, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Pool entered its current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>Utilization and resource usage statistics for the entire lifetime of the Pool. This property is populated only if the BatchPool was retrieved with an expand clause including the 'stats' attribute; otherwise it is null. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDedicatedNodes" /></td>
    <td><code>integer</code></td>
    <td>The desired number of dedicated Compute Nodes in the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="targetLowPriorityNodes" /></td>
    <td><code>integer</code></td>
    <td>The desired number of Spot/Low-priority Compute Nodes in the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSchedulingPolicy" /></td>
    <td><code>object</code></td>
    <td>How Tasks are distributed across Compute Nodes in a Pool. If not specified, the default is spread.</td>
</tr>
<tr>
    <td><CopyableCode code="taskSlotsPerNode" /></td>
    <td><code>integer</code></td>
    <td>The number of task slots that can be used to run concurrent tasks on a single compute node in the pool. The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the pool or 256.</td>
</tr>
<tr>
    <td><CopyableCode code="upgradePolicy" /></td>
    <td><code>object</code></td>
    <td>The upgrade policy for the Pool. Describes an upgrade policy - automatic, manual, or rolling.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Pool. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userAccounts" /></td>
    <td><code>array</code></td>
    <td>The list of user Accounts to be created on each Compute Node in the Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineConfiguration" /></td>
    <td><code>object</code></td>
    <td>The virtual machine configuration for the Pool. This property must be specified.</td>
</tr>
<tr>
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of virtual machines in the Pool. All virtual machines in a Pool are the same size. For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (`https://learn.microsoft.com/azure/batch/batch-pool-vm-sizes `_). Required.</td>
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
    <td><a href="#get_pool"><CopyableCode code="get_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets information about the specified Pool.</td>
</tr>
<tr>
    <td><a href="#list_pools"><CopyableCode code="list_pools" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the Pools in the specified Account. Lists all of the Pools in the specified Account.</td>
</tr>
<tr>
    <td><a href="#create_pool"><CopyableCode code="create_pool" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-vmSize"><code>vmSize</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Creates a Pool to the specified Account. When naming Pools, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.</td>
</tr>
<tr>
    <td><a href="#update_pool"><CopyableCode code="update_pool" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Updates the properties of the specified Pool. This only replaces the Pool properties specified in the request. For example, if the Pool has a StartTask associated with it, and a request does not specify a StartTask element, then the Pool keeps the existing StartTask.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool to get. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>An OData $expand clause. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-pools `_. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>An OData $select clause. Default value is None.</td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td>A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. Default value is None.</td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td>A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. A maximum of 1000 applications can be returned. Default value is None.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_pool"
    values={[
        { label: 'get_pool', value: 'get_pool' },
        { label: 'list_pools', value: 'list_pools' }
    ]}
>
<TabItem value="get_pool">

Gets information about the specified Pool.

```sql
SELECT
id,
allocationState,
allocationStateTransitionTime,
applicationPackageReferences,
autoScaleEvaluationInterval,
autoScaleFormula,
autoScaleRun,
creationTime,
currentDedicatedNodes,
currentLowPriorityNodes,
displayName,
eTag,
enableAutoScale,
enableInterNodeCommunication,
identity,
lastModified,
metadata,
mountConfiguration,
networkConfiguration,
resizeErrors,
resizeTimeout,
startTask,
state,
stateTransitionTime,
stats,
targetDedicatedNodes,
targetLowPriorityNodes,
taskSchedulingPolicy,
taskSlotsPerNode,
upgradePolicy,
url,
userAccounts,
virtualMachineConfiguration,
vmSize
FROM azure.batch_dataplane.pools
WHERE pool_id = '{{ pool_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_pools">

Lists all of the Pools in the specified Account. Lists all of the Pools in the specified Account.

```sql
SELECT
id,
allocationState,
allocationStateTransitionTime,
applicationPackageReferences,
autoScaleEvaluationInterval,
autoScaleFormula,
autoScaleRun,
creationTime,
currentDedicatedNodes,
currentLowPriorityNodes,
displayName,
eTag,
enableAutoScale,
enableInterNodeCommunication,
identity,
lastModified,
metadata,
mountConfiguration,
networkConfiguration,
resizeErrors,
resizeTimeout,
startTask,
state,
stateTransitionTime,
stats,
targetDedicatedNodes,
targetLowPriorityNodes,
taskSchedulingPolicy,
taskSlotsPerNode,
upgradePolicy,
url,
userAccounts,
virtualMachineConfiguration,
vmSize
FROM azure.batch_dataplane.pools
WHERE endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_pool"
    values={[
        { label: 'create_pool', value: 'create_pool' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_pool">

Creates a Pool to the specified Account. When naming Pools, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

```sql
INSERT INTO azure.batch_dataplane.pools (
id,
displayName,
vmSize,
virtualMachineConfiguration,
resizeTimeout,
targetDedicatedNodes,
targetLowPriorityNodes,
enableAutoScale,
autoScaleFormula,
autoScaleEvaluationInterval,
enableInterNodeCommunication,
networkConfiguration,
startTask,
applicationPackageReferences,
taskSlotsPerNode,
taskSchedulingPolicy,
userAccounts,
metadata,
mountConfiguration,
upgradePolicy,
endpoint,
timeOut,
ocp-date
)
SELECT 
'{{ id }}' /* required */,
'{{ displayName }}',
'{{ vmSize }}' /* required */,
'{{ virtualMachineConfiguration }}',
'{{ resizeTimeout }}',
{{ targetDedicatedNodes }},
{{ targetLowPriorityNodes }},
{{ enableAutoScale }},
'{{ autoScaleFormula }}',
'{{ autoScaleEvaluationInterval }}',
{{ enableInterNodeCommunication }},
'{{ networkConfiguration }}',
'{{ startTask }}',
'{{ applicationPackageReferences }}',
{{ taskSlotsPerNode }},
'{{ taskSchedulingPolicy }}',
'{{ userAccounts }}',
'{{ metadata }}',
'{{ mountConfiguration }}',
'{{ upgradePolicy }}',
'{{ endpoint }}',
'{{ timeOut }}',
'{{ ocp-date }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: pools
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the pools resource.
    - name: id
      value: "{{ id }}"
      description: |
        A string that uniquely identifies the Pool within the Account. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two Pool IDs within an Account that differ only by case). Required.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the Pool. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.
    - name: vmSize
      value: "{{ vmSize }}"
      description: |
        The size of virtual machines in the Pool. All virtual machines in a Pool are the same size. For information about available VM sizes for Pools using Images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration), see Sizes for Virtual Machines in Azure (\`https://learn.microsoft.com/azure/virtual-machines/sizes/overview \`_). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). Required.
    - name: virtualMachineConfiguration
      description: |
        The virtual machine configuration for the Pool. This property must be specified.
      value:
        imageReference:
          publisher: "{{ publisher }}"
          offer: "{{ offer }}"
          sku: "{{ sku }}"
          version: "{{ version }}"
          virtualMachineImageId: "{{ virtualMachineImageId }}"
          exactVersion: "{{ exactVersion }}"
          sharedGalleryImageId: "{{ sharedGalleryImageId }}"
          communityGalleryImageId: "{{ communityGalleryImageId }}"
        nodeAgentSKUId: "{{ nodeAgentSKUId }}"
        windowsConfiguration:
          enableAutomaticUpdates: {{ enableAutomaticUpdates }}
        dataDisks:
          - lun: {{ lun }}
            caching: "{{ caching }}"
            diskSizeGB: {{ diskSizeGB }}
            managedDisk:
              diskEncryptionSet:
                id: "{{ id }}"
              storageAccountType: "{{ storageAccountType }}"
              securityProfile:
                securityEncryptionType: "{{ securityEncryptionType }}"
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
          customerManagedKey:
            identityReference:
              resourceId: "{{ resourceId }}"
            keyUrl: "{{ keyUrl }}"
            rotationToLatestKeyVersionEnabled: {{ rotationToLatestKeyVersionEnabled }}
          targets:
            - "{{ targets }}"
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
          diskSizeGB: {{ diskSizeGB }}
          managedDisk:
            diskEncryptionSet:
              id: "{{ id }}"
            storageAccountType: "{{ storageAccountType }}"
            securityProfile:
              securityEncryptionType: "{{ securityEncryptionType }}"
          writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
        securityProfile:
          encryptionAtHost: {{ encryptionAtHost }}
          proxyAgentSettings:
            enabled: {{ enabled }}
            imds:
              inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
              mode: "{{ mode }}"
            wireServer:
              inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
              mode: "{{ mode }}"
          securityType: "{{ securityType }}"
          uefiSettings:
            secureBootEnabled: {{ secureBootEnabled }}
            vTpmEnabled: {{ vTpmEnabled }}
        serviceArtifactReference:
          id: "{{ id }}"
    - name: resizeTimeout
      value: "{{ resizeTimeout }}"
      description: |
        The timeout for allocation of Compute Nodes to the Pool. This timeout applies only to manual scaling; it has no effect when enableAutoScale is set to true. The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). The time duration is specified in ISO 8601 format.
    - name: targetDedicatedNodes
      value: {{ targetDedicatedNodes }}
      description: |
        The desired number of dedicated Compute Nodes in the Pool. This property must not be specified if enableAutoScale is set to true. If enableAutoScale is set to false, then you must set either targetDedicatedNodes, targetLowPriorityNodes, or both.
    - name: targetLowPriorityNodes
      value: {{ targetLowPriorityNodes }}
      description: |
        The desired number of Spot/Low-priority Compute Nodes in the Pool. This property must not be specified if enableAutoScale is set to true. If enableAutoScale is set to false, then you must set either targetDedicatedNodes, targetLowPriorityNodes, or both.
    - name: enableAutoScale
      value: {{ enableAutoScale }}
      description: |
        Whether the Pool size should automatically adjust over time. If false, at least one of targetDedicatedNodes and targetLowPriorityNodes must be specified. If true, the autoScaleFormula property is required and the Pool automatically resizes according to the formula. The default value is false.
    - name: autoScaleFormula
      value: "{{ autoScaleFormula }}"
      description: |
        A formula for the desired number of Compute Nodes in the Pool. This property must not be specified if enableAutoScale is set to false. It is required if enableAutoScale is set to true. The formula is checked for validity before the Pool is created. If the formula is not valid, the Batch service rejects the request with detailed error information. For more information about specifying this formula, see 'Automatically scale Compute Nodes in an Azure Batch Pool' (\`https://learn.microsoft.com/azure/batch/batch-automatic-scaling \`_).
    - name: autoScaleEvaluationInterval
      value: "{{ autoScaleEvaluationInterval }}"
      description: |
        The time interval at which to automatically adjust the Pool size according to the autoscale formula. The default value is 15 minutes. The minimum and maximum value are 5 minutes and 168 hours respectively. If you specify a value less than 5 minutes or greater than 168 hours, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). The time duration is specified in ISO 8601 format.
    - name: enableInterNodeCommunication
      value: {{ enableInterNodeCommunication }}
      description: |
        Whether the Pool permits direct communication between Compute Nodes. Enabling inter-node communication limits the maximum size of the Pool due to deployment restrictions on the Compute Nodes of the Pool. This may result in the Pool not reaching its desired size. The default value is false.
    - name: networkConfiguration
      description: |
        The network configuration for the Pool.
      value:
        subnetId: "{{ subnetId }}"
        dynamicVNetAssignmentScope: "{{ dynamicVNetAssignmentScope }}"
        endpointConfiguration:
          inboundNATPools:
            - name: "{{ name }}"
              protocol: "{{ protocol }}"
              backendPort: {{ backendPort }}
              frontendPortRangeStart: {{ frontendPortRangeStart }}
              frontendPortRangeEnd: {{ frontendPortRangeEnd }}
              networkSecurityGroupRules: "{{ networkSecurityGroupRules }}"
        publicIPAddressConfiguration:
          provision: "{{ provision }}"
          ipFamilies:
            - "{{ ipFamilies }}"
          ipAddressIds:
            - "{{ ipAddressIds }}"
          ipTags:
            - ipTagType: "{{ ipTagType }}"
              tag: "{{ tag }}"
        enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
    - name: startTask
      description: |
        A Task specified to run on each Compute Node as it joins the Pool. The Task runs when the Compute Node is added to the Pool or when the Compute Node is restarted.
      value:
        commandLine: "{{ commandLine }}"
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
          username: "{{ username }}"
          autoUser:
            scope: "{{ scope }}"
            elevationLevel: "{{ elevationLevel }}"
        maxTaskRetryCount: {{ maxTaskRetryCount }}
        waitForSuccess: {{ waitForSuccess }}
    - name: applicationPackageReferences
      description: |
        The list of Packages to be installed on each Compute Node in the Pool. When creating a pool, the package's application ID must be fully qualified (/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationName}). Changes to Package references affect all new Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. There is a maximum of 10 Package references on any given Pool.
      value:
        - applicationId: "{{ applicationId }}"
          version: "{{ version }}"
    - name: taskSlotsPerNode
      value: {{ taskSlotsPerNode }}
      description: |
        The number of task slots that can be used to run concurrent tasks on a single compute node in the pool. The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the pool or 256.
    - name: taskSchedulingPolicy
      description: |
        How Tasks are distributed across Compute Nodes in a Pool. If not specified, the default is spread.
      value:
        jobDefaultOrder: "{{ jobDefaultOrder }}"
        nodeFillType: "{{ nodeFillType }}"
    - name: userAccounts
      description: |
        The list of user Accounts to be created on each Compute Node in the Pool.
      value:
        - name: "{{ name }}"
          password: "{{ password }}"
          elevationLevel: "{{ elevationLevel }}"
          linuxUserConfiguration:
            uid: {{ uid }}
            gid: {{ gid }}
            sshPrivateKey: "{{ sshPrivateKey }}"
          windowsUserConfiguration:
            loginMode: "{{ loginMode }}"
    - name: metadata
      description: |
        A list of name-value pairs associated with the Pool as metadata. The Batch service does not assign any meaning to metadata; it is solely for the use of user code.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
    - name: mountConfiguration
      description: |
        Mount storage using specified file system for the entire lifetime of the pool. Mount the storage using Azure fileshare, NFS, CIFS or Blobfuse based file system.
      value:
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
            username: "{{ username }}"
            source: "{{ source }}"
            relativeMountPath: "{{ relativeMountPath }}"
            mountOptions: "{{ mountOptions }}"
            password: "{{ password }}"
          azureFileShareConfiguration:
            accountName: "{{ accountName }}"
            accountKey: "{{ accountKey }}"
            azureFileUrl: "{{ azureFileUrl }}"
            relativeMountPath: "{{ relativeMountPath }}"
            mountOptions: "{{ mountOptions }}"
    - name: upgradePolicy
      description: |
        The upgrade policy for the Pool. Describes an upgrade policy - automatic, manual, or rolling.
      value:
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
    - name: timeOut
      value: {{ timeOut }}
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
    - name: ocp-date
      value: "{{ ocp-date }}"
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_pool"
    values={[
        { label: 'update_pool', value: 'update_pool' }
    ]}
>
<TabItem value="update_pool">

Updates the properties of the specified Pool. This only replaces the Pool properties specified in the request. For example, if the Pool has a StartTask associated with it, and a request does not specify a StartTask element, then the Pool keeps the existing StartTask.

```sql
UPDATE azure.batch_dataplane.pools
SET 
displayName = '{{ displayName }}',
vmSize = '{{ vmSize }}',
enableInterNodeCommunication = {{ enableInterNodeCommunication }},
startTask = '{{ startTask }}',
applicationPackageReferences = '{{ applicationPackageReferences }}',
metadata = '{{ metadata }}',
virtualMachineConfiguration = '{{ virtualMachineConfiguration }}',
taskSlotsPerNode = {{ taskSlotsPerNode }},
taskSchedulingPolicy = '{{ taskSchedulingPolicy }}',
networkConfiguration = '{{ networkConfiguration }}',
userAccounts = '{{ userAccounts }}',
mountConfiguration = '{{ mountConfiguration }}',
upgradePolicy = '{{ upgradePolicy }}'
WHERE 
pool_id = '{{ pool_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut}}'
AND ocp-date = '{{ ocp-date}}'
AND If-Modified-Since = '{{ If-Modified-Since}}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since}}';
```
</TabItem>
</Tabs>
