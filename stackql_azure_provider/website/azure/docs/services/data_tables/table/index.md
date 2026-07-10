--- 
title: table
hide_title: false
hide_table_of_contents: false
keywords:
  - table
  - data_tables
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

Creates, updates, deletes, gets or lists a <code>table</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="table" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_tables.table" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_access_policy"
    values={[
        { label: 'get_access_policy', value: 'get_access_policy' }
    ]}
>
<TabItem value="get_access_policy">

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
    <td><CopyableCode code="identifiers" /></td>
    <td><code>array</code></td>
    <td>An array of signed identifiers. Required.</td>
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
    <td><a href="#get_access_policy"><CopyableCode code="get_access_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves details about any stored access policies specified on the table that may be used with Shared Access Signatures.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-$format"><code>$format</code></a>, <a href="#parameter-Prefer"><code>Prefer</code></a></td>
    <td>Creates a new table under the given account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td></td>
    <td>Deletes an existing table.</td>
</tr>
<tr>
    <td><a href="#set_access_policy"><CopyableCode code="set_access_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-account"><code>account</code></a>, <a href="#parameter-identifiers"><code>identifiers</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Sets stored access policies for the table that may be used with Shared Access Signatures.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-$format"><code>$format</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-NextTableName"><code>NextTableName</code></a></td>
    <td>Queries tables under the given account.</td>
</tr>
<tr>
    <td><a href="#query_entities"><CopyableCode code="query_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-$format"><code>$format</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-NextPartitionKey"><code>NextPartitionKey</code></a>, <a href="#parameter-NextRowKey"><code>NextRowKey</code></a></td>
    <td>Queries entities under the given table.</td>
</tr>
<tr>
    <td><a href="#query_entity_with_partition_and_row_key"><CopyableCode code="query_entity_with_partition_and_row_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-partition_key"><code>partition_key</code></a>, <a href="#parameter-row_key"><code>row_key</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-$format"><code>$format</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieve a single entity.</td>
</tr>
<tr>
    <td><a href="#update_entity"><CopyableCode code="update_entity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-partition_key"><code>partition_key</code></a>, <a href="#parameter-row_key"><code>row_key</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Update entity in a table.</td>
</tr>
<tr>
    <td><a href="#merge_entity"><CopyableCode code="merge_entity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-partition_key"><code>partition_key</code></a>, <a href="#parameter-row_key"><code>row_key</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Merge entity in a table.</td>
</tr>
<tr>
    <td><a href="#delete_entity"><CopyableCode code="delete_entity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-partition_key"><code>partition_key</code></a>, <a href="#parameter-row_key"><code>row_key</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Deletes the specified entity in a table.</td>
</tr>
<tr>
    <td><a href="#insert_entity"><CopyableCode code="insert_entity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a>, <a href="#parameter-$format"><code>$format</code></a>, <a href="#parameter-Prefer"><code>Prefer</code></a></td>
    <td>Insert entity in a table.</td>
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
<tr id="parameter-account">
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Cosmos DB Table API account name. (default: )</td>
</tr>
<tr id="parameter-partition_key">
    <td><CopyableCode code="partition_key" /></td>
    <td><code>string</code></td>
    <td>The partition key of the entity. Required.</td>
</tr>
<tr id="parameter-row_key">
    <td><CopyableCode code="row_key" /></td>
    <td><code>string</code></td>
    <td>The row key of the entity. Required.</td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>The name of the table. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter expression. Default value is None.</td>
</tr>
<tr id="parameter-$format">
    <td><CopyableCode code="$format" /></td>
    <td><code>string</code></td>
    <td>Specifies the metadata format for the response. Known values are: "application/json;odata=nometadata", "application/json;odata=minimalmetadata", and "application/json;odata=fullmetadata". Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>Select expression using OData notation. Limits the columns on each record to just those requested. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of records to return. Default value is None.</td>
</tr>
<tr id="parameter-NextPartitionKey">
    <td><CopyableCode code="NextPartitionKey" /></td>
    <td><code>string</code></td>
    <td>An entity partition key query continuation token from a previous call. Default value is None.</td>
</tr>
<tr id="parameter-NextRowKey">
    <td><CopyableCode code="NextRowKey" /></td>
    <td><code>string</code></td>
    <td>An entity row key query continuation token from a previous call. Default value is None.</td>
</tr>
<tr id="parameter-NextTableName">
    <td><CopyableCode code="NextTableName" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-Prefer">
    <td><CopyableCode code="Prefer" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the response should include the inserted entity in the payload. Possible values are return-no-content and return-content. Known values are: "return-no-content" and "return-content". Default value is None.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout parameter is expressed in seconds. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_access_policy"
    values={[
        { label: 'get_access_policy', value: 'get_access_policy' }
    ]}
>
<TabItem value="get_access_policy">

Retrieves details about any stored access policies specified on the table that may be used with Shared Access Signatures.

```sql
SELECT
identifiers
FROM azure.data_tables.table
WHERE table_name = '{{ table_name }}' -- required
AND account = '{{ account }}' -- required
AND timeout = '{{ timeout }}'
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

Creates a new table under the given account.

```sql
INSERT INTO azure.data_tables.table (
TableName,
odata,
account,
$format,
Prefer
)
SELECT 
'{{ TableName }}',
'{{ odata }}',
'{{ account }}',
'{{ $format }}',
'{{ Prefer }}'
RETURNING
TableName,
odata
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: table
  props:
    - name: account
      value: "{{ account }}"
      description: Required parameter for the table resource.
    - name: TableName
      value: "{{ TableName }}"
      description: |
        The name of the table.
    - name: odata
      value:
        type: "{{ type }}"
        id: "{{ id }}"
        editLink: "{{ editLink }}"
    - name: $format
      value: "{{ $format }}"
      description: Specifies the metadata format for the response. Known values are: "application/json;odata=nometadata", "application/json;odata=minimalmetadata", and "application/json;odata=fullmetadata". Default value is None.
      description: Specifies the metadata format for the response. Known values are: "application/json;odata=nometadata", "application/json;odata=minimalmetadata", and "application/json;odata=fullmetadata". Default value is None.
    - name: Prefer
      value: "{{ Prefer }}"
      description: Specifies whether the response should include the created table in the payload. Possible values are return-no-content and return-content. Known values are: "return-no-content" and "return-content". Default value is None.
      description: Specifies whether the response should include the created table in the payload. Possible values are return-no-content and return-content. Known values are: "return-no-content" and "return-content". Default value is None.
`}</CodeBlock>

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

Deletes an existing table.

```sql
DELETE FROM azure.data_tables.table
WHERE table_name = '{{ table_name }}' --required
AND account = '{{ account }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="set_access_policy"
    values={[
        { label: 'set_access_policy', value: 'set_access_policy' },
        { label: 'query', value: 'query' },
        { label: 'query_entities', value: 'query_entities' },
        { label: 'query_entity_with_partition_and_row_key', value: 'query_entity_with_partition_and_row_key' },
        { label: 'update_entity', value: 'update_entity' },
        { label: 'merge_entity', value: 'merge_entity' },
        { label: 'delete_entity', value: 'delete_entity' },
        { label: 'insert_entity', value: 'insert_entity' }
    ]}
>
<TabItem value="set_access_policy">

Sets stored access policies for the table that may be used with Shared Access Signatures.

```sql
EXEC azure.data_tables.table.set_access_policy 
@table_name='{{ table_name }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"identifiers": "{{ identifiers }}"
}'
;
```
</TabItem>
<TabItem value="query">

Queries tables under the given account.

```sql
EXEC azure.data_tables.table.query 
@account='{{ account }}' --required, 
@$format='{{ $format }}', 
@$top='{{ $top }}', 
@$select='{{ $select }}', 
@$filter='{{ $filter }}', 
@NextTableName='{{ NextTableName }}'
;
```
</TabItem>
<TabItem value="query_entities">

Queries entities under the given table.

```sql
EXEC azure.data_tables.table.query_entities 
@table_name='{{ table_name }}' --required, 
@account='{{ account }}' --required, 
@$format='{{ $format }}', 
@$top='{{ $top }}', 
@$select='{{ $select }}', 
@$filter='{{ $filter }}', 
@timeout='{{ timeout }}', 
@NextPartitionKey='{{ NextPartitionKey }}', 
@NextRowKey='{{ NextRowKey }}'
;
```
</TabItem>
<TabItem value="query_entity_with_partition_and_row_key">

Retrieve a single entity.

```sql
EXEC azure.data_tables.table.query_entity_with_partition_and_row_key 
@table_name='{{ table_name }}' --required, 
@partition_key='{{ partition_key }}' --required, 
@row_key='{{ row_key }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}', 
@$format='{{ $format }}', 
@$select='{{ $select }}', 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="update_entity">

Update entity in a table.

```sql
EXEC azure.data_tables.table.update_entity 
@table_name='{{ table_name }}' --required, 
@partition_key='{{ partition_key }}' --required, 
@row_key='{{ row_key }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="merge_entity">

Merge entity in a table.

```sql
EXEC azure.data_tables.table.merge_entity 
@table_name='{{ table_name }}' --required, 
@partition_key='{{ partition_key }}' --required, 
@row_key='{{ row_key }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="delete_entity">

Deletes the specified entity in a table.

```sql
EXEC azure.data_tables.table.delete_entity 
@table_name='{{ table_name }}' --required, 
@partition_key='{{ partition_key }}' --required, 
@row_key='{{ row_key }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
<TabItem value="insert_entity">

Insert entity in a table.

```sql
EXEC azure.data_tables.table.insert_entity 
@table_name='{{ table_name }}' --required, 
@account='{{ account }}' --required, 
@timeout='{{ timeout }}', 
@$format='{{ $format }}', 
@Prefer='{{ Prefer }}'
;
```
</TabItem>
</Tabs>
