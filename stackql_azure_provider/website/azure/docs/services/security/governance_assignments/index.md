--- 
title: governance_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_assignments
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

Creates, updates, deletes, gets or lists a <code>governance_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="governance_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.governance_assignments" /></td></tr>
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
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>The additional data for the governance assignment - e.g. links to ticket (optional), see example.</td>
</tr>
<tr>
    <td><CopyableCode code="governanceEmailNotification" /></td>
    <td><code>object</code></td>
    <td>The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners.</td>
</tr>
<tr>
    <td><CopyableCode code="isGracePeriod" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether there is a grace period on the governance assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The Owner for the governance assignment - e.g. `user@contoso.com `_ - see example.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationDueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The remediation due-date - after this date Secure Score will be affected (in case of active grace-period). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationEta" /></td>
    <td><code>object</code></td>
    <td>The ETA (estimated time of arrival) for remediation (optional), see example.</td>
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
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>The additional data for the governance assignment - e.g. links to ticket (optional), see example.</td>
</tr>
<tr>
    <td><CopyableCode code="governanceEmailNotification" /></td>
    <td><code>object</code></td>
    <td>The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners.</td>
</tr>
<tr>
    <td><CopyableCode code="isGracePeriod" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether there is a grace period on the governance assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The Owner for the governance assignment - e.g. `user@contoso.com `_ - see example.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationDueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The remediation due-date - after this date Secure Score will be affected (in case of active grace-period). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationEta" /></td>
    <td><code>object</code></td>
    <td>The ETA (estimated time of arrival) for remediation (optional), see example.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-assignment_key"><code>assignment_key</code></a></td>
    <td></td>
    <td>Get a specific governanceAssignment for the requested scope by AssignmentKey.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a></td>
    <td></td>
    <td>Get governance assignments on all of your resources inside a scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-assignment_key"><code>assignment_key</code></a></td>
    <td></td>
    <td>Creates or updates a governance assignment on the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-assignment_key"><code>assignment_key</code></a></td>
    <td></td>
    <td>Creates or updates a governance assignment on the given subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-assignment_key"><code>assignment_key</code></a></td>
    <td></td>
    <td>Delete a GovernanceAssignment over a given scope.</td>
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
<tr id="parameter-assessment_name">
    <td><CopyableCode code="assessment_name" /></td>
    <td><code>string</code></td>
    <td>The assessment key of the governance assignment. Required.</td>
</tr>
<tr id="parameter-assignment_key">
    <td><CopyableCode code="assignment_key" /></td>
    <td><code>string</code></td>
    <td>The governance assignment key. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the governance assignment. Required.</td>
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

Get a specific governanceAssignment for the requested scope by AssignmentKey.

```sql
SELECT
id,
name,
additionalData,
governanceEmailNotification,
isGracePeriod,
owner,
remediationDueDate,
remediationEta,
systemData,
type
FROM azure.security.governance_assignments
WHERE scope = '{{ scope }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND assignment_key = '{{ assignment_key }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get governance assignments on all of your resources inside a scope.

```sql
SELECT
id,
name,
additionalData,
governanceEmailNotification,
isGracePeriod,
owner,
remediationDueDate,
remediationEta,
systemData,
type
FROM azure.security.governance_assignments
WHERE scope = '{{ scope }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a governance assignment on the given subscription.

```sql
INSERT INTO azure.security.governance_assignments (
properties,
scope,
assessment_name,
assignment_key
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ assessment_name }}',
'{{ assignment_key }}'
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
- name: governance_assignments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the governance_assignments resource.
    - name: assessment_name
      value: "{{ assessment_name }}"
      description: Required parameter for the governance_assignments resource.
    - name: assignment_key
      value: "{{ assignment_key }}"
      description: Required parameter for the governance_assignments resource.
    - name: properties
      description: |
        The properties of a governance assignment.
      value:
        owner: "{{ owner }}"
        remediationDueDate: "{{ remediationDueDate }}"
        remediationEta:
          eta: "{{ eta }}"
          justification: "{{ justification }}"
        isGracePeriod: {{ isGracePeriod }}
        governanceEmailNotification:
          disableManagerEmailNotification: {{ disableManagerEmailNotification }}
          disableOwnerEmailNotification: {{ disableOwnerEmailNotification }}
        additionalData:
          ticketNumber: {{ ticketNumber }}
          ticketLink: "{{ ticketLink }}"
          ticketStatus: "{{ ticketStatus }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a governance assignment on the given subscription.

```sql
REPLACE azure.security.governance_assignments
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND assessment_name = '{{ assessment_name }}' --required
AND assignment_key = '{{ assignment_key }}' --required
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

Delete a GovernanceAssignment over a given scope.

```sql
DELETE FROM azure.security.governance_assignments
WHERE scope = '{{ scope }}' --required
AND assessment_name = '{{ assessment_name }}' --required
AND assignment_key = '{{ assignment_key }}' --required
;
```
</TabItem>
</Tabs>
