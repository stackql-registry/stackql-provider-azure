--- 
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>backup_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.backup_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_backup_policy_by_name"
    values={[
        { label: 'get_backup_policy_by_name', value: 'get_backup_policy_by_name' }
    ]}
>
<TabItem value="get_backup_policy_by_name">

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
    <td><CopyableCode code="AutoRestoreOnDataLoss" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="MaxIncrementalBackups" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="RetentionPolicy" /></td>
    <td><code>object</code></td>
    <td>Describes the retention policy configured. You probably want to use the sub-classes and not this class directly. Known sub-classes are: BasicRetentionPolicyDescription All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="Schedule" /></td>
    <td><code>object</code></td>
    <td>Describes the backup schedule parameters. You probably want to use the sub-classes and not this class directly. Known sub-classes are: FrequencyBasedBackupScheduleDescription, TimeBasedBackupScheduleDescription All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="Storage" /></td>
    <td><code>object</code></td>
    <td>Describes the parameters for the backup storage. You probably want to use the sub-classes and not this class directly. Known sub-classes are: AzureBlobBackupStorageDescription, FileShareBackupStorageDescription, DsmsAzureBlobBackupStorageDescription, ManagedIdentityAzureBlobBackupStorageDescription All required parameters must be populated in order to send to Azure.</td>
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
    <td><a href="#get_backup_policy_by_name"><CopyableCode code="get_backup_policy_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets a particular backup policy by name. Gets a particular backup policy identified by &#123;backupPolicyName&#125;.</td>
</tr>
<tr>
    <td><a href="#create_backup_policy"><CopyableCode code="create_backup_policy" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Name"><code>Name</code></a>, <a href="#parameter-AutoRestoreOnDataLoss"><code>AutoRestoreOnDataLoss</code></a>, <a href="#parameter-MaxIncrementalBackups"><code>MaxIncrementalBackups</code></a>, <a href="#parameter-Schedule"><code>Schedule</code></a>, <a href="#parameter-Storage"><code>Storage</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-ValidateConnection"><code>ValidateConnection</code></a></td>
    <td>Creates a backup policy. Creates a backup policy which can be associated later with a Service Fabric application, service or a partition for periodic backup.</td>
</tr>
<tr>
    <td><a href="#delete_backup_policy"><CopyableCode code="delete_backup_policy" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes the backup policy. Deletes an existing backup policy. A backup policy must be created before it can be deleted. A currently active backup policy, associated with any Service Fabric application, service or partition, cannot be deleted without first deleting the mapping.</td>
</tr>
<tr>
    <td><a href="#update_backup_policy"><CopyableCode code="update_backup_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-Name"><code>Name</code></a>, <a href="#parameter-AutoRestoreOnDataLoss"><code>AutoRestoreOnDataLoss</code></a>, <a href="#parameter-MaxIncrementalBackups"><code>MaxIncrementalBackups</code></a>, <a href="#parameter-Schedule"><code>Schedule</code></a>, <a href="#parameter-Storage"><code>Storage</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-ValidateConnection"><code>ValidateConnection</code></a></td>
    <td>Updates the backup policy. Updates the backup policy identified by &#123;backupPolicyName&#125;.</td>
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
<tr id="parameter-backup_policy_name">
    <td><CopyableCode code="backup_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the backup policy.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-ValidateConnection">
    <td><CopyableCode code="ValidateConnection" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to validate the storage connection and credentials before creating or updating the backup policies.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_backup_policy_by_name"
    values={[
        { label: 'get_backup_policy_by_name', value: 'get_backup_policy_by_name' }
    ]}
>
<TabItem value="get_backup_policy_by_name">

Gets a particular backup policy by name. Gets a particular backup policy identified by &#123;backupPolicyName&#125;.

```sql
SELECT
AutoRestoreOnDataLoss,
MaxIncrementalBackups,
Name,
RetentionPolicy,
Schedule,
Storage
FROM azure.service_fabric_dataplane.backup_policies
WHERE backup_policy_name = '{{ backup_policy_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_backup_policy"
    values={[
        { label: 'create_backup_policy', value: 'create_backup_policy' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_backup_policy">

Creates a backup policy. Creates a backup policy which can be associated later with a Service Fabric application, service or a partition for periodic backup.

```sql
INSERT INTO azure.service_fabric_dataplane.backup_policies (
Name,
AutoRestoreOnDataLoss,
MaxIncrementalBackups,
Schedule,
Storage,
RetentionPolicy,
endpoint,
timeout,
ValidateConnection
)
SELECT 
'{{ Name }}' /* required */,
{{ AutoRestoreOnDataLoss }} /* required */,
{{ MaxIncrementalBackups }} /* required */,
'{{ Schedule }}' /* required */,
'{{ Storage }}' /* required */,
'{{ RetentionPolicy }}',
'{{ endpoint }}',
'{{ timeout }}',
'{{ ValidateConnection }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: backup_policies
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the backup_policies resource.
    - name: Name
      value: "{{ Name }}"
    - name: AutoRestoreOnDataLoss
      value: {{ AutoRestoreOnDataLoss }}
    - name: MaxIncrementalBackups
      value: {{ MaxIncrementalBackups }}
    - name: Schedule
      description: |
        Describes the backup schedule parameters. You probably want to use the sub-classes and not this class directly. Known sub-classes are: FrequencyBasedBackupScheduleDescription, TimeBasedBackupScheduleDescription All required parameters must be populated in order to send to Azure.
      value:
        ScheduleKind: "{{ ScheduleKind }}"
    - name: Storage
      description: |
        Describes the parameters for the backup storage. You probably want to use the sub-classes and not this class directly. Known sub-classes are: AzureBlobBackupStorageDescription, FileShareBackupStorageDescription, DsmsAzureBlobBackupStorageDescription, ManagedIdentityAzureBlobBackupStorageDescription All required parameters must be populated in order to send to Azure.
      value:
        FriendlyName: "{{ FriendlyName }}"
        StorageKind: "{{ StorageKind }}"
    - name: RetentionPolicy
      description: |
        Describes the retention policy configured. You probably want to use the sub-classes and not this class directly. Known sub-classes are: BasicRetentionPolicyDescription All required parameters must be populated in order to send to Azure.
      value:
        RetentionPolicyType: "{{ RetentionPolicyType }}"
    - name: timeout
      value: "{{ timeout }}"
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    - name: ValidateConnection
      value: {{ ValidateConnection }}
      description: Specifies whether to validate the storage connection and credentials before creating or updating the backup policies.
      description: Specifies whether to validate the storage connection and credentials before creating or updating the backup policies.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_backup_policy"
    values={[
        { label: 'delete_backup_policy', value: 'delete_backup_policy' }
    ]}
>
<TabItem value="delete_backup_policy">

Deletes the backup policy. Deletes an existing backup policy. A backup policy must be created before it can be deleted. A currently active backup policy, associated with any Service Fabric application, service or partition, cannot be deleted without first deleting the mapping.

```sql
DELETE FROM azure.service_fabric_dataplane.backup_policies
WHERE backup_policy_name = '{{ backup_policy_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_backup_policy"
    values={[
        { label: 'update_backup_policy', value: 'update_backup_policy' }
    ]}
>
<TabItem value="update_backup_policy">

Updates the backup policy. Updates the backup policy identified by &#123;backupPolicyName&#125;.

```sql
EXEC azure.service_fabric_dataplane.backup_policies.update_backup_policy 
@backup_policy_name='{{ backup_policy_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}', 
@ValidateConnection={{ ValidateConnection }} 
@@json=
'{
"Name": "{{ Name }}", 
"AutoRestoreOnDataLoss": {{ AutoRestoreOnDataLoss }}, 
"MaxIncrementalBackups": {{ MaxIncrementalBackups }}, 
"Schedule": "{{ Schedule }}", 
"Storage": "{{ Storage }}", 
"RetentionPolicy": "{{ RetentionPolicy }}"
}'
;
```
</TabItem>
</Tabs>
