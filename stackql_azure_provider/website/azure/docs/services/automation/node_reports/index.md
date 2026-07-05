--- 
title: node_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - node_reports
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

Creates, updates, deletes, gets or lists a <code>node_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.node_reports" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_node', value: 'list_by_node' }
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
    <td>Gets or sets the id.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the configurationVersion of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the errors for the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the hostname of the node that sent the report.</td>
</tr>
<tr>
    <td><CopyableCode code="iPV4Addresses" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the IPv4 address of the node that sent the report.</td>
</tr>
<tr>
    <td><CopyableCode code="iPV6Addresses" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the IPv6 address of the node that sent the report.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the lastModifiedTime of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="metaConfiguration" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the metaConfiguration of the node at the time of the report.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfResources" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of resource in the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="rawErrors" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the unparsed errors for the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="rebootRequested" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the rebootRequested of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="refreshMode" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the refreshMode of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="reportFormatVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the reportFormatVersion of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="reportId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the id of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the resource for the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the node report.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_node">

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
    <td>Gets or sets the id.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the configurationVersion of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the errors for the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the hostname of the node that sent the report.</td>
</tr>
<tr>
    <td><CopyableCode code="iPV4Addresses" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the IPv4 address of the node that sent the report.</td>
</tr>
<tr>
    <td><CopyableCode code="iPV6Addresses" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the IPv6 address of the node that sent the report.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the lastModifiedTime of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="metaConfiguration" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the metaConfiguration of the node at the time of the report.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfResources" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the number of resource in the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="rawErrors" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the unparsed errors for the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="rebootRequested" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the rebootRequested of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="refreshMode" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the refreshMode of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="reportFormatVersion" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the reportFormatVersion of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="reportId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the id of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the resource for the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the status of the node report.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the type of the node report.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-report_id"><code>report_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the Dsc node report data by node id and report id.</td>
</tr>
<tr>
    <td><a href="#list_by_node"><CopyableCode code="list_by_node" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieve the Dsc node report list by node id.</td>
</tr>
<tr>
    <td><a href="#get_content"><CopyableCode code="get_content" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-report_id"><code>report_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the Dsc node reports by node id and report id.</td>
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
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The node id. Required.</td>
</tr>
<tr id="parameter-report_id">
    <td><CopyableCode code="report_id" /></td>
    <td><code>string</code></td>
    <td>The report id. Required.</td>
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
        { label: 'list_by_node', value: 'list_by_node' }
    ]}
>
<TabItem value="get">

Retrieve the Dsc node report data by node id and report id.

```sql
SELECT
id,
configurationVersion,
endTime,
errors,
hostName,
iPV4Addresses,
iPV6Addresses,
lastModifiedTime,
metaConfiguration,
numberOfResources,
rawErrors,
rebootRequested,
refreshMode,
reportFormatVersion,
reportId,
resources,
startTime,
status,
type
FROM azure.automation.node_reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND node_id = '{{ node_id }}' -- required
AND report_id = '{{ report_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_node">

Retrieve the Dsc node report list by node id.

```sql
SELECT
id,
configurationVersion,
endTime,
errors,
hostName,
iPV4Addresses,
iPV6Addresses,
lastModifiedTime,
metaConfiguration,
numberOfResources,
rawErrors,
rebootRequested,
refreshMode,
reportFormatVersion,
reportId,
resources,
startTime,
status,
type
FROM azure.automation.node_reports
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND node_id = '{{ node_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_content"
    values={[
        { label: 'get_content', value: 'get_content' }
    ]}
>
<TabItem value="get_content">

Retrieve the Dsc node reports by node id and report id.

```sql
EXEC azure.automation.node_reports.get_content 
@resource_group_name='{{ resource_group_name }}' --required, 
@automation_account_name='{{ automation_account_name }}' --required, 
@node_id='{{ node_id }}' --required, 
@report_id='{{ report_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
