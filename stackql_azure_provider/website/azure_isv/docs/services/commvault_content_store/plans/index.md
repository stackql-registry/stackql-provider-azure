--- 
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
  - commvault_content_store
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.commvault_content_store.plans" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cloud_account', value: 'list_by_cloud_account' }
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the Commvault Plan. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="retention" /></td>
    <td><code>object</code></td>
    <td>The Commvault Plan Retention.</td>
</tr>
<tr>
    <td><CopyableCode code="schedules" /></td>
    <td><code>array</code></td>
    <td>The Commvault Plan Schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePlans" /></td>
    <td><code>array</code></td>
    <td>The storage plans associated with the Commvault Plan. Required.</td>
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
<TabItem value="list_by_cloud_account">

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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the Commvault Plan. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="retention" /></td>
    <td><code>object</code></td>
    <td>The Commvault Plan Retention.</td>
</tr>
<tr>
    <td><CopyableCode code="schedules" /></td>
    <td><code>array</code></td>
    <td>The Commvault Plan Schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="storagePlans" /></td>
    <td><code>array</code></td>
    <td>The storage plans associated with the Commvault Plan. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-plan_name"><code>plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a CommvaultPlan.</td>
</tr>
<tr>
    <td><a href="#list_by_cloud_account"><CopyableCode code="list_by_cloud_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List CommvaultPlan resources by CloudAccount.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-plan_name"><code>plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a CommvaultPlan.</td>
</tr>
<tr>
    <td><a href="#create_orupdate"><CopyableCode code="create_orupdate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cloud_account_name"><code>cloud_account_name</code></a>, <a href="#parameter-plan_name"><code>plan_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a CommvaultPlan.</td>
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
<tr id="parameter-cloud_account_name">
    <td><CopyableCode code="cloud_account_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Cloud Account resource. Required.</td>
</tr>
<tr id="parameter-plan_name">
    <td><CopyableCode code="plan_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Plan resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_cloud_account', value: 'list_by_cloud_account' }
    ]}
>
<TabItem value="get">

Get a CommvaultPlan.

```sql
SELECT
id,
name,
location,
provisioningState,
retention,
schedules,
storagePlans,
systemData,
type
FROM azure_isv.commvault_content_store.plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_account_name = '{{ cloud_account_name }}' -- required
AND plan_name = '{{ plan_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cloud_account">

List CommvaultPlan resources by CloudAccount.

```sql
SELECT
id,
name,
location,
provisioningState,
retention,
schedules,
storagePlans,
systemData,
type
FROM azure_isv.commvault_content_store.plans
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cloud_account_name = '{{ cloud_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
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

Delete a CommvaultPlan.

```sql
DELETE FROM azure_isv.commvault_content_store.plans
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cloud_account_name = '{{ cloud_account_name }}' --required
AND plan_name = '{{ plan_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_orupdate"
    values={[
        { label: 'create_orupdate', value: 'create_orupdate' }
    ]}
>
<TabItem value="create_orupdate">

Create a CommvaultPlan.

```sql
EXEC azure_isv.commvault_content_store.plans.create_orupdate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cloud_account_name='{{ cloud_account_name }}' --required, 
@plan_name='{{ plan_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
