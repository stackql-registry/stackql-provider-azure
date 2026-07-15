--- 
title: storage_class
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_class
  - container_orchestrator_runtime
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

Creates, updates, deletes, gets or lists a <code>storage_class</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="storage_class" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_orchestrator_runtime.storage_class" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="accessModes" /></td>
    <td><code>array</code></td>
    <td>The access mode: [ReadWriteOnce, ReadWriteMany] or [ReadWriteOnce].</td>
</tr>
<tr>
    <td><CopyableCode code="allowVolumeExpansion" /></td>
    <td><code>string</code></td>
    <td>Volume can be expanded or not. Known values are: "Allow" and "Disallow". (Allow, Disallow)</td>
</tr>
<tr>
    <td><CopyableCode code="dataResilience" /></td>
    <td><code>string</code></td>
    <td>Allow single data node failure. Known values are: "NotDataResilient" and "DataResilient". (NotDataResilient, DataResilient)</td>
</tr>
<tr>
    <td><CopyableCode code="failoverSpeed" /></td>
    <td><code>string</code></td>
    <td>Failover speed: NA, Slow, Fast. Known values are: "NotAvailable", "Slow", "Fast", and "Super". (NotAvailable, Slow, Fast, Super)</td>
</tr>
<tr>
    <td><CopyableCode code="limitations" /></td>
    <td><code>array</code></td>
    <td>Limitations of the storage class.</td>
</tr>
<tr>
    <td><CopyableCode code="mountOptions" /></td>
    <td><code>array</code></td>
    <td>Additional mount options.</td>
</tr>
<tr>
    <td><CopyableCode code="performance" /></td>
    <td><code>string</code></td>
    <td>Performance tier. Known values are: "Undefined", "Basic", "Standard", "Premium", and "Ultra". (Undefined, Basic, Standard, Premium, Ultra)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Selection priority when multiple storage classes meet the criteria. 0: Highest, -1: Never use.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioner" /></td>
    <td><code>string</code></td>
    <td>Provisioner name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provision state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
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
<tr>
    <td><CopyableCode code="typeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the StorageClass. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeBindingMode" /></td>
    <td><code>string</code></td>
    <td>Binding mode of volumes: Immediate, WaitForFirstConsumer. Known values are: "Immediate" and "WaitForFirstConsumer". (Immediate, WaitForFirstConsumer)</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="accessModes" /></td>
    <td><code>array</code></td>
    <td>The access mode: [ReadWriteOnce, ReadWriteMany] or [ReadWriteOnce].</td>
</tr>
<tr>
    <td><CopyableCode code="allowVolumeExpansion" /></td>
    <td><code>string</code></td>
    <td>Volume can be expanded or not. Known values are: "Allow" and "Disallow". (Allow, Disallow)</td>
</tr>
<tr>
    <td><CopyableCode code="dataResilience" /></td>
    <td><code>string</code></td>
    <td>Allow single data node failure. Known values are: "NotDataResilient" and "DataResilient". (NotDataResilient, DataResilient)</td>
</tr>
<tr>
    <td><CopyableCode code="failoverSpeed" /></td>
    <td><code>string</code></td>
    <td>Failover speed: NA, Slow, Fast. Known values are: "NotAvailable", "Slow", "Fast", and "Super". (NotAvailable, Slow, Fast, Super)</td>
</tr>
<tr>
    <td><CopyableCode code="limitations" /></td>
    <td><code>array</code></td>
    <td>Limitations of the storage class.</td>
</tr>
<tr>
    <td><CopyableCode code="mountOptions" /></td>
    <td><code>array</code></td>
    <td>Additional mount options.</td>
</tr>
<tr>
    <td><CopyableCode code="performance" /></td>
    <td><code>string</code></td>
    <td>Performance tier. Known values are: "Undefined", "Basic", "Standard", "Premium", and "Ultra". (Undefined, Basic, Standard, Premium, Ultra)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Selection priority when multiple storage classes meet the criteria. 0: Highest, -1: Never use.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioner" /></td>
    <td><code>string</code></td>
    <td>Provisioner name.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provision state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
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
<tr>
    <td><CopyableCode code="typeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of the StorageClass. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeBindingMode" /></td>
    <td><code>string</code></td>
    <td>Binding mode of volumes: Immediate, WaitForFirstConsumer. Known values are: "Immediate" and "WaitForFirstConsumer". (Immediate, WaitForFirstConsumer)</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-storage_class_name"><code>storage_class_name</code></a></td>
    <td></td>
    <td>Get a StorageClassResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>List StorageClassResource resources by parent.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-storage_class_name"><code>storage_class_name</code></a></td>
    <td></td>
    <td>Create a StorageClassResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-storage_class_name"><code>storage_class_name</code></a></td>
    <td></td>
    <td>Update a StorageClassResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-storage_class_name"><code>storage_class_name</code></a></td>
    <td></td>
    <td>Create a StorageClassResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-storage_class_name"><code>storage_class_name</code></a></td>
    <td></td>
    <td>Delete a StorageClassResource.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-storage_class_name">
    <td><CopyableCode code="storage_class_name" /></td>
    <td><code>string</code></td>
    <td>The name of the the storage class. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a StorageClassResource.

```sql
SELECT
id,
name,
accessModes,
allowVolumeExpansion,
dataResilience,
failoverSpeed,
limitations,
mountOptions,
performance,
priority,
provisioner,
provisioningState,
systemData,
type,
typeProperties,
volumeBindingMode
FROM azure.container_orchestrator_runtime.storage_class
WHERE resource_uri = '{{ resource_uri }}' -- required
AND storage_class_name = '{{ storage_class_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List StorageClassResource resources by parent.

```sql
SELECT
id,
name,
accessModes,
allowVolumeExpansion,
dataResilience,
failoverSpeed,
limitations,
mountOptions,
performance,
priority,
provisioner,
provisioningState,
systemData,
type,
typeProperties,
volumeBindingMode
FROM azure.container_orchestrator_runtime.storage_class
WHERE resource_uri = '{{ resource_uri }}' -- required
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

Create a StorageClassResource.

```sql
INSERT INTO azure.container_orchestrator_runtime.storage_class (
properties,
resource_uri,
storage_class_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ storage_class_name }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: storage_class
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the storage_class resource.
    - name: storage_class_name
      value: "{{ storage_class_name }}"
      description: Required parameter for the storage_class resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        allowVolumeExpansion: "{{ allowVolumeExpansion }}"
        mountOptions:
          - "{{ mountOptions }}"
        provisioner: "{{ provisioner }}"
        volumeBindingMode: "{{ volumeBindingMode }}"
        accessModes:
          - "{{ accessModes }}"
        dataResilience: "{{ dataResilience }}"
        failoverSpeed: "{{ failoverSpeed }}"
        limitations:
          - "{{ limitations }}"
        performance: "{{ performance }}"
        priority: {{ priority }}
        typeProperties:
          type: "{{ type }}"
        provisioningState: "{{ provisioningState }}"
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

Update a StorageClassResource.

```sql
UPDATE azure.container_orchestrator_runtime.storage_class
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND storage_class_name = '{{ storage_class_name }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Create a StorageClassResource.

```sql
REPLACE azure.container_orchestrator_runtime.storage_class
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND storage_class_name = '{{ storage_class_name }}' --required
RETURNING
id,
name,
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

Delete a StorageClassResource.

```sql
DELETE FROM azure.container_orchestrator_runtime.storage_class
WHERE resource_uri = '{{ resource_uri }}' --required
AND storage_class_name = '{{ storage_class_name }}' --required
;
```
</TabItem>
</Tabs>
