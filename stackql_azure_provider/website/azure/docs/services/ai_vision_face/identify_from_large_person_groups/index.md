--- 
title: identify_from_large_person_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - identify_from_large_person_groups
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

Creates, updates, deletes, gets or lists an <code>identify_from_large_person_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="identify_from_large_person_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.identify_from_large_person_groups" /></td></tr>
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
    <td><a href="#identify_from_large_person_group"><CopyableCode code="identify_from_large_person_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>1-to-many identification to find the closest matches of the specific query person face from a Large Person Group. Please refer to https://learn.microsoft.com/rest/api/face/face-recognition-operations/identify-from-person-group for more details.</td>
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
    defaultValue="identify_from_large_person_group"
    values={[
        { label: 'identify_from_large_person_group', value: 'identify_from_large_person_group' }
    ]}
>
<TabItem value="identify_from_large_person_group">

1-to-many identification to find the closest matches of the specific query person face from a Large Person Group. Please refer to https://learn.microsoft.com/rest/api/face/face-recognition-operations/identify-from-person-group for more details.

```sql
EXEC azure.ai_vision_face.identify_from_large_person_groups.identify_from_large_person_group 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
</Tabs>
