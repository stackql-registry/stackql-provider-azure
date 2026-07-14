--- 
title: recovery_plan_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_plan_actions
  - resilience_management
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

Creates, updates, deletes, gets or lists a <code>recovery_plan_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recovery_plan_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resilience_management.recovery_plan_actions" /></td></tr>
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
    <td><a href="#finalize"><CopyableCode code="finalize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action finalizes the recovery orchestration plan, ensuring all necessary configurations are in place.</td>
</tr>
<tr>
    <td><a href="#update_resources"><CopyableCode code="update_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action adds or updates the resources to be included in the recovery orchestration plan.</td>
</tr>
<tr>
    <td><a href="#validate_for_operation"><CopyableCode code="validate_for_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-operationName"><code>operationName</code></a></td>
    <td></td>
    <td>This action checks if the recovery orchestration plan is eligible for operations like failover and reprotect, ensuring it meets the necessary criteria.</td>
</tr>
<tr>
    <td><a href="#validate_for_failover"><CopyableCode code="validate_for_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-failoverDirection"><code>failoverDirection</code></a></td>
    <td></td>
    <td>This action checks if the recovery orchestration plan is eligible for failover operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.</td>
</tr>
<tr>
    <td><a href="#validate_for_failover_commit"><CopyableCode code="validate_for_failover_commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action checks if the recovery orchestration plan is eligible for failover commit operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.</td>
</tr>
<tr>
    <td><a href="#validate_for_test_failover"><CopyableCode code="validate_for_test_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-failoverDirection"><code>failoverDirection</code></a></td>
    <td></td>
    <td>This action checks if the recovery orchestration plan is eligible for test failover operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.</td>
</tr>
<tr>
    <td><a href="#validate_for_test_failover_cleanup"><CopyableCode code="validate_for_test_failover_cleanup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action checks if the recovery orchestration plan is eligible for test failover cleanup operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.</td>
</tr>
<tr>
    <td><a href="#validate_for_reprotect"><CopyableCode code="validate_for_reprotect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action checks if the recovery orchestration plan is eligible for reprotect operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.</td>
</tr>
<tr>
    <td><a href="#check_readiness"><CopyableCode code="check_readiness" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action performs the necessary readiness check on the recovery orchestration plan to ensure it is in the desired state and eligible for all recovery actions, including all protected resources.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-failoverDirection"><code>failoverDirection</code></a></td>
    <td></td>
    <td>This action triggers the failover operation on the recovery orchestration plan for the qualified resources.</td>
</tr>
<tr>
    <td><a href="#failover_commit"><CopyableCode code="failover_commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action triggers the failover commit operation on the recovery orchestration plan for the qualified resources.</td>
</tr>
<tr>
    <td><a href="#reprotect"><CopyableCode code="reprotect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action triggers the reprotect operation on the recovery orchestration plan for the qualified resources.</td>
</tr>
<tr>
    <td><a href="#test_failover"><CopyableCode code="test_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a>, <a href="#parameter-failoverDirection"><code>failoverDirection</code></a></td>
    <td></td>
    <td>This action triggers the test failover operation on the recovery orchestration plan for the qualified resources.</td>
</tr>
<tr>
    <td><a href="#test_failover_cleanup"><CopyableCode code="test_failover_cleanup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-recovery_plan_name"><code>recovery_plan_name</code></a>, <a href="#parameter-operation-id"><code>operation-id</code></a></td>
    <td></td>
    <td>This action triggers the test failover cleanup operation on the recovery orchestration plan for the qualified resources.</td>
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
<tr id="parameter-operation-id">
    <td><CopyableCode code="operation-id" /></td>
    <td><code>string</code></td>
    <td>A GUID that represents the Long Running OperationId. Required.</td>
</tr>
<tr id="parameter-recovery_plan_name">
    <td><CopyableCode code="recovery_plan_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery orchestration plan. Required.</td>
</tr>
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="finalize"
    values={[
        { label: 'finalize', value: 'finalize' },
        { label: 'update_resources', value: 'update_resources' },
        { label: 'validate_for_operation', value: 'validate_for_operation' },
        { label: 'validate_for_failover', value: 'validate_for_failover' },
        { label: 'validate_for_failover_commit', value: 'validate_for_failover_commit' },
        { label: 'validate_for_test_failover', value: 'validate_for_test_failover' },
        { label: 'validate_for_test_failover_cleanup', value: 'validate_for_test_failover_cleanup' },
        { label: 'validate_for_reprotect', value: 'validate_for_reprotect' },
        { label: 'check_readiness', value: 'check_readiness' },
        { label: 'failover', value: 'failover' },
        { label: 'failover_commit', value: 'failover_commit' },
        { label: 'reprotect', value: 'reprotect' },
        { label: 'test_failover', value: 'test_failover' },
        { label: 'test_failover_cleanup', value: 'test_failover_cleanup' }
    ]}
>
<TabItem value="finalize">

This action finalizes the recovery orchestration plan, ensuring all necessary configurations are in place.

```sql
EXEC azure.resilience_management.recovery_plan_actions.finalize 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="update_resources">

This action adds or updates the resources to be included in the recovery orchestration plan.

```sql
EXEC azure.resilience_management.recovery_plan_actions.update_resources 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"resourcesToUpdate": "{{ resourcesToUpdate }}", 
"resourcesToRemove": "{{ resourcesToRemove }}"
}'
;
```
</TabItem>
<TabItem value="validate_for_operation">

This action checks if the recovery orchestration plan is eligible for operations like failover and reprotect, ensuring it meets the necessary criteria.

```sql
EXEC azure.resilience_management.recovery_plan_actions.validate_for_operation 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"operationName": "{{ operationName }}"
}'
;
```
</TabItem>
<TabItem value="validate_for_failover">

This action checks if the recovery orchestration plan is eligible for failover operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.validate_for_failover 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"failoverDirection": "{{ failoverDirection }}", 
"failoverRequestProperties": "{{ failoverRequestProperties }}"
}'
;
```
</TabItem>
<TabItem value="validate_for_failover_commit">

This action checks if the recovery orchestration plan is eligible for failover commit operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.validate_for_failover_commit 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="validate_for_test_failover">

This action checks if the recovery orchestration plan is eligible for test failover operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.validate_for_test_failover 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"failoverDirection": "{{ failoverDirection }}", 
"failoverRequestProperties": "{{ failoverRequestProperties }}"
}'
;
```
</TabItem>
<TabItem value="validate_for_test_failover_cleanup">

This action checks if the recovery orchestration plan is eligible for test failover cleanup operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.validate_for_test_failover_cleanup 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="validate_for_reprotect">

This action checks if the recovery orchestration plan is eligible for reprotect operation, ensuring it meets the necessary criteria and provides a list of qualified and unqualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.validate_for_reprotect 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"reprotectRequestProperties": "{{ reprotectRequestProperties }}"
}'
;
```
</TabItem>
<TabItem value="check_readiness">

This action performs the necessary readiness check on the recovery orchestration plan to ensure it is in the desired state and eligible for all recovery actions, including all protected resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.check_readiness 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="failover">

This action triggers the failover operation on the recovery orchestration plan for the qualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.failover 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"failoverDirection": "{{ failoverDirection }}", 
"failoverRequestProperties": "{{ failoverRequestProperties }}"
}'
;
```
</TabItem>
<TabItem value="failover_commit">

This action triggers the failover commit operation on the recovery orchestration plan for the qualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.failover_commit 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required
;
```
</TabItem>
<TabItem value="reprotect">

This action triggers the reprotect operation on the recovery orchestration plan for the qualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.reprotect 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"reprotectRequestProperties": "{{ reprotectRequestProperties }}"
}'
;
```
</TabItem>
<TabItem value="test_failover">

This action triggers the test failover operation on the recovery orchestration plan for the qualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.test_failover 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"failoverDirection": "{{ failoverDirection }}", 
"failoverRequestProperties": "{{ failoverRequestProperties }}"
}'
;
```
</TabItem>
<TabItem value="test_failover_cleanup">

This action triggers the test failover cleanup operation on the recovery orchestration plan for the qualified resources.

```sql
EXEC azure.resilience_management.recovery_plan_actions.test_failover_cleanup 
@service_group_name='{{ service_group_name }}' --required, 
@recovery_plan_name='{{ recovery_plan_name }}' --required, 
@operation-id='{{ operation-id }}' --required 
@@json=
'{
"comments": "{{ comments }}"
}'
;
```
</TabItem>
</Tabs>
