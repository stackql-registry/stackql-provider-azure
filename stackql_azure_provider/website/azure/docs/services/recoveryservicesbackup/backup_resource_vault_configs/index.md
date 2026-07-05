--- 
title: backup_resource_vault_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_resource_vault_configs
  - recoveryservicesbackup
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

Creates, updates, deletes, gets or lists a <code>backup_resource_vault_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_resource_vault_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesbackup.backup_resource_vault_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Optional ETag.</td>
</tr>
<tr>
    <td><CopyableCode code="enhancedSecurityState" /></td>
    <td><code>string</code></td>
    <td>Enabled or Disabled. Known values are: "Invalid", "Enabled", and "Disabled". (Invalid, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="isSoftDeleteFeatureStateEditable" /></td>
    <td><code>boolean</code></td>
    <td>This flag is no longer in use. Please use 'softDeleteFeatureState' to set the soft delete state for the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuardOperationRequests" /></td>
    <td><code>array</code></td>
    <td>ResourceGuard Operation Requests.</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteFeatureState" /></td>
    <td><code>string</code></td>
    <td>Soft Delete feature state. Known values are: "Invalid", "Enabled", "Disabled", and "AlwaysON". (Invalid, Enabled, Disabled, AlwaysON)</td>
</tr>
<tr>
    <td><CopyableCode code="softDeleteRetentionPeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Soft delete retention period in days.</td>
</tr>
<tr>
    <td><CopyableCode code="storageModelType" /></td>
    <td><code>string</code></td>
    <td>Storage type. Known values are: "Invalid", "GeoRedundant", "LocallyRedundant", "ZoneRedundant", and "ReadAccessGeoZoneRedundant". (Invalid, GeoRedundant, LocallyRedundant, ZoneRedundant, ReadAccessGeoZoneRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="storageType" /></td>
    <td><code>string</code></td>
    <td>Storage type. Known values are: "Invalid", "GeoRedundant", "LocallyRedundant", "ZoneRedundant", and "ReadAccessGeoZoneRedundant". (Invalid, GeoRedundant, LocallyRedundant, ZoneRedundant, ReadAccessGeoZoneRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="storageTypeState" /></td>
    <td><code>string</code></td>
    <td>Locked or Unlocked. Once a machine is registered against a resource, the storageTypeState is always Locked. Known values are: "Invalid", "Locked", and "Unlocked". (Invalid, Locked, Unlocked)</td>
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
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetches resource vault config.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Updates vault security config.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-x-ms-authorization-auxiliary"><code>x-ms-authorization-auxiliary</code></a></td>
    <td>Updates vault security config.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VaultResource. Required.</td>
</tr>
<tr id="parameter-x-ms-authorization-auxiliary">
    <td><CopyableCode code="x-ms-authorization-auxiliary" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Fetches resource vault config.

```sql
SELECT
id,
name,
eTag,
enhancedSecurityState,
isSoftDeleteFeatureStateEditable,
location,
resourceGuardOperationRequests,
softDeleteFeatureState,
softDeleteRetentionPeriodInDays,
storageModelType,
storageType,
storageTypeState,
systemData,
tags,
type
FROM azure.recoveryservicesbackup.backup_resource_vault_configs
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
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

Updates vault security config.

```sql
UPDATE azure.recoveryservicesbackup.backup_resource_vault_configs
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
eTag = '{{ eTag }}'
WHERE 
vault_name = '{{ vault_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND x-ms-authorization-auxiliary = '{{ x-ms-authorization-auxiliary}}'
RETURNING
id,
name,
eTag,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="put">

Updates vault security config.

```sql
EXEC azure.recoveryservicesbackup.backup_resource_vault_configs.put 
@vault_name='{{ vault_name }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@x-ms-authorization-auxiliary='{{ x-ms-authorization-auxiliary }}' 
@@json=
'{
"properties": "{{ properties }}", 
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"eTag": "{{ eTag }}"
}'
;
```
</TabItem>
</Tabs>
