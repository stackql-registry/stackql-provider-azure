--- 
title: discounts
hide_title: false
hide_table_of_contents: false
keywords:
  - discounts
  - billing_benefits
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

Creates, updates, deletes, gets or lists a <code>discounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="discounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.discounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-discount_name"><code>discount_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create discount.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-discount_name"><code>discount_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete discount. Clears the metadata from the user's view.</td>
</tr>
<tr>
    <td><a href="#resource_group_list"><CopyableCode code="resource_group_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List discounts at resource group level.</td>
</tr>
<tr>
    <td><a href="#subscription_list"><CopyableCode code="subscription_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List discounts at subscription level.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-discount_name"><code>discount_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel discount. Stops applying the benefit.</td>
</tr>
<tr>
    <td><a href="#scope_list"><CopyableCode code="scope_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>List discounts that are applicable for a given scope. Currently supported scopes: billing accounts.</td>
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
<tr id="parameter-discount_name">
    <td><CopyableCode code="discount_name" /></td>
    <td><code>string</code></td>
    <td>Name of the discount. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the benefits are listed. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create discount.

```sql
INSERT INTO azure.billing_benefits.discounts (
tags,
location,
properties,
managedBy,
kind,
identity,
sku,
plan,
resource_group_name,
discount_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ resource_group_name }}',
'{{ discount_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: discounts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the discounts resource.
    - name: discount_name
      value: "{{ discount_name }}"
      description: Required parameter for the discounts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the discounts resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Discount properties.
      value:
        entityType: "{{ entityType }}"
        productCode: "{{ productCode }}"
        startAt: "{{ startAt }}"
        systemId: "{{ systemId }}"
        provisioningState: "{{ provisioningState }}"
        billingAccountResourceId: "{{ billingAccountResourceId }}"
        billingProfileResourceId: "{{ billingProfileResourceId }}"
        customerResourceId: "{{ customerResourceId }}"
        displayName: "{{ displayName }}"
        status: "{{ status }}"
        benefitResourceId: "{{ benefitResourceId }}"
        appliedScopeType: "{{ appliedScopeType }}"
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: identity
      description: |
        Managed service identity (system assigned and/or user assigned identities).
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        The resource model definition representing SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: plan
      description: |
        Plan for the resource.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
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

Delete discount. Clears the metadata from the user's view.

```sql
DELETE FROM azure.billing_benefits.discounts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND discount_name = '{{ discount_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resource_group_list"
    values={[
        { label: 'resource_group_list', value: 'resource_group_list' },
        { label: 'subscription_list', value: 'subscription_list' },
        { label: 'cancel', value: 'cancel' },
        { label: 'scope_list', value: 'scope_list' }
    ]}
>
<TabItem value="resource_group_list">

List discounts at resource group level.

```sql
EXEC azure.billing_benefits.discounts.resource_group_list 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="subscription_list">

List discounts at subscription level.

```sql
EXEC azure.billing_benefits.discounts.subscription_list 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cancel">

Cancel discount. Stops applying the benefit.

```sql
EXEC azure.billing_benefits.discounts.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@discount_name='{{ discount_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="scope_list">

List discounts that are applicable for a given scope. Currently supported scopes: billing accounts.

```sql
EXEC azure.billing_benefits.discounts.scope_list 
@scope='{{ scope }}' --required
;
```
</TabItem>
</Tabs>
