--- 
title: scenario_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - scenario_configurations
  - chaos
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

Creates, updates, deletes, gets or lists a <code>scenario_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scenario_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.chaos.scenario_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
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
    <td><CopyableCode code="exclusions" /></td>
    <td><code>object</code></td>
    <td>Exclusion criteria for protecting resources from fault injection.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>Filter criteria used to constrain which discovered resources participate in fault injection.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>Runtime parameter values for the scenario. Keys must match parameter names defined in the scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Most recent provisioning state for the given scenario resource. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Running". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Running)</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the scenario this configuration applies to. Required.</td>
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
<TabItem value="list_all">

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
    <td><CopyableCode code="exclusions" /></td>
    <td><code>object</code></td>
    <td>Exclusion criteria for protecting resources from fault injection.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>Filter criteria used to constrain which discovered resources participate in fault injection.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>Runtime parameter values for the scenario. Keys must match parameter names defined in the scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Most recent provisioning state for the given scenario resource. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", "Deleting", and "Running". (Succeeded, Failed, Canceled, Creating, Updating, Deleting, Running)</td>
</tr>
<tr>
    <td><CopyableCode code="scenarioId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the scenario this configuration applies to. Required.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a scenario definition.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of scenario definitions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a scenario definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a scenario definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a scenario definition.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute the scenario execution with the given scenario configuration.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validate the given scenario configuration.</td>
</tr>
<tr>
    <td><a href="#fix_resource_permissions"><CopyableCode code="fix_resource_permissions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-scenario_name"><code>scenario_name</code></a>, <a href="#parameter-scenario_configuration_name"><code>scenario_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fixes resource permissions for the given scenario configuration.</td>
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
<tr id="parameter-scenario_configuration_name">
    <td><CopyableCode code="scenario_configuration_name" /></td>
    <td><code>string</code></td>
    <td>Name of the scenario definition. Required.</td>
</tr>
<tr id="parameter-scenario_name">
    <td><CopyableCode code="scenario_name" /></td>
    <td><code>string</code></td>
    <td>Name of the scenario. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>String that represents a Workspace resource name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get a scenario definition.

```sql
SELECT
id,
name,
exclusions,
filters,
parameters,
provisioningState,
scenarioId,
systemData,
type
FROM azure.chaos.scenario_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND scenario_name = '{{ scenario_name }}' -- required
AND scenario_configuration_name = '{{ scenario_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Get a list of scenario definitions.

```sql
SELECT
id,
name,
exclusions,
filters,
parameters,
provisioningState,
scenarioId,
systemData,
type
FROM azure.chaos.scenario_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND scenario_name = '{{ scenario_name }}' -- required
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

Create or update a scenario definition.

```sql
INSERT INTO azure.chaos.scenario_configurations (
properties,
resource_group_name,
workspace_name,
scenario_name,
scenario_configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ scenario_name }}',
'{{ scenario_configuration_name }}',
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
- name: scenario_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the scenario_configurations resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the scenario_configurations resource.
    - name: scenario_name
      value: "{{ scenario_name }}"
      description: Required parameter for the scenario_configurations resource.
    - name: scenario_configuration_name
      value: "{{ scenario_configuration_name }}"
      description: Required parameter for the scenario_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the scenario_configurations resource.
    - name: properties
      description: |
        The properties of scenario definition.
      value:
        scenarioId: "{{ scenarioId }}"
        parameters:
          - key: "{{ key }}"
            value: "{{ value }}"
        exclusions:
          resources:
            - "{{ resources }}"
          tags:
            - key: "{{ key }}"
              value: "{{ value }}"
          types:
            - "{{ types }}"
        provisioningState: "{{ provisioningState }}"
        filters:
          locations:
            - "{{ locations }}"
          zones:
            - "{{ zones }}"
          physicalZones:
            - "{{ physicalZones }}"
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

Create or update a scenario definition.

```sql
REPLACE azure.chaos.scenario_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND scenario_name = '{{ scenario_name }}' --required
AND scenario_configuration_name = '{{ scenario_configuration_name }}' --required
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

Delete a scenario definition.

```sql
DELETE FROM azure.chaos.scenario_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND scenario_name = '{{ scenario_name }}' --required
AND scenario_configuration_name = '{{ scenario_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute"
    values={[
        { label: 'execute', value: 'execute' },
        { label: 'validate', value: 'validate' },
        { label: 'fix_resource_permissions', value: 'fix_resource_permissions' }
    ]}
>
<TabItem value="execute">

Execute the scenario execution with the given scenario configuration.

```sql
EXEC azure.chaos.scenario_configurations.execute 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@scenario_name='{{ scenario_name }}' --required, 
@scenario_configuration_name='{{ scenario_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate">

Validate the given scenario configuration.

```sql
EXEC azure.chaos.scenario_configurations.validate 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@scenario_name='{{ scenario_name }}' --required, 
@scenario_configuration_name='{{ scenario_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="fix_resource_permissions">

Fixes resource permissions for the given scenario configuration.

```sql
EXEC azure.chaos.scenario_configurations.fix_resource_permissions 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@scenario_name='{{ scenario_name }}' --required, 
@scenario_configuration_name='{{ scenario_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"whatIf": {{ whatIf }}
}'
;
```
</TabItem>
</Tabs>
