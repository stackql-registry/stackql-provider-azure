--- 
title: subscription_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_policy
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

Creates, updates, deletes, gets or lists a <code>subscription_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscription_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.subscription_policy" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_policy_for_tenant"
    values={[
        { label: 'list_policy_for_tenant', value: 'list_policy_for_tenant' }
    ]}
>
<TabItem value="list_policy_for_tenant">

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
    <td><CopyableCode code="blockSubscriptionsIntoTenant" /></td>
    <td><code>boolean</code></td>
    <td>Blocks the entering of subscriptions into user's tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="blockSubscriptionsLeavingTenant" /></td>
    <td><code>boolean</code></td>
    <td>Blocks the leaving of subscriptions from user's tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="exemptedPrincipals" /></td>
    <td><code>array</code></td>
    <td>List of user objectIds that are exempted from the set subscription tenant policies for the user's tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>Policy Id.</td>
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
    <td><a href="#list_policy_for_tenant"><CopyableCode code="list_policy_for_tenant" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the subscription tenant policy for the user's tenant.</td>
</tr>
<tr>
    <td><a href="#get_policy_for_tenant"><CopyableCode code="get_policy_for_tenant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Get the subscription tenant policy for the user's tenant.</td>
</tr>
<tr>
    <td><a href="#add_update_policy_for_tenant"><CopyableCode code="add_update_policy_for_tenant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Create or Update Subscription tenant policy for user's tenant.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_policy_for_tenant"
    values={[
        { label: 'list_policy_for_tenant', value: 'list_policy_for_tenant' }
    ]}
>
<TabItem value="list_policy_for_tenant">

Get the subscription tenant policy for the user's tenant.

```sql
SELECT
id,
name,
blockSubscriptionsIntoTenant,
blockSubscriptionsLeavingTenant,
exemptedPrincipals,
policyId,
systemData,
type
FROM azure.subscription.subscription_policy
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_policy_for_tenant"
    values={[
        { label: 'get_policy_for_tenant', value: 'get_policy_for_tenant' },
        { label: 'add_update_policy_for_tenant', value: 'add_update_policy_for_tenant' }
    ]}
>
<TabItem value="get_policy_for_tenant">

Get the subscription tenant policy for the user's tenant.

```sql
EXEC azure.subscription.subscription_policy.get_policy_for_tenant 

;
```
</TabItem>
<TabItem value="add_update_policy_for_tenant">

Create or Update Subscription tenant policy for user's tenant.

```sql
EXEC azure.subscription.subscription_policy.add_update_policy_for_tenant 
@@json=
'{
"blockSubscriptionsLeavingTenant": {{ blockSubscriptionsLeavingTenant }}, 
"blockSubscriptionsIntoTenant": {{ blockSubscriptionsIntoTenant }}, 
"exemptedPrincipals": "{{ exemptedPrincipals }}"
}'
;
```
</TabItem>
</Tabs>
