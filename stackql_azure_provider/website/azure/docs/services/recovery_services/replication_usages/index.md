--- 
title: replication_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_usages
  - recovery_services
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

Creates, updates, deletes, gets or lists a <code>replication_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_usages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.replication_usages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="jobsSummary" /></td>
    <td><code>object</code></td>
    <td>Summary of the replication jobs data for this vault.</td>
</tr>
<tr>
    <td><CopyableCode code="monitoringSummary" /></td>
    <td><code>object</code></td>
    <td>Summary of the replication monitoring data for this vault.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemCount" /></td>
    <td><code>integer</code></td>
    <td>Number of replication protected items for this vault.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryPlanCount" /></td>
    <td><code>integer</code></td>
    <td>Number of replication recovery plans for this vault.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryServicesProviderAuthType" /></td>
    <td><code>integer</code></td>
    <td>The authentication type of recovery service providers in the vault.</td>
</tr>
<tr>
    <td><CopyableCode code="registeredServersCount" /></td>
    <td><code>integer</code></td>
    <td>Number of servers registered to this vault.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetches the replication usages of the vault.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Fetches the replication usages of the vault.

```sql
SELECT
jobsSummary,
monitoringSummary,
protectedItemCount,
recoveryPlanCount,
recoveryServicesProviderAuthType,
registeredServersCount
FROM azure.recovery_services.replication_usages
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
