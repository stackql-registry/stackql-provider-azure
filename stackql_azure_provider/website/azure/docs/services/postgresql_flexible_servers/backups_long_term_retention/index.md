--- 
title: backups_long_term_retention
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_long_term_retention
  - postgresql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>backups_long_term_retention</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backups_long_term_retention" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_flexible_servers.backups_long_term_retention" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'check_prerequisites', value: 'check_prerequisites' },
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
    <td><CopyableCode code="backupMetadata" /></td>
    <td><code>string</code></td>
    <td>Metadata to be stored in RP. Store everything that will be required to perform a successful restore using this Recovery point. e.g. Versions, DataFormat etc.</td>
</tr>
<tr>
    <td><CopyableCode code="backupName" /></td>
    <td><code>string</code></td>
    <td>Name of Backup operation.</td>
</tr>
<tr>
    <td><CopyableCode code="dataTransferredInBytes" /></td>
    <td><code>integer</code></td>
    <td>Data transferred in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceSizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of datasource in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>string</code></td>
    <td>Error code.</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Error message.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>number</code></td>
    <td>Percentage completed.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Service-set extensible enum indicating the status of operation. Required. Known values are: "Running", "Cancelled", "Failed", and "Succeeded". (Running, Cancelled, Failed, Succeeded)</td>
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
<TabItem value="check_prerequisites">

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
    <td><CopyableCode code="numberOfContainers" /></td>
    <td><code>integer</code></td>
    <td>Number of storage containers the plugin will use during backup. More than one containers may be used for size limitations, parallelism, or redundancy etc. Required.</td>
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
    <td><CopyableCode code="backupMetadata" /></td>
    <td><code>string</code></td>
    <td>Metadata to be stored in RP. Store everything that will be required to perform a successful restore using this Recovery point. e.g. Versions, DataFormat etc.</td>
</tr>
<tr>
    <td><CopyableCode code="backupName" /></td>
    <td><code>string</code></td>
    <td>Name of Backup operation.</td>
</tr>
<tr>
    <td><CopyableCode code="dataTransferredInBytes" /></td>
    <td><code>integer</code></td>
    <td>Data transferred in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="datasourceSizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of datasource in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>string</code></td>
    <td>Error code.</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Error message.</td>
</tr>
<tr>
    <td><CopyableCode code="percentComplete" /></td>
    <td><code>number</code></td>
    <td>Percentage completed.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Service-set extensible enum indicating the status of operation. Required. Known values are: "Running", "Cancelled", "Failed", and "Succeeded". (Running, Cancelled, Failed, Succeeded)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-backup_name"><code>backup_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the results of a long retention backup operation for a server.</td>
</tr>
<tr>
    <td><a href="#check_prerequisites"><CopyableCode code="check_prerequisites" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Performs all checks required for a long term retention backup operation to succeed.</td>
</tr>
<tr>
    <td><a href="#list_by_server"><CopyableCode code="list_by_server" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the results of the long term retention backup operations for a server.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupSettings"><code>backupSettings</code></a>, <a href="#parameter-targetDetails"><code>targetDetails</code></a></td>
    <td></td>
    <td>Initiates a long term retention backup.</td>
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
<tr id="parameter-backup_name">
    <td><CopyableCode code="backup_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backup. Required.</td>
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
        { label: 'check_prerequisites', value: 'check_prerequisites' },
        { label: 'list_by_server', value: 'list_by_server' }
    ]}
>
<TabItem value="get">

Gets the results of a long retention backup operation for a server.

```sql
SELECT
id,
name,
backupMetadata,
backupName,
dataTransferredInBytes,
datasourceSizeInBytes,
endTime,
errorCode,
errorMessage,
percentComplete,
startTime,
status,
systemData,
type
FROM azure.postgresql_flexible_servers.backups_long_term_retention
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND backup_name = '{{ backup_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_prerequisites">

Performs all checks required for a long term retention backup operation to succeed.

```sql
SELECT
numberOfContainers
FROM azure.postgresql_flexible_servers.backups_long_term_retention
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_server">

Lists the results of the long term retention backup operations for a server.

```sql
SELECT
id,
name,
backupMetadata,
backupName,
dataTransferredInBytes,
datasourceSizeInBytes,
endTime,
errorCode,
errorMessage,
percentComplete,
startTime,
status,
systemData,
type
FROM azure.postgresql_flexible_servers.backups_long_term_retention
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' }
    ]}
>
<TabItem value="start">

Initiates a long term retention backup.

```sql
EXEC azure.postgresql_flexible_servers.backups_long_term_retention.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"backupSettings": "{{ backupSettings }}", 
"targetDetails": "{{ targetDetails }}"
}'
;
```
</TabItem>
</Tabs>
