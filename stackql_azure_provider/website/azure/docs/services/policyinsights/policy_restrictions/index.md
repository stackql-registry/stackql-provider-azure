--- 
title: policy_restrictions
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_restrictions
  - policyinsights
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

Creates, updates, deletes, gets or lists a <code>policy_restrictions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_restrictions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.policyinsights.policy_restrictions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#check_at_subscription_scope"><CopyableCode code="check_at_subscription_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceDetails"><code>resourceDetails</code></a></td>
    <td></td>
    <td>Checks what restrictions Azure Policy will place on a resource within a subscription.</td>
</tr>
<tr>
    <td><a href="#check_at_resource_group_scope"><CopyableCode code="check_at_resource_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resourceDetails"><code>resourceDetails</code></a></td>
    <td></td>
    <td>Checks what restrictions Azure Policy will place on a resource within a resource group. Use this when the resource group the resource will be created in is already known.</td>
</tr>
<tr>
    <td><a href="#check_at_management_group_scope"><CopyableCode code="check_at_management_group_scope" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a></td>
    <td></td>
    <td>Checks what restrictions Azure Policy will place on resources within a management group.</td>
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
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>Management group ID. Required.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="check_at_subscription_scope"
    values={[
        { label: 'check_at_subscription_scope', value: 'check_at_subscription_scope' },
        { label: 'check_at_resource_group_scope', value: 'check_at_resource_group_scope' },
        { label: 'check_at_management_group_scope', value: 'check_at_management_group_scope' }
    ]}
>
<TabItem value="check_at_subscription_scope">

Checks what restrictions Azure Policy will place on a resource within a subscription.

```sql
EXEC azure.policyinsights.policy_restrictions.check_at_subscription_scope 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceDetails": "{{ resourceDetails }}", 
"pendingFields": "{{ pendingFields }}", 
"includeAuditEffect": {{ includeAuditEffect }}
}'
;
```
</TabItem>
<TabItem value="check_at_resource_group_scope">

Checks what restrictions Azure Policy will place on a resource within a resource group. Use this when the resource group the resource will be created in is already known.

```sql
EXEC azure.policyinsights.policy_restrictions.check_at_resource_group_scope 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resourceDetails": "{{ resourceDetails }}", 
"pendingFields": "{{ pendingFields }}", 
"includeAuditEffect": {{ includeAuditEffect }}
}'
;
```
</TabItem>
<TabItem value="check_at_management_group_scope">

Checks what restrictions Azure Policy will place on resources within a management group.

```sql
EXEC azure.policyinsights.policy_restrictions.check_at_management_group_scope 
@management_group_id='{{ management_group_id }}' --required 
@@json=
'{
"resourceDetails": "{{ resourceDetails }}", 
"pendingFields": "{{ pendingFields }}"
}'
;
```
</TabItem>
</Tabs>
