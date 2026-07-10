--- 
title: detect_from_session_images
hide_title: false
hide_table_of_contents: false
keywords:
  - detect_from_session_images
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

Creates, updates, deletes, gets or lists a <code>detect_from_session_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="detect_from_session_images" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_face.detect_from_session_images" /></td></tr>
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
    <td><a href="#detect_from_session_image"><CopyableCode code="detect_from_session_image" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-api_version"><code>api_version</code></a></td>
    <td><a href="#parameter-detectionModel"><code>detectionModel</code></a>, <a href="#parameter-recognitionModel"><code>recognitionModel</code></a>, <a href="#parameter-returnFaceId"><code>returnFaceId</code></a>, <a href="#parameter-returnFaceAttributes"><code>returnFaceAttributes</code></a>, <a href="#parameter-returnFaceLandmarks"><code>returnFaceLandmarks</code></a>, <a href="#parameter-returnRecognitionModel"><code>returnRecognitionModel</code></a>, <a href="#parameter-faceIdTimeToLive"><code>faceIdTimeToLive</code></a></td>
    <td>Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks, and attributes. Please refer to https://learn.microsoft.com/rest/api/face/face-detection-operations/detect-from-session-image-id for more details.</td>
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
<tr id="parameter-detectionModel">
    <td><CopyableCode code="detectionModel" /></td>
    <td><code>string</code></td>
    <td>The 'detectionModel' associated with the detected faceIds. Supported 'detectionModel' values include 'detection_01', 'detection_02' and 'detection_03'. The default value is 'detection_01'. 'detection_03' is recommended since its accuracy is improved on smaller faces (64x64 pixels) and rotated face orientations. Known values are: "detection_01", "detection_02", and "detection_03". Default value is None.</td>
</tr>
<tr id="parameter-faceIdTimeToLive">
    <td><CopyableCode code="faceIdTimeToLive" /></td>
    <td><code>integer</code></td>
    <td>The number of seconds for the face ID being cached. Supported range from 60 seconds up to 86400 seconds. The default value is 86400 (24 hours). Default value is None.</td>
</tr>
<tr id="parameter-recognitionModel">
    <td><CopyableCode code="recognitionModel" /></td>
    <td><code>string</code></td>
    <td>The 'recognitionModel' associated with the detected faceIds. Supported 'recognitionModel' values include 'recognition_01', 'recognition_02', 'recognition_03' or 'recognition_04'. The default value is 'recognition_01'. 'recognition_04' is recommended since its accuracy is improved on faces wearing masks compared with 'recognition_03', and its overall accuracy is improved compared with 'recognition_01' and 'recognition_02'. Known values are: "recognition_01", "recognition_02", "recognition_03", and "recognition_04". Default value is None.</td>
</tr>
<tr id="parameter-returnFaceAttributes">
    <td><CopyableCode code="returnFaceAttributes" /></td>
    <td><code>array</code></td>
    <td>Analyze and return the one or more specified face attributes in the comma-separated string like 'returnFaceAttributes=headPose,glasses'. Face attribute analysis has additional computational and time cost. Default value is None.</td>
</tr>
<tr id="parameter-returnFaceId">
    <td><CopyableCode code="returnFaceId" /></td>
    <td><code>boolean</code></td>
    <td>Return faceIds of the detected faces or not. The default value is true. Default value is None.</td>
</tr>
<tr id="parameter-returnFaceLandmarks">
    <td><CopyableCode code="returnFaceLandmarks" /></td>
    <td><code>boolean</code></td>
    <td>Return face landmarks of the detected faces or not. The default value is false. Default value is None.</td>
</tr>
<tr id="parameter-returnRecognitionModel">
    <td><CopyableCode code="returnRecognitionModel" /></td>
    <td><code>boolean</code></td>
    <td>Return 'recognitionModel' or not. The default value is false. This is only applicable when returnFaceId = true. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="detect_from_session_image"
    values={[
        { label: 'detect_from_session_image', value: 'detect_from_session_image' }
    ]}
>
<TabItem value="detect_from_session_image">

Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks, and attributes. Please refer to https://learn.microsoft.com/rest/api/face/face-detection-operations/detect-from-session-image-id for more details.

```sql
EXEC azure.ai_vision_face.detect_from_session_images.detect_from_session_image 
@endpoint='{{ endpoint }}' --required, 
@api_version='{{ api_version }}' --required, 
@detectionModel='{{ detectionModel }}', 
@recognitionModel='{{ recognitionModel }}', 
@returnFaceId={{ returnFaceId }}, 
@returnFaceAttributes='{{ returnFaceAttributes }}', 
@returnFaceLandmarks={{ returnFaceLandmarks }}, 
@returnRecognitionModel={{ returnRecognitionModel }}, 
@faceIdTimeToLive='{{ faceIdTimeToLive }}'
;
```
</TabItem>
</Tabs>
