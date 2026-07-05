--- 
title: notebook
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>notebook</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="notebook" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.notebook" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_notebook"
    values={[
        { label: 'get_notebook', value: 'get_notebook' },
        { label: 'get_notebooks_by_workspace', value: 'get_notebooks_by_workspace' }
    ]}
>
<TabItem value="get_notebook">

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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="bigDataPool" /></td>
    <td><code>object</code></td>
    <td>Big data pool reference.</td>
</tr>
<tr>
    <td><CopyableCode code="cells" /></td>
    <td><code>array</code></td>
    <td>Array of cells of the current notebook. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the notebook.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this notebook is in. If not specified, this notebook will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Notebook root-level metadata. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nbformat" /></td>
    <td><code>integer</code></td>
    <td>Notebook format (major number). Incremented between backwards incompatible changes to the notebook format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nbformat_minor" /></td>
    <td><code>integer</code></td>
    <td>Notebook format (minor number). Incremented for backward compatible changes to the notebook format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionProperties" /></td>
    <td><code>object</code></td>
    <td>Session properties.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSparkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The spark configuration of the spark job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_notebooks_by_workspace">

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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="bigDataPool" /></td>
    <td><code>object</code></td>
    <td>Big data pool reference.</td>
</tr>
<tr>
    <td><CopyableCode code="cells" /></td>
    <td><code>array</code></td>
    <td>Array of cells of the current notebook. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the notebook.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this notebook is in. If not specified, this notebook will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Notebook root-level metadata. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nbformat" /></td>
    <td><code>integer</code></td>
    <td>Notebook format (major number). Incremented between backwards incompatible changes to the notebook format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nbformat_minor" /></td>
    <td><code>integer</code></td>
    <td>Notebook format (minor number). Incremented for backward compatible changes to the notebook format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionProperties" /></td>
    <td><code>object</code></td>
    <td>Session properties.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSparkConfiguration" /></td>
    <td><code>object</code></td>
    <td>The spark configuration of the spark job.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
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
    <td><a href="#get_notebook"><CopyableCode code="get_notebook" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-notebook_name"><code>notebook_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a Note Book.</td>
</tr>
<tr>
    <td><a href="#get_notebooks_by_workspace"><CopyableCode code="get_notebooks_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists Notebooks.</td>
</tr>
<tr>
    <td><a href="#create_or_update_notebook"><CopyableCode code="create_or_update_notebook" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-notebook_name"><code>notebook_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a Note Book.</td>
</tr>
<tr>
    <td><a href="#create_or_update_notebook"><CopyableCode code="create_or_update_notebook" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-notebook_name"><code>notebook_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a Note Book.</td>
</tr>
<tr>
    <td><a href="#delete_notebook"><CopyableCode code="delete_notebook" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-notebook_name"><code>notebook_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a Note book.</td>
</tr>
<tr>
    <td><a href="#get_notebook_summary_by_work_space"><CopyableCode code="get_notebook_summary_by_work_space" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists a summary of Notebooks.</td>
</tr>
<tr>
    <td><a href="#rename_notebook"><CopyableCode code="rename_notebook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-notebook_name"><code>notebook_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a notebook.</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-notebook_name">
    <td><CopyableCode code="notebook_name" /></td>
    <td><code>string</code></td>
    <td>The notebook name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the Note book entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the Notebook entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_notebook"
    values={[
        { label: 'get_notebook', value: 'get_notebook' },
        { label: 'get_notebooks_by_workspace', value: 'get_notebooks_by_workspace' }
    ]}
>
<TabItem value="get_notebook">

Gets a Note Book.

```sql
SELECT
id,
name,
,
bigDataPool,
cells,
description,
etag,
folder,
metadata,
nbformat,
nbformat_minor,
sessionProperties,
targetSparkConfiguration,
type
FROM azure.synapse_artifacts.notebook
WHERE notebook_name = '{{ notebook_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_notebooks_by_workspace">

Lists Notebooks.

```sql
SELECT
id,
name,
,
bigDataPool,
cells,
description,
etag,
folder,
metadata,
nbformat,
nbformat_minor,
sessionProperties,
targetSparkConfiguration,
type
FROM azure.synapse_artifacts.notebook
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_notebook"
    values={[
        { label: 'create_or_update_notebook', value: 'create_or_update_notebook' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_notebook">

Creates or updates a Note Book.

```sql
INSERT INTO azure.synapse_artifacts.notebook (
name,
properties,
notebook_name,
endpoint,
If-Match
)
SELECT 
'{{ name }}' /* required */,
'{{ properties }}' /* required */,
'{{ notebook_name }}',
'{{ endpoint }}',
'{{ If-Match }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: notebook
  props:
    - name: notebook_name
      value: "{{ notebook_name }}"
      description: Required parameter for the notebook resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the notebook resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource. Required.
    - name: properties
      description: |
        Properties of Notebook. Required.
      value:
        : "{{  }}"
        description: "{{ description }}"
        bigDataPool:
          type: "{{ type }}"
          referenceName: "{{ referenceName }}"
        targetSparkConfiguration:
          type: "{{ type }}"
          referenceName: "{{ referenceName }}"
        sessionProperties:
          driverMemory: "{{ driverMemory }}"
          driverCores: {{ driverCores }}
          executorMemory: "{{ executorMemory }}"
          executorCores: {{ executorCores }}
          numExecutors: {{ numExecutors }}
        metadata:
          : "{{  }}"
          kernelspec:
            : "{{  }}"
            name: "{{ name }}"
            display_name: "{{ display_name }}"
          language_info:
            : "{{  }}"
            name: "{{ name }}"
            codemirror_mode: "{{ codemirror_mode }}"
        nbformat: {{ nbformat }}
        nbformat_minor: {{ nbformat_minor }}
        cells:
          - : "{{  }}"
            cell_type: "{{ cell_type }}"
            metadata: "{{ metadata }}"
            source: "{{ source }}"
            attachments: "{{ attachments }}"
            outputs: "{{ outputs }}"
        folder:
          name: "{{ name }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the Note book entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the Note book entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_notebook"
    values={[
        { label: 'create_or_update_notebook', value: 'create_or_update_notebook' }
    ]}
>
<TabItem value="create_or_update_notebook">

Creates or updates a Note Book.

```sql
REPLACE azure.synapse_artifacts.notebook
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
notebook_name = '{{ notebook_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND name = '{{ name }}' --required
AND properties = '{{ properties }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_notebook"
    values={[
        { label: 'delete_notebook', value: 'delete_notebook' }
    ]}
>
<TabItem value="delete_notebook">

Deletes a Note book.

```sql
DELETE FROM azure.synapse_artifacts.notebook
WHERE notebook_name = '{{ notebook_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_notebook_summary_by_work_space"
    values={[
        { label: 'get_notebook_summary_by_work_space', value: 'get_notebook_summary_by_work_space' },
        { label: 'rename_notebook', value: 'rename_notebook' }
    ]}
>
<TabItem value="get_notebook_summary_by_work_space">

Lists a summary of Notebooks.

```sql
EXEC azure.synapse_artifacts.notebook.get_notebook_summary_by_work_space 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="rename_notebook">

Renames a notebook.

```sql
EXEC azure.synapse_artifacts.notebook.rename_notebook 
@notebook_name='{{ notebook_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
