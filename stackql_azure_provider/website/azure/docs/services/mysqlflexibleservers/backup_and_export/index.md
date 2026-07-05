--- 
title: backup_and_export
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_and_export
  - mysqlflexibleservers
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

Creates, updates, deletes, gets or lists a <code>backup_and_export</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="backup_and_export" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysqlflexibleservers.backup_and_export" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-backupSettings"><code>backupSettings</code></a>, <a href="#parameter-targetDetails"><code>targetDetails</code></a></td>
    <td></td>
    <td>Exports the backup of the given server by creating a backup if not existing.</td>
</tr>
<tr>
    <td><a href="#validate_backup"><CopyableCode code="validate_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates if backup can be performed for given server.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Exports the backup of the given server by creating a backup if not existing.

```sql
INSERT INTO azure.mysqlflexibleservers.backup_and_export (
backupSettings,
targetDetails,
resource_group_name,
server_name,
subscription_id
)
SELECT 
'{{ backupSettings }}' /* required */,
'{{ targetDetails }}' /* required */,
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
endTime,
error,
percentComplete,
properties,
startTime,
status,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: backup_and_export
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the backup_and_export resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the backup_and_export resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the backup_and_export resource.
    - name: backupSettings
      description: |
        Backup Settings. Required.
      value:
        backupName: "{{ backupName }}"
        backupFormat: "{{ backupFormat }}"
    - name: targetDetails
      description: |
        Backup Target Store Details. Required.
      value:
        objectType: "{{ objectType }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_backup"
    values={[
        { label: 'validate_backup', value: 'validate_backup' }
    ]}
>
<TabItem value="validate_backup">

Validates if backup can be performed for given server.

```sql
EXEC azure.mysqlflexibleservers.backup_and_export.validate_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@server_name='{{ server_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
