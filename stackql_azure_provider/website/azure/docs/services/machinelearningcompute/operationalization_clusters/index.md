--- 
title: operationalization_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - operationalization_clusters
  - machinelearningcompute
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

Creates, updates, deletes, gets or lists an <code>operationalization_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operationalization_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machinelearningcompute.operationalization_clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appInsights" /></td>
    <td><code>object</code></td>
    <td>AppInsights configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>The cluster type. Known values are: "ACS" and "Local".</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>object</code></td>
    <td>Container Registry properties.</td>
</tr>
<tr>
    <td><CopyableCode code="containerService" /></td>
    <td><code>object</code></td>
    <td>Parameters for the Azure Container Service cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="globalServiceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Contains global configuration for the web services in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the cluster was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningErrors" /></td>
    <td><code>array</code></td>
    <td>List of provisioning errors reported by the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. Known values are: "Unknown", "Updating", "Creating", "Deleting", "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccount" /></td>
    <td><code>object</code></td>
    <td>Storage Account properties.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appInsights" /></td>
    <td><code>object</code></td>
    <td>AppInsights configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>The cluster type. Known values are: "ACS" and "Local".</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>object</code></td>
    <td>Container Registry properties.</td>
</tr>
<tr>
    <td><CopyableCode code="containerService" /></td>
    <td><code>object</code></td>
    <td>Parameters for the Azure Container Service cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="globalServiceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Contains global configuration for the web services in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the cluster was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningErrors" /></td>
    <td><code>array</code></td>
    <td>List of provisioning errors reported by the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. Known values are: "Unknown", "Updating", "Creating", "Deleting", "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccount" /></td>
    <td><code>object</code></td>
    <td>Storage Account properties.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription_id">

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
    <td>Specifies the resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appInsights" /></td>
    <td><code>object</code></td>
    <td>AppInsights configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>The cluster type. Known values are: "ACS" and "Local".</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>object</code></td>
    <td>Container Registry properties.</td>
</tr>
<tr>
    <td><CopyableCode code="containerService" /></td>
    <td><code>object</code></td>
    <td>Parameters for the Azure Container Service cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="globalServiceConfiguration" /></td>
    <td><code>object</code></td>
    <td>Contains global configuration for the web services in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the cluster was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningErrors" /></td>
    <td><code>array</code></td>
    <td>List of provisioning errors reported by the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. Known values are: "Unknown", "Updating", "Creating", "Deleting", "Succeeded", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccount" /></td>
    <td><code>object</code></td>
    <td>Storage Account properties.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains resource tags defined as key/value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the resource.</td>
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
    <td>Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Gets the clusters in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription_id"><CopyableCode code="list_by_subscription_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Gets the operationalization clusters in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an operationalization cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an operationalization cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteAll"><code>deleteAll</code></a></td>
    <td>Deletes the specified cluster.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the credentials for the specified cluster such as Storage, ACR and ACS credentials. This is a long running operation because it fetches keys from dependencies.</td>
</tr>
<tr>
    <td><a href="#check_system_services_updates_available"><CopyableCode code="check_system_services_updates_available" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks if updates are available for system services in the cluster.</td>
</tr>
<tr>
    <td><a href="#update_system_services"><CopyableCode code="update_system_services" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates system services in a cluster.</td>
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
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group in which the cluster is located. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Continuation token for pagination. Default value is None.</td>
</tr>
<tr id="parameter-deleteAll">
    <td><CopyableCode code="deleteAll" /></td>
    <td><code>boolean</code></td>
    <td>If true, deletes all resources associated with this cluster. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription_id', value: 'list_by_subscription_id' }
    ]}
>
<TabItem value="get">

Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them.

```sql
SELECT
id,
name,
appInsights,
clusterType,
containerRegistry,
containerService,
createdOn,
description,
globalServiceConfiguration,
location,
modifiedOn,
provisioningErrors,
provisioningState,
storageAccount,
tags,
type
FROM azure.machinelearningcompute.operationalization_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets the clusters in the specified resource group.

```sql
SELECT
id,
name,
appInsights,
clusterType,
containerRegistry,
containerService,
createdOn,
description,
globalServiceConfiguration,
location,
modifiedOn,
provisioningErrors,
provisioningState,
storageAccount,
tags,
type
FROM azure.machinelearningcompute.operationalization_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
<TabItem value="list_by_subscription_id">

Gets the operationalization clusters in the specified subscription.

```sql
SELECT
id,
name,
appInsights,
clusterType,
containerRegistry,
containerService,
createdOn,
description,
globalServiceConfiguration,
location,
modifiedOn,
provisioningErrors,
provisioningState,
storageAccount,
tags,
type
FROM azure.machinelearningcompute.operationalization_clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
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

Create or update an operationalization cluster.

```sql
INSERT INTO azure.machinelearningcompute.operationalization_clusters (
location,
tags,
properties,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: operationalization_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the operationalization_clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the operationalization_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the operationalization_clusters resource.
    - name: location
      value: "{{ location }}"
      description: |
        Specifies the location of the resource. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Contains resource tags defined as key/value pairs.
    - name: properties
      value:
        description: "{{ description }}"
        clusterType: "{{ clusterType }}"
        storageAccount:
          resourceId: "{{ resourceId }}"
        containerRegistry:
          resourceId: "{{ resourceId }}"
        containerService:
          clusterFqdn: "{{ clusterFqdn }}"
          orchestratorType: "{{ orchestratorType }}"
          orchestratorProperties:
            servicePrincipal:
              clientId: "{{ clientId }}"
              secret: "{{ secret }}"
          systemServices:
            - systemServiceType: "{{ systemServiceType }}"
              publicIpAddress: "{{ publicIpAddress }}"
              version: "{{ version }}"
          masterCount: {{ masterCount }}
          agentCount: {{ agentCount }}
          agentVmSize: "{{ agentVmSize }}"
        appInsights:
          resourceId: "{{ resourceId }}"
        globalServiceConfiguration:
          : "{{  }}"
          etag: "{{ etag }}"
          ssl:
            status: "{{ status }}"
            cert: "{{ cert }}"
            key: "{{ key }}"
            cname: "{{ cname }}"
          serviceAuth:
            primaryAuthKeyHash: "{{ primaryAuthKeyHash }}"
            secondaryAuthKeyHash: "{{ secondaryAuthKeyHash }}"
          autoScale:
            status: "{{ status }}"
            minReplicas: {{ minReplicas }}
            maxReplicas: {{ maxReplicas }}
            targetUtilization: {{ targetUtilization }}
            refreshPeriodInSeconds: {{ refreshPeriodInSeconds }}
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

The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties.

```sql
UPDATE azure.machinelearningcompute.operationalization_clusters
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Create or update an operationalization cluster.

```sql
REPLACE azure.machinelearningcompute.operationalization_clusters
SET 
location = '{{ location }}',
tags = '{{ tags }}',
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

Deletes the specified cluster.

```sql
DELETE FROM azure.machinelearningcompute.operationalization_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteAll = '{{ deleteAll }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'check_system_services_updates_available', value: 'check_system_services_updates_available' },
        { label: 'update_system_services', value: 'update_system_services' }
    ]}
>
<TabItem value="list_keys">

Gets the credentials for the specified cluster such as Storage, ACR and ACS credentials. This is a long running operation because it fetches keys from dependencies.

```sql
EXEC azure.machinelearningcompute.operationalization_clusters.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_system_services_updates_available">

Checks if updates are available for system services in the cluster.

```sql
EXEC azure.machinelearningcompute.operationalization_clusters.check_system_services_updates_available 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_system_services">

Updates system services in a cluster.

```sql
EXEC azure.machinelearningcompute.operationalization_clusters.update_system_services 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
