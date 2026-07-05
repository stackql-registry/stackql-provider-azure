--- 
title: copy_model_tos
hide_title: false
hide_table_of_contents: false
keywords:
  - copy_model_tos
  - ai_documentintelligence
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

Creates, updates, deletes, gets or lists a <code>copy_model_tos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="copy_model_tos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_documentintelligence.copy_model_tos" /></td></tr>
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
    <td><a href="#copy_model_to"><CopyableCode code="copy_model_to" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-targetResourceRegion"><code>targetResourceRegion</code></a>, <a href="#parameter-targetModelId"><code>targetModelId</code></a>, <a href="#parameter-targetModelLocation"><code>targetModelLocation</code></a>, <a href="#parameter-accessToken"><code>accessToken</code></a>, <a href="#parameter-expirationDateTime"><code>expirationDateTime</code></a></td>
    <td></td>
    <td>Copies document model to the target resource, region, and modelId.</td>
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
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="copy_model_to"
    values={[
        { label: 'copy_model_to', value: 'copy_model_to' }
    ]}
>
<TabItem value="copy_model_to">

Copies document model to the target resource, region, and modelId.

```sql
EXEC azure.ai_documentintelligence.copy_model_tos.copy_model_to 
@model_id='{{ model_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"targetResourceRegion": "{{ targetResourceRegion }}", 
"targetModelId": "{{ targetModelId }}", 
"targetModelLocation": "{{ targetModelLocation }}", 
"accessToken": "{{ accessToken }}", 
"expirationDateTime": "{{ expirationDateTime }}"
}'
;
```
</TabItem>
</Tabs>
