--- 
title: import_assets
hide_title: false
hide_table_of_contents: false
keywords:
  - import_assets
  - ai_language
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

Creates, updates, deletes, gets or lists an <code>import_assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="import_assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language.import_assets" /></td></tr>
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
    <td><a href="#import_assets"><CopyableCode code="import_assets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-assetKind"><code>assetKind</code></a></td>
    <td>Import project assets.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of the project to use. Required.</td>
</tr>
<tr id="parameter-assetKind">
    <td><CopyableCode code="assetKind" /></td>
    <td><code>string</code></td>
    <td>Kind of the asset of the project. Known values are: "qnas" and "synonyms". Default value is None.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Knowledge base Import or Export format. Known values are: "json", "tsv", and "excel". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="import_assets"
    values={[
        { label: 'import_assets', value: 'import_assets' }
    ]}
>
<TabItem value="import_assets">

Import project assets.

```sql
EXEC azure.ai_language.import_assets.import_assets 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@format='{{ format }}', 
@assetKind='{{ assetKind }}' 
@@json=
'{
"metadata": "{{ metadata }}", 
"assets": "{{ assets }}", 
"fileUri": "{{ fileUri }}"
}'
;
```
</TabItem>
</Tabs>
