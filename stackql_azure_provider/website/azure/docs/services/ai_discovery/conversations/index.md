--- 
title: conversations
hide_title: false
hide_table_of_contents: false
keywords:
  - conversations
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

Creates, updates, deletes, gets or lists a <code>conversations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conversations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_discovery.conversations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>The conversation name. Required.</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The title.</td>
</tr>
<tr>
    <td><CopyableCode code="investigationName" /></td>
    <td><code>string</code></td>
    <td>The Name of the associated Investigation.</td>
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
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The name of the associated Project.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The conversation name. Required.</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The title.</td>
</tr>
<tr>
    <td><CopyableCode code="investigationName" /></td>
    <td><code>string</code></td>
    <td>The Name of the associated Investigation.</td>
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
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The name of the associated Project.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-conversation_name"><code>conversation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a Conversation by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-investigationName"><code>investigationName</code></a>, <a href="#parameter-projectName"><code>projectName</code></a>, <a href="#parameter-createdSince"><code>createdSince</code></a></td>
    <td>List Conversation resources.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates a Conversation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-conversation_name"><code>conversation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Updates a Conversation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-conversation_name"><code>conversation_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a Conversation.</td>
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
<tr id="parameter-conversation_name">
    <td><CopyableCode code="conversation_name" /></td>
    <td><code>string</code></td>
    <td>The conversation name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-createdSince">
    <td><CopyableCode code="createdSince" /></td>
    <td><code>string (date-time)</code></td>
    <td>The oldest creation timestamp to keep. Default value is None.</td>
</tr>
<tr id="parameter-investigationName">
    <td><CopyableCode code="investigationName" /></td>
    <td><code>string</code></td>
    <td>The name of the associated Investigation. Default value is None.</td>
</tr>
<tr id="parameter-projectName">
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The name of the associated Project. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Fetch a Conversation by name.

```sql
SELECT
name,
createdAt,
createdBy,
createdByType,
displayName,
investigationName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName
FROM azure.ai_discovery.conversations
WHERE conversation_name = '{{ conversation_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Conversation resources.

```sql
SELECT
name,
createdAt,
createdBy,
createdByType,
displayName,
investigationName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName
FROM azure.ai_discovery.conversations
WHERE endpoint = '{{ endpoint }}' -- required
AND investigationName = '{{ investigationName }}'
AND projectName = '{{ projectName }}'
AND createdSince = '{{ createdSince }}'
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

Creates a Conversation.

```sql
INSERT INTO azure.ai_discovery.conversations (
endpoint
)
SELECT 
'{{ endpoint }}'
RETURNING
name,
createdAt,
createdBy,
createdByType,
displayName,
investigationName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: conversations
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the conversations resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a Conversation.

```sql
UPDATE azure.ai_discovery.conversations
SET 
displayName = '{{ displayName }}',
investigationName = '{{ investigationName }}',
projectName = '{{ projectName }}'
WHERE 
conversation_name = '{{ conversation_name }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
name,
createdAt,
createdBy,
createdByType,
displayName,
investigationName,
lastModifiedAt,
lastModifiedBy,
lastModifiedByType,
projectName;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a Conversation.

```sql
DELETE FROM azure.ai_discovery.conversations
WHERE conversation_name = '{{ conversation_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
