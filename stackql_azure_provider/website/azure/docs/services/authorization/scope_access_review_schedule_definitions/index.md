--- 
title: scope_access_review_schedule_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_schedule_definitions
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

Creates, updates, deletes, gets or lists a <code>scope_access_review_schedule_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scope_access_review_schedule_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_schedule_definitions" /></td></tr>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a></td>
    <td></td>
    <td>Get single access review definition.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get access review schedule definitions.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_id"><CopyableCode code="create_or_update_by_id" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a></td>
    <td></td>
    <td>Create or Update access review schedule definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_id"><CopyableCode code="create_or_update_by_id" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a></td>
    <td></td>
    <td>Create or Update access review schedule definition.</td>
</tr>
<tr>
    <td><a href="#delete_by_id"><CopyableCode code="delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a></td>
    <td></td>
    <td>Delete access review schedule definition.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-schedule_definition_id"><code>schedule_definition_id</code></a></td>
    <td></td>
    <td>Stop access review definition.</td>
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

Get single access review definition.

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
FROM azure.authorization.scope_access_review_schedule_definitions
WHERE scope = '{{ scope }}' -- required
AND schedule_definition_id = '{{ schedule_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get access review schedule definitions.

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
FROM azure.authorization.scope_access_review_schedule_definitions
WHERE scope = '{{ scope }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_by_id"
    values={[
        { label: 'create_or_update_by_id', value: 'create_or_update_by_id' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_by_id">

Create or Update access review schedule definition.

```sql
INSERT INTO azure.authorization.scope_access_review_schedule_definitions (
displayName,
descriptionForAdmins,
descriptionForReviewers,
settings,
reviewers,
backupReviewers,
instances,
scope,
schedule_definition_id
)
SELECT 
'{{ displayName }}',
'{{ descriptionForAdmins }}',
'{{ descriptionForReviewers }}',
'{{ settings }}',
'{{ reviewers }}',
'{{ backupReviewers }}',
'{{ instances }}',
'{{ scope }}',
'{{ schedule_definition_id }}'
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
- name: scope_access_review_schedule_definitions
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the scope_access_review_schedule_definitions resource.
    - name: schedule_definition_id
      value: "{{ schedule_definition_id }}"
      description: Required parameter for the scope_access_review_schedule_definitions resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the schedule definition.
    - name: descriptionForAdmins
      value: "{{ descriptionForAdmins }}"
      description: |
        The description provided by the access review creator and visible to admins.
    - name: descriptionForReviewers
      value: "{{ descriptionForReviewers }}"
      description: |
        The description provided by the access review creator to be shown to reviewers.
    - name: settings
      description: |
        Access Review Settings.
      value:
        mailNotificationsEnabled: {{ mailNotificationsEnabled }}
        reminderNotificationsEnabled: {{ reminderNotificationsEnabled }}
        defaultDecisionEnabled: {{ defaultDecisionEnabled }}
        justificationRequiredOnApproval: {{ justificationRequiredOnApproval }}
        defaultDecision: "{{ defaultDecision }}"
        autoApplyDecisionsEnabled: {{ autoApplyDecisionsEnabled }}
        recommendationsEnabled: {{ recommendationsEnabled }}
        recommendationLookBackDuration: "{{ recommendationLookBackDuration }}"
        instanceDurationInDays: {{ instanceDurationInDays }}
        recurrence:
          pattern:
            type: "{{ type }}"
            interval: {{ interval }}
          range:
            type: "{{ type }}"
            numberOfOccurrences: {{ numberOfOccurrences }}
            startDate: "{{ startDate }}"
            endDate: "{{ endDate }}"
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
    - name: instances
      description: |
        This is the collection of instances returned when one does an expand on it.
      value:
        - id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          systemData:
            createdBy: "{{ createdBy }}"
            createdByType: "{{ createdByType }}"
            createdAt: "{{ createdAt }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedByType: "{{ lastModifiedByType }}"
            lastModifiedAt: "{{ lastModifiedAt }}"
          properties:
            status: "{{ status }}"
            startDateTime: "{{ startDateTime }}"
            endDateTime: "{{ endDateTime }}"
            reviewers:
              - principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
            backupReviewers:
              - principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
            reviewersType: "{{ reviewersType }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_by_id"
    values={[
        { label: 'create_or_update_by_id', value: 'create_or_update_by_id' }
    ]}
>
<TabItem value="create_or_update_by_id">

Create or Update access review schedule definition.

```sql
REPLACE azure.authorization.scope_access_review_schedule_definitions
SET 
displayName = '{{ displayName }}',
descriptionForAdmins = '{{ descriptionForAdmins }}',
descriptionForReviewers = '{{ descriptionForReviewers }}',
settings = '{{ settings }}',
reviewers = '{{ reviewers }}',
backupReviewers = '{{ backupReviewers }}',
instances = '{{ instances }}'
WHERE 
scope = '{{ scope }}' --required
AND schedule_definition_id = '{{ schedule_definition_id }}' --required
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
    defaultValue="delete_by_id"
    values={[
        { label: 'delete_by_id', value: 'delete_by_id' }
    ]}
>
<TabItem value="delete_by_id">

Delete access review schedule definition.

```sql
DELETE FROM azure.authorization.scope_access_review_schedule_definitions
WHERE scope = '{{ scope }}' --required
AND schedule_definition_id = '{{ schedule_definition_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="stop">

Stop access review definition.

```sql
EXEC azure.authorization.scope_access_review_schedule_definitions.stop 
@scope='{{ scope }}' --required, 
@schedule_definition_id='{{ schedule_definition_id }}' --required
;
```
</TabItem>
</Tabs>
