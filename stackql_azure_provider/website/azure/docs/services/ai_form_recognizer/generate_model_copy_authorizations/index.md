--- 
title: generate_model_copy_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_model_copy_authorizations
  - ai_form_recognizer
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

Creates, updates, deletes, gets or lists a <code>generate_model_copy_authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="generate_model_copy_authorizations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_form_recognizer.generate_model_copy_authorizations" /></td></tr>
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
    <td><a href="#generate_model_copy_authorization"><CopyableCode code="generate_model_copy_authorization" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Generate Copy Authorization. Generate authorization to copy a model into the target Form Recognizer resource.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="generate_model_copy_authorization"
    values={[
        { label: 'generate_model_copy_authorization', value: 'generate_model_copy_authorization' }
    ]}
>
<TabItem value="generate_model_copy_authorization">

Generate Copy Authorization. Generate authorization to copy a model into the target Form Recognizer resource.

```sql
EXEC azure.ai_form_recognizer.generate_model_copy_authorizations.generate_model_copy_authorization 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
