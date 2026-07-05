--- 
title: seasonal_fields
hide_title: false
hide_table_of_contents: false
keywords:
  - seasonal_fields
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

Creates, updates, deletes, gets or lists a <code>seasonal_fields</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="seasonal_fields" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.seasonal_fields" /></td></tr>
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
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-seasonalFieldId"><code>seasonalFieldId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a cascade delete job for specified seasonal field.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-seasonal_field_id"><code>seasonal_field_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or Updates a seasonal field resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-seasonal_field_id"><code>seasonal_field_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or Updates a seasonal field resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-seasonal_field_id"><code>seasonal_field_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified seasonal-field resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-seasonal_field_id"><code>seasonal_field_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a specified seasonal field resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of seasonal field resources across all parties.</td>
</tr>
<tr>
    <td><a href="#list_by_party_id"><CopyableCode code="list_by_party_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of seasonal field resources under a particular party.</td>
</tr>
<tr>
    <td><a href="#get_cascade_delete_job_details"><CopyableCode code="get_cascade_delete_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get cascade delete job for specified seasonal field.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Id of the job. Required.</td>
</tr>
<tr id="parameter-partyId">
    <td><CopyableCode code="partyId" /></td>
    <td><code>string</code></td>
    <td>ID of the associated party. Required.</td>
</tr>
<tr id="parameter-party_id">
    <td><CopyableCode code="party_id" /></td>
    <td><code>string</code></td>
    <td>Id of the associated party. Required.</td>
</tr>
<tr id="parameter-seasonalFieldId">
    <td><CopyableCode code="seasonalFieldId" /></td>
    <td><code>string</code></td>
    <td>ID of the seasonalField to be deleted. Required.</td>
</tr>
<tr id="parameter-seasonal_field_id">
    <td><CopyableCode code="seasonal_field_id" /></td>
    <td><code>string</code></td>
    <td>Id of the seasonal field. Required.</td>
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
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
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

Create a cascade delete job for specified seasonal field.

```sql
INSERT INTO azure.agrifood_farming.seasonal_fields (
job_id,
partyId,
seasonalFieldId,
endpoint
)
SELECT 
'{{ job_id }}',
'{{ partyId }}',
'{{ seasonalFieldId }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="create_or_update">

Creates or Updates a seasonal field resource under a particular party.

```sql
INSERT INTO azure.agrifood_farming.seasonal_fields (
party_id,
seasonal_field_id,
endpoint
)
SELECT 
'{{ party_id }}',
'{{ seasonal_field_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: seasonal_fields
  props:
    - name: job_id
      value: "{{ job_id }}"
      description: Required parameter for the seasonal_fields resource.
    - name: partyId
      value: "{{ partyId }}"
      description: Required parameter for the seasonal_fields resource.
    - name: seasonalFieldId
      value: "{{ seasonalFieldId }}"
      description: Required parameter for the seasonal_fields resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the seasonal_fields resource.
    - name: party_id
      value: "{{ party_id }}"
      description: Required parameter for the seasonal_fields resource.
    - name: seasonal_field_id
      value: "{{ seasonal_field_id }}"
      description: Required parameter for the seasonal_fields resource.
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

Creates or Updates a seasonal field resource under a particular party.

```sql
REPLACE azure.agrifood_farming.seasonal_fields
SET 
-- No updatable properties
WHERE 
party_id = '{{ party_id }}' --required
AND seasonal_field_id = '{{ seasonal_field_id }}' --required
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

Deletes a specified seasonal-field resource under a particular party.

```sql
DELETE FROM azure.agrifood_farming.seasonal_fields
WHERE party_id = '{{ party_id }}' --required
AND seasonal_field_id = '{{ seasonal_field_id }}' --required
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
        { label: 'list_by_party_id', value: 'list_by_party_id' },
        { label: 'get_cascade_delete_job_details', value: 'get_cascade_delete_job_details' }
    ]}
>
<TabItem value="get_raw">

Gets a specified seasonal field resource under a particular party.

```sql
EXEC azure.agrifood_farming.seasonal_fields.get_raw 
@party_id='{{ party_id }}' --required, 
@seasonal_field_id='{{ seasonal_field_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Returns a paginated list of seasonal field resources across all parties.

```sql
EXEC azure.agrifood_farming.seasonal_fields.list_raw 
@endpoint='{{ endpoint }}' --required, 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="list_by_party_id">

Returns a paginated list of seasonal field resources under a particular party.

```sql
EXEC azure.agrifood_farming.seasonal_fields.list_by_party_id 
@party_id='{{ party_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="get_cascade_delete_job_details">

Get cascade delete job for specified seasonal field.

```sql
EXEC azure.agrifood_farming.seasonal_fields.get_cascade_delete_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
