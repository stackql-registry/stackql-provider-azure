--- 
title: alert_rule_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_incidents
  - monitor
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

Creates, updates, deletes, gets or lists an <code>alert_rule_incidents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alert_rule_incidents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.alert_rule_incidents" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_alert_rule', value: 'list_by_alert_rule' }
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Incident name.</td>
</tr>
<tr>
    <td><CopyableCode code="activatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the incident was activated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>A boolean to indicate whether the incident is active or resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="resolvedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the incident was resolved in ISO8601 format. If null, it means the incident is still active.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>Rule name that is associated with the incident.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_alert_rule">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Incident name.</td>
</tr>
<tr>
    <td><CopyableCode code="activatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the incident was activated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>A boolean to indicate whether the incident is active or resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="resolvedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the incident was resolved in ISO8601 format. If null, it means the incident is still active.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>Rule name that is associated with the incident.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-incident_name"><code>incident_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an incident associated to an alert rule.</td>
</tr>
<tr>
    <td><a href="#list_by_alert_rule"><CopyableCode code="list_by_alert_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of incidents associated to an alert rule.</td>
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
<tr id="parameter-incident_name">
    <td><CopyableCode code="incident_name" /></td>
    <td><code>string</code></td>
    <td>The name of the incident to retrieve. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the rule. Required.</td>
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
        { label: 'list_by_alert_rule', value: 'list_by_alert_rule' }
    ]}
>
<TabItem value="get">

Gets an incident associated to an alert rule.

```sql
SELECT
name,
activatedTime,
isActive,
resolvedTime,
ruleName
FROM azure.monitor.alert_rule_incidents
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND incident_name = '{{ incident_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_alert_rule">

Gets a list of incidents associated to an alert rule.

```sql
SELECT
name,
activatedTime,
isActive,
resolvedTime,
ruleName
FROM azure.monitor.alert_rule_incidents
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
