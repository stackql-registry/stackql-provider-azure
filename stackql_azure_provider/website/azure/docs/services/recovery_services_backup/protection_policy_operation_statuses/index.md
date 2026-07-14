--- 
title: protection_policy_operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_policy_operation_statuses
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>protection_policy_operation_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protection_policy_operation_statuses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protection_policy_operation_statuses" /></td></tr>
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
    <td>ID of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Operation end time. Format: ISO-8601.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error information related to this operation.</td>
</tr>
<tr>
    <td><CopyableCode code="objectType" /></td>
    <td><code>string</code></td>
    <td>This property will be used as the discriminator for deciding the specific types in the polymorphic chain of types. Required. Default value is None.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Operation start time. Format: ISO-8601.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Known values are: "Invalid", "InProgress", "Succeeded", "Failed", and "Canceled". (Invalid, InProgress, Succeeded, Failed, Canceled)</td>
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
    <td><a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Provides the status of the asynchronous operations like backup, restore. The status can be in progress, completed or failed. You can refer to the Operation Status enum for all the possible states of an operation. Some operations create jobs. This method returns the list of jobs associated with operation.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The name of the ProtectionPolicyResource. Required.</td>
</tr>
<tr id="parameter-policy_name">
    <td><CopyableCode code="policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ProtectionPolicyResource. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>vaults. Required.</td>
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

Provides the status of the asynchronous operations like backup, restore. The status can be in progress, completed or failed. You can refer to the Operation Status enum for all the possible states of an operation. Some operations create jobs. This method returns the list of jobs associated with operation.

```sql
SELECT
id,
name,
endTime,
error,
objectType,
startTime,
status
FROM azure.recovery_services_backup.protection_policy_operation_statuses
WHERE vault_name = '{{ vault_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND policy_name = '{{ policy_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
