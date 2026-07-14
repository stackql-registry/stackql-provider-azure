--- 
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
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

Creates, updates, deletes, gets or lists an <code>insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="insights" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood_farming.insights" /></td></tr>
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
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_id"><code>insight_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates insight entity.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_id"><code>insight_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates insight entity.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_id"><code>insight_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified insight resource.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_id"><code>insight_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a specified insight resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#list_by_party_id_model_id_and_resource"><CopyableCode code="list_by_party_id_model_id_and_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minInsightStartDateTime"><code>minInsightStartDateTime</code></a>, <a href="#parameter-maxInsightStartDateTime"><code>maxInsightStartDateTime</code></a>, <a href="#parameter-minInsightEndDateTime"><code>minInsightEndDateTime</code></a>, <a href="#parameter-maxInsightEndDateTime"><code>maxInsightEndDateTime</code></a>, <a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of insight resources.</td>
</tr>
<tr>
    <td><a href="#get_cascade_delete_job_details"><CopyableCode code="get_cascade_delete_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a cascade delete job for specified insight.</td>
</tr>
<tr>
    <td><a href="#create_cascade_delete_job"><CopyableCode code="create_cascade_delete_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-partyId"><code>partyId</code></a>, <a href="#parameter-modelId"><code>modelId</code></a>, <a href="#parameter-resourceType"><code>resourceType</code></a>, <a href="#parameter-resourceId"><code>resourceId</code></a>, <a href="#parameter-insightId"><code>insightId</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a cascade delete job for insights specified partyId/modelId/resourceType/resourceId.</td>
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
<tr id="parameter-insightId">
    <td><CopyableCode code="insightId" /></td>
    <td><code>string</code></td>
    <td>Insight id. Required.</td>
</tr>
<tr id="parameter-insight_id">
    <td><CopyableCode code="insight_id" /></td>
    <td><code>string</code></td>
    <td>Id of the insight resource. Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>Job ID supplied by end user. Required.</td>
</tr>
<tr id="parameter-modelId">
    <td><CopyableCode code="modelId" /></td>
    <td><code>string</code></td>
    <td>Id of the associated model. Required.</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Id of the associated model. Required.</td>
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
<tr id="parameter-resourceId">
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Id of the associated resource. Required.</td>
</tr>
<tr id="parameter-resourceType">
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Resource Type. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Id of the associated resource. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Resource type associated with the record. Required.</td>
</tr>
<tr id="parameter-maxCreatedDateTime">
    <td><CopyableCode code="maxCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxInsightEndDateTime">
    <td><CopyableCode code="maxInsightEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum insightEndDateTime time of insight resources (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-maxInsightStartDateTime">
    <td><CopyableCode code="maxInsightStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum insightStartDateTime time of insight resources (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
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
<tr id="parameter-minInsightEndDateTime">
    <td><CopyableCode code="minInsightEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum insightEndDateTime time of insight resources (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
</tr>
<tr id="parameter-minInsightStartDateTime">
    <td><CopyableCode code="minInsightStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum insightStartDateTime time of insight resources (inclusive), sample format: yyyy-MM-ddTHH:mm:ssZ. Default value is None.</td>
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
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates insight entity.

```sql
INSERT INTO azure_extras.agrifood_farming.insights (
party_id,
model_id,
resource_type,
resource_id,
insight_id,
endpoint
)
SELECT 
'{{ party_id }}',
'{{ model_id }}',
'{{ resource_type }}',
'{{ resource_id }}',
'{{ insight_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: insights
  props:
    - name: party_id
      value: "{{ party_id }}"
      description: Required parameter for the insights resource.
    - name: model_id
      value: "{{ model_id }}"
      description: Required parameter for the insights resource.
    - name: resource_type
      value: "{{ resource_type }}"
      description: Required parameter for the insights resource.
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the insights resource.
    - name: insight_id
      value: "{{ insight_id }}"
      description: Required parameter for the insights resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the insights resource.
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

Creates or updates insight entity.

```sql
REPLACE azure_extras.agrifood_farming.insights
SET 
-- No updatable properties
WHERE 
party_id = '{{ party_id }}' --required
AND model_id = '{{ model_id }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_id = '{{ resource_id }}' --required
AND insight_id = '{{ insight_id }}' --required
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

Deletes a specified insight resource.

```sql
DELETE FROM azure_extras.agrifood_farming.insights
WHERE party_id = '{{ party_id }}' --required
AND model_id = '{{ model_id }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_id = '{{ resource_id }}' --required
AND insight_id = '{{ insight_id }}' --required
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
        { label: 'list_by_party_id_model_id_and_resource', value: 'list_by_party_id_model_id_and_resource' },
        { label: 'get_cascade_delete_job_details', value: 'get_cascade_delete_job_details' },
        { label: 'create_cascade_delete_job', value: 'create_cascade_delete_job' }
    ]}
>
<TabItem value="get_raw">

Gets a specified insight resource under a particular party.

```sql
EXEC azure_extras.agrifood_farming.insights.get_raw 
@party_id='{{ party_id }}' --required, 
@model_id='{{ model_id }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_id='{{ resource_id }}' --required, 
@insight_id='{{ insight_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_by_party_id_model_id_and_resource">

Returns a paginated list of insight resources.

```sql
EXEC azure_extras.agrifood_farming.insights.list_by_party_id_model_id_and_resource 
@party_id='{{ party_id }}' --required, 
@model_id='{{ model_id }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_id='{{ resource_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minInsightStartDateTime='{{ minInsightStartDateTime }}', 
@maxInsightStartDateTime='{{ maxInsightStartDateTime }}', 
@minInsightEndDateTime='{{ minInsightEndDateTime }}', 
@maxInsightEndDateTime='{{ maxInsightEndDateTime }}', 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="get_cascade_delete_job_details">

Get a cascade delete job for specified insight.

```sql
EXEC azure_extras.agrifood_farming.insights.get_cascade_delete_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_cascade_delete_job">

Create a cascade delete job for insights specified partyId/modelId/resourceType/resourceId.

```sql
EXEC azure_extras.agrifood_farming.insights.create_cascade_delete_job 
@job_id='{{ job_id }}' --required, 
@partyId='{{ partyId }}' --required, 
@modelId='{{ modelId }}' --required, 
@resourceType='{{ resourceType }}' --required, 
@resourceId='{{ resourceId }}' --required, 
@insightId='{{ insightId }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
