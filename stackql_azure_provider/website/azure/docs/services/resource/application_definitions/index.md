--- 
title: application_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_definitions
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

Creates, updates, deletes, gets or lists an <code>application_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.application_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The managed application provider authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="createUiDefinition" /></td>
    <td><code>object</code></td>
    <td>The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application deployment policy.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The managed application definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The managed application definition display name.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether the package is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="lockLevel" /></td>
    <td><code>string</code></td>
    <td>The managed application lock level. Required. Known values are: "CanNotDelete", "ReadOnly", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="lockingPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application locking policy.</td>
</tr>
<tr>
    <td><CopyableCode code="mainTemplate" /></td>
    <td><code>object</code></td>
    <td>The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ID of the resource that manages this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managementPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application management policy that determines publisher's access to the managed resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application notification policy.</td>
</tr>
<tr>
    <td><CopyableCode code="packageFileUri" /></td>
    <td><code>string</code></td>
    <td>The managed application definition package file Uri. Use this element.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>The managed application provider policies.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The managed application provider authorizations.</td>
</tr>
<tr>
    <td><CopyableCode code="createUiDefinition" /></td>
    <td><code>object</code></td>
    <td>The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application deployment policy.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The managed application definition description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The managed application definition display name.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether the package is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="lockLevel" /></td>
    <td><code>string</code></td>
    <td>The managed application lock level. Required. Known values are: "CanNotDelete", "ReadOnly", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="lockingPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application locking policy.</td>
</tr>
<tr>
    <td><CopyableCode code="mainTemplate" /></td>
    <td><code>object</code></td>
    <td>The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ID of the resource that manages this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managementPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application management policy that determines publisher's access to the managed resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application notification policy.</td>
</tr>
<tr>
    <td><CopyableCode code="packageFileUri" /></td>
    <td><code>string</code></td>
    <td>The managed application definition package file Uri. Use this element.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>The managed application provider policies.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_definition_name"><code>application_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the managed application definition.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the managed application definitions in a resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_definition_name"><code>application_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new managed application definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_definition_name"><code>application_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new managed application definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_definition_name"><code>application_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the managed application definition.</td>
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
<tr id="parameter-application_definition_name">
    <td><CopyableCode code="application_definition_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed application definition to delete. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' }
    ]}
>
<TabItem value="get">

Gets the managed application definition.

```sql
SELECT
id,
name,
artifacts,
authorizations,
createUiDefinition,
deploymentPolicy,
description,
displayName,
isEnabled,
location,
lockLevel,
lockingPolicy,
mainTemplate,
managedBy,
managementPolicy,
notificationPolicy,
packageFileUri,
policies,
sku,
tags,
type
FROM azure.resource.application_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND application_definition_name = '{{ application_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the managed application definitions in a resource group.

```sql
SELECT
id,
name,
artifacts,
authorizations,
createUiDefinition,
deploymentPolicy,
description,
displayName,
isEnabled,
location,
lockLevel,
lockingPolicy,
mainTemplate,
managedBy,
managementPolicy,
notificationPolicy,
packageFileUri,
policies,
sku,
tags,
type
FROM azure.resource.application_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
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

Creates a new managed application definition.

```sql
INSERT INTO azure.resource.application_definitions (
location,
tags,
managedBy,
sku,
properties,
resource_group_name,
application_definition_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ managedBy }}',
'{{ sku }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ application_definition_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
managedBy,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: application_definitions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the application_definitions resource.
    - name: application_definition_name
      value: "{{ application_definition_name }}"
      description: Required parameter for the application_definitions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the application_definitions resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        ID of the resource that manages this resource.
    - name: sku
      description: |
        The SKU of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        model: "{{ model }}"
        capacity: {{ capacity }}
    - name: properties
      value:
        lockLevel: "{{ lockLevel }}"
        displayName: "{{ displayName }}"
        isEnabled: {{ isEnabled }}
        authorizations:
          - principalId: "{{ principalId }}"
            roleDefinitionId: "{{ roleDefinitionId }}"
        artifacts:
          - name: "{{ name }}"
            uri: "{{ uri }}"
            type: "{{ type }}"
        description: "{{ description }}"
        packageFileUri: "{{ packageFileUri }}"
        mainTemplate: "{{ mainTemplate }}"
        createUiDefinition: "{{ createUiDefinition }}"
        notificationPolicy:
          notificationEndpoints:
            - uri: "{{ uri }}"
        lockingPolicy:
          allowedActions:
            - "{{ allowedActions }}"
          allowedDataActions:
            - "{{ allowedDataActions }}"
        deploymentPolicy:
          deploymentMode: "{{ deploymentMode }}"
        managementPolicy:
          mode: "{{ mode }}"
        policies:
          - name: "{{ name }}"
            policyDefinitionId: "{{ policyDefinitionId }}"
            parameters: "{{ parameters }}"
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

Creates a new managed application definition.

```sql
REPLACE azure.resource.application_definitions
SET 
location = '{{ location }}',
tags = '{{ tags }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_definition_name = '{{ application_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
location,
managedBy,
properties,
sku,
tags,
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

Deletes the managed application definition.

```sql
DELETE FROM azure.resource.application_definitions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND application_definition_name = '{{ application_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
