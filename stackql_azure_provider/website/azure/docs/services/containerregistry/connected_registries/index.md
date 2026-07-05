--- 
title: connected_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_registries
  - containerregistry
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

Creates, updates, deletes, gets or lists a <code>connected_registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connected_registries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerregistry.connected_registries" /></td></tr>
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
    <td>The name of the private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activation" /></td>
    <td><code>object</code></td>
    <td>The activation properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="clientTokenIds" /></td>
    <td><code>array</code></td>
    <td>The list of the ACR token resource IDs used to authenticate clients to the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>The current connection state of the connected registry. Known values are: "Online", "Offline", "Syncing", and "Unhealthy". (Online, Offline, Syncing, Unhealthy)</td>
</tr>
<tr>
    <td><CopyableCode code="garbageCollection" /></td>
    <td><code>object</code></td>
    <td>The garbage collection properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActivityTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last activity time of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>The logging properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="loginServer" /></td>
    <td><code>object</code></td>
    <td>The login server properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode of the connected registry resource that indicates the permissions of the registry. Required. Known values are: "ReadWrite", "ReadOnly", "Registry", and "Mirror". (ReadWrite, ReadOnly, Registry, Mirror)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationsList" /></td>
    <td><code>array</code></td>
    <td>The list of notifications subscription information for the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td>The parent of the connected registry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="registrySyncResult" /></td>
    <td><code>object</code></td>
    <td>The result of the connected registry's most recent sync with its parent.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>array</code></td>
    <td>The list of current statuses of the connected registry.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The current version of ACR runtime on the connected registry.</td>
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
    <td>The name of the private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="activation" /></td>
    <td><code>object</code></td>
    <td>The activation properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="clientTokenIds" /></td>
    <td><code>array</code></td>
    <td>The list of the ACR token resource IDs used to authenticate clients to the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>The current connection state of the connected registry. Known values are: "Online", "Offline", "Syncing", and "Unhealthy". (Online, Offline, Syncing, Unhealthy)</td>
</tr>
<tr>
    <td><CopyableCode code="garbageCollection" /></td>
    <td><code>object</code></td>
    <td>The garbage collection properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActivityTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last activity time of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>The logging properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="loginServer" /></td>
    <td><code>object</code></td>
    <td>The login server properties of the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode of the connected registry resource that indicates the permissions of the registry. Required. Known values are: "ReadWrite", "ReadOnly", "Registry", and "Mirror". (ReadWrite, ReadOnly, Registry, Mirror)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationsList" /></td>
    <td><code>array</code></td>
    <td>The list of notifications subscription information for the connected registry.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td>The parent of the connected registry. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="registrySyncResult" /></td>
    <td><code>object</code></td>
    <td>The result of the connected registry's most recent sync with its parent.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>array</code></td>
    <td>The list of current statuses of the connected registry.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The current version of ACR runtime on the connected registry.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-connected_registry_name"><code>connected_registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the connected registry.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all connected registries for the specified container registry.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-connected_registry_name"><code>connected_registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a connected registry for a container registry with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-connected_registry_name"><code>connected_registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a connected registry with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-connected_registry_name"><code>connected_registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a connected registry from a container registry.</td>
</tr>
<tr>
    <td><a href="#deactivate"><CopyableCode code="deactivate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-connected_registry_name"><code>connected_registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deactivates the connected registry instance.</td>
</tr>
<tr>
    <td><a href="#resync"><CopyableCode code="resync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-connected_registry_name"><code>connected_registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resync the connected registry instance.</td>
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
<tr id="parameter-connected_registry_name">
    <td><CopyableCode code="connected_registry_name" /></td>
    <td><code>string</code></td>
    <td>The name of the connected registry. Required.</td>
</tr>
<tr id="parameter-registry_name">
    <td><CopyableCode code="registry_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container registry. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that describes a subset of connectedRegistries to return. The parameters that can be filtered are parent.id (the resource id of the connectedRegistry parent), mode, and connectionState. The supported operator is eq. Default value is None.</td>
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

Gets the properties of the connected registry.

```sql
SELECT
id,
name,
activation,
clientTokenIds,
connectionState,
garbageCollection,
lastActivityTime,
logging,
loginServer,
mode,
notificationsList,
parent,
provisioningState,
registrySyncResult,
statusDetails,
systemData,
type,
version
FROM azure.containerregistry.connected_registries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND connected_registry_name = '{{ connected_registry_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all connected registries for the specified container registry.

```sql
SELECT
id,
name,
activation,
clientTokenIds,
connectionState,
garbageCollection,
lastActivityTime,
logging,
loginServer,
mode,
notificationsList,
parent,
provisioningState,
registrySyncResult,
statusDetails,
systemData,
type,
version
FROM azure.containerregistry.connected_registries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a connected registry for a container registry with the specified parameters.

```sql
INSERT INTO azure.containerregistry.connected_registries (
properties,
resource_group_name,
registry_name,
connected_registry_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ registry_name }}',
'{{ connected_registry_name }}',
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
- name: connected_registries
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connected_registries resource.
    - name: registry_name
      value: "{{ registry_name }}"
      description: Required parameter for the connected_registries resource.
    - name: connected_registry_name
      value: "{{ connected_registry_name }}"
      description: Required parameter for the connected_registries resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connected_registries resource.
    - name: properties
      description: |
        The properties of the connected registry.
      value:
        provisioningState: "{{ provisioningState }}"
        mode: "{{ mode }}"
        version: "{{ version }}"
        connectionState: "{{ connectionState }}"
        lastActivityTime: "{{ lastActivityTime }}"
        activation:
          status: "{{ status }}"
        parent:
          id: "{{ id }}"
          syncProperties:
            tokenId: "{{ tokenId }}"
            schedule: "{{ schedule }}"
            syncWindow: "{{ syncWindow }}"
            messageTtl: "{{ messageTtl }}"
            lastSyncTime: "{{ lastSyncTime }}"
            gatewayEndpoint: "{{ gatewayEndpoint }}"
        clientTokenIds:
          - "{{ clientTokenIds }}"
        loginServer:
          host: "{{ host }}"
          tls:
            status: "{{ status }}"
            certificate:
              type: "{{ type }}"
              location: "{{ location }}"
        logging:
          logLevel: "{{ logLevel }}"
          auditLogStatus: "{{ auditLogStatus }}"
        statusDetails:
          - type: "{{ type }}"
            code: "{{ code }}"
            description: "{{ description }}"
            timestamp: "{{ timestamp }}"
            correlationId: "{{ correlationId }}"
        notificationsList:
          - "{{ notificationsList }}"
        garbageCollection:
          enabled: {{ enabled }}
          schedule: "{{ schedule }}"
        registrySyncResult:
          syncTrigger: "{{ syncTrigger }}"
          syncState: "{{ syncState }}"
          lastSyncStartTime: "{{ lastSyncStartTime }}"
          lastSyncEndTime: "{{ lastSyncEndTime }}"
          lastSuccessfulSyncEndTime: "{{ lastSuccessfulSyncEndTime }}"
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

Updates a connected registry with the specified parameters.

```sql
UPDATE azure.containerregistry.connected_registries
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND connected_registry_name = '{{ connected_registry_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Deletes a connected registry from a container registry.

```sql
DELETE FROM azure.containerregistry.connected_registries
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND registry_name = '{{ registry_name }}' --required
AND connected_registry_name = '{{ connected_registry_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="deactivate"
    values={[
        { label: 'deactivate', value: 'deactivate' },
        { label: 'resync', value: 'resync' }
    ]}
>
<TabItem value="deactivate">

Deactivates the connected registry instance.

```sql
EXEC azure.containerregistry.connected_registries.deactivate 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@connected_registry_name='{{ connected_registry_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resync">

Resync the connected registry instance.

```sql
EXEC azure.containerregistry.connected_registries.resync 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@connected_registry_name='{{ connected_registry_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
