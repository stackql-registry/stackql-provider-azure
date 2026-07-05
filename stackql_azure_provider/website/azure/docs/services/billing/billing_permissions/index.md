--- 
title: billing_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_permissions
  - billing
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

Creates, updates, deletes, gets or lists a <code>billing_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_permissions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_customer"
    values={[
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer_at_billing_account', value: 'list_by_customer_at_billing_account' },
        { label: 'list_by_department', value: 'list_by_department' },
        { label: 'list_by_enrollment_account', value: 'list_by_enrollment_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="list_by_customer">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_invoice_section">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_billing_profile">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_customer_at_billing_account">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_department">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_enrollment_account">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_billing_account">

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
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is allowed to perform.</td>
</tr>
<tr>
    <td><CopyableCode code="notActions" /></td>
    <td><code>array</code></td>
    <td>The set of actions that the caller is not allowed to perform.</td>
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
    <td><a href="#list_by_customer"><CopyableCode code="list_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has for a customer.</td>
</tr>
<tr>
    <td><a href="#list_by_invoice_section"><CopyableCode code="list_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has for an invoice section.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has on a billing profile.</td>
</tr>
<tr>
    <td><a href="#list_by_customer_at_billing_account"><CopyableCode code="list_by_customer_at_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has for a customer at billing account level.</td>
</tr>
<tr>
    <td><a href="#list_by_department"><CopyableCode code="list_by_department" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has for a department.</td>
</tr>
<tr>
    <td><a href="#list_by_enrollment_account"><CopyableCode code="list_by_enrollment_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has for an enrollment account.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Lists the billing permissions the caller has on a billing account.</td>
</tr>
<tr>
    <td><a href="#check_access_by_billing_account"><CopyableCode code="check_access_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td></td>
    <td>Provides a list of check access response objects for a billing account.</td>
</tr>
<tr>
    <td><a href="#check_access_by_billing_profile"><CopyableCode code="check_access_by_billing_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td></td>
    <td>Provides a list of check access response objects for a billing profile.</td>
</tr>
<tr>
    <td><a href="#check_access_by_customer"><CopyableCode code="check_access_by_customer" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td></td>
    <td>Provides a list of check access response objects for a customer.</td>
</tr>
<tr>
    <td><a href="#check_access_by_department"><CopyableCode code="check_access_by_department" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a></td>
    <td></td>
    <td>Provides a list of check access response objects for a department.</td>
</tr>
<tr>
    <td><a href="#check_access_by_enrollment_account"><CopyableCode code="check_access_by_enrollment_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a></td>
    <td></td>
    <td>Provides a list of check access response objects for an enrollment account.</td>
</tr>
<tr>
    <td><a href="#check_access_by_invoice_section"><CopyableCode code="check_access_by_invoice_section" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Provides a list of check access response objects for an invoice section.</td>
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
    <td>The ID that uniquely identifies a billing account. Required.</td>
</tr>
<tr id="parameter-billing_profile_name">
    <td><CopyableCode code="billing_profile_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing profile. Required.</td>
</tr>
<tr id="parameter-customer_name">
    <td><CopyableCode code="customer_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer. Required.</td>
</tr>
<tr id="parameter-department_name">
    <td><CopyableCode code="department_name" /></td>
    <td><code>string</code></td>
    <td>The name of the department. Required.</td>
</tr>
<tr id="parameter-enrollment_account_name">
    <td><CopyableCode code="enrollment_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account. Required.</td>
</tr>
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_customer"
    values={[
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_customer_at_billing_account', value: 'list_by_customer_at_billing_account' },
        { label: 'list_by_department', value: 'list_by_department' },
        { label: 'list_by_enrollment_account', value: 'list_by_enrollment_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="list_by_customer">

Lists the billing permissions the caller has for a customer.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_invoice_section">

Lists the billing permissions the caller has for an invoice section.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists the billing permissions the caller has on a billing profile.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_customer_at_billing_account">

Lists the billing permissions the caller has for a customer at billing account level.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_department">

Lists the billing permissions the caller has for a department.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND department_name = '{{ department_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_enrollment_account">

Lists the billing permissions the caller has for an enrollment account.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND enrollment_account_name = '{{ enrollment_account_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the billing permissions the caller has on a billing account.

```sql
SELECT
actions,
notActions
FROM azure.billing.billing_permissions
WHERE billing_account_name = '{{ billing_account_name }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_access_by_billing_account"
    values={[
        { label: 'check_access_by_billing_account', value: 'check_access_by_billing_account' },
        { label: 'check_access_by_billing_profile', value: 'check_access_by_billing_profile' },
        { label: 'check_access_by_customer', value: 'check_access_by_customer' },
        { label: 'check_access_by_department', value: 'check_access_by_department' },
        { label: 'check_access_by_enrollment_account', value: 'check_access_by_enrollment_account' },
        { label: 'check_access_by_invoice_section', value: 'check_access_by_invoice_section' }
    ]}
>
<TabItem value="check_access_by_billing_account">

Provides a list of check access response objects for a billing account.

```sql
EXEC azure.billing.billing_permissions.check_access_by_billing_account 
@billing_account_name='{{ billing_account_name }}' --required 
@@json=
'{
"actions": "{{ actions }}"
}'
;
```
</TabItem>
<TabItem value="check_access_by_billing_profile">

Provides a list of check access response objects for a billing profile.

```sql
EXEC azure.billing.billing_permissions.check_access_by_billing_profile 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required 
@@json=
'{
"actions": "{{ actions }}"
}'
;
```
</TabItem>
<TabItem value="check_access_by_customer">

Provides a list of check access response objects for a customer.

```sql
EXEC azure.billing.billing_permissions.check_access_by_customer 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@customer_name='{{ customer_name }}' --required 
@@json=
'{
"actions": "{{ actions }}"
}'
;
```
</TabItem>
<TabItem value="check_access_by_department">

Provides a list of check access response objects for a department.

```sql
EXEC azure.billing.billing_permissions.check_access_by_department 
@billing_account_name='{{ billing_account_name }}' --required, 
@department_name='{{ department_name }}' --required 
@@json=
'{
"actions": "{{ actions }}"
}'
;
```
</TabItem>
<TabItem value="check_access_by_enrollment_account">

Provides a list of check access response objects for an enrollment account.

```sql
EXEC azure.billing.billing_permissions.check_access_by_enrollment_account 
@billing_account_name='{{ billing_account_name }}' --required, 
@enrollment_account_name='{{ enrollment_account_name }}' --required 
@@json=
'{
"actions": "{{ actions }}"
}'
;
```
</TabItem>
<TabItem value="check_access_by_invoice_section">

Provides a list of check access response objects for an invoice section.

```sql
EXEC azure.billing.billing_permissions.check_access_by_invoice_section 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@invoice_section_name='{{ invoice_section_name }}' --required 
@@json=
'{
"actions": "{{ actions }}"
}'
;
```
</TabItem>
</Tabs>
