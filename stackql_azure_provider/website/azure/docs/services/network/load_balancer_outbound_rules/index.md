--- 
title: load_balancer_outbound_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_outbound_rules
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

Creates, updates, deletes, gets or lists a <code>load_balancer_outbound_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancer_outbound_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_outbound_rules" /></td></tr>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allocatedOutboundPorts" /></td>
    <td><code>integer</code></td>
    <td>The number of outbound ports to be used for NAT.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPool" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTcpReset" /></td>
    <td><code>boolean</code></td>
    <td>Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>The Frontend IP addresses of the load balancer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The timeout for the TCP idle connection.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The protocol for the outbound rule in load balancer. Required. Known values are: "Tcp", "Udp", and "All". (Tcp, Udp, All)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the outbound rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allocatedOutboundPorts" /></td>
    <td><code>integer</code></td>
    <td>The number of outbound ports to be used for NAT.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPool" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableTcpReset" /></td>
    <td><code>boolean</code></td>
    <td>Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>The Frontend IP addresses of the load balancer. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The timeout for the TCP idle connection.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The protocol for the outbound rule in load balancer. Required. Known values are: "Tcp", "Udp", and "All". (Tcp, Udp, All)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the outbound rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-outbound_rule_name"><code>outbound_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified load balancer outbound rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the outbound rules in a load balancer.</td>
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
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancer. Required.</td>
</tr>
<tr id="parameter-outbound_rule_name">
    <td><CopyableCode code="outbound_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the outbound rule. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the specified load balancer outbound rule.

```sql
SELECT
id,
name,
allocatedOutboundPorts,
backendAddressPool,
enableTcpReset,
etag,
frontendIPConfigurations,
idleTimeoutInMinutes,
protocol,
provisioningState,
type
FROM azure.network.load_balancer_outbound_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND outbound_rule_name = '{{ outbound_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the outbound rules in a load balancer.

```sql
SELECT
id,
name,
allocatedOutboundPorts,
backendAddressPool,
enableTcpReset,
etag,
frontendIPConfigurations,
idleTimeoutInMinutes,
protocol,
provisioningState,
type
FROM azure.network.load_balancer_outbound_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
