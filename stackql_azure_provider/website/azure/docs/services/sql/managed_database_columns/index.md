--- 
title: managed_database_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_columns
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_database_columns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_database_columns" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_columns" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_table', value: 'list_by_table' },
        { label: 'list_by_database', value: 'list_by_database' }
    ]}
>
<TabItem value="get">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="columnType" /></td>
    <td><code>string</code></td>
    <td>The column data type. Known values are: "image", "text", "uniqueidentifier", "date", "time", "datetime2", "datetimeoffset", "tinyint", "smallint", "int", "smalldatetime", "real", "money", "datetime", "float", "sql_variant", "ntext", "bit", "decimal", "numeric", "smallmoney", "bigint", "hierarchyid", "geometry", "geography", "varbinary", "varchar", "binary", "char", "timestamp", "nvarchar", "nchar", "xml", and "sysname". (image, text, uniqueidentifier, date, time, datetime2, datetimeoffset, tinyint, smallint, int, smalldatetime, real, money, datetime, float, sql_variant, ntext, bit, decimal, numeric, smallmoney, bigint, hierarchyid, geometry, geography, varbinary, varchar, binary, char, timestamp, nvarchar, nchar, xml, sysname)</td>
</tr>
<tr>
    <td><CopyableCode code="isComputed" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the column is computed.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryOptimized" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the column belongs to a memory optimized table.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="temporalType" /></td>
    <td><code>string</code></td>
    <td>The table temporal type. Known values are: "NonTemporalTable", "HistoryTable", and "SystemVersionedTemporalTable". (NonTemporalTable, HistoryTable, SystemVersionedTemporalTable)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_table">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="columnType" /></td>
    <td><code>string</code></td>
    <td>The column data type. Known values are: "image", "text", "uniqueidentifier", "date", "time", "datetime2", "datetimeoffset", "tinyint", "smallint", "int", "smalldatetime", "real", "money", "datetime", "float", "sql_variant", "ntext", "bit", "decimal", "numeric", "smallmoney", "bigint", "hierarchyid", "geometry", "geography", "varbinary", "varchar", "binary", "char", "timestamp", "nvarchar", "nchar", "xml", and "sysname". (image, text, uniqueidentifier, date, time, datetime2, datetimeoffset, tinyint, smallint, int, smalldatetime, real, money, datetime, float, sql_variant, ntext, bit, decimal, numeric, smallmoney, bigint, hierarchyid, geometry, geography, varbinary, varchar, binary, char, timestamp, nvarchar, nchar, xml, sysname)</td>
</tr>
<tr>
    <td><CopyableCode code="isComputed" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the column is computed.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryOptimized" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the column belongs to a memory optimized table.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="temporalType" /></td>
    <td><code>string</code></td>
    <td>The table temporal type. Known values are: "NonTemporalTable", "HistoryTable", and "SystemVersionedTemporalTable". (NonTemporalTable, HistoryTable, SystemVersionedTemporalTable)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_database">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="columnType" /></td>
    <td><code>string</code></td>
    <td>The column data type. Known values are: "image", "text", "uniqueidentifier", "date", "time", "datetime2", "datetimeoffset", "tinyint", "smallint", "int", "smalldatetime", "real", "money", "datetime", "float", "sql_variant", "ntext", "bit", "decimal", "numeric", "smallmoney", "bigint", "hierarchyid", "geometry", "geography", "varbinary", "varchar", "binary", "char", "timestamp", "nvarchar", "nchar", "xml", and "sysname". (image, text, uniqueidentifier, date, time, datetime2, datetimeoffset, tinyint, smallint, int, smalldatetime, real, money, datetime, float, sql_variant, ntext, bit, decimal, numeric, smallmoney, bigint, hierarchyid, geometry, geography, varbinary, varchar, binary, char, timestamp, nvarchar, nchar, xml, sysname)</td>
</tr>
<tr>
    <td><CopyableCode code="isComputed" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the column is computed.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryOptimized" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the column belongs to a memory optimized table.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="temporalType" /></td>
    <td><code>string</code></td>
    <td>The table temporal type. Known values are: "NonTemporalTable", "HistoryTable", and "SystemVersionedTemporalTable". (NonTemporalTable, HistoryTable, SystemVersionedTemporalTable)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-column_name"><code>column_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get managed database column.</td>
</tr>
<tr>
    <td><a href="#list_by_table"><CopyableCode code="list_by_table" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-table_name"><code>table_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>List managed database columns.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>List managed database columns.</td>
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
<tr id="parameter-column_name">
    <td><CopyableCode code="column_name" /></td>
    <td><code>string</code></td>
    <td>The name of the column. Required.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>The name of the schema. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>The name of the table. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData filter expression that filters elements in the collection. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>An opaque token that identifies a starting point in the collection. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_table', value: 'list_by_table' },
        { label: 'list_by_database', value: 'list_by_database' }
    ]}
>
<TabItem value="get">

Get managed database column.

```sql
SELECT
id,
name,
columnType,
isComputed,
memoryOptimized,
systemData,
temporalType,
type
FROM azure.sql.managed_database_columns
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND table_name = '{{ table_name }}' -- required
AND column_name = '{{ column_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_table">

List managed database columns.

```sql
SELECT
id,
name,
columnType,
isComputed,
memoryOptimized,
systemData,
temporalType,
type
FROM azure.sql.managed_database_columns
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND table_name = '{{ table_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_database">

List managed database columns.

```sql
SELECT
id,
name,
columnType,
isComputed,
memoryOptimized,
systemData,
temporalType,
type
FROM azure.sql.managed_database_columns
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
;
```
</TabItem>
</Tabs>
