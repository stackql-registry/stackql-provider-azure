--- 
title: large_face_list
hide_title: false
hide_table_of_contents: false
keywords:
  - large_face_list
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

Creates, updates, deletes, gets or lists a <code>large_face_list</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="large_face_list" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.large_face_list" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_face"
    values={[
        { label: 'get_face', value: 'get_face' },
        { label: 'get', value: 'get' },
        { label: 'get_large_face_lists', value: 'get_large_face_lists' }
    ]}
>
<TabItem value="get_face">

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
    <td><CopyableCode code="persistedFaceId" /></td>
    <td><code>string</code></td>
    <td>Face ID of the face. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>User-provided data attached to the face. The length limit is 1K.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>User defined name, maximum length is 128. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="largeFaceListId" /></td>
    <td><code>string</code></td>
    <td>Valid character is letter in lower case or digit or '-' or '_', maximum length is 64. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="recognitionModel" /></td>
    <td><code>string</code></td>
    <td>Name of recognition model. Recognition model is used when the face features are extracted and associated with detected faceIds. Known values are: "recognition_01", "recognition_02", "recognition_03", and "recognition_04". (recognition_01, recognition_02, recognition_03, recognition_04)</td>
</tr>
<tr>
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>Optional user defined data. Length should not exceed 16K.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_large_face_lists">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>User defined name, maximum length is 128. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="largeFaceListId" /></td>
    <td><code>string</code></td>
    <td>Valid character is letter in lower case or digit or '-' or '_', maximum length is 64. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="recognitionModel" /></td>
    <td><code>string</code></td>
    <td>Name of recognition model. Recognition model is used when the face features are extracted and associated with detected faceIds. Known values are: "recognition_01", "recognition_02", "recognition_03", and "recognition_04". (recognition_01, recognition_02, recognition_03, recognition_04)</td>
</tr>
<tr>
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>Optional user defined data. Length should not exceed 16K.</td>
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
    <td><a href="#get_face"><CopyableCode code="get_face" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-persisted_face_id"><code>persisted_face_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list-face for more details.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-returnRecognitionModel"><code>returnRecognitionModel</code></a></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list for more details.</td>
</tr>
<tr>
    <td><a href="#get_large_face_lists"><CopyableCode code="get_large_face_lists" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-returnRecognitionModel"><code>returnRecognitionModel</code></a></td>
    <td>List Large Face Lists' information of largeFaceListId, name, userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-lists for more details.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Create an empty Large Face List with user-specified largeFaceListId, name, an optional userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/create-large-face-list for more details.</td>
</tr>
<tr>
    <td><a href="#update_face"><CopyableCode code="update_face" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-persisted_face_id"><code>persisted_face_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/update-large-face-list-face for more details.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/update-large-face-list for more details.</td>
</tr>
<tr>
    <td><a href="#delete_face"><CopyableCode code="delete_face" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-persisted_face_id"><code>persisted_face_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/delete-large-face-list-face for more details.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Delete a face from a Large Face List by specified largeFaceListId and persistedFaceId. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/delete-large-face-list for more details.</td>
</tr>
<tr>
    <td><a href="#get_training_status"><CopyableCode code="get_training_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list-training-status for more details.</td>
</tr>
<tr>
    <td><a href="#get_faces"><CopyableCode code="get_faces" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List faces' persistedFaceId and userData in a specified Large Face List. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list-faces for more details.</td>
</tr>
<tr>
    <td><a href="#add_face_from_url"><CopyableCode code="add_face_from_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-targetFace"><code>targetFace</code></a>, <a href="#parameter-detectionModel"><code>detectionModel</code></a>, <a href="#parameter-userData"><code>userData</code></a></td>
    <td>Add a face to a specified Large Face List, up to 1,000,000 faces. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/add-large-face-list-face-from-url for more details.</td>
</tr>
<tr>
    <td><a href="#train"><CopyableCode code="train" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_face_list_id"><code>large_face_list_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Submit a Large Face List training task. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/train-large-face-list for more details.</td>
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
<tr id="parameter-large_face_list_id">
    <td><CopyableCode code="large_face_list_id" /></td>
    <td><code>string</code></td>
    <td>Valid character is letter in lower case or digit or '-' or '_', maximum length is 64. Required.</td>
</tr>
<tr id="parameter-persisted_face_id">
    <td><CopyableCode code="persisted_face_id" /></td>
    <td><code>string</code></td>
    <td>Face ID of the face. Required.</td>
</tr>
<tr id="parameter-detectionModel">
    <td><CopyableCode code="detectionModel" /></td>
    <td><code>string</code></td>
    <td>The 'detectionModel' associated with the detected faceIds. Supported 'detectionModel' values include 'detection_01', 'detection_02' and 'detection_03'. The default value is 'detection_01'. Known values are: "detection_01", "detection_02", and "detection_03". Default value is None.</td>
</tr>
<tr id="parameter-returnRecognitionModel">
    <td><CopyableCode code="returnRecognitionModel" /></td>
    <td><code>boolean</code></td>
    <td>Return 'recognitionModel' or not. The default value is false. Default value is None.</td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string</code></td>
    <td>List resources greater than the "start". It contains no more than 64 characters. Default is empty. Default value is None.</td>
</tr>
<tr id="parameter-targetFace">
    <td><CopyableCode code="targetFace" /></td>
    <td><code>array</code></td>
    <td>A face rectangle to specify the target face to be added to a person, in the format of 'targetFace=left,top,width,height'. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to list, ranging in [1, 1000]. Default is 1000. Default value is None.</td>
</tr>
<tr id="parameter-userData">
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>User-provided data attached to the face. The size limit is 1K. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_face"
    values={[
        { label: 'get_face', value: 'get_face' },
        { label: 'get', value: 'get' },
        { label: 'get_large_face_lists', value: 'get_large_face_lists' }
    ]}
>
<TabItem value="get_face">

Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list-face for more details.

```sql
SELECT
persistedFaceId,
userData
FROM azure.ai_vision_face.large_face_list
WHERE large_face_list_id = '{{ large_face_list_id }}' -- required
AND persisted_face_id = '{{ persisted_face_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
<TabItem value="get">

Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list for more details.

```sql
SELECT
name,
largeFaceListId,
recognitionModel,
userData
FROM azure.ai_vision_face.large_face_list
WHERE large_face_list_id = '{{ large_face_list_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
AND returnRecognitionModel = '{{ returnRecognitionModel }}'
;
```
</TabItem>
<TabItem value="get_large_face_lists">

List Large Face Lists' information of largeFaceListId, name, userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-lists for more details.

```sql
SELECT
name,
largeFaceListId,
recognitionModel,
userData
FROM azure.ai_vision_face.large_face_list
WHERE endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
AND start = '{{ start }}'
AND top = '{{ top }}'
AND returnRecognitionModel = '{{ returnRecognitionModel }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create an empty Large Face List with user-specified largeFaceListId, name, an optional userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/create-large-face-list for more details.

```sql
INSERT INTO azure.ai_vision_face.large_face_list (
large_face_list_id,
endpoint,
api_version
)
SELECT 
'{{ large_face_list_id }}',
'{{ endpoint }}',
'{{ api_version }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: large_face_list
  props:
    - name: large_face_list_id
      value: "{{ large_face_list_id }}"
      description: Required parameter for the large_face_list resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the large_face_list resource.
    - name: api_version
      value: "{{ api_version }}"
      description: Required parameter for the large_face_list resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_face"
    values={[
        { label: 'update_face', value: 'update_face' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_face">

Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/update-large-face-list-face for more details.

```sql
UPDATE azure.ai_vision_face.large_face_list
SET 
-- No updatable properties
WHERE 
large_face_list_id = '{{ large_face_list_id }}' --required
AND persisted_face_id = '{{ persisted_face_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required;
```
</TabItem>
<TabItem value="update">

Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/update-large-face-list for more details.

```sql
UPDATE azure.ai_vision_face.large_face_list
SET 
-- No updatable properties
WHERE 
large_face_list_id = '{{ large_face_list_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_face"
    values={[
        { label: 'delete_face', value: 'delete_face' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_face">

Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/delete-large-face-list-face for more details.

```sql
DELETE FROM azure.ai_vision_face.large_face_list
WHERE large_face_list_id = '{{ large_face_list_id }}' --required
AND persisted_face_id = '{{ persisted_face_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete a face from a Large Face List by specified largeFaceListId and persistedFaceId. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/delete-large-face-list for more details.

```sql
DELETE FROM azure.ai_vision_face.large_face_list
WHERE large_face_list_id = '{{ large_face_list_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_training_status"
    values={[
        { label: 'get_training_status', value: 'get_training_status' },
        { label: 'get_faces', value: 'get_faces' },
        { label: 'add_face_from_url', value: 'add_face_from_url' },
        { label: 'train', value: 'train' }
    ]}
>
<TabItem value="get_training_status">

Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list-training-status for more details.

```sql
EXEC azure.ai_vision_face.large_face_list.get_training_status 
@large_face_list_id='{{ large_face_list_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="get_faces">

List faces' persistedFaceId and userData in a specified Large Face List. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/get-large-face-list-faces for more details.

```sql
EXEC azure.ai_vision_face.large_face_list.get_faces 
@large_face_list_id='{{ large_face_list_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required, 
@start='{{ start }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="add_face_from_url">

Add a face to a specified Large Face List, up to 1,000,000 faces. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/add-large-face-list-face-from-url for more details.

```sql
EXEC azure.ai_vision_face.large_face_list.add_face_from_url 
@large_face_list_id='{{ large_face_list_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required, 
@targetFace='{{ targetFace }}', 
@detectionModel='{{ detectionModel }}', 
@userData='{{ userData }}'
;
```
</TabItem>
<TabItem value="train">

Submit a Large Face List training task. Please refer to https://learn.microsoft.com/rest/api/face/face-list-operations/train-large-face-list for more details.

```sql
EXEC azure.ai_vision_face.large_face_list.train 
@large_face_list_id='{{ large_face_list_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
</Tabs>
