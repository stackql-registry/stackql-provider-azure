--- 
title: proactive_detection_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - proactive_detection_configurations
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>proactive_detection_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="proactive_detection_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.proactive_detection_configurations" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The rule name.</td>
</tr>
<tr>
    <td><CopyableCode code="customEmails" /></td>
    <td><code>array</code></td>
    <td>Custom email addresses for this rule notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates whether this rule is enabled by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string</code></td>
    <td>The last time this rule was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleDefinitions" /></td>
    <td><code>object</code></td>
    <td>Static definitions of the ProactiveDetection configuration rule (same values for all components).</td>
</tr>
<tr>
    <td><CopyableCode code="sendEmailsToSubscriptionOwners" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicated whether notifications on this rule should be sent to subscription owners.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The rule name.</td>
</tr>
<tr>
    <td><CopyableCode code="customEmails" /></td>
    <td><code>array</code></td>
    <td>Custom email addresses for this rule notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicates whether this rule is enabled by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string</code></td>
    <td>The last time this rule was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleDefinitions" /></td>
    <td><code>object</code></td>
    <td>Static definitions of the ProactiveDetection configuration rule (same values for all components).</td>
</tr>
<tr>
    <td><CopyableCode code="sendEmailsToSubscriptionOwners" /></td>
    <td><code>boolean</code></td>
    <td>A flag that indicated whether notifications on this rule should be sent to subscription owners.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-configuration_id"><code>configuration_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the ProactiveDetection configuration for this configuration id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of ProactiveDetection configurations of an Application Insights component.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-configuration_id"><code>configuration_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the ProactiveDetection configuration for this configuration id.</td>
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
<tr id="parameter-configuration_id">
    <td><CopyableCode code="configuration_id" /></td>
    <td><code>string</code></td>
    <td>The ProactiveDetection configuration ID. This is unique within a Application Insights component. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
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

Get the ProactiveDetection configuration for this configuration id.

```sql
SELECT
name,
customEmails,
enabled,
lastUpdatedTime,
ruleDefinitions,
sendEmailsToSubscriptionOwners
FROM azure.application_insights.proactive_detection_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND configuration_id = '{{ configuration_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of ProactiveDetection configurations of an Application Insights component.

```sql
SELECT
name,
customEmails,
enabled,
lastUpdatedTime,
ruleDefinitions,
sendEmailsToSubscriptionOwners
FROM azure.application_insights.proactive_detection_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update the ProactiveDetection configuration for this configuration id.

```sql
UPDATE azure.application_insights.proactive_detection_configurations
SET 
name = '{{ name }}',
enabled = {{ enabled }},
sendEmailsToSubscriptionOwners = {{ sendEmailsToSubscriptionOwners }},
customEmails = '{{ customEmails }}',
lastUpdatedTime = '{{ lastUpdatedTime }}',
ruleDefinitions = '{{ ruleDefinitions }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND configuration_id = '{{ configuration_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
name,
customEmails,
enabled,
lastUpdatedTime,
ruleDefinitions,
sendEmailsToSubscriptionOwners;
```
</TabItem>
</Tabs>
