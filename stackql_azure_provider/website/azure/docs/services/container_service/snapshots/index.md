--- 
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - container_service
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.snapshots" /></td></tr>
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
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source agent pool resource ID to create this snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use a FIPS-enabled OS.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of node image.</td>
</tr>
<tr>
    <td><CopyableCode code="osSku" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes &lt;= 1.24 or Windows2022 when Kubernetes &gt;= 1.25 if OSType is Windows. Known values are: "Ubuntu", "AzureLinux", "AzureLinux3", "Mariner", "Flatcar", "CBLMariner", "Windows2019", "Windows2022", "Ubuntu2204", "Windows2025", "WindowsAnnual", "Ubuntu2404", and "AzureContainerLinux". (Ubuntu, AzureLinux, AzureLinux3, Mariner, Flatcar, CBLMariner, Windows2019, Windows2022, Ubuntu2204, Windows2025, WindowsAnnual, Ubuntu2404, AzureContainerLinux)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type. The default is Linux. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotType" /></td>
    <td><code>string</code></td>
    <td>The type of a snapshot. The default is NodePool. Known values are: "NodePool" and "ManagedCluster". (NodePool, ManagedCluster)</td>
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
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the VM.</td>
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
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source agent pool resource ID to create this snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use a FIPS-enabled OS.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of node image.</td>
</tr>
<tr>
    <td><CopyableCode code="osSku" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes &lt;= 1.24 or Windows2022 when Kubernetes &gt;= 1.25 if OSType is Windows. Known values are: "Ubuntu", "AzureLinux", "AzureLinux3", "Mariner", "Flatcar", "CBLMariner", "Windows2019", "Windows2022", "Ubuntu2204", "Windows2025", "WindowsAnnual", "Ubuntu2404", and "AzureContainerLinux". (Ubuntu, AzureLinux, AzureLinux3, Mariner, Flatcar, CBLMariner, Windows2019, Windows2022, Ubuntu2204, Windows2025, WindowsAnnual, Ubuntu2404, AzureContainerLinux)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type. The default is Linux. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotType" /></td>
    <td><code>string</code></td>
    <td>The type of a snapshot. The default is NodePool. Known values are: "NodePool" and "ManagedCluster". (NodePool, ManagedCluster)</td>
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
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the VM.</td>
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
    <td><CopyableCode code="creationData" /></td>
    <td><code>object</code></td>
    <td>CreationData to be used to specify the source agent pool resource ID to create this snapshot.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFIPS" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use a FIPS-enabled OS.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of node image.</td>
</tr>
<tr>
    <td><CopyableCode code="osSku" /></td>
    <td><code>string</code></td>
    <td>Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes &lt;= 1.24 or Windows2022 when Kubernetes &gt;= 1.25 if OSType is Windows. Known values are: "Ubuntu", "AzureLinux", "AzureLinux3", "Mariner", "Flatcar", "CBLMariner", "Windows2019", "Windows2022", "Ubuntu2204", "Windows2025", "WindowsAnnual", "Ubuntu2404", and "AzureContainerLinux". (Ubuntu, AzureLinux, AzureLinux3, Mariner, Flatcar, CBLMariner, Windows2019, Windows2022, Ubuntu2204, Windows2025, WindowsAnnual, Ubuntu2404, AzureContainerLinux)</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type. The default is Linux. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotType" /></td>
    <td><code>string</code></td>
    <td>The type of a snapshot. The default is NodePool. Known values are: "NodePool" and "ManagedCluster". (NodePool, ManagedCluster)</td>
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
    <td><CopyableCode code="vmSize" /></td>
    <td><code>string</code></td>
    <td>The size of the VM.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a snapshot.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists snapshots in the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of snapshots in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a snapshot.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags on a snapshot.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a snapshot.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a snapshot.</td>
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
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed cluster resource. Required.</td>
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

Gets a snapshot.

```sql
SELECT
id,
name,
creationData,
enableFIPS,
kubernetesVersion,
location,
nodeImageVersion,
osSku,
osType,
snapshotType,
systemData,
tags,
type,
vmSize
FROM azure.container_service.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists snapshots in the specified subscription and resource group.

```sql
SELECT
id,
name,
creationData,
enableFIPS,
kubernetesVersion,
location,
nodeImageVersion,
osSku,
osType,
snapshotType,
systemData,
tags,
type,
vmSize
FROM azure.container_service.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of snapshots in the specified subscription.

```sql
SELECT
id,
name,
creationData,
enableFIPS,
kubernetesVersion,
location,
nodeImageVersion,
osSku,
osType,
snapshotType,
systemData,
tags,
type,
vmSize
FROM azure.container_service.snapshots
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

Creates or updates a snapshot.

```sql
INSERT INTO azure.container_service.snapshots (
tags,
location,
properties,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
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
- name: snapshots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the snapshots resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the snapshots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the snapshots resource.
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
        Properties of a snapshot.
      value:
        creationData:
          sourceResourceId: "{{ sourceResourceId }}"
        snapshotType: "{{ snapshotType }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        nodeImageVersion: "{{ nodeImageVersion }}"
        osType: "{{ osType }}"
        osSku: "{{ osSku }}"
        vmSize: "{{ vmSize }}"
        enableFIPS: {{ enableFIPS }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates tags on a snapshot.

```sql
UPDATE azure.container_service.snapshots
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
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

Creates or updates a snapshot.

```sql
REPLACE azure.container_service.snapshots
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
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

Deletes a snapshot.

```sql
DELETE FROM azure.container_service.snapshots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
