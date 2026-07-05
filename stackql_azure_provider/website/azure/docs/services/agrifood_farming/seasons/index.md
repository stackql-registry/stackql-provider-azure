--- 
title: seasons
hide_title: false
hide_table_of_contents: false
keywords:
  - seasons
  - agrifood_farming
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

Creates, updates, deletes, gets or lists a <code>seasons</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="seasons" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.seasons" /></td></tr>
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
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-season_id"><code>season_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a season resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-season_id"><code>season_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a season resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-season_id"><code>season_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified season resource.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-season_id"><code>season_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a specified season resource.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minStartDateTime"><code>minStartDateTime</code></a>, <a href="#parameter-maxStartDateTime"><code>maxStartDateTime</code></a>, <a href="#parameter-minEndDateTime"><code>minEndDateTime</code></a>, <a href="#parameter-maxEndDateTime"><code>maxEndDateTime</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of season resources.</td>
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
<tr id="parameter-season_id">
    <td><CopyableCode code="season_id" /></td>
    <td><code>string</code></td>
    <td>Id of the season. Required.</td>
</tr>
<tr id="parameter-maxCreatedDateTime">
    <td><CopyableCode code="maxCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxEndDateTime">
    <td><CopyableCode code="maxEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum season end datetime, sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-maxLastModifiedDateTime">
    <td><CopyableCode code="maxLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxStartDateTime">
    <td><CopyableCode code="maxStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum season start datetime, sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-minCreatedDateTime">
    <td><CopyableCode code="minCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minEndDateTime">
    <td><CopyableCode code="minEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum season end datetime, sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-minLastModifiedDateTime">
    <td><CopyableCode code="minLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minStartDateTime">
    <td><CopyableCode code="minStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum season start datetime, sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a season resource.

```sql
INSERT INTO azure.agrifood_farming.seasons (
season_id,
endpoint
)
SELECT 
'{{ season_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: seasons
  props:
    - name: season_id
      value: "{{ season_id }}"
      description: Required parameter for the seasons resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the seasons resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a season resource.

```sql
REPLACE azure.agrifood_farming.seasons
SET 
-- No updatable properties
WHERE 
season_id = '{{ season_id }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
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

Deletes a specified season resource.

```sql
DELETE FROM azure.agrifood_farming.seasons
WHERE season_id = '{{ season_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="get_raw">

Gets a specified season resource.

```sql
EXEC azure.agrifood_farming.seasons.get_raw 
@season_id='{{ season_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Returns a paginated list of season resources.

```sql
EXEC azure.agrifood_farming.seasons.list_raw 
@endpoint='{{ endpoint }}' --required, 
@minStartDateTime='{{ minStartDateTime }}', 
@maxStartDateTime='{{ maxStartDateTime }}', 
@minEndDateTime='{{ minEndDateTime }}', 
@maxEndDateTime='{{ maxEndDateTime }}', 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
</Tabs>
