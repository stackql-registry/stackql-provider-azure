--- 
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - devcenter
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_project', value: 'list_by_project' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="devBoxCount" /></td>
    <td><code>integer</code></td>
    <td>Indicates the number of provisioned Dev Boxes in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="devBoxDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Name of a Dev Box definition in parent Project of this Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the Pool. Indicates whether or not the Pool is available to create Dev Boxes. Known values are: "Unknown", "Pending", "Healthy", "Warning", and "Unhealthy".</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatusDetails" /></td>
    <td><code>array</code></td>
    <td>Details on the Pool health status to help diagnose issues. This is only populated when the pool status indicates the pool is in a non-healthy state.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created. "Windows_Client"</td>
</tr>
<tr>
    <td><CopyableCode code="localAdministrator" /></td>
    <td><code>string</code></td>
    <td>Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetworkRegions" /></td>
    <td><code>array</code></td>
    <td>The regions of the managed virtual network (required when managedNetworkType is Managed).</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionName" /></td>
    <td><code>string</code></td>
    <td>Name of a Network Connection in parent Project of this Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="singleSignOnStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="stopOnDisconnect" /></td>
    <td><code>object</code></td>
    <td>Stop on disconnect configuration settings for Dev Boxes created in this pool.</td>
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
    <td><CopyableCode code="virtualNetworkType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network. Known values are: "Managed" and "Unmanaged".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_project">

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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="devBoxCount" /></td>
    <td><code>integer</code></td>
    <td>Indicates the number of provisioned Dev Boxes in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="devBoxDefinitionName" /></td>
    <td><code>string</code></td>
    <td>Name of a Dev Box definition in parent Project of this Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the Pool. Indicates whether or not the Pool is available to create Dev Boxes. Known values are: "Unknown", "Pending", "Healthy", "Warning", and "Unhealthy".</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatusDetails" /></td>
    <td><code>array</code></td>
    <td>Details on the Pool health status to help diagnose issues. This is only populated when the pool status indicates the pool is in a non-healthy state.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created. "Windows_Client"</td>
</tr>
<tr>
    <td><CopyableCode code="localAdministrator" /></td>
    <td><code>string</code></td>
    <td>Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedVirtualNetworkRegions" /></td>
    <td><code>array</code></td>
    <td>The regions of the managed virtual network (required when managedNetworkType is Managed).</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionName" /></td>
    <td><code>string</code></td>
    <td>Name of a Network Connection in parent Project of this Pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="singleSignOnStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Dev Boxes in this pool are created with single sign on enabled. The also requires that single sign on be enabled on the tenant. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="stopOnDisconnect" /></td>
    <td><code>object</code></td>
    <td>Stop on disconnect configuration settings for Dev Boxes created in this pool.</td>
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
    <td><CopyableCode code="virtualNetworkType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the pool uses a Virtual Network managed by Microsoft or a customer provided network. Known values are: "Managed" and "Unmanaged".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a machine pool.</td>
</tr>
<tr>
    <td><a href="#list_by_project"><CopyableCode code="list_by_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists pools for a project.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a machine pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Partially updates a machine pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a machine pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a machine pool.</td>
</tr>
<tr>
    <td><a href="#run_health_checks"><CopyableCode code="run_health_checks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Triggers a refresh of the pool status.</td>
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
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>Name of the pool. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of the project. Required.</td>
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
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_project', value: 'list_by_project' }
    ]}
>
<TabItem value="get">

Gets a machine pool.

```sql
SELECT
id,
name,
devBoxCount,
devBoxDefinitionName,
displayName,
healthStatus,
healthStatusDetails,
licenseType,
localAdministrator,
location,
managedVirtualNetworkRegions,
networkConnectionName,
provisioningState,
singleSignOnStatus,
stopOnDisconnect,
systemData,
tags,
type,
virtualNetworkType
FROM azure.devcenter.pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_project">

Lists pools for a project.

```sql
SELECT
id,
name,
devBoxCount,
devBoxDefinitionName,
displayName,
healthStatus,
healthStatusDetails,
licenseType,
localAdministrator,
location,
managedVirtualNetworkRegions,
networkConnectionName,
provisioningState,
singleSignOnStatus,
stopOnDisconnect,
systemData,
tags,
type,
virtualNetworkType
FROM azure.devcenter.pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Creates or updates a machine pool.

```sql
INSERT INTO azure.devcenter.pools (
tags,
location,
properties,
resource_group_name,
project_name,
pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ project_name }}',
'{{ pool_name }}',
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
- name: pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the pools resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the pools resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the pools resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        devBoxDefinitionName: "{{ devBoxDefinitionName }}"
        networkConnectionName: "{{ networkConnectionName }}"
        licenseType: "{{ licenseType }}"
        localAdministrator: "{{ localAdministrator }}"
        stopOnDisconnect:
          status: "{{ status }}"
          gracePeriodMinutes: {{ gracePeriodMinutes }}
        singleSignOnStatus: "{{ singleSignOnStatus }}"
        displayName: "{{ displayName }}"
        virtualNetworkType: "{{ virtualNetworkType }}"
        managedVirtualNetworkRegions:
          - "{{ managedVirtualNetworkRegions }}"
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

Partially updates a machine pool.

```sql
UPDATE azure.devcenter.pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND pool_name = '{{ pool_name }}' --required
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

Creates or updates a machine pool.

```sql
REPLACE azure.devcenter.pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND pool_name = '{{ pool_name }}' --required
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

Deletes a machine pool.

```sql
DELETE FROM azure.devcenter.pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="run_health_checks"
    values={[
        { label: 'run_health_checks', value: 'run_health_checks' }
    ]}
>
<TabItem value="run_health_checks">

Triggers a refresh of the pool status.

```sql
EXEC azure.devcenter.pools.run_health_checks 
@resource_group_name='{{ resource_group_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
