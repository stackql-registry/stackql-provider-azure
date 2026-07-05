--- 
title: database_migrations_sql_mi
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_mi
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

Creates, updates, deletes, gets or lists a <code>database_migrations_sql_mi</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_migrations_sql_mi" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datamigration.database_migrations_sql_mi" /></td></tr>
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
    <td><CopyableCode code="backupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Backup configuration info.</td>
</tr>
<tr>
    <td><CopyableCode code="endedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Database migration end time.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Required. SqlMi.</td>
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
    <td><CopyableCode code="migrationStatusDetails" /></td>
    <td><code>object</code></td>
    <td>Detailed migration status. Not included by default.</td>
</tr>
<tr>
    <td><CopyableCode code="offlineConfiguration" /></td>
    <td><code>object</code></td>
    <td>Offline configuration.</td>
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
    <td><CopyableCode code="sourceDatabaseName" /></td>
    <td><code>string</code></td>
    <td>Name of the source database.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceServerName" /></td>
    <td><code>string</code></td>
    <td>Name of the source sql server.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSqlConnection" /></td>
    <td><code>object</code></td>
    <td>Source SQL Server connection details.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerInstanceId" /></td>
    <td><code>string</code></td>
    <td>Optional property - Resource Id for the source Sql server instance. Validations are performed on this property to ensure that it follows the correct format.</td>
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
    <td><CopyableCode code="targetDatabaseCollation" /></td>
    <td><code>string</code></td>
    <td>Database collation to be used for the target database.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-target_db_name"><code>target_db_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-migrationOperationId"><code>migrationOperationId</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the specified database migration for a given SQL Managed Instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-target_db_name"><code>target_db_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new database migration to a given SQL Managed Instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-target_db_name"><code>target_db_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new database migration to a given SQL Managed Instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-target_db_name"><code>target_db_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete Database Migration resource.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-target_db_name"><code>target_db_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop in-progress database migration to SQL Managed Instance.</td>
</tr>
<tr>
    <td><a href="#cutover"><CopyableCode code="cutover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-target_db_name"><code>target_db_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiate cutover for in-progress online database migration to SQL Managed Instance.</td>
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
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the target SQL Managed Instance. Required.</td>
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
<tr id="parameter-target_db_name">
    <td><CopyableCode code="target_db_name" /></td>
    <td><code>string</code></td>
    <td>The name of the target database. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Complete migration details be included in the response. Default value is None.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Optional force delete boolean. If this is provided as true, migration will be deleted even if active. Default value is None.</td>
</tr>
<tr id="parameter-migrationOperationId">
    <td><CopyableCode code="migrationOperationId" /></td>
    <td><code>string</code></td>
    <td>Optional migration operation ID. If this is provided, then details of migration operation for that ID are retrieved. If not provided (default), then details related to most recent or current operation are retrieved. Default value is None.</td>
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

Retrieve the specified database migration for a given SQL Managed Instance.

```sql
SELECT
id,
name,
backupConfiguration,
endedOn,
kind,
migrationFailureError,
migrationOperationId,
migrationService,
migrationStatus,
migrationStatusDetails,
offlineConfiguration,
provisioningError,
provisioningState,
scope,
sourceDatabaseName,
sourceServerName,
sourceSqlConnection,
sqlServerInstanceId,
startedOn,
systemData,
targetDatabaseCollation,
type
FROM azure.datamigration.database_migrations_sql_mi
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND target_db_name = '{{ target_db_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND migrationOperationId = '{{ migrationOperationId }}'
AND $expand = '{{ $expand }}'
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

Create a new database migration to a given SQL Managed Instance.

```sql
INSERT INTO azure.datamigration.database_migrations_sql_mi (
properties,
resource_group_name,
managed_instance_name,
target_db_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ managed_instance_name }}',
'{{ target_db_name }}',
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
- name: database_migrations_sql_mi
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the database_migrations_sql_mi resource.
    - name: managed_instance_name
      value: "{{ managed_instance_name }}"
      description: Required parameter for the database_migrations_sql_mi resource.
    - name: target_db_name
      value: "{{ target_db_name }}"
      description: Required parameter for the database_migrations_sql_mi resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the database_migrations_sql_mi resource.
    - name: properties
      description: |
        Database Migration Resource properties for SQL Managed Instance.
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
        sourceSqlConnection:
          dataSource: "{{ dataSource }}"
          authentication: "{{ authentication }}"
          userName: "{{ userName }}"
          password: "{{ password }}"
          encryptConnection: {{ encryptConnection }}
          trustServerCertificate: {{ trustServerCertificate }}
        sourceDatabaseName: "{{ sourceDatabaseName }}"
        sourceServerName: "{{ sourceServerName }}"
        targetDatabaseCollation: "{{ targetDatabaseCollation }}"
        sqlServerInstanceId: "{{ sqlServerInstanceId }}"
        migrationStatusDetails:
          migrationState: "{{ migrationState }}"
          fullBackupSetInfo:
            backupSetId: "{{ backupSetId }}"
            firstLSN: "{{ firstLSN }}"
            lastLSN: "{{ lastLSN }}"
            backupType: "{{ backupType }}"
            listOfBackupFiles:
              - fileName: "{{ fileName }}"
                status: "{{ status }}"
                totalSize: {{ totalSize }}
                dataRead: {{ dataRead }}
                dataWritten: {{ dataWritten }}
                copyThroughput: {{ copyThroughput }}
                copyDuration: {{ copyDuration }}
                familySequenceNumber: {{ familySequenceNumber }}
            backupStartDate: "{{ backupStartDate }}"
            backupFinishDate: "{{ backupFinishDate }}"
            isBackupRestored: {{ isBackupRestored }}
            hasBackupChecksums: {{ hasBackupChecksums }}
            familyCount: {{ familyCount }}
            ignoreReasons:
              - "{{ ignoreReasons }}"
          lastRestoredBackupSetInfo:
            backupSetId: "{{ backupSetId }}"
            firstLSN: "{{ firstLSN }}"
            lastLSN: "{{ lastLSN }}"
            backupType: "{{ backupType }}"
            listOfBackupFiles:
              - fileName: "{{ fileName }}"
                status: "{{ status }}"
                totalSize: {{ totalSize }}
                dataRead: {{ dataRead }}
                dataWritten: {{ dataWritten }}
                copyThroughput: {{ copyThroughput }}
                copyDuration: {{ copyDuration }}
                familySequenceNumber: {{ familySequenceNumber }}
            backupStartDate: "{{ backupStartDate }}"
            backupFinishDate: "{{ backupFinishDate }}"
            isBackupRestored: {{ isBackupRestored }}
            hasBackupChecksums: {{ hasBackupChecksums }}
            familyCount: {{ familyCount }}
            ignoreReasons:
              - "{{ ignoreReasons }}"
          activeBackupSets:
            - backupSetId: "{{ backupSetId }}"
              firstLSN: "{{ firstLSN }}"
              lastLSN: "{{ lastLSN }}"
              backupType: "{{ backupType }}"
              listOfBackupFiles: "{{ listOfBackupFiles }}"
              backupStartDate: "{{ backupStartDate }}"
              backupFinishDate: "{{ backupFinishDate }}"
              isBackupRestored: {{ isBackupRestored }}
              hasBackupChecksums: {{ hasBackupChecksums }}
              familyCount: {{ familyCount }}
              ignoreReasons: "{{ ignoreReasons }}"
          invalidFiles:
            - "{{ invalidFiles }}"
          blobContainerName: "{{ blobContainerName }}"
          isFullBackupRestored: {{ isFullBackupRestored }}
          restoreBlockingReason: "{{ restoreBlockingReason }}"
          completeRestoreErrorMessage: "{{ completeRestoreErrorMessage }}"
          fileUploadBlockingErrors:
            - "{{ fileUploadBlockingErrors }}"
          currentRestoringFilename: "{{ currentRestoringFilename }}"
          lastRestoredFilename: "{{ lastRestoredFilename }}"
          pendingLogBackupsCount: {{ pendingLogBackupsCount }}
        backupConfiguration:
          sourceLocation:
            fileShare:
              path: "{{ path }}"
              username: "{{ username }}"
              password: "{{ password }}"
            azureBlob:
              authType: "{{ authType }}"
              identity:
                principalId: "{{ principalId }}"
                tenantId: "{{ tenantId }}"
                type: "{{ type }}"
                userAssignedIdentities: "{{ userAssignedIdentities }}"
              storageAccountResourceId: "{{ storageAccountResourceId }}"
              accountKey: "{{ accountKey }}"
              blobContainerName: "{{ blobContainerName }}"
            fileStorageType: "{{ fileStorageType }}"
          targetLocation:
            storageAccountResourceId: "{{ storageAccountResourceId }}"
            accountKey: "{{ accountKey }}"
        offlineConfiguration:
          offline: {{ offline }}
          lastBackupName: "{{ lastBackupName }}"
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

Create a new database migration to a given SQL Managed Instance.

```sql
REPLACE azure.datamigration.database_migrations_sql_mi
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND target_db_name = '{{ target_db_name }}' --required
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

Delete Database Migration resource.

```sql
DELETE FROM azure.datamigration.database_migrations_sql_mi
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND target_db_name = '{{ target_db_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'cutover', value: 'cutover' }
    ]}
>
<TabItem value="cancel">

Stop in-progress database migration to SQL Managed Instance.

```sql
EXEC azure.datamigration.database_migrations_sql_mi.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@target_db_name='{{ target_db_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"migrationOperationId": "{{ migrationOperationId }}"
}'
;
```
</TabItem>
<TabItem value="cutover">

Initiate cutover for in-progress online database migration to SQL Managed Instance.

```sql
EXEC azure.datamigration.database_migrations_sql_mi.cutover 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@target_db_name='{{ target_db_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"migrationOperationId": "{{ migrationOperationId }}"
}'
;
```
</TabItem>
</Tabs>
