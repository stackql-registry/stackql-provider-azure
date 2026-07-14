--- 
title: synchronization_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_settings
  - data_share
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

Creates, updates, deletes, gets or lists a <code>synchronization_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.synchronization_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_share', value: 'list_by_share' }
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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of synchronization setting. Required. "ScheduleBased"</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_share">

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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of synchronization setting. Required. "ScheduleBased"</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-synchronization_setting_name"><code>synchronization_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get synchronizationSetting in a share. Get a synchronizationSetting in a share.</td>
</tr>
<tr>
    <td><a href="#list_by_share"><CopyableCode code="list_by_share" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List synchronizationSettings in a share. List synchronizationSettings in a share.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-synchronization_setting_name"><code>synchronization_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Adds a new synchronization setting to an existing share. Create a synchronizationSetting.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_name"><code>share_name</code></a>, <a href="#parameter-synchronization_setting_name"><code>synchronization_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete synchronizationSetting in a share. Delete a synchronizationSetting in a share.</td>
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
    <td>The name of the share account. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-share_name">
    <td><CopyableCode code="share_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-synchronization_setting_name">
    <td><CopyableCode code="synchronization_setting_name" /></td>
    <td><code>string</code></td>
    <td>The name of the synchronizationSetting . Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>continuation token. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_share', value: 'list_by_share' }
    ]}
>
<TabItem value="get">

Get synchronizationSetting in a share. Get a synchronizationSetting in a share.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.data_share.synchronization_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND synchronization_setting_name = '{{ synchronization_setting_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_share">

List synchronizationSettings in a share. List synchronizationSettings in a share.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.data_share.synchronization_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_name = '{{ share_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
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

Adds a new synchronization setting to an existing share. Create a synchronizationSetting.

```sql
INSERT INTO azure.data_share.synchronization_settings (
kind,
resource_group_name,
account_name,
share_name,
synchronization_setting_name,
subscription_id
)
SELECT 
'{{ kind }}' /* required */,
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ share_name }}',
'{{ synchronization_setting_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: synchronization_settings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the synchronization_settings resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the synchronization_settings resource.
    - name: share_name
      value: "{{ share_name }}"
      description: Required parameter for the synchronization_settings resource.
    - name: synchronization_setting_name
      value: "{{ synchronization_setting_name }}"
      description: Required parameter for the synchronization_settings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the synchronization_settings resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of synchronization setting. Required. "ScheduleBased"
`}</CodeBlock>

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

Delete synchronizationSetting in a share. Delete a synchronizationSetting in a share.

```sql
DELETE FROM azure.data_share.synchronization_settings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND share_name = '{{ share_name }}' --required
AND synchronization_setting_name = '{{ synchronization_setting_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
