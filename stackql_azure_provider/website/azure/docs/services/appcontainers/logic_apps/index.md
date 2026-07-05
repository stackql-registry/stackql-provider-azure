--- 
title: logic_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - logic_apps
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>logic_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="logic_apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.logic_apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_workflow"
    values={[
        { label: 'get_workflow', value: 'get_workflow' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_workflow">

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
    <td><CopyableCode code="files" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the files.</td>
</tr>
<tr>
    <td><CopyableCode code="flowState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the state of the workflow. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended". (NotSpecified, Completed, Enabled, Disabled, Deleted, Suspended)</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Gets or sets workflow health.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Gets the logic app hybrid workflow kind. Known values are: "Stateful", "Stateless", and "Agentic". (Stateful, Stateless, Agentic)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_workflow"><CopyableCode code="get_workflow" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get workflow information by its name. Get workflow information by its name.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a logic app extension resource. Gets a logic app extension resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Logic App extension resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Logic App extension resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Logic App extension resource.</td>
</tr>
<tr>
    <td><a href="#list_workflows_connections"><CopyableCode code="list_workflows_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets logic app's connections. Gets logic app's connections.</td>
</tr>
<tr>
    <td><a href="#list_workflows"><CopyableCode code="list_workflows" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_app_name"><code>container_app_name</code></a>, <a href="#parameter-logic_app_name"><code>logic_app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the workflows for a logic app. List the workflows for a logic app.</td>
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
<tr id="parameter-container_app_name">
    <td><CopyableCode code="container_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Container App. Required.</td>
</tr>
<tr id="parameter-logic_app_name">
    <td><CopyableCode code="logic_app_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Logic App, the extension resource. Required.</td>
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
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>Workflow name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_workflow"
    values={[
        { label: 'get_workflow', value: 'get_workflow' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_workflow">

Get workflow information by its name. Get workflow information by its name.

```sql
SELECT
id,
name,
files,
flowState,
health,
kind,
systemData,
type
FROM azure.appcontainers.logic_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND logic_app_name = '{{ logic_app_name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets a logic app extension resource. Gets a logic app extension resource.

```sql
SELECT
id,
name,
systemData,
type
FROM azure.appcontainers.logic_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_app_name = '{{ container_app_name }}' -- required
AND logic_app_name = '{{ logic_app_name }}' -- required
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

Create or update a Logic App extension resource.

```sql
INSERT INTO azure.appcontainers.logic_apps (
id,
name,
type,
systemData,
resource_group_name,
container_app_name,
logic_app_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ type }}',
'{{ systemData }}',
'{{ resource_group_name }}',
'{{ container_app_name }}',
'{{ logic_app_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: logic_apps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the logic_apps resource.
    - name: container_app_name
      value: "{{ container_app_name }}"
      description: Required parameter for the logic_apps resource.
    - name: logic_app_name
      value: "{{ logic_app_name }}"
      description: Required parameter for the logic_apps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the logic_apps resource.
    - name: id
      value: "{{ id }}"
      description: |
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource.
    - name: type
      value: "{{ type }}"
      description: |
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".
    - name: systemData
      description: |
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
      value:
        createdBy: "{{ createdBy }}"
        createdByType: "{{ createdByType }}"
        createdAt: "{{ createdAt }}"
        lastModifiedBy: "{{ lastModifiedBy }}"
        lastModifiedByType: "{{ lastModifiedByType }}"
        lastModifiedAt: "{{ lastModifiedAt }}"
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

Create or update a Logic App extension resource.

```sql
REPLACE azure.appcontainers.logic_apps
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
systemData = '{{ systemData }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND logic_app_name = '{{ logic_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes a Logic App extension resource.

```sql
DELETE FROM azure.appcontainers.logic_apps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND container_app_name = '{{ container_app_name }}' --required
AND logic_app_name = '{{ logic_app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_workflows_connections"
    values={[
        { label: 'list_workflows_connections', value: 'list_workflows_connections' },
        { label: 'list_workflows', value: 'list_workflows' }
    ]}
>
<TabItem value="list_workflows_connections">

Gets logic app's connections. Gets logic app's connections.

```sql
EXEC azure.appcontainers.logic_apps.list_workflows_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@logic_app_name='{{ logic_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_workflows">

List the workflows for a logic app. List the workflows for a logic app.

```sql
EXEC azure.appcontainers.logic_apps.list_workflows 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_app_name='{{ container_app_name }}' --required, 
@logic_app_name='{{ logic_app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
