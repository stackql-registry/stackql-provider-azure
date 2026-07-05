--- 
title: standard_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - standard_assignments
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

Creates, updates, deletes, gets or lists a <code>standard_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="standard_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.standard_assignments" /></td></tr>
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
    <td><CopyableCode code="assignedStandard" /></td>
    <td><code>object</code></td>
    <td>Standard item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="attestationData" /></td>
    <td><code>object</code></td>
    <td>Additional data about assignment that has Attest effect.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effect" /></td>
    <td><code>string</code></td>
    <td>Expected effect of this assignment (Audit/Exempt/Attest). Known values are: "Audit", "Exempt", and "Attest". (Audit, Exempt, Attest)</td>
</tr>
<tr>
    <td><CopyableCode code="excludedScopes" /></td>
    <td><code>array</code></td>
    <td>Excluded scopes, filter out the descendants of the scope (on management scopes).</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionData" /></td>
    <td><code>object</code></td>
    <td>Additional data about assignment that has Exempt effect.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of this assignment as a full ISO date.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The standard assignment metadata.</td>
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
    <td><CopyableCode code="assignedStandard" /></td>
    <td><code>object</code></td>
    <td>Standard item with key as applied to this standard assignment over the given scope.</td>
</tr>
<tr>
    <td><CopyableCode code="attestationData" /></td>
    <td><code>object</code></td>
    <td>Additional data about assignment that has Attest effect.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the standardAssignment.</td>
</tr>
<tr>
    <td><CopyableCode code="effect" /></td>
    <td><code>string</code></td>
    <td>Expected effect of this assignment (Audit/Exempt/Attest). Known values are: "Audit", "Exempt", and "Attest". (Audit, Exempt, Attest)</td>
</tr>
<tr>
    <td><CopyableCode code="excludedScopes" /></td>
    <td><code>array</code></td>
    <td>Excluded scopes, filter out the descendants of the scope (on management scopes).</td>
</tr>
<tr>
    <td><CopyableCode code="exemptionData" /></td>
    <td><code>object</code></td>
    <td>Additional data about assignment that has Exempt effect.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date of this assignment as a full ISO date.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The standard assignment metadata.</td>
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
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-standard_assignment_name"><code>standard_assignment_name</code></a></td>
    <td></td>
    <td>Retrieves a standard assignment. This operation retrieves a single standard assignment, given its name and the scope it was created at.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get a list of all relevant standard assignments over a scope.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-standard_assignment_name"><code>standard_assignment_name</code></a></td>
    <td></td>
    <td>Creates or updates a standard assignment. This operation creates or updates a standard assignment with the given scope and name. standard assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-standard_assignment_name"><code>standard_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a standard assignment. This operation deletes a standard assignment, given its name and the scope it was created in. The scope of a standard assignment is the part of its ID preceding '/providers/Microsoft.Security/standardAssignments/&#123;standardAssignmentName&#125;'.</td>
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
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-standard_assignment_name">
    <td><CopyableCode code="standard_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The standard assignments assignment key - unique key for the standard assignment. Required.</td>
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

Retrieves a standard assignment. This operation retrieves a single standard assignment, given its name and the scope it was created at.

```sql
SELECT
id,
name,
assignedStandard,
attestationData,
description,
displayName,
effect,
excludedScopes,
exemptionData,
expiresOn,
metadata,
systemData,
type
FROM azure.security.standard_assignments
WHERE resource_id = '{{ resource_id }}' -- required
AND standard_assignment_name = '{{ standard_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all relevant standard assignments over a scope.

```sql
SELECT
id,
name,
assignedStandard,
attestationData,
description,
displayName,
effect,
excludedScopes,
exemptionData,
expiresOn,
metadata,
systemData,
type
FROM azure.security.standard_assignments
WHERE scope = '{{ scope }}' -- required
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

Creates or updates a standard assignment. This operation creates or updates a standard assignment with the given scope and name. standard assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.

```sql
INSERT INTO azure.security.standard_assignments (
properties,
resource_id,
standard_assignment_name
)
SELECT 
'{{ properties }}',
'{{ resource_id }}',
'{{ standard_assignment_name }}'
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
- name: standard_assignments
  props:
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the standard_assignments resource.
    - name: standard_assignment_name
      value: "{{ standard_assignment_name }}"
      description: Required parameter for the standard_assignments resource.
    - name: properties
      description: |
        Properties of a standard assignments assignment.
      value:
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        assignedStandard:
          id: "{{ id }}"
        effect: "{{ effect }}"
        excludedScopes:
          - "{{ excludedScopes }}"
        expiresOn: "{{ expiresOn }}"
        exemptionData:
          exemptionCategory: "{{ exemptionCategory }}"
          assignedAssessment:
            assessmentKey: "{{ assessmentKey }}"
        attestationData:
          complianceState: "{{ complianceState }}"
          assignedAssessment:
            assessmentKey: "{{ assessmentKey }}"
          complianceDate: "{{ complianceDate }}"
          evidence:
            - description: "{{ description }}"
              sourceUrl: "{{ sourceUrl }}"
        metadata:
          createdBy: "{{ createdBy }}"
          createdOn: "{{ createdOn }}"
          lastUpdatedBy: "{{ lastUpdatedBy }}"
          lastUpdatedOn: "{{ lastUpdatedOn }}"
`}</CodeBlock>

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

Deletes a standard assignment. This operation deletes a standard assignment, given its name and the scope it was created in. The scope of a standard assignment is the part of its ID preceding '/providers/Microsoft.Security/standardAssignments/&#123;standardAssignmentName&#125;'.

```sql
DELETE FROM azure.security.standard_assignments
WHERE resource_id = '{{ resource_id }}' --required
AND standard_assignment_name = '{{ standard_assignment_name }}' --required
;
```
</TabItem>
</Tabs>
