--- 
title: rules_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - rules_engines
  - frontdoor
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

Creates, updates, deletes, gets or lists a <code>rules_engines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rules_engines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.frontdoor.rules_engines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_front_door', value: 'list_by_front_door' }
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
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>A list of rules that define a particular Rules Engine Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_front_door">

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
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>A list of rules that define a particular Rules Engine Configuration.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-rules_engine_name"><code>rules_engine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Rules Engine Configuration with the specified name within the specified Front Door.</td>
</tr>
<tr>
    <td><a href="#list_by_front_door"><CopyableCode code="list_by_front_door" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Rules Engine Configurations within a Front Door.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-rules_engine_name"><code>rules_engine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Rules Engine Configuration with the specified name within the specified Front Door.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-rules_engine_name"><code>rules_engine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Rules Engine Configuration with the specified name within the specified Front Door.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-rules_engine_name"><code>rules_engine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Rules Engine Configuration with the specified parameters.</td>
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
<tr id="parameter-front_door_name">
    <td><CopyableCode code="front_door_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Front Door which is globally unique. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rules_engine_name">
    <td><CopyableCode code="rules_engine_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Rules Engine which is unique within the Front Door. Required.</td>
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
        { label: 'list_by_front_door', value: 'list_by_front_door' }
    ]}
>
<TabItem value="get">

Gets a Rules Engine Configuration with the specified name within the specified Front Door.

```sql
SELECT
id,
name,
resourceState,
rules,
type
FROM azure.frontdoor.rules_engines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND front_door_name = '{{ front_door_name }}' -- required
AND rules_engine_name = '{{ rules_engine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_front_door">

Lists all of the Rules Engine Configurations within a Front Door.

```sql
SELECT
id,
name,
resourceState,
rules,
type
FROM azure.frontdoor.rules_engines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND front_door_name = '{{ front_door_name }}' -- required
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

Creates a new Rules Engine Configuration with the specified name within the specified Front Door.

```sql
INSERT INTO azure.frontdoor.rules_engines (
properties,
resource_group_name,
front_door_name,
rules_engine_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ front_door_name }}',
'{{ rules_engine_name }}',
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
- name: rules_engines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the rules_engines resource.
    - name: front_door_name
      value: "{{ front_door_name }}"
      description: Required parameter for the rules_engines resource.
    - name: rules_engine_name
      value: "{{ rules_engine_name }}"
      description: Required parameter for the rules_engines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the rules_engines resource.
    - name: properties
      description: |
        Properties of the Rules Engine Configuration.
      value:
        rules:
          - name: "{{ name }}"
            priority: {{ priority }}
            action:
              requestHeaderActions:
                - headerActionType: "{{ headerActionType }}"
                  headerName: "{{ headerName }}"
                  value: "{{ value }}"
              responseHeaderActions:
                - headerActionType: "{{ headerActionType }}"
                  headerName: "{{ headerName }}"
                  value: "{{ value }}"
              routeConfigurationOverride:
                @odata:
                  type: "{{ type }}"
            matchConditions: "{{ matchConditions }}"
            matchProcessingBehavior: "{{ matchProcessingBehavior }}"
        resourceState: "{{ resourceState }}"
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

Creates a new Rules Engine Configuration with the specified name within the specified Front Door.

```sql
REPLACE azure.frontdoor.rules_engines
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND front_door_name = '{{ front_door_name }}' --required
AND rules_engine_name = '{{ rules_engine_name }}' --required
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

Deletes an existing Rules Engine Configuration with the specified parameters.

```sql
DELETE FROM azure.frontdoor.rules_engines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND front_door_name = '{{ front_door_name }}' --required
AND rules_engine_name = '{{ rules_engine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
