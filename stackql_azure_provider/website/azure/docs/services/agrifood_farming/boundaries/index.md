--- 
title: boundaries
hide_title: false
hide_table_of_contents: false
keywords:
  - boundaries
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

Creates, updates, deletes, gets or lists a <code>boundaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="boundaries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.boundaries" /></td></tr>
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
    <td><a href="#create_cascade_delete_job"><CopyableCode code="create_cascade_delete_job" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-boundaryId"><code>boundaryId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a cascade delete job for specified boundary.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-boundary_id"><code>boundary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a boundary resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-boundary_id"><code>boundary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a boundary resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-boundary_id"><code>boundary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified boundary resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-boundary_id"><code>boundary_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a specified boundary resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-parentType"><code>parentType</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-minArea"><code>minArea</code></a>, <a href="#parameter-maxArea"><code>maxArea</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of boundary resources across all parties.</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Search for boundaries across all parties by fields and intersecting geometry.</td>
</tr>
<tr>
    <td><a href="#list_by_party_id"><CopyableCode code="list_by_party_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-parentType"><code>parentType</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-minArea"><code>minArea</code></a>, <a href="#parameter-maxArea"><code>maxArea</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of boundary resources under a particular party.</td>
</tr>
<tr>
    <td><a href="#search_by_party_id"><CopyableCode code="search_by_party_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Search for boundaries by fields and intersecting geometry.</td>
</tr>
<tr>
    <td><a href="#get_cascade_delete_job_details"><CopyableCode code="get_cascade_delete_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get cascade delete job for specified boundary.</td>
</tr>
<tr>
    <td><a href="#get_overlap"><CopyableCode code="get_overlap" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-boundary_id"><code>boundary_id</code></a>, <a href="#parameter-otherPartyId"><code>otherPartyId</code></a>, <a href="#parameter-otherBoundaryId"><code>otherBoundaryId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Returns overlapping area between two boundary Ids.</td>
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
<tr id="parameter-boundaryId">
    <td><CopyableCode code="boundaryId" /></td>
    <td><code>string</code></td>
    <td>ID of the boundary to be deleted. Required.</td>
</tr>
<tr id="parameter-boundary_id">
    <td><CopyableCode code="boundary_id" /></td>
    <td><code>string</code></td>
    <td>Id of the boundary. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Id of the job. Required.</td>
</tr>
<tr id="parameter-otherBoundaryId">
    <td><CopyableCode code="otherBoundaryId" /></td>
    <td><code>string</code></td>
    <td>Id of the other boundary. Required.</td>
</tr>
<tr id="parameter-otherPartyId">
    <td><CopyableCode code="otherPartyId" /></td>
    <td><code>string</code></td>
    <td>PartyId of the other field. Required.</td>
</tr>
<tr id="parameter-partyId">
    <td><CopyableCode code="partyId" /></td>
    <td><code>string</code></td>
    <td>ID of the associated party. Required.</td>
</tr>
<tr id="parameter-party_id">
    <td><CopyableCode code="party_id" /></td>
    <td><code>string</code></td>
    <td>Id of the party. Required.</td>
</tr>
<tr id="parameter-maxArea">
    <td><CopyableCode code="maxArea" /></td>
    <td><code>number</code></td>
    <td>Maximum acreage of the boundary (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxCreatedDateTime">
    <td><CopyableCode code="maxCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxLastModifiedDateTime">
    <td><CopyableCode code="maxLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minArea">
    <td><CopyableCode code="minArea" /></td>
    <td><code>number</code></td>
    <td>Minimum area of the boundary (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minCreatedDateTime">
    <td><CopyableCode code="minCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minLastModifiedDateTime">
    <td><CopyableCode code="minLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-parentType">
    <td><CopyableCode code="parentType" /></td>
    <td><code>string</code></td>
    <td>Type of the parent it belongs to. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type it belongs to. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_cascade_delete_job"
    values={[
        { label: 'create_cascade_delete_job', value: 'create_cascade_delete_job' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_cascade_delete_job">

Create a cascade delete job for specified boundary.

```sql
INSERT INTO azure.agrifood_farming.boundaries (
job_id,
partyId,
boundaryId,
endpoint
)
SELECT 
'{{ job_id }}',
'{{ partyId }}',
'{{ boundaryId }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="create_or_update">

Creates or updates a boundary resource.

```sql
INSERT INTO azure.agrifood_farming.boundaries (
party_id,
boundary_id,
endpoint
)
SELECT 
'{{ party_id }}',
'{{ boundary_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: boundaries
  props:
    - name: job_id
      value: "{{ job_id }}"
      description: Required parameter for the boundaries resource.
    - name: partyId
      value: "{{ partyId }}"
      description: Required parameter for the boundaries resource.
    - name: boundaryId
      value: "{{ boundaryId }}"
      description: Required parameter for the boundaries resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the boundaries resource.
    - name: party_id
      value: "{{ party_id }}"
      description: Required parameter for the boundaries resource.
    - name: boundary_id
      value: "{{ boundary_id }}"
      description: Required parameter for the boundaries resource.
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

Creates or updates a boundary resource.

```sql
REPLACE azure.agrifood_farming.boundaries
SET 
-- No updatable properties
WHERE 
party_id = '{{ party_id }}' --required
AND boundary_id = '{{ boundary_id }}' --required
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

Deletes a specified boundary resource under a particular party.

```sql
DELETE FROM azure.agrifood_farming.boundaries
WHERE party_id = '{{ party_id }}' --required
AND boundary_id = '{{ boundary_id }}' --required
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
        { label: 'list_raw', value: 'list_raw' },
        { label: 'search', value: 'search' },
        { label: 'list_by_party_id', value: 'list_by_party_id' },
        { label: 'search_by_party_id', value: 'search_by_party_id' },
        { label: 'get_cascade_delete_job_details', value: 'get_cascade_delete_job_details' },
        { label: 'get_overlap', value: 'get_overlap' }
    ]}
>
<TabItem value="get_raw">

Gets a specified boundary resource under a particular party.

```sql
EXEC azure.agrifood_farming.boundaries.get_raw 
@party_id='{{ party_id }}' --required, 
@boundary_id='{{ boundary_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Returns a paginated list of boundary resources across all parties.

```sql
EXEC azure.agrifood_farming.boundaries.list_raw 
@endpoint='{{ endpoint }}' --required, 
@parentType='{{ parentType }}', 
@type='{{ type }}', 
@minArea='{{ minArea }}', 
@maxArea='{{ maxArea }}', 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="search">

Search for boundaries across all parties by fields and intersecting geometry.

```sql
EXEC azure.agrifood_farming.boundaries.search 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_by_party_id">

Returns a paginated list of boundary resources under a particular party.

```sql
EXEC azure.agrifood_farming.boundaries.list_by_party_id 
@party_id='{{ party_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@parentType='{{ parentType }}', 
@type='{{ type }}', 
@minArea='{{ minArea }}', 
@maxArea='{{ maxArea }}', 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="search_by_party_id">

Search for boundaries by fields and intersecting geometry.

```sql
EXEC azure.agrifood_farming.boundaries.search_by_party_id 
@party_id='{{ party_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_cascade_delete_job_details">

Get cascade delete job for specified boundary.

```sql
EXEC azure.agrifood_farming.boundaries.get_cascade_delete_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_overlap">

Returns overlapping area between two boundary Ids.

```sql
EXEC azure.agrifood_farming.boundaries.get_overlap 
@party_id='{{ party_id }}' --required, 
@boundary_id='{{ boundary_id }}' --required, 
@otherPartyId='{{ otherPartyId }}' --required, 
@otherBoundaryId='{{ otherBoundaryId }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
