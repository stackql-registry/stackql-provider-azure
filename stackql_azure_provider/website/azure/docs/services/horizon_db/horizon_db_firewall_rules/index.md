--- 
title: horizon_db_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - horizon_db_firewall_rules
  - horizon_db
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

Creates, updates, deletes, gets or lists a <code>horizon_db_firewall_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="horizon_db_firewall_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.horizon_db.horizon_db_firewall_rules" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the HorizonDb firewall rule.</td>
</tr>
<tr>
    <td><CopyableCode code="endIpAddress" /></td>
    <td><code>string</code></td>
    <td>The end IP address of the firewall rule (IPv4). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the firewall rule. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Provisioning". (Succeeded, Failed, Canceled, InProgress, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="startIpAddress" /></td>
    <td><code>string</code></td>
    <td>The start IP address of the firewall rule (IPv4). Required.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the HorizonDb firewall rule.</td>
</tr>
<tr>
    <td><CopyableCode code="endIpAddress" /></td>
    <td><code>string</code></td>
    <td>The end IP address of the firewall rule (IPv4). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the firewall rule. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Provisioning". (Succeeded, Failed, Canceled, InProgress, Provisioning)</td>
</tr>
<tr>
    <td><CopyableCode code="startIpAddress" /></td>
    <td><code>string</code></td>
    <td>The start IP address of the firewall rule (IPv4). Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-firewall_rule_name"><code>firewall_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a HorizonDb firewall rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all HorizonDb firewall rules in a pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-firewall_rule_name"><code>firewall_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new HorizonDb firewall rule or updates an existing rule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-firewall_rule_name"><code>firewall_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new HorizonDb firewall rule or updates an existing rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-firewall_rule_name"><code>firewall_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a HorizonDb firewall rule.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the HorizonDb cluster. Required.</td>
</tr>
<tr id="parameter-firewall_rule_name">
    <td><CopyableCode code="firewall_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the HorizonDb firewall rule. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the HorizonDb pool. Required.</td>
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

Gets information about a HorizonDb firewall rule.

```sql
SELECT
id,
name,
description,
endIpAddress,
provisioningState,
startIpAddress,
systemData,
type
FROM azure.horizon_db.horizon_db_firewall_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND firewall_rule_name = '{{ firewall_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all HorizonDb firewall rules in a pool.

```sql
SELECT
id,
name,
description,
endIpAddress,
provisioningState,
startIpAddress,
systemData,
type
FROM azure.horizon_db.horizon_db_firewall_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
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

Creates a new HorizonDb firewall rule or updates an existing rule.

```sql
INSERT INTO azure.horizon_db.horizon_db_firewall_rules (
properties,
resource_group_name,
cluster_name,
pool_name,
firewall_rule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ pool_name }}',
'{{ firewall_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: horizon_db_firewall_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the horizon_db_firewall_rules resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the horizon_db_firewall_rules resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the horizon_db_firewall_rules resource.
    - name: firewall_rule_name
      value: "{{ firewall_rule_name }}"
      description: Required parameter for the horizon_db_firewall_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the horizon_db_firewall_rules resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        startIpAddress: "{{ startIpAddress }}"
        endIpAddress: "{{ endIpAddress }}"
        description: "{{ description }}"
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

Creates a new HorizonDb firewall rule or updates an existing rule.

```sql
REPLACE azure.horizon_db.horizon_db_firewall_rules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND firewall_rule_name = '{{ firewall_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Deletes a HorizonDb firewall rule.

```sql
DELETE FROM azure.horizon_db.horizon_db_firewall_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND firewall_rule_name = '{{ firewall_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
