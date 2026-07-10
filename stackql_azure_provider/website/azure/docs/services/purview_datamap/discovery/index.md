--- 
title: discovery
hide_title: false
hide_table_of_contents: false
keywords:
  - discovery
  - purview_datamap
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

Creates, updates, deletes, gets or lists a <code>discovery</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="discovery" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_datamap.discovery" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get data using search.</td>
</tr>
<tr>
    <td><a href="#suggest"><CopyableCode code="suggest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get search suggestions by query criteria.</td>
</tr>
<tr>
    <td><a href="#auto_complete"><CopyableCode code="auto_complete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get auto complete options.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' },
        { label: 'suggest', value: 'suggest' },
        { label: 'auto_complete', value: 'auto_complete' }
    ]}
>
<TabItem value="query">

Get data using search.

```sql
EXEC azure.purview_datamap.discovery.query 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"keywords": "{{ keywords }}", 
"limit": {{ limit }}, 
"continuationToken": "{{ continuationToken }}", 
"orderby": "{{ orderby }}", 
"filter": "{{ filter }}", 
"facets": "{{ facets }}", 
"taxonomySetting": "{{ taxonomySetting }}"
}'
;
```
</TabItem>
<TabItem value="suggest">

Get search suggestions by query criteria.

```sql
EXEC azure.purview_datamap.discovery.suggest 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"keywords": "{{ keywords }}", 
"limit": {{ limit }}, 
"filter": "{{ filter }}"
}'
;
```
</TabItem>
<TabItem value="auto_complete">

Get auto complete options.

```sql
EXEC azure.purview_datamap.discovery.auto_complete 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"keywords": "{{ keywords }}", 
"limit": {{ limit }}, 
"filter": "{{ filter }}"
}'
;
```
</TabItem>
</Tabs>
