--- 
title: access_review_instance_my_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instance_my_decisions
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

Creates, updates, deletes, gets or lists an <code>access_review_instance_my_decisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_review_instance_my_decisions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_instance_my_decisions" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedBy" /></td>
    <td><code>object</code></td>
    <td>Details of the approver.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the review decision was applied.</td>
</tr>
<tr>
    <td><CopyableCode code="applyResult" /></td>
    <td><code>string</code></td>
    <td>The outcome of applying the decision. Known values are: "New", "Applying", "AppliedSuccessfully", "AppliedWithUnknownFailure", "AppliedSuccessfullyButObjectNotFound", and "ApplyNotSupported". (New, Applying, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound, ApplyNotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The decision on the approval step. This value is initially set to NotReviewed. Approvers can take action of Approve/Deny. Known values are: "Approve", "Deny", "NotReviewed", "DontKnow", and "NotNotified". (Approve, Deny, NotReviewed, DontKnow, NotNotified)</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>array</code></td>
    <td>This is the collection of insights for this decision item.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification provided by approvers for their action.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code>object</code></td>
    <td>Principal associated with the decision record. Can be AccessReviewDecisionUserIdentity or AccessReviewDecisionServicePrincipalIdentity.</td>
</tr>
<tr>
    <td><CopyableCode code="principalResourceMembership" /></td>
    <td><code>object</code></td>
    <td>Details of the membership type.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendation" /></td>
    <td><code>string</code></td>
    <td>The feature- generated recommendation shown to the reviewer. Known values are: "Approve", "Deny", and "NoInfoAvailable". (Approve, Deny, NoInfoAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>Resource associated with this decision record.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>Details of the approver.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date Time when a decision was taken.</td>
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
    <td><CopyableCode code="appliedBy" /></td>
    <td><code>object</code></td>
    <td>Details of the approver.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the review decision was applied.</td>
</tr>
<tr>
    <td><CopyableCode code="applyResult" /></td>
    <td><code>string</code></td>
    <td>The outcome of applying the decision. Known values are: "New", "Applying", "AppliedSuccessfully", "AppliedWithUnknownFailure", "AppliedSuccessfullyButObjectNotFound", and "ApplyNotSupported". (New, Applying, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound, ApplyNotSupported)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The decision on the approval step. This value is initially set to NotReviewed. Approvers can take action of Approve/Deny. Known values are: "Approve", "Deny", "NotReviewed", "DontKnow", and "NotNotified". (Approve, Deny, NotReviewed, DontKnow, NotNotified)</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>array</code></td>
    <td>This is the collection of insights for this decision item.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification provided by approvers for their action.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code>object</code></td>
    <td>Principal associated with the decision record. Can be AccessReviewDecisionUserIdentity or AccessReviewDecisionServicePrincipalIdentity.</td>
</tr>
<tr>
    <td><CopyableCode code="principalResourceMembership" /></td>
    <td><code>object</code></td>
    <td>Details of the membership type.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendation" /></td>
    <td><code>string</code></td>
    <td>The feature- generated recommendation shown to the reviewer. Known values are: "Approve", "Deny", and "NoInfoAvailable". (Approve, Deny, NoInfoAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>Resource associated with this decision record.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code>object</code></td>
    <td>Details of the approver.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date Time when a decision was taken.</td>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-decision_id"><code>decision_id</code></a></td>
    <td></td>
    <td>Get my single access review instance decision.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get my access review instance decisions.</td>
</tr>
<tr>
    <td><a href="#patch"><CopyableCode code="patch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-decision_id"><code>decision_id</code></a></td>
    <td></td>
    <td>Record a decision.</td>
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
<tr id="parameter-decision_id">
    <td><CopyableCode code="decision_id" /></td>
    <td><code>string</code></td>
    <td>The id of the decision record. Required.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The id of the access review instance. Required.</td>
</tr>
<tr id="parameter-schedule_definition_id">
    <td><CopyableCode code="schedule_definition_id" /></td>
    <td><code>string</code></td>
    <td>The id of the access review schedule definition. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Other than standard filters, one custom filter option is supported : 'assignedToMeToReview()'. When one specified $filter=assignedToMeToReview(), only items that are assigned to the calling user to review are returned. Default value is None.</td>
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

Get my single access review instance decision.

```sql
SELECT
id,
name,
appliedBy,
appliedDateTime,
applyResult,
decision,
insights,
justification,
principal,
principalResourceMembership,
recommendation,
resource,
reviewedBy,
reviewedDateTime,
systemData,
type
FROM azure.authorization.access_review_instance_my_decisions
WHERE schedule_definition_id = '{{ schedule_definition_id }}' -- required
AND id = '{{ id }}' -- required
AND decision_id = '{{ decision_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get my access review instance decisions.

```sql
SELECT
id,
name,
appliedBy,
appliedDateTime,
applyResult,
decision,
insights,
justification,
principal,
principalResourceMembership,
recommendation,
resource,
reviewedBy,
reviewedDateTime,
systemData,
type
FROM azure.authorization.access_review_instance_my_decisions
WHERE schedule_definition_id = '{{ schedule_definition_id }}' -- required
AND id = '{{ id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' }
    ]}
>
<TabItem value="patch">

Record a decision.

```sql
EXEC azure.authorization.access_review_instance_my_decisions.patch 
@schedule_definition_id='{{ schedule_definition_id }}' --required, 
@id='{{ id }}' --required, 
@decision_id='{{ decision_id }}' --required 
@@json=
'{
"decision": "{{ decision }}", 
"justification": "{{ justification }}", 
"insights": "{{ insights }}"
}'
;
```
</TabItem>
</Tabs>
