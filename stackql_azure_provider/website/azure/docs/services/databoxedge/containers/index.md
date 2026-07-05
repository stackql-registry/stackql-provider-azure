--- 
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - databoxedge
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

Creates, updates, deletes, gets or lists a <code>containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databoxedge.containers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_storage_account', value: 'list_by_storage_account' }
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
    <td><CopyableCode code="containerStatus" /></td>
    <td><code>string</code></td>
    <td>Current status of the container. Known values are: "OK", "Offline", "Unknown", "Updating", and "NeedsAttention". (OK, Offline, Unknown, Updating, NeedsAttention)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time when container got created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataFormat" /></td>
    <td><code>string</code></td>
    <td>DataFormat for Container. Required. Known values are: "BlockBlob", "PageBlob", and "AzureFile". (BlockBlob, PageBlob, AzureFile)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the refresh job on this container.</td>
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
<TabItem value="list_by_storage_account">

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
    <td><CopyableCode code="containerStatus" /></td>
    <td><code>string</code></td>
    <td>Current status of the container. Known values are: "OK", "Offline", "Unknown", "Updating", and "NeedsAttention". (OK, Offline, Unknown, Updating, NeedsAttention)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time when container got created.</td>
</tr>
<tr>
    <td><CopyableCode code="dataFormat" /></td>
    <td><code>string</code></td>
    <td>DataFormat for Container. Required. Known values are: "BlockBlob", "PageBlob", and "AzureFile". (BlockBlob, PageBlob, AzureFile)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the refresh job on this container.</td>
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
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-storage_account_name"><code>storage_account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a container by name. Gets a container by name.</td>
</tr>
<tr>
    <td><a href="#list_by_storage_account"><CopyableCode code="list_by_storage_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-storage_account_name"><code>storage_account_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the containers of a storage Account in a Data Box Edge/Data Box Gateway device. Lists all the containers of a storage Account in a Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-storage_account_name"><code>storage_account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new container or updates an existing container on the device. Creates a new container or updates an existing container on the device.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-storage_account_name"><code>storage_account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new container or updates an existing container on the device. Creates a new container or updates an existing container on the device.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-storage_account_name"><code>storage_account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the container on the Data Box Edge/Data Box Gateway device.</td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device_name"><code>device_name</code></a>, <a href="#parameter-storage_account_name"><code>storage_account_name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refreshes the container metadata with the data from the cloud. Refreshes the container metadata with the data from the cloud.</td>
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
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>The container Name. Required.</td>
</tr>
<tr id="parameter-device_name">
    <td><CopyableCode code="device_name" /></td>
    <td><code>string</code></td>
    <td>The device name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_account_name">
    <td><CopyableCode code="storage_account_name" /></td>
    <td><code>string</code></td>
    <td>The storage account name. Required.</td>
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
        { label: 'list_by_storage_account', value: 'list_by_storage_account' }
    ]}
>
<TabItem value="get">

Gets a container by name. Gets a container by name.

```sql
SELECT
id,
name,
containerStatus,
createdDateTime,
dataFormat,
refreshDetails,
systemData,
type
FROM azure.databoxedge.containers
WHERE device_name = '{{ device_name }}' -- required
AND storage_account_name = '{{ storage_account_name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_storage_account">

Lists all the containers of a storage Account in a Data Box Edge/Data Box Gateway device. Lists all the containers of a storage Account in a Data Box Edge/Data Box Gateway device.

```sql
SELECT
id,
name,
containerStatus,
createdDateTime,
dataFormat,
refreshDetails,
systemData,
type
FROM azure.databoxedge.containers
WHERE device_name = '{{ device_name }}' -- required
AND storage_account_name = '{{ storage_account_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
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

Creates a new container or updates an existing container on the device. Creates a new container or updates an existing container on the device.

```sql
INSERT INTO azure.databoxedge.containers (
properties,
device_name,
storage_account_name,
container_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ device_name }}',
'{{ storage_account_name }}',
'{{ container_name }}',
'{{ resource_group_name }}',
'{{ subscription_id }}'
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
- name: containers
  props:
    - name: device_name
      value: "{{ device_name }}"
      description: Required parameter for the containers resource.
    - name: storage_account_name
      value: "{{ storage_account_name }}"
      description: Required parameter for the containers resource.
    - name: container_name
      value: "{{ container_name }}"
      description: Required parameter for the containers resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the containers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the containers resource.
    - name: properties
      description: |
        The container properties. Required.
      value:
        containerStatus: "{{ containerStatus }}"
        dataFormat: "{{ dataFormat }}"
        refreshDetails:
          inProgressRefreshJobId: "{{ inProgressRefreshJobId }}"
          lastCompletedRefreshJobTimeInUTC: "{{ lastCompletedRefreshJobTimeInUTC }}"
          errorManifestFile: "{{ errorManifestFile }}"
          lastJob: "{{ lastJob }}"
        createdDateTime: "{{ createdDateTime }}"
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

Creates a new container or updates an existing container on the device. Creates a new container or updates an existing container on the device.

```sql
REPLACE azure.databoxedge.containers
SET 
properties = '{{ properties }}'
WHERE 
device_name = '{{ device_name }}' --required
AND storage_account_name = '{{ storage_account_name }}' --required
AND container_name = '{{ container_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Deletes the container on the Data Box Edge/Data Box Gateway device.

```sql
DELETE FROM azure.databoxedge.containers
WHERE device_name = '{{ device_name }}' --required
AND storage_account_name = '{{ storage_account_name }}' --required
AND container_name = '{{ container_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh"
    values={[
        { label: 'refresh', value: 'refresh' }
    ]}
>
<TabItem value="refresh">

Refreshes the container metadata with the data from the cloud. Refreshes the container metadata with the data from the cloud.

```sql
EXEC azure.databoxedge.containers.refresh 
@device_name='{{ device_name }}' --required, 
@storage_account_name='{{ storage_account_name }}' --required, 
@container_name='{{ container_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
