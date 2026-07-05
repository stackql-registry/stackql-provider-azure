--- 
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - storagemover
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storagemover.connections" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Approved", "Rejected", "Disconnected", "Pending", and "Stale". (Approved, Rejected, Disconnected, Pending, Stale)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the Connection.</td>
</tr>
<tr>
    <td><CopyableCode code="jobList" /></td>
    <td><code>array</code></td>
    <td>List of job definitions associated with this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>The PrivateEndpointName associated with the connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointResourceId" /></td>
    <td><code>string</code></td>
    <td>The privateEndpoint resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceId" /></td>
    <td><code>string</code></td>
    <td>The PrivateLinkServiceId for the connection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
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
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>The connection status. Known values are: "Approved", "Rejected", "Disconnected", "Pending", and "Stale". (Approved, Rejected, Disconnected, Pending, Stale)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the Connection.</td>
</tr>
<tr>
    <td><CopyableCode code="jobList" /></td>
    <td><code>array</code></td>
    <td>List of job definitions associated with this connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>The PrivateEndpointName associated with the connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointResourceId" /></td>
    <td><code>string</code></td>
    <td>The privateEndpoint resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceId" /></td>
    <td><code>string</code></td>
    <td>The PrivateLinkServiceId for the connection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of this resource. Known values are: "Succeeded", "Canceled", "Failed", and "Deleting". (Succeeded, Canceled, Failed, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Connection resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Connections in a Storage Mover.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Connection resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates a Connection resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-storage_mover_name"><code>storage_mover_name</code></a>, <a href="#parameter-connection_name"><code>connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Connection resource. Returns 409 if there are active jobs using this connection.</td>
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
<tr id="parameter-connection_name">
    <td><CopyableCode code="connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Connection resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-storage_mover_name">
    <td><CopyableCode code="storage_mover_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Storage Mover resource. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a Connection resource.

```sql
SELECT
id,
name,
connectionStatus,
description,
jobList,
privateEndpointName,
privateEndpointResourceId,
privateLinkServiceId,
provisioningState,
systemData,
type
FROM azure.storagemover.connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
AND connection_name = '{{ connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Connections in a Storage Mover.

```sql
SELECT
id,
name,
connectionStatus,
description,
jobList,
privateEndpointName,
privateEndpointResourceId,
privateLinkServiceId,
provisioningState,
systemData,
type
FROM azure.storagemover.connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND storage_mover_name = '{{ storage_mover_name }}' -- required
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

Creates or updates a Connection resource.

```sql
INSERT INTO azure.storagemover.connections (
properties,
resource_group_name,
storage_mover_name,
connection_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ storage_mover_name }}',
'{{ connection_name }}',
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
- name: connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connections resource.
    - name: storage_mover_name
      value: "{{ storage_mover_name }}"
      description: Required parameter for the connections resource.
    - name: connection_name
      value: "{{ connection_name }}"
      description: Required parameter for the connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connections resource.
    - name: properties
      description: |
        Connection properties. Required.
      value:
        description: "{{ description }}"
        connectionStatus: "{{ connectionStatus }}"
        privateLinkServiceId: "{{ privateLinkServiceId }}"
        privateEndpointName: "{{ privateEndpointName }}"
        privateEndpointResourceId: "{{ privateEndpointResourceId }}"
        jobList:
          - "{{ jobList }}"
        provisioningState: "{{ provisioningState }}"
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

Creates or updates a Connection resource.

```sql
REPLACE azure.storagemover.connections
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND connection_name = '{{ connection_name }}' --required
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

Deletes a Connection resource. Returns 409 if there are active jobs using this connection.

```sql
DELETE FROM azure.storagemover.connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND storage_mover_name = '{{ storage_mover_name }}' --required
AND connection_name = '{{ connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
