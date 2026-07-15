--- 
title: skillsets
hide_title: false
hide_table_of_contents: false
keywords:
  - skillsets
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

Creates, updates, deletes, gets or lists a <code>skillsets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="skillsets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search_documents.skillsets" /></td></tr>
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
    <td><a href="#create_skillset"><CopyableCode code="create_skillset" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Creates a new skillset in a search service.</td>
</tr>
<tr>
    <td><a href="#get_skillset"><CopyableCode code="get_skillset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-skillset_name"><code>skillset_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a></td>
    <td></td>
    <td>Retrieves a skillset in a search service.</td>
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
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>Search service name. (default: )</td>
</tr>
<tr id="parameter-skillset_name">
    <td><CopyableCode code="skillset_name" /></td>
    <td><code>string</code></td>
    <td>The name of the skillset. Required.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_skillset"
    values={[
        { label: 'create_skillset', value: 'create_skillset' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_skillset">

Creates a new skillset in a search service.

```sql
INSERT INTO azure.search_documents.skillsets (
search_service_name
)
SELECT 
'{{ search_service_name }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: skillsets
  props:
    - name: search_service_name
      value: "{{ search_service_name }}"
      description: Required parameter for the skillsets resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_skillset"
    values={[
        { label: 'get_skillset', value: 'get_skillset' }
    ]}
>
<TabItem value="get_skillset">

Retrieves a skillset in a search service.

```sql
EXEC azure.search_documents.skillsets.get_skillset 
@skillset_name='{{ skillset_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required
;
```
</TabItem>
</Tabs>
