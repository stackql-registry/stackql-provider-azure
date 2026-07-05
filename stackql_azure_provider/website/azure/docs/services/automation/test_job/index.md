--- 
title: test_job
hide_title: false
hide_table_of_contents: false
keywords:
  - test_job
  - automation
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

Creates, updates, deletes, gets or lists a <code>test_job</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="test_job" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.test_job" /></td></tr>
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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the creation time of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="exception" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the exception of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last modified time of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastStatusModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the last status modified time of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="logActivityTrace" /></td>
    <td><code>integer</code></td>
    <td>The activity-level tracing options of the runbook.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the parameters of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="runOn" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the runOn which specifies the group name where the job is to be executed.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status of the test job.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status details of the test job.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runbook_name"><code>runbook_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the test job for the specified runbook.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runbook_name"><code>runbook_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a test job of the runbook.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runbook_name"><code>runbook_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resume the test job.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runbook_name"><code>runbook_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop the test job.</td>
</tr>
<tr>
    <td><a href="#suspend"><CopyableCode code="suspend" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-runbook_name"><code>runbook_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Suspend the test job.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-runbook_name">
    <td><CopyableCode code="runbook_name" /></td>
    <td><code>string</code></td>
    <td>The runbook name. Required.</td>
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

Retrieve the test job for the specified runbook.

```sql
SELECT
creationTime,
endTime,
exception,
lastModifiedTime,
lastStatusModifiedTime,
logActivityTrace,
parameters,
runOn,
startTime,
status,
statusDetails
FROM azure.automation.test_job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND runbook_name = '{{ runbook_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a test job of the runbook.

```sql
INSERT INTO azure.automation.test_job (
parameters,
runOn,
runtimeEnvironment,
resource_group_name,
automation_account_name,
runbook_name,
subscription_id
)
SELECT 
'{{ parameters }}',
'{{ runOn }}',
'{{ runtimeEnvironment }}',
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ runbook_name }}',
'{{ subscription_id }}'
RETURNING
creationTime,
endTime,
exception,
lastModifiedTime,
lastStatusModifiedTime,
logActivityTrace,
parameters,
runOn,
startTime,
status,
statusDetails
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: test_job
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the test_job resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the test_job resource.
    - name: runbook_name
      value: "{{ runbook_name }}"
      description: Required parameter for the test_job resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the test_job resource.
    - name: parameters
      value: "{{ parameters }}"
      description: |
        Gets or sets the parameters of the test job.
    - name: runOn
      value: "{{ runOn }}"
      description: |
        Gets or sets the runOn which specifies the group name where the job is to be executed.
    - name: runtimeEnvironment
      value: "{{ runtimeEnvironment }}"
      description: |
        The runtime Environment Name on which job needs to be tested.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resume"
    values={[
        { label: 'resume', value: 'resume' },
        { label: 'stop', value: 'stop' },
        { label: 'suspend', value: 'suspend' }
    ]}
>
<TabItem value="resume">

Resume the test job.

```sql
EXEC azure.automation.test_job.resume 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@runbook_name='{{ runbook_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop the test job.

```sql
EXEC azure.automation.test_job.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@runbook_name='{{ runbook_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="suspend">

Suspend the test job.

```sql
EXEC azure.automation.test_job.suspend 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@runbook_name='{{ runbook_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
