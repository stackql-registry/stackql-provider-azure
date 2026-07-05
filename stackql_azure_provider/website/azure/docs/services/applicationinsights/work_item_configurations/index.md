--- 
title: work_item_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - work_item_configurations
  - applicationinsights
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

Creates, updates, deletes, gets or lists a <code>work_item_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="work_item_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.work_item_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_item"
    values={[
        { label: 'get_item', value: 'get_item' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_item">

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
    <td><CopyableCode code="ConfigDisplayName" /></td>
    <td><code>string</code></td>
    <td>Configuration friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="ConfigProperties" /></td>
    <td><code>string</code></td>
    <td>Serialized JSON object for detailed properties.</td>
</tr>
<tr>
    <td><CopyableCode code="ConnectorId" /></td>
    <td><code>string</code></td>
    <td>Connector identifier where work item is created.</td>
</tr>
<tr>
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td>Unique Id for work item.</td>
</tr>
<tr>
    <td><CopyableCode code="IsDefault" /></td>
    <td><code>boolean</code></td>
    <td>Boolean value indicating whether configuration is default.</td>
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
    <td><CopyableCode code="ConfigDisplayName" /></td>
    <td><code>string</code></td>
    <td>Configuration friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="ConfigProperties" /></td>
    <td><code>string</code></td>
    <td>Serialized JSON object for detailed properties.</td>
</tr>
<tr>
    <td><CopyableCode code="ConnectorId" /></td>
    <td><code>string</code></td>
    <td>Connector identifier where work item is created.</td>
</tr>
<tr>
    <td><CopyableCode code="Id" /></td>
    <td><code>string</code></td>
    <td>Unique Id for work item.</td>
</tr>
<tr>
    <td><CopyableCode code="IsDefault" /></td>
    <td><code>boolean</code></td>
    <td>Boolean value indicating whether configuration is default.</td>
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
    <td><a href="#get_item"><CopyableCode code="get_item" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-work_item_config_id"><code>work_item_config_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets specified work item configuration for an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list work item configurations that exist for the application.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a work item configuration for an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#update_item"><CopyableCode code="update_item" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-work_item_config_id"><code>work_item_config_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a work item configuration for an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-work_item_config_id"><code>work_item_config_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a work item configuration of an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#get_default"><CopyableCode code="get_default" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets default work item configurations that exist for the application.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-work_item_config_id">
    <td><CopyableCode code="work_item_config_id" /></td>
    <td><code>string</code></td>
    <td>The unique work item configuration Id. This can be either friendly name of connector as defined in connector configuration. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_item"
    values={[
        { label: 'get_item', value: 'get_item' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_item">

Gets specified work item configuration for an Application Insights component.

```sql
SELECT
ConfigDisplayName,
ConfigProperties,
ConnectorId,
Id,
IsDefault
FROM azure.applicationinsights.work_item_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND work_item_config_id = '{{ work_item_config_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list work item configurations that exist for the application.

```sql
SELECT
ConfigDisplayName,
ConfigProperties,
ConnectorId,
Id,
IsDefault
FROM azure.applicationinsights.work_item_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a work item configuration for an Application Insights component.

```sql
INSERT INTO azure.applicationinsights.work_item_configurations (
ConnectorId,
ConnectorDataConfiguration,
ValidateOnly,
WorkItemProperties,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ ConnectorId }}',
'{{ ConnectorDataConfiguration }}',
{{ ValidateOnly }},
'{{ WorkItemProperties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
ConfigDisplayName,
ConfigProperties,
ConnectorId,
Id,
IsDefault
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: work_item_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the work_item_configurations resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the work_item_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the work_item_configurations resource.
    - name: ConnectorId
      value: "{{ ConnectorId }}"
      description: |
        Unique connector id.
    - name: ConnectorDataConfiguration
      value: "{{ ConnectorDataConfiguration }}"
      description: |
        Serialized JSON object for detailed properties.
    - name: ValidateOnly
      value: {{ ValidateOnly }}
      description: |
        Boolean indicating validate only.
    - name: WorkItemProperties
      value: "{{ WorkItemProperties }}"
      description: |
        Custom work item properties.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_item"
    values={[
        { label: 'update_item', value: 'update_item' }
    ]}
>
<TabItem value="update_item">

Update a work item configuration for an Application Insights component.

```sql
UPDATE azure.applicationinsights.work_item_configurations
SET 
ConnectorId = '{{ ConnectorId }}',
ConnectorDataConfiguration = '{{ ConnectorDataConfiguration }}',
ValidateOnly = {{ ValidateOnly }},
WorkItemProperties = '{{ WorkItemProperties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND work_item_config_id = '{{ work_item_config_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
ConfigDisplayName,
ConfigProperties,
ConnectorId,
Id,
IsDefault;
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

Delete a work item configuration of an Application Insights component.

```sql
DELETE FROM azure.applicationinsights.work_item_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND work_item_config_id = '{{ work_item_config_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_default"
    values={[
        { label: 'get_default', value: 'get_default' }
    ]}
>
<TabItem value="get_default">

Gets default work item configurations that exist for the application.

```sql
EXEC azure.applicationinsights.work_item_configurations.get_default 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
