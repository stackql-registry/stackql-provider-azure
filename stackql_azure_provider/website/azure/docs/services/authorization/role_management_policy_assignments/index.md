--- 
title: role_management_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policy_assignments
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

Creates, updates, deletes, gets or lists a <code>role_management_policy_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_management_policy_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_management_policy_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
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
    <td><CopyableCode code="effectiveRules" /></td>
    <td><code>array</code></td>
    <td>The readonly computed rule applied to the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of scope, role definition and policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The policy id role management policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition of management policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role management policy scope.</td>
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
<TabItem value="list_for_scope">

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
    <td><CopyableCode code="effectiveRules" /></td>
    <td><code>array</code></td>
    <td>The readonly computed rule applied to the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyAssignmentProperties" /></td>
    <td><code>object</code></td>
    <td>Additional properties of scope, role definition and policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The policy id role management policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The role definition of management policy assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The role management policy scope.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_management_policy_assignment_name"><code>role_management_policy_assignment_name</code></a></td>
    <td></td>
    <td>Get the specified role management policy assignment for a resource scope.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Gets role management assignment policies for a resource scope.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_management_policy_assignment_name"><code>role_management_policy_assignment_name</code></a></td>
    <td></td>
    <td>Create a role management policy assignment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-role_management_policy_assignment_name"><code>role_management_policy_assignment_name</code></a></td>
    <td></td>
    <td>Delete a role management policy assignment.</td>
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
<tr id="parameter-role_management_policy_assignment_name">
    <td><CopyableCode code="role_management_policy_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The name of format &#123;guid_guid&#125; the role management policy assignment to get. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
    ]}
>
<TabItem value="get">

Get the specified role management policy assignment for a resource scope.

```sql
SELECT
id,
name,
effectiveRules,
policyAssignmentProperties,
policyId,
roleDefinitionId,
scope,
systemData,
type
FROM azure.authorization.role_management_policy_assignments
WHERE scope = '{{ scope }}' -- required
AND role_management_policy_assignment_name = '{{ role_management_policy_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="list_for_scope">

Gets role management assignment policies for a resource scope.

```sql
SELECT
id,
name,
effectiveRules,
policyAssignmentProperties,
policyId,
roleDefinitionId,
scope,
systemData,
type
FROM azure.authorization.role_management_policy_assignments
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

Create a role management policy assignment.

```sql
INSERT INTO azure.authorization.role_management_policy_assignments (
properties,
scope,
role_management_policy_assignment_name
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ role_management_policy_assignment_name }}'
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
- name: role_management_policy_assignments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the role_management_policy_assignments resource.
    - name: role_management_policy_assignment_name
      value: "{{ role_management_policy_assignment_name }}"
      description: Required parameter for the role_management_policy_assignments resource.
    - name: properties
      description: |
        Role management policy properties.
      value:
        scope: "{{ scope }}"
        roleDefinitionId: "{{ roleDefinitionId }}"
        policyId: "{{ policyId }}"
        effectiveRules:
          - id: "{{ id }}"
            ruleType: "{{ ruleType }}"
            target:
              caller: "{{ caller }}"
              operations:
                - "{{ operations }}"
              level: "{{ level }}"
              targetObjects:
                - "{{ targetObjects }}"
              inheritableSettings:
                - "{{ inheritableSettings }}"
              enforcedSettings:
                - "{{ enforcedSettings }}"
        policyAssignmentProperties:
          scope:
            id: "{{ id }}"
            displayName: "{{ displayName }}"
            type: "{{ type }}"
          roleDefinition:
            id: "{{ id }}"
            displayName: "{{ displayName }}"
            type: "{{ type }}"
          policy:
            id: "{{ id }}"
            lastModifiedBy:
              id: "{{ id }}"
              displayName: "{{ displayName }}"
              type: "{{ type }}"
              email: "{{ email }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
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

Delete a role management policy assignment.

```sql
DELETE FROM azure.authorization.role_management_policy_assignments
WHERE scope = '{{ scope }}' --required
AND role_management_policy_assignment_name = '{{ role_management_policy_assignment_name }}' --required
;
```
</TabItem>
</Tabs>
