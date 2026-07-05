--- 
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
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

Creates, updates, deletes, gets or lists a <code>catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="catalogs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.catalogs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' }
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
    <td><CopyableCode code="adoGit" /></td>
    <td><code>object</code></td>
    <td>Properties for an Azure DevOps catalog type.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>The connection state of the catalog. Known values are: "Connected" and "Disconnected".</td>
</tr>
<tr>
    <td><CopyableCode code="gitHub" /></td>
    <td><code>object</code></td>
    <td>Properties for a GitHub catalog type.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the catalog was last connected.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncStats" /></td>
    <td><code>object</code></td>
    <td>Stats of the latest synchronization.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the catalog was last synced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="syncState" /></td>
    <td><code>string</code></td>
    <td>The synchronization state of the catalog. Known values are: "Succeeded", "InProgress", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="syncType" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of sync that is configured for the catalog. Known values are: "Manual" and "Scheduled".</td>
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
<TabItem value="list_by_dev_center">

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
    <td><CopyableCode code="adoGit" /></td>
    <td><code>object</code></td>
    <td>Properties for an Azure DevOps catalog type.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionState" /></td>
    <td><code>string</code></td>
    <td>The connection state of the catalog. Known values are: "Connected" and "Disconnected".</td>
</tr>
<tr>
    <td><CopyableCode code="gitHub" /></td>
    <td><code>object</code></td>
    <td>Properties for a GitHub catalog type.</td>
</tr>
<tr>
    <td><CopyableCode code="lastConnectionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the catalog was last connected.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncStats" /></td>
    <td><code>object</code></td>
    <td>Stats of the latest synchronization.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSyncTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the catalog was last synced.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="syncState" /></td>
    <td><code>string</code></td>
    <td>The synchronization state of the catalog. Known values are: "Succeeded", "InProgress", "Failed", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="syncType" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of sync that is configured for the catalog. Known values are: "Manual" and "Scheduled".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a catalog.</td>
</tr>
<tr>
    <td><a href="#list_by_dev_center"><CopyableCode code="list_by_dev_center" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists catalogs for a devcenter.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a catalog.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Partially updates a catalog.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a catalog.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a catalog resource.</td>
</tr>
<tr>
    <td><a href="#get_sync_error_details"><CopyableCode code="get_sync_error_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets catalog synchronization error details.</td>
</tr>
<tr>
    <td><a href="#sync"><CopyableCode code="sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Syncs templates for a template source.</td>
</tr>
<tr>
    <td><a href="#connect"><CopyableCode code="connect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Connects a catalog to enable syncing.</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Catalog. Required.</td>
</tr>
<tr id="parameter-dev_center_name">
    <td><CopyableCode code="dev_center_name" /></td>
    <td><code>string</code></td>
    <td>The name of the devcenter. Required.</td>
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
        { label: 'list_by_dev_center', value: 'list_by_dev_center' }
    ]}
>
<TabItem value="get">

Gets a catalog.

```sql
SELECT
id,
name,
adoGit,
connectionState,
gitHub,
lastConnectionTime,
lastSyncStats,
lastSyncTime,
provisioningState,
syncState,
syncType,
systemData,
tags,
type
FROM azure.devcenter.catalogs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND catalog_name = '{{ catalog_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_dev_center">

Lists catalogs for a devcenter.

```sql
SELECT
id,
name,
adoGit,
connectionState,
gitHub,
lastConnectionTime,
lastSyncStats,
lastSyncTime,
provisioningState,
syncState,
syncType,
systemData,
tags,
type
FROM azure.devcenter.catalogs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
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

Creates or updates a catalog.

```sql
INSERT INTO azure.devcenter.catalogs (
properties,
resource_group_name,
dev_center_name,
catalog_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ dev_center_name }}',
'{{ catalog_name }}',
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
- name: catalogs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the catalogs resource.
    - name: dev_center_name
      value: "{{ dev_center_name }}"
      description: Required parameter for the catalogs resource.
    - name: catalog_name
      value: "{{ catalog_name }}"
      description: Required parameter for the catalogs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the catalogs resource.
    - name: properties
      value:
        gitHub:
          uri: "{{ uri }}"
          branch: "{{ branch }}"
          secretIdentifier: "{{ secretIdentifier }}"
          path: "{{ path }}"
        adoGit:
          uri: "{{ uri }}"
          branch: "{{ branch }}"
          secretIdentifier: "{{ secretIdentifier }}"
          path: "{{ path }}"
        syncType: "{{ syncType }}"
        tags: "{{ tags }}"
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

Partially updates a catalog.

```sql
UPDATE azure.devcenter.catalogs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a catalog.

```sql
REPLACE azure.devcenter.catalogs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
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

Deletes a catalog resource.

```sql
DELETE FROM azure.devcenter.catalogs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND catalog_name = '{{ catalog_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_sync_error_details"
    values={[
        { label: 'get_sync_error_details', value: 'get_sync_error_details' },
        { label: 'sync', value: 'sync' },
        { label: 'connect', value: 'connect' }
    ]}
>
<TabItem value="get_sync_error_details">

Gets catalog synchronization error details.

```sql
EXEC azure.devcenter.catalogs.get_sync_error_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@dev_center_name='{{ dev_center_name }}' --required, 
@catalog_name='{{ catalog_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="sync">

Syncs templates for a template source.

```sql
EXEC azure.devcenter.catalogs.sync 
@resource_group_name='{{ resource_group_name }}' --required, 
@dev_center_name='{{ dev_center_name }}' --required, 
@catalog_name='{{ catalog_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="connect">

Connects a catalog to enable syncing.

```sql
EXEC azure.devcenter.catalogs.connect 
@resource_group_name='{{ resource_group_name }}' --required, 
@dev_center_name='{{ dev_center_name }}' --required, 
@catalog_name='{{ catalog_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
