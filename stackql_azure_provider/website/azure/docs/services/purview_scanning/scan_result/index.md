--- 
title: scan_result
hide_title: false
hide_table_of_contents: false
keywords:
  - scan_result
  - purview_scanning
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

Creates, updates, deletes, gets or lists a <code>scan_result</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scan_result" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_scanning.scan_result" /></td></tr>
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
    <td><a href="#list_scan_history"><CopyableCode code="list_scan_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists the scan history of a scan.</td>
</tr>
<tr>
    <td><a href="#run_scan"><CopyableCode code="run_scan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Runs the scan.</td>
</tr>
<tr>
    <td><a href="#cancel_scan"><CopyableCode code="cancel_scan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancels a scan.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_scan_history"
    values={[
        { label: 'list_scan_history', value: 'list_scan_history' },
        { label: 'run_scan', value: 'run_scan' },
        { label: 'cancel_scan', value: 'cancel_scan' }
    ]}
>
<TabItem value="list_scan_history">

Lists the scan history of a scan.

```sql
EXEC azure.purview_scanning.scan_result.list_scan_history 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="run_scan">

Runs the scan.

```sql
EXEC azure.purview_scanning.scan_result.run_scan 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_scan">

Cancels a scan.

```sql
EXEC azure.purview_scanning.scan_result.cancel_scan 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
