--- 
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - appconfiguration_dataplane
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

Creates, updates, deletes, gets or lists a <code>labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="labels" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appconfiguration_dataplane.labels" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_labels"
    values={[
        { label: 'get_labels', value: 'get_labels' }
    ]}
>
<TabItem value="get_labels">

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
    <td>The name of the label.</td>
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
    <td><a href="#get_labels"><CopyableCode code="get_labels" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-Sync-Token"><code>Sync-Token</code></a>, <a href="#parameter-After"><code>After</code></a>, <a href="#parameter-Accept-Datetime"><code>Accept-Datetime</code></a>, <a href="#parameter-$Select"><code>$Select</code></a></td>
    <td>Gets a list of labels. Gets a list of labels.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-$Select">
    <td><CopyableCode code="$Select" /></td>
    <td><code>array</code></td>
    <td>Used to select what fields are present in the returned resource(s). Default value is None.</td>
</tr>
<tr id="parameter-Accept-Datetime">
    <td><CopyableCode code="Accept-Datetime" /></td>
    <td><code>string</code></td>
    <td>Requests the server to respond with the state of the resource at the specified time. Default value is None.</td>
</tr>
<tr id="parameter-After">
    <td><CopyableCode code="After" /></td>
    <td><code>string</code></td>
    <td>Instructs the server to return elements that appear after the element referred to by the specified token. Default value is None.</td>
</tr>
<tr id="parameter-Sync-Token">
    <td><CopyableCode code="Sync-Token" /></td>
    <td><code>string</code></td>
    <td>Used to guarantee real-time consistency between requests. Default value is None.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A filter for the name of the returned labels. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_labels"
    values={[
        { label: 'get_labels', value: 'get_labels' }
    ]}
>
<TabItem value="get_labels">

Gets a list of labels. Gets a list of labels.

```sql
SELECT
name
FROM azure.appconfiguration_dataplane.labels
WHERE endpoint = '{{ endpoint }}' -- required
AND name = '{{ name }}'
AND Sync-Token = '{{ Sync-Token }}'
AND After = '{{ After }}'
AND Accept-Datetime = '{{ Accept-Datetime }}'
AND $Select = '{{ $Select }}'
;
```
</TabItem>
</Tabs>
