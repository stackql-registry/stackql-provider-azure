--- 
title: software_update_configuration_machine_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configuration_machine_runs
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

Creates, updates, deletes, gets or lists a <code>software_update_configuration_machine_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="software_update_configuration_machine_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.software_update_configuration_machine_runs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

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
    <td>Resource Id of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="configuredDuration" /></td>
    <td><code>string</code></td>
    <td>configured duration for the software update configuration run.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>correlation id of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>createdBy property, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the resource, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Details of provisioning error.</td>
</tr>
<tr>
    <td><CopyableCode code="job" /></td>
    <td><code>object</code></td>
    <td>Job associated with the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>lastModifiedBy property, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time resource was modified, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Operating system target of the software update configuration triggered this run.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareUpdateConfiguration" /></td>
    <td><code>object</code></td>
    <td>software update configuration triggered this run.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceComputerId" /></td>
    <td><code>string</code></td>
    <td>source computer id of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="targetComputer" /></td>
    <td><code>string</code></td>
    <td>name of the updated computer.</td>
</tr>
<tr>
    <td><CopyableCode code="targetComputerType" /></td>
    <td><code>string</code></td>
    <td>type of the updated computer.</td>
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
    <td>Resource Id of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="configuredDuration" /></td>
    <td><code>string</code></td>
    <td>configured duration for the software update configuration run.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>correlation id of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>createdBy property, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the resource, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Details of provisioning error.</td>
</tr>
<tr>
    <td><CopyableCode code="job" /></td>
    <td><code>object</code></td>
    <td>Job associated with the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>lastModifiedBy property, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time resource was modified, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Operating system target of the software update configuration triggered this run.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareUpdateConfiguration" /></td>
    <td><code>object</code></td>
    <td>software update configuration triggered this run.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceComputerId" /></td>
    <td><code>string</code></td>
    <td>source computer id of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the software update configuration machine run.</td>
</tr>
<tr>
    <td><CopyableCode code="targetComputer" /></td>
    <td><code>string</code></td>
    <td>name of the updated computer.</td>
</tr>
<tr>
    <td><CopyableCode code="targetComputerType" /></td>
    <td><code>string</code></td>
    <td>type of the updated computer.</td>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-software_update_configuration_machine_run_id"><code>software_update_configuration_machine_run_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Get a single software update configuration machine run by Id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Return list of software update configuration machine runs.</td>
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
<tr id="parameter-software_update_configuration_machine_run_id">
    <td><CopyableCode code="software_update_configuration_machine_run_id" /></td>
    <td><code>string</code></td>
    <td>The Id of the software update configuration machine run. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. You can use the following filters: 'properties/osType', 'properties/status', 'properties/startTime', and 'properties/softwareUpdateConfiguration/name'. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>string</code></td>
    <td>number of entries you skip before returning results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>string</code></td>
    <td>Maximum number of entries returned in the results collection. Default value is None.</td>
</tr>
<tr id="parameter-clientRequestId">
    <td><CopyableCode code="clientRequestId" /></td>
    <td><code>string</code></td>
    <td>Identifies this specific client request. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_id">

Get a single software update configuration machine run by Id.

```sql
SELECT
id,
name,
configuredDuration,
correlationId,
createdBy,
creationTime,
endTime,
error,
job,
lastModifiedBy,
lastModifiedTime,
osType,
softwareUpdateConfiguration,
sourceComputerId,
startTime,
status,
targetComputer,
targetComputerType
FROM azure.automation.software_update_configuration_machine_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND software_update_configuration_machine_run_id = '{{ software_update_configuration_machine_run_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND clientRequestId = '{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="list">

Return list of software update configuration machine runs.

```sql
SELECT
id,
name,
configuredDuration,
correlationId,
createdBy,
creationTime,
endTime,
error,
job,
lastModifiedBy,
lastModifiedTime,
osType,
softwareUpdateConfiguration,
sourceComputerId,
startTime,
status,
targetComputer,
targetComputerType
FROM azure.automation.software_update_configuration_machine_runs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND clientRequestId = '{{ clientRequestId }}'
AND $filter = '{{ $filter }}'
AND $skip = '{{ $skip }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>
