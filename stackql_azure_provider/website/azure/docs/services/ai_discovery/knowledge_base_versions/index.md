--- 
title: knowledge_base_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_base_versions
  - ai_discovery
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

Creates, updates, deletes, gets or lists a <code>knowledge_base_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_base_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_discovery.knowledge_base_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_status"
    values={[
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_operation_status">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error object that describes the error when status is 'Failed'.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>A version.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the operation. Required. Known values are: "NotStarted", "Running", "Succeeded", "Failed", and "Canceled". (NotStarted, Running, Succeeded, Failed, Canceled)</td>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The ID for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The version name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bookshelfName" /></td>
    <td><code>string</code></td>
    <td>The name of the associated Bookshelf tracked resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="copilotInstruction" /></td>
    <td><code>string</code></td>
    <td>The copilot instruction. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who created this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who created this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeBaseUrl" /></td>
    <td><code>string</code></td>
    <td>URL to access the knowledge base.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who updated this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who updated this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "NotStarted", "Running", "Succeeded", "Canceled", and "Failed". (NotStarted, Running, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAssetReferences" /></td>
    <td><code>array</code></td>
    <td>Storage asset references to index.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The ID for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The version name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="bookshelfName" /></td>
    <td><code>string</code></td>
    <td>The name of the associated Bookshelf tracked resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="copilotInstruction" /></td>
    <td><code>string</code></td>
    <td>The copilot instruction. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who created this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who created this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeBaseUrl" /></td>
    <td><code>string</code></td>
    <td>URL to access the knowledge base.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the resource was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The ID of the user who updated this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedByType" /></td>
    <td><code>string</code></td>
    <td>The type of user who updated this resource. Known values are: "User", "Application", and "System". (User, Application, System)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "NotStarted", "Running", "Succeeded", "Canceled", and "Failed". (NotStarted, Running, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAssetReferences" /></td>
    <td><code>array</code></td>
    <td>Storage asset references to index.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version. Required.</td>
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
    <td><a href="#get_operation_status"><CopyableCode code="get_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the status of a long-running operation.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a KnowledgeBaseVersion by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createdSince"><code>createdSince</code></a></td>
    <td>List KnowledgeBaseVersion resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-copilotInstruction"><code>copilotInstruction</code></a></td>
    <td></td>
    <td>Creates or updates a KnowledgeBaseVersion.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-copilotInstruction"><code>copilotInstruction</code></a></td>
    <td></td>
    <td>Creates or updates a KnowledgeBaseVersion.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a KnowledgeBaseVersion.</td>
</tr>
<tr>
    <td><a href="#delete_latest_version"><CopyableCode code="delete_latest_version" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete the most recent version of KnowledgeBase.</td>
</tr>
<tr>
    <td><a href="#get_latest_version"><CopyableCode code="get_latest_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get the most recent version of KnowledgeBase.</td>
</tr>
<tr>
    <td><a href="#start_indexing"><CopyableCode code="start_indexing" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Start indexing.</td>
</tr>
<tr>
    <td><a href="#cancel_indexing"><CopyableCode code="cancel_indexing" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-knowledge_base_name"><code>knowledge_base_name</code></a>, <a href="#parameter-version_name"><code>version_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancel indexing.</td>
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
<tr id="parameter-knowledge_base_name">
    <td><CopyableCode code="knowledge_base_name" /></td>
    <td><code>string</code></td>
    <td>The knowledgeBase name. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the operation. Required.</td>
</tr>
<tr id="parameter-version_name">
    <td><CopyableCode code="version_name" /></td>
    <td><code>string</code></td>
    <td>The version name. Required.</td>
</tr>
<tr id="parameter-createdSince">
    <td><CopyableCode code="createdSince" /></td>
    <td><code>string (date-time)</code></td>
    <td>The oldest creation timestamp to keep. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_operation_status"
    values={[
        { label: 'get_operation_status', value: 'get_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_operation_status">

Get the status of a long-running operation.

```sql
SELECT
id,
error,
result,
status
FROM azure.ai_discovery.knowledge_base_versions
WHERE knowledge_base_name = '{{ knowledge_base_name }}' -- required
AND version_name = '{{ version_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Fetch a KnowledgeBaseVersion by name.

```sql
SELECT
id,
name,
bookshelfName,
copilotInstruction,
createdAt,
createdBy,
createdByType,
description,
knowledgeBaseUrl,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
provisioningState,
status,
storageAssetReferences,
tags,
version
FROM azure.ai_discovery.knowledge_base_versions
WHERE knowledge_base_name = '{{ knowledge_base_name }}' -- required
AND version_name = '{{ version_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List KnowledgeBaseVersion resources.

```sql
SELECT
id,
name,
bookshelfName,
copilotInstruction,
createdAt,
createdBy,
createdByType,
description,
knowledgeBaseUrl,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
provisioningState,
status,
storageAssetReferences,
tags,
version
FROM azure.ai_discovery.knowledge_base_versions
WHERE knowledge_base_name = '{{ knowledge_base_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND createdSince = '{{ createdSince }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a KnowledgeBaseVersion.

```sql
INSERT INTO azure.ai_discovery.knowledge_base_versions (
storageAssetReferences,
tags,
description,
copilotInstruction,
knowledge_base_name,
version_name,
endpoint
)
SELECT 
'{{ storageAssetReferences }}',
'{{ tags }}',
'{{ description }}' /* required */,
'{{ copilotInstruction }}' /* required */,
'{{ knowledge_base_name }}',
'{{ version_name }}',
'{{ endpoint }}'
RETURNING
id,
name,
bookshelfName,
copilotInstruction,
createdAt,
createdBy,
createdByType,
description,
knowledgeBaseUrl,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
provisioningState,
status,
storageAssetReferences,
tags,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: knowledge_base_versions
  props:
    - name: knowledge_base_name
      value: "{{ knowledge_base_name }}"
      description: Required parameter for the knowledge_base_versions resource.
    - name: version_name
      value: "{{ version_name }}"
      description: Required parameter for the knowledge_base_versions resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the knowledge_base_versions resource.
    - name: storageAssetReferences
      description: |
        Storage asset references to index.
      value:
        - id: "{{ id }}"
          userAssignedIdentity: "{{ userAssignedIdentity }}"
    - name: tags
      description: |
        The tags.
      value:
        - key: "{{ key }}"
          value: "{{ value }}"
    - name: description
      value: "{{ description }}"
      description: |
        The description. Required.
    - name: copilotInstruction
      value: "{{ copilotInstruction }}"
      description: |
        The copilot instruction. Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a KnowledgeBaseVersion.

```sql
REPLACE azure.ai_discovery.knowledge_base_versions
SET 
storageAssetReferences = '{{ storageAssetReferences }}',
tags = '{{ tags }}',
description = '{{ description }}',
copilotInstruction = '{{ copilotInstruction }}'
WHERE 
knowledge_base_name = '{{ knowledge_base_name }}' --required
AND version_name = '{{ version_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND description = '{{ description }}' --required
AND copilotInstruction = '{{ copilotInstruction }}' --required
RETURNING
id,
name,
bookshelfName,
copilotInstruction,
createdAt,
createdBy,
createdByType,
description,
knowledgeBaseUrl,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
provisioningState,
status,
storageAssetReferences,
tags,
version;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_latest_version', value: 'delete_latest_version' }
    ]}
>
<TabItem value="delete">

Delete a KnowledgeBaseVersion.

```sql
DELETE FROM azure.ai_discovery.knowledge_base_versions
WHERE knowledge_base_name = '{{ knowledge_base_name }}' --required
AND version_name = '{{ version_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_latest_version">

Delete the most recent version of KnowledgeBase.

```sql
DELETE FROM azure.ai_discovery.knowledge_base_versions
WHERE knowledge_base_name = '{{ knowledge_base_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_latest_version"
    values={[
        { label: 'get_latest_version', value: 'get_latest_version' },
        { label: 'start_indexing', value: 'start_indexing' },
        { label: 'cancel_indexing', value: 'cancel_indexing' }
    ]}
>
<TabItem value="get_latest_version">

Get the most recent version of KnowledgeBase.

```sql
EXEC azure.ai_discovery.knowledge_base_versions.get_latest_version 
@knowledge_base_name='{{ knowledge_base_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="start_indexing">

Start indexing.

```sql
EXEC azure.ai_discovery.knowledge_base_versions.start_indexing 
@knowledge_base_name='{{ knowledge_base_name }}' --required, 
@version_name='{{ version_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_indexing">

Cancel indexing.

```sql
EXEC azure.ai_discovery.knowledge_base_versions.cancel_indexing 
@knowledge_base_name='{{ knowledge_base_name }}' --required, 
@version_name='{{ version_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
