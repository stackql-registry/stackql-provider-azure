--- 
title: database_migrations_mongo_to_cosmos_dbv_core_mongo
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_mongo_to_cosmos_dbv_core_mongo
  - datamigration
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

Creates, updates, deletes, gets or lists a <code>database_migrations_mongo_to_cosmos_dbv_core_mongo</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_migrations_mongo_to_cosmos_dbv_core_mongo" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datamigration.database_migrations_mongo_to_cosmos_dbv_core_mongo" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_for_scope', value: 'get_for_scope' }
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
    <td><CopyableCode code="collectionList" /></td>
    <td><code>array</code></td>
    <td>List of Mongo Collections to be migrated.</td>
</tr>
<tr>
    <td><CopyableCode code="endedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Database migration end time.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Required. MongoToCosmosDbMongo.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationFailureError" /></td>
    <td><code>object</code></td>
    <td>Error details in case of migration failure.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationOperationId" /></td>
    <td><code>string</code></td>
    <td>ID for current migration operation.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationService" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the Migration Service.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationStatus" /></td>
    <td><code>string</code></td>
    <td>Migration status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>string</code></td>
    <td>Error message for migration provisioning failure, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of migration. ProvisioningState as Succeeded implies that validations have been performed and migration has started. Known values are: "Provisioning", "Updating", "Succeeded", "Failed", and "Canceled". (Provisioning, Updating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceMongoConnection" /></td>
    <td><code>object</code></td>
    <td>Source Mongo connection details.</td>
</tr>
<tr>
    <td><CopyableCode code="startedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Database migration start time.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetMongoConnection" /></td>
    <td><code>object</code></td>
    <td>Target Cosmos DB Mongo connection details.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_for_scope">

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
    <td><CopyableCode code="collectionList" /></td>
    <td><code>array</code></td>
    <td>List of Mongo Collections to be migrated.</td>
</tr>
<tr>
    <td><CopyableCode code="endedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Database migration end time.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Required. MongoToCosmosDbMongo.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationFailureError" /></td>
    <td><code>object</code></td>
    <td>Error details in case of migration failure.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationOperationId" /></td>
    <td><code>string</code></td>
    <td>ID for current migration operation.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationService" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the Migration Service.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationStatus" /></td>
    <td><code>string</code></td>
    <td>Migration status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningError" /></td>
    <td><code>string</code></td>
    <td>Error message for migration provisioning failure, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of migration. ProvisioningState as Succeeded implies that validations have been performed and migration has started. Known values are: "Provisioning", "Updating", "Succeeded", "Failed", and "Canceled". (Provisioning, Updating, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceMongoConnection" /></td>
    <td><code>object</code></td>
    <td>Source Mongo connection details.</td>
</tr>
<tr>
    <td><CopyableCode code="startedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Database migration start time.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetMongoConnection" /></td>
    <td><code>object</code></td>
    <td>Target Cosmos DB Mongo connection details.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_resource_name"><code>target_resource_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Database Migration resource.</td>
</tr>
<tr>
    <td><a href="#get_for_scope"><CopyableCode code="get_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_resource_name"><code>target_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Database Migration resources for the scope.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_resource_name"><code>target_resource_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update Database Migration resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-target_resource_name"><code>target_resource_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete Database Migration resource.</td>
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
<tr id="parameter-migration_name">
    <td><CopyableCode code="migration_name" /></td>
    <td><code>string</code></td>
    <td>Name of the migration. Required.</td>
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
<tr id="parameter-target_resource_name">
    <td><CopyableCode code="target_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the target resource/account. Required.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Optional force delete boolean. If this is provided as true, migration will be deleted even if active. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_for_scope', value: 'get_for_scope' }
    ]}
>
<TabItem value="get">

Get Database Migration resource.

```sql
SELECT
id,
name,
collectionList,
endedOn,
kind,
migrationFailureError,
migrationOperationId,
migrationService,
migrationStatus,
provisioningError,
provisioningState,
scope,
sourceMongoConnection,
startedOn,
systemData,
targetMongoConnection,
type
FROM azure.datamigration.database_migrations_mongo_to_cosmos_dbv_core_mongo
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND target_resource_name = '{{ target_resource_name }}' -- required
AND migration_name = '{{ migration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_for_scope">

Get Database Migration resources for the scope.

```sql
SELECT
id,
name,
collectionList,
endedOn,
kind,
migrationFailureError,
migrationOperationId,
migrationService,
migrationStatus,
provisioningError,
provisioningState,
scope,
sourceMongoConnection,
startedOn,
systemData,
targetMongoConnection,
type
FROM azure.datamigration.database_migrations_mongo_to_cosmos_dbv_core_mongo
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND target_resource_name = '{{ target_resource_name }}' -- required
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

Create or Update Database Migration resource.

```sql
INSERT INTO azure.datamigration.database_migrations_mongo_to_cosmos_dbv_core_mongo (
properties,
resource_group_name,
target_resource_name,
migration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ target_resource_name }}',
'{{ migration_name }}',
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
- name: database_migrations_mongo_to_cosmos_dbv_core_mongo
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the database_migrations_mongo_to_cosmos_dbv_core_mongo resource.
    - name: target_resource_name
      value: "{{ target_resource_name }}"
      description: Required parameter for the database_migrations_mongo_to_cosmos_dbv_core_mongo resource.
    - name: migration_name
      value: "{{ migration_name }}"
      description: Required parameter for the database_migrations_mongo_to_cosmos_dbv_core_mongo resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the database_migrations_mongo_to_cosmos_dbv_core_mongo resource.
    - name: properties
      description: |
        Database Migration Resource properties for CosmosDb for Mongo.
      value:
        kind: "{{ kind }}"
        scope: "{{ scope }}"
        provisioningState: "{{ provisioningState }}"
        migrationStatus: "{{ migrationStatus }}"
        startedOn: "{{ startedOn }}"
        endedOn: "{{ endedOn }}"
        migrationService: "{{ migrationService }}"
        migrationOperationId: "{{ migrationOperationId }}"
        migrationFailureError:
          code: "{{ code }}"
          message: "{{ message }}"
        provisioningError: "{{ provisioningError }}"
        sourceMongoConnection:
          host: "{{ host }}"
          port: {{ port }}
          userName: "{{ userName }}"
          password: "{{ password }}"
          useSsl: {{ useSsl }}
          connectionString: "{{ connectionString }}"
        targetMongoConnection:
          host: "{{ host }}"
          port: {{ port }}
          userName: "{{ userName }}"
          password: "{{ password }}"
          useSsl: {{ useSsl }}
          connectionString: "{{ connectionString }}"
        collectionList:
          - sourceDatabase: "{{ sourceDatabase }}"
            sourceCollection: "{{ sourceCollection }}"
            targetDatabase: "{{ targetDatabase }}"
            targetCollection: "{{ targetCollection }}"
            migrationProgressDetails:
              migrationStatus: "{{ migrationStatus }}"
              migrationError: "{{ migrationError }}"
              sourceDocumentCount: {{ sourceDocumentCount }}
              processedDocumentCount: {{ processedDocumentCount }}
              durationInSeconds: {{ durationInSeconds }}
`}</CodeBlock>

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

Delete Database Migration resource.

```sql
DELETE FROM azure.datamigration.database_migrations_mongo_to_cosmos_dbv_core_mongo
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND target_resource_name = '{{ target_resource_name }}' --required
AND migration_name = '{{ migration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
