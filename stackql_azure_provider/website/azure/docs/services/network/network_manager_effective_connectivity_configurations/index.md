--- 
title: network_manager_effective_connectivity_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_manager_effective_connectivity_configurations
  - network
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

Creates, updates, deletes, gets or lists a <code>network_manager_effective_connectivity_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_manager_effective_connectivity_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_manager_effective_connectivity_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_network_manager_effective_connectivity_configurations"
    values={[
        { label: 'list_network_manager_effective_connectivity_configurations', value: 'list_network_manager_effective_connectivity_configurations' }
    ]}
>
<TabItem value="list_network_manager_effective_connectivity_configurations">

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
    <td>Connectivity configuration ID.</td>
</tr>
<tr>
    <td><CopyableCode code="appliesToGroups" /></td>
    <td><code>array</code></td>
    <td>Groups for configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationGroups" /></td>
    <td><code>array</code></td>
    <td>Effective configuration groups.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityCapabilities" /></td>
    <td><code>object</code></td>
    <td>Collection of additional settings to enhance specific topology behaviors of the connectivity configuration resource.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityTopology" /></td>
    <td><code>string</code></td>
    <td>Connectivity topology type. Required. Known values are: "HubAndSpoke" and "Mesh". (HubAndSpoke, Mesh)</td>
</tr>
<tr>
    <td><CopyableCode code="deleteExistingPeering" /></td>
    <td><code>string</code></td>
    <td>Flag if need to remove current existing peerings. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the connectivity configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="hubs" /></td>
    <td><code>array</code></td>
    <td>List of hubItems.</td>
</tr>
<tr>
    <td><CopyableCode code="isGlobal" /></td>
    <td><code>string</code></td>
    <td>Flag if global mesh is supported. Known values are: "False" and "True". (False, True)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the connectivity configuration resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for this resource.</td>
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
    <td><a href="#list_network_manager_effective_connectivity_configurations"><CopyableCode code="list_network_manager_effective_connectivity_configurations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_name"><code>virtual_network_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>List all effective connectivity configurations applied on a virtual network.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_network_name">
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network. Required.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>An optional query parameter which specifies the maximum number of records to be returned by the server. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_network_manager_effective_connectivity_configurations"
    values={[
        { label: 'list_network_manager_effective_connectivity_configurations', value: 'list_network_manager_effective_connectivity_configurations' }
    ]}
>
<TabItem value="list_network_manager_effective_connectivity_configurations">

List all effective connectivity configurations applied on a virtual network.

```sql
SELECT
id,
appliesToGroups,
configurationGroups,
connectivityCapabilities,
connectivityTopology,
deleteExistingPeering,
description,
hubs,
isGlobal,
provisioningState,
resourceGuid
FROM azure.network.network_manager_effective_connectivity_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_name = '{{ virtual_network_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>
