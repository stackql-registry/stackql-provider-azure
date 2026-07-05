--- 
title: system_scan_rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - system_scan_rulesets
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

Creates, updates, deletes, gets or lists a <code>system_scan_rulesets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="system_scan_rulesets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_scanning.system_scan_rulesets" /></td></tr>
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
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a system scan ruleset for a data source.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all system scan rulesets for an account.</td>
</tr>
<tr>
    <td><a href="#list_versions_by_data_source"><CopyableCode code="list_versions_by_data_source" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List system scan ruleset versions in Data catalog.</td>
</tr>
<tr>
    <td><a href="#get_by_version"><CopyableCode code="get_by_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a scan ruleset by version.</td>
</tr>
<tr>
    <td><a href="#get_latest"><CopyableCode code="get_latest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the latest version of a system scan ruleset.</td>
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
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'list_all', value: 'list_all' },
        { label: 'list_versions_by_data_source', value: 'list_versions_by_data_source' },
        { label: 'get_by_version', value: 'get_by_version' },
        { label: 'get_latest', value: 'get_latest' }
    ]}
>
<TabItem value="get_raw">

Get a system scan ruleset for a data source.

```sql
EXEC azure.purview_scanning.system_scan_rulesets.get_raw 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_all">

List all system scan rulesets for an account.

```sql
EXEC azure.purview_scanning.system_scan_rulesets.list_all 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_versions_by_data_source">

List system scan ruleset versions in Data catalog.

```sql
EXEC azure.purview_scanning.system_scan_rulesets.list_versions_by_data_source 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_by_version">

Get a scan ruleset by version.

```sql
EXEC azure.purview_scanning.system_scan_rulesets.get_by_version 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_latest">

Get the latest version of a system scan ruleset.

```sql
EXEC azure.purview_scanning.system_scan_rulesets.get_latest 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
