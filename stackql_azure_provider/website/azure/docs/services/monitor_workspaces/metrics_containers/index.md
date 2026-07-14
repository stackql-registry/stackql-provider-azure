--- 
title: metrics_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_containers
  - monitor_workspaces
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

Creates, updates, deletes, gets or lists a <code>metrics_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metrics_containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor_workspaces.metrics_containers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_azure_monitor_workspace', value: 'list_by_azure_monitor_workspace' }
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the metrics container. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of Metrics Query Service that this AMW will use for all metric queries.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_azure_monitor_workspace">

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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the metrics container. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
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
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of Metrics Query Service that this AMW will use for all metric queries.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-metrics_container_name"><code>metrics_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets metrics container settings for a monitoring account.</td>
</tr>
<tr>
    <td><a href="#list_by_azure_monitor_workspace"><CopyableCode code="list_by_azure_monitor_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists metrics containers for a monitoring account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-metrics_container_name"><code>metrics_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates metrics container settings for a monitoring account.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_monitor_workspace_name"><code>azure_monitor_workspace_name</code></a>, <a href="#parameter-metrics_container_name"><code>metrics_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates metrics container settings for a monitoring account.</td>
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
<tr id="parameter-azure_monitor_workspace_name">
    <td><CopyableCode code="azure_monitor_workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure Monitor Workspace. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-metrics_container_name">
    <td><CopyableCode code="metrics_container_name" /></td>
    <td><code>string</code></td>
    <td>The name of the MetricsContainer. Required.</td>
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
        { label: 'list_by_azure_monitor_workspace', value: 'list_by_azure_monitor_workspace' }
    ]}
>
<TabItem value="get">

Gets metrics container settings for a monitoring account.

```sql
SELECT
id,
name,
provisioningState,
systemData,
type,
version
FROM azure.monitor_workspaces.metrics_containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' -- required
AND metrics_container_name = '{{ metrics_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_azure_monitor_workspace">

Lists metrics containers for a monitoring account.

```sql
SELECT
id,
name,
provisioningState,
systemData,
type,
version
FROM azure.monitor_workspaces.metrics_containers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' -- required
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

Creates or updates metrics container settings for a monitoring account.

```sql
INSERT INTO azure.monitor_workspaces.metrics_containers (
properties,
resource_group_name,
azure_monitor_workspace_name,
metrics_container_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ azure_monitor_workspace_name }}',
'{{ metrics_container_name }}',
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
- name: metrics_containers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the metrics_containers resource.
    - name: azure_monitor_workspace_name
      value: "{{ azure_monitor_workspace_name }}"
      description: Required parameter for the metrics_containers resource.
    - name: metrics_container_name
      value: "{{ metrics_container_name }}"
      description: Required parameter for the metrics_containers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the metrics_containers resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        version: "{{ version }}"
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

Creates or updates metrics container settings for a monitoring account.

```sql
REPLACE azure.monitor_workspaces.metrics_containers
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_monitor_workspace_name = '{{ azure_monitor_workspace_name }}' --required
AND metrics_container_name = '{{ metrics_container_name }}' --required
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
