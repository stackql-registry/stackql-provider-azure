--- 
title: firewall_policy_rule_collection_group_drafts
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_rule_collection_group_drafts
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_rule_collection_group_drafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_policy_rule_collection_group_drafts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_rule_collection_group_drafts" /></td></tr>
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
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of the Firewall Policy Rule Collection Group resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleCollections" /></td>
    <td><code>array</code></td>
    <td>Group of Firewall Policy rule collections.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>A read-only string that represents the size of the FirewallPolicyRuleCollectionGroupProperties in MB. (ex 1.2MB).</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-rule_collection_group_name"><code>rule_collection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Rule Collection Group Draft.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-rule_collection_group_name"><code>rule_collection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update Rule Collection Group Draft.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-rule_collection_group_name"><code>rule_collection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update Rule Collection Group Draft.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-rule_collection_group_name"><code>rule_collection_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Rule Collection Group Draft.</td>
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
<tr id="parameter-firewall_policy_name">
    <td><CopyableCode code="firewall_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Firewall Policy. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rule_collection_group_name">
    <td><CopyableCode code="rule_collection_group_name" /></td>
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

Get Rule Collection Group Draft.

```sql
SELECT
id,
name,
priority,
ruleCollections,
size,
type
FROM azure.network.firewall_policy_rule_collection_group_drafts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND firewall_policy_name = '{{ firewall_policy_name }}' -- required
AND rule_collection_group_name = '{{ rule_collection_group_name }}' -- required
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

Create or Update Rule Collection Group Draft.

```sql
INSERT INTO azure.network.firewall_policy_rule_collection_group_drafts (
id,
name,
properties,
resource_group_name,
firewall_policy_name,
rule_collection_group_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ firewall_policy_name }}',
'{{ rule_collection_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: firewall_policy_rule_collection_group_drafts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the firewall_policy_rule_collection_group_drafts resource.
    - name: firewall_policy_name
      value: "{{ firewall_policy_name }}"
      description: Required parameter for the firewall_policy_rule_collection_group_drafts resource.
    - name: rule_collection_group_name
      value: "{{ rule_collection_group_name }}"
      description: Required parameter for the firewall_policy_rule_collection_group_drafts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the firewall_policy_rule_collection_group_drafts resource.
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
        The properties of the firewall policy rule collection group.
      value:
        size: "{{ size }}"
        priority: {{ priority }}
        ruleCollections:
          - ruleCollectionType: "{{ ruleCollectionType }}"
            name: "{{ name }}"
            priority: {{ priority }}
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

Create or Update Rule Collection Group Draft.

```sql
REPLACE azure.network.firewall_policy_rule_collection_group_drafts
SET 
id = '{{ id }}',
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND rule_collection_group_name = '{{ rule_collection_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete Rule Collection Group Draft.

```sql
DELETE FROM azure.network.firewall_policy_rule_collection_group_drafts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND rule_collection_group_name = '{{ rule_collection_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
