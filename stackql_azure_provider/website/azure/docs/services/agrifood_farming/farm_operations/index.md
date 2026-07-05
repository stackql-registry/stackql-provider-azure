--- 
title: farm_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - farm_operations
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

Creates, updates, deletes, gets or lists a <code>farm_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="farm_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.farm_operations" /></td></tr>
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
    <td><a href="#create_data_ingestion_job"><CopyableCode code="create_data_ingestion_job" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a farm operation data ingestion job.</td>
</tr>
<tr>
    <td><a href="#get_data_ingestion_job_details"><CopyableCode code="get_data_ingestion_job_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a farm operation data ingestion job.</td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_data_ingestion_job"
    values={[
        { label: 'create_data_ingestion_job', value: 'create_data_ingestion_job' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_data_ingestion_job">

Create a farm operation data ingestion job.

```sql
INSERT INTO azure.agrifood_farming.farm_operations (
job_id,
endpoint
)
SELECT 
'{{ job_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: farm_operations
  props:
    - name: job_id
      value: "{{ job_id }}"
      description: Required parameter for the farm_operations resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the farm_operations resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_data_ingestion_job_details"
    values={[
        { label: 'get_data_ingestion_job_details', value: 'get_data_ingestion_job_details' }
    ]}
>
<TabItem value="get_data_ingestion_job_details">

Get a farm operation data ingestion job.

```sql
EXEC azure.agrifood_farming.farm_operations.get_data_ingestion_job_details 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
