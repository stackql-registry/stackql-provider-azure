--- 
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
  - netapp
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.backup_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="backupPolicyId" /></td>
    <td><code>string</code></td>
    <td>Backup Policy GUID ID.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyBackupsToKeep" /></td>
    <td><code>integer</code></td>
    <td>Daily backups count to keep.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The property to decide policy is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyBackupsToKeep" /></td>
    <td><code>integer</code></td>
    <td>Monthly backups count to keep.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeBackups" /></td>
    <td><code>array</code></td>
    <td>A list of volumes assigned to this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="volumesAssigned" /></td>
    <td><code>integer</code></td>
    <td>Volumes using current backup policy.</td>
</tr>
<tr>
    <td><CopyableCode code="weeklyBackupsToKeep" /></td>
    <td><code>integer</code></td>
    <td>Weekly backups count to keep.</td>
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
    <td><CopyableCode code="backupPolicyId" /></td>
    <td><code>string</code></td>
    <td>Backup Policy GUID ID.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyBackupsToKeep" /></td>
    <td><code>integer</code></td>
    <td>Daily backups count to keep.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The property to decide policy is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>"If etag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.").</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyBackupsToKeep" /></td>
    <td><code>integer</code></td>
    <td>Monthly backups count to keep.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumeBackups" /></td>
    <td><code>array</code></td>
    <td>A list of volumes assigned to this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="volumesAssigned" /></td>
    <td><code>integer</code></td>
    <td>Volumes using current backup policy.</td>
</tr>
<tr>
    <td><CopyableCode code="weeklyBackupsToKeep" /></td>
    <td><code>integer</code></td>
    <td>Weekly backups count to keep.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a particular backup Policy.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List backup policies for Netapp Account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a backup policy for Netapp Account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a backup policy for Netapp Account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-backup_policy_name"><code>backup_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete backup policy.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NetApp account. Required.</td>
</tr>
<tr id="parameter-backup_policy_name">
    <td><CopyableCode code="backup_policy_name" /></td>
    <td><code>string</code></td>
    <td>Backup policy Name which uniquely identify backup policy. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a particular backup Policy.

```sql
SELECT
id,
name,
backupPolicyId,
dailyBackupsToKeep,
enabled,
etag,
location,
monthlyBackupsToKeep,
provisioningState,
systemData,
tags,
type,
volumeBackups,
volumesAssigned,
weeklyBackupsToKeep
FROM azure.netapp.backup_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND backup_policy_name = '{{ backup_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List backup policies for Netapp Account.

```sql
SELECT
id,
name,
backupPolicyId,
dailyBackupsToKeep,
enabled,
etag,
location,
monthlyBackupsToKeep,
provisioningState,
systemData,
tags,
type,
volumeBackups,
volumesAssigned,
weeklyBackupsToKeep
FROM azure.netapp.backup_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

Create a backup policy for Netapp Account.

```sql
INSERT INTO azure.netapp.backup_policies (
tags,
location,
properties,
resource_group_name,
account_name,
backup_policy_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ backup_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: backup_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the backup_policies resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the backup_policies resource.
    - name: backup_policy_name
      value: "{{ backup_policy_name }}"
      description: Required parameter for the backup_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the backup_policies resource.
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
        Backup policy Properties. Required.
      value:
        backupPolicyId: "{{ backupPolicyId }}"
        provisioningState: "{{ provisioningState }}"
        dailyBackupsToKeep: {{ dailyBackupsToKeep }}
        weeklyBackupsToKeep: {{ weeklyBackupsToKeep }}
        monthlyBackupsToKeep: {{ monthlyBackupsToKeep }}
        volumesAssigned: {{ volumesAssigned }}
        enabled: {{ enabled }}
        volumeBackups:
          - volumeName: "{{ volumeName }}"
            volumeResourceId: "{{ volumeResourceId }}"
            backupsCount: {{ backupsCount }}
            policyEnabled: {{ policyEnabled }}
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

Patch a backup policy for Netapp Account.

```sql
UPDATE azure.netapp.backup_policies
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND backup_policy_name = '{{ backup_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete backup policy.

```sql
DELETE FROM azure.netapp.backup_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND backup_policy_name = '{{ backup_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
