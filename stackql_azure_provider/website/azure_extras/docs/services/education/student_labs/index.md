--- 
title: student_labs
hide_title: false
hide_table_of_contents: false
keywords:
  - student_labs
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

Creates, updates, deletes, gets or lists a <code>student_labs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="student_labs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.student_labs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Student Budget.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detail description of this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Student lab Display Name.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>User Added Date.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the lab will expire and by default will be the expiration date for each student in this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="labScope" /></td>
    <td><code>string</code></td>
    <td>Lab Scope. /providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;/invoiceSections/&#123;invoiceSectionName&#125;/providers/Microsoft.Education/labs/default.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Student Role. Known values are: "Student" and "Admin". (Student, Admin)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Student Lab Status. Known values are: "Active", "Disabled", "Expired", "Pending", and "Deleted". (Active, Disabled, Expired, Pending, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription Id.</td>
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
<TabItem value="list_all">

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
    <td>Student Budget.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detail description of this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Student lab Display Name.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>User Added Date.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date the lab will expire and by default will be the expiration date for each student in this lab.</td>
</tr>
<tr>
    <td><CopyableCode code="labScope" /></td>
    <td><code>string</code></td>
    <td>Lab Scope. /providers/Microsoft.Billing/billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;/invoiceSections/&#123;invoiceSectionName&#125;/providers/Microsoft.Education/labs/default.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>Student Role. Known values are: "Student" and "Admin". (Student, Admin)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Student Lab Status. Known values are: "Active", "Disabled", "Expired", "Pending", and "Deleted". (Active, Disabled, Expired, Pending, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Subscription Id.</td>
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
    <td><a href="#parameter-student_lab_name"><code>student_lab_name</code></a></td>
    <td></td>
    <td>Get the details for a specified lab associated with the student lab.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of all labs associated with the caller of the API.</td>
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
<tr id="parameter-student_lab_name">
    <td><CopyableCode code="student_lab_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a student lab. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get the details for a specified lab associated with the student lab.

```sql
SELECT
id,
name,
budget,
description,
displayName,
effectiveDate,
expirationDate,
labScope,
role,
status,
subscriptionId,
systemData,
type
FROM azure_extras.education.student_labs
WHERE student_lab_name = '{{ student_lab_name }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Get a list of all labs associated with the caller of the API.

```sql
SELECT
id,
name,
budget,
description,
displayName,
effectiveDate,
expirationDate,
labScope,
role,
status,
subscriptionId,
systemData,
type
FROM azure_extras.education.student_labs
;
```
</TabItem>
</Tabs>
