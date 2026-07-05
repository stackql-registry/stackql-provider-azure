--- 
title: iot_security_solutions_analytics_aggregated_alert
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solutions_analytics_aggregated_alert
  - security
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

Creates, updates, deletes, gets or lists an <code>iot_security_solutions_analytics_aggregated_alert</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iot_security_solutions_analytics_aggregated_alert" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solutions_analytics_aggregated_alert" /></td></tr>
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
    <td><CopyableCode code="actionTaken" /></td>
    <td><code>string</code></td>
    <td>IoT Security solution alert response.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregatedDateUtc" /></td>
    <td><code>string (date)</code></td>
    <td>Date of detection.</td>
</tr>
<tr>
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the alert type.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Name of the alert type.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of alerts occurrences within the aggregated time window.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspected vulnerability and meaning.</td>
</tr>
<tr>
    <td><CopyableCode code="effectedResourceType" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the resource that received the alerts.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsQuery" /></td>
    <td><code>string</code></td>
    <td>Log analytics query for getting the list of affected devices/alerts.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>string</code></td>
    <td>Recommended steps for remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedSeverity" /></td>
    <td><code>string</code></td>
    <td>Assessed alert severity. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSource" /></td>
    <td><code>string</code></td>
    <td>The type of the alerted resource (Azure, Non-Azure).</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="topDevicesList" /></td>
    <td><code>array</code></td>
    <td>10 devices with the highest number of occurrences of this alert type, on this day.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>Name of the organization that raised the alert.</td>
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
    <td><CopyableCode code="actionTaken" /></td>
    <td><code>string</code></td>
    <td>IoT Security solution alert response.</td>
</tr>
<tr>
    <td><CopyableCode code="aggregatedDateUtc" /></td>
    <td><code>string (date)</code></td>
    <td>Date of detection.</td>
</tr>
<tr>
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the alert type.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Name of the alert type.</td>
</tr>
<tr>
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of alerts occurrences within the aggregated time window.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspected vulnerability and meaning.</td>
</tr>
<tr>
    <td><CopyableCode code="effectedResourceType" /></td>
    <td><code>string</code></td>
    <td>Azure resource ID of the resource that received the alerts.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsQuery" /></td>
    <td><code>string</code></td>
    <td>Log analytics query for getting the list of affected devices/alerts.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>string</code></td>
    <td>Recommended steps for remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedSeverity" /></td>
    <td><code>string</code></td>
    <td>Assessed alert severity. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSource" /></td>
    <td><code>string</code></td>
    <td>The type of the alerted resource (Azure, Non-Azure).</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="topDevicesList" /></td>
    <td><code>array</code></td>
    <td>10 devices with the highest number of occurrences of this alert type, on this day.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>Name of the organization that raised the alert.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-aggregated_alert_name"><code>aggregated_alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Use this method to get the aggregated alert list of yours IoT Security solution.</td>
</tr>
<tr>
    <td><a href="#dismiss"><CopyableCode code="dismiss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_name"><code>solution_name</code></a>, <a href="#parameter-aggregated_alert_name"><code>aggregated_alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Use this method to dismiss an aggregated IoT Security Solution Alert.</td>
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
<tr id="parameter-aggregated_alert_name">
    <td><CopyableCode code="aggregated_alert_name" /></td>
    <td><code>string</code></td>
    <td>Identifier of the aggregated alert. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-solution_name">
    <td><CopyableCode code="solution_name" /></td>
    <td><code>string</code></td>
    <td>The name of the IoT Security solution. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of results to retrieve. Default value is None.</td>
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

Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name.

```sql
SELECT
id,
name,
actionTaken,
aggregatedDateUtc,
alertDisplayName,
alertType,
count,
description,
effectedResourceType,
logAnalyticsQuery,
remediationSteps,
reportedSeverity,
systemData,
systemSource,
tags,
topDevicesList,
type,
vendorName
FROM azure.security.iot_security_solutions_analytics_aggregated_alert
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND solution_name = '{{ solution_name }}' -- required
AND aggregated_alert_name = '{{ aggregated_alert_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Use this method to get the aggregated alert list of yours IoT Security solution.

```sql
SELECT
id,
name,
actionTaken,
aggregatedDateUtc,
alertDisplayName,
alertType,
count,
description,
effectedResourceType,
logAnalyticsQuery,
remediationSteps,
reportedSeverity,
systemData,
systemSource,
tags,
topDevicesList,
type,
vendorName
FROM azure.security.iot_security_solutions_analytics_aggregated_alert
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND solution_name = '{{ solution_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="dismiss"
    values={[
        { label: 'dismiss', value: 'dismiss' }
    ]}
>
<TabItem value="dismiss">

Use this method to dismiss an aggregated IoT Security Solution Alert.

```sql
EXEC azure.security.iot_security_solutions_analytics_aggregated_alert.dismiss 
@resource_group_name='{{ resource_group_name }}' --required, 
@solution_name='{{ solution_name }}' --required, 
@aggregated_alert_name='{{ aggregated_alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
