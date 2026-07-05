--- 
title: alerts_suppression_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_suppression_rules
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

Creates, updates, deletes, gets or lists an <code>alerts_suppression_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts_suppression_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts_suppression_rules" /></td></tr>
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
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Type of the alert to automatically suppress. For all alert types, use '*'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Any comment regarding the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of the rule, if value is not provided or provided as null there will no expiration at all.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time this rule was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for dismissing the alert. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Possible states of the rule. Required. Known values are: "Enabled", "Disabled", and "Expired". (Enabled, Disabled, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="suppressionAlertsScope" /></td>
    <td><code>object</code></td>
    <td>The suppression conditions.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Type of the alert to automatically suppress. For all alert types, use '*'. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Any comment regarding the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of the rule, if value is not provided or provided as null there will no expiration at all.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time this rule was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for dismissing the alert. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Possible states of the rule. Required. Known values are: "Enabled", "Disabled", and "Expired". (Enabled, Disabled, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="suppressionAlertsScope" /></td>
    <td><code>object</code></td>
    <td>The suppression conditions.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#parameter-alerts_suppression_rule_name"><code>alerts_suppression_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get dismiss rule, with name: &#123;alertsSuppressionRuleName&#125;, for the given subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-AlertType"><code>AlertType</code></a></td>
    <td>List of all the dismiss rules for the given subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-alerts_suppression_rule_name"><code>alerts_suppression_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update existing rule or create new rule if it doesn't exist.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-alerts_suppression_rule_name"><code>alerts_suppression_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete dismiss alert rule for this subscription.</td>
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
<tr id="parameter-alerts_suppression_rule_name">
    <td><CopyableCode code="alerts_suppression_rule_name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the suppression alert rule. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-AlertType">
    <td><CopyableCode code="AlertType" /></td>
    <td><code>string</code></td>
    <td>Type of the alert to get rules for. Default value is None.</td>
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

Get dismiss rule, with name: &#123;alertsSuppressionRuleName&#125;, for the given subscription.

```sql
SELECT
id,
name,
alertType,
comment,
expirationDateUtc,
lastModifiedUtc,
reason,
state,
suppressionAlertsScope,
systemData,
type
FROM azure.security.alerts_suppression_rules
WHERE alerts_suppression_rule_name = '{{ alerts_suppression_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List of all the dismiss rules for the given subscription.

```sql
SELECT
id,
name,
alertType,
comment,
expirationDateUtc,
lastModifiedUtc,
reason,
state,
suppressionAlertsScope,
systemData,
type
FROM azure.security.alerts_suppression_rules
WHERE subscription_id = '{{ subscription_id }}' -- required
AND AlertType = '{{ AlertType }}'
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

Update existing rule or create new rule if it doesn't exist.

```sql
UPDATE azure.security.alerts_suppression_rules
SET 
properties = '{{ properties }}'
WHERE 
alerts_suppression_rule_name = '{{ alerts_suppression_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete dismiss alert rule for this subscription.

```sql
DELETE FROM azure.security.alerts_suppression_rules
WHERE alerts_suppression_rule_name = '{{ alerts_suppression_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
