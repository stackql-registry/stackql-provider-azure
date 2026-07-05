--- 
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - ai_vision_face
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.groups" /></td></tr>
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
    <td><a href="#group"><CopyableCode code="group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Divide candidate faces into groups based on face similarity. Please refer to https://learn.microsoft.com/rest/api/face/face-recognition-operations/group for more details.</td>
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
<tr id="parameter-api_version">
    <td><CopyableCode code="api_version" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `apiVersion` parameter. (default: )</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="group"
    values={[
        { label: 'group', value: 'group' }
    ]}
>
<TabItem value="group">

Divide candidate faces into groups based on face similarity. Please refer to https://learn.microsoft.com/rest/api/face/face-recognition-operations/group for more details.

```sql
EXEC azure.ai_vision_face.groups.group 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
</Tabs>
