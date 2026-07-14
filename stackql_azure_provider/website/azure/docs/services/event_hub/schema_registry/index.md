--- 
title: schema_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_registry
  - event_hub
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

Creates, updates, deletes, gets or lists a <code>schema_registry</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schema_registry" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hub.schema_registry" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_namespace', value: 'list_by_namespace' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the Schema Group was created.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag value.</td>
</tr>
<tr>
    <td><CopyableCode code="groupProperties" /></td>
    <td><code>object</code></td>
    <td>dictionary object for SchemaGroup group properties.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaCompatibility" /></td>
    <td><code>string</code></td>
    <td>Known values are: "None", "Backward", and "Forward".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaType" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Unknown" and "Avro".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the Schema Group was updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_namespace">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the Schema Group was created.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag value.</td>
</tr>
<tr>
    <td><CopyableCode code="groupProperties" /></td>
    <td><code>object</code></td>
    <td>dictionary object for SchemaGroup group properties.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaCompatibility" /></td>
    <td><code>string</code></td>
    <td>Known values are: "None", "Backward", and "Forward".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaType" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Unknown" and "Avro".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedAtUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Exact time the Schema Group was updated.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-schema_group_name"><code>schema_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of an EventHub schema group.</td>
</tr>
<tr>
    <td><a href="#list_by_namespace"><CopyableCode code="list_by_namespace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all the Schema Groups in a Namespace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-schema_group_name"><code>schema_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates an EventHub schema group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-schema_group_name"><code>schema_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates an EventHub schema group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-schema_group_name"><code>schema_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an EventHub schema group.</td>
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
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The Namespace name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group within the azure subscription. Required.</td>
</tr>
<tr id="parameter-schema_group_name">
    <td><CopyableCode code="schema_group_name" /></td>
    <td><code>string</code></td>
    <td>The Schema Group name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>May be used to limit the number of results to the most recent N usageDetails. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_namespace', value: 'list_by_namespace' }
    ]}
>
<TabItem value="get">

Gets the details of an EventHub schema group.

```sql
SELECT
id,
name,
createdAtUtc,
eTag,
groupProperties,
location,
schemaCompatibility,
schemaType,
systemData,
type,
updatedAtUtc
FROM azure.event_hub.schema_registry
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND schema_group_name = '{{ schema_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_namespace">

Gets all the Schema Groups in a Namespace.

```sql
SELECT
id,
name,
createdAtUtc,
eTag,
groupProperties,
location,
schemaCompatibility,
schemaType,
systemData,
type,
updatedAtUtc
FROM azure.event_hub.schema_registry
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
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

Creates or Updates an EventHub schema group.

```sql
INSERT INTO azure.event_hub.schema_registry (
properties,
resource_group_name,
namespace_name,
schema_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ schema_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: schema_registry
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the schema_registry resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the schema_registry resource.
    - name: schema_group_name
      value: "{{ schema_group_name }}"
      description: Required parameter for the schema_registry resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the schema_registry resource.
    - name: properties
      value:
        groupProperties: "{{ groupProperties }}"
        schemaCompatibility: "{{ schemaCompatibility }}"
        schemaType: "{{ schemaType }}"
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

Creates or Updates an EventHub schema group.

```sql
REPLACE azure.event_hub.schema_registry
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND schema_group_name = '{{ schema_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
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

Deletes an EventHub schema group.

```sql
DELETE FROM azure.event_hub.schema_registry
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND schema_group_name = '{{ schema_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
