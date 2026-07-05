--- 
title: inbound_security_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_security_rule
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

Creates, updates, deletes, gets or lists an <code>inbound_security_rule</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="inbound_security_rule" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.inbound_security_rule" /></td></tr>
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleType" /></td>
    <td><code>string</code></td>
    <td>Rule Type. This should be either AutoExpire or Permanent. Auto Expire Rule only creates NSG rules. Permanent Rule creates NSG rule and SLB LB Rule. Known values are: "AutoExpire" and "Permanent". (AutoExpire, Permanent)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>List of allowed rules.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-rule_collection_name"><code>rule_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the available specified Network Virtual Appliance Inbound Security Rules Collection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-rule_collection_name"><code>rule_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Network Virtual Appliance Inbound Security Rules.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_virtual_appliance_name"><code>network_virtual_appliance_name</code></a>, <a href="#parameter-rule_collection_name"><code>rule_collection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Network Virtual Appliance Inbound Security Rules.</td>
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
<tr id="parameter-network_virtual_appliance_name">
    <td><CopyableCode code="network_virtual_appliance_name" /></td>
    <td><code>string</code></td>
    <td>The name of Network Virtual Appliance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rule_collection_name">
    <td><CopyableCode code="rule_collection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource that is unique within a resource group. This name can be used to access the resource. Required.</td>
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

Retrieves the available specified Network Virtual Appliance Inbound Security Rules Collection.

```sql
SELECT
id,
name,
etag,
provisioningState,
ruleType,
rules,
type
FROM azure.network.inbound_security_rule
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' -- required
AND rule_collection_name = '{{ rule_collection_name }}' -- required
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

Creates or updates the specified Network Virtual Appliance Inbound Security Rules.

```sql
INSERT INTO azure.network.inbound_security_rule (
id,
name,
properties,
resource_group_name,
network_virtual_appliance_name,
rule_collection_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_virtual_appliance_name }}',
'{{ rule_collection_name }}',
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
- name: inbound_security_rule
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the inbound_security_rule resource.
    - name: network_virtual_appliance_name
      value: "{{ network_virtual_appliance_name }}"
      description: Required parameter for the inbound_security_rule resource.
    - name: rule_collection_name
      value: "{{ rule_collection_name }}"
      description: Required parameter for the inbound_security_rule resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the inbound_security_rule resource.
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
        The properties of the Inbound Security Rules.
      value:
        ruleType: "{{ ruleType }}"
        rules:
          - name: "{{ name }}"
            protocol: "{{ protocol }}"
            sourceAddressPrefix: "{{ sourceAddressPrefix }}"
            destinationPortRange: {{ destinationPortRange }}
            destinationPortRanges: "{{ destinationPortRanges }}"
            appliesOn: "{{ appliesOn }}"
        provisioningState: "{{ provisioningState }}"
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

Creates or updates the specified Network Virtual Appliance Inbound Security Rules.

```sql
REPLACE azure.network.inbound_security_rule
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_virtual_appliance_name = '{{ network_virtual_appliance_name }}' --required
AND rule_collection_name = '{{ rule_collection_name }}' --required
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
