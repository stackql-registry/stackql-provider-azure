--- 
title: management_group_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_subscriptions
  - managementgroups
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

Creates, updates, deletes, gets or lists a <code>management_group_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="management_group_subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managementgroups.management_group_subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_subscription"
    values={[
        { label: 'get_subscription', value: 'get_subscription' },
        { label: 'get_subscriptions_under_management_group', value: 'get_subscriptions_under_management_group' }
    ]}
>
<TabItem value="get_subscription">

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
    <td>The friendly name of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td>The ID of the parent management group.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenant" /></td>
    <td><code>string</code></td>
    <td>The AAD Tenant ID associated with the subscription. For example, 00000000-0000-0000-0000-000000000000.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_subscriptions_under_management_group">

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
    <td>The friendly name of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td>The ID of the parent management group.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenant" /></td>
    <td><code>string</code></td>
    <td>The AAD Tenant ID associated with the subscription. For example, 00000000-0000-0000-0000-000000000000.</td>
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
    <td><a href="#get_subscription"><CopyableCode code="get_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Retrieves details about given subscription which is associated with the management group.</td>
</tr>
<tr>
    <td><a href="#get_subscriptions_under_management_group"><CopyableCode code="get_subscriptions_under_management_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-$skiptoken"><code>$skiptoken</code></a></td>
    <td>Retrieves details about all subscriptions which are associated with the management group.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>Associates existing subscription with the management group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-Cache-Control"><code>Cache-Control</code></a></td>
    <td>De-associates subscription from the management group.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>Management Group ID. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>Subscription ID. Required.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>string</code></td>
    <td>Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-Cache-Control">
    <td><CopyableCode code="Cache-Control" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_subscription"
    values={[
        { label: 'get_subscription', value: 'get_subscription' },
        { label: 'get_subscriptions_under_management_group', value: 'get_subscriptions_under_management_group' }
    ]}
>
<TabItem value="get_subscription">

Retrieves details about given subscription which is associated with the management group.

```sql
SELECT
id,
name,
displayName,
parent,
state,
systemData,
tenant,
type
FROM azure.managementgroups.management_group_subscriptions
WHERE group_id = '{{ group_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND Cache-Control = '{{ Cache-Control }}'
;
```
</TabItem>
<TabItem value="get_subscriptions_under_management_group">

Retrieves details about all subscriptions which are associated with the management group.

```sql
SELECT
id,
name,
displayName,
parent,
state,
systemData,
tenant,
type
FROM azure.managementgroups.management_group_subscriptions
WHERE group_id = '{{ group_id }}' -- required
AND $skiptoken = '{{ $skiptoken }}'
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

Associates existing subscription with the management group.

```sql
INSERT INTO azure.managementgroups.management_group_subscriptions (
group_id,
subscription_id,
Cache-Control
)
SELECT 
'{{ group_id }}',
'{{ subscription_id }}',
'{{ Cache-Control }}'
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
- name: management_group_subscriptions
  props:
    - name: group_id
      value: "{{ group_id }}"
      description: Required parameter for the management_group_subscriptions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the management_group_subscriptions resource.
    - name: Cache-Control
      value: "{{ Cache-Control }}"
      description: Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
      description: Indicates whether the request should utilize any caches. Populate the header with 'no-cache' value to bypass existing caches. Default value is "no-cache".
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

De-associates subscription from the management group.

```sql
DELETE FROM azure.managementgroups.management_group_subscriptions
WHERE group_id = '{{ group_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND Cache-Control = '{{ Cache-Control }}'
;
```
</TabItem>
</Tabs>
