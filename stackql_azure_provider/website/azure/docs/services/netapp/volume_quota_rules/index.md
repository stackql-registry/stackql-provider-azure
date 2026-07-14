--- 
title: volume_quota_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_quota_rules
  - netapp
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

Creates, updates, deletes, gets or lists a <code>volume_quota_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="volume_quota_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.volume_quota_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_volume', value: 'list_by_volume' }
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
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the VolumeQuotaRule at the time the operation was called. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaSizeInKiBs" /></td>
    <td><code>integer</code></td>
    <td>Size of quota.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaTarget" /></td>
    <td><code>string</code></td>
    <td>UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running .</td>
</tr>
<tr>
    <td><CopyableCode code="quotaType" /></td>
    <td><code>string</code></td>
    <td>Type of quota. Known values are: "DefaultUserQuota", "DefaultGroupQuota", "IndividualUserQuota", and "IndividualGroupQuota". (DefaultUserQuota, DefaultGroupQuota, IndividualUserQuota, IndividualGroupQuota)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_volume">

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
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the VolumeQuotaRule at the time the operation was called. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaSizeInKiBs" /></td>
    <td><code>integer</code></td>
    <td>Size of quota.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaTarget" /></td>
    <td><code>string</code></td>
    <td>UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running .</td>
</tr>
<tr>
    <td><CopyableCode code="quotaType" /></td>
    <td><code>string</code></td>
    <td>Type of quota. Known values are: "DefaultUserQuota", "DefaultGroupQuota", "IndividualUserQuota", and "IndividualGroupQuota". (DefaultUserQuota, DefaultGroupQuota, IndividualUserQuota, IndividualGroupQuota)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-volume_quota_rule_name"><code>volume_quota_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of the specified quota rule.</td>
</tr>
<tr>
    <td><a href="#list_by_volume"><CopyableCode code="list_by_volume" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all quota rules associated with the volume.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-volume_quota_rule_name"><code>volume_quota_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create the specified quota rule within the given volume.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-volume_quota_rule_name"><code>volume_quota_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch a quota rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-volume_quota_rule_name"><code>volume_quota_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete quota rule.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NetApp account. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity pool. Required.</td>
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
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volume. Required.</td>
</tr>
<tr id="parameter-volume_quota_rule_name">
    <td><CopyableCode code="volume_quota_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of volume quota rule. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_volume', value: 'list_by_volume' }
    ]}
>
<TabItem value="get">

Get details of the specified quota rule.

```sql
SELECT
id,
name,
location,
provisioningState,
quotaSizeInKiBs,
quotaTarget,
quotaType,
systemData,
tags,
type
FROM azure.netapp.volume_quota_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND volume_quota_rule_name = '{{ volume_quota_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_volume">

List all quota rules associated with the volume.

```sql
SELECT
id,
name,
location,
provisioningState,
quotaSizeInKiBs,
quotaTarget,
quotaType,
systemData,
tags,
type
FROM azure.netapp.volume_quota_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create the specified quota rule within the given volume.

```sql
INSERT INTO azure.netapp.volume_quota_rules (
tags,
location,
properties,
resource_group_name,
account_name,
pool_name,
volume_name,
volume_quota_rule_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ pool_name }}',
'{{ volume_name }}',
'{{ volume_quota_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: volume_quota_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the volume_quota_rules resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the volume_quota_rules resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the volume_quota_rules resource.
    - name: volume_name
      value: "{{ volume_name }}"
      description: Required parameter for the volume_quota_rules resource.
    - name: volume_quota_rule_name
      value: "{{ volume_quota_rule_name }}"
      description: Required parameter for the volume_quota_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the volume_quota_rules resource.
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
        Volume Quota Rule Properties.
      value:
        provisioningState: "{{ provisioningState }}"
        quotaSizeInKiBs: {{ quotaSizeInKiBs }}
        quotaType: "{{ quotaType }}"
        quotaTarget: "{{ quotaTarget }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Patch a quota rule.

```sql
UPDATE azure.netapp.volume_quota_rules
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND volume_quota_rule_name = '{{ volume_quota_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Delete quota rule.

```sql
DELETE FROM azure.netapp.volume_quota_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND volume_quota_rule_name = '{{ volume_quota_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
