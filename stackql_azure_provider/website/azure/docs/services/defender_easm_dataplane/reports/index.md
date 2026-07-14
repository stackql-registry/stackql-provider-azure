--- 
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - defender_easm_dataplane
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.defender_easm_dataplane.reports" /></td></tr>
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
    <td><a href="#billable"><CopyableCode code="billable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get billable assets summary for the workspace. Get billable assets summary for the workspace.</td>
</tr>
<tr>
    <td><a href="#snapshot"><CopyableCode code="snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the most recent snapshot of asset summary values for the snapshot request. Get the most recent snapshot of asset summary values for the snapshot request.</td>
</tr>
<tr>
    <td><a href="#summary"><CopyableCode code="summary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get asset summary details for the summary request. Get asset summary details for the summary request.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="billable"
    values={[
        { label: 'billable', value: 'billable' },
        { label: 'snapshot', value: 'snapshot' },
        { label: 'summary', value: 'summary' }
    ]}
>
<TabItem value="billable">

Get billable assets summary for the workspace. Get billable assets summary for the workspace.

```sql
EXEC azure.defender_easm_dataplane.reports.billable 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="snapshot">

Get the most recent snapshot of asset summary values for the snapshot request. Get the most recent snapshot of asset summary values for the snapshot request.

```sql
EXEC azure.defender_easm_dataplane.reports.snapshot 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="summary">

Get asset summary details for the summary request. Get asset summary details for the summary request.

```sql
EXEC azure.defender_easm_dataplane.reports.summary 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
