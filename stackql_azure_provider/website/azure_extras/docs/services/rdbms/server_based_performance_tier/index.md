--- 
title: server_based_performance_tier
hide_title: false
hide_table_of_contents: false
keywords:
  - server_based_performance_tier
  - rdbms
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>server_based_performance_tier</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_based_performance_tier" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.rdbms.server_based_performance_tier" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>ID of the performance tier.</td>
</tr>
<tr>
    <td><CopyableCode code="maxBackupRetentionDays" /></td>
    <td><code>integer</code></td>
    <td>Maximum Backup retention in days for the performance tier edition.</td>
</tr>
<tr>
    <td><CopyableCode code="maxLargeStorageMB" /></td>
    <td><code>integer</code></td>
    <td>Max storage allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="maxStorageMB" /></td>
    <td><code>integer</code></td>
    <td>Max storage allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="minBackupRetentionDays" /></td>
    <td><code>integer</code></td>
    <td>Minimum Backup retention in days for the performance tier edition.</td>
</tr>
<tr>
    <td><CopyableCode code="minLargeStorageMB" /></td>
    <td><code>integer</code></td>
    <td>Max storage allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="minStorageMB" /></td>
    <td><code>integer</code></td>
    <td>Max storage allowed for a server.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevelObjectives" /></td>
    <td><code>array</code></td>
    <td>Service level objectives associated with the performance tier.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the performance tiers for a MariaDB server.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List all the performance tiers for a MariaDB server.

```sql
SELECT
id,
maxBackupRetentionDays,
maxLargeStorageMB,
maxStorageMB,
minBackupRetentionDays,
minLargeStorageMB,
minStorageMB,
serviceLevelObjectives
FROM azure_extras.rdbms.server_based_performance_tier
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
