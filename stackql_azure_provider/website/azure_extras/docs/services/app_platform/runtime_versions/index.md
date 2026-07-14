--- 
title: runtime_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_versions
  - app_platform
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

Creates, updates, deletes, gets or lists a <code>runtime_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="runtime_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_platform.runtime_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_runtime_versions"
    values={[
        { label: 'list_runtime_versions', value: 'list_runtime_versions' }
    ]}
>
<TabItem value="list_runtime_versions">

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
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>A list of all supported runtime versions.</td>
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
    <td><a href="#list_runtime_versions"><CopyableCode code="list_runtime_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists all of the available runtime versions supported by Microsoft.AppPlatform provider.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_runtime_versions"
    values={[
        { label: 'list_runtime_versions', value: 'list_runtime_versions' }
    ]}
>
<TabItem value="list_runtime_versions">

Lists all of the available runtime versions supported by Microsoft.AppPlatform provider.

```sql
SELECT
value
FROM azure_extras.app_platform.runtime_versions
;
```
</TabItem>
</Tabs>
