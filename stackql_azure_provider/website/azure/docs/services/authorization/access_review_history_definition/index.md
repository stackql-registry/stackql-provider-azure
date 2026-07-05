--- 
title: access_review_history_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definition
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

Creates, updates, deletes, gets or lists an <code>access_review_history_definition</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_review_history_definition" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_history_definition" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-history_definition_id"><code>history_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a scheduled or one-time Access Review History Definition.</td>
</tr>
<tr>
    <td><a href="#delete_by_id"><CopyableCode code="delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-history_definition_id"><code>history_definition_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an access review history definition.</td>
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
<tr id="parameter-history_definition_id">
    <td><CopyableCode code="history_definition_id" /></td>
    <td><code>string</code></td>
    <td>The id of the access review history definition. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a scheduled or one-time Access Review History Definition.

```sql
INSERT INTO azure.authorization.access_review_history_definition (
displayName,
decisions,
scopes,
settings,
instances,
history_definition_id,
subscription_id
)
SELECT 
'{{ displayName }}',
'{{ decisions }}',
'{{ scopes }}',
'{{ settings }}',
'{{ instances }}',
'{{ history_definition_id }}',
'{{ subscription_id }}'
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
- name: access_review_history_definition
  props:
    - name: history_definition_id
      value: "{{ history_definition_id }}"
      description: Required parameter for the access_review_history_definition resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the access_review_history_definition resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the history definition.
    - name: decisions
      value:
        - "{{ decisions }}"
      description: |
        Collection of review decisions which the history data should be filtered on. For example if Approve and Deny are supplied the data will only contain review results in which the decision maker approved or denied a review request.
    - name: scopes
      description: |
        A collection of scopes used when selecting review history data.
      value:
        - resourceId: "{{ resourceId }}"
          roleDefinitionId: "{{ roleDefinitionId }}"
          principalType: "{{ principalType }}"
          assignmentState: "{{ assignmentState }}"
          inactiveDuration: "{{ inactiveDuration }}"
          expandNestedMemberships: {{ expandNestedMemberships }}
          includeInheritedAccess: {{ includeInheritedAccess }}
          includeAccessBelowResource: {{ includeAccessBelowResource }}
          excludeResourceId: "{{ excludeResourceId }}"
          excludeRoleDefinitionId: "{{ excludeRoleDefinitionId }}"
    - name: settings
      description: |
        Recurrence settings for recurring history reports, skip for one-time reports.
      value:
        pattern:
          type: "{{ type }}"
          interval: {{ interval }}
        range:
          type: "{{ type }}"
          numberOfOccurrences: {{ numberOfOccurrences }}
          startDate: "{{ startDate }}"
          endDate: "{{ endDate }}"
    - name: instances
      description: |
        Set of access review history instances for this history definition.
      value:
        - id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
          properties:
            reviewHistoryPeriodStartDateTime: "{{ reviewHistoryPeriodStartDateTime }}"
            reviewHistoryPeriodEndDateTime: "{{ reviewHistoryPeriodEndDateTime }}"
            displayName: "{{ displayName }}"
            status: "{{ status }}"
            runDateTime: "{{ runDateTime }}"
            fulfilledDateTime: "{{ fulfilledDateTime }}"
            downloadUri: "{{ downloadUri }}"
            expiration: "{{ expiration }}"
`}</CodeBlock>

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

Delete an access review history definition.

```sql
DELETE FROM azure.authorization.access_review_history_definition
WHERE history_definition_id = '{{ history_definition_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
