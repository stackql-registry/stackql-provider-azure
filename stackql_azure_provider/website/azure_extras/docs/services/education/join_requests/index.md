--- 
title: join_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - join_requests
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

Creates, updates, deletes, gets or lists a <code>join_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="join_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.education.join_requests" /></td></tr>
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
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>join request email.</td>
</tr>
<tr>
    <td><CopyableCode code="firstName" /></td>
    <td><code>string</code></td>
    <td>First Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastName" /></td>
    <td><code>string</code></td>
    <td>Last Name.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Join request status. Known values are: "Pending" and "Denied". (Pending, Denied)</td>
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
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>join request email.</td>
</tr>
<tr>
    <td><CopyableCode code="firstName" /></td>
    <td><code>string</code></td>
    <td>First Name.</td>
</tr>
<tr>
    <td><CopyableCode code="lastName" /></td>
    <td><code>string</code></td>
    <td>Last Name.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Join request status. Known values are: "Pending" and "Denied". (Pending, Denied)</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-join_request_name"><code>join_request_name</code></a></td>
    <td></td>
    <td>get student join requests.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-includeDenied"><code>includeDenied</code></a></td>
    <td>get student join requests.</td>
</tr>
<tr>
    <td><a href="#approve"><CopyableCode code="approve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-join_request_name"><code>join_request_name</code></a></td>
    <td></td>
    <td>Approve student joining the redeemable lab.</td>
</tr>
<tr>
    <td><a href="#deny"><CopyableCode code="deny" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-join_request_name"><code>join_request_name</code></a></td>
    <td></td>
    <td>Deny student joining the redeemable lab.</td>
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
<tr id="parameter-join_request_name">
    <td><CopyableCode code="join_request_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a join request. Required.</td>
</tr>
<tr id="parameter-includeDenied">
    <td><CopyableCode code="includeDenied" /></td>
    <td><code>boolean</code></td>
    <td>Include denied. Default value is None.</td>
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

get student join requests.

```sql
SELECT
id,
name,
email,
firstName,
lastName,
status,
systemData,
type
FROM azure_extras.education.join_requests
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND join_request_name = '{{ join_request_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

get student join requests.

```sql
SELECT
id,
name,
email,
firstName,
lastName,
status,
systemData,
type
FROM azure_extras.education.join_requests
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND includeDenied = '{{ includeDenied }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="approve"
    values={[
        { label: 'approve', value: 'approve' },
        { label: 'deny', value: 'deny' }
    ]}
>
<TabItem value="approve">

Approve student joining the redeemable lab.

```sql
EXEC azure_extras.education.join_requests.approve 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@invoice_section_name='{{ invoice_section_name }}' --required, 
@join_request_name='{{ join_request_name }}' --required
;
```
</TabItem>
<TabItem value="deny">

Deny student joining the redeemable lab.

```sql
EXEC azure_extras.education.join_requests.deny 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@invoice_section_name='{{ invoice_section_name }}' --required, 
@join_request_name='{{ join_request_name }}' --required
;
```
</TabItem>
</Tabs>
