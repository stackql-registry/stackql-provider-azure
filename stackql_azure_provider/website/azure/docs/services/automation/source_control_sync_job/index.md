--- 
title: source_control_sync_job
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_job
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

Creates, updates, deletes, gets or lists a <code>source_control_sync_job</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="source_control_sync_job" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control_sync_job" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
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
    <td>The id of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="exception" /></td>
    <td><code>string</code></td>
    <td>The exceptions that occurred while running the sync job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the job. Known values are: "Completed", "Failed", and "Running". (Completed, Failed, Running)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceControlSyncJobId" /></td>
    <td><code>string</code></td>
    <td>The source control sync job id.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="syncType" /></td>
    <td><code>string</code></td>
    <td>The sync type. Known values are: "PartialSync" and "FullSync". (PartialSync, FullSync)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_automation_account">

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
    <td>Resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the job. Known values are: "Completed", "Failed", and "Running". (Completed, Failed, Running)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceControlSyncJobId" /></td>
    <td><code>string</code></td>
    <td>The source control sync job id.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="syncType" /></td>
    <td><code>string</code></td>
    <td>The sync type. Known values are: "PartialSync" and "FullSync". (PartialSync, FullSync)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-source_control_sync_job_id"><code>source_control_sync_job_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the source control sync job identified by job id.</td>
</tr>
<tr>
    <td><a href="#list_by_automation_account"><CopyableCode code="list_by_automation_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieve a list of source control sync jobs.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-source_control_name"><code>source_control_name</code></a>, <a href="#parameter-source_control_sync_job_id"><code>source_control_sync_job_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates the sync job for a source control.</td>
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
<tr id="parameter-source_control_name">
    <td><CopyableCode code="source_control_name" /></td>
    <td><code>string</code></td>
    <td>The name of source control. Required.</td>
</tr>
<tr id="parameter-source_control_sync_job_id">
    <td><CopyableCode code="source_control_sync_job_id" /></td>
    <td><code>string</code></td>
    <td>The source control sync job id. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_automation_account', value: 'list_by_automation_account' }
    ]}
>
<TabItem value="get">

Retrieve the source control sync job identified by job id.

```sql
SELECT
id,
creationTime,
endTime,
exception,
provisioningState,
sourceControlSyncJobId,
startTime,
syncType
FROM azure.automation.source_control_sync_job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND source_control_name = '{{ source_control_name }}' -- required
AND source_control_sync_job_id = '{{ source_control_sync_job_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_automation_account">

Retrieve a list of source control sync jobs.

```sql
SELECT
id,
name,
creationTime,
endTime,
provisioningState,
sourceControlSyncJobId,
startTime,
syncType,
type
FROM azure.automation.source_control_sync_job
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND source_control_name = '{{ source_control_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Creates the sync job for a source control.

```sql
INSERT INTO azure.automation.source_control_sync_job (
properties,
resource_group_name,
automation_account_name,
source_control_name,
source_control_sync_job_id,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ source_control_name }}',
'{{ source_control_sync_job_id }}',
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
- name: source_control_sync_job
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the source_control_sync_job resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the source_control_sync_job resource.
    - name: source_control_name
      value: "{{ source_control_name }}"
      description: Required parameter for the source_control_sync_job resource.
    - name: source_control_sync_job_id
      value: "{{ source_control_sync_job_id }}"
      description: Required parameter for the source_control_sync_job resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the source_control_sync_job resource.
    - name: properties
      description: |
        The properties of the source control sync job. Required.
      value:
        commitId: "{{ commitId }}"
`}</CodeBlock>

</TabItem>
</Tabs>
