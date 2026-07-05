--- 
title: load_balancer_load_balancing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_load_balancing_rules
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

Creates, updates, deletes, gets or lists a <code>load_balancer_load_balancing_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancer_load_balancing_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_load_balancing_rules" /></td></tr>
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
    <td><CopyableCode code="backendAddressPool" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>An array of references to pool of DIPs.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPort" /></td>
    <td><code>integer</code></td>
    <td>The port used for internal connections on the endpoint. Acceptable values are between 0 and 65535. Note that value 0 enables "Any Port".</td>
</tr>
<tr>
    <td><CopyableCode code="disableOutboundSnat" /></td>
    <td><code>boolean</code></td>
    <td>Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enableConnectionTracking" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether connections between 2 communicating endpoints can be tracked and associated to the same backend VM over its lifetime when using UDP protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFloatingIP" /></td>
    <td><code>boolean</code></td>
    <td>Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.</td>
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
    <td><CopyableCode code="frontendIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPort" /></td>
    <td><code>integer</code></td>
    <td>The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values are between 0 and 65534. Note that value 0 enables "Any Port". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="loadDistribution" /></td>
    <td><code>string</code></td>
    <td>The load distribution policy for this rule. Known values are: "Default", "SourceIP", and "SourceIPProtocol". (Default, SourceIP, SourceIPProtocol)</td>
</tr>
<tr>
    <td><CopyableCode code="probe" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The reference to the transport protocol used by the load balancing rule. Required. Known values are: "Udp", "Tcp", "All", and "Quic". (Udp, Tcp, All, Quic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the load balancing rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="backendAddressPool" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>An array of references to pool of DIPs.</td>
</tr>
<tr>
    <td><CopyableCode code="backendPort" /></td>
    <td><code>integer</code></td>
    <td>The port used for internal connections on the endpoint. Acceptable values are between 0 and 65535. Note that value 0 enables "Any Port".</td>
</tr>
<tr>
    <td><CopyableCode code="disableOutboundSnat" /></td>
    <td><code>boolean</code></td>
    <td>Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enableConnectionTracking" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether connections between 2 communicating endpoints can be tracked and associated to the same backend VM over its lifetime when using UDP protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="enableFloatingIP" /></td>
    <td><code>boolean</code></td>
    <td>Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint.</td>
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
    <td><CopyableCode code="frontendIPConfiguration" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPort" /></td>
    <td><code>integer</code></td>
    <td>The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Acceptable values are between 0 and 65534. Note that value 0 enables "Any Port". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="idleTimeoutInMinutes" /></td>
    <td><code>integer</code></td>
    <td>The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="loadDistribution" /></td>
    <td><code>string</code></td>
    <td>The load distribution policy for this rule. Known values are: "Default", "SourceIP", and "SourceIPProtocol". (Default, SourceIP, SourceIPProtocol)</td>
</tr>
<tr>
    <td><CopyableCode code="probe" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The reference to the transport protocol used by the load balancing rule. Required. Known values are: "Udp", "Tcp", "All", and "Quic". (Udp, Tcp, All, Quic)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the load balancing rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-load_balancing_rule_name"><code>load_balancing_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified load balancer load balancing rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the load balancing rules in a load balancer.</td>
</tr>
<tr>
    <td><a href="#health"><CopyableCode code="health" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-load_balancing_rule_name"><code>load_balancing_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get health details of a load balancing rule.</td>
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
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancer. Required.</td>
</tr>
<tr id="parameter-load_balancing_rule_name">
    <td><CopyableCode code="load_balancing_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancing rule. Required.</td>
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

Gets the specified load balancer load balancing rule.

```sql
SELECT
id,
name,
backendAddressPool,
backendAddressPools,
backendPort,
disableOutboundSnat,
enableConnectionTracking,
enableFloatingIP,
enableTcpReset,
etag,
frontendIPConfiguration,
frontendPort,
idleTimeoutInMinutes,
loadDistribution,
probe,
protocol,
provisioningState,
type
FROM azure.network.load_balancer_load_balancing_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND load_balancing_rule_name = '{{ load_balancing_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the load balancing rules in a load balancer.

```sql
SELECT
id,
name,
backendAddressPool,
backendAddressPools,
backendPort,
disableOutboundSnat,
enableConnectionTracking,
enableFloatingIP,
enableTcpReset,
etag,
frontendIPConfiguration,
frontendPort,
idleTimeoutInMinutes,
loadDistribution,
probe,
protocol,
provisioningState,
type
FROM azure.network.load_balancer_load_balancing_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="health"
    values={[
        { label: 'health', value: 'health' }
    ]}
>
<TabItem value="health">

Get health details of a load balancing rule.

```sql
EXEC azure.network.load_balancer_load_balancing_rules.health 
@group_name='{{ group_name }}' --required, 
@load_balancer_name='{{ load_balancer_name }}' --required, 
@load_balancing_rule_name='{{ load_balancing_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
