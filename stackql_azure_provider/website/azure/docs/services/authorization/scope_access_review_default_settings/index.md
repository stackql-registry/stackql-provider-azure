--- 
title: scope_access_review_default_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_default_settings
  - authorization
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

Creates, updates, deletes, gets or lists a <code>scope_access_review_default_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scope_access_review_default_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_default_settings" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="autoApplyDecisionsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether auto-apply capability, to automatically change the target object access resource, is enabled. If not enabled, a user must, after the review completes, apply the access review.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDecision" /></td>
    <td><code>string</code></td>
    <td>This specifies the behavior for the autoReview feature when an access review completes. Known values are: "Approve", "Deny", and "Recommendation". (Approve, Deny, Recommendation)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDecisionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether reviewers are required to provide a justification when reviewing access.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceDurationInDays" /></td>
    <td><code>integer</code></td>
    <td>The duration in days for an instance.</td>
</tr>
<tr>
    <td><CopyableCode code="justificationRequiredOnApproval" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether the reviewer is required to pass justification when recording a decision.</td>
</tr>
<tr>
    <td><CopyableCode code="mailNotificationsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether sending mails to reviewers and the review creator is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationLookBackDuration" /></td>
    <td><code>string</code></td>
    <td>Recommendations for access reviews are calculated by looking back at 30 days of data(w.r.t the start date of the review) by default. However, in some scenarios, customers want to change how far back to look at and want to configure 60 days, 90 days, etc. instead. This setting allows customers to configure this duration. The value should be in ISO 8601 format (`http://en.wikipedia.org/wiki/ISO_8601#Durations).This `_ code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds)).</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether showing recommendations to reviewers is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="recurrence" /></td>
    <td><code>object</code></td>
    <td>Access Review Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="reminderNotificationsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag to indicate whether sending reminder emails to reviewers are enabled.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get access review default settings for the subscription.</td>
</tr>
<tr>
    <td><a href="#put"><CopyableCode code="put" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get access review default settings for the subscription.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the resource. Required.</td>
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

Get access review default settings for the subscription.

```sql
SELECT
id,
name,
autoApplyDecisionsEnabled,
defaultDecision,
defaultDecisionEnabled,
instanceDurationInDays,
justificationRequiredOnApproval,
mailNotificationsEnabled,
recommendationLookBackDuration,
recommendationsEnabled,
recurrence,
reminderNotificationsEnabled,
systemData,
type
FROM azure.authorization.scope_access_review_default_settings
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="put"
    values={[
        { label: 'put', value: 'put' }
    ]}
>
<TabItem value="put">

Get access review default settings for the subscription.

```sql
EXEC azure.authorization.scope_access_review_default_settings.put 
@scope='{{ scope }}' --required 
@@json=
'{
"mailNotificationsEnabled": {{ mailNotificationsEnabled }}, 
"reminderNotificationsEnabled": {{ reminderNotificationsEnabled }}, 
"defaultDecisionEnabled": {{ defaultDecisionEnabled }}, 
"justificationRequiredOnApproval": {{ justificationRequiredOnApproval }}, 
"defaultDecision": "{{ defaultDecision }}", 
"autoApplyDecisionsEnabled": {{ autoApplyDecisionsEnabled }}, 
"recommendationsEnabled": {{ recommendationsEnabled }}, 
"recommendationLookBackDuration": "{{ recommendationLookBackDuration }}", 
"instanceDurationInDays": {{ instanceDurationInDays }}, 
"recurrence": "{{ recurrence }}"
}'
;
```
</TabItem>
</Tabs>
