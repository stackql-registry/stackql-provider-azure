--- 
title: migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - migrations
  - postgresqlflexibleservers
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

Creates, updates, deletes, gets or lists a <code>migrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="migrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresqlflexibleservers.migrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_target_server', value: 'list_by_target_server' }
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
    <td><CopyableCode code="cancel" /></td>
    <td><code>string</code></td>
    <td>Indicates if cancel must be triggered for the entire migration. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="currentStatus" /></td>
    <td><code>object</code></td>
    <td>Current status of a migration.</td>
</tr>
<tr>
    <td><CopyableCode code="dbsToCancelMigrationOn" /></td>
    <td><code>array</code></td>
    <td>When you want to trigger cancel for specific databases set 'triggerCutover' to 'True' and the names of the specific databases in this array.</td>
</tr>
<tr>
    <td><CopyableCode code="dbsToMigrate" /></td>
    <td><code>array</code></td>
    <td>Names of databases to migrate.</td>
</tr>
<tr>
    <td><CopyableCode code="dbsToTriggerCutoverOn" /></td>
    <td><code>array</code></td>
    <td>When you want to trigger cutover for specific databases set 'triggerCutover' to 'True' and the names of the specific databases in this array.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="migrateRoles" /></td>
    <td><code>string</code></td>
    <td>Indicates if roles and permissions must be migrated. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationId" /></td>
    <td><code>string</code></td>
    <td>Identifier of a migration.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationInstanceResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the private endpoint migration instance.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationMode" /></td>
    <td><code>string</code></td>
    <td>Mode used to perform the migration: Online or Offline. Known values are: "Offline" and "Online". (Offline, Online)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationOption" /></td>
    <td><code>string</code></td>
    <td>Supported option for a migration. Known values are: "Validate", "Migrate", and "ValidateAndMigrate". (Validate, Migrate, ValidateAndMigrate)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationWindowEndTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time (UTC) for migration window.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationWindowStartTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time (UTC) for migration window.</td>
</tr>
<tr>
    <td><CopyableCode code="overwriteDbsInTarget" /></td>
    <td><code>string</code></td>
    <td>Indicates if databases on the target server can be overwritten when already present. If set to 'False', when the migration workflow detects that the database already exists on the target server, it will wait for a confirmation. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="secretParameters" /></td>
    <td><code>object</code></td>
    <td>Migration secret parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="setupLogicalReplicationOnSourceDbIfNeeded" /></td>
    <td><code>string</code></td>
    <td>Indicates whether to setup logical replication on source server, if needed. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDbServerFullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name (FQDN) or IP address of the source server. This property is optional. When provided, the migration service will always use it to connect to the source server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDbServerMetadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of source database server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDbServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the source database server resource, when 'sourceType' is 'PostgreSQLSingleServer'. For other source types this must be set to ipaddress:port@username or hostname:port@username.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceType" /></td>
    <td><code>string</code></td>
    <td>Source server type used for the migration: ApsaraDB_RDS, AWS, AWS_AURORA, AWS_EC2, AWS_RDS, AzureVM, Crunchy_PostgreSQL, Digital_Ocean_Droplets, Digital_Ocean_PostgreSQL, EDB, EDB_Oracle_Server, EDB_PostgreSQL, GCP, GCP_AlloyDB, GCP_CloudSQL, GCP_Compute, Heroku_PostgreSQL, Huawei_Compute, Huawei_RDS, OnPremises, PostgreSQLCosmosDB, PostgreSQLFlexibleServer, PostgreSQLSingleServer, or Supabase_PostgreSQL. Known values are: "OnPremises", "AWS", "GCP", "AzureVM", "PostgreSQLSingleServer", "AWS_RDS", "AWS_AURORA", "AWS_EC2", "GCP_CloudSQL", "GCP_AlloyDB", "GCP_Compute", "EDB", "EDB_Oracle_Server", "EDB_PostgreSQL", "PostgreSQLFlexibleServer", "PostgreSQLCosmosDB", "Huawei_RDS", "Huawei_Compute", "Heroku_PostgreSQL", "Crunchy_PostgreSQL", "ApsaraDB_RDS", "Digital_Ocean_Droplets", "Digital_Ocean_PostgreSQL", and "Supabase_PostgreSQL". (OnPremises, AWS, GCP, AzureVM, PostgreSQLSingleServer, AWS_RDS, AWS_AURORA, AWS_EC2, GCP_CloudSQL, GCP_AlloyDB, GCP_Compute, EDB, EDB_Oracle_Server, EDB_PostgreSQL, PostgreSQLFlexibleServer, PostgreSQLCosmosDB, Huawei_RDS, Huawei_Compute, Heroku_PostgreSQL, Crunchy_PostgreSQL, ApsaraDB_RDS, Digital_Ocean_Droplets, Digital_Ocean_PostgreSQL, Supabase_PostgreSQL)</td>
</tr>
<tr>
    <td><CopyableCode code="sslMode" /></td>
    <td><code>string</code></td>
    <td>SSL mode used by a migration. Default SSL mode for 'PostgreSQLSingleServer' is 'VerifyFull'. Default SSL mode for other source types is 'Prefer'. Known values are: "Prefer", "Require", "VerifyCA", and "VerifyFull". (Prefer, Require, VerifyCA, VerifyFull)</td>
</tr>
<tr>
    <td><CopyableCode code="startDataMigration" /></td>
    <td><code>string</code></td>
    <td>Indicates if data migration must start right away. Known values are: "True" and "False". (True, False)</td>
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
    <td><CopyableCode code="targetDbServerFullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name (FQDN) or IP address of the target server. This property is optional. When provided, the migration service will always use it to connect to the target server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDbServerMetadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of target database server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDbServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the target database server resource.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerCutover" /></td>
    <td><code>string</code></td>
    <td>Indicates if cutover must be triggered for the entire migration. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_target_server">

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
    <td><CopyableCode code="cancel" /></td>
    <td><code>string</code></td>
    <td>Indicates if cancel must be triggered for the entire migration. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="currentStatus" /></td>
    <td><code>object</code></td>
    <td>Current status of a migration.</td>
</tr>
<tr>
    <td><CopyableCode code="dbsToCancelMigrationOn" /></td>
    <td><code>array</code></td>
    <td>When you want to trigger cancel for specific databases set 'triggerCutover' to 'True' and the names of the specific databases in this array.</td>
</tr>
<tr>
    <td><CopyableCode code="dbsToMigrate" /></td>
    <td><code>array</code></td>
    <td>Names of databases to migrate.</td>
</tr>
<tr>
    <td><CopyableCode code="dbsToTriggerCutoverOn" /></td>
    <td><code>array</code></td>
    <td>When you want to trigger cutover for specific databases set 'triggerCutover' to 'True' and the names of the specific databases in this array.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="migrateRoles" /></td>
    <td><code>string</code></td>
    <td>Indicates if roles and permissions must be migrated. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationId" /></td>
    <td><code>string</code></td>
    <td>Identifier of a migration.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationInstanceResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the private endpoint migration instance.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationMode" /></td>
    <td><code>string</code></td>
    <td>Mode used to perform the migration: Online or Offline. Known values are: "Offline" and "Online". (Offline, Online)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationOption" /></td>
    <td><code>string</code></td>
    <td>Supported option for a migration. Known values are: "Validate", "Migrate", and "ValidateAndMigrate". (Validate, Migrate, ValidateAndMigrate)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationWindowEndTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time (UTC) for migration window.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationWindowStartTimeInUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time (UTC) for migration window.</td>
</tr>
<tr>
    <td><CopyableCode code="overwriteDbsInTarget" /></td>
    <td><code>string</code></td>
    <td>Indicates if databases on the target server can be overwritten when already present. If set to 'False', when the migration workflow detects that the database already exists on the target server, it will wait for a confirmation. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="secretParameters" /></td>
    <td><code>object</code></td>
    <td>Migration secret parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="setupLogicalReplicationOnSourceDbIfNeeded" /></td>
    <td><code>string</code></td>
    <td>Indicates whether to setup logical replication on source server, if needed. Known values are: "True" and "False". (True, False)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDbServerFullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name (FQDN) or IP address of the source server. This property is optional. When provided, the migration service will always use it to connect to the source server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDbServerMetadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of source database server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceDbServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the source database server resource, when 'sourceType' is 'PostgreSQLSingleServer'. For other source types this must be set to ipaddress:port@username or hostname:port@username.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceType" /></td>
    <td><code>string</code></td>
    <td>Source server type used for the migration: ApsaraDB_RDS, AWS, AWS_AURORA, AWS_EC2, AWS_RDS, AzureVM, Crunchy_PostgreSQL, Digital_Ocean_Droplets, Digital_Ocean_PostgreSQL, EDB, EDB_Oracle_Server, EDB_PostgreSQL, GCP, GCP_AlloyDB, GCP_CloudSQL, GCP_Compute, Heroku_PostgreSQL, Huawei_Compute, Huawei_RDS, OnPremises, PostgreSQLCosmosDB, PostgreSQLFlexibleServer, PostgreSQLSingleServer, or Supabase_PostgreSQL. Known values are: "OnPremises", "AWS", "GCP", "AzureVM", "PostgreSQLSingleServer", "AWS_RDS", "AWS_AURORA", "AWS_EC2", "GCP_CloudSQL", "GCP_AlloyDB", "GCP_Compute", "EDB", "EDB_Oracle_Server", "EDB_PostgreSQL", "PostgreSQLFlexibleServer", "PostgreSQLCosmosDB", "Huawei_RDS", "Huawei_Compute", "Heroku_PostgreSQL", "Crunchy_PostgreSQL", "ApsaraDB_RDS", "Digital_Ocean_Droplets", "Digital_Ocean_PostgreSQL", and "Supabase_PostgreSQL". (OnPremises, AWS, GCP, AzureVM, PostgreSQLSingleServer, AWS_RDS, AWS_AURORA, AWS_EC2, GCP_CloudSQL, GCP_AlloyDB, GCP_Compute, EDB, EDB_Oracle_Server, EDB_PostgreSQL, PostgreSQLFlexibleServer, PostgreSQLCosmosDB, Huawei_RDS, Huawei_Compute, Heroku_PostgreSQL, Crunchy_PostgreSQL, ApsaraDB_RDS, Digital_Ocean_Droplets, Digital_Ocean_PostgreSQL, Supabase_PostgreSQL)</td>
</tr>
<tr>
    <td><CopyableCode code="sslMode" /></td>
    <td><code>string</code></td>
    <td>SSL mode used by a migration. Default SSL mode for 'PostgreSQLSingleServer' is 'VerifyFull'. Default SSL mode for other source types is 'Prefer'. Known values are: "Prefer", "Require", "VerifyCA", and "VerifyFull". (Prefer, Require, VerifyCA, VerifyFull)</td>
</tr>
<tr>
    <td><CopyableCode code="startDataMigration" /></td>
    <td><code>string</code></td>
    <td>Indicates if data migration must start right away. Known values are: "True" and "False". (True, False)</td>
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
    <td><CopyableCode code="targetDbServerFullyQualifiedDomainName" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name (FQDN) or IP address of the target server. This property is optional. When provided, the migration service will always use it to connect to the target server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDbServerMetadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of target database server.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDbServerResourceId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the target database server resource.</td>
</tr>
<tr>
    <td><CopyableCode code="triggerCutover" /></td>
    <td><code>string</code></td>
    <td>Indicates if cutover must be triggered for the entire migration. Known values are: "True" and "False". (True, False)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a migration.</td>
</tr>
<tr>
    <td><a href="#list_by_target_server"><CopyableCode code="list_by_target_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-migrationListFilter"><code>migrationListFilter</code></a></td>
    <td>Lists all migrations of a target flexible server.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new migration.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing migration. The request body can contain one to many of the mutable properties present in the migration definition. Certain property updates initiate migration state transitions.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-migration_name"><code>migration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels an active migration.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Check the validity and availability of the given name, to assign it to a new migration. Checks if a proposed migration name is valid and available.</td>
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
    <td>Name of migration. Required.</td>
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
<tr id="parameter-migrationListFilter">
    <td><CopyableCode code="migrationListFilter" /></td>
    <td><code>string</code></td>
    <td>Migration list filter. Indicates if the request should retrieve only active migrations or all migrations. Defaults to Active. Known values are: "Active" and "All". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_target_server', value: 'list_by_target_server' }
    ]}
>
<TabItem value="get">

Gets information about a migration.

```sql
SELECT
id,
name,
cancel,
currentStatus,
dbsToCancelMigrationOn,
dbsToMigrate,
dbsToTriggerCutoverOn,
location,
migrateRoles,
migrationId,
migrationInstanceResourceId,
migrationMode,
migrationOption,
migrationWindowEndTimeInUtc,
migrationWindowStartTimeInUtc,
overwriteDbsInTarget,
secretParameters,
setupLogicalReplicationOnSourceDbIfNeeded,
sourceDbServerFullyQualifiedDomainName,
sourceDbServerMetadata,
sourceDbServerResourceId,
sourceType,
sslMode,
startDataMigration,
systemData,
tags,
targetDbServerFullyQualifiedDomainName,
targetDbServerMetadata,
targetDbServerResourceId,
triggerCutover,
type
FROM azure.postgresqlflexibleservers.migrations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND migration_name = '{{ migration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_target_server">

Lists all migrations of a target flexible server.

```sql
SELECT
id,
name,
cancel,
currentStatus,
dbsToCancelMigrationOn,
dbsToMigrate,
dbsToTriggerCutoverOn,
location,
migrateRoles,
migrationId,
migrationInstanceResourceId,
migrationMode,
migrationOption,
migrationWindowEndTimeInUtc,
migrationWindowStartTimeInUtc,
overwriteDbsInTarget,
secretParameters,
setupLogicalReplicationOnSourceDbIfNeeded,
sourceDbServerFullyQualifiedDomainName,
sourceDbServerMetadata,
sourceDbServerResourceId,
sourceType,
sslMode,
startDataMigration,
systemData,
tags,
targetDbServerFullyQualifiedDomainName,
targetDbServerMetadata,
targetDbServerResourceId,
triggerCutover,
type
FROM azure.postgresqlflexibleservers.migrations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND migrationListFilter = '{{ migrationListFilter }}'
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

Creates a new migration.

```sql
INSERT INTO azure.postgresqlflexibleservers.migrations (
tags,
location,
properties,
resource_group_name,
server_name,
migration_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ migration_name }}',
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
- name: migrations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the migrations resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the migrations resource.
    - name: migration_name
      value: "{{ migration_name }}"
      description: Required parameter for the migrations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the migrations resource.
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
        Migration properties.
      value:
        migrationId: "{{ migrationId }}"
        currentStatus:
          state: "{{ state }}"
          error: "{{ error }}"
          currentSubStateDetails:
            currentSubState: "{{ currentSubState }}"
            dbDetails: "{{ dbDetails }}"
            validationDetails:
              status: "{{ status }}"
              validationStartTimeInUtc: "{{ validationStartTimeInUtc }}"
              validationEndTimeInUtc: "{{ validationEndTimeInUtc }}"
              serverLevelValidationDetails:
                - type: "{{ type }}"
                  state: "{{ state }}"
                  messages: "{{ messages }}"
              dbLevelValidationDetails:
                - databaseName: "{{ databaseName }}"
                  startedOn: "{{ startedOn }}"
                  endedOn: "{{ endedOn }}"
                  summary: "{{ summary }}"
        migrationInstanceResourceId: "{{ migrationInstanceResourceId }}"
        migrationMode: "{{ migrationMode }}"
        migrationOption: "{{ migrationOption }}"
        sourceType: "{{ sourceType }}"
        sslMode: "{{ sslMode }}"
        sourceDbServerMetadata:
          location: "{{ location }}"
          version: "{{ version }}"
          storageMb: {{ storageMb }}
          sku:
            name: "{{ name }}"
            tier: "{{ tier }}"
        targetDbServerMetadata:
          location: "{{ location }}"
          version: "{{ version }}"
          storageMb: {{ storageMb }}
          sku:
            name: "{{ name }}"
            tier: "{{ tier }}"
        sourceDbServerResourceId: "{{ sourceDbServerResourceId }}"
        sourceDbServerFullyQualifiedDomainName: "{{ sourceDbServerFullyQualifiedDomainName }}"
        targetDbServerResourceId: "{{ targetDbServerResourceId }}"
        targetDbServerFullyQualifiedDomainName: "{{ targetDbServerFullyQualifiedDomainName }}"
        secretParameters:
          adminCredentials:
            sourceServerPassword: "{{ sourceServerPassword }}"
            targetServerPassword: "{{ targetServerPassword }}"
          sourceServerUsername: "{{ sourceServerUsername }}"
          targetServerUsername: "{{ targetServerUsername }}"
        dbsToMigrate:
          - "{{ dbsToMigrate }}"
        setupLogicalReplicationOnSourceDbIfNeeded: "{{ setupLogicalReplicationOnSourceDbIfNeeded }}"
        overwriteDbsInTarget: "{{ overwriteDbsInTarget }}"
        migrationWindowStartTimeInUtc: "{{ migrationWindowStartTimeInUtc }}"
        migrationWindowEndTimeInUtc: "{{ migrationWindowEndTimeInUtc }}"
        migrateRoles: "{{ migrateRoles }}"
        startDataMigration: "{{ startDataMigration }}"
        triggerCutover: "{{ triggerCutover }}"
        dbsToTriggerCutoverOn:
          - "{{ dbsToTriggerCutoverOn }}"
        cancel: "{{ cancel }}"
        dbsToCancelMigrationOn:
          - "{{ dbsToCancelMigrationOn }}"
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

Updates an existing migration. The request body can contain one to many of the mutable properties present in the migration definition. Certain property updates initiate migration state transitions.

```sql
UPDATE azure.postgresqlflexibleservers.migrations
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND migration_name = '{{ migration_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancels an active migration.

```sql
DELETE FROM azure.postgresqlflexibleservers.migrations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND migration_name = '{{ migration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Check the validity and availability of the given name, to assign it to a new migration. Checks if a proposed migration name is valid and available.

```sql
EXEC azure.postgresqlflexibleservers.migrations.check_name_availability 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
