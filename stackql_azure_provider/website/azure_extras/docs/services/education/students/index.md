--- 
title: students
hide_title: false
hide_table_of_contents: false
keywords:
  - students
  - education
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>students</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="students" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.students" /></td></tr>
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
    <td><CopyableCode code="budget" /></td>
    <td><code>object</code></td>
    <td>Student Budget. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date student was added to the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>Student Email. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date this student is set to expire from the lab. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="firstName" /></td>
    <td><code>string</code></td>
    <td>First Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastName" /></td>
    <td><code>string</code></td>
    <td>Last Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Student Role. Required. Known values are: "Student" and "Admin". (Student, Admin)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Student Lab Status. Known values are: "Active", "Disabled", "Expired", "Pending", and "Deleted". (Active, Disabled, Expired, Pending, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionAlias" /></td>
    <td><code>string</code></td>
    <td>Subscription alias.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionInviteLastSentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>subscription invite last sent date.</td>
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
    <td><CopyableCode code="budget" /></td>
    <td><code>object</code></td>
    <td>Student Budget. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date student was added to the lab.</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>Student Email. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date this student is set to expire from the lab. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="firstName" /></td>
    <td><code>string</code></td>
    <td>First Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastName" /></td>
    <td><code>string</code></td>
    <td>Last Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Student Role. Required. Known values are: "Student" and "Admin". (Student, Admin)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Student Lab Status. Known values are: "Active", "Disabled", "Expired", "Pending", and "Deleted". (Active, Disabled, Expired, Pending, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionAlias" /></td>
    <td><code>string</code></td>
    <td>Subscription alias.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionInviteLastSentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>subscription invite last sent date.</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-student_alias"><code>student_alias</code></a></td>
    <td></td>
    <td>Get the details for a specific student in the specified lab by student alias.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a></td>
    <td>Get a list of details about students that are associated with the specified lab.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-student_alias"><code>student_alias</code></a></td>
    <td></td>
    <td>Create and add a new student to the specified lab or update the details of an existing student in a lab. Note the student must have a valid tenant to accept the lab after they have been added to lab.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-student_alias"><code>student_alias</code></a></td>
    <td></td>
    <td>Create and add a new student to the specified lab or update the details of an existing student in a lab. Note the student must have a valid tenant to accept the lab after they have been added to lab.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-student_alias"><code>student_alias</code></a></td>
    <td></td>
    <td>Delete the specified student based on the student alias.</td>
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
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account. Required.</td>
</tr>
<tr id="parameter-billing_profile_name">
    <td><CopyableCode code="billing_profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile. Required.</td>
</tr>
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section. Required.</td>
</tr>
<tr id="parameter-student_alias">
    <td><CopyableCode code="student_alias" /></td>
    <td><code>string</code></td>
    <td>The student alias. Required.</td>
</tr>
<tr id="parameter-includeDeleted">
    <td><CopyableCode code="includeDeleted" /></td>
    <td><code>boolean</code></td>
    <td>May be used to show deleted items. Default value is None.</td>
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

Get the details for a specific student in the specified lab by student alias.

```sql
SELECT
id,
name,
budget,
effectiveDate,
email,
expirationDate,
firstName,
lastName,
role,
status,
subscriptionAlias,
subscriptionId,
subscriptionInviteLastSentDate,
systemData,
type
FROM azure_extras.education.students
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND student_alias = '{{ student_alias }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of details about students that are associated with the specified lab.

```sql
SELECT
id,
name,
budget,
effectiveDate,
email,
expirationDate,
firstName,
lastName,
role,
status,
subscriptionAlias,
subscriptionId,
subscriptionInviteLastSentDate,
systemData,
type
FROM azure_extras.education.students
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
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

Create and add a new student to the specified lab or update the details of an existing student in a lab. Note the student must have a valid tenant to accept the lab after they have been added to lab.

```sql
INSERT INTO azure_extras.education.students (
properties,
billing_account_name,
billing_profile_name,
invoice_section_name,
student_alias
)
SELECT 
'{{ properties }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}',
'{{ invoice_section_name }}',
'{{ student_alias }}'
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
- name: students
  props:
    - name: billing_account_name
      value: "{{ billing_account_name }}"
      description: Required parameter for the students resource.
    - name: billing_profile_name
      value: "{{ billing_profile_name }}"
      description: Required parameter for the students resource.
    - name: invoice_section_name
      value: "{{ invoice_section_name }}"
      description: Required parameter for the students resource.
    - name: student_alias
      value: "{{ student_alias }}"
      description: Required parameter for the students resource.
    - name: properties
      description: |
        Get student response properties.
      value:
        firstName: "{{ firstName }}"
        lastName: "{{ lastName }}"
        email: "{{ email }}"
        role: "{{ role }}"
        budget:
          currency: "{{ currency }}"
          value: {{ value }}
        subscriptionId: "{{ subscriptionId }}"
        expirationDate: "{{ expirationDate }}"
        status: "{{ status }}"
        effectiveDate: "{{ effectiveDate }}"
        subscriptionAlias: "{{ subscriptionAlias }}"
        subscriptionInviteLastSentDate: "{{ subscriptionInviteLastSentDate }}"
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

Create and add a new student to the specified lab or update the details of an existing student in a lab. Note the student must have a valid tenant to accept the lab after they have been added to lab.

```sql
REPLACE azure_extras.education.students
SET 
properties = '{{ properties }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND invoice_section_name = '{{ invoice_section_name }}' --required
AND student_alias = '{{ student_alias }}' --required
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

Delete the specified student based on the student alias.

```sql
DELETE FROM azure_extras.education.students
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND invoice_section_name = '{{ invoice_section_name }}' --required
AND student_alias = '{{ student_alias }}' --required
;
```
</TabItem>
</Tabs>
