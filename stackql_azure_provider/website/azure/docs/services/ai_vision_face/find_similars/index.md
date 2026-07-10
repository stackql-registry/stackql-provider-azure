--- 
title: find_similars
hide_title: false
hide_table_of_contents: false
keywords:
  - find_similars
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

Creates, updates, deletes, gets or lists a <code>find_similars</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="find_similars" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.find_similars" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="find_similar"
    values={[
        { label: 'find_similar', value: 'find_similar' }
    ]}
>
<TabItem value="find_similar">

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
    <td><CopyableCode code="confidence" /></td>
    <td><code>number</code></td>
    <td>Confidence value of the candidate. The higher confidence, the more similar. Range between [0,1]. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="faceId" /></td>
    <td><code>string</code></td>
    <td>faceId of candidate face when find by faceIds. faceId is created by "Detect" and will expire 24 hours after the detection call.</td>
</tr>
<tr>
    <td><CopyableCode code="persistedFaceId" /></td>
    <td><code>string</code></td>
    <td>persistedFaceId of candidate face when find by faceListId or largeFaceListId. persistedFaceId in face list/large face list is persisted and will not expire.</td>
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
    <td><a href="#find_similar"><CopyableCode code="find_similar" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Given query face's faceId, to search the similar-looking faces from a faceId array. A faceId array contains the faces created by Detect. Please refer to https://learn.microsoft.com/rest/api/face/face-recognition-operations/find-similar for more details.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `apiVersion` parameter. (default: )</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="find_similar"
    values={[
        { label: 'find_similar', value: 'find_similar' }
    ]}
>
<TabItem value="find_similar">

Given query face's faceId, to search the similar-looking faces from a faceId array. A faceId array contains the faces created by Detect. Please refer to https://learn.microsoft.com/rest/api/face/face-recognition-operations/find-similar for more details.

```sql
SELECT
confidence,
faceId,
persistedFaceId
FROM azure.ai_vision_face.find_similars
WHERE endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
</Tabs>
