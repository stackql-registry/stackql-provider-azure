--- 
title: open_ai
hide_title: false
hide_table_of_contents: false
keywords:
  - open_ai
  - elastic
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>open_ai</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="open_ai" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.open_ai" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the integration.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the integration.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>Value of API key for Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRefreshAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Update Timestamp for key updation.</td>
</tr>
<tr>
    <td><CopyableCode code="openAIConnectorId" /></td>
    <td><code>string</code></td>
    <td>The connector id of Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="openAIResourceEndpoint" /></td>
    <td><code>string</code></td>
    <td>The API endpoint for Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="openAIResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource name of Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the integration.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the integration.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the integration.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>Value of API key for Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRefreshAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Update Timestamp for key updation.</td>
</tr>
<tr>
    <td><CopyableCode code="openAIConnectorId" /></td>
    <td><code>string</code></td>
    <td>The connector id of Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="openAIResourceEndpoint" /></td>
    <td><code>string</code></td>
    <td>The API endpoint for Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="openAIResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource name of Open AI resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the integration.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-integration_name"><code>integration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get detailed information about OpenAI integration rules for a given Elastic monitor resource. Get detailed information about OpenAI integration rules for a given Elastic monitor resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all OpenAI integration rules for a given Elastic monitor resource, helping you manage AI-driven observability and monitoring. List all OpenAI integration rules for a given Elastic monitor resource, helping you manage AI-driven observability and monitoring.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-integration_name"><code>integration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring. Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-integration_name"><code>integration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring. Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-integration_name"><code>integration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an OpenAI integration rule for a given Elastic monitor resource, removing AI-driven observability and monitoring capabilities. Delete an OpenAI integration rule for a given Elastic monitor resource, removing AI-driven observability and monitoring capabilities.</td>
</tr>
<tr>
    <td><a href="#get_status"><CopyableCode code="get_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-integration_name"><code>integration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of OpenAI integration for a given Elastic monitor resource, ensuring optimal observability and performance. Get the status of OpenAI integration for a given Elastic monitor resource, ensuring optimal observability and performance.</td>
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
<tr id="parameter-integration_name">
    <td><CopyableCode code="integration_name" /></td>
    <td><code>string</code></td>
    <td>OpenAI Integration name. Required.</td>
</tr>
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get detailed information about OpenAI integration rules for a given Elastic monitor resource. Get detailed information about OpenAI integration rules for a given Elastic monitor resource.

```sql
SELECT
id,
name,
key,
lastRefreshAt,
openAIConnectorId,
openAIResourceEndpoint,
openAIResourceId,
type
FROM azure_isv.elastic.open_ai
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND integration_name = '{{ integration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all OpenAI integration rules for a given Elastic monitor resource, helping you manage AI-driven observability and monitoring. List all OpenAI integration rules for a given Elastic monitor resource, helping you manage AI-driven observability and monitoring.

```sql
SELECT
id,
name,
key,
lastRefreshAt,
openAIConnectorId,
openAIResourceEndpoint,
openAIResourceId,
type
FROM azure_isv.elastic.open_ai
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring. Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring.

```sql
INSERT INTO azure_isv.elastic.open_ai (
properties,
resource_group_name,
monitor_name,
integration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
'{{ integration_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: open_ai
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the open_ai resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the open_ai resource.
    - name: integration_name
      value: "{{ integration_name }}"
      description: Required parameter for the open_ai resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the open_ai resource.
    - name: properties
      description: |
        Open AI Integration details.
      value:
        openAIResourceId: "{{ openAIResourceId }}"
        openAIResourceEndpoint: "{{ openAIResourceEndpoint }}"
        openAIConnectorId: "{{ openAIConnectorId }}"
        key: "{{ key }}"
        lastRefreshAt: "{{ lastRefreshAt }}"
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

Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring. Create or update an OpenAI integration rule for a given Elastic monitor resource, enabling advanced AI-driven observability and monitoring.

```sql
REPLACE azure_isv.elastic.open_ai
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND integration_name = '{{ integration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
type;
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

Delete an OpenAI integration rule for a given Elastic monitor resource, removing AI-driven observability and monitoring capabilities. Delete an OpenAI integration rule for a given Elastic monitor resource, removing AI-driven observability and monitoring capabilities.

```sql
DELETE FROM azure_isv.elastic.open_ai
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND integration_name = '{{ integration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_status"
    values={[
        { label: 'get_status', value: 'get_status' }
    ]}
>
<TabItem value="get_status">

Get the status of OpenAI integration for a given Elastic monitor resource, ensuring optimal observability and performance. Get the status of OpenAI integration for a given Elastic monitor resource, ensuring optimal observability and performance.

```sql
EXEC azure_isv.elastic.open_ai.get_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@integration_name='{{ integration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
