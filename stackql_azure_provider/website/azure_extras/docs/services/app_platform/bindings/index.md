--- 
title: bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - bindings
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

Creates, updates, deletes, gets or lists a <code>bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bindings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_platform.bindings" /></td></tr>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingParameters" /></td>
    <td><code>object</code></td>
    <td>Binding parameters of the Binding resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td>Creation time of the Binding resource.</td>
</tr>
<tr>
    <td><CopyableCode code="generatedProperties" /></td>
    <td><code>string</code></td>
    <td>The generated Spring Boot property file for this binding. The secret will be deducted.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The key of the bound resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource id of the bound resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>The name of the bound resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The standard Azure resource type of the bound resource.</td>
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
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string</code></td>
    <td>Update time of the Binding resource.</td>
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
    <td><CopyableCode code="bindingParameters" /></td>
    <td><code>object</code></td>
    <td>Binding parameters of the Binding resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td>Creation time of the Binding resource.</td>
</tr>
<tr>
    <td><CopyableCode code="generatedProperties" /></td>
    <td><code>string</code></td>
    <td>The generated Spring Boot property file for this binding. The secret will be deducted.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The key of the bound resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure resource id of the bound resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>The name of the bound resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>The standard Azure resource type of the bound resource.</td>
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
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string</code></td>
    <td>Update time of the Binding resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-binding_name"><code>binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Binding and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in an App.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-binding_name"><code>binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Binding or update an exiting Binding.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-binding_name"><code>binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to update an exiting Binding.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-binding_name"><code>binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Binding or update an exiting Binding.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-binding_name"><code>binding_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to delete a Binding.</td>
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
<tr id="parameter-app_name">
    <td><CopyableCode code="app_name" /></td>
    <td><code>string</code></td>
    <td>The name of the App resource. Required.</td>
</tr>
<tr id="parameter-binding_name">
    <td><CopyableCode code="binding_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Binding resource. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a Binding and its properties.

```sql
SELECT
id,
name,
bindingParameters,
createdAt,
generatedProperties,
key,
resourceId,
resourceName,
resourceType,
systemData,
type,
updatedAt
FROM azure_extras.app_platform.bindings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND app_name = '{{ app_name }}' -- required
AND binding_name = '{{ binding_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handles requests to list all resources in an App.

```sql
SELECT
id,
name,
bindingParameters,
createdAt,
generatedProperties,
key,
resourceId,
resourceName,
resourceType,
systemData,
type,
updatedAt
FROM azure_extras.app_platform.bindings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND app_name = '{{ app_name }}' -- required
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

Create a new Binding or update an exiting Binding.

```sql
INSERT INTO azure_extras.app_platform.bindings (
properties,
resource_group_name,
service_name,
app_name,
binding_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ app_name }}',
'{{ binding_name }}',
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
- name: bindings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bindings resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the bindings resource.
    - name: app_name
      value: "{{ app_name }}"
      description: Required parameter for the bindings resource.
    - name: binding_name
      value: "{{ binding_name }}"
      description: Required parameter for the bindings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bindings resource.
    - name: properties
      description: |
        Properties of the Binding resource.
      value:
        resourceName: "{{ resourceName }}"
        resourceType: "{{ resourceType }}"
        resourceId: "{{ resourceId }}"
        key: "{{ key }}"
        bindingParameters: "{{ bindingParameters }}"
        generatedProperties: "{{ generatedProperties }}"
        createdAt: "{{ createdAt }}"
        updatedAt: "{{ updatedAt }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Operation to update an exiting Binding.

```sql
UPDATE azure_extras.app_platform.bindings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND binding_name = '{{ binding_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create a new Binding or update an exiting Binding.

```sql
REPLACE azure_extras.app_platform.bindings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND binding_name = '{{ binding_name }}' --required
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

Operation to delete a Binding.

```sql
DELETE FROM azure_extras.app_platform.bindings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND binding_name = '{{ binding_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
