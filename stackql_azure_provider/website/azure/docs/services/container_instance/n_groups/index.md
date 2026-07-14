--- 
title: n_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - n_groups
  - container_instance
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

Creates, updates, deletes, gets or lists a <code>n_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="n_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instance.n_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="containerGroupProfiles" /></td>
    <td><code>array</code></td>
    <td>The Container Group Profiles that could be used in the NGroups resource.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticProfile" /></td>
    <td><code>object</code></td>
    <td>The elastic profile.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the NGroup, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="placementProfile" /></td>
    <td><code>object</code></td>
    <td>Provides options w.r.t allocation and management w.r.t certain placement policies. These utilize capabilities provided by the underlying Azure infrastructure. They are typically used for high availability scenarios. E.g., distributing CGs across fault domains.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Canceled", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Canceled, Deleting, Migrating)</td>
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
    <td><CopyableCode code="updateProfile" /></td>
    <td><code>object</code></td>
    <td>Used by the customer to specify the way to update the Container Groups in NGroup.</td>
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
    <td><CopyableCode code="containerGroupProfiles" /></td>
    <td><code>array</code></td>
    <td>The Container Group Profiles that could be used in the NGroups resource.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticProfile" /></td>
    <td><code>object</code></td>
    <td>The elastic profile.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the NGroup, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="placementProfile" /></td>
    <td><code>object</code></td>
    <td>Provides options w.r.t allocation and management w.r.t certain placement policies. These utilize capabilities provided by the underlying Azure infrastructure. They are typically used for high availability scenarios. E.g., distributing CGs across fault domains.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Canceled", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Canceled, Deleting, Migrating)</td>
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
    <td><CopyableCode code="updateProfile" /></td>
    <td><code>object</code></td>
    <td>Used by the customer to specify the way to update the Container Groups in NGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="containerGroupProfiles" /></td>
    <td><code>array</code></td>
    <td>The Container Group Profiles that could be used in the NGroups resource.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticProfile" /></td>
    <td><code>object</code></td>
    <td>The elastic profile.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the NGroup, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="placementProfile" /></td>
    <td><code>object</code></td>
    <td>Provides options w.r.t allocation and management w.r.t certain placement policies. These utilize capabilities provided by the underlying Azure infrastructure. They are typically used for high availability scenarios. E.g., distributing CGs across fault domains.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Canceled", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Canceled, Deleting, Migrating)</td>
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
    <td><CopyableCode code="updateProfile" /></td>
    <td><code>object</code></td>
    <td>Used by the customer to specify the way to update the Container Groups in NGroup.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>NGroups GET REST API. Get the properties of the specified NGroups resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>GET NGroups under a resource group REST API. Gets a list of all NGroups resources under a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List NGroups in a subscription. Gets a list of all NGroups resources under a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>NGroup PUT REST API. Create or update a NGroups resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>NGroups PATCH REST API. Update a specified NGroups resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>NGroup PUT REST API. Create or update a NGroups resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>NGroups Delete REST API. Deletes the NGroups resource.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts all container groups in the specified NGroups resource. Starts all container groups in the specified NGroups resource. Compute resources will be allocated and billing will start.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops all container groups in the specified NGroups resource. Stops all container groups in the specified NGroups resource. Compute resources will be deallocated and billing will stop.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ngroups_name"><code>ngroups_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts all container groups in the specified NGroups resource. Restarts all container groups in the specified NGroups resource in place. If container image has updates, new image will be downloaded.</td>
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
<tr id="parameter-ngroups_name">
    <td><CopyableCode code="ngroups_name" /></td>
    <td><code>string</code></td>
    <td>The NGroups name. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

NGroups GET REST API. Get the properties of the specified NGroups resource.

```sql
SELECT
id,
name,
containerGroupProfiles,
elasticProfile,
identity,
location,
placementProfile,
provisioningState,
systemData,
tags,
type,
updateProfile,
zones
FROM azure.container_instance.n_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND ngroups_name = '{{ ngroups_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

GET NGroups under a resource group REST API. Gets a list of all NGroups resources under a resource group.

```sql
SELECT
id,
name,
containerGroupProfiles,
elasticProfile,
identity,
location,
placementProfile,
provisioningState,
systemData,
tags,
type,
updateProfile,
zones
FROM azure.container_instance.n_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List NGroups in a subscription. Gets a list of all NGroups resources under a subscription.

```sql
SELECT
id,
name,
containerGroupProfiles,
elasticProfile,
identity,
location,
placementProfile,
provisioningState,
systemData,
tags,
type,
updateProfile,
zones
FROM azure.container_instance.n_groups
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

NGroup PUT REST API. Create or update a NGroups resource.

```sql
INSERT INTO azure.container_instance.n_groups (
properties,
tags,
location,
zones,
identity,
resource_group_name,
ngroups_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ zones }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ ngroups_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: n_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the n_groups resource.
    - name: ngroups_name
      value: "{{ ngroups_name }}"
      description: Required parameter for the n_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the n_groups resource.
    - name: properties
      description: |
        Describes the properties of the NGroups resource.
      value:
        elasticProfile:
          desiredCount: {{ desiredCount }}
          maintainDesiredCount: {{ maintainDesiredCount }}
          containerGroupNamingPolicy:
            guidNamingPolicy:
              prefix: "{{ prefix }}"
        placementProfile:
          faultDomainCount: {{ faultDomainCount }}
        containerGroupProfiles:
          - resource:
              id: "{{ id }}"
            revision: {{ revision }}
            networkProfile:
              loadBalancer:
                backendAddressPools:
                  - resource: "{{ resource }}"
              applicationGateway:
                resource: "{{ resource }}"
                backendAddressPools:
                  - resource: "{{ resource }}"
            storageProfile:
              fileShares:
                - name: "{{ name }}"
                  resourceGroupName: "{{ resourceGroupName }}"
                  storageAccountName: "{{ storageAccountName }}"
                  properties:
                    shareAccessType: "{{ shareAccessType }}"
                    shareAccessTier: "{{ shareAccessTier }}"
            containerGroupProperties:
              subnetIds:
                - id: "{{ id }}"
                  name: "{{ name }}"
              volumes:
                - name: "{{ name }}"
                  azureFile:
                    shareName: "{{ shareName }}"
                    readOnly: {{ readOnly }}
                    storageAccountName: "{{ storageAccountName }}"
                    storageAccountKey: "{{ storageAccountKey }}"
                    storageAccountKeyReference: "{{ storageAccountKeyReference }}"
              containers:
                - name: "{{ name }}"
                  properties:
                    volumeMounts: "{{ volumeMounts }}"
        provisioningState: "{{ provisioningState }}"
        updateProfile:
          updateMode: "{{ updateMode }}"
          rollingUpdateProfile:
            maxBatchPercent: {{ maxBatchPercent }}
            maxUnhealthyPercent: {{ maxUnhealthyPercent }}
            pauseTimeBetweenBatches: "{{ pauseTimeBetweenBatches }}"
            inPlaceUpdate: {{ inPlaceUpdate }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: identity
      description: |
        The identity of the NGroup, if configured.
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

NGroups PATCH REST API. Update a specified NGroups resource.

```sql
UPDATE azure.container_instance.n_groups
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND ngroups_name = '{{ ngroups_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

NGroup PUT REST API. Create or update a NGroups resource.

```sql
REPLACE azure.container_instance.n_groups
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
zones = '{{ zones }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND ngroups_name = '{{ ngroups_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

NGroups Delete REST API. Deletes the NGroups resource.

```sql
DELETE FROM azure.container_instance.n_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND ngroups_name = '{{ ngroups_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'restart', value: 'restart' }
    ]}
>
<TabItem value="start">

Starts all container groups in the specified NGroups resource. Starts all container groups in the specified NGroups resource. Compute resources will be allocated and billing will start.

```sql
EXEC azure.container_instance.n_groups.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@ngroups_name='{{ ngroups_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops all container groups in the specified NGroups resource. Stops all container groups in the specified NGroups resource. Compute resources will be deallocated and billing will stop.

```sql
EXEC azure.container_instance.n_groups.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@ngroups_name='{{ ngroups_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restarts all container groups in the specified NGroups resource. Restarts all container groups in the specified NGroups resource in place. If container image has updates, new image will be downloaded.

```sql
EXEC azure.container_instance.n_groups.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@ngroups_name='{{ ngroups_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
