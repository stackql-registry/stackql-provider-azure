--- 
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - mongocluster
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

Creates, updates, deletes, gets or lists a <code>replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replicas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mongocluster.replicas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_parent"
    values={[
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
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
    <td><CopyableCode code="administrator" /></td>
    <td><code>object</code></td>
    <td>The local administrator properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="authConfig" /></td>
    <td><code>object</code></td>
    <td>The authentication configuration for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="backup" /></td>
    <td><code>object</code></td>
    <td>The backup properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the mongo cluster. Known values are: "Ready", "Provisioning", "Updating", "Starting", "Stopping", "Stopped", and "Dropping". (Ready, Provisioning, Updating, Starting, Stopping, Stopped, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="compute" /></td>
    <td><code>object</code></td>
    <td>The compute properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionString" /></td>
    <td><code>string</code></td>
    <td>The default mongo connection string for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a mongo cluster. Known values are: "Default", "PointInTimeRestore", "GeoReplica", and "Replica". (Default, PointInTimeRestore, GeoReplica, Replica)</td>
</tr>
<tr>
    <td><CopyableCode code="dataApi" /></td>
    <td><code>object</code></td>
    <td>The Data API properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption configuration for the cluster. Depends on identity being configured.</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailability" /></td>
    <td><code>object</code></td>
    <td>The high availability properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureVersion" /></td>
    <td><code>string</code></td>
    <td>The infrastructure version the cluster is provisioned on.</td>
</tr>
<tr>
    <td><CopyableCode code="networkBypassMode" /></td>
    <td><code>string</code></td>
    <td>The network bypass mode for the cluster. Setting to 'AzureCosmosDB' allows Azure Cosmos DB service to bypass network restrictions. Known values are: "None" and "AzureCosmosDB". (None, AzureCosmosDB)</td>
</tr>
<tr>
    <td><CopyableCode code="previewFeatures" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the mongo cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", "Updating", and "Dropping". (Succeeded, Failed, Canceled, InProgress, Updating, Dropping)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public endpoint access is allowed for this mongo cluster. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="replica" /></td>
    <td><code>object</code></td>
    <td>The replication properties for the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a replica mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="restoreParameters" /></td>
    <td><code>object</code></td>
    <td>The parameters to create a point-in-time restore mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The Mongo DB server version. Defaults to the latest available version if not specified.</td>
</tr>
<tr>
    <td><CopyableCode code="sharding" /></td>
    <td><code>object</code></td>
    <td>The sharding properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storage" /></td>
    <td><code>object</code></td>
    <td>The storage properties of the mongo cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-mongo_cluster_name"><code>mongo_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the replicas for the mongo cluster.</td>
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
<tr id="parameter-mongo_cluster_name">
    <td><CopyableCode code="mongo_cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the mongo cluster. Required.</td>
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
    defaultValue="list_by_parent"
    values={[
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="list_by_parent">

List all the replicas for the mongo cluster.

```sql
SELECT
id,
name,
administrator,
authConfig,
backup,
clusterStatus,
compute,
connectionString,
createMode,
dataApi,
encryption,
highAvailability,
infrastructureVersion,
networkBypassMode,
previewFeatures,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
replica,
replicaParameters,
restoreParameters,
serverVersion,
sharding,
storage,
systemData,
type
FROM azure.mongocluster.replicas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND mongo_cluster_name = '{{ mongo_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
