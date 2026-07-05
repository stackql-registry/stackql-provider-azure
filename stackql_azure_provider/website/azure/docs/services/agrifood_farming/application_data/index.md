--- 
title: application_data
hide_title: false
hide_table_of_contents: false
keywords:
  - application_data
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

Creates, updates, deletes, gets or lists an <code>application_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_data" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.application_data" /></td></tr>
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
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-applicationDataId"><code>applicationDataId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create cascade delete job for application data resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-application_data_id"><code>application_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates an application data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-application_data_id"><code>application_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates an application data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-application_data_id"><code>application_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified application data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-application_data_id"><code>application_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a specified application data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minAvgMaterial"><code>minAvgMaterial</code></a>, <a href="#parameter-maxAvgMaterial"><code>maxAvgMaterial</code></a>, <a href="#parameter-minTotalMaterial"><code>minTotalMaterial</code></a>, <a href="#parameter-maxTotalMaterial"><code>maxTotalMaterial</code></a>, <a href="#parameter-minOperationStartDateTime"><code>minOperationStartDateTime</code></a>, <a href="#parameter-maxOperationStartDateTime"><code>maxOperationStartDateTime</code></a>, <a href="#parameter-minOperationEndDateTime"><code>minOperationEndDateTime</code></a>, <a href="#parameter-maxOperationEndDateTime"><code>maxOperationEndDateTime</code></a>, <a href="#parameter-minOperationModifiedDateTime"><code>minOperationModifiedDateTime</code></a>, <a href="#parameter-maxOperationModifiedDateTime"><code>maxOperationModifiedDateTime</code></a>, <a href="#parameter-minArea"><code>minArea</code></a>, <a href="#parameter-maxArea"><code>maxArea</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of application data resources across all parties.</td>
</tr>
<tr>
    <td><a href="#list_by_party_id"><CopyableCode code="list_by_party_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minAvgMaterial"><code>minAvgMaterial</code></a>, <a href="#parameter-maxAvgMaterial"><code>maxAvgMaterial</code></a>, <a href="#parameter-minTotalMaterial"><code>minTotalMaterial</code></a>, <a href="#parameter-maxTotalMaterial"><code>maxTotalMaterial</code></a>, <a href="#parameter-minOperationStartDateTime"><code>minOperationStartDateTime</code></a>, <a href="#parameter-maxOperationStartDateTime"><code>maxOperationStartDateTime</code></a>, <a href="#parameter-minOperationEndDateTime"><code>minOperationEndDateTime</code></a>, <a href="#parameter-maxOperationEndDateTime"><code>maxOperationEndDateTime</code></a>, <a href="#parameter-minOperationModifiedDateTime"><code>minOperationModifiedDateTime</code></a>, <a href="#parameter-maxOperationModifiedDateTime"><code>maxOperationModifiedDateTime</code></a>, <a href="#parameter-minArea"><code>minArea</code></a>, <a href="#parameter-maxArea"><code>maxArea</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of application data resources under a particular party.</td>
</tr>
<tr>
    <td><a href="#get_cascade_delete_job_details"><CopyableCode code="get_cascade_delete_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get cascade delete job for application data resource.</td>
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
<tr id="parameter-applicationDataId">
    <td><CopyableCode code="applicationDataId" /></td>
    <td><code>string</code></td>
    <td>Id of the application data. Required.</td>
</tr>
<tr id="parameter-application_data_id">
    <td><CopyableCode code="application_data_id" /></td>
    <td><code>string</code></td>
    <td>ID of the application data resource. Required.</td>
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
<tr id="parameter-partyId">
    <td><CopyableCode code="partyId" /></td>
    <td><code>string</code></td>
    <td>Id of the party. Required.</td>
</tr>
<tr id="parameter-party_id">
    <td><CopyableCode code="party_id" /></td>
    <td><code>string</code></td>
    <td>ID of the associated party. Required.</td>
</tr>
<tr id="parameter-maxArea">
    <td><CopyableCode code="maxArea" /></td>
    <td><code>number</code></td>
    <td>Maximum area for which operation was applied (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxAvgMaterial">
    <td><CopyableCode code="maxAvgMaterial" /></td>
    <td><code>number</code></td>
    <td>Maximum average amount of material applied during the application (inclusive). Default value is None.</td>
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
<tr id="parameter-maxOperationEndDateTime">
    <td><CopyableCode code="maxOperationEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum end date-time of the operation data, sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxOperationModifiedDateTime">
    <td><CopyableCode code="maxOperationModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum modified date-time of the operation data, sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxOperationStartDateTime">
    <td><CopyableCode code="maxOperationStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum start date-time of the operation data, sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxTotalMaterial">
    <td><CopyableCode code="maxTotalMaterial" /></td>
    <td><code>number</code></td>
    <td>Maximum total amount of material applied during the application (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minArea">
    <td><CopyableCode code="minArea" /></td>
    <td><code>number</code></td>
    <td>Minimum area for which operation was applied (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minAvgMaterial">
    <td><CopyableCode code="minAvgMaterial" /></td>
    <td><code>number</code></td>
    <td>Minimum average amount of material applied during the application (inclusive). Default value is None.</td>
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
<tr id="parameter-minOperationEndDateTime">
    <td><CopyableCode code="minOperationEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum end date-time of the operation data, sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minOperationModifiedDateTime">
    <td><CopyableCode code="minOperationModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum modified date-time of the operation data, sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minOperationStartDateTime">
    <td><CopyableCode code="minOperationStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum start date-time of the operation data, sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minTotalMaterial">
    <td><CopyableCode code="minTotalMaterial" /></td>
    <td><code>number</code></td>
    <td>Minimum total amount of material applied during the application (inclusive). Default value is None.</td>
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

Create cascade delete job for application data resource.

```sql
INSERT INTO azure.agrifood_farming.application_data (
job_id,
partyId,
applicationDataId,
endpoint
)
SELECT 
'{{ job_id }}',
'{{ partyId }}',
'{{ applicationDataId }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="create_or_update">

Creates or updates an application data resource under a particular party.

```sql
INSERT INTO azure.agrifood_farming.application_data (
party_id,
application_data_id,
endpoint
)
SELECT 
'{{ party_id }}',
'{{ application_data_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: application_data
  props:
    - name: job_id
      value: "{{ job_id }}"
      description: Required parameter for the application_data resource.
    - name: partyId
      value: "{{ partyId }}"
      description: Required parameter for the application_data resource.
    - name: applicationDataId
      value: "{{ applicationDataId }}"
      description: Required parameter for the application_data resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the application_data resource.
    - name: party_id
      value: "{{ party_id }}"
      description: Required parameter for the application_data resource.
    - name: application_data_id
      value: "{{ application_data_id }}"
      description: Required parameter for the application_data resource.
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

Creates or updates an application data resource under a particular party.

```sql
REPLACE azure.agrifood_farming.application_data
SET 
-- No updatable properties
WHERE 
party_id = '{{ party_id }}' --required
AND application_data_id = '{{ application_data_id }}' --required
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

Deletes a specified application data resource under a particular party.

```sql
DELETE FROM azure.agrifood_farming.application_data
WHERE party_id = '{{ party_id }}' --required
AND application_data_id = '{{ application_data_id }}' --required
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

Get a specified application data resource under a particular party.

```sql
EXEC azure.agrifood_farming.application_data.get_raw 
@party_id='{{ party_id }}' --required, 
@application_data_id='{{ application_data_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Returns a paginated list of application data resources across all parties.

```sql
EXEC azure.agrifood_farming.application_data.list_raw 
@endpoint='{{ endpoint }}' --required, 
@minAvgMaterial='{{ minAvgMaterial }}', 
@maxAvgMaterial='{{ maxAvgMaterial }}', 
@minTotalMaterial='{{ minTotalMaterial }}', 
@maxTotalMaterial='{{ maxTotalMaterial }}', 
@minOperationStartDateTime='{{ minOperationStartDateTime }}', 
@maxOperationStartDateTime='{{ maxOperationStartDateTime }}', 
@minOperationEndDateTime='{{ minOperationEndDateTime }}', 
@maxOperationEndDateTime='{{ maxOperationEndDateTime }}', 
@minOperationModifiedDateTime='{{ minOperationModifiedDateTime }}', 
@maxOperationModifiedDateTime='{{ maxOperationModifiedDateTime }}', 
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
<TabItem value="list_by_party_id">

Returns a paginated list of application data resources under a particular party.

```sql
EXEC azure.agrifood_farming.application_data.list_by_party_id 
@party_id='{{ party_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minAvgMaterial='{{ minAvgMaterial }}', 
@maxAvgMaterial='{{ maxAvgMaterial }}', 
@minTotalMaterial='{{ minTotalMaterial }}', 
@maxTotalMaterial='{{ maxTotalMaterial }}', 
@minOperationStartDateTime='{{ minOperationStartDateTime }}', 
@maxOperationStartDateTime='{{ maxOperationStartDateTime }}', 
@minOperationEndDateTime='{{ minOperationEndDateTime }}', 
@maxOperationEndDateTime='{{ maxOperationEndDateTime }}', 
@minOperationModifiedDateTime='{{ minOperationModifiedDateTime }}', 
@maxOperationModifiedDateTime='{{ maxOperationModifiedDateTime }}', 
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
<TabItem value="get_cascade_delete_job_details">

Get cascade delete job for application data resource.

```sql
EXEC azure.agrifood_farming.application_data.get_cascade_delete_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
