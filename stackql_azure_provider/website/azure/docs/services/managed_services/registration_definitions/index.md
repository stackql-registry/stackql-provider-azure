--- 
title: registration_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_definitions
  - managed_services
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

Creates, updates, deletes, gets or lists a <code>registration_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registration_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.registration_definitions" /></td></tr>
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
    <td>The fully qualified path of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The collection of authorization objects describing the access Azure Active Directory principals in the managedBy tenant will receive on the delegated resource in the managed tenant. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="eligibleAuthorizations" /></td>
    <td><code>array</code></td>
    <td>The collection of eligible authorization objects describing the just-in-time access Azure Active Directory principals in the managedBy tenant will receive on the delegated resource in the managed tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByTenantId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the managedBy tenant. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByTenantName" /></td>
    <td><code>string</code></td>
    <td>The name of the managedBy tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="manageeTenantId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the managed tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="manageeTenantName" /></td>
    <td><code>string</code></td>
    <td>The name of the managed tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The details for the Managed Services offer’s plan in Azure Marketplace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the registration definition. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDefinitionName" /></td>
    <td><code>string</code></td>
    <td>The name of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the Azure resource (Microsoft.ManagedServices/registrationDefinitions).</td>
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
    <td>The fully qualified path of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The collection of authorization objects describing the access Azure Active Directory principals in the managedBy tenant will receive on the delegated resource in the managed tenant. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="eligibleAuthorizations" /></td>
    <td><code>array</code></td>
    <td>The collection of eligible authorization objects describing the just-in-time access Azure Active Directory principals in the managedBy tenant will receive on the delegated resource in the managed tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByTenantId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the managedBy tenant. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByTenantName" /></td>
    <td><code>string</code></td>
    <td>The name of the managedBy tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="manageeTenantId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the managed tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="manageeTenantName" /></td>
    <td><code>string</code></td>
    <td>The name of the managed tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The details for the Managed Services offer’s plan in Azure Marketplace.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the registration definition. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDefinitionName" /></td>
    <td><code>string</code></td>
    <td>The name of the registration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the Azure resource (Microsoft.ManagedServices/registrationDefinitions).</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-registration_definition_id"><code>registration_definition_id</code></a></td>
    <td></td>
    <td>Gets the registration definition details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Gets a list of the registration definitions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-registration_definition_id"><code>registration_definition_id</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Creates or updates a registration definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-registration_definition_id"><code>registration_definition_id</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Creates or updates a registration definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-registration_definition_id"><code>registration_definition_id</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Deletes the registration definition.</td>
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
<tr id="parameter-registration_definition_id">
    <td><CopyableCode code="registration_definition_id" /></td>
    <td><code>string</code></td>
    <td>The GUID of the registration definition. Required.</td>
</tr>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the registration definition details.

```sql
SELECT
id,
name,
authorizations,
description,
eligibleAuthorizations,
managedByTenantId,
managedByTenantName,
manageeTenantId,
manageeTenantName,
plan,
provisioningState,
registrationDefinitionName,
type
FROM azure.managed_services.registration_definitions
WHERE scope = '{{ scope }}' -- required
AND registration_definition_id = '{{ registration_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of the registration definitions.

```sql
SELECT
id,
name,
authorizations,
description,
eligibleAuthorizations,
managedByTenantId,
managedByTenantName,
manageeTenantId,
manageeTenantName,
plan,
provisioningState,
registrationDefinitionName,
type
FROM azure.managed_services.registration_definitions
WHERE scope = '{{ scope }}' -- required
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

Creates or updates a registration definition.

```sql
INSERT INTO azure.managed_services.registration_definitions (
properties,
plan,
registration_definition_id,
scope
)
SELECT 
'{{ properties }}',
'{{ plan }}',
'{{ registration_definition_id }}',
'{{ scope }}'
RETURNING
id,
name,
plan,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: registration_definitions
  props:
    - name: registration_definition_id
      value: "{{ registration_definition_id }}"
      description: Required parameter for the registration_definitions resource.
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the registration_definitions resource.
    - name: properties
      description: |
        The properties of a registration definition.
      value:
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
              managedByTenantApprovers:
                - principalId: "{{ principalId }}"
                  principalIdDisplayName: "{{ principalIdDisplayName }}"
        registrationDefinitionName: "{{ registrationDefinitionName }}"
        managedByTenantId: "{{ managedByTenantId }}"
        provisioningState: "{{ provisioningState }}"
        manageeTenantId: "{{ manageeTenantId }}"
        manageeTenantName: "{{ manageeTenantName }}"
        managedByTenantName: "{{ managedByTenantName }}"
    - name: plan
      description: |
        The details for the Managed Services offer’s plan in Azure Marketplace.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        version: "{{ version }}"
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

Creates or updates a registration definition.

```sql
REPLACE azure.managed_services.registration_definitions
SET 
properties = '{{ properties }}',
plan = '{{ plan }}'
WHERE 
registration_definition_id = '{{ registration_definition_id }}' --required
AND scope = '{{ scope }}' --required
RETURNING
id,
name,
plan,
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

Deletes the registration definition.

```sql
DELETE FROM azure.managed_services.registration_definitions
WHERE registration_definition_id = '{{ registration_definition_id }}' --required
AND scope = '{{ scope }}' --required
;
```
</TabItem>
</Tabs>
