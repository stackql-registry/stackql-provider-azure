--- 
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - ai_documentintelligence
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

Creates, updates, deletes, gets or lists a <code>models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="models" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_documentintelligence.models" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_model"
    values={[
        { label: 'get_model', value: 'get_model' },
        { label: 'list_models', value: 'list_models' }
    ]}
>
<TabItem value="get_model">

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
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>API version used to create this document model.</td>
</tr>
<tr>
    <td><CopyableCode code="azureBlobFileListSource" /></td>
    <td><code>object</code></td>
    <td>Azure Blob Storage file list specifying the training data. Either azureBlobSource or azureBlobFileListSource must be specified.</td>
</tr>
<tr>
    <td><CopyableCode code="azureBlobSource" /></td>
    <td><code>object</code></td>
    <td>Azure Blob Storage location containing the training data. Either azureBlobSource or azureBlobFileListSource must be specified.</td>
</tr>
<tr>
    <td><CopyableCode code="buildMode" /></td>
    <td><code>string</code></td>
    <td>Custom document model build mode. Known values are: "template" and "neural". (template, neural)</td>
</tr>
<tr>
    <td><CopyableCode code="classifierId" /></td>
    <td><code>string</code></td>
    <td>For composed models, the custom classifier to split and classify the input file.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Document model description.</td>
</tr>
<tr>
    <td><CopyableCode code="docTypes" /></td>
    <td><code>object</code></td>
    <td>Supported document types.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="split" /></td>
    <td><code>string</code></td>
    <td>For composed models, the file splitting behavior. Known values are: "auto", "none", and "perPage". (auto, none, perPage)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>List of key-value tag attributes associated with the document model.</td>
</tr>
<tr>
    <td><CopyableCode code="trainingHours" /></td>
    <td><code>number</code></td>
    <td>Number of V100-equivalent GPU hours consumed for model training.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>List of warnings encountered while building the model.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_models">

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
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>API version used to create this document model.</td>
</tr>
<tr>
    <td><CopyableCode code="azureBlobFileListSource" /></td>
    <td><code>object</code></td>
    <td>Azure Blob Storage file list specifying the training data. Either azureBlobSource or azureBlobFileListSource must be specified.</td>
</tr>
<tr>
    <td><CopyableCode code="azureBlobSource" /></td>
    <td><code>object</code></td>
    <td>Azure Blob Storage location containing the training data. Either azureBlobSource or azureBlobFileListSource must be specified.</td>
</tr>
<tr>
    <td><CopyableCode code="buildMode" /></td>
    <td><code>string</code></td>
    <td>Custom document model build mode. Known values are: "template" and "neural". (template, neural)</td>
</tr>
<tr>
    <td><CopyableCode code="classifierId" /></td>
    <td><code>string</code></td>
    <td>For composed models, the custom classifier to split and classify the input file.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Document model description.</td>
</tr>
<tr>
    <td><CopyableCode code="docTypes" /></td>
    <td><code>object</code></td>
    <td>Supported document types.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="split" /></td>
    <td><code>string</code></td>
    <td>For composed models, the file splitting behavior. Known values are: "auto", "none", and "perPage". (auto, none, perPage)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>List of key-value tag attributes associated with the document model.</td>
</tr>
<tr>
    <td><CopyableCode code="trainingHours" /></td>
    <td><code>number</code></td>
    <td>Number of V100-equivalent GPU hours consumed for model training.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>List of warnings encountered while building the model.</td>
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
    <td><a href="#get_model"><CopyableCode code="get_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets detailed document model information.</td>
</tr>
<tr>
    <td><a href="#list_models"><CopyableCode code="list_models" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all document models.</td>
</tr>
<tr>
    <td><a href="#delete_model"><CopyableCode code="delete_model" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes document model.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Unique document model name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_model"
    values={[
        { label: 'get_model', value: 'get_model' },
        { label: 'list_models', value: 'list_models' }
    ]}
>
<TabItem value="get_model">

Gets detailed document model information.

```sql
SELECT
apiVersion,
azureBlobFileListSource,
azureBlobSource,
buildMode,
classifierId,
createdDateTime,
description,
docTypes,
expirationDateTime,
modelId,
modifiedDateTime,
split,
tags,
trainingHours,
warnings
FROM azure.ai_documentintelligence.models
WHERE model_id = '{{ model_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_models">

List all document models.

```sql
SELECT
apiVersion,
azureBlobFileListSource,
azureBlobSource,
buildMode,
classifierId,
createdDateTime,
description,
docTypes,
expirationDateTime,
modelId,
modifiedDateTime,
split,
tags,
trainingHours,
warnings
FROM azure.ai_documentintelligence.models
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_model"
    values={[
        { label: 'delete_model', value: 'delete_model' }
    ]}
>
<TabItem value="delete_model">

Deletes document model.

```sql
DELETE FROM azure.ai_documentintelligence.models
WHERE model_id = '{{ model_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
