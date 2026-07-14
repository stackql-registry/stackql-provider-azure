--- 
title: authorize_model_copies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorize_model_copies
  - ai_document_intelligence
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

Creates, updates, deletes, gets or lists an <code>authorize_model_copies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authorize_model_copies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.authorize_model_copies" /></td></tr>
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
    <td><a href="#authorize_model_copy"><CopyableCode code="authorize_model_copy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-modelId"><code>modelId</code></a></td>
    <td></td>
    <td>Generates authorization to copy a document model to this location with specified modelId and optional description.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="authorize_model_copy"
    values={[
        { label: 'authorize_model_copy', value: 'authorize_model_copy' }
    ]}
>
<TabItem value="authorize_model_copy">

Generates authorization to copy a document model to this location with specified modelId and optional description.

```sql
EXEC azure.ai_document_intelligence.authorize_model_copies.authorize_model_copy 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"modelId": "{{ modelId }}", 
"description": "{{ description }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
</Tabs>
