--- 
title: elastic_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pools
  - sql
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

Creates, updates, deletes, gets or lists an <code>elastic_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="elastic_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.elastic_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
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
    <td><CopyableCode code="autoPauseDelay" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes after which elastic pool is automatically paused. A value of -1 means that automatic pause is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability zone the pool's primary replica is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the elastic pool (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityReplicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of secondary replicas associated with the Business Critical, Premium, or Hyperscale edition elastic pool that are used to provide high availability. Applicable only to Hyperscale elastic pools.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of elastic pool. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this elastic pool. Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Maintenance configuration id assigned to the elastic pool. This configuration defines the period when the maintenance updates will will occur.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The storage limit for the database elastic pool in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="minCapacity" /></td>
    <td><code>number</code></td>
    <td>Minimal capacity that serverless pool will not shrink below, if not paused.</td>
</tr>
<tr>
    <td><CopyableCode code="perDatabaseSettings" /></td>
    <td><code>object</code></td>
    <td>The per database settings for the elastic pool.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredEnclaveType" /></td>
    <td><code>string</code></td>
    <td>Type of enclave requested on the elastic pool. Known values are: "Default" and "VBS". (Default, VBS)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The elastic pool SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or the following command: .. code-block:: azurecli az sql elastic-pool list-editions -l -o table</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the elastic pool. Known values are: "Creating", "Ready", and "Disabled". (Creating, Ready, Disabled)</td>
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
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_server">

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
    <td><CopyableCode code="autoPauseDelay" /></td>
    <td><code>integer</code></td>
    <td>Time in minutes after which elastic pool is automatically paused. A value of -1 means that automatic pause is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>string</code></td>
    <td>Specifies the availability zone the pool's primary replica is pinned to. Known values are: "NoPreference", "1", "2", and "3". (NoPreference, 1, 2, 3)</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the elastic pool (ISO8601 format).</td>
</tr>
<tr>
    <td><CopyableCode code="highAvailabilityReplicaCount" /></td>
    <td><code>integer</code></td>
    <td>The number of secondary replicas associated with the Business Critical, Premium, or Hyperscale edition elastic pool that are used to provide high availability. Applicable only to Hyperscale elastic pools.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of elastic pool. This is metadata used for the Azure portal experience.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseType" /></td>
    <td><code>string</code></td>
    <td>The license type to apply for this elastic pool. Known values are: "LicenseIncluded" and "BasePrice". (LicenseIncluded, BasePrice)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceConfigurationId" /></td>
    <td><code>string</code></td>
    <td>Maintenance configuration id assigned to the elastic pool. This configuration defines the period when the maintenance updates will will occur.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer</code></td>
    <td>The storage limit for the database elastic pool in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="minCapacity" /></td>
    <td><code>number</code></td>
    <td>Minimal capacity that serverless pool will not shrink below, if not paused.</td>
</tr>
<tr>
    <td><CopyableCode code="perDatabaseSettings" /></td>
    <td><code>object</code></td>
    <td>The per database settings for the elastic pool.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredEnclaveType" /></td>
    <td><code>string</code></td>
    <td>Type of enclave requested on the elastic pool. Known values are: "Default" and "VBS". (Default, VBS)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The elastic pool SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or the following command: .. code-block:: azurecli az sql elastic-pool list-editions -l -o table</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the elastic pool. Known values are: "Creating", "Ready", and "Disabled". (Creating, Ready, Disabled)</td>
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
    <td><CopyableCode code="zoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an elastic pool.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Gets all elastic pools in a server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an elastic pool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an elastic pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an elastic pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an elastic pool.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-elastic_pool_name"><code>elastic_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Failovers an elastic pool.</td>
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
<tr id="parameter-elastic_pool_name">
    <td><CopyableCode code="elastic_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the elastic pool. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>The number of elements in the collection to skip. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Gets an elastic pool.

```sql
SELECT
id,
name,
autoPauseDelay,
availabilityZone,
creationDate,
highAvailabilityReplicaCount,
kind,
licenseType,
location,
maintenanceConfigurationId,
maxSizeBytes,
minCapacity,
perDatabaseSettings,
preferredEnclaveType,
sku,
state,
systemData,
tags,
type,
zoneRedundant
FROM azure.sql.elastic_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND elastic_pool_name = '{{ elastic_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

Gets all elastic pools in a server.

```sql
SELECT
id,
name,
autoPauseDelay,
availabilityZone,
creationDate,
highAvailabilityReplicaCount,
kind,
licenseType,
location,
maintenanceConfigurationId,
maxSizeBytes,
minCapacity,
perDatabaseSettings,
preferredEnclaveType,
sku,
state,
systemData,
tags,
type,
zoneRedundant
FROM azure.sql.elastic_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skip = '{{ $skip }}'
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

Creates or updates an elastic pool.

```sql
INSERT INTO azure.sql.elastic_pools (
tags,
location,
properties,
sku,
resource_group_name,
server_name,
elastic_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ elastic_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: elastic_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the elastic_pools resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the elastic_pools resource.
    - name: elastic_pool_name
      value: "{{ elastic_pool_name }}"
      description: Required parameter for the elastic_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the elastic_pools resource.
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
        Resource properties.
      value:
        state: "{{ state }}"
        creationDate: "{{ creationDate }}"
        maxSizeBytes: {{ maxSizeBytes }}
        minCapacity: {{ minCapacity }}
        perDatabaseSettings:
          minCapacity: {{ minCapacity }}
          maxCapacity: {{ maxCapacity }}
          autoPauseDelay: {{ autoPauseDelay }}
        zoneRedundant: {{ zoneRedundant }}
        licenseType: "{{ licenseType }}"
        maintenanceConfigurationId: "{{ maintenanceConfigurationId }}"
        highAvailabilityReplicaCount: {{ highAvailabilityReplicaCount }}
        autoPauseDelay: {{ autoPauseDelay }}
        preferredEnclaveType: "{{ preferredEnclaveType }}"
        availabilityZone: "{{ availabilityZone }}"
    - name: sku
      description: |
        The elastic pool SKU. The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the \`Capabilities_ListByLocation\` REST API or the following command: .. code-block:: azurecli az sql elastic-pool list-editions -l -o table
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
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

Updates an elastic pool.

```sql
UPDATE azure.sql.elastic_pools
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND elastic_pool_name = '{{ elastic_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
sku,
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

Creates or updates an elastic pool.

```sql
REPLACE azure.sql.elastic_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND elastic_pool_name = '{{ elastic_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
kind,
location,
properties,
sku,
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

Deletes an elastic pool.

```sql
DELETE FROM azure.sql.elastic_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND elastic_pool_name = '{{ elastic_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="failover"
    values={[
        { label: 'failover', value: 'failover' }
    ]}
>
<TabItem value="failover">

Failovers an elastic pool.

```sql
EXEC azure.sql.elastic_pools.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@elastic_pool_name='{{ elastic_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
