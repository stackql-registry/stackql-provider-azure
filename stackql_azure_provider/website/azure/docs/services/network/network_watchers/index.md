--- 
title: network_watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_watchers
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

Creates, updates, deletes, gets or lists a <code>network_watchers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_watchers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_watchers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network watcher resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network watcher resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network watcher resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified network watcher by resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network watchers by resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network watchers by subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network watcher in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a network watcher tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network watcher in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified network watcher resource.</td>
</tr>
<tr>
    <td><a href="#list_available_providers"><CopyableCode code="list_available_providers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>NOTE: This feature is currently in preview and still being tested for stability. Lists all available internet service providers for a specified Azure region.</td>
</tr>
<tr>
    <td><a href="#get_topology"><CopyableCode code="get_topology" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the current network topology by resource group.</td>
</tr>
<tr>
    <td><a href="#get_next_hop"><CopyableCode code="get_next_hop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-sourceIPAddress"><code>sourceIPAddress</code></a>, <a href="#parameter-destinationIPAddress"><code>destinationIPAddress</code></a></td>
    <td></td>
    <td>Gets the next hop from the specified VM.</td>
</tr>
<tr>
    <td><a href="#get_vm_security_rules"><CopyableCode code="get_vm_security_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a></td>
    <td></td>
    <td>Gets the configured and effective security group rules on the specified VM.</td>
</tr>
<tr>
    <td><a href="#get_troubleshooting"><CopyableCode code="get_troubleshooting" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Initiate troubleshooting on a specified resource.</td>
</tr>
<tr>
    <td><a href="#get_troubleshooting_result"><CopyableCode code="get_troubleshooting_result" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a></td>
    <td></td>
    <td>Get the last completed troubleshooting result on a specified resource.</td>
</tr>
<tr>
    <td><a href="#get_flow_log_status"><CopyableCode code="get_flow_log_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a></td>
    <td></td>
    <td>Queries status of flow log and traffic analytics (optional) on a specified resource.</td>
</tr>
<tr>
    <td><a href="#get_azure_reachability_report"><CopyableCode code="get_azure_reachability_report" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-providerLocation"><code>providerLocation</code></a>, <a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a></td>
    <td></td>
    <td>NOTE: This feature is currently in preview and still being tested for stability. Gets the relative latency score for internet service providers from a specified location to Azure regions.</td>
</tr>
<tr>
    <td><a href="#get_network_configuration_diagnostic"><CopyableCode code="get_network_configuration_diagnostic" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-profiles"><code>profiles</code></a></td>
    <td></td>
    <td>Gets Network Configuration Diagnostic data to help customers understand and debug network behavior. It provides detailed information on what security rules were applied to a specified traffic flow and the result of evaluating these rules. Customers must provide details of a flow like source, destination, protocol, etc. The API returns whether traffic was allowed or denied, the rules evaluated for the specified flow and the evaluation results.</td>
</tr>
<tr>
    <td><a href="#verify_ip_flow"><CopyableCode code="verify_ip_flow" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-protocol"><code>protocol</code></a>, <a href="#parameter-localPort"><code>localPort</code></a>, <a href="#parameter-remotePort"><code>remotePort</code></a>, <a href="#parameter-localIPAddress"><code>localIPAddress</code></a>, <a href="#parameter-remoteIPAddress"><code>remoteIPAddress</code></a></td>
    <td></td>
    <td>Verify IP flow from the specified VM to a location given the currently configured NSG rules.</td>
</tr>
<tr>
    <td><a href="#set_flow_log_configuration"><CopyableCode code="set_flow_log_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetResourceId"><code>targetResourceId</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Configures flow log and traffic analytics (optional) on a specified resource.</td>
</tr>
<tr>
    <td><a href="#check_connectivity"><CopyableCode code="check_connectivity" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_watcher_name"><code>network_watcher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server.</td>
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
<tr id="parameter-network_watcher_name">
    <td><CopyableCode code="network_watcher_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network watcher. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified network watcher by resource group.

```sql
SELECT
id,
name,
etag,
location,
provisioningState,
tags,
type
FROM azure.network.network_watchers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_watcher_name = '{{ network_watcher_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all network watchers by resource group.

```sql
SELECT
id,
name,
etag,
location,
provisioningState,
tags,
type
FROM azure.network.network_watchers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all network watchers by subscription.

```sql
SELECT
id,
name,
etag,
location,
provisioningState,
tags,
type
FROM azure.network.network_watchers
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a network watcher in the specified resource group.

```sql
INSERT INTO azure.network.network_watchers (
id,
location,
tags,
properties,
resource_group_name,
network_watcher_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_watcher_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: network_watchers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_watchers resource.
    - name: network_watcher_name
      value: "{{ network_watcher_name }}"
      description: Required parameter for the network_watchers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_watchers resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the network watcher.
      value:
        provisioningState: "{{ provisioningState }}"
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

Updates a network watcher tags.

```sql
UPDATE azure.network.network_watchers
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Creates or updates a network watcher in the specified resource group.

```sql
REPLACE azure.network.network_watchers
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Deletes the specified network watcher resource.

```sql
DELETE FROM azure.network.network_watchers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_watcher_name = '{{ network_watcher_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_available_providers"
    values={[
        { label: 'list_available_providers', value: 'list_available_providers' },
        { label: 'get_topology', value: 'get_topology' },
        { label: 'get_next_hop', value: 'get_next_hop' },
        { label: 'get_vm_security_rules', value: 'get_vm_security_rules' },
        { label: 'get_troubleshooting', value: 'get_troubleshooting' },
        { label: 'get_troubleshooting_result', value: 'get_troubleshooting_result' },
        { label: 'get_flow_log_status', value: 'get_flow_log_status' },
        { label: 'get_azure_reachability_report', value: 'get_azure_reachability_report' },
        { label: 'get_network_configuration_diagnostic', value: 'get_network_configuration_diagnostic' },
        { label: 'verify_ip_flow', value: 'verify_ip_flow' },
        { label: 'set_flow_log_configuration', value: 'set_flow_log_configuration' },
        { label: 'check_connectivity', value: 'check_connectivity' }
    ]}
>
<TabItem value="list_available_providers">

NOTE: This feature is currently in preview and still being tested for stability. Lists all available internet service providers for a specified Azure region.

```sql
EXEC azure.network.network_watchers.list_available_providers 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"azureLocations": "{{ azureLocations }}", 
"country": "{{ country }}", 
"state": "{{ state }}", 
"city": "{{ city }}"
}'
;
```
</TabItem>
<TabItem value="get_topology">

Gets the current network topology by resource group.

```sql
EXEC azure.network.network_watchers.get_topology 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceGroupName": "{{ targetResourceGroupName }}", 
"targetVirtualNetwork": "{{ targetVirtualNetwork }}", 
"targetSubnet": "{{ targetSubnet }}"
}'
;
```
</TabItem>
<TabItem value="get_next_hop">

Gets the next hop from the specified VM.

```sql
EXEC azure.network.network_watchers.get_next_hop 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"sourceIPAddress": "{{ sourceIPAddress }}", 
"destinationIPAddress": "{{ destinationIPAddress }}", 
"targetNicResourceId": "{{ targetNicResourceId }}"
}'
;
```
</TabItem>
<TabItem value="get_vm_security_rules">

Gets the configured and effective security group rules on the specified VM.

```sql
EXEC azure.network.network_watchers.get_vm_security_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}"
}'
;
```
</TabItem>
<TabItem value="get_troubleshooting">

Initiate troubleshooting on a specified resource.

```sql
EXEC azure.network.network_watchers.get_troubleshooting 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_troubleshooting_result">

Get the last completed troubleshooting result on a specified resource.

```sql
EXEC azure.network.network_watchers.get_troubleshooting_result 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}"
}'
;
```
</TabItem>
<TabItem value="get_flow_log_status">

Queries status of flow log and traffic analytics (optional) on a specified resource.

```sql
EXEC azure.network.network_watchers.get_flow_log_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}"
}'
;
```
</TabItem>
<TabItem value="get_azure_reachability_report">

NOTE: This feature is currently in preview and still being tested for stability. Gets the relative latency score for internet service providers from a specified location to Azure regions.

```sql
EXEC azure.network.network_watchers.get_azure_reachability_report 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"providerLocation": "{{ providerLocation }}", 
"providers": "{{ providers }}", 
"azureLocations": "{{ azureLocations }}", 
"startTime": "{{ startTime }}", 
"endTime": "{{ endTime }}"
}'
;
```
</TabItem>
<TabItem value="get_network_configuration_diagnostic">

Gets Network Configuration Diagnostic data to help customers understand and debug network behavior. It provides detailed information on what security rules were applied to a specified traffic flow and the result of evaluating these rules. Customers must provide details of a flow like source, destination, protocol, etc. The API returns whether traffic was allowed or denied, the rules evaluated for the specified flow and the evaluation results.

```sql
EXEC azure.network.network_watchers.get_network_configuration_diagnostic 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"verbosityLevel": "{{ verbosityLevel }}", 
"profiles": "{{ profiles }}"
}'
;
```
</TabItem>
<TabItem value="verify_ip_flow">

Verify IP flow from the specified VM to a location given the currently configured NSG rules.

```sql
EXEC azure.network.network_watchers.verify_ip_flow 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"direction": "{{ direction }}", 
"protocol": "{{ protocol }}", 
"localPort": "{{ localPort }}", 
"remotePort": "{{ remotePort }}", 
"localIPAddress": "{{ localIPAddress }}", 
"remoteIPAddress": "{{ remoteIPAddress }}", 
"targetNicResourceId": "{{ targetNicResourceId }}"
}'
;
```
</TabItem>
<TabItem value="set_flow_log_configuration">

Configures flow log and traffic analytics (optional) on a specified resource.

```sql
EXEC azure.network.network_watchers.set_flow_log_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetResourceId": "{{ targetResourceId }}", 
"properties": "{{ properties }}", 
"flowAnalyticsConfiguration": "{{ flowAnalyticsConfiguration }}", 
"identity": "{{ identity }}"
}'
;
```
</TabItem>
<TabItem value="check_connectivity">

Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server.

```sql
EXEC azure.network.network_watchers.check_connectivity 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_watcher_name='{{ network_watcher_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"source": "{{ source }}", 
"destination": "{{ destination }}", 
"protocol": "{{ protocol }}", 
"protocolConfiguration": "{{ protocolConfiguration }}", 
"preferredIPVersion": "{{ preferredIPVersion }}"
}'
;
```
</TabItem>
</Tabs>
