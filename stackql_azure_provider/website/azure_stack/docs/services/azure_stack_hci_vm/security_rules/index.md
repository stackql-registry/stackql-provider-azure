--- 
title: security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_rules
  - azure_stack_hci_vm
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>security_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci_vm.security_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_network_security_group', value: 'list_by_network_security_group' }
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
    <td><CopyableCode code="destinationAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The destination address prefixes. CIDR or destination IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPortRanges" /></td>
    <td><code>array</code></td>
    <td>The destination port ranges. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Required. Known values are: "Inbound" and "Outbound". (Inbound, Outbound)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Network protocol this rule applies to. Required. Known values are: "Tcp", "Udp", "Icmp", and "*". (Tcp, Udp, Icmp, *)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the SR. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The CIDR or source IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePortRanges" /></td>
    <td><code>array</code></td>
    <td>The source port ranges. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
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
<TabItem value="list_by_network_security_group">

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
    <td><CopyableCode code="destinationAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The destination address prefixes. CIDR or destination IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationPortRanges" /></td>
    <td><code>array</code></td>
    <td>The destination port ranges. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. Required. Known values are: "Inbound" and "Outbound". (Inbound, Outbound)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Network protocol this rule applies to. Required. Known values are: "Tcp", "Udp", "Icmp", and "*". (Tcp, Udp, Icmp, *)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the SR. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceAddressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The CIDR or source IP ranges.</td>
</tr>
<tr>
    <td><CopyableCode code="sourcePortRanges" /></td>
    <td><code>array</code></td>
    <td>The source port ranges. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-security_rule_name"><code>security_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified security rule.</td>
</tr>
<tr>
    <td><a href="#list_by_network_security_group"><CopyableCode code="list_by_network_security_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all security rules in a Network Security Group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-security_rule_name"><code>security_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a security rule in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-security_rule_name"><code>security_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a security rule in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_group_name"><code>network_security_group_name</code></a>, <a href="#parameter-security_rule_name"><code>security_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified security rule.</td>
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
<tr id="parameter-network_security_group_name">
    <td><CopyableCode code="network_security_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the network security group. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_rule_name">
    <td><CopyableCode code="security_rule_name" /></td>
    <td><code>string</code></td>
    <td>Name of the security rule. Required.</td>
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
        { label: 'list_by_network_security_group', value: 'list_by_network_security_group' }
    ]}
>
<TabItem value="get">

Gets the specified security rule.

```sql
SELECT
id,
name,
access,
description,
destinationAddressPrefixes,
destinationPortRanges,
direction,
extendedLocation,
priority,
protocol,
provisioningState,
sourceAddressPrefixes,
sourcePortRanges,
systemData,
type
FROM azure_stack.azure_stack_hci_vm.security_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_group_name = '{{ network_security_group_name }}' -- required
AND security_rule_name = '{{ security_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_network_security_group">

Gets all security rules in a Network Security Group.

```sql
SELECT
id,
name,
access,
description,
destinationAddressPrefixes,
destinationPortRanges,
direction,
extendedLocation,
priority,
protocol,
provisioningState,
sourceAddressPrefixes,
sourcePortRanges,
systemData,
type
FROM azure_stack.azure_stack_hci_vm.security_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_group_name = '{{ network_security_group_name }}' -- required
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

Creates or updates a security rule in the specified resource group.

```sql
INSERT INTO azure_stack.azure_stack_hci_vm.security_rules (
properties,
extendedLocation,
resource_group_name,
network_security_group_name,
security_rule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ resource_group_name }}',
'{{ network_security_group_name }}',
'{{ security_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: security_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the security_rules resource.
    - name: network_security_group_name
      value: "{{ network_security_group_name }}"
      description: Required parameter for the security_rules resource.
    - name: security_rule_name
      value: "{{ security_rule_name }}"
      description: Required parameter for the security_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the security_rules resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        description: "{{ description }}"
        protocol: "{{ protocol }}"
        sourceAddressPrefixes:
          - "{{ sourceAddressPrefixes }}"
        destinationAddressPrefixes:
          - "{{ destinationAddressPrefixes }}"
        sourcePortRanges:
          - "{{ sourcePortRanges }}"
        destinationPortRanges:
          - "{{ destinationPortRanges }}"
        access: "{{ access }}"
        priority: {{ priority }}
        direction: "{{ direction }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        The extendedLocation of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

Creates or updates a security rule in the specified resource group.

```sql
REPLACE azure_stack.azure_stack_hci_vm.security_rules
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_security_group_name = '{{ network_security_group_name }}' --required
AND security_rule_name = '{{ security_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
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

Deletes the specified security rule.

```sql
DELETE FROM azure_stack.azure_stack_hci_vm.security_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_security_group_name = '{{ network_security_group_name }}' --required
AND security_rule_name = '{{ security_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
