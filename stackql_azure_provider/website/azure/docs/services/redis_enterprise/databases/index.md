--- 
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - redis_enterprise
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="databases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.redis_enterprise.databases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cluster', value: 'list_by_cluster' }
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
    <td><CopyableCode code="accessKeysAuthentication" /></td>
    <td><code>string</code></td>
    <td>This property can be Enabled/Disabled to allow or deny access with the current access keys. Can be updated even after database is created. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="clientProtocol" /></td>
    <td><code>string</code></td>
    <td>Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted. Known values are: "Encrypted" and "Plaintext". (Encrypted, Plaintext)</td>
</tr>
<tr>
    <td><CopyableCode code="clusteringPolicy" /></td>
    <td><code>string</code></td>
    <td>Clustering policy - default is OSSCluster. This property can be updated only if the current value is NoCluster. If the value is OSSCluster or EnterpriseCluster, it cannot be updated without deleting the database. Known values are: "EnterpriseCluster", "OSSCluster", and "NoCluster". (EnterpriseCluster, OSSCluster, NoCluster)</td>
</tr>
<tr>
    <td><CopyableCode code="deferUpgrade" /></td>
    <td><code>string</code></td>
    <td>Option to defer upgrade when newest version is released - default is NotDeferred. Learn more: `https://aka.ms/redisversionupgrade `_. Known values are: "Deferred" and "NotDeferred". (Deferred, NotDeferred)</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Redis eviction policy - default is VolatileLRU. Known values are: "AllKeysLFU", "AllKeysLRU", "AllKeysRandom", "VolatileLRU", "VolatileLFU", "VolatileTTL", "VolatileRandom", and "NoEviction". (AllKeysLFU, AllKeysLRU, AllKeysRandom, VolatileLRU, VolatileLFU, VolatileTTL, VolatileRandom, NoEviction)</td>
</tr>
<tr>
    <td><CopyableCode code="geoReplication" /></td>
    <td><code>object</code></td>
    <td>Optional set of properties to configure geo replication for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>Optional set of redis modules to enable in this database - modules can only be added at creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="notifyKeyspaceEvents" /></td>
    <td><code>string</code></td>
    <td>Specifies which keyspace events should trigger notifications. Default is an empty string, meaning this feature is disabled. When enabled, at least 'K' (keyspace events) or 'E' (keyevent events) must be present. For example, 'AKE' enables all standard events. See `https://redis.io/docs/latest/develop/use/keyspace-notifications/ `_ for the complete list of event types.</td>
</tr>
<tr>
    <td><CopyableCode code="persistence" /></td>
    <td><code>object</code></td>
    <td>Persistence settings.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>TCP port of the database endpoint. Specified at create time. Defaults to an available port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning status of the database. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Redis the database is running on, e.g. '6.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Current resource status of the database. Known values are: "Running", "Creating", "CreateFailed", "Updating", "UpdateFailed", "Deleting", "DeleteFailed", "Enabling", "EnableFailed", "Disabling", "DisableFailed", "Disabled", "Scaling", "ScalingFailed", and "Moving". (Running, Creating, CreateFailed, Updating, UpdateFailed, Deleting, DeleteFailed, Enabling, EnableFailed, Disabling, DisableFailed, Disabled, Scaling, ScalingFailed, Moving)</td>
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
<TabItem value="list_by_cluster">

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
    <td><CopyableCode code="accessKeysAuthentication" /></td>
    <td><code>string</code></td>
    <td>This property can be Enabled/Disabled to allow or deny access with the current access keys. Can be updated even after database is created. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="clientProtocol" /></td>
    <td><code>string</code></td>
    <td>Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted. Known values are: "Encrypted" and "Plaintext". (Encrypted, Plaintext)</td>
</tr>
<tr>
    <td><CopyableCode code="clusteringPolicy" /></td>
    <td><code>string</code></td>
    <td>Clustering policy - default is OSSCluster. This property can be updated only if the current value is NoCluster. If the value is OSSCluster or EnterpriseCluster, it cannot be updated without deleting the database. Known values are: "EnterpriseCluster", "OSSCluster", and "NoCluster". (EnterpriseCluster, OSSCluster, NoCluster)</td>
</tr>
<tr>
    <td><CopyableCode code="deferUpgrade" /></td>
    <td><code>string</code></td>
    <td>Option to defer upgrade when newest version is released - default is NotDeferred. Learn more: `https://aka.ms/redisversionupgrade `_. Known values are: "Deferred" and "NotDeferred". (Deferred, NotDeferred)</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>Redis eviction policy - default is VolatileLRU. Known values are: "AllKeysLFU", "AllKeysLRU", "AllKeysRandom", "VolatileLRU", "VolatileLFU", "VolatileTTL", "VolatileRandom", and "NoEviction". (AllKeysLFU, AllKeysLRU, AllKeysRandom, VolatileLRU, VolatileLFU, VolatileTTL, VolatileRandom, NoEviction)</td>
</tr>
<tr>
    <td><CopyableCode code="geoReplication" /></td>
    <td><code>object</code></td>
    <td>Optional set of properties to configure geo replication for this database.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>Optional set of redis modules to enable in this database - modules can only be added at creation time.</td>
</tr>
<tr>
    <td><CopyableCode code="notifyKeyspaceEvents" /></td>
    <td><code>string</code></td>
    <td>Specifies which keyspace events should trigger notifications. Default is an empty string, meaning this feature is disabled. When enabled, at least 'K' (keyspace events) or 'E' (keyevent events) must be present. For example, 'AKE' enables all standard events. See `https://redis.io/docs/latest/develop/use/keyspace-notifications/ `_ for the complete list of event types.</td>
</tr>
<tr>
    <td><CopyableCode code="persistence" /></td>
    <td><code>object</code></td>
    <td>Persistence settings.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>TCP port of the database endpoint. Specified at create time. Defaults to an available port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning status of the database. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="redisVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Redis the database is running on, e.g. '6.0'.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Current resource status of the database. Known values are: "Running", "Creating", "CreateFailed", "Updating", "UpdateFailed", "Deleting", "DeleteFailed", "Enabling", "EnableFailed", "Disabling", "DisableFailed", "Disabled", "Scaling", "ScalingFailed", and "Moving". (Running, Creating, CreateFailed, Updating, UpdateFailed, Deleting, DeleteFailed, Enabling, EnableFailed, Disabling, DisableFailed, Disabled, Scaling, ScalingFailed, Moving)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a database in a Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_cluster"><CopyableCode code="list_by_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all databases in the specified Redis Enterprise cluster.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a database.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a database.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a single database.</td>
</tr>
<tr>
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the access keys for the Redis Enterprise database.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyType"><code>keyType</code></a></td>
    <td></td>
    <td>Regenerates the Redis Enterprise database's access keys.</td>
</tr>
<tr>
    <td><a href="#import_method"><CopyableCode code="import_method" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sasUris"><code>sasUris</code></a></td>
    <td></td>
    <td>Imports database files to target database.</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sasUri"><code>sasUri</code></a></td>
    <td></td>
    <td>Exports a database file from target database.</td>
</tr>
<tr>
    <td><a href="#force_unlink"><CopyableCode code="force_unlink" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-ids"><code>ids</code></a></td>
    <td></td>
    <td>Forcibly removes the link to the specified database resource.</td>
</tr>
<tr>
    <td><a href="#force_link_to_replication_group"><CopyableCode code="force_link_to_replication_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-geoReplication"><code>geoReplication</code></a></td>
    <td></td>
    <td>Forcibly recreates an existing database on the specified cluster, and rejoins it to an existing replication group. **IMPORTANT NOTE:** All data in this database will be discarded, and the database will temporarily be unavailable while rejoining the replication group.</td>
</tr>
<tr>
    <td><a href="#flush"><CopyableCode code="flush" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Flushes all the keys in this database and also from its linked databases.</td>
</tr>
<tr>
    <td><a href="#upgrade_db_redis_version"><CopyableCode code="upgrade_db_redis_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upgrades the database Redis version to the latest available.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Redis Enterprise cluster. Name must be 1-60 characters long. Allowed characters(A-Z, a-z, 0-9) and hyphen(-). There can be no leading nor trailing nor consecutive hyphens. Required.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Redis Enterprise database. Required.</td>
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
        { label: 'list_by_cluster', value: 'list_by_cluster' }
    ]}
>
<TabItem value="get">

Gets information about a database in a Redis Enterprise cluster.

```sql
SELECT
id,
name,
accessKeysAuthentication,
clientProtocol,
clusteringPolicy,
deferUpgrade,
evictionPolicy,
geoReplication,
modules,
notifyKeyspaceEvents,
persistence,
port,
provisioningState,
redisVersion,
resourceState,
systemData,
type
FROM azure.redis_enterprise.databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cluster">

Gets all databases in the specified Redis Enterprise cluster.

```sql
SELECT
id,
name,
accessKeysAuthentication,
clientProtocol,
clusteringPolicy,
deferUpgrade,
evictionPolicy,
geoReplication,
modules,
notifyKeyspaceEvents,
persistence,
port,
provisioningState,
redisVersion,
resourceState,
systemData,
type
FROM azure.redis_enterprise.databases
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates a database.

```sql
INSERT INTO azure.redis_enterprise.databases (
properties,
resource_group_name,
cluster_name,
database_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ database_name }}',
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
- name: databases
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the databases resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the databases resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the databases resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the databases resource.
    - name: properties
      description: |
        Other properties of the database.
      value:
        clientProtocol: "{{ clientProtocol }}"
        port: {{ port }}
        provisioningState: "{{ provisioningState }}"
        resourceState: "{{ resourceState }}"
        clusteringPolicy: "{{ clusteringPolicy }}"
        evictionPolicy: "{{ evictionPolicy }}"
        persistence:
          aofEnabled: {{ aofEnabled }}
          rdbEnabled: {{ rdbEnabled }}
          aofFrequency: "{{ aofFrequency }}"
          rdbFrequency: "{{ rdbFrequency }}"
        modules:
          - name: "{{ name }}"
            args: "{{ args }}"
            version: "{{ version }}"
        geoReplication:
          groupNickname: "{{ groupNickname }}"
          linkedDatabases:
            - id: "{{ id }}"
              state: "{{ state }}"
        redisVersion: "{{ redisVersion }}"
        deferUpgrade: "{{ deferUpgrade }}"
        accessKeysAuthentication: "{{ accessKeysAuthentication }}"
        notifyKeyspaceEvents: "{{ notifyKeyspaceEvents }}"
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

Updates a database.

```sql
UPDATE azure.redis_enterprise.databases
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND database_name = '{{ database_name }}' --required
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

Deletes a single database.

```sql
DELETE FROM azure.redis_enterprise.databases
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND database_name = '{{ database_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'import_method', value: 'import_method' },
        { label: 'export', value: 'export' },
        { label: 'force_unlink', value: 'force_unlink' },
        { label: 'force_link_to_replication_group', value: 'force_link_to_replication_group' },
        { label: 'flush', value: 'flush' },
        { label: 'upgrade_db_redis_version', value: 'upgrade_db_redis_version' }
    ]}
>
<TabItem value="list_keys">

Retrieves the access keys for the Redis Enterprise database.

```sql
EXEC azure.redis_enterprise.databases.list_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerates the Redis Enterprise database's access keys.

```sql
EXEC azure.redis_enterprise.databases.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
<TabItem value="import_method">

Imports database files to target database.

```sql
EXEC azure.redis_enterprise.databases.import_method 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sasUris": "{{ sasUris }}"
}'
;
```
</TabItem>
<TabItem value="export">

Exports a database file from target database.

```sql
EXEC azure.redis_enterprise.databases.export 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sasUri": "{{ sasUri }}"
}'
;
```
</TabItem>
<TabItem value="force_unlink">

Forcibly removes the link to the specified database resource.

```sql
EXEC azure.redis_enterprise.databases.force_unlink 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="force_link_to_replication_group">

Forcibly recreates an existing database on the specified cluster, and rejoins it to an existing replication group. **IMPORTANT NOTE:** All data in this database will be discarded, and the database will temporarily be unavailable while rejoining the replication group.

```sql
EXEC azure.redis_enterprise.databases.force_link_to_replication_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"geoReplication": "{{ geoReplication }}"
}'
;
```
</TabItem>
<TabItem value="flush">

Flushes all the keys in this database and also from its linked databases.

```sql
EXEC azure.redis_enterprise.databases.flush 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="upgrade_db_redis_version">

Upgrades the database Redis version to the latest available.

```sql
EXEC azure.redis_enterprise.databases.upgrade_db_redis_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@database_name='{{ database_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
