--- 
title: deidentify_documents
hide_title: false
hide_table_of_contents: false
keywords:
  - deidentify_documents
  - health_deidentification
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

Creates, updates, deletes, gets or lists a <code>deidentify_documents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deidentify_documents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.health_deidentification.deidentify_documents" /></td></tr>
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
    <td><a href="#deidentify_documents"><CopyableCode code="deidentify_documents" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-sourceLocation"><code>sourceLocation</code></a>, <a href="#parameter-targetLocation"><code>targetLocation</code></a></td>
    <td></td>
    <td>Create a de-identification job. Long-running resource create or replace operation template.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of a job. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="deidentify_documents"
    values={[
        { label: 'deidentify_documents', value: 'deidentify_documents' }
    ]}
>
<TabItem value="deidentify_documents">

Create a de-identification job. Long-running resource create or replace operation template.

```sql
EXEC azure.health_deidentification.deidentify_documents.deidentify_documents 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"operation": "{{ operation }}", 
"sourceLocation": "{{ sourceLocation }}", 
"targetLocation": "{{ targetLocation }}", 
"customizations": "{{ customizations }}"
}'
;
```
</TabItem>
</Tabs>
