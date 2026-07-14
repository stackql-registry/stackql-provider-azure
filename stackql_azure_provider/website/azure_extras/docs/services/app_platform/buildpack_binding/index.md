--- 
title: buildpack_binding
hide_title: false
hide_table_of_contents: false
keywords:
  - buildpack_binding
  - app_platform
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

Creates, updates, deletes, gets or lists a <code>buildpack_binding</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="buildpack_binding" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_platform.buildpack_binding" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_for_cluster', value: 'list_for_cluster' }
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingType" /></td>
    <td><code>string</code></td>
    <td>Buildpack Binding Type. Known values are: "ApplicationInsights", "ApacheSkyWalking", "AppDynamics", "Dynatrace", "NewRelic", and "ElasticAPM".</td>
</tr>
<tr>
    <td><CopyableCode code="launchProperties" /></td>
    <td><code>object</code></td>
    <td>The object describes the buildpack binding launch properties.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Buildpack Binding. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingType" /></td>
    <td><code>string</code></td>
    <td>Buildpack Binding Type. Known values are: "ApplicationInsights", "ApacheSkyWalking", "AppDynamics", "Dynatrace", "NewRelic", and "ElasticAPM".</td>
</tr>
<tr>
    <td><CopyableCode code="launchProperties" /></td>
    <td><code>object</code></td>
    <td>The object describes the buildpack binding launch properties.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Buildpack Binding. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_cluster">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingType" /></td>
    <td><code>string</code></td>
    <td>Buildpack Binding Type. Known values are: "ApplicationInsights", "ApacheSkyWalking", "AppDynamics", "Dynatrace", "NewRelic", and "ElasticAPM".</td>
</tr>
<tr>
    <td><CopyableCode code="launchProperties" /></td>
    <td><code>object</code></td>
    <td>The object describes the buildpack binding launch properties.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the Buildpack Binding. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-builder_name"><code>builder_name</code></a>, <a href="#parameter-buildpack_binding_name"><code>buildpack_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a buildpack binding by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-builder_name"><code>builder_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all buildpack bindings in a builder.</td>
</tr>
<tr>
    <td><a href="#list_for_cluster"><CopyableCode code="list_for_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get collection of buildpack bindings under all builders.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-builder_name"><code>builder_name</code></a>, <a href="#parameter-buildpack_binding_name"><code>buildpack_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a buildpack binding.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-builder_name"><code>builder_name</code></a>, <a href="#parameter-buildpack_binding_name"><code>buildpack_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a buildpack binding.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-builder_name"><code>builder_name</code></a>, <a href="#parameter-buildpack_binding_name"><code>buildpack_binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to delete a Buildpack Binding.</td>
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
<tr id="parameter-build_service_name">
    <td><CopyableCode code="build_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the build service resource. Required.</td>
</tr>
<tr id="parameter-builder_name">
    <td><CopyableCode code="builder_name" /></td>
    <td><code>string</code></td>
    <td>The name of the builder resource. Required.</td>
</tr>
<tr id="parameter-buildpack_binding_name">
    <td><CopyableCode code="buildpack_binding_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Buildpack Binding Name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Service resource. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_for_cluster', value: 'list_for_cluster' }
    ]}
>
<TabItem value="get">

Get a buildpack binding by name.

```sql
SELECT
id,
name,
bindingType,
launchProperties,
provisioningState,
systemData,
type
FROM azure_extras.app_platform.buildpack_binding
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND builder_name = '{{ builder_name }}' -- required
AND buildpack_binding_name = '{{ buildpack_binding_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handles requests to list all buildpack bindings in a builder.

```sql
SELECT
id,
name,
bindingType,
launchProperties,
provisioningState,
systemData,
type
FROM azure_extras.app_platform.buildpack_binding
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND builder_name = '{{ builder_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_cluster">

Get collection of buildpack bindings under all builders.

```sql
SELECT
id,
name,
bindingType,
launchProperties,
provisioningState,
systemData,
type
FROM azure_extras.app_platform.buildpack_binding
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
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

Create or update a buildpack binding.

```sql
INSERT INTO azure_extras.app_platform.buildpack_binding (
properties,
resource_group_name,
service_name,
build_service_name,
builder_name,
buildpack_binding_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ build_service_name }}',
'{{ builder_name }}',
'{{ buildpack_binding_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: buildpack_binding
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the buildpack_binding resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the buildpack_binding resource.
    - name: build_service_name
      value: "{{ build_service_name }}"
      description: Required parameter for the buildpack_binding resource.
    - name: builder_name
      value: "{{ builder_name }}"
      description: Required parameter for the buildpack_binding resource.
    - name: buildpack_binding_name
      value: "{{ buildpack_binding_name }}"
      description: Required parameter for the buildpack_binding resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the buildpack_binding resource.
    - name: properties
      description: |
        Properties of a buildpack binding.
      value:
        bindingType: "{{ bindingType }}"
        provisioningState: "{{ provisioningState }}"
        launchProperties:
          properties: "{{ properties }}"
          secrets: "{{ secrets }}"
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

Create or update a buildpack binding.

```sql
REPLACE azure_extras.app_platform.buildpack_binding
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND build_service_name = '{{ build_service_name }}' --required
AND builder_name = '{{ builder_name }}' --required
AND buildpack_binding_name = '{{ buildpack_binding_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Operation to delete a Buildpack Binding.

```sql
DELETE FROM azure_extras.app_platform.buildpack_binding
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND build_service_name = '{{ build_service_name }}' --required
AND builder_name = '{{ builder_name }}' --required
AND buildpack_binding_name = '{{ buildpack_binding_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
