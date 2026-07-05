--- 
title: server_dev_ops_audit_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dev_ops_audit_settings
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

Creates, updates, deletes, gets or lists a <code>server_dev_ops_audit_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_dev_ops_audit_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_dev_ops_audit_settings" /></td></tr>
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
    <td><CopyableCode code="isAzureMonitorTargetEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether DevOps audit events are sent to Azure Monitor. In order to send the events to Azure Monitor, specify 'State' as 'Enabled' and 'IsAzureMonitorTargetEnabled' as true. When using REST API to configure DevOps audit, Diagnostic Settings with 'DevOpsOperationsAudit' diagnostic logs category on the master database should be also created. Diagnostic Settings URI format: PUT `https://management.azure.com/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Sql/servers/&#123;serverName&#125;/databases/master/providers/microsoft.insights/diagnosticSettings/&#123;settingsName&#125;?api-version=2017-05-01-preview `_ For more information, see `Diagnostic Settings REST API `_ or `Diagnostic Settings PowerShell `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagedIdentityInUse" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether Managed Identity is used to access blob storage.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountAccessKey" /></td>
    <td><code>string</code></td>
    <td>Specifies the identifier key of the auditing storage account. If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage. Prerequisites for using managed identity authentication: 1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD). 2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity. For more information, see [Auditing to storage using Managed Identity authentication](https://go.microsoft.com/fwlink/?linkid=2114355).</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage endpoint (e.g. `https://MyAccount.blob.core.windows.net `_). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required.</td>
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
    <td><CopyableCode code="isAzureMonitorTargetEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether DevOps audit events are sent to Azure Monitor. In order to send the events to Azure Monitor, specify 'State' as 'Enabled' and 'IsAzureMonitorTargetEnabled' as true. When using REST API to configure DevOps audit, Diagnostic Settings with 'DevOpsOperationsAudit' diagnostic logs category on the master database should be also created. Diagnostic Settings URI format: PUT `https://management.azure.com/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Sql/servers/&#123;serverName&#125;/databases/master/providers/microsoft.insights/diagnosticSettings/&#123;settingsName&#125;?api-version=2017-05-01-preview `_ For more information, see `Diagnostic Settings REST API `_ or `Diagnostic Settings PowerShell `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagedIdentityInUse" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether Managed Identity is used to access blob storage.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required. Required. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountAccessKey" /></td>
    <td><code>string</code></td>
    <td>Specifies the identifier key of the auditing storage account. If state is Enabled and storageEndpoint is specified, not specifying the storageAccountAccessKey will use SQL server system-assigned managed identity to access the storage. Prerequisites for using managed identity authentication: 1. Assign SQL Server a system-assigned managed identity in Azure Active Directory (AAD). 2. Grant SQL Server identity access to the storage account by adding 'Storage Blob Data Contributor' RBAC role to the server identity. For more information, see [Auditing to storage using Managed Identity authentication](https://go.microsoft.com/fwlink/?linkid=2114355).</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage endpoint (e.g. `https://MyAccount.blob.core.windows.net `_). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-dev_ops_auditing_settings_name"><code>dev_ops_auditing_settings_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a server's DevOps audit settings.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists DevOps audit settings of a server.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-dev_ops_auditing_settings_name"><code>dev_ops_auditing_settings_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a server's DevOps audit settings.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-dev_ops_auditing_settings_name"><code>dev_ops_auditing_settings_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a server's DevOps audit settings.</td>
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
<tr id="parameter-dev_ops_auditing_settings_name">
    <td><CopyableCode code="dev_ops_auditing_settings_name" /></td>
    <td><code>string</code></td>
    <td>"Default" Required.</td>
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

Gets a server's DevOps audit settings.

```sql
SELECT
id,
name,
isAzureMonitorTargetEnabled,
isManagedIdentityInUse,
state,
storageAccountAccessKey,
storageAccountSubscriptionId,
storageEndpoint,
systemData,
type
FROM azure.sql.server_dev_ops_audit_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND dev_ops_auditing_settings_name = '{{ dev_ops_auditing_settings_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

Lists DevOps audit settings of a server.

```sql
SELECT
id,
name,
isAzureMonitorTargetEnabled,
isManagedIdentityInUse,
state,
storageAccountAccessKey,
storageAccountSubscriptionId,
storageEndpoint,
systemData,
type
FROM azure.sql.server_dev_ops_audit_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
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

Creates or updates a server's DevOps audit settings.

```sql
INSERT INTO azure.sql.server_dev_ops_audit_settings (
properties,
resource_group_name,
server_name,
dev_ops_auditing_settings_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ dev_ops_auditing_settings_name }}',
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
- name: server_dev_ops_audit_settings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the server_dev_ops_audit_settings resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the server_dev_ops_audit_settings resource.
    - name: dev_ops_auditing_settings_name
      value: "{{ dev_ops_auditing_settings_name }}"
      description: Required parameter for the server_dev_ops_audit_settings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the server_dev_ops_audit_settings resource.
    - name: properties
      description: |
        Resource properties.
      value:
        isAzureMonitorTargetEnabled: {{ isAzureMonitorTargetEnabled }}
        isManagedIdentityInUse: {{ isManagedIdentityInUse }}
        state: "{{ state }}"
        storageEndpoint: "{{ storageEndpoint }}"
        storageAccountAccessKey: "{{ storageAccountAccessKey }}"
        storageAccountSubscriptionId: "{{ storageAccountSubscriptionId }}"
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

Creates or updates a server's DevOps audit settings.

```sql
REPLACE azure.sql.server_dev_ops_audit_settings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND dev_ops_auditing_settings_name = '{{ dev_ops_auditing_settings_name }}' --required
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
