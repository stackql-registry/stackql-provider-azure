--- 
title: model_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - model_infos
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

Creates, updates, deletes, gets or lists a <code>model_infos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="model_infos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_inference.model_infos" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_model_info"
    values={[
        { label: 'get_model_info', value: 'get_model_info' }
    ]}
>
<TabItem value="get_model_info">

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
    <td><CopyableCode code="model_name" /></td>
    <td><code>string</code></td>
    <td>The name of the AI model. For example: `Phi21`. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="model_provider_name" /></td>
    <td><code>string</code></td>
    <td>The model provider name. For example: `Microsoft Research`. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="model_type" /></td>
    <td><code>string</code></td>
    <td>The type of the AI model. A Unique identifier for the profile. Required. Known values are: "embeddings", "image_generation", "text_generation", "image_embeddings", "audio_generation", and "chat_completion". (embeddings, image_generation, text_generation, image_embeddings, audio_generation, chat_completion)</td>
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
    <td><a href="#get_model_info"><CopyableCode code="get_model_info" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Returns information about the AI model. The method makes a REST API call to the `/info` route on the given endpoint. This method will only work when using Serverless API or Managed Compute endpoint. It will not work for GitHub Models endpoint or Azure OpenAI endpoint.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="get_model_info"
    values={[
        { label: 'get_model_info', value: 'get_model_info' }
    ]}
>
<TabItem value="get_model_info">

Returns information about the AI model. The method makes a REST API call to the `/info` route on the given endpoint. This method will only work when using Serverless API or Managed Compute endpoint. It will not work for GitHub Models endpoint or Azure OpenAI endpoint.

```sql
SELECT
model_name,
model_provider_name,
model_type
FROM azure.ai_inference.model_infos
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
