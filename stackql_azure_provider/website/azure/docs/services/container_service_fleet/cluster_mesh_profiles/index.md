--- 
title: cluster_mesh_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_mesh_profiles
  - container_service_fleet
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

Creates, updates, deletes, gets or lists a <code>cluster_mesh_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_mesh_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service_fleet.cluster_mesh_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_fleet', value: 'list_by_fleet' }
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
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="memberSelector" /></td>
    <td><code>object</code></td>
    <td>Select the members of the mesh. * Only key/value pairs with the `=` operator are accepted in the label selector. * If empty or not specified, no Fleet members will be selected to join the mesh.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster mesh profile. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The cluster mesh profile status.</td>
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
<TabItem value="list_by_fleet">

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
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="memberSelector" /></td>
    <td><code>object</code></td>
    <td>Select the members of the mesh. * Only key/value pairs with the `=` operator are accepted in the label selector. * If empty or not specified, no Fleet members will be selected to join the mesh.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster mesh profile. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The cluster mesh profile status.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-cluster_mesh_profile_name"><code>cluster_mesh_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ClusterMeshProfile.</td>
</tr>
<tr>
    <td><a href="#list_by_fleet"><CopyableCode code="list_by_fleet" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ClusterMeshProfile resources by Fleet.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-cluster_mesh_profile_name"><code>cluster_mesh_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ClusterMeshProfile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-cluster_mesh_profile_name"><code>cluster_mesh_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a ClusterMeshProfile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-cluster_mesh_profile_name"><code>cluster_mesh_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ClusterMeshProfile.</td>
</tr>
<tr>
    <td><a href="#apply"><CopyableCode code="apply" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fleet_name"><code>fleet_name</code></a>, <a href="#parameter-cluster_mesh_profile_name"><code>cluster_mesh_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Applies the cluster mesh profile to selected fleet members.</td>
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
<tr id="parameter-cluster_mesh_profile_name">
    <td><CopyableCode code="cluster_mesh_profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ClusterMeshProfile resource. Required.</td>
</tr>
<tr id="parameter-fleet_name">
    <td><CopyableCode code="fleet_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Fleet resource. Required.</td>
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
        { label: 'list_by_fleet', value: 'list_by_fleet' }
    ]}
>
<TabItem value="get">

Get a ClusterMeshProfile.

```sql
SELECT
id,
name,
eTag,
memberSelector,
provisioningState,
status,
systemData,
type
FROM azure.container_service_fleet.cluster_mesh_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND cluster_mesh_profile_name = '{{ cluster_mesh_profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_fleet">

List ClusterMeshProfile resources by Fleet.

```sql
SELECT
id,
name,
eTag,
memberSelector,
provisioningState,
status,
systemData,
type
FROM azure.container_service_fleet.cluster_mesh_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND fleet_name = '{{ fleet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a ClusterMeshProfile.

```sql
INSERT INTO azure.container_service_fleet.cluster_mesh_profiles (
properties,
resource_group_name,
fleet_name,
cluster_mesh_profile_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ fleet_name }}',
'{{ cluster_mesh_profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cluster_mesh_profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cluster_mesh_profiles resource.
    - name: fleet_name
      value: "{{ fleet_name }}"
      description: Required parameter for the cluster_mesh_profiles resource.
    - name: cluster_mesh_profile_name
      value: "{{ cluster_mesh_profile_name }}"
      description: Required parameter for the cluster_mesh_profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cluster_mesh_profiles resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        memberSelector:
          byLabel: "{{ byLabel }}"
        status:
          state: "{{ state }}"
          lastAppliedMemberSelector:
            byLabel: "{{ byLabel }}"
          lastOperationId: "{{ lastOperationId }}"
          lastOperationError:
            code: "{{ code }}"
            message: "{{ message }}"
            target: "{{ target }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                target: "{{ target }}"
                details: "{{ details }}"
                additionalInfo: "{{ additionalInfo }}"
            additionalInfo:
              - type: "{{ type }}"
                info: "{{ info }}"
`}</CodeBlock>

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

Create a ClusterMeshProfile.

```sql
REPLACE azure.container_service_fleet.cluster_mesh_profiles
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND cluster_mesh_profile_name = '{{ cluster_mesh_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
properties,
systemData,
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

Delete a ClusterMeshProfile.

```sql
DELETE FROM azure.container_service_fleet.cluster_mesh_profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND fleet_name = '{{ fleet_name }}' --required
AND cluster_mesh_profile_name = '{{ cluster_mesh_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="apply"
    values={[
        { label: 'apply', value: 'apply' }
    ]}
>
<TabItem value="apply">

Applies the cluster mesh profile to selected fleet members.

```sql
EXEC azure.container_service_fleet.cluster_mesh_profiles.apply 
@resource_group_name='{{ resource_group_name }}' --required, 
@fleet_name='{{ fleet_name }}' --required, 
@cluster_mesh_profile_name='{{ cluster_mesh_profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
