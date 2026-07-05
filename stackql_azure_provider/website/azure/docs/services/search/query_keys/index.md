--- 
title: query_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - query_keys
  - search
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

Creates, updates, deletes, gets or lists a <code>query_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="query_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.query_keys" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates a new query key for the specified search service. You can create up to 50 query keys per service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified query key. Unlike admin keys, query keys are not regenerated. The process for regenerating a query key is to delete and then recreate it. Returns 200 (OK) on successful deletion, 204 (No Content) if the service exists but the query keys not found, or 404 (Not Found) if the service is not found. NOTE: The behavior of returning 404 is inconsistent with ARM guidelines. Clients should expect a 204 response in future versions and avoid new dependencies on the 404 response.</td>
</tr>
<tr>
    <td><a href="#list_by_search_service"><CopyableCode code="list_by_search_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the list of query API keys for the given Azure AI Search service.</td>
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
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The query key to be deleted. Query keys are identified by value, not by name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the new query API key. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure AI Search service associated with the specified resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Generates a new query key for the specified search service. You can create up to 50 query keys per service.

```sql
INSERT INTO azure.search.query_keys (
resource_group_name,
search_service_name,
name,
subscription_id
)
SELECT 
'{{ resource_group_name }}',
'{{ search_service_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
name,
key
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: query_keys
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the query_keys resource.
    - name: search_service_name
      value: "{{ search_service_name }}"
      description: Required parameter for the query_keys resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the query_keys resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the query_keys resource.
`}</CodeBlock>

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

Deletes the specified query key. Unlike admin keys, query keys are not regenerated. The process for regenerating a query key is to delete and then recreate it. Returns 200 (OK) on successful deletion, 204 (No Content) if the service exists but the query keys not found, or 404 (Not Found) if the service is not found. NOTE: The behavior of returning 404 is inconsistent with ARM guidelines. Clients should expect a 204 response in future versions and avoid new dependencies on the 404 response.

```sql
DELETE FROM azure.search.query_keys
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND search_service_name = '{{ search_service_name }}' --required
AND key = '{{ key }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_by_search_service"
    values={[
        { label: 'list_by_search_service', value: 'list_by_search_service' }
    ]}
>
<TabItem value="list_by_search_service">

Returns the list of query API keys for the given Azure AI Search service.

```sql
EXEC azure.search.query_keys.list_by_search_service 
@resource_group_name='{{ resource_group_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
