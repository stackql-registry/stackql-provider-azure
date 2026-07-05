--- 
title: access_review_schedule_definitions_assigned_for_my_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions_assigned_for_my_approval
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

Creates, updates, deletes, gets or lists an <code>access_review_schedule_definitions_assigned_for_my_approval</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_review_schedule_definitions_assigned_for_my_approval" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_schedule_definitions_assigned_for_my_approval" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="backupReviewers" /></td>
    <td><code>array</code></td>
    <td>This is the collection of backup reviewers.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The user or other identity who created this review.</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionForAdmins" /></td>
    <td><code>string</code></td>
    <td>The description provided by the access review creator and visible to admins.</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionForReviewers" /></td>
    <td><code>string</code></td>
    <td>The description provided by the access review creator to be shown to reviewers.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the schedule definition.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>This is the collection of instances returned when one does an expand on it.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This is the collection of reviewers.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewersType" /></td>
    <td><code>string</code></td>
    <td>This field specifies the type of reviewers for a review. Usually for a review, reviewers are explicitly assigned. However, in some cases, the reviewers may not be assigned and instead be chosen dynamically. For example managers review or self review. Known values are: "Assigned", "Self", and "Managers". (Assigned, Self, Managers)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>Descriptor for what needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Access Review Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This read-only field specifies the status of an accessReview. Known values are: "NotStarted", "InProgress", "Completed", "Applied", "Initializing", "Applying", "Completing", "Scheduled", "AutoReviewing", "AutoReviewed", and "Starting". (NotStarted, InProgress, Completed, Applied, Initializing, Applying, Completing, Scheduled, AutoReviewing, AutoReviewed, Starting)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get access review instances assigned for my approval.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. One custom filter option is supported : 'assignedToMeToReview()'. When specified $filter=assignedToMeToReview(), only items that are assigned to the calling user to review are returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get access review instances assigned for my approval.

```sql
SELECT
id,
name,
backupReviewers,
createdBy,
descriptionForAdmins,
descriptionForReviewers,
displayName,
instances,
reviewers,
reviewersType,
scope,
settings,
status,
systemData,
type
FROM azure.authorization.access_review_schedule_definitions_assigned_for_my_approval
WHERE $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
