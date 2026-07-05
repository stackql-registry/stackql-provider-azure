--- 
title: insight_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - insight_attachments
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

Creates, updates, deletes, gets or lists an <code>insight_attachments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="insight_attachments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.agrifood_farming.insight_attachments" /></td></tr>
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
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_attachment_id"><code>insight_attachment_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a specified insight resource.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_attachment_id"><code>insight_attachment_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a specified insight resource under a particular party.</td>
</tr>
<tr>
    <td><a href="#list_by_party_id_model_id_and_resource"><CopyableCode code="list_by_party_id_model_id_and_resource" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Returns a paginated list of insight resources.</td>
</tr>
<tr>
    <td><a href="#download"><CopyableCode code="download" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-party_id"><code>party_id</code></a>, <a href="#parameter-model_id"><code>model_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-insight_attachment_id"><code>insight_attachment_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Downloads and returns insight-attachment as response for the given input filePath.</td>
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
<tr id="parameter-insight_attachment_id">
    <td><CopyableCode code="insight_attachment_id" /></td>
    <td><code>string</code></td>
    <td>Id of the insight attachment resource. Required.</td>
</tr>
<tr id="parameter-model_id">
    <td><CopyableCode code="model_id" /></td>
    <td><code>string</code></td>
    <td>Id of the associated model. It can be either 'BiomassModelId', 'SensorPlacementModelId', 'SoilMoistureModelId' or any solution id. Required.</td>
</tr>
<tr id="parameter-party_id">
    <td><CopyableCode code="party_id" /></td>
    <td><code>string</code></td>
    <td>Id of the associated party. Required.</td>
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
DELETE FROM azure.agrifood_farming.insight_attachments
WHERE party_id = '{{ party_id }}' --required
AND model_id = '{{ model_id }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_id = '{{ resource_id }}' --required
AND insight_attachment_id = '{{ insight_attachment_id }}' --required
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
        { label: 'download', value: 'download' }
    ]}
>
<TabItem value="get_raw">

Gets a specified insight resource under a particular party.

```sql
EXEC azure.agrifood_farming.insight_attachments.get_raw 
@party_id='{{ party_id }}' --required, 
@model_id='{{ model_id }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_id='{{ resource_id }}' --required, 
@insight_attachment_id='{{ insight_attachment_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_by_party_id_model_id_and_resource">

Returns a paginated list of insight resources.

```sql
EXEC azure.agrifood_farming.insight_attachments.list_by_party_id_model_id_and_resource 
@party_id='{{ party_id }}' --required, 
@model_id='{{ model_id }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_id='{{ resource_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="download">

Downloads and returns insight-attachment as response for the given input filePath.

```sql
EXEC azure.agrifood_farming.insight_attachments.download 
@party_id='{{ party_id }}' --required, 
@model_id='{{ model_id }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_id='{{ resource_id }}' --required, 
@insight_attachment_id='{{ insight_attachment_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
