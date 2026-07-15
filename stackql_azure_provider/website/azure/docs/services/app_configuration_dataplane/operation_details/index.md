--- 
title: operation_details
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_details
  - app_configuration_dataplane
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

Creates, updates, deletes, gets or lists an <code>operation_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operation_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration_dataplane.operation_details" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_details"
    values={[
        { label: 'get_operation_details', value: 'get_operation_details' }
    ]}
>
<TabItem value="get_operation_details">

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
    <td>The unique id of the operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>An error, available when the status is `Failed`, describing why the operation failed.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the operation. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
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
    <td><a href="#get_operation_details"><CopyableCode code="get_operation_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-snapshot"><code>snapshot</code></a>, <a href="#parameter-config_store_name"><code>config_store_name</code></a></td>
    <td></td>
    <td>Gets the state of a long running operation. Gets the state of a long running operation.</td>
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
<tr id="parameter-config_store_name">
    <td><CopyableCode code="config_store_name" /></td>
    <td><code>string</code></td>
    <td>App Configuration store name. (default: )</td>
</tr>
<tr id="parameter-snapshot">
    <td><CopyableCode code="snapshot" /></td>
    <td><code>string</code></td>
    <td>Snapshot identifier for the long running operation. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_operation_details"
    values={[
        { label: 'get_operation_details', value: 'get_operation_details' }
    ]}
>
<TabItem value="get_operation_details">

Gets the state of a long running operation. Gets the state of a long running operation.

```sql
SELECT
id,
error,
status
FROM azure.app_configuration_dataplane.operation_details
WHERE snapshot = '{{ snapshot }}' -- required
AND config_store_name = '{{ config_store_name }}' -- required
;
```
</TabItem>
</Tabs>
