--- 
title: container_apps_session_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_session_pools
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>container_apps_session_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_apps_session_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.container_apps_session_pools" /></td></tr>
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
    <td><CopyableCode code="containerType" /></td>
    <td><code>string</code></td>
    <td>The container type of the sessions. You can use your own container to build the session pool, or you can use a predefined container to run workload with specific language. Known values are: "CustomContainer" and "PythonLTS". (CustomContainer, PythonLTS)</td>
</tr>
<tr>
    <td><CopyableCode code="customContainerTemplate" /></td>
    <td><code>object</code></td>
    <td>The custom container configuration if the containerType is CustomContainer.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicPoolConfiguration" /></td>
    <td><code>object</code></td>
    <td>The pool configuration if the poolManagementType is dynamic.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the session pool's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentitySettings" /></td>
    <td><code>array</code></td>
    <td>Optional settings for a Managed Identity that is assigned to the Session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes the session pool is using.</td>
</tr>
<tr>
    <td><CopyableCode code="poolManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint to manage the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="poolManagementType" /></td>
    <td><code>string</code></td>
    <td>The pool management type of the session pool. Known values are: "Manual" and "Dynamic". (Manual, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the session pool. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>The scale configuration of the session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>array</code></td>
    <td>The secrets of the session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration of the sessions in the session pool.</td>
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
    <td><CopyableCode code="containerType" /></td>
    <td><code>string</code></td>
    <td>The container type of the sessions. You can use your own container to build the session pool, or you can use a predefined container to run workload with specific language. Known values are: "CustomContainer" and "PythonLTS". (CustomContainer, PythonLTS)</td>
</tr>
<tr>
    <td><CopyableCode code="customContainerTemplate" /></td>
    <td><code>object</code></td>
    <td>The custom container configuration if the containerType is CustomContainer.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicPoolConfiguration" /></td>
    <td><code>object</code></td>
    <td>The pool configuration if the poolManagementType is dynamic.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the session pool's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentitySettings" /></td>
    <td><code>array</code></td>
    <td>Optional settings for a Managed Identity that is assigned to the Session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes the session pool is using.</td>
</tr>
<tr>
    <td><CopyableCode code="poolManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint to manage the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="poolManagementType" /></td>
    <td><code>string</code></td>
    <td>The pool management type of the session pool. Known values are: "Manual" and "Dynamic". (Manual, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the session pool. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>The scale configuration of the session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>array</code></td>
    <td>The secrets of the session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration of the sessions in the session pool.</td>
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
    <td><CopyableCode code="containerType" /></td>
    <td><code>string</code></td>
    <td>The container type of the sessions. You can use your own container to build the session pool, or you can use a predefined container to run workload with specific language. Known values are: "CustomContainer" and "PythonLTS". (CustomContainer, PythonLTS)</td>
</tr>
<tr>
    <td><CopyableCode code="customContainerTemplate" /></td>
    <td><code>object</code></td>
    <td>The custom container configuration if the containerType is CustomContainer.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicPoolConfiguration" /></td>
    <td><code>object</code></td>
    <td>The pool configuration if the poolManagementType is dynamic.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the session pool's environment.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedIdentitySettings" /></td>
    <td><code>array</code></td>
    <td>Optional settings for a Managed Identity that is assigned to the Session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes the session pool is using.</td>
</tr>
<tr>
    <td><CopyableCode code="poolManagementEndpoint" /></td>
    <td><code>string</code></td>
    <td>The endpoint to manage the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="poolManagementType" /></td>
    <td><code>string</code></td>
    <td>The pool management type of the session pool. Known values are: "Manual" and "Dynamic". (Manual, Dynamic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the session pool. Known values are: "InProgress", "Succeeded", "Failed", "Canceled", and "Deleting". (InProgress, Succeeded, Failed, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="scaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>The scale configuration of the session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>array</code></td>
    <td>The secrets of the session pool.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionNetworkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The network configuration of the sessions in the session pool.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-session_pool_name"><code>session_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a session pool. Get the properties of a session pool.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the session pools in a given resource group of a subscription. Get the session pools in a given resource group of a subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the session pools in a given subscription. Get the session pools in a given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-session_pool_name"><code>session_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a session pool. Create or update a session pool with the given properties.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-session_pool_name"><code>session_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update properties of a session pool. Patches a session pool using JSON merge patch.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-session_pool_name"><code>session_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a session pool. Create or update a session pool with the given properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-session_pool_name"><code>session_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a session pool. Delete the session pool with the given name.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-session_pool_name">
    <td><CopyableCode code="session_pool_name" /></td>
    <td><code>string</code></td>
    <td>Name of the session pool. Required.</td>
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

Get the properties of a session pool. Get the properties of a session pool.

```sql
SELECT
id,
name,
containerType,
customContainerTemplate,
dynamicPoolConfiguration,
environmentId,
identity,
location,
managedIdentitySettings,
nodeCount,
poolManagementEndpoint,
poolManagementType,
provisioningState,
scaleConfiguration,
secrets,
sessionNetworkConfiguration,
systemData,
tags,
type
FROM azure.appcontainers.container_apps_session_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND session_pool_name = '{{ session_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get the session pools in a given resource group of a subscription. Get the session pools in a given resource group of a subscription.

```sql
SELECT
id,
name,
containerType,
customContainerTemplate,
dynamicPoolConfiguration,
environmentId,
identity,
location,
managedIdentitySettings,
nodeCount,
poolManagementEndpoint,
poolManagementType,
provisioningState,
scaleConfiguration,
secrets,
sessionNetworkConfiguration,
systemData,
tags,
type
FROM azure.appcontainers.container_apps_session_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Get the session pools in a given subscription. Get the session pools in a given subscription.

```sql
SELECT
id,
name,
containerType,
customContainerTemplate,
dynamicPoolConfiguration,
environmentId,
identity,
location,
managedIdentitySettings,
nodeCount,
poolManagementEndpoint,
poolManagementType,
provisioningState,
scaleConfiguration,
secrets,
sessionNetworkConfiguration,
systemData,
tags,
type
FROM azure.appcontainers.container_apps_session_pools
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

Create or update a session pool. Create or update a session pool with the given properties.

```sql
INSERT INTO azure.appcontainers.container_apps_session_pools (
tags,
location,
properties,
identity,
resource_group_name,
session_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ session_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: container_apps_session_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the container_apps_session_pools resource.
    - name: session_pool_name
      value: "{{ session_pool_name }}"
      description: Required parameter for the container_apps_session_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the container_apps_session_pools resource.
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
        Container App session pool resource specific properties.
      value:
        environmentId: "{{ environmentId }}"
        containerType: "{{ containerType }}"
        poolManagementType: "{{ poolManagementType }}"
        nodeCount: {{ nodeCount }}
        scaleConfiguration:
          maxConcurrentSessions: {{ maxConcurrentSessions }}
          readySessionInstances: {{ readySessionInstances }}
        secrets:
          - name: "{{ name }}"
            value: "{{ value }}"
        dynamicPoolConfiguration:
          lifecycleConfiguration:
            lifecycleType: "{{ lifecycleType }}"
            cooldownPeriodInSeconds: {{ cooldownPeriodInSeconds }}
            maxAlivePeriodInSeconds: {{ maxAlivePeriodInSeconds }}
        customContainerTemplate:
          registryCredentials:
            server: "{{ server }}"
            username: "{{ username }}"
            passwordSecretRef: "{{ passwordSecretRef }}"
            identity: "{{ identity }}"
          containers:
            - image: "{{ image }}"
              name: "{{ name }}"
              command: "{{ command }}"
              args: "{{ args }}"
              env: "{{ env }}"
              resources:
                cpu: {{ cpu }}
                memory: "{{ memory }}"
          ingress:
            targetPort: {{ targetPort }}
        sessionNetworkConfiguration:
          status: "{{ status }}"
        poolManagementEndpoint: "{{ poolManagementEndpoint }}"
        provisioningState: "{{ provisioningState }}"
        managedIdentitySettings:
          - identity: "{{ identity }}"
            lifecycle: "{{ lifecycle }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update properties of a session pool. Patches a session pool using JSON merge patch.

```sql
UPDATE azure.appcontainers.container_apps_session_pools
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND session_pool_name = '{{ session_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Create or update a session pool. Create or update a session pool with the given properties.

```sql
REPLACE azure.appcontainers.container_apps_session_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND session_pool_name = '{{ session_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Delete a session pool. Delete the session pool with the given name.

```sql
DELETE FROM azure.appcontainers.container_apps_session_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND session_pool_name = '{{ session_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
