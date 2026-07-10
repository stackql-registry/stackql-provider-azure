--- 
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - ai_language_conversations_authoring
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="projects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language_conversations_authoring.projects" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_projects"
    values={[
        { label: 'list_projects', value: 'list_projects' }
    ]}
>
<TabItem value="list_projects">

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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the project creation datetime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The project description.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>The project language. This is BCP-47 representation of a language. For example, use "en" for English, "en-gb" for English (UK), "es" for Spanish etc. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastDeployedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the project last deployed datetime.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the project creation datetime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTrainedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the project last trained datetime.</td>
</tr>
<tr>
    <td><CopyableCode code="multilingual" /></td>
    <td><code>boolean</code></td>
    <td>Whether the project would be used for multiple languages or not.</td>
</tr>
<tr>
    <td><CopyableCode code="projectKind" /></td>
    <td><code>string</code></td>
    <td>Represents the project kind. Required. Known values are: "Conversation", "Orchestration", and "CustomConversationSummarization". (Conversation, Orchestration, CustomConversationSummarization)</td>
</tr>
<tr>
    <td><CopyableCode code="projectName" /></td>
    <td><code>string</code></td>
    <td>The new project name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>The project settings.</td>
</tr>
<tr>
    <td><CopyableCode code="storageInputContainerName" /></td>
    <td><code>string</code></td>
    <td>The storage container name in case of conversation summarization.</td>
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
    <td><a href="#list_projects"><CopyableCode code="list_projects" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Lists the existing projects.</td>
</tr>
<tr>
    <td><a href="#delete_project"><CopyableCode code="delete_project" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a project.</td>
</tr>
<tr>
    <td><a href="#create_project"><CopyableCode code="create_project" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-projectKind"><code>projectKind</code></a>, <a href="#parameter-projectName"><code>projectName</code></a>, <a href="#parameter-language"><code>language</code></a></td>
    <td></td>
    <td>Creates a new project or updates an existing one.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The new project name. Required.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to skip. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The number of result items to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_projects"
    values={[
        { label: 'list_projects', value: 'list_projects' }
    ]}
>
<TabItem value="list_projects">

Lists the existing projects.

```sql
SELECT
createdDateTime,
description,
language,
lastDeployedDateTime,
lastModifiedDateTime,
lastTrainedDateTime,
multilingual,
projectKind,
projectName,
settings,
storageInputContainerName
FROM azure.ai_language_conversations_authoring.projects
WHERE endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_project"
    values={[
        { label: 'delete_project', value: 'delete_project' }
    ]}
>
<TabItem value="delete_project">

Deletes a project.

```sql
DELETE FROM azure.ai_language_conversations_authoring.projects
WHERE project_name = '{{ project_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_project"
    values={[
        { label: 'create_project', value: 'create_project' }
    ]}
>
<TabItem value="create_project">

Creates a new project or updates an existing one.

```sql
EXEC azure.ai_language_conversations_authoring.projects.create_project 
@project_name='{{ project_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"projectKind": "{{ projectKind }}", 
"settings": "{{ settings }}", 
"storageInputContainerName": "{{ storageInputContainerName }}", 
"projectName": "{{ projectName }}", 
"multilingual": {{ multilingual }}, 
"description": "{{ description }}", 
"language": "{{ language }}"
}'
;
```
</TabItem>
</Tabs>
