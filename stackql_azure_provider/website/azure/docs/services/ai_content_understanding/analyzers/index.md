--- 
title: analyzers
hide_title: false
hide_table_of_contents: false
keywords:
  - analyzers
  - ai_content_understanding
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

Creates, updates, deletes, gets or lists an <code>analyzers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyzers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_content_understanding.analyzers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_analyzer"
    values={[
        { label: 'get_analyzer', value: 'get_analyzer' },
        { label: 'list_analyzers', value: 'list_analyzers' }
    ]}
>
<TabItem value="get_analyzer">

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
    <td><CopyableCode code="analyzerId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the analyzer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="baseAnalyzerId" /></td>
    <td><code>string</code></td>
    <td>The analyzer to incrementally train from.</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>Analyzer configuration settings.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the analyzer was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicFieldSchema" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the result may contain additional fields outside of the defined schema.</td>
</tr>
<tr>
    <td><CopyableCode code="fieldSchema" /></td>
    <td><code>object</code></td>
    <td>The schema of fields to extracted.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeSources" /></td>
    <td><code>array</code></td>
    <td>Additional knowledge sources used to enhance the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the analyzer was last modified. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="models" /></td>
    <td><code>object</code></td>
    <td>Mapping of model roles to specific model names. Ex. &#123; "completion": "gpt-4.1", "embedding": "text-embedding-3-large" &#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="processingLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the data may be processed. Defaults to global. Known values are: "geography", "dataZone", and "global". (geography, dataZone, global)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the analyzer. Required. Known values are: "creating", "ready", "deleting", and "failed". (creating, ready, deleting, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedModels" /></td>
    <td><code>object</code></td>
    <td>Chat completion and embedding models supported by the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags associated with the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Warnings encountered while creating the analyzer.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_analyzers">

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
    <td><CopyableCode code="analyzerId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the analyzer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="baseAnalyzerId" /></td>
    <td><code>string</code></td>
    <td>The analyzer to incrementally train from.</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>Analyzer configuration settings.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the analyzer was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="dynamicFieldSchema" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the result may contain additional fields outside of the defined schema.</td>
</tr>
<tr>
    <td><CopyableCode code="fieldSchema" /></td>
    <td><code>object</code></td>
    <td>The schema of fields to extracted.</td>
</tr>
<tr>
    <td><CopyableCode code="knowledgeSources" /></td>
    <td><code>array</code></td>
    <td>Additional knowledge sources used to enhance the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the analyzer was last modified. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="models" /></td>
    <td><code>object</code></td>
    <td>Mapping of model roles to specific model names. Ex. &#123; "completion": "gpt-4.1", "embedding": "text-embedding-3-large" &#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="processingLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the data may be processed. Defaults to global. Known values are: "geography", "dataZone", and "global". (geography, dataZone, global)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the analyzer. Required. Known values are: "creating", "ready", "deleting", and "failed". (creating, ready, deleting, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedModels" /></td>
    <td><code>object</code></td>
    <td>Chat completion and embedding models supported by the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags associated with the analyzer.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>Warnings encountered while creating the analyzer.</td>
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
    <td><a href="#get_analyzer"><CopyableCode code="get_analyzer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-analyzer_id"><code>analyzer_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get analyzer properties.</td>
</tr>
<tr>
    <td><a href="#list_analyzers"><CopyableCode code="list_analyzers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List analyzers.</td>
</tr>
<tr>
    <td><a href="#create_analyzer"><CopyableCode code="create_analyzer" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-analyzer_id"><code>analyzer_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-allowReplace"><code>allowReplace</code></a></td>
    <td>Create a new analyzer asynchronously.</td>
</tr>
<tr>
    <td><a href="#update_analyzer"><CopyableCode code="update_analyzer" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-analyzer_id"><code>analyzer_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update analyzer properties.</td>
</tr>
<tr>
    <td><a href="#delete_analyzer"><CopyableCode code="delete_analyzer" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-analyzer_id"><code>analyzer_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete analyzer.</td>
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
<tr id="parameter-analyzer_id">
    <td><CopyableCode code="analyzer_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the analyzer. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-allowReplace">
    <td><CopyableCode code="allowReplace" /></td>
    <td><code>boolean</code></td>
    <td>Allow the operation to replace an existing resource. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_analyzer"
    values={[
        { label: 'get_analyzer', value: 'get_analyzer' },
        { label: 'list_analyzers', value: 'list_analyzers' }
    ]}
>
<TabItem value="get_analyzer">

Get analyzer properties.

```sql
SELECT
analyzerId,
baseAnalyzerId,
config,
createdAt,
description,
dynamicFieldSchema,
fieldSchema,
knowledgeSources,
lastModifiedAt,
models,
processingLocation,
status,
supportedModels,
tags,
warnings
FROM azure.ai_content_understanding.analyzers
WHERE analyzer_id = '{{ analyzer_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_analyzers">

List analyzers.

```sql
SELECT
analyzerId,
baseAnalyzerId,
config,
createdAt,
description,
dynamicFieldSchema,
fieldSchema,
knowledgeSources,
lastModifiedAt,
models,
processingLocation,
status,
supportedModels,
tags,
warnings
FROM azure.ai_content_understanding.analyzers
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_analyzer"
    values={[
        { label: 'create_analyzer', value: 'create_analyzer' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_analyzer">

Create a new analyzer asynchronously.

```sql
INSERT INTO azure.ai_content_understanding.analyzers (
description,
tags,
baseAnalyzerId,
config,
fieldSchema,
dynamicFieldSchema,
processingLocation,
knowledgeSources,
models,
analyzer_id,
endpoint,
allowReplace
)
SELECT 
'{{ description }}',
'{{ tags }}',
'{{ baseAnalyzerId }}',
'{{ config }}',
'{{ fieldSchema }}',
{{ dynamicFieldSchema }},
'{{ processingLocation }}',
'{{ knowledgeSources }}',
'{{ models }}',
'{{ analyzer_id }}',
'{{ endpoint }}',
'{{ allowReplace }}'
RETURNING
analyzerId,
baseAnalyzerId,
config,
createdAt,
description,
dynamicFieldSchema,
fieldSchema,
knowledgeSources,
lastModifiedAt,
models,
processingLocation,
status,
supportedModels,
tags,
warnings
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: analyzers
  props:
    - name: analyzer_id
      value: "{{ analyzer_id }}"
      description: Required parameter for the analyzers resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the analyzers resource.
    - name: description
      value: "{{ description }}"
      description: |
        A description of the analyzer.
    - name: tags
      value: "{{ tags }}"
      description: |
        Tags associated with the analyzer.
    - name: baseAnalyzerId
      value: "{{ baseAnalyzerId }}"
      description: |
        The analyzer to incrementally train from.
    - name: config
      description: |
        Analyzer configuration settings.
      value:
        returnDetails: {{ returnDetails }}
        locales:
          - "{{ locales }}"
        enableOcr: {{ enableOcr }}
        enableLayout: {{ enableLayout }}
        enableFigureDescription: {{ enableFigureDescription }}
        enableFigureAnalysis: {{ enableFigureAnalysis }}
        enableFormula: {{ enableFormula }}
        tableFormat: "{{ tableFormat }}"
        chartFormat: "{{ chartFormat }}"
        annotationFormat: "{{ annotationFormat }}"
        disableFaceBlurring: {{ disableFaceBlurring }}
        estimateFieldSourceAndConfidence: {{ estimateFieldSourceAndConfidence }}
        contentCategories: "{{ contentCategories }}"
        enableSegment: {{ enableSegment }}
        segmentPerPage: {{ segmentPerPage }}
        omitContent: {{ omitContent }}
    - name: fieldSchema
      description: |
        The schema of fields to extracted.
      value:
        name: "{{ name }}"
        description: "{{ description }}"
        fields: "{{ fields }}"
        definitions: "{{ definitions }}"
    - name: dynamicFieldSchema
      value: {{ dynamicFieldSchema }}
      description: |
        Indicates whether the result may contain additional fields outside of the defined schema.
    - name: processingLocation
      value: "{{ processingLocation }}"
      description: |
        The location where the data may be processed. Defaults to global. Known values are: "geography", "dataZone", and "global".
      valid_values: ['geography', 'dataZone', 'global']
    - name: knowledgeSources
      description: |
        Additional knowledge sources used to enhance the analyzer.
      value:
        - kind: "{{ kind }}"
    - name: models
      value: "{{ models }}"
      description: |
        Mapping of model roles to specific model names. Ex. { "completion": "gpt-4.1", "embedding": "text-embedding-3-large" }.
    - name: allowReplace
      value: {{ allowReplace }}
      description: Allow the operation to replace an existing resource. Default value is None.
      description: Allow the operation to replace an existing resource. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_analyzer"
    values={[
        { label: 'update_analyzer', value: 'update_analyzer' }
    ]}
>
<TabItem value="update_analyzer">

Update analyzer properties.

```sql
UPDATE azure.ai_content_understanding.analyzers
SET 
description = '{{ description }}',
tags = '{{ tags }}',
baseAnalyzerId = '{{ baseAnalyzerId }}',
config = '{{ config }}',
fieldSchema = '{{ fieldSchema }}',
dynamicFieldSchema = {{ dynamicFieldSchema }},
processingLocation = '{{ processingLocation }}',
knowledgeSources = '{{ knowledgeSources }}',
models = '{{ models }}'
WHERE 
analyzer_id = '{{ analyzer_id }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
analyzerId,
baseAnalyzerId,
config,
createdAt,
description,
dynamicFieldSchema,
fieldSchema,
knowledgeSources,
lastModifiedAt,
models,
processingLocation,
status,
supportedModels,
tags,
warnings;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_analyzer"
    values={[
        { label: 'delete_analyzer', value: 'delete_analyzer' }
    ]}
>
<TabItem value="delete_analyzer">

Delete analyzer.

```sql
DELETE FROM azure.ai_content_understanding.analyzers
WHERE analyzer_id = '{{ analyzer_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
