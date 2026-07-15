--- 
title: embeds
hide_title: false
hide_table_of_contents: false
keywords:
  - embeds
  - ai_inference
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

Creates, updates, deletes, gets or lists an <code>embeds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="embeds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_inference.embeds" /></td></tr>
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
    <td><a href="#embed"><CopyableCode code="embed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-extra-parameters"><code>extra-parameters</code></a></td>
    <td>Return the embedding vectors for given text prompts. The method makes a REST API call to the `/embeddings` route on the given endpoint.</td>
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
<tr id="parameter-extra-parameters">
    <td><CopyableCode code="extra-parameters" /></td>
    <td><code>string</code></td>
    <td>Controls what happens if extra parameters, undefined by the REST API, are passed in the JSON request payload. This sets the HTTP request header `extra-parameters`. Known values are: "error", "drop", and "pass-through". Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="embed"
    values={[
        { label: 'embed', value: 'embed' }
    ]}
>
<TabItem value="embed">

Return the embedding vectors for given text prompts. The method makes a REST API call to the `/embeddings` route on the given endpoint.

```sql
EXEC azure.ai_inference.embeds.embed 
@endpoint='{{ endpoint }}' --required, 
@extra-parameters='{{ extra-parameters }}'
;
```
</TabItem>
</Tabs>
