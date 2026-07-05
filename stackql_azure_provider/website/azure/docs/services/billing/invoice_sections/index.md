--- 
title: invoice_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - invoice_sections
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

Creates, updates, deletes, gets or lists an <code>invoice_sections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invoice_sections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.invoice_sections" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' }
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="reasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified invoice section status. Known values are: "Other", "PastDue", "UnusualActivity", "SpendingLimitReached", and "SpendingLimitExpired". (Other, PastDue, UnusualActivity, SpendingLimitReached, SpendingLimitExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Identifies the status of an invoice section. Known values are: "Other", "Active", "Deleted", "Disabled", "UnderReview", "Warned", and "Restricted". (Other, Active, Deleted, Disabled, UnderReview, Warned, Restricted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>The system generated unique identifier for an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="targetCloud" /></td>
    <td><code>string</code></td>
    <td>Identifies the cloud environments that are associated with an invoice section. This is a system managed optional field and gets updated as the invoice section gets associated with accounts in various clouds.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="reasonCode" /></td>
    <td><code>string</code></td>
    <td>Reason for the specified invoice section status. Known values are: "Other", "PastDue", "UnusualActivity", "SpendingLimitReached", and "SpendingLimitExpired". (Other, PastDue, UnusualActivity, SpendingLimitReached, SpendingLimitExpired)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Identifies the status of an invoice section. Known values are: "Other", "Active", "Deleted", "Disabled", "UnderReview", "Warned", and "Restricted". (Other, Active, Deleted, Disabled, UnderReview, Warned, Restricted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>The system generated unique identifier for an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="targetCloud" /></td>
    <td><code>string</code></td>
    <td>Identifies the cloud environments that are associated with an invoice section. This is a system managed optional field and gets updated as the invoice section gets associated with accounts in various clouds.</td>
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
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Gets an invoice section by its ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-includeDeleted"><code>includeDeleted</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists the invoice sections that a user has access to. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Deletes an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#validate_delete_eligibility"><CopyableCode code="validate_delete_eligibility" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td></td>
    <td>Validates if the invoice section can be deleted. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
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
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section. Required.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>boolean</code></td>
    <td>The count query option allows clients to request a count of the matching resources included with the resources in the response. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter a collection of resources that are addressed by a request URL. Default value is None.</td>
</tr>
<tr id="parameter-includeDeleted">
    <td><CopyableCode code="includeDeleted" /></td>
    <td><code>boolean</code></td>
    <td>Can be used to get deleted invoice sections. Default value is False.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>The orderby query option allows clients to request resources in a particular order. Default value is None.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>The search query option allows clients to request items within a collection matching a free-text search expression. search is only supported for string fields. Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The skip query option requests the number of items in the queried collection that are to be skipped and not included in the result. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The top query option requests the number of items in the queried collection to be included in the result. The maximum supported value for top is 50. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' }
    ]}
>
<TabItem value="get">

Gets an invoice section by its ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
displayName,
provisioningState,
reasonCode,
state,
systemData,
systemId,
tags,
targetCloud,
type
FROM azure.billing.invoice_sections
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists the invoice sections that a user has access to. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
displayName,
provisioningState,
reasonCode,
state,
systemData,
systemId,
tags,
targetCloud,
type
FROM azure.billing.invoice_sections
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND includeDeleted = '{{ includeDeleted }}'
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
AND count = '{{ count }}'
AND search = '{{ search }}'
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

Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
INSERT INTO azure.billing.invoice_sections (
properties,
tags,
billing_account_name,
billing_profile_name,
invoice_section_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}',
'{{ invoice_section_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: invoice_sections
  props:
    - name: billing_account_name
      value: "{{ billing_account_name }}"
      description: Required parameter for the invoice_sections resource.
    - name: billing_profile_name
      value: "{{ billing_profile_name }}"
      description: Required parameter for the invoice_sections resource.
    - name: invoice_section_name
      value: "{{ invoice_section_name }}"
      description: Required parameter for the invoice_sections resource.
    - name: properties
      description: |
        An invoice section.
      value:
        provisioningState: "{{ provisioningState }}"
        displayName: "{{ displayName }}"
        state: "{{ state }}"
        reasonCode: "{{ reasonCode }}"
        systemId: "{{ systemId }}"
        targetCloud: "{{ targetCloud }}"
        tags: "{{ tags }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? /.
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

Creates or updates an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

```sql
REPLACE azure.billing.invoice_sections
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND invoice_section_name = '{{ invoice_section_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
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

Deletes an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
DELETE FROM azure.billing.invoice_sections
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND invoice_section_name = '{{ invoice_section_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_delete_eligibility"
    values={[
        { label: 'validate_delete_eligibility', value: 'validate_delete_eligibility' }
    ]}
>
<TabItem value="validate_delete_eligibility">

Validates if the invoice section can be deleted. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.invoice_sections.validate_delete_eligibility 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@invoice_section_name='{{ invoice_section_name }}' --required
;
```
</TabItem>
</Tabs>
