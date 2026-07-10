--- 
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - developer_devcenter
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_devcenter.pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_pool"
    values={[
        { label: 'get_pool', value: 'get_pool' },
        { label: 'list_pools', value: 'list_pools' }
    ]}
>
<TabItem value="get_pool">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Pool name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Hardware settings for the Dev Boxes created in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the Pool. Indicates whether or not the Pool is available to create Dev Boxes. Required. Known values are: "Unknown", "Pending", "Healthy", "Warning", and "Unhealthy". (Unknown, Pending, Healthy, Warning, Unhealthy)</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether hibernate is enabled/disabled or unknown. Known values are: "Enabled", "Disabled", and "OsUnsupported". (Enabled, Disabled, OsUnsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Image settings for Dev Boxes create in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="localAdministrator" /></td>
    <td><code>string</code></td>
    <td>Indicates whether owners of Dev Boxes in this pool are local administrators on the Dev Boxes. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region where Dev Boxes in the pool are located. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type of Dev Boxes in this pool. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="stopOnDisconnect" /></td>
    <td><code>object</code></td>
    <td>Stop on disconnect configuration settings for Dev Boxes created in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage settings for Dev Box created in this pool.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_pools">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Pool name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Hardware settings for the Dev Boxes created in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the Pool. Indicates whether or not the Pool is available to create Dev Boxes. Required. Known values are: "Unknown", "Pending", "Healthy", "Warning", and "Unhealthy". (Unknown, Pending, Healthy, Warning, Unhealthy)</td>
</tr>
<tr>
    <td><CopyableCode code="hibernateSupport" /></td>
    <td><code>string</code></td>
    <td>Indicates whether hibernate is enabled/disabled or unknown. Known values are: "Enabled", "Disabled", and "OsUnsupported". (Enabled, Disabled, OsUnsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>Image settings for Dev Boxes create in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="localAdministrator" /></td>
    <td><code>string</code></td>
    <td>Indicates whether owners of Dev Boxes in this pool are local administrators on the Dev Boxes. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure region where Dev Boxes in the pool are located. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type of Dev Boxes in this pool. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="stopOnDisconnect" /></td>
    <td><code>object</code></td>
    <td>Stop on disconnect configuration settings for Dev Boxes created in this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage settings for Dev Box created in this pool.</td>
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
    <td><a href="#get_pool"><CopyableCode code="get_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a pool.</td>
</tr>
<tr>
    <td><a href="#list_pools"><CopyableCode code="list_pools" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists available pools.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>Pool name. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_pool"
    values={[
        { label: 'get_pool', value: 'get_pool' },
        { label: 'list_pools', value: 'list_pools' }
    ]}
>
<TabItem value="get_pool">

Gets a pool.

```sql
SELECT
name,
hardwareProfile,
healthStatus,
hibernateSupport,
imageReference,
localAdministrator,
location,
osType,
stopOnDisconnect,
storageProfile
FROM azure.developer_devcenter.pools
WHERE project_name = '{{ project_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_pools">

Lists available pools.

```sql
SELECT
name,
hardwareProfile,
healthStatus,
hibernateSupport,
imageReference,
localAdministrator,
location,
osType,
stopOnDisconnect,
storageProfile
FROM azure.developer_devcenter.pools
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
