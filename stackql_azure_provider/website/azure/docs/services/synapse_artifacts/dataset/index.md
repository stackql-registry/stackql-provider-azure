--- 
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
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

Creates, updates, deletes, gets or lists a <code>dataset</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dataset" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.dataset" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_dataset"
    values={[
        { label: 'get_dataset', value: 'get_dataset' },
        { label: 'get_datasets_by_workspace', value: 'get_datasets_by_workspace' }
    ]}
>
<TabItem value="get_dataset">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Dataset description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this Dataset is in. If not specified, Dataset will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedServiceName" /></td>
    <td><code>object</code></td>
    <td>Linked service reference. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Parameters for dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>Columns that define the physical type schema of the dataset. Type: array (or Expression with resultType array), itemType: DatasetSchemaDataElement.</td>
</tr>
<tr>
    <td><CopyableCode code="structure" /></td>
    <td><code>object</code></td>
    <td>Columns that define the structure of the dataset. Type: array (or Expression with resultType array), itemType: DatasetDataElement.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_datasets_by_workspace">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the Dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Dataset description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this Dataset is in. If not specified, Dataset will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="linkedServiceName" /></td>
    <td><code>object</code></td>
    <td>Linked service reference. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Parameters for dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>Columns that define the physical type schema of the dataset. Type: array (or Expression with resultType array), itemType: DatasetSchemaDataElement.</td>
</tr>
<tr>
    <td><CopyableCode code="structure" /></td>
    <td><code>object</code></td>
    <td>Columns that define the structure of the dataset. Type: array (or Expression with resultType array), itemType: DatasetDataElement.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_dataset"><CopyableCode code="get_dataset" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-dataset_name"><code>dataset_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a dataset.</td>
</tr>
<tr>
    <td><a href="#get_datasets_by_workspace"><CopyableCode code="get_datasets_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists datasets.</td>
</tr>
<tr>
    <td><a href="#create_or_update_dataset"><CopyableCode code="create_or_update_dataset" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-dataset_name"><code>dataset_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-linkedServiceName"><code>linkedServiceName</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a dataset.</td>
</tr>
<tr>
    <td><a href="#create_or_update_dataset"><CopyableCode code="create_or_update_dataset" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-dataset_name"><code>dataset_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-linkedServiceName"><code>linkedServiceName</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a dataset.</td>
</tr>
<tr>
    <td><a href="#delete_dataset"><CopyableCode code="delete_dataset" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dataset_name"><code>dataset_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a dataset.</td>
</tr>
<tr>
    <td><a href="#rename_dataset"><CopyableCode code="rename_dataset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-dataset_name"><code>dataset_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a dataset.</td>
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
<tr id="parameter-dataset_name">
    <td><CopyableCode code="dataset_name" /></td>
    <td><code>string</code></td>
    <td>The dataset name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the dataset entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the dataset entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_dataset"
    values={[
        { label: 'get_dataset', value: 'get_dataset' },
        { label: 'get_datasets_by_workspace', value: 'get_datasets_by_workspace' }
    ]}
>
<TabItem value="get_dataset">

Gets a dataset.

```sql
SELECT
id,
name,
,
annotations,
description,
etag,
folder,
linkedServiceName,
parameters,
schema,
structure,
type
FROM azure.synapse_artifacts.dataset
WHERE dataset_name = '{{ dataset_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_datasets_by_workspace">

Lists datasets.

```sql
SELECT
id,
name,
,
annotations,
description,
etag,
folder,
linkedServiceName,
parameters,
schema,
structure,
type
FROM azure.synapse_artifacts.dataset
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_dataset"
    values={[
        { label: 'create_or_update_dataset', value: 'create_or_update_dataset' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_dataset">

Creates or updates a dataset.

```sql
INSERT INTO azure.synapse_artifacts.dataset (
,
type,
description,
structure,
schema,
linkedServiceName,
parameters,
annotations,
folder,
dataset_name,
endpoint,
If-Match
)
SELECT 
'{{  }}',
'{{ type }}' /* required */,
'{{ description }}',
'{{ structure }}',
'{{ schema }}',
'{{ linkedServiceName }}' /* required */,
'{{ parameters }}',
'{{ annotations }}',
'{{ folder }}',
'{{ dataset_name }}',
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
- name: dataset
  props:
    - name: dataset_name
      value: "{{ dataset_name }}"
      description: Required parameter for the dataset resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the dataset resource.
    - name: 
      value: "{{  }}"
      description: |
        Unmatched properties from the message are deserialized to this collection.
    - name: type
      value: "{{ type }}"
      description: |
        Type of dataset. Required.
    - name: description
      value: "{{ description }}"
      description: |
        Dataset description.
    - name: structure
      value: "{{ structure }}"
      description: |
        Columns that define the structure of the dataset. Type: array (or Expression with resultType array), itemType: DatasetDataElement.
    - name: schema
      value: "{{ schema }}"
      description: |
        Columns that define the physical type schema of the dataset. Type: array (or Expression with resultType array), itemType: DatasetSchemaDataElement.
    - name: linkedServiceName
      description: |
        Linked service reference. Required.
      value:
        type: "{{ type }}"
        referenceName: "{{ referenceName }}"
        parameters: "{{ parameters }}"
    - name: parameters
      value: "{{ parameters }}"
      description: |
        Parameters for dataset.
    - name: annotations
      value: "{{ annotations }}"
      description: |
        List of tags that can be used for describing the Dataset.
    - name: folder
      description: |
        The folder that this Dataset is in. If not specified, Dataset will appear at the root level.
      value:
        name: "{{ name }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the dataset entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the dataset entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_dataset"
    values={[
        { label: 'create_or_update_dataset', value: 'create_or_update_dataset' }
    ]}
>
<TabItem value="create_or_update_dataset">

Creates or updates a dataset.

```sql
REPLACE azure.synapse_artifacts.dataset
SET 
 = '{{  }}',
type = '{{ type }}',
description = '{{ description }}',
structure = '{{ structure }}',
schema = '{{ schema }}',
linkedServiceName = '{{ linkedServiceName }}',
parameters = '{{ parameters }}',
annotations = '{{ annotations }}',
folder = '{{ folder }}'
WHERE 
dataset_name = '{{ dataset_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND type = '{{ type }}' --required
AND linkedServiceName = '{{ linkedServiceName }}' --required
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
    defaultValue="delete_dataset"
    values={[
        { label: 'delete_dataset', value: 'delete_dataset' }
    ]}
>
<TabItem value="delete_dataset">

Deletes a dataset.

```sql
DELETE FROM azure.synapse_artifacts.dataset
WHERE dataset_name = '{{ dataset_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_dataset"
    values={[
        { label: 'rename_dataset', value: 'rename_dataset' }
    ]}
>
<TabItem value="rename_dataset">

Renames a dataset.

```sql
EXEC azure.synapse_artifacts.dataset.rename_dataset 
@dataset_name='{{ dataset_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
