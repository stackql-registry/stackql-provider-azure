--- 
title: large_person_group
hide_title: false
hide_table_of_contents: false
keywords:
  - large_person_group
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

Creates, updates, deletes, gets or lists a <code>large_person_group</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="large_person_group" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.large_person_group" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_face"
    values={[
        { label: 'get_face', value: 'get_face' },
        { label: 'get_person', value: 'get_person' },
        { label: 'get', value: 'get' },
        { label: 'get_large_person_groups', value: 'get_large_person_groups' }
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
<TabItem value="get_person">

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
    <td><CopyableCode code="persistedFaceIds" /></td>
    <td><code>array</code></td>
    <td>Face ids of registered faces in the person.</td>
</tr>
<tr>
    <td><CopyableCode code="personId" /></td>
    <td><code>string</code></td>
    <td>ID of the person. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userData" /></td>
    <td><code>string</code></td>
    <td>Optional user defined data. Length should not exceed 16K.</td>
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
    <td><CopyableCode code="largePersonGroupId" /></td>
    <td><code>string</code></td>
    <td>ID of the container. Required.</td>
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
<TabItem value="get_large_person_groups">

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
    <td><CopyableCode code="largePersonGroupId" /></td>
    <td><code>string</code></td>
    <td>ID of the container. Required.</td>
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
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-persisted_face_id"><code>persisted_face_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-person-face for more details.</td>
</tr>
<tr>
    <td><a href="#get_person"><CopyableCode code="get_person" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-person for more details.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-returnRecognitionModel"><code>returnRecognitionModel</code></a></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group for more details.</td>
</tr>
<tr>
    <td><a href="#get_large_person_groups"><CopyableCode code="get_large_person_groups" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-returnRecognitionModel"><code>returnRecognitionModel</code></a></td>
    <td>List all existing Large Person Groups' largePersonGroupId, name, userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-groups for more details.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Create a new Large Person Group with user-specified largePersonGroupId, name, an optional userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/create-large-person-group for more details.</td>
</tr>
<tr>
    <td><a href="#update_face"><CopyableCode code="update_face" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-persisted_face_id"><code>persisted_face_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/update-large-person-group-person-face for more details.</td>
</tr>
<tr>
    <td><a href="#update_person"><CopyableCode code="update_person" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/update-large-person-group-person for more details.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/update-large-person-group for more details.</td>
</tr>
<tr>
    <td><a href="#delete_face"><CopyableCode code="delete_face" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-persisted_face_id"><code>persisted_face_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Delete a face from a person in a Large Person Group by specified largePersonGroupId, personId and persistedFaceId. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/delete-large-person-group-person-face for more details.</td>
</tr>
<tr>
    <td><a href="#delete_person"><CopyableCode code="delete_person" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/delete-large-person-group-person for more details.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/delete-large-person-group for more details.</td>
</tr>
<tr>
    <td><a href="#get_training_status"><CopyableCode code="get_training_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>To check Large Person Group training status completed or still ongoing. Large Person Group training is an asynchronous operation triggered by "Train Large Person Group" API. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-training-status for more details.</td>
</tr>
<tr>
    <td><a href="#get_persons"><CopyableCode code="get_persons" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>List all persons' information in the specified Large Person Group, including personId, name, userData and persistedFaceIds of registered person faces. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-persons for more details.</td>
</tr>
<tr>
    <td><a href="#create_person"><CopyableCode code="create_person" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Create a new person in a specified Large Person Group. To add face to this person, please call "Add Large Person Group Person Face". Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/create-large-person-group-person for more details.</td>
</tr>
<tr>
    <td><a href="#train"><CopyableCode code="train" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td></td>
    <td>Submit a Large Person Group training task. Training is a crucial step that only a trained Large Person Group can be used by "Identify From Large Person Group". Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/train-large-person-group for more details.</td>
</tr>
<tr>
    <td><a href="#add_face_from_url"><CopyableCode code="add_face_from_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-large_person_group_id"><code>large_person_group_id</code></a>, <a href="#parameter-person_id"><code>person_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-targetFace"><code>targetFace</code></a>, <a href="#parameter-detectionModel"><code>detectionModel</code></a>, <a href="#parameter-userData"><code>userData</code></a></td>
    <td>Add a face to a person into a Large Person Group for face identification or verification. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/add-large-person-group-person-face-from-url for more details.</td>
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
<tr id="parameter-large_person_group_id">
    <td><CopyableCode code="large_person_group_id" /></td>
    <td><code>string</code></td>
    <td>ID of the container. Required.</td>
</tr>
<tr id="parameter-persisted_face_id">
    <td><CopyableCode code="persisted_face_id" /></td>
    <td><code>string</code></td>
    <td>Face ID of the face. Required.</td>
</tr>
<tr id="parameter-person_id">
    <td><CopyableCode code="person_id" /></td>
    <td><code>string</code></td>
    <td>ID of the person. Required.</td>
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
        { label: 'get_person', value: 'get_person' },
        { label: 'get', value: 'get' },
        { label: 'get_large_person_groups', value: 'get_large_person_groups' }
    ]}
>
<TabItem value="get_face">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-person-face for more details.

```sql
SELECT
persistedFaceId,
userData
FROM azure.ai_vision_face.large_person_group
WHERE large_person_group_id = '{{ large_person_group_id }}' -- required
AND person_id = '{{ person_id }}' -- required
AND persisted_face_id = '{{ persisted_face_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
<TabItem value="get_person">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-person for more details.

```sql
SELECT
name,
persistedFaceIds,
personId,
userData
FROM azure.ai_vision_face.large_person_group
WHERE large_person_group_id = '{{ large_person_group_id }}' -- required
AND person_id = '{{ person_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
;
```
</TabItem>
<TabItem value="get">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group for more details.

```sql
SELECT
name,
largePersonGroupId,
recognitionModel,
userData
FROM azure.ai_vision_face.large_person_group
WHERE large_person_group_id = '{{ large_person_group_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND api_version = '{{ api_version }}' -- required
AND returnRecognitionModel = '{{ returnRecognitionModel }}'
;
```
</TabItem>
<TabItem value="get_large_person_groups">

List all existing Large Person Groups' largePersonGroupId, name, userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-groups for more details.

```sql
SELECT
name,
largePersonGroupId,
recognitionModel,
userData
FROM azure.ai_vision_face.large_person_group
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

Create a new Large Person Group with user-specified largePersonGroupId, name, an optional userData and recognitionModel. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/create-large-person-group for more details.

```sql
INSERT INTO azure.ai_vision_face.large_person_group (
large_person_group_id,
endpoint,
api_version
)
SELECT 
'{{ large_person_group_id }}',
'{{ endpoint }}',
'{{ api_version }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: large_person_group
  props:
    - name: large_person_group_id
      value: "{{ large_person_group_id }}"
      description: Required parameter for the large_person_group resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the large_person_group resource.
    - name: api_version
      value: "{{ api_version }}"
      description: Required parameter for the large_person_group resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_face"
    values={[
        { label: 'update_face', value: 'update_face' },
        { label: 'update_person', value: 'update_person' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_face">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/update-large-person-group-person-face for more details.

```sql
UPDATE azure.ai_vision_face.large_person_group
SET 
-- No updatable properties
WHERE 
large_person_group_id = '{{ large_person_group_id }}' --required
AND person_id = '{{ person_id }}' --required
AND persisted_face_id = '{{ persisted_face_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required;
```
</TabItem>
<TabItem value="update_person">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/update-large-person-group-person for more details.

```sql
UPDATE azure.ai_vision_face.large_person_group
SET 
-- No updatable properties
WHERE 
large_person_group_id = '{{ large_person_group_id }}' --required
AND person_id = '{{ person_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required;
```
</TabItem>
<TabItem value="update">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/update-large-person-group for more details.

```sql
UPDATE azure.ai_vision_face.large_person_group
SET 
-- No updatable properties
WHERE 
large_person_group_id = '{{ large_person_group_id }}' --required
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
        { label: 'delete_person', value: 'delete_person' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_face">

Delete a face from a person in a Large Person Group by specified largePersonGroupId, personId and persistedFaceId. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/delete-large-person-group-person-face for more details.

```sql
DELETE FROM azure.ai_vision_face.large_person_group
WHERE large_person_group_id = '{{ large_person_group_id }}' --required
AND person_id = '{{ person_id }}' --required
AND persisted_face_id = '{{ persisted_face_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="delete_person">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/delete-large-person-group-person for more details.

```sql
DELETE FROM azure.ai_vision_face.large_person_group
WHERE large_person_group_id = '{{ large_person_group_id }}' --required
AND person_id = '{{ person_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND api_version = '{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="delete">

Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/delete-large-person-group for more details.

```sql
DELETE FROM azure.ai_vision_face.large_person_group
WHERE large_person_group_id = '{{ large_person_group_id }}' --required
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
        { label: 'get_persons', value: 'get_persons' },
        { label: 'create_person', value: 'create_person' },
        { label: 'train', value: 'train' },
        { label: 'add_face_from_url', value: 'add_face_from_url' }
    ]}
>
<TabItem value="get_training_status">

To check Large Person Group training status completed or still ongoing. Large Person Group training is an asynchronous operation triggered by "Train Large Person Group" API. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-training-status for more details.

```sql
EXEC azure.ai_vision_face.large_person_group.get_training_status 
@large_person_group_id='{{ large_person_group_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="get_persons">

List all persons' information in the specified Large Person Group, including personId, name, userData and persistedFaceIds of registered person faces. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/get-large-person-group-persons for more details.

```sql
EXEC azure.ai_vision_face.large_person_group.get_persons 
@large_person_group_id='{{ large_person_group_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required, 
@start='{{ start }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="create_person">

Create a new person in a specified Large Person Group. To add face to this person, please call "Add Large Person Group Person Face". Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/create-large-person-group-person for more details.

```sql
EXEC azure.ai_vision_face.large_person_group.create_person 
@large_person_group_id='{{ large_person_group_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="train">

Submit a Large Person Group training task. Training is a crucial step that only a trained Large Person Group can be used by "Identify From Large Person Group". Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/train-large-person-group for more details.

```sql
EXEC azure.ai_vision_face.large_person_group.train 
@large_person_group_id='{{ large_person_group_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required
;
```
</TabItem>
<TabItem value="add_face_from_url">

Add a face to a person into a Large Person Group for face identification or verification. Please refer to https://learn.microsoft.com/rest/api/face/person-group-operations/add-large-person-group-person-face-from-url for more details.

```sql
EXEC azure.ai_vision_face.large_person_group.add_face_from_url 
@large_person_group_id='{{ large_person_group_id }}' --required, 
@person_id='{{ person_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required, 
@targetFace='{{ targetFace }}', 
@detectionModel='{{ detectionModel }}', 
@userData='{{ userData }}'
;
```
</TabItem>
</Tabs>
