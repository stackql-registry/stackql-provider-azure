--- 
title: virtual_network_gateway_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_nat_rules
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateway_nat_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_network_gateway_nat_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateway_nat_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_virtual_network_gateway', value: 'list_by_virtual_network_gateway' }
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="externalMappings" /></td>
    <td><code>array</code></td>
    <td>The private IP address external mapping for NAT.</td>
</tr>
<tr>
    <td><CopyableCode code="internalMappings" /></td>
    <td><code>array</code></td>
    <td>The private IP address internal mapping for NAT.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurationId" /></td>
    <td><code>string</code></td>
    <td>The IP Configuration ID this NAT rule applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The Source NAT direction of a VPN NAT. Known values are: "EgressSnat" and "IngressSnat". (EgressSnat, IngressSnat)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NAT Rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_virtual_network_gateway">

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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="externalMappings" /></td>
    <td><code>array</code></td>
    <td>The private IP address external mapping for NAT.</td>
</tr>
<tr>
    <td><CopyableCode code="internalMappings" /></td>
    <td><code>array</code></td>
    <td>The private IP address internal mapping for NAT.</td>
</tr>
<tr>
    <td><CopyableCode code="ipConfigurationId" /></td>
    <td><code>string</code></td>
    <td>The IP Configuration ID this NAT rule applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The Source NAT direction of a VPN NAT. Known values are: "EgressSnat" and "IngressSnat". (EgressSnat, IngressSnat)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the NAT Rule resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-nat_rule_name"><code>nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the details of a nat rule.</td>
</tr>
<tr>
    <td><a href="#list_by_virtual_network_gateway"><CopyableCode code="list_by_virtual_network_gateway" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves all nat rules for a particular virtual network gateway.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-nat_rule_name"><code>nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a nat rule to a scalable virtual network gateway if it doesn't exist else updates the existing nat rules.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-nat_rule_name"><code>nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a nat rule to a scalable virtual network gateway if it doesn't exist else updates the existing nat rules.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-virtual_network_gateway_name"><code>virtual_network_gateway_name</code></a>, <a href="#parameter-nat_rule_name"><code>nat_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a nat rule.</td>
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
<tr id="parameter-nat_rule_name">
    <td><CopyableCode code="nat_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
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
<tr id="parameter-virtual_network_gateway_name">
    <td><CopyableCode code="virtual_network_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the virtual network gateway. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_virtual_network_gateway', value: 'list_by_virtual_network_gateway' }
    ]}
>
<TabItem value="get">

Retrieves the details of a nat rule.

```sql
SELECT
id,
name,
etag,
externalMappings,
internalMappings,
ipConfigurationId,
mode,
provisioningState,
type
FROM azure.network.virtual_network_gateway_nat_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' -- required
AND nat_rule_name = '{{ nat_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_virtual_network_gateway">

Retrieves all nat rules for a particular virtual network gateway.

```sql
SELECT
id,
name,
etag,
externalMappings,
internalMappings,
ipConfigurationId,
mode,
provisioningState,
type
FROM azure.network.virtual_network_gateway_nat_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' -- required
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

Creates a nat rule to a scalable virtual network gateway if it doesn't exist else updates the existing nat rules.

```sql
INSERT INTO azure.network.virtual_network_gateway_nat_rules (
id,
name,
properties,
resource_group_name,
virtual_network_gateway_name,
nat_rule_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ virtual_network_gateway_name }}',
'{{ nat_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_network_gateway_nat_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_network_gateway_nat_rules resource.
    - name: virtual_network_gateway_name
      value: "{{ virtual_network_gateway_name }}"
      description: Required parameter for the virtual_network_gateway_nat_rules resource.
    - name: nat_rule_name
      value: "{{ nat_rule_name }}"
      description: Required parameter for the virtual_network_gateway_nat_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_network_gateway_nat_rules resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource.
    - name: properties
      description: |
        Properties of the Virtual Network Gateway NAT rule.
      value:
        provisioningState: "{{ provisioningState }}"
        type: "{{ type }}"
        mode: "{{ mode }}"
        internalMappings:
          - addressSpace: "{{ addressSpace }}"
            portRange: "{{ portRange }}"
        externalMappings:
          - addressSpace: "{{ addressSpace }}"
            portRange: "{{ portRange }}"
        ipConfigurationId: "{{ ipConfigurationId }}"
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

Creates a nat rule to a scalable virtual network gateway if it doesn't exist else updates the existing nat rules.

```sql
REPLACE azure.network.virtual_network_gateway_nat_rules
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' --required
AND nat_rule_name = '{{ nat_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
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

Deletes a nat rule.

```sql
DELETE FROM azure.network.virtual_network_gateway_nat_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND virtual_network_gateway_name = '{{ virtual_network_gateway_name }}' --required
AND nat_rule_name = '{{ nat_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
