--- 
title: elastic_snapshot_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_snapshot_policies
  - netapp
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

Creates, updates, deletes, gets or lists an <code>elastic_snapshot_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="elastic_snapshot_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.elastic_snapshot_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_elastic_account', value: 'list_by_elastic_account' }
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
    <td><CopyableCode code="dailySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for daily snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="hourlySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for hourly snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for monthly snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="policyStatus" /></td>
    <td><code>string</code></td>
    <td>Configures if the snapshot policy is enabled on the volumes connected to the policy. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
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
<tr>
    <td><CopyableCode code="weeklySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for weekly snapshots.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_elastic_account">

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
    <td><CopyableCode code="dailySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for daily snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="hourlySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for hourly snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for monthly snapshots.</td>
</tr>
<tr>
    <td><CopyableCode code="policyStatus" /></td>
    <td><code>string</code></td>
    <td>Configures if the snapshot policy is enabled on the volumes connected to the policy. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure lifecycle management. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
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
<tr>
    <td><CopyableCode code="weeklySchedule" /></td>
    <td><code>object</code></td>
    <td>Schedule for weekly snapshots.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-snapshot_policy_name"><code>snapshot_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a ElasticSnapshotPolicy.</td>
</tr>
<tr>
    <td><a href="#list_by_elastic_account"><CopyableCode code="list_by_elastic_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List ElasticSnapshotPolicy resources by ElasticAccount.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-snapshot_policy_name"><code>snapshot_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ElasticSnapshotPolicy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-snapshot_policy_name"><code>snapshot_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a ElasticSnapshotPolicy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-snapshot_policy_name"><code>snapshot_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a ElasticSnapshotPolicy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-snapshot_policy_name"><code>snapshot_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a ElasticSnapshotPolicy.</td>
</tr>
<tr>
    <td><a href="#list_elastic_volumes"><CopyableCode code="list_elastic_volumes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-snapshot_policy_name"><code>snapshot_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get elastic volumes associated with Elastic Snapshot Policy.</td>
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
    <td>The name of the ElasticAccount. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-snapshot_policy_name">
    <td><CopyableCode code="snapshot_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ElasticSnapshotPolicy. Required.</td>
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
        { label: 'list_by_elastic_account', value: 'list_by_elastic_account' }
    ]}
>
<TabItem value="get">

Get a ElasticSnapshotPolicy.

```sql
SELECT
id,
name,
dailySchedule,
eTag,
hourlySchedule,
location,
monthlySchedule,
policyStatus,
provisioningState,
systemData,
tags,
type,
weeklySchedule
FROM azure_isv.netapp.elastic_snapshot_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND snapshot_policy_name = '{{ snapshot_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_elastic_account">

List ElasticSnapshotPolicy resources by ElasticAccount.

```sql
SELECT
id,
name,
dailySchedule,
eTag,
hourlySchedule,
location,
monthlySchedule,
policyStatus,
provisioningState,
systemData,
tags,
type,
weeklySchedule
FROM azure_isv.netapp.elastic_snapshot_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
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

Create a ElasticSnapshotPolicy.

```sql
INSERT INTO azure_isv.netapp.elastic_snapshot_policies (
tags,
location,
properties,
resource_group_name,
account_name,
snapshot_policy_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ snapshot_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
eTag,
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
- name: elastic_snapshot_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the elastic_snapshot_policies resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the elastic_snapshot_policies resource.
    - name: snapshot_policy_name
      value: "{{ snapshot_policy_name }}"
      description: Required parameter for the elastic_snapshot_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the elastic_snapshot_policies resource.
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
        The resource-specific properties for this resource.
      value:
        hourlySchedule:
          snapshotsToKeep: {{ snapshotsToKeep }}
          minute: {{ minute }}
        dailySchedule:
          snapshotsToKeep: {{ snapshotsToKeep }}
          hour: {{ hour }}
          minute: {{ minute }}
        weeklySchedule:
          snapshotsToKeep: {{ snapshotsToKeep }}
          days:
            - "{{ days }}"
          hour: {{ hour }}
          minute: {{ minute }}
        monthlySchedule:
          snapshotsToKeep: {{ snapshotsToKeep }}
          daysOfMonth:
            - {{ daysOfMonth }}
          hour: {{ hour }}
          minute: {{ minute }}
        policyStatus: "{{ policyStatus }}"
        provisioningState: "{{ provisioningState }}"
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

Update a ElasticSnapshotPolicy.

```sql
UPDATE azure_isv.netapp.elastic_snapshot_policies
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND snapshot_policy_name = '{{ snapshot_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
eTag,
location,
properties,
systemData,
tags,
type;
```
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

Create a ElasticSnapshotPolicy.

```sql
REPLACE azure_isv.netapp.elastic_snapshot_policies
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND snapshot_policy_name = '{{ snapshot_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
eTag,
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

Delete a ElasticSnapshotPolicy.

```sql
DELETE FROM azure_isv.netapp.elastic_snapshot_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND snapshot_policy_name = '{{ snapshot_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_elastic_volumes"
    values={[
        { label: 'list_elastic_volumes', value: 'list_elastic_volumes' }
    ]}
>
<TabItem value="list_elastic_volumes">

Get elastic volumes associated with Elastic Snapshot Policy.

```sql
EXEC azure_isv.netapp.elastic_snapshot_policies.list_elastic_volumes 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@snapshot_policy_name='{{ snapshot_policy_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
