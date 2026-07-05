--- 
title: synonym_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - synonym_maps
  - search_documents
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

Creates, updates, deletes, gets or lists a <code>synonym_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synonym_maps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.synonym_maps" /></td></tr>
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
    <td><a href="#create_synonym_map"><CopyableCode code="create_synonym_map" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a new synonym map.</td>
</tr>
<tr>
    <td><a href="#get_synonym_map"><CopyableCode code="get_synonym_map" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-synonym_map_name"><code>synonym_map_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Retrieves a synonym map definition.</td>
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
<tr id="parameter-synonym_map_name">
    <td><CopyableCode code="synonym_map_name" /></td>
    <td><code>string</code></td>
    <td>The name of the synonym map. Required.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_synonym_map"
    values={[
        { label: 'create_synonym_map', value: 'create_synonym_map' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_synonym_map">

Creates a new synonym map.

```sql
INSERT INTO azure.search_documents.synonym_maps (
endpoint
)
SELECT 
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: synonym_maps
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the synonym_maps resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_synonym_map"
    values={[
        { label: 'get_synonym_map', value: 'get_synonym_map' }
    ]}
>
<TabItem value="get_synonym_map">

Retrieves a synonym map definition.

```sql
EXEC azure.search_documents.synonym_maps.get_synonym_map 
@synonym_map_name='{{ synonym_map_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
