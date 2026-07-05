--- 
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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

Creates, updates, deletes, gets or lists a <code>service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_tables.service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' }
    ]}
>
<TabItem value="get_properties">

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
    <td><CopyableCode code="cors" /></td>
    <td><code>array</code></td>
    <td>The CORS properties.</td>
</tr>
<tr>
    <td><CopyableCode code="hourMetrics" /></td>
    <td><code>object</code></td>
    <td>The hour metrics properties.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>The logging properties.</td>
</tr>
<tr>
    <td><CopyableCode code="minuteMetrics" /></td>
    <td><code>object</code></td>
    <td>The minute metrics properties.</td>
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
    <td><a href="#get_properties"><CopyableCode code="get_properties" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the properties of an account's Table service, including properties for Analytics and CORS (Cross-Origin Resource Sharing) rules.</td>
</tr>
<tr>
    <td><a href="#set_properties"><CopyableCode code="set_properties" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Sets properties for an account's Table service endpoint, including properties for Analytics and CORS (Cross-Origin Resource Sharing) rules.</td>
</tr>
<tr>
    <td><a href="#get_statistics"><CopyableCode code="get_statistics" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Retrieves statistics related to replication for the Table service. It is only available on the secondary location endpoint when read-access geo-redundant replication is enabled for the account.</td>
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
<tr id="parameter-url">
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `url` parameter. (default: )</td>
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
    defaultValue="get_properties"
    values={[
        { label: 'get_properties', value: 'get_properties' }
    ]}
>
<TabItem value="get_properties">

Gets the properties of an account's Table service, including properties for Analytics and CORS (Cross-Origin Resource Sharing) rules.

```sql
SELECT
cors,
hourMetrics,
logging,
minuteMetrics
FROM azure.data_tables.service
WHERE url = '{{ url }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_properties"
    values={[
        { label: 'set_properties', value: 'set_properties' }
    ]}
>
<TabItem value="set_properties">

Sets properties for an account's Table service endpoint, including properties for Analytics and CORS (Cross-Origin Resource Sharing) rules.

```sql
REPLACE azure.data_tables.service
SET 
logging = '{{ logging }}',
hourMetrics = '{{ hourMetrics }}',
minuteMetrics = '{{ minuteMetrics }}',
cors = '{{ cors }}'
WHERE 
url = '{{ url }}' --required
AND timeout = '{{ timeout}}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_statistics"
    values={[
        { label: 'get_statistics', value: 'get_statistics' }
    ]}
>
<TabItem value="get_statistics">

Retrieves statistics related to replication for the Table service. It is only available on the secondary location endpoint when read-access geo-redundant replication is enabled for the account.

```sql
EXEC azure.data_tables.service.get_statistics 
@url='{{ url }}' --required, 
@timeout='{{ timeout }}'
;
```
</TabItem>
</Tabs>
