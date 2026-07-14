--- 
title: recoverable_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - recoverable_servers
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

Creates, updates, deletes, gets or lists a <code>recoverable_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recoverable_servers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.rdbms.recoverable_servers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="edition" /></td>
    <td><code>string</code></td>
    <td>Edition of the performance tier.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareGeneration" /></td>
    <td><code>string</code></td>
    <td>Hardware generation associated with the service level objective.</td>
</tr>
<tr>
    <td><CopyableCode code="lastAvailableBackupDateTime" /></td>
    <td><code>string</code></td>
    <td>The last available backup date time.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevelObjective" /></td>
    <td><code>string</code></td>
    <td>The service level objective.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vCore" /></td>
    <td><code>integer</code></td>
    <td>vCore associated with the service level objective.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The PostgreSQL version.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a recoverable MariaDB Server.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a recoverable MariaDB Server.

```sql
SELECT
id,
name,
edition,
hardwareGeneration,
lastAvailableBackupDateTime,
serviceLevelObjective,
type,
vCore,
version
FROM azure_extras.rdbms.recoverable_servers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
