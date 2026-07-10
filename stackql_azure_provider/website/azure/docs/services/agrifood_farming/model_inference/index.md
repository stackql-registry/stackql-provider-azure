--- 
title: model_inference
hide_title: false
hide_table_of_contents: false
keywords:
  - model_inference
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

Creates, updates, deletes, gets or lists a <code>model_inference</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="model_inference" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.model_inference" /></td></tr>
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
    <td><a href="#get_biomass_model_job"><CopyableCode code="get_biomass_model_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Biomass Model job's details.</td>
</tr>
<tr>
    <td><a href="#create_biomass_model_job"><CopyableCode code="create_biomass_model_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a Biomass Model job.</td>
</tr>
<tr>
    <td><a href="#get_sensor_placement_model_job"><CopyableCode code="get_sensor_placement_model_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get Sensor Placement Model job's details.</td>
</tr>
<tr>
    <td><a href="#create_sensor_placement_model_job"><CopyableCode code="create_sensor_placement_model_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a Sensor Placement Model job.</td>
</tr>
<tr>
    <td><a href="#get_soil_moisture_model_job"><CopyableCode code="get_soil_moisture_model_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get SoilMoisture Model job's details.</td>
</tr>
<tr>
    <td><a href="#create_soil_moisture_model_job"><CopyableCode code="create_soil_moisture_model_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a SoilMoisture Model job.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>JobId provided by user. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_biomass_model_job"
    values={[
        { label: 'get_biomass_model_job', value: 'get_biomass_model_job' },
        { label: 'create_biomass_model_job', value: 'create_biomass_model_job' },
        { label: 'get_sensor_placement_model_job', value: 'get_sensor_placement_model_job' },
        { label: 'create_sensor_placement_model_job', value: 'create_sensor_placement_model_job' },
        { label: 'get_soil_moisture_model_job', value: 'get_soil_moisture_model_job' },
        { label: 'create_soil_moisture_model_job', value: 'create_soil_moisture_model_job' }
    ]}
>
<TabItem value="get_biomass_model_job">

Get Biomass Model job's details.

```sql
EXEC azure.agrifood_farming.model_inference.get_biomass_model_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_biomass_model_job">

Create a Biomass Model job.

```sql
EXEC azure.agrifood_farming.model_inference.create_biomass_model_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_sensor_placement_model_job">

Get Sensor Placement Model job's details.

```sql
EXEC azure.agrifood_farming.model_inference.get_sensor_placement_model_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_sensor_placement_model_job">

Create a Sensor Placement Model job.

```sql
EXEC azure.agrifood_farming.model_inference.create_sensor_placement_model_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_soil_moisture_model_job">

Get SoilMoisture Model job's details.

```sql
EXEC azure.agrifood_farming.model_inference.get_soil_moisture_model_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_soil_moisture_model_job">

Create a SoilMoisture Model job.

```sql
EXEC azure.agrifood_farming.model_inference.create_soil_moisture_model_job 
@job_id='{{ job_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
