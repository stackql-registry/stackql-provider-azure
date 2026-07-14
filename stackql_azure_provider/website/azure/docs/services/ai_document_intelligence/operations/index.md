--- 
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - ai_document_intelligence
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

Creates, updates, deletes, gets or lists an <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_document_intelligence.operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation"
    values={[
        { label: 'get_operation', value: 'get_operation' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_operation">

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
    <td>API version used to create this operation.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the operation was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Encountered error.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of operation. Required. Known values are: "documentModelBuild", "documentModelCompose", "documentModelCopyTo", "documentClassifierCopyTo", and "documentClassifierBuild".</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the status was last updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Operation ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="percentCompleted" /></td>
    <td><code>integer</code></td>
    <td>Operation progress (0-100).</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>URL of the resource targeted by this operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. notStarted, running, completed, or failed. Required. Known values are: "notStarted", "running", "failed", "succeeded", "canceled", and "skipped". (notStarted, running, failed, succeeded, canceled, skipped)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>List of key-value tag attributes associated with the document model.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_operations">

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
    <td>API version used to create this operation.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the operation was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Encountered error.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of operation. Required. Known values are: "documentModelBuild", "documentModelCompose", "documentModelCopyTo", "documentClassifierCopyTo", and "documentClassifierBuild".</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the status was last updated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Operation ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="percentCompleted" /></td>
    <td><code>integer</code></td>
    <td>Operation progress (0-100).</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>URL of the resource targeted by this operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. notStarted, running, completed, or failed. Required. Known values are: "notStarted", "running", "failed", "succeeded", "canceled", and "skipped". (notStarted, running, failed, succeeded, canceled, skipped)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>List of key-value tag attributes associated with the document model.</td>
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
    <td><a href="#get_operation"><CopyableCode code="get_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets operation info.</td>
</tr>
<tr>
    <td><a href="#list_operations"><CopyableCode code="list_operations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all operations.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation ID. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_operation"
    values={[
        { label: 'get_operation', value: 'get_operation' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_operation">

Gets operation info.

```sql
SELECT
apiVersion,
createdDateTime,
error,
kind,
lastUpdatedDateTime,
operationId,
percentCompleted,
resourceLocation,
status,
tags
FROM azure.ai_document_intelligence.operations
WHERE operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_operations">

Lists all operations.

```sql
SELECT
apiVersion,
createdDateTime,
error,
kind,
lastUpdatedDateTime,
operationId,
percentCompleted,
resourceLocation,
status,
tags
FROM azure.ai_document_intelligence.operations
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>
