--- 
title: file_share_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - file_share_snapshots
  - file_shares
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

Creates, updates, deletes, gets or lists a <code>file_share_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="file_share_snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.file_shares.file_share_snapshots" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_file_share_snapshot"
    values={[
        { label: 'get_file_share_snapshot', value: 'get_file_share_snapshot' },
        { label: 'list_by_file_share', value: 'list_by_file_share' }
    ]}
>
<TabItem value="get_file_share_snapshot">

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
    <td><CopyableCode code="initiatorId" /></td>
    <td><code>string</code></td>
    <td>The initiator of the FileShareSnapshot. This is a user-defined value.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotTime" /></td>
    <td><code>string</code></td>
    <td>The FileShareSnapshot time in UTC in string representation.</td>
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
<TabItem value="list_by_file_share">

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
    <td><CopyableCode code="initiatorId" /></td>
    <td><code>string</code></td>
    <td>The initiator of the FileShareSnapshot. This is a user-defined value.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="snapshotTime" /></td>
    <td><code>string</code></td>
    <td>The FileShareSnapshot time in UTC in string representation.</td>
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
    <td><a href="#get_file_share_snapshot"><CopyableCode code="get_file_share_snapshot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a FileShareSnapshot.</td>
</tr>
<tr>
    <td><a href="#list_by_file_share"><CopyableCode code="list_by_file_share" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List FileShareSnapshot by FileShare.</td>
</tr>
<tr>
    <td><a href="#create_or_update_file_share_snapshot"><CopyableCode code="create_or_update_file_share_snapshot" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a FileShareSnapshot.</td>
</tr>
<tr>
    <td><a href="#update_file_share_snapshot"><CopyableCode code="update_file_share_snapshot" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a FileShareSnapshot.</td>
</tr>
<tr>
    <td><a href="#create_or_update_file_share_snapshot"><CopyableCode code="create_or_update_file_share_snapshot" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a FileShareSnapshot.</td>
</tr>
<tr>
    <td><a href="#delete_file_share_snapshot"><CopyableCode code="delete_file_share_snapshot" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a FileShareSnapshot.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the FileShareSnapshot. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The resource name of the file share, as seen by the administrator through Azure Resource Manager. Required.</td>
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
    defaultValue="get_file_share_snapshot"
    values={[
        { label: 'get_file_share_snapshot', value: 'get_file_share_snapshot' },
        { label: 'list_by_file_share', value: 'list_by_file_share' }
    ]}
>
<TabItem value="get_file_share_snapshot">

Get a FileShareSnapshot.

```sql
SELECT
id,
name,
initiatorId,
metadata,
snapshotTime,
systemData,
type
FROM azure.file_shares.file_share_snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_file_share">

List FileShareSnapshot by FileShare.

```sql
SELECT
id,
name,
initiatorId,
metadata,
snapshotTime,
systemData,
type
FROM azure.file_shares.file_share_snapshots
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_file_share_snapshot"
    values={[
        { label: 'create_or_update_file_share_snapshot', value: 'create_or_update_file_share_snapshot' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_file_share_snapshot">

Create a FileShareSnapshot.

```sql
INSERT INTO azure.file_shares.file_share_snapshots (
properties,
resource_group_name,
resource_name,
name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ name }}',
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
- name: file_share_snapshots
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the file_share_snapshots resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the file_share_snapshots resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the file_share_snapshots resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the file_share_snapshots resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        snapshotTime: "{{ snapshotTime }}"
        initiatorId: "{{ initiatorId }}"
        metadata: "{{ metadata }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_file_share_snapshot"
    values={[
        { label: 'update_file_share_snapshot', value: 'update_file_share_snapshot' }
    ]}
>
<TabItem value="update_file_share_snapshot">

Update a FileShareSnapshot.

```sql
UPDATE azure.file_shares.file_share_snapshots
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND name = '{{ name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_file_share_snapshot"
    values={[
        { label: 'create_or_update_file_share_snapshot', value: 'create_or_update_file_share_snapshot' }
    ]}
>
<TabItem value="create_or_update_file_share_snapshot">

Create a FileShareSnapshot.

```sql
REPLACE azure.file_shares.file_share_snapshots
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND name = '{{ name }}' --required
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
    defaultValue="delete_file_share_snapshot"
    values={[
        { label: 'delete_file_share_snapshot', value: 'delete_file_share_snapshot' }
    ]}
>
<TabItem value="delete_file_share_snapshot">

Delete a FileShareSnapshot.

```sql
DELETE FROM azure.file_shares.file_share_snapshots
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
