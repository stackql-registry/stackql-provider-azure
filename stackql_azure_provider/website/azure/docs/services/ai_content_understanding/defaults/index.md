--- 
title: defaults
hide_title: false
hide_table_of_contents: false
keywords:
  - defaults
  - ai_content_understanding
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

Creates, updates, deletes, gets or lists a <code>defaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="defaults" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_content_understanding.defaults" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_defaults"
    values={[
        { label: 'get_defaults', value: 'get_defaults' }
    ]}
>
<TabItem value="get_defaults">

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
    <td><CopyableCode code="modelDeployments" /></td>
    <td><code>object</code></td>
    <td>Specify the default mapping of model names to LLM/embedding deployments in Microsoft Foundry. For details and current semantics, see `https://aka.ms/cudoc-quickstart-rest `_. Required.</td>
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
    <td><a href="#get_defaults"><CopyableCode code="get_defaults" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Return default settings for this Content Understanding resource.</td>
</tr>
<tr>
    <td><a href="#update_defaults"><CopyableCode code="update_defaults" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update default settings for this Content Understanding resource.</td>
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
    defaultValue="get_defaults"
    values={[
        { label: 'get_defaults', value: 'get_defaults' }
    ]}
>
<TabItem value="get_defaults">

Return default settings for this Content Understanding resource.

```sql
SELECT
modelDeployments
FROM azure.ai_content_understanding.defaults
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_defaults"
    values={[
        { label: 'update_defaults', value: 'update_defaults' }
    ]}
>
<TabItem value="update_defaults">

Update default settings for this Content Understanding resource.

```sql
UPDATE azure.ai_content_understanding.defaults
SET 
-- No updatable properties
WHERE 
endpoint = '{{ endpoint }}' --required
RETURNING
modelDeployments;
```
</TabItem>
</Tabs>
