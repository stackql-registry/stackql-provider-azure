--- 
title: registration_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_assignments
  - managedservices
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

Creates, updates, deletes, gets or lists a <code>registration_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registration_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managedservices.registration_assignments" /></td></tr>
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
    <td>The fully qualified path of the registration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the registration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the registration assignment. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDefinition" /></td>
    <td><code>object</code></td>
    <td>The registration definition associated with the registration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified path of the registration definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the Azure resource (Microsoft.ManagedServices/registrationAssignments).</td>
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
    <td>The fully qualified path of the registration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the registration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the registration assignment. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDefinition" /></td>
    <td><code>object</code></td>
    <td>The registration definition associated with the registration assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified path of the registration definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the Azure resource (Microsoft.ManagedServices/registrationAssignments).</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-registration_assignment_id"><code>registration_assignment_id</code></a></td>
    <td><a href="#parameter-$expandRegistrationDefinition"><code>$expandRegistrationDefinition</code></a></td>
    <td>Gets the details of the specified registration assignment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$expandRegistrationDefinition"><code>$expandRegistrationDefinition</code></a></td>
    <td>Gets a list of the registration assignments.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-registration_assignment_id"><code>registration_assignment_id</code></a></td>
    <td></td>
    <td>Creates or updates a registration assignment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-registration_assignment_id"><code>registration_assignment_id</code></a></td>
    <td></td>
    <td>Creates or updates a registration assignment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-registration_assignment_id"><code>registration_assignment_id</code></a></td>
    <td></td>
    <td>Deletes the specified registration assignment.</td>
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
<tr id="parameter-registration_assignment_id">
    <td><CopyableCode code="registration_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The GUID of the registration assignment. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the resource. Required.</td>
</tr>
<tr id="parameter-$expandRegistrationDefinition">
    <td><CopyableCode code="$expandRegistrationDefinition" /></td>
    <td><code>boolean</code></td>
    <td>The flag indicating whether to return the registration definition details along with the registration assignment details. Default value is None.</td>
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

Gets the details of the specified registration assignment.

```sql
SELECT
id,
name,
provisioningState,
registrationDefinition,
registrationDefinitionId,
type
FROM azure.managedservices.registration_assignments
WHERE scope = '{{ scope }}' -- required
AND registration_assignment_id = '{{ registration_assignment_id }}' -- required
AND $expandRegistrationDefinition = '{{ $expandRegistrationDefinition }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of the registration assignments.

```sql
SELECT
id,
name,
provisioningState,
registrationDefinition,
registrationDefinitionId,
type
FROM azure.managedservices.registration_assignments
WHERE scope = '{{ scope }}' -- required
AND $expandRegistrationDefinition = '{{ $expandRegistrationDefinition }}'
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

Creates or updates a registration assignment.

```sql
INSERT INTO azure.managedservices.registration_assignments (
properties,
scope,
registration_assignment_id
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ registration_assignment_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: registration_assignments
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the registration_assignments resource.
    - name: registration_assignment_id
      value: "{{ registration_assignment_id }}"
      description: Required parameter for the registration_assignments resource.
    - name: properties
      description: |
        The properties of a registration assignment.
      value:
        registrationDefinitionId: "{{ registrationDefinitionId }}"
        provisioningState: "{{ provisioningState }}"
        registrationDefinition:
          properties:
            description: "{{ description }}"
            authorizations:
              - principalId: "{{ principalId }}"
                principalIdDisplayName: "{{ principalIdDisplayName }}"
                roleDefinitionId: "{{ roleDefinitionId }}"
                delegatedRoleDefinitionIds: "{{ delegatedRoleDefinitionIds }}"
            eligibleAuthorizations:
              - principalId: "{{ principalId }}"
                principalIdDisplayName: "{{ principalIdDisplayName }}"
                roleDefinitionId: "{{ roleDefinitionId }}"
                justInTimeAccessPolicy:
                  multiFactorAuthProvider: "{{ multiFactorAuthProvider }}"
                  maximumActivationDuration: "{{ maximumActivationDuration }}"
                  managedByTenantApprovers: "{{ managedByTenantApprovers }}"
            registrationDefinitionName: "{{ registrationDefinitionName }}"
            provisioningState: "{{ provisioningState }}"
            manageeTenantId: "{{ manageeTenantId }}"
            manageeTenantName: "{{ manageeTenantName }}"
            managedByTenantId: "{{ managedByTenantId }}"
            managedByTenantName: "{{ managedByTenantName }}"
          plan:
            name: "{{ name }}"
            publisher: "{{ publisher }}"
            product: "{{ product }}"
            version: "{{ version }}"
          id: "{{ id }}"
          type: "{{ type }}"
          name: "{{ name }}"
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

Creates or updates a registration assignment.

```sql
REPLACE azure.managedservices.registration_assignments
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND registration_assignment_id = '{{ registration_assignment_id }}' --required
RETURNING
id,
name,
properties,
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

Deletes the specified registration assignment.

```sql
DELETE FROM azure.managedservices.registration_assignments
WHERE scope = '{{ scope }}' --required
AND registration_assignment_id = '{{ registration_assignment_id }}' --required
;
```
</TabItem>
</Tabs>
