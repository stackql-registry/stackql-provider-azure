--- 
title: knowledge_bases
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_bases
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

Creates, updates, deletes, gets or lists a <code>knowledge_bases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_bases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_discovery.knowledge_bases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>The knowledgeBase name. Required.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List KnowledgeBase resources.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List KnowledgeBase resources.

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
FROM azure.ai_discovery.knowledge_bases
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
