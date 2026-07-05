--- 
title: long_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_policies
  - sql
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="long_term_retention_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' }
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
    <td><CopyableCode code="monthlyRetention" /></td>
    <td><code>string</code></td>
    <td>The monthly retention policy for an LTR backup in an ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether to enable time-based immutability for future backups. When set, future backups will have TimeBasedImmutability enabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The setting for time-based immutability mode for future backup (Value can be either Locked or UnLocked. Only effective if TimeBasedImmutability is enabled). Caution: Immutability of LTR backup cannot be removed if TimeBasedImmutabilityMode is Locked. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="weekOfYear" /></td>
    <td><code>integer</code></td>
    <td>The week of year to take the yearly backup in an ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="weeklyRetention" /></td>
    <td><code>string</code></td>
    <td>The weekly retention policy for an LTR backup in an ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="yearlyRetention" /></td>
    <td><code>string</code></td>
    <td>The yearly retention policy for an LTR backup in an ISO 8601 format.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_database">

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
    <td><CopyableCode code="monthlyRetention" /></td>
    <td><code>string</code></td>
    <td>The monthly retention policy for an LTR backup in an ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutability" /></td>
    <td><code>string</code></td>
    <td>The setting for whether to enable time-based immutability for future backups. When set, future backups will have TimeBasedImmutability enabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="timeBasedImmutabilityMode" /></td>
    <td><code>string</code></td>
    <td>The setting for time-based immutability mode for future backup (Value can be either Locked or UnLocked. Only effective if TimeBasedImmutability is enabled). Caution: Immutability of LTR backup cannot be removed if TimeBasedImmutabilityMode is Locked. Known values are: "Locked" and "Unlocked". (Locked, Unlocked)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="weekOfYear" /></td>
    <td><code>integer</code></td>
    <td>The week of year to take the yearly backup in an ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="weeklyRetention" /></td>
    <td><code>string</code></td>
    <td>The weekly retention policy for an LTR backup in an ISO 8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="yearlyRetention" /></td>
    <td><code>string</code></td>
    <td>The yearly retention policy for an LTR backup in an ISO 8601 format.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a database's long term retention policy.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a database's long term retention policy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Set or update a database's long term retention policy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-server_name"><code>server_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Set or update a database's long term retention policy.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-policy_name">
    <td><CopyableCode code="policy_name" /></td>
    <td><code>string</code></td>
    <td>The policy name. Should always be Default. "default" Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-server_name">
    <td><CopyableCode code="server_name" /></td>
    <td><code>string</code></td>
    <td>The name of the server. Required.</td>
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
        { label: 'list_by_database', value: 'list_by_database' }
    ]}
>
<TabItem value="get">

Gets a database's long term retention policy.

```sql
SELECT
id,
name,
monthlyRetention,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type,
weekOfYear,
weeklyRetention,
yearlyRetention
FROM azure.sql.long_term_retention_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND policy_name = '{{ policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_database">

Gets a database's long term retention policy.

```sql
SELECT
id,
name,
monthlyRetention,
systemData,
timeBasedImmutability,
timeBasedImmutabilityMode,
type,
weekOfYear,
weeklyRetention,
yearlyRetention
FROM azure.sql.long_term_retention_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND server_name = '{{ server_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Set or update a database's long term retention policy.

```sql
INSERT INTO azure.sql.long_term_retention_policies (
properties,
resource_group_name,
server_name,
database_name,
policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ server_name }}',
'{{ database_name }}',
'{{ policy_name }}',
'{{ subscription_id }}'
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
- name: long_term_retention_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the long_term_retention_policies resource.
    - name: server_name
      value: "{{ server_name }}"
      description: Required parameter for the long_term_retention_policies resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the long_term_retention_policies resource.
    - name: policy_name
      value: "{{ policy_name }}"
      description: Required parameter for the long_term_retention_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the long_term_retention_policies resource.
    - name: properties
      description: |
        Resource properties.
      value:
        timeBasedImmutability: "{{ timeBasedImmutability }}"
        timeBasedImmutabilityMode: "{{ timeBasedImmutabilityMode }}"
        weeklyRetention: "{{ weeklyRetention }}"
        monthlyRetention: "{{ monthlyRetention }}"
        yearlyRetention: "{{ yearlyRetention }}"
        weekOfYear: {{ weekOfYear }}
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

Set or update a database's long term retention policy.

```sql
REPLACE azure.sql.long_term_retention_policies
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND server_name = '{{ server_name }}' --required
AND database_name = '{{ database_name }}' --required
AND policy_name = '{{ policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
