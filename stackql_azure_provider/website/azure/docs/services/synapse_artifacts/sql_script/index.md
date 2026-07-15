--- 
title: sql_script
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_script
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

Creates, updates, deletes, gets or lists a <code>sql_script</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_script" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.sql_script" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_sql_script"
    values={[
        { label: 'get_sql_script', value: 'get_sql_script' },
        { label: 'get_sql_scripts_by_workspace', value: 'get_sql_scripts_by_workspace' }
    ]}
>
<TabItem value="get_sql_script">

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
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>The content of the SQL script. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the SQL script.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this SQL script is in. If not specified, this SQL script will appear at the root level.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_sql_scripts_by_workspace">

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
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>The content of the SQL script. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the SQL script.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="folder" /></td>
    <td><code>object</code></td>
    <td>The folder that this SQL script is in. If not specified, this SQL script will appear at the root level.</td>
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
    <td><a href="#get_sql_script"><CopyableCode code="get_sql_script" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-sql_script_name"><code>sql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a sql script.</td>
</tr>
<tr>
    <td><a href="#get_sql_scripts_by_workspace"><CopyableCode code="get_sql_scripts_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists sql scripts.</td>
</tr>
<tr>
    <td><a href="#create_or_update_sql_script"><CopyableCode code="create_or_update_sql_script" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sql_script_name"><code>sql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a Sql Script.</td>
</tr>
<tr>
    <td><a href="#create_or_update_sql_script"><CopyableCode code="create_or_update_sql_script" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-sql_script_name"><code>sql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a Sql Script.</td>
</tr>
<tr>
    <td><a href="#delete_sql_script"><CopyableCode code="delete_sql_script" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-sql_script_name"><code>sql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a Sql Script.</td>
</tr>
<tr>
    <td><a href="#rename_sql_script"><CopyableCode code="rename_sql_script" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sql_script_name"><code>sql_script_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a sqlScript.</td>
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
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-sql_script_name">
    <td><CopyableCode code="sql_script_name" /></td>
    <td><code>string</code></td>
    <td>The sql script name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the SQL script entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the sql compute entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_sql_script"
    values={[
        { label: 'get_sql_script', value: 'get_sql_script' },
        { label: 'get_sql_scripts_by_workspace', value: 'get_sql_scripts_by_workspace' }
    ]}
>
<TabItem value="get_sql_script">

Gets a sql script.

```sql
SELECT
id,
name,
,
content,
description,
etag,
folder,
type
FROM azure.synapse_artifacts.sql_script
WHERE sql_script_name = '{{ sql_script_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_sql_scripts_by_workspace">

Lists sql scripts.

```sql
SELECT
id,
name,
,
content,
description,
etag,
folder,
type
FROM azure.synapse_artifacts.sql_script
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_sql_script"
    values={[
        { label: 'create_or_update_sql_script', value: 'create_or_update_sql_script' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_sql_script">

Creates or updates a Sql Script.

```sql
INSERT INTO azure.synapse_artifacts.sql_script (
name,
properties,
sql_script_name,
endpoint,
If-Match
)
SELECT 
'{{ name }}' /* required */,
'{{ properties }}' /* required */,
'{{ sql_script_name }}',
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
- name: sql_script
  props:
    - name: sql_script_name
      value: "{{ sql_script_name }}"
      description: Required parameter for the sql_script resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the sql_script resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource. Required.
    - name: properties
      description: |
        Properties of sql script. Required.
      value:
        : "{{  }}"
        description: "{{ description }}"
        type: "{{ type }}"
        content:
          : "{{  }}"
          query: "{{ query }}"
          currentConnection:
            : "{{  }}"
            type: "{{ type }}"
            name: "{{ name }}"
            poolName: "{{ poolName }}"
            databaseName: "{{ databaseName }}"
          resultLimit: {{ resultLimit }}
          metadata:
            : "{{  }}"
            language: "{{ language }}"
        folder:
          name: "{{ name }}"
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the SQL script entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the SQL script entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_sql_script"
    values={[
        { label: 'create_or_update_sql_script', value: 'create_or_update_sql_script' }
    ]}
>
<TabItem value="create_or_update_sql_script">

Creates or updates a Sql Script.

```sql
REPLACE azure.synapse_artifacts.sql_script
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
sql_script_name = '{{ sql_script_name }}' --required
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
    defaultValue="delete_sql_script"
    values={[
        { label: 'delete_sql_script', value: 'delete_sql_script' }
    ]}
>
<TabItem value="delete_sql_script">

Deletes a Sql Script.

```sql
DELETE FROM azure.synapse_artifacts.sql_script
WHERE sql_script_name = '{{ sql_script_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_sql_script"
    values={[
        { label: 'rename_sql_script', value: 'rename_sql_script' }
    ]}
>
<TabItem value="rename_sql_script">

Renames a sqlScript.

```sql
EXEC azure.synapse_artifacts.sql_script.rename_sql_script 
@sql_script_name='{{ sql_script_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
