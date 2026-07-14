--- 
title: azure_traffic_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_traffic_collectors
  - network_function
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

Creates, updates, deletes, gets or lists an <code>azure_traffic_collectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="azure_traffic_collectors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_function.azure_traffic_collectors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="collectorPolicies" /></td>
    <td><code>array</code></td>
    <td>Collector Policies for Azure Traffic Collector.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the application rule collection resource. Known values are: "Succeeded", "Updating", "Deleting", and "Failed". (Succeeded, Updating, Deleting, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>Resource reference properties.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_traffic_collector_name"><code>azure_traffic_collector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified Azure Traffic Collector in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_traffic_collector_name"><code>azure_traffic_collector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Azure Traffic Collector resource.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_traffic_collector_name"><code>azure_traffic_collector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified Azure Traffic Collector tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_traffic_collector_name"><code>azure_traffic_collector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Azure Traffic Collector resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-azure_traffic_collector_name"><code>azure_traffic_collector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a specified Azure Traffic Collector resource.</td>
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
<tr id="parameter-azure_traffic_collector_name">
    <td><CopyableCode code="azure_traffic_collector_name" /></td>
    <td><code>string</code></td>
    <td>Azure Traffic Collector name. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the specified Azure Traffic Collector in a specified resource group.

```sql
SELECT
id,
name,
collectorPolicies,
etag,
location,
provisioningState,
systemData,
tags,
type,
virtualHub
FROM azure.network_function.azure_traffic_collectors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND azure_traffic_collector_name = '{{ azure_traffic_collector_name }}' -- required
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

Creates or updates a Azure Traffic Collector resource.

```sql
INSERT INTO azure.network_function.azure_traffic_collectors (
properties,
location,
tags,
resource_group_name,
azure_traffic_collector_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ location }}' /* required */,
'{{ tags }}',
'{{ resource_group_name }}',
'{{ azure_traffic_collector_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: azure_traffic_collectors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the azure_traffic_collectors resource.
    - name: azure_traffic_collector_name
      value: "{{ azure_traffic_collector_name }}"
      description: Required parameter for the azure_traffic_collectors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the azure_traffic_collectors resource.
    - name: properties
      description: |
        Properties of the Azure Traffic Collector.
      value:
        collectorPolicies:
          - id: "{{ id }}"
        virtualHub:
          id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates the specified Azure Traffic Collector tags.

```sql
UPDATE azure.network_function.azure_traffic_collectors
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_traffic_collector_name = '{{ azure_traffic_collector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
systemData,
tags,
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

Creates or updates a Azure Traffic Collector resource.

```sql
REPLACE azure.network_function.azure_traffic_collectors
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND azure_traffic_collector_name = '{{ azure_traffic_collector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
location,
properties,
systemData,
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

Deletes a specified Azure Traffic Collector resource.

```sql
DELETE FROM azure.network_function.azure_traffic_collectors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND azure_traffic_collector_name = '{{ azure_traffic_collector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
