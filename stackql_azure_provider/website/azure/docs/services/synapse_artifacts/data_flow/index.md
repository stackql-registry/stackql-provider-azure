--- 
title: data_flow
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flow
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

Creates, updates, deletes, gets or lists a <code>data_flow</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_flow" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.data_flow" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_data_flow"
    values={[
        { label: 'get_data_flow', value: 'get_data_flow' },
        { label: 'get_data_flows_by_workspace', value: 'get_data_flows_by_workspace' }
    ]}
>
<TabItem value="get_data_flow">

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
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the data flow.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the data flow.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this data flow is in. If not specified, Data flow will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_data_flows_by_workspace">

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
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the data flow.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the data flow.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this data flow is in. If not specified, Data flow will appear at the root level.</td>
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
    <td><a href="#get_data_flow"><CopyableCode code="get_data_flow" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-data_flow_name"><code>data_flow_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a data flow.</td>
</tr>
<tr>
    <td><a href="#get_data_flows_by_workspace"><CopyableCode code="get_data_flows_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists data flows.</td>
</tr>
<tr>
    <td><a href="#create_or_update_data_flow"><CopyableCode code="create_or_update_data_flow" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data_flow_name"><code>data_flow_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a data flow.</td>
</tr>
<tr>
    <td><a href="#create_or_update_data_flow"><CopyableCode code="create_or_update_data_flow" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-data_flow_name"><code>data_flow_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a data flow.</td>
</tr>
<tr>
    <td><a href="#delete_data_flow"><CopyableCode code="delete_data_flow" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-data_flow_name"><code>data_flow_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a data flow.</td>
</tr>
<tr>
    <td><a href="#rename_data_flow"><CopyableCode code="rename_data_flow" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-data_flow_name"><code>data_flow_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a dataflow.</td>
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
<tr id="parameter-data_flow_name">
    <td><CopyableCode code="data_flow_name" /></td>
    <td><code>string</code></td>
    <td>The data flow name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the data flow entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the data flow entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_data_flow"
    values={[
        { label: 'get_data_flow', value: 'get_data_flow' },
        { label: 'get_data_flows_by_workspace', value: 'get_data_flows_by_workspace' }
    ]}
>
<TabItem value="get_data_flow">

Gets a data flow.

```sql
SELECT
id,
name,
annotations,
description,
etag,
folder,
type
FROM azure.synapse_artifacts.data_flow
WHERE data_flow_name = '{{ data_flow_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_data_flows_by_workspace">

Lists data flows.

```sql
SELECT
id,
name,
annotations,
description,
etag,
folder,
type
FROM azure.synapse_artifacts.data_flow
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_data_flow"
    values={[
        { label: 'create_or_update_data_flow', value: 'create_or_update_data_flow' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_data_flow">

Creates or updates a data flow.

```sql
INSERT INTO azure.synapse_artifacts.data_flow (
type,
description,
annotations,
folder,
data_flow_name,
endpoint,
If-Match
)
SELECT 
'{{ type }}' /* required */,
'{{ description }}',
'{{ annotations }}',
'{{ folder }}',
'{{ data_flow_name }}',
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
- name: data_flow
  props:
    - name: data_flow_name
      value: "{{ data_flow_name }}"
      description: Required parameter for the data_flow resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the data_flow resource.
    - name: type
      value: "{{ type }}"
      description: |
        Type of data flow. Required.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the data flow.
    - name: annotations
      value: "{{ annotations }}"
      description: |
        List of tags that can be used for describing the data flow.
    - name: folder
      description: |
        The folder that this data flow is in. If not specified, Data flow will appear at the root level.
      value:
        name: "{{ name }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the data flow entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the data flow entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_data_flow"
    values={[
        { label: 'create_or_update_data_flow', value: 'create_or_update_data_flow' }
    ]}
>
<TabItem value="create_or_update_data_flow">

Creates or updates a data flow.

```sql
REPLACE azure.synapse_artifacts.data_flow
SET 
type = '{{ type }}',
description = '{{ description }}',
annotations = '{{ annotations }}',
folder = '{{ folder }}'
WHERE 
data_flow_name = '{{ data_flow_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND type = '{{ type }}' --required
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
    defaultValue="delete_data_flow"
    values={[
        { label: 'delete_data_flow', value: 'delete_data_flow' }
    ]}
>
<TabItem value="delete_data_flow">

Deletes a data flow.

```sql
DELETE FROM azure.synapse_artifacts.data_flow
WHERE data_flow_name = '{{ data_flow_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_data_flow"
    values={[
        { label: 'rename_data_flow', value: 'rename_data_flow' }
    ]}
>
<TabItem value="rename_data_flow">

Renames a dataflow.

```sql
EXEC azure.synapse_artifacts.data_flow.rename_data_flow 
@data_flow_name='{{ data_flow_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
