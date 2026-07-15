--- 
title: replication_migration_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_migration_items
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_migration_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_migration_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_migration_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
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
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the migration item based on the current migration state of the item.</td>
</tr>
<tr>
    <td><CopyableCode code="criticalJobHistory" /></td>
    <td><code>array</code></td>
    <td>The critical past job details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentJob" /></td>
    <td><code>object</code></td>
    <td>The current job details.</td>
</tr>
<tr>
    <td><CopyableCode code="eventCorrelationId" /></td>
    <td><code>string</code></td>
    <td>The correlation Id for events associated with this migration item.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>The consolidated health. Known values are: "None", "Normal", "Warning", and "Critical". (None, Normal, Warning, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>The list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMigrationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the last migration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMigrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last migration time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestMigrationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the last test migration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestMigrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last test migration time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The on-premise virtual machine name.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationState" /></td>
    <td><code>string</code></td>
    <td>The migration status. Known values are: "None", "EnableMigrationInProgress", "EnableMigrationFailed", "DisableMigrationInProgress", "DisableMigrationFailed", "InitialSeedingInProgress", "InitialSeedingFailed", "Replicating", "MigrationInProgress", "MigrationSucceeded", "MigrationFailed", "ResumeInProgress", "ResumeInitiated", "SuspendingProtection", "ProtectionSuspended", "MigrationCompletedWithInformation", and "MigrationPartiallySucceeded". (None, EnableMigrationInProgress, EnableMigrationFailed, DisableMigrationInProgress, DisableMigrationFailed, InitialSeedingInProgress, InitialSeedingFailed, Replicating, MigrationInProgress, MigrationSucceeded, MigrationFailed, ResumeInProgress, ResumeInitiated, SuspendingProtection, ProtectionSuspended, MigrationCompletedWithInformation, MigrationPartiallySucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationStateDescription" /></td>
    <td><code>string</code></td>
    <td>The migration state description.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of policy governing this item.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The ARM Id of policy governing this item.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The migration provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery services provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationStatus" /></td>
    <td><code>string</code></td>
    <td>The replication status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testMigrateState" /></td>
    <td><code>string</code></td>
    <td>The test migrate state. Known values are: "None", "TestMigrationInProgress", "TestMigrationSucceeded", "TestMigrationFailed", "TestMigrationCleanupInProgress", "TestMigrationCompletedWithInformation", and "TestMigrationPartiallySucceeded". (None, TestMigrationInProgress, TestMigrationSucceeded, TestMigrationFailed, TestMigrationCleanupInProgress, TestMigrationCompletedWithInformation, TestMigrationPartiallySucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="testMigrateStateDescription" /></td>
    <td><code>string</code></td>
    <td>The test migrate state description.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_replication_protection_containers">

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
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the migration item based on the current migration state of the item.</td>
</tr>
<tr>
    <td><CopyableCode code="criticalJobHistory" /></td>
    <td><code>array</code></td>
    <td>The critical past job details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentJob" /></td>
    <td><code>object</code></td>
    <td>The current job details.</td>
</tr>
<tr>
    <td><CopyableCode code="eventCorrelationId" /></td>
    <td><code>string</code></td>
    <td>The correlation Id for events associated with this migration item.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>The consolidated health. Known values are: "None", "Normal", "Warning", and "Critical". (None, Normal, Warning, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>The list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMigrationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the last migration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMigrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last migration time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestMigrationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the last test migration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestMigrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last test migration time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The on-premise virtual machine name.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationState" /></td>
    <td><code>string</code></td>
    <td>The migration status. Known values are: "None", "EnableMigrationInProgress", "EnableMigrationFailed", "DisableMigrationInProgress", "DisableMigrationFailed", "InitialSeedingInProgress", "InitialSeedingFailed", "Replicating", "MigrationInProgress", "MigrationSucceeded", "MigrationFailed", "ResumeInProgress", "ResumeInitiated", "SuspendingProtection", "ProtectionSuspended", "MigrationCompletedWithInformation", and "MigrationPartiallySucceeded". (None, EnableMigrationInProgress, EnableMigrationFailed, DisableMigrationInProgress, DisableMigrationFailed, InitialSeedingInProgress, InitialSeedingFailed, Replicating, MigrationInProgress, MigrationSucceeded, MigrationFailed, ResumeInProgress, ResumeInitiated, SuspendingProtection, ProtectionSuspended, MigrationCompletedWithInformation, MigrationPartiallySucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationStateDescription" /></td>
    <td><code>string</code></td>
    <td>The migration state description.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of policy governing this item.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The ARM Id of policy governing this item.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The migration provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery services provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationStatus" /></td>
    <td><code>string</code></td>
    <td>The replication status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testMigrateState" /></td>
    <td><code>string</code></td>
    <td>The test migrate state. Known values are: "None", "TestMigrationInProgress", "TestMigrationSucceeded", "TestMigrationFailed", "TestMigrationCleanupInProgress", "TestMigrationCompletedWithInformation", and "TestMigrationPartiallySucceeded". (None, TestMigrationInProgress, TestMigrationSucceeded, TestMigrationFailed, TestMigrationCleanupInProgress, TestMigrationCompletedWithInformation, TestMigrationPartiallySucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="testMigrateStateDescription" /></td>
    <td><code>string</code></td>
    <td>The test migrate state description.</td>
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
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the migration item based on the current migration state of the item.</td>
</tr>
<tr>
    <td><CopyableCode code="criticalJobHistory" /></td>
    <td><code>array</code></td>
    <td>The critical past job details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentJob" /></td>
    <td><code>object</code></td>
    <td>The current job details.</td>
</tr>
<tr>
    <td><CopyableCode code="eventCorrelationId" /></td>
    <td><code>string</code></td>
    <td>The correlation Id for events associated with this migration item.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>The consolidated health. Known values are: "None", "Normal", "Warning", and "Critical". (None, Normal, Warning, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>The list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMigrationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the last migration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastMigrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last migration time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestMigrationStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the last test migration.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestMigrationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last test migration time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The on-premise virtual machine name.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationState" /></td>
    <td><code>string</code></td>
    <td>The migration status. Known values are: "None", "EnableMigrationInProgress", "EnableMigrationFailed", "DisableMigrationInProgress", "DisableMigrationFailed", "InitialSeedingInProgress", "InitialSeedingFailed", "Replicating", "MigrationInProgress", "MigrationSucceeded", "MigrationFailed", "ResumeInProgress", "ResumeInitiated", "SuspendingProtection", "ProtectionSuspended", "MigrationCompletedWithInformation", and "MigrationPartiallySucceeded". (None, EnableMigrationInProgress, EnableMigrationFailed, DisableMigrationInProgress, DisableMigrationFailed, InitialSeedingInProgress, InitialSeedingFailed, Replicating, MigrationInProgress, MigrationSucceeded, MigrationFailed, ResumeInProgress, ResumeInitiated, SuspendingProtection, ProtectionSuspended, MigrationCompletedWithInformation, MigrationPartiallySucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="migrationStateDescription" /></td>
    <td><code>string</code></td>
    <td>The migration state description.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of policy governing this item.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The ARM Id of policy governing this item.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The migration provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery services provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationStatus" /></td>
    <td><code>string</code></td>
    <td>The replication status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testMigrateState" /></td>
    <td><code>string</code></td>
    <td>The test migrate state. Known values are: "None", "TestMigrationInProgress", "TestMigrationSucceeded", "TestMigrationFailed", "TestMigrationCleanupInProgress", "TestMigrationCompletedWithInformation", and "TestMigrationPartiallySucceeded". (None, TestMigrationInProgress, TestMigrationSucceeded, TestMigrationFailed, TestMigrationCleanupInProgress, TestMigrationCompletedWithInformation, TestMigrationPartiallySucceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="testMigrateStateDescription" /></td>
    <td><code>string</code></td>
    <td>The test migrate state description.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a migration item. Gets the details of a migration item.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_protection_containers"><CopyableCode code="list_by_replication_protection_containers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipToken"><code>skipToken</code></a>, <a href="#parameter-takeToken"><code>takeToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the list of migration items in the protection container. Gets the list of ASR migration items in the protection container.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipToken"><code>skipToken</code></a>, <a href="#parameter-takeToken"><code>takeToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the list of migration items in the vault. Gets the list of migration items in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Enables migration. The operation to create an ASR migration item (enable migration).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates migration item. The operation to update the recovery settings of an ASR migration item.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteOption"><code>deleteOption</code></a></td>
    <td>Delete the migration item. The operation to delete an ASR migration item.</td>
</tr>
<tr>
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Migrate item. The operation to initiate migration of the item.</td>
</tr>
<tr>
    <td><a href="#pause_replication"><CopyableCode code="pause_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Pause replication. The operation to initiate pause replication of the item.</td>
</tr>
<tr>
    <td><a href="#resume_replication"><CopyableCode code="resume_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Resume replication. The operation to initiate resume replication of the item.</td>
</tr>
<tr>
    <td><a href="#resync"><CopyableCode code="resync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Resynchronizes replication. The operation to resynchronize replication of an ASR migration item.</td>
</tr>
<tr>
    <td><a href="#test_migrate"><CopyableCode code="test_migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Test migrate item. The operation to initiate test migration of the item.</td>
</tr>
<tr>
    <td><a href="#test_migrate_cleanup"><CopyableCode code="test_migrate_cleanup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-migration_item_name"><code>migration_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Test migrate cleanup. The operation to initiate test migrate cleanup.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-migration_item_name">
    <td><CopyableCode code="migration_item_name" /></td>
    <td><code>string</code></td>
    <td>Migration item name. Required.</td>
</tr>
<tr id="parameter-protection_container_name">
    <td><CopyableCode code="protection_container_name" /></td>
    <td><code>string</code></td>
    <td>Protection container name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
<tr id="parameter-deleteOption">
    <td><CopyableCode code="deleteOption" /></td>
    <td><code>string</code></td>
    <td>The delete option. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>The pagination token. Default value is None.</td>
</tr>
<tr id="parameter-takeToken">
    <td><CopyableCode code="takeToken" /></td>
    <td><code>string</code></td>
    <td>The page size. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details of a migration item. Gets the details of a migration item.

```sql
SELECT
id,
name,
allowedOperations,
criticalJobHistory,
currentJob,
eventCorrelationId,
health,
healthErrors,
lastMigrationStatus,
lastMigrationTime,
lastTestMigrationStatus,
lastTestMigrationTime,
location,
machineName,
migrationState,
migrationStateDescription,
policyFriendlyName,
policyId,
providerSpecificDetails,
recoveryServicesProviderId,
replicationStatus,
systemData,
testMigrateState,
testMigrateStateDescription,
type
FROM azure.recovery_services_site_recovery.replication_migration_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND migration_item_name = '{{ migration_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_protection_containers">

Gets the list of migration items in the protection container. Gets the list of ASR migration items in the protection container.

```sql
SELECT
id,
name,
allowedOperations,
criticalJobHistory,
currentJob,
eventCorrelationId,
health,
healthErrors,
lastMigrationStatus,
lastMigrationTime,
lastTestMigrationStatus,
lastTestMigrationTime,
location,
machineName,
migrationState,
migrationStateDescription,
policyFriendlyName,
policyId,
providerSpecificDetails,
recoveryServicesProviderId,
replicationStatus,
systemData,
testMigrateState,
testMigrateStateDescription,
type
FROM azure.recovery_services_site_recovery.replication_migration_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND skipToken = '{{ skipToken }}'
AND takeToken = '{{ takeToken }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Gets the list of migration items in the vault. Gets the list of migration items in the vault.

```sql
SELECT
id,
name,
allowedOperations,
criticalJobHistory,
currentJob,
eventCorrelationId,
health,
healthErrors,
lastMigrationStatus,
lastMigrationTime,
lastTestMigrationStatus,
lastTestMigrationTime,
location,
machineName,
migrationState,
migrationStateDescription,
policyFriendlyName,
policyId,
providerSpecificDetails,
recoveryServicesProviderId,
replicationStatus,
systemData,
testMigrateState,
testMigrateStateDescription,
type
FROM azure.recovery_services_site_recovery.replication_migration_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND skipToken = '{{ skipToken }}'
AND takeToken = '{{ takeToken }}'
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

Enables migration. The operation to create an ASR migration item (enable migration).

```sql
INSERT INTO azure.recovery_services_site_recovery.replication_migration_items (
properties,
resource_group_name,
resource_name,
fabric_name,
protection_container_name,
migration_item_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ protection_container_name }}',
'{{ migration_item_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_migration_items
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_migration_items resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_migration_items resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_migration_items resource.
    - name: protection_container_name
      value: "{{ protection_container_name }}"
      description: Required parameter for the replication_migration_items resource.
    - name: migration_item_name
      value: "{{ migration_item_name }}"
      description: Required parameter for the replication_migration_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_migration_items resource.
    - name: properties
      description: |
        Enable migration input properties. Required.
      value:
        policyId: "{{ policyId }}"
        providerSpecificDetails:
          instanceType: "{{ instanceType }}"
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

Updates migration item. The operation to update the recovery settings of an ASR migration item.

```sql
UPDATE azure.recovery_services_site_recovery.replication_migration_items
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND migration_item_name = '{{ migration_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Delete the migration item. The operation to delete an ASR migration item.

```sql
DELETE FROM azure.recovery_services_site_recovery.replication_migration_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND migration_item_name = '{{ migration_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteOption = '{{ deleteOption }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="migrate"
    values={[
        { label: 'migrate', value: 'migrate' },
        { label: 'pause_replication', value: 'pause_replication' },
        { label: 'resume_replication', value: 'resume_replication' },
        { label: 'resync', value: 'resync' },
        { label: 'test_migrate', value: 'test_migrate' },
        { label: 'test_migrate_cleanup', value: 'test_migrate_cleanup' }
    ]}
>
<TabItem value="migrate">

Migrate item. The operation to initiate migration of the item.

```sql
EXEC azure.recovery_services_site_recovery.replication_migration_items.migrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@migration_item_name='{{ migration_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="pause_replication">

Pause replication. The operation to initiate pause replication of the item.

```sql
EXEC azure.recovery_services_site_recovery.replication_migration_items.pause_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@migration_item_name='{{ migration_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="resume_replication">

Resume replication. The operation to initiate resume replication of the item.

```sql
EXEC azure.recovery_services_site_recovery.replication_migration_items.resume_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@migration_item_name='{{ migration_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="resync">

Resynchronizes replication. The operation to resynchronize replication of an ASR migration item.

```sql
EXEC azure.recovery_services_site_recovery.replication_migration_items.resync 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@migration_item_name='{{ migration_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="test_migrate">

Test migrate item. The operation to initiate test migration of the item.

```sql
EXEC azure.recovery_services_site_recovery.replication_migration_items.test_migrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@migration_item_name='{{ migration_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="test_migrate_cleanup">

Test migrate cleanup. The operation to initiate test migrate cleanup.

```sql
EXEC azure.recovery_services_site_recovery.replication_migration_items.test_migrate_cleanup 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@migration_item_name='{{ migration_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
