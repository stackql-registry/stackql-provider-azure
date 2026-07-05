--- 
title: horizon_db_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - horizon_db_clusters
  - horizondb
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

Creates, updates, deletes, gets or lists a <code>horizon_db_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="horizon_db_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.horizondb.horizon_db_clusters" /></td></tr>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>The administrator login name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a new HorizonDb cluster. Known values are: "Create", "Update", and "PointInTimeRestore". (Create, Update, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>The network related info.</td>
</tr>
<tr>
    <td><CopyableCode code="parameterGroup" /></td>
    <td><code>object</code></td>
    <td>Defines connection to a parameter group.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Restore point creation time specifying the time to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="poolName" /></td>
    <td><code>string</code></td>
    <td>The pool name for restore or replica operations.</td>
</tr>
<tr>
    <td><CopyableCode code="processorType" /></td>
    <td><code>string</code></td>
    <td>The processor type for the HorizonDb cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Provisioning". (Succeeded, Failed, Canceled, InProgress, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="readonlyEndpoint" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name used for readonly endpoint for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCount" /></td>
    <td><code>integer</code></td>
    <td>Number of replicas.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceClusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The source cluster resource ID for restore or replica creation.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the cluster. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", "Updating", and "Healthy". (Ready, Dropping, Disabled, Starting, Stopping, Stopped, Updating, Healthy)</td>
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
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>Number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the HorizonDb cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="zonePlacementPolicy" /></td>
    <td><code>string</code></td>
    <td>Defines how replicas are placed across availability zones. Known values are: "Strict" and "BestEffort". (Strict, BestEffort)</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>The administrator login name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a new HorizonDb cluster. Known values are: "Create", "Update", and "PointInTimeRestore". (Create, Update, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>The network related info.</td>
</tr>
<tr>
    <td><CopyableCode code="parameterGroup" /></td>
    <td><code>object</code></td>
    <td>Defines connection to a parameter group.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Restore point creation time specifying the time to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="poolName" /></td>
    <td><code>string</code></td>
    <td>The pool name for restore or replica operations.</td>
</tr>
<tr>
    <td><CopyableCode code="processorType" /></td>
    <td><code>string</code></td>
    <td>The processor type for the HorizonDb cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Provisioning". (Succeeded, Failed, Canceled, InProgress, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="readonlyEndpoint" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name used for readonly endpoint for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCount" /></td>
    <td><code>integer</code></td>
    <td>Number of replicas.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceClusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The source cluster resource ID for restore or replica creation.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the cluster. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", "Updating", and "Healthy". (Ready, Dropping, Disabled, Starting, Stopping, Stopped, Updating, Healthy)</td>
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
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>Number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the HorizonDb cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="zonePlacementPolicy" /></td>
    <td><code>string</code></td>
    <td>Defines how replicas are placed across availability zones. Known values are: "Strict" and "BestEffort". (Strict, BestEffort)</td>
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
    <td><CopyableCode code="administratorLogin" /></td>
    <td><code>string</code></td>
    <td>The administrator login name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="administratorLoginPassword" /></td>
    <td><code>string</code></td>
    <td>The administrator login password.</td>
</tr>
<tr>
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>The mode to create a new HorizonDb cluster. Known values are: "Create", "Update", and "PointInTimeRestore". (Create, Update, PointInTimeRestore)</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>The network related info.</td>
</tr>
<tr>
    <td><CopyableCode code="parameterGroup" /></td>
    <td><code>object</code></td>
    <td>Defines connection to a parameter group.</td>
</tr>
<tr>
    <td><CopyableCode code="pointInTimeUTC" /></td>
    <td><code>string (date-time)</code></td>
    <td>Restore point creation time specifying the time to restore from.</td>
</tr>
<tr>
    <td><CopyableCode code="poolName" /></td>
    <td><code>string</code></td>
    <td>The pool name for restore or replica operations.</td>
</tr>
<tr>
    <td><CopyableCode code="processorType" /></td>
    <td><code>string</code></td>
    <td>The processor type for the HorizonDb cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Provisioning". (Succeeded, Failed, Canceled, InProgress, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="readonlyEndpoint" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name used for readonly endpoint for the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="replicaCount" /></td>
    <td><code>integer</code></td>
    <td>Number of replicas.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceClusterResourceId" /></td>
    <td><code>string</code></td>
    <td>The source cluster resource ID for restore or replica creation.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the cluster. Known values are: "Ready", "Dropping", "Disabled", "Starting", "Stopping", "Stopped", "Updating", and "Healthy". (Ready, Dropping, Disabled, Starting, Stopping, Stopped, Updating, Healthy)</td>
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
    <td><CopyableCode code="vCores" /></td>
    <td><code>integer</code></td>
    <td>Number of vCores.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the HorizonDb cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="zonePlacementPolicy" /></td>
    <td><code>string</code></td>
    <td>Defines how replicas are placed across availability zones. Known values are: "Strict" and "BestEffort". (Strict, BestEffort)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a HorizonDb cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all HorizonDb clusters in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all HorizonDb clusters in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new HorizonDb cluster or updates an existing cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing HorizonDb cluster (e.g., tags, virtual cores, replica count).</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new HorizonDb cluster or updates an existing cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a HorizonDb cluster.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the HorizonDb cluster. Required.</td>
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

Gets information about a HorizonDb cluster.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
createMode,
fullyQualifiedDomainName,
location,
network,
parameterGroup,
pointInTimeUTC,
poolName,
processorType,
provisioningState,
readonlyEndpoint,
replicaCount,
sourceClusterResourceId,
state,
systemData,
tags,
type,
vCores,
version,
zonePlacementPolicy
FROM azure.horizondb.horizon_db_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all HorizonDb clusters in a resource group.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
createMode,
fullyQualifiedDomainName,
location,
network,
parameterGroup,
pointInTimeUTC,
poolName,
processorType,
provisioningState,
readonlyEndpoint,
replicaCount,
sourceClusterResourceId,
state,
systemData,
tags,
type,
vCores,
version,
zonePlacementPolicy
FROM azure.horizondb.horizon_db_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all HorizonDb clusters in a subscription.

```sql
SELECT
id,
name,
administratorLogin,
administratorLoginPassword,
createMode,
fullyQualifiedDomainName,
location,
network,
parameterGroup,
pointInTimeUTC,
poolName,
processorType,
provisioningState,
readonlyEndpoint,
replicaCount,
sourceClusterResourceId,
state,
systemData,
tags,
type,
vCores,
version,
zonePlacementPolicy
FROM azure.horizondb.horizon_db_clusters
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

Creates a new HorizonDb cluster or updates an existing cluster.

```sql
INSERT INTO azure.horizondb.horizon_db_clusters (
tags,
location,
properties,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
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
- name: horizon_db_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the horizon_db_clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the horizon_db_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the horizon_db_clusters resource.
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
        administratorLogin: "{{ administratorLogin }}"
        administratorLoginPassword: "{{ administratorLoginPassword }}"
        version: "{{ version }}"
        createMode: "{{ createMode }}"
        pointInTimeUTC: "{{ pointInTimeUTC }}"
        sourceClusterResourceId: "{{ sourceClusterResourceId }}"
        poolName: "{{ poolName }}"
        replicaCount: {{ replicaCount }}
        vCores: {{ vCores }}
        processorType: "{{ processorType }}"
        network:
          publicNetworkAccess: "{{ publicNetworkAccess }}"
        state: "{{ state }}"
        fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
        readonlyEndpoint: "{{ readonlyEndpoint }}"
        provisioningState: "{{ provisioningState }}"
        zonePlacementPolicy: "{{ zonePlacementPolicy }}"
        parameterGroup:
          id: "{{ id }}"
          syncStatus: "{{ syncStatus }}"
          applyImmediately: {{ applyImmediately }}
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

Updates an existing HorizonDb cluster (e.g., tags, virtual cores, replica count).

```sql
UPDATE azure.horizondb.horizon_db_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
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

Creates a new HorizonDb cluster or updates an existing cluster.

```sql
REPLACE azure.horizondb.horizon_db_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
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

Deletes a HorizonDb cluster.

```sql
DELETE FROM azure.horizondb.horizon_db_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
