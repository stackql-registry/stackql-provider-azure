--- 
title: scope_access_review_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instances
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

Creates, updates, deletes, gets or lists a <code>scope_access_review_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scope_access_review_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_instances" /></td></tr>
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
    <td><CopyableCode code="backupReviewers" /></td>
    <td><code>array</code></td>
    <td>This is the collection of backup reviewers.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The DateTime when the review instance is scheduled to end.</td>
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
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The DateTime when the review instance is scheduled to be start.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This read-only field specifies the status of an access review instance. Known values are: "NotStarted", "InProgress", "Completed", "Applied", "Initializing", "Applying", "Completing", "Scheduled", "AutoReviewing", "AutoReviewed", and "Starting". (NotStarted, InProgress, Completed, Applied, Initializing, Applying, Completing, Scheduled, AutoReviewing, AutoReviewed, Starting)</td>
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
    <td><CopyableCode code="backupReviewers" /></td>
    <td><code>array</code></td>
    <td>This is the collection of backup reviewers.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The DateTime when the review instance is scheduled to end.</td>
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
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The DateTime when the review instance is scheduled to be start.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This read-only field specifies the status of an access review instance. Known values are: "NotStarted", "InProgress", "Completed", "Applied", "Initializing", "Applying", "Completing", "Scheduled", "AutoReviewing", "AutoReviewed", and "Starting". (NotStarted, InProgress, Completed, Applied, Initializing, Applying, Completing, Scheduled, AutoReviewing, AutoReviewed, Starting)</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Get access review instances.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get access review instances.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Update access review instance.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the resource. Required.</td>
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

Get access review instances.

```sql
SELECT
id,
name,
backupReviewers,
endDateTime,
reviewers,
reviewersType,
startDateTime,
status,
systemData,
type
FROM azure.authorization.scope_access_review_instances
WHERE scope = '{{ scope }}' -- required
AND schedule_definition_id = '{{ schedule_definition_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get access review instances.

```sql
SELECT
id,
name,
backupReviewers,
endDateTime,
reviewers,
reviewersType,
startDateTime,
status,
systemData,
type
FROM azure.authorization.scope_access_review_instances
WHERE scope = '{{ scope }}' -- required
AND schedule_definition_id = '{{ schedule_definition_id }}' -- required
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

Update access review instance.

```sql
INSERT INTO azure.authorization.scope_access_review_instances (
startDateTime,
endDateTime,
reviewers,
backupReviewers,
scope,
schedule_definition_id,
id
)
SELECT 
'{{ startDateTime }}',
'{{ endDateTime }}',
'{{ reviewers }}',
'{{ backupReviewers }}',
'{{ scope }}',
'{{ schedule_definition_id }}',
'{{ id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: scope_access_review_instances
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the scope_access_review_instances resource.
    - name: schedule_definition_id
      value: "{{ schedule_definition_id }}"
      description: Required parameter for the scope_access_review_instances resource.
    - name: id
      value: "{{ id }}"
      description: Required parameter for the scope_access_review_instances resource.
    - name: startDateTime
      value: "{{ startDateTime }}"
      description: |
        The DateTime when the review instance is scheduled to be start.
    - name: endDateTime
      value: "{{ endDateTime }}"
      description: |
        The DateTime when the review instance is scheduled to end.
    - name: reviewers
      description: |
        This is the collection of reviewers.
      value:
        - principalId: "{{ principalId }}"
          principalType: "{{ principalType }}"
    - name: backupReviewers
      description: |
        This is the collection of backup reviewers.
      value:
        - principalId: "{{ principalId }}"
          principalType: "{{ principalType }}"
`}</CodeBlock>

</TabItem>
</Tabs>
