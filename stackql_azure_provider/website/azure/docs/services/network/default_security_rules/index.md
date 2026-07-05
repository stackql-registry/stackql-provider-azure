--- 
title: default_security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - default_security_rules
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

Creates, updates, deletes, gets or lists a <code>default_security_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="default_security_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.default_security_rules" /></td></tr>
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
    <td><CopyableCode code="access" /></td>
    <td><code>string</code></td>
    <td>The network traffic is allowed or denied. Required. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for this rule. Restricted to 140 chars.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The destination address prefix. CIDR or destination IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The destination address prefixes. CIDR or destination IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationApplicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>The application security group specified as destination.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPortRange" /></td>
    <td><code>string</code></td>
    <td>The destination port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPortRanges" /></td>
    <td><code>array</code></td>
    <td>The destination port ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Required. Known values are: "Inbound" and "Outbound". (Inbound, Outbound)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Network protocol this rule applies to. Required. Known values are: "Tcp", "Udp", "Icmp", "Esp", "*", and "Ah". (Tcp, Udp, Icmp, Esp, *, Ah)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the security rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The CIDR or source IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The CIDR or source IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceApplicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>The application security group specified as source.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePortRange" /></td>
    <td><code>string</code></td>
    <td>The source port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePortRanges" /></td>
    <td><code>array</code></td>
    <td>The source port ranges.</td>
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
    <td><CopyableCode code="access" /></td>
    <td><code>string</code></td>
    <td>The network traffic is allowed or denied. Required. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for this rule. Restricted to 140 chars.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The destination address prefix. CIDR or destination IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The destination address prefixes. CIDR or destination IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationApplicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>The application security group specified as destination.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPortRange" /></td>
    <td><code>string</code></td>
    <td>The destination port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPortRanges" /></td>
    <td><code>array</code></td>
    <td>The destination port ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Required. Known values are: "Inbound" and "Outbound". (Inbound, Outbound)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Network protocol this rule applies to. Required. Known values are: "Tcp", "Udp", "Icmp", "Esp", "*", and "Ah". (Tcp, Udp, Icmp, Esp, *, Ah)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the security rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceAddressPrefix" /></td>
    <td><code>string</code></td>
    <td>The CIDR or source IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The CIDR or source IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceApplicationSecurityGroups" /></td>
    <td><code>array</code></td>
    <td>The application security group specified as source.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePortRange" /></td>
    <td><code>string</code></td>
    <td>The source port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePortRanges" /></td>
    <td><code>array</code></td>
    <td>The source port ranges.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-default_security_rule_name"><code>default_security_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified default network security rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all default security rules in a network security group.</td>
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
<tr id="parameter-default_security_rule_name">
    <td><CopyableCode code="default_security_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the default security rule. Required.</td>
</tr>
<tr id="parameter-network_security_group_name">
    <td><CopyableCode code="network_security_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network security group. Required.</td>
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

Get the specified default network security rule.

```sql
SELECT
id,
name,
access,
description,
destinationAddressPrefix,
destinationAddressPrefixes,
destinationApplicationSecurityGroups,
destinationPortRange,
destinationPortRanges,
direction,
etag,
priority,
protocol,
provisioningState,
sourceAddressPrefix,
sourceAddressPrefixes,
sourceApplicationSecurityGroups,
sourcePortRange,
sourcePortRanges,
type
FROM azure.network.default_security_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_group_name = '{{ network_security_group_name }}' -- required
AND default_security_rule_name = '{{ default_security_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all default security rules in a network security group.

```sql
SELECT
id,
name,
access,
description,
destinationAddressPrefix,
destinationAddressPrefixes,
destinationApplicationSecurityGroups,
destinationPortRange,
destinationPortRanges,
direction,
etag,
priority,
protocol,
provisioningState,
sourceAddressPrefix,
sourceAddressPrefixes,
sourceApplicationSecurityGroups,
sourcePortRange,
sourcePortRanges,
type
FROM azure.network.default_security_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_group_name = '{{ network_security_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
