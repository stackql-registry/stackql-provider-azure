--- 
title: workspace_managed_sql_server_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_blob_auditing_policies
  - synapse
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

Creates, updates, deletes, gets or lists a <code>workspace_managed_sql_server_blob_auditing_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_managed_sql_server_blob_auditing_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="auditActionsAndGroups" /></td>
    <td><code>array</code></td>
    <td>Specifies the Actions-Groups and Actions to audit. The recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins: BATCH_COMPLETED_GROUP, SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP, FAILED_DATABASE_AUTHENTICATION_GROUP. This above combination is also the set that is configured by default when enabling auditing from the Azure portal. The supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records): APPLICATION_ROLE_CHANGE_PASSWORD_GROUP BACKUP_RESTORE_GROUP DATABASE_LOGOUT_GROUP DATABASE_OBJECT_CHANGE_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP FAILED_DATABASE_AUTHENTICATION_GROUP SCHEMA_OBJECT_ACCESS_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP USER_CHANGE_PASSWORD_GROUP BATCH_STARTED_GROUP BATCH_COMPLETED_GROUP These are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs. For more information, see `Database-Level Audit Action Groups `_. For Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are: SELECT UPDATE INSERT DELETE EXECUTE RECEIVE REFERENCES The general form for defining an action to be audited is: &#123;action&#125; ON &#123;object&#125; BY &#123;principal&#125; Note that in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms DATABASE::&#123;db_name&#125; and SCHEMA::&#123;schema_name&#125; are used, respectively. For example: SELECT on dbo.myTable by public SELECT on DATABASE::myDatabase by public SELECT on SCHEMA::mySchema by public For more information, see `Database-Level Audit Actions `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isAzureMonitorTargetEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether audit events are sent to Azure Monitor. In order to send the events to Azure Monitor, specify 'state' as 'Enabled' and 'isAzureMonitorTargetEnabled' as true. When using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created. Note that for server level audit you should use the 'master' database as &#123;databaseName&#125;. Diagnostic Settings URI format: PUT https://management.azure.com/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Sql/servers/&#123;serverName&#125;/databases/&#123;databaseName&#125;/providers/microsoft.insights/diagnosticSettings/&#123;settingsName&#125;?api-version=2017-05-01-preview For more information, see `Diagnostic Settings REST API `_ or `Diagnostic Settings PowerShell `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isDevopsAuditEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the state of devops audit. If state is Enabled, devops logs will be sent to Azure Monitor. In order to send the events to Azure Monitor, specify 'State' as 'Enabled', 'IsAzureMonitorTargetEnabled' as true and 'IsDevopsAuditEnabled' as true When using REST API to configure auditing, Diagnostic Settings with 'DevOpsOperationsAudit' diagnostic logs category on the master database should also be created. Diagnostic Settings URI format: PUT https://management.azure.com/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Sql/servers/&#123;serverName&#125;/databases/master/providers/microsoft.insights/diagnosticSettings/&#123;settingsName&#125;?api-version=2017-05-01-preview For more information, see `Diagnostic Settings REST API `_ or `Diagnostic Settings PowerShell `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isStorageSecondaryKeyInUse" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether storageAccountAccessKey value is the storage's secondary key.</td>
</tr>
<tr>
    <td><CopyableCode code="queueDelayMs" /></td>
    <td><code>integer</code></td>
    <td>Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed. The default minimum value is 1000 (1 second). The maximum is 2,147,483,647.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days to keep in the audit logs in the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the policy. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountAccessKey" /></td>
    <td><code>string</code></td>
    <td>Specifies the identifier key of the auditing storage account. If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage. Prerequisites for using managed identity authentication: #. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD). #. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity. For more information, see `Auditing to storage using Managed Identity authentication `_.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="auditActionsAndGroups" /></td>
    <td><code>array</code></td>
    <td>Specifies the Actions-Groups and Actions to audit. The recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins: BATCH_COMPLETED_GROUP, SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP, FAILED_DATABASE_AUTHENTICATION_GROUP. This above combination is also the set that is configured by default when enabling auditing from the Azure portal. The supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records): APPLICATION_ROLE_CHANGE_PASSWORD_GROUP BACKUP_RESTORE_GROUP DATABASE_LOGOUT_GROUP DATABASE_OBJECT_CHANGE_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP FAILED_DATABASE_AUTHENTICATION_GROUP SCHEMA_OBJECT_ACCESS_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP USER_CHANGE_PASSWORD_GROUP BATCH_STARTED_GROUP BATCH_COMPLETED_GROUP These are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs. For more information, see `Database-Level Audit Action Groups `_. For Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are: SELECT UPDATE INSERT DELETE EXECUTE RECEIVE REFERENCES The general form for defining an action to be audited is: &#123;action&#125; ON &#123;object&#125; BY &#123;principal&#125; Note that in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms DATABASE::&#123;db_name&#125; and SCHEMA::&#123;schema_name&#125; are used, respectively. For example: SELECT on dbo.myTable by public SELECT on DATABASE::myDatabase by public SELECT on SCHEMA::mySchema by public For more information, see `Database-Level Audit Actions `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isAzureMonitorTargetEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether audit events are sent to Azure Monitor. In order to send the events to Azure Monitor, specify 'state' as 'Enabled' and 'isAzureMonitorTargetEnabled' as true. When using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created. Note that for server level audit you should use the 'master' database as &#123;databaseName&#125;. Diagnostic Settings URI format: PUT https://management.azure.com/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Sql/servers/&#123;serverName&#125;/databases/&#123;databaseName&#125;/providers/microsoft.insights/diagnosticSettings/&#123;settingsName&#125;?api-version=2017-05-01-preview For more information, see `Diagnostic Settings REST API `_ or `Diagnostic Settings PowerShell `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isDevopsAuditEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the state of devops audit. If state is Enabled, devops logs will be sent to Azure Monitor. In order to send the events to Azure Monitor, specify 'State' as 'Enabled', 'IsAzureMonitorTargetEnabled' as true and 'IsDevopsAuditEnabled' as true When using REST API to configure auditing, Diagnostic Settings with 'DevOpsOperationsAudit' diagnostic logs category on the master database should also be created. Diagnostic Settings URI format: PUT https://management.azure.com/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Sql/servers/&#123;serverName&#125;/databases/master/providers/microsoft.insights/diagnosticSettings/&#123;settingsName&#125;?api-version=2017-05-01-preview For more information, see `Diagnostic Settings REST API `_ or `Diagnostic Settings PowerShell `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isStorageSecondaryKeyInUse" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether storageAccountAccessKey value is the storage's secondary key.</td>
</tr>
<tr>
    <td><CopyableCode code="queueDelayMs" /></td>
    <td><code>integer</code></td>
    <td>Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed. The default minimum value is 1000 (1 second). The maximum is 2,147,483,647.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days to keep in the audit logs in the storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the policy. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountAccessKey" /></td>
    <td><code>string</code></td>
    <td>Specifies the identifier key of the auditing storage account. If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage. Prerequisites for using managed identity authentication: #. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD). #. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity. For more information, see `Auditing to storage using Managed Identity authentication `_.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-blob_auditing_policy_name"><code>blob_auditing_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get server's blob auditing policy. Get a workspace managed sql server's blob auditing policy.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List workspace server's blob auditing policies. List workspace managed sql server's blob auditing policies.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-blob_auditing_policy_name"><code>blob_auditing_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update server's blob auditing policy. Create or Update a workspace managed sql server's blob auditing policy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-blob_auditing_policy_name"><code>blob_auditing_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update server's blob auditing policy. Create or Update a workspace managed sql server's blob auditing policy.</td>
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
<tr id="parameter-blob_auditing_policy_name">
    <td><CopyableCode code="blob_auditing_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the blob auditing policy. "default" Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Get server's blob auditing policy. Get a workspace managed sql server's blob auditing policy.

```sql
SELECT
id,
name,
auditActionsAndGroups,
isAzureMonitorTargetEnabled,
isDevopsAuditEnabled,
isStorageSecondaryKeyInUse,
queueDelayMs,
retentionDays,
state,
storageAccountAccessKey,
storageAccountSubscriptionId,
storageEndpoint,
type
FROM azure.synapse.workspace_managed_sql_server_blob_auditing_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND blob_auditing_policy_name = '{{ blob_auditing_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

List workspace server's blob auditing policies. List workspace managed sql server's blob auditing policies.

```sql
SELECT
id,
name,
auditActionsAndGroups,
isAzureMonitorTargetEnabled,
isDevopsAuditEnabled,
isStorageSecondaryKeyInUse,
queueDelayMs,
retentionDays,
state,
storageAccountAccessKey,
storageAccountSubscriptionId,
storageEndpoint,
type
FROM azure.synapse.workspace_managed_sql_server_blob_auditing_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Create or Update server's blob auditing policy. Create or Update a workspace managed sql server's blob auditing policy.

```sql
INSERT INTO azure.synapse.workspace_managed_sql_server_blob_auditing_policies (
properties,
resource_group_name,
workspace_name,
blob_auditing_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ blob_auditing_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_managed_sql_server_blob_auditing_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the workspace_managed_sql_server_blob_auditing_policies resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the workspace_managed_sql_server_blob_auditing_policies resource.
    - name: blob_auditing_policy_name
      value: "{{ blob_auditing_policy_name }}"
      description: Required parameter for the workspace_managed_sql_server_blob_auditing_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the workspace_managed_sql_server_blob_auditing_policies resource.
    - name: properties
      value:
        state: "{{ state }}"
        storageEndpoint: "{{ storageEndpoint }}"
        storageAccountAccessKey: "{{ storageAccountAccessKey }}"
        retentionDays: {{ retentionDays }}
        auditActionsAndGroups:
          - "{{ auditActionsAndGroups }}"
        storageAccountSubscriptionId: "{{ storageAccountSubscriptionId }}"
        isStorageSecondaryKeyInUse: {{ isStorageSecondaryKeyInUse }}
        isAzureMonitorTargetEnabled: {{ isAzureMonitorTargetEnabled }}
        queueDelayMs: {{ queueDelayMs }}
        isDevopsAuditEnabled: {{ isDevopsAuditEnabled }}
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

Create or Update server's blob auditing policy. Create or Update a workspace managed sql server's blob auditing policy.

```sql
REPLACE azure.synapse.workspace_managed_sql_server_blob_auditing_policies
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND blob_auditing_policy_name = '{{ blob_auditing_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
</Tabs>
