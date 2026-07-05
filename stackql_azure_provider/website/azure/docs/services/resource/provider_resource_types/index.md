--- 
title: provider_resource_types
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_resource_types
  - resource
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

Creates, updates, deletes, gets or lists a <code>provider_resource_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_resource_types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.provider_resource_types" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="aliases" /></td>
    <td><code>array</code></td>
    <td>The aliases that are supported by this resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="apiProfiles" /></td>
    <td><code>array</code></td>
    <td>The API profiles for the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="apiVersions" /></td>
    <td><code>array</code></td>
    <td>The API version.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>string</code></td>
    <td>The additional capabilities offered by this resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultApiVersion" /></td>
    <td><code>string</code></td>
    <td>The default API version.</td>
</tr>
<tr>
    <td><CopyableCode code="locationMappings" /></td>
    <td><code>array</code></td>
    <td>The location mappings that are supported by this resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="locations" /></td>
    <td><code>array</code></td>
    <td>The collection of locations where this resource type can be created.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The properties.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneMappings" /></td>
    <td><code>array</code></td>
    <td>:vartype zone_mappings: list[~azure.mgmt.resource.resources.models.ZoneMapping]</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List the resource types for a specified resource provider.</td>
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
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace of the resource provider. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The $expand query parameter. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List the resource types for a specified resource provider.

```sql
SELECT
aliases,
apiProfiles,
apiVersions,
capabilities,
defaultApiVersion,
locationMappings,
locations,
properties,
resourceType,
zoneMappings
FROM azure.resource.provider_resource_types
WHERE resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
