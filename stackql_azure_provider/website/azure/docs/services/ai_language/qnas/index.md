--- 
title: qnas
hide_title: false
hide_table_of_contents: false
keywords:
  - qnas
  - ai_language
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

Creates, updates, deletes, gets or lists a <code>qnas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="qnas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_language.qnas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_qnas"
    values={[
        { label: 'list_qnas', value: 'list_qnas' }
    ]}
>
<TabItem value="list_qnas">

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
    <td><code>integer</code></td>
    <td>Unique ID for the QnA. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="activeLearningSuggestions" /></td>
    <td><code>array</code></td>
    <td>List of Active Learning suggestions for the QnA.</td>
</tr>
<tr>
    <td><CopyableCode code="answer" /></td>
    <td><code>string</code></td>
    <td>Answer text.</td>
</tr>
<tr>
    <td><CopyableCode code="dialog" /></td>
    <td><code>object</code></td>
    <td>Context of a QnA.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date-time when the QnA was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata associated with the answer, useful to categorize or filter question answers.</td>
</tr>
<tr>
    <td><CopyableCode code="questions" /></td>
    <td><code>array</code></td>
    <td>List of questions associated with the answer.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source from which QnA was indexed e.g. `https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs `_ .</td>
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
    <td><a href="#list_qnas"><CopyableCode code="list_qnas" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a>, <a href="#parameter-source"><code>source</code></a></td>
    <td>Gets all the QnAs of a project.</td>
</tr>
<tr>
    <td><a href="#update_qnas"><CopyableCode code="update_qnas" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-op"><code>op</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Updates the QnAs of a project.</td>
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
    <td>The name of the project to use. Required.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>An offset into the collection of the first resource to be returned. Default value is None.</td>
</tr>
<tr id="parameter-source">
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the QnA. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the collection. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_qnas"
    values={[
        { label: 'list_qnas', value: 'list_qnas' }
    ]}
>
<TabItem value="list_qnas">

Gets all the QnAs of a project.

```sql
SELECT
id,
activeLearningSuggestions,
answer,
dialog,
lastUpdatedDateTime,
metadata,
questions,
source
FROM azure.ai_language.qnas
WHERE project_name = '{{ project_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND maxpagesize = '{{ maxpagesize }}'
AND source = '{{ source }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_qnas"
    values={[
        { label: 'update_qnas', value: 'update_qnas' }
    ]}
>
<TabItem value="update_qnas">

Updates the QnAs of a project.

```sql
UPDATE azure.ai_language.qnas
SET 
op = '{{ op }}',
value = '{{ value }}'
WHERE 
project_name = '{{ project_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND op = '{{ op }}' --required
AND value = '{{ value }}' --required;
```
</TabItem>
</Tabs>
