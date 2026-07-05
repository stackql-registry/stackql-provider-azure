--- 
title: alias
hide_title: false
hide_table_of_contents: false
keywords:
  - alias
  - subscription
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

Creates, updates, deletes, gets or lists an <code>alias</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alias" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.alias" /></td></tr>
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
    <td><CopyableCode code="acceptOwnershipState" /></td>
    <td><code>string</code></td>
    <td>The accept ownership state of the resource. Known values are: "Pending", "Completed", and "Expired". (Pending, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="acceptOwnershipUrl" /></td>
    <td><code>string</code></td>
    <td>Url to accept ownership of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>Billing scope of the subscription. For CustomerLed and FieldLed - /billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;/invoiceSections/&#123;invoiceSectionName&#125; For PartnerLed - /billingAccounts/&#123;billingAccountName&#125;/customers/&#123;customerName&#125; For Legacy EA - /billingAccounts/&#123;billingAccountName&#125;/enrollmentAccounts/&#123;enrollmentAccountName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string</code></td>
    <td>Created Time.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupId" /></td>
    <td><code>string</code></td>
    <td>The Management Group Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Accepted", "Succeeded", and "Failed". (Accepted, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resellerId" /></td>
    <td><code>string</code></td>
    <td>Reseller Id.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Newly created subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionOwnerId" /></td>
    <td><code>string</code></td>
    <td>Owner Id of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workload" /></td>
    <td><code>string</code></td>
    <td>The workload type of the subscription. It can be either Production or DevTest. Known values are: "Production" and "DevTest". (Production, DevTest)</td>
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
    <td><CopyableCode code="acceptOwnershipState" /></td>
    <td><code>string</code></td>
    <td>The accept ownership state of the resource. Known values are: "Pending", "Completed", and "Expired". (Pending, Completed, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="acceptOwnershipUrl" /></td>
    <td><code>string</code></td>
    <td>Url to accept ownership of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="billingScope" /></td>
    <td><code>string</code></td>
    <td>Billing scope of the subscription. For CustomerLed and FieldLed - /billingAccounts/&#123;billingAccountName&#125;/billingProfiles/&#123;billingProfileName&#125;/invoiceSections/&#123;invoiceSectionName&#125; For PartnerLed - /billingAccounts/&#123;billingAccountName&#125;/customers/&#123;customerName&#125; For Legacy EA - /billingAccounts/&#123;billingAccountName&#125;/enrollmentAccounts/&#123;enrollmentAccountName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string</code></td>
    <td>Created Time.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="managementGroupId" /></td>
    <td><code>string</code></td>
    <td>The Management Group Id.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "Accepted", "Succeeded", and "Failed". (Accepted, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resellerId" /></td>
    <td><code>string</code></td>
    <td>Reseller Id.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Newly created subscription Id.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionOwnerId" /></td>
    <td><code>string</code></td>
    <td>Owner Id of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workload" /></td>
    <td><code>string</code></td>
    <td>The workload type of the subscription. It can be either Production or DevTest. Known values are: "Production" and "DevTest". (Production, DevTest)</td>
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
    <td><a href="#parameter-alias_name"><code>alias_name</code></a></td>
    <td></td>
    <td>Get Alias Subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>List Alias Subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-alias_name"><code>alias_name</code></a></td>
    <td></td>
    <td>Create Alias Subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-alias_name"><code>alias_name</code></a></td>
    <td></td>
    <td>Delete Alias.</td>
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
<tr id="parameter-alias_name">
    <td><CopyableCode code="alias_name" /></td>
    <td><code>string</code></td>
    <td>AliasName is the name for the subscription creation request. Note that this is not the same as subscription name and this doesn’t have any other lifecycle need beyond the request for subscription creation. Required.</td>
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

Get Alias Subscription.

```sql
SELECT
id,
name,
acceptOwnershipState,
acceptOwnershipUrl,
billingScope,
createdTime,
displayName,
managementGroupId,
provisioningState,
resellerId,
subscriptionId,
subscriptionOwnerId,
systemData,
tags,
type,
workload
FROM azure.subscription.alias
WHERE alias_name = '{{ alias_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Alias Subscription.

```sql
SELECT
id,
name,
acceptOwnershipState,
acceptOwnershipUrl,
billingScope,
createdTime,
displayName,
managementGroupId,
provisioningState,
resellerId,
subscriptionId,
subscriptionOwnerId,
systemData,
tags,
type,
workload
FROM azure.subscription.alias
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

Create Alias Subscription.

```sql
INSERT INTO azure.subscription.alias (
properties,
alias_name
)
SELECT 
'{{ properties }}',
'{{ alias_name }}'
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
- name: alias
  props:
    - name: alias_name
      value: "{{ alias_name }}"
      description: Required parameter for the alias resource.
    - name: properties
      description: |
        Put alias request properties.
      value:
        displayName: "{{ displayName }}"
        workload: "{{ workload }}"
        billingScope: "{{ billingScope }}"
        subscriptionId: "{{ subscriptionId }}"
        resellerId: "{{ resellerId }}"
        additionalProperties:
          managementGroupId: "{{ managementGroupId }}"
          subscriptionTenantId: "{{ subscriptionTenantId }}"
          subscriptionOwnerId: "{{ subscriptionOwnerId }}"
          tags: "{{ tags }}"
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

Delete Alias.

```sql
DELETE FROM azure.subscription.alias
WHERE alias_name = '{{ alias_name }}' --required
;
```
</TabItem>
</Tabs>
