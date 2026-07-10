--- 
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - containerregistrytasks
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

Creates, updates, deletes, gets or lists a <code>registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerregistrytasks.registries" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_build_source_upload_url"
    values={[
        { label: 'get_build_source_upload_url', value: 'get_build_source_upload_url' }
    ]}
>
<TabItem value="get_build_source_upload_url">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="relativePath" /></td>
    <td><code>string</code></td>
    <td>The relative path to the source. This is used to submit the subsequent queue build request.</td>
</tr>
<tr>
    <td><CopyableCode code="uploadUrl" /></td>
    <td><code>string</code></td>
    <td>The URL where the client can upload the source.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

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
    <td><a href="#get_build_source_upload_url"><CopyableCode code="get_build_source_upload_url" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the upload location for the user to be able to upload the source.</td>
</tr>
<tr>
    <td><a href="#schedule_run"><CopyableCode code="schedule_run" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-registry_name"><code>registry_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Schedules a new run based on the request parameters and add it to the run queue.</td>
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
<tr id="parameter-registry_name">
    <td><CopyableCode code="registry_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container registry. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_build_source_upload_url"
    values={[
        { label: 'get_build_source_upload_url', value: 'get_build_source_upload_url' }
    ]}
>
<TabItem value="get_build_source_upload_url">

Get the upload location for the user to be able to upload the source.

```sql
SELECT
relativePath,
uploadUrl
FROM azure.containerregistrytasks.registries
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND registry_name = '{{ registry_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="schedule_run"
    values={[
        { label: 'schedule_run', value: 'schedule_run' }
    ]}
>
<TabItem value="schedule_run">

Schedules a new run based on the request parameters and add it to the run queue.

```sql
EXEC azure.containerregistrytasks.registries.schedule_run 
@resource_group_name='{{ resource_group_name }}' --required, 
@registry_name='{{ registry_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"type": "{{ type }}", 
"isArchiveEnabled": {{ isArchiveEnabled }}, 
"agentPoolName": "{{ agentPoolName }}", 
"logTemplate": "{{ logTemplate }}"
}'
;
```
</TabItem>
</Tabs>
