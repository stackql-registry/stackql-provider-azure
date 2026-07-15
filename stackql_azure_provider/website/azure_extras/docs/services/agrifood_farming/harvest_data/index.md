--- 
title: harvest_data
hide_title: false
hide_table_of_contents: false
keywords:
  - harvest_data
  - agrifood_farming
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>harvest_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="harvest_data" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood_farming.harvest_data" /></td></tr>
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
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-harvest_data_id"><code>harvest_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates harvest data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-harvest_data_id"><code>harvest_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates harvest data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-harvest_data_id"><code>harvest_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified harvest data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-harvest_data_id"><code>harvest_data_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a specified harvest data resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minTotalYield"><code>minTotalYield</code></a>, <a href="#parameter-maxTotalYield"><code>maxTotalYield</code></a>, <a href="#parameter-minAvgYield"><code>minAvgYield</code></a>, <a href="#parameter-maxAvgYield"><code>maxAvgYield</code></a>, <a href="#parameter-minTotalWetMass"><code>minTotalWetMass</code></a>, <a href="#parameter-maxTotalWetMass"><code>maxTotalWetMass</code></a>, <a href="#parameter-minAvgWetMass"><code>minAvgWetMass</code></a>, <a href="#parameter-maxAvgWetMass"><code>maxAvgWetMass</code></a>, <a href="#parameter-minAvgMoisture"><code>minAvgMoisture</code></a>, <a href="#parameter-maxAvgMoisture"><code>maxAvgMoisture</code></a>, <a href="#parameter-minAvgSpeed"><code>minAvgSpeed</code></a>, <a href="#parameter-maxAvgSpeed"><code>maxAvgSpeed</code></a>, <a href="#parameter-minOperationStartDateTime"><code>minOperationStartDateTime</code></a>, <a href="#parameter-maxOperationStartDateTime"><code>maxOperationStartDateTime</code></a>, <a href="#parameter-minOperationEndDateTime"><code>minOperationEndDateTime</code></a>, <a href="#parameter-maxOperationEndDateTime"><code>maxOperationEndDateTime</code></a>, <a href="#parameter-minOperationModifiedDateTime"><code>minOperationModifiedDateTime</code></a>, <a href="#parameter-maxOperationModifiedDateTime"><code>maxOperationModifiedDateTime</code></a>, <a href="#parameter-minArea"><code>minArea</code></a>, <a href="#parameter-maxArea"><code>maxArea</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of harvest data resources across all parties.</td>
</tr>
<tr>
    <td><a href="#list_by_party_id"><CopyableCode code="list_by_party_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minTotalYield"><code>minTotalYield</code></a>, <a href="#parameter-maxTotalYield"><code>maxTotalYield</code></a>, <a href="#parameter-minAvgYield"><code>minAvgYield</code></a>, <a href="#parameter-maxAvgYield"><code>maxAvgYield</code></a>, <a href="#parameter-minTotalWetMass"><code>minTotalWetMass</code></a>, <a href="#parameter-maxTotalWetMass"><code>maxTotalWetMass</code></a>, <a href="#parameter-minAvgWetMass"><code>minAvgWetMass</code></a>, <a href="#parameter-maxAvgWetMass"><code>maxAvgWetMass</code></a>, <a href="#parameter-minAvgMoisture"><code>minAvgMoisture</code></a>, <a href="#parameter-maxAvgMoisture"><code>maxAvgMoisture</code></a>, <a href="#parameter-minAvgSpeed"><code>minAvgSpeed</code></a>, <a href="#parameter-maxAvgSpeed"><code>maxAvgSpeed</code></a>, <a href="#parameter-minOperationStartDateTime"><code>minOperationStartDateTime</code></a>, <a href="#parameter-maxOperationStartDateTime"><code>maxOperationStartDateTime</code></a>, <a href="#parameter-minOperationEndDateTime"><code>minOperationEndDateTime</code></a>, <a href="#parameter-maxOperationEndDateTime"><code>maxOperationEndDateTime</code></a>, <a href="#parameter-minOperationModifiedDateTime"><code>minOperationModifiedDateTime</code></a>, <a href="#parameter-maxOperationModifiedDateTime"><code>maxOperationModifiedDateTime</code></a>, <a href="#parameter-minArea"><code>minArea</code></a>, <a href="#parameter-maxArea"><code>maxArea</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of harvest data resources under a particular farm.</td>
</tr>
<tr>
    <td><a href="#get_cascade_delete_job_details"><CopyableCode code="get_cascade_delete_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get cascade delete job for harvest data resource.</td>
</tr>
<tr>
    <td><a href="#create_cascade_delete_job"><CopyableCode code="create_cascade_delete_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-harvestDataId"><code>harvestDataId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create cascade delete job for harvest data resource.</td>
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
<tr id="parameter-harvestDataId">
    <td><CopyableCode code="harvestDataId" /></td>
    <td><code>string</code></td>
    <td>Id of the harvest data. Required.</td>
</tr>
<tr id="parameter-harvest_data_id">
    <td><CopyableCode code="harvest_data_id" /></td>
    <td><code>string</code></td>
    <td>ID of the harvest data resource. Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Job Id supplied by end user. Required.</td>
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
<tr id="parameter-maxAvgMoisture">
    <td><CopyableCode code="maxAvgMoisture" /></td>
    <td><code>number</code></td>
    <td>Maximum AvgMoisture value (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxAvgSpeed">
    <td><CopyableCode code="maxAvgSpeed" /></td>
    <td><code>number</code></td>
    <td>Maximum AvgSpeed value (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxAvgWetMass">
    <td><CopyableCode code="maxAvgWetMass" /></td>
    <td><code>number</code></td>
    <td>Maximum AvgWetMass value (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxAvgYield">
    <td><CopyableCode code="maxAvgYield" /></td>
    <td><code>number</code></td>
    <td>Maximum AvgYield value (inclusive). Default value is None.</td>
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
<tr id="parameter-maxTotalWetMass">
    <td><CopyableCode code="maxTotalWetMass" /></td>
    <td><code>number</code></td>
    <td>Maximum Total WetMass value (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxTotalYield">
    <td><CopyableCode code="maxTotalYield" /></td>
    <td><code>number</code></td>
    <td>Maximum Yield value (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minArea">
    <td><CopyableCode code="minArea" /></td>
    <td><code>number</code></td>
    <td>Minimum area for which operation was applied (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minAvgMoisture">
    <td><CopyableCode code="minAvgMoisture" /></td>
    <td><code>number</code></td>
    <td>Minimum AvgMoisture value(inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minAvgSpeed">
    <td><CopyableCode code="minAvgSpeed" /></td>
    <td><code>number</code></td>
    <td>Minimum AvgSpeed value(inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minAvgWetMass">
    <td><CopyableCode code="minAvgWetMass" /></td>
    <td><code>number</code></td>
    <td>Minimum AvgWetMass value(inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minAvgYield">
    <td><CopyableCode code="minAvgYield" /></td>
    <td><code>number</code></td>
    <td>Minimum AvgYield value(inclusive). Default value is None.</td>
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
<tr id="parameter-minTotalWetMass">
    <td><CopyableCode code="minTotalWetMass" /></td>
    <td><code>number</code></td>
    <td>Minimum Total WetMass value(inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minTotalYield">
    <td><CopyableCode code="minTotalYield" /></td>
    <td><code>number</code></td>
    <td>Minimum Yield value(inclusive). Default value is None.</td>
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

Creates or updates harvest data resource under a particular party.

```sql
INSERT INTO azure_extras.agrifood_farming.harvest_data (
party_id,
harvest_data_id,
endpoint
)
SELECT 
'{{ party_id }}',
'{{ harvest_data_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: harvest_data
  props:
    - name: party_id
      value: "{{ party_id }}"
      description: Required parameter for the harvest_data resource.
    - name: harvest_data_id
      value: "{{ harvest_data_id }}"
      description: Required parameter for the harvest_data resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the harvest_data resource.
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

Creates or updates harvest data resource under a particular party.

```sql
REPLACE azure_extras.agrifood_farming.harvest_data
SET 
-- No updatable properties
WHERE 
party_id = '{{ party_id }}' --required
AND harvest_data_id = '{{ harvest_data_id }}' --required
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

Deletes a specified harvest data resource under a particular party.

```sql
DELETE FROM azure_extras.agrifood_farming.harvest_data
WHERE party_id = '{{ party_id }}' --required
AND harvest_data_id = '{{ harvest_data_id }}' --required
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
        { label: 'get_cascade_delete_job_details', value: 'get_cascade_delete_job_details' },
        { label: 'create_cascade_delete_job', value: 'create_cascade_delete_job' }
    ]}
>
<TabItem value="get_raw">

Get a specified harvest data resource under a particular party.

```sql
EXEC azure_extras.agrifood_farming.harvest_data.get_raw 
@party_id='{{ party_id }}' --required, 
@harvest_data_id='{{ harvest_data_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Returns a paginated list of harvest data resources across all parties.

```sql
EXEC azure_extras.agrifood_farming.harvest_data.list_raw 
@endpoint='{{ endpoint }}' --required, 
@minTotalYield='{{ minTotalYield }}', 
@maxTotalYield='{{ maxTotalYield }}', 
@minAvgYield='{{ minAvgYield }}', 
@maxAvgYield='{{ maxAvgYield }}', 
@minTotalWetMass='{{ minTotalWetMass }}', 
@maxTotalWetMass='{{ maxTotalWetMass }}', 
@minAvgWetMass='{{ minAvgWetMass }}', 
@maxAvgWetMass='{{ maxAvgWetMass }}', 
@minAvgMoisture='{{ minAvgMoisture }}', 
@maxAvgMoisture='{{ maxAvgMoisture }}', 
@minAvgSpeed='{{ minAvgSpeed }}', 
@maxAvgSpeed='{{ maxAvgSpeed }}', 
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

Returns a paginated list of harvest data resources under a particular farm.

```sql
EXEC azure_extras.agrifood_farming.harvest_data.list_by_party_id 
@party_id='{{ party_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minTotalYield='{{ minTotalYield }}', 
@maxTotalYield='{{ maxTotalYield }}', 
@minAvgYield='{{ minAvgYield }}', 
@maxAvgYield='{{ maxAvgYield }}', 
@minTotalWetMass='{{ minTotalWetMass }}', 
@maxTotalWetMass='{{ maxTotalWetMass }}', 
@minAvgWetMass='{{ minAvgWetMass }}', 
@maxAvgWetMass='{{ maxAvgWetMass }}', 
@minAvgMoisture='{{ minAvgMoisture }}', 
@maxAvgMoisture='{{ maxAvgMoisture }}', 
@minAvgSpeed='{{ minAvgSpeed }}', 
@maxAvgSpeed='{{ maxAvgSpeed }}', 
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

Get cascade delete job for harvest data resource.

```sql
EXEC azure_extras.agrifood_farming.harvest_data.get_cascade_delete_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_cascade_delete_job">

Create cascade delete job for harvest data resource.

```sql
EXEC azure_extras.agrifood_farming.harvest_data.create_cascade_delete_job 
@job_id='{{ job_id }}' --required, 
@partyId='{{ partyId }}' --required, 
@harvestDataId='{{ harvestDataId }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
