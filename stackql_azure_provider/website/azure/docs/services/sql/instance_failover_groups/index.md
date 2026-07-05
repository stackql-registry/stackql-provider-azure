--- 
title: instance_failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_failover_groups
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

Creates, updates, deletes, gets or lists an <code>instance_failover_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="instance_failover_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.instance_failover_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_location', value: 'list_by_location' }
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
    <td><CopyableCode code="managedInstancePairs" /></td>
    <td><code>array</code></td>
    <td>List of managed instance pairs in the failover group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegions" /></td>
    <td><code>array</code></td>
    <td>Partner region information for the failover group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="readOnlyEndpoint" /></td>
    <td><code>object</code></td>
    <td>Read-only endpoint of the failover group instance.</td>
</tr>
<tr>
    <td><CopyableCode code="readWriteEndpoint" /></td>
    <td><code>object</code></td>
    <td>Read-write endpoint of the failover group instance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>Local replication role of the failover group instance. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state of the failover group instance.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryType" /></td>
    <td><code>string</code></td>
    <td>Type of the geo-secondary instance. Set 'Standby' if the instance is used as a DR option only. Known values are: "Geo" and "Standby". (Geo, Standby)</td>
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
<TabItem value="list_by_location">

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
    <td><CopyableCode code="managedInstancePairs" /></td>
    <td><code>array</code></td>
    <td>List of managed instance pairs in the failover group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerRegions" /></td>
    <td><code>array</code></td>
    <td>Partner region information for the failover group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="readOnlyEndpoint" /></td>
    <td><code>object</code></td>
    <td>Read-only endpoint of the failover group instance.</td>
</tr>
<tr>
    <td><CopyableCode code="readWriteEndpoint" /></td>
    <td><code>object</code></td>
    <td>Read-write endpoint of the failover group instance. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationRole" /></td>
    <td><code>string</code></td>
    <td>Local replication role of the failover group instance. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationState" /></td>
    <td><code>string</code></td>
    <td>Replication state of the failover group instance.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryType" /></td>
    <td><code>string</code></td>
    <td>Type of the geo-secondary instance. Set 'Standby' if the instance is used as a DR option only. Known values are: "Geo" and "Standby". (Geo, Standby)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-failover_group_name"><code>failover_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a failover group.</td>
</tr>
<tr>
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the failover groups in a location.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-failover_group_name"><code>failover_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a failover group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-failover_group_name"><code>failover_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a failover group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-failover_group_name"><code>failover_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a failover group.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-failover_group_name"><code>failover_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fails over from the current primary managed instance to this managed instance.</td>
</tr>
<tr>
    <td><a href="#force_failover_allow_data_loss"><CopyableCode code="force_failover_allow_data_loss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-failover_group_name"><code>failover_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fails over from the current primary managed instance to this managed instance. This operation might result in data loss.</td>
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
<tr id="parameter-failover_group_name">
    <td><CopyableCode code="failover_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the failover group. Required.</td>
</tr>
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The name of the region where the resource is located. Required.</td>
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
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="get">

Gets a failover group.

```sql
SELECT
id,
name,
managedInstancePairs,
partnerRegions,
readOnlyEndpoint,
readWriteEndpoint,
replicationRole,
replicationState,
secondaryType,
systemData,
type
FROM azure.sql.instance_failover_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
AND failover_group_name = '{{ failover_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_location">

Lists the failover groups in a location.

```sql
SELECT
id,
name,
managedInstancePairs,
partnerRegions,
readOnlyEndpoint,
readWriteEndpoint,
replicationRole,
replicationState,
secondaryType,
systemData,
type
FROM azure.sql.instance_failover_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location_name = '{{ location_name }}' -- required
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

Creates or updates a failover group.

```sql
INSERT INTO azure.sql.instance_failover_groups (
properties,
resource_group_name,
location_name,
failover_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ location_name }}',
'{{ failover_group_name }}',
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
- name: instance_failover_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the instance_failover_groups resource.
    - name: location_name
      value: "{{ location_name }}"
      description: Required parameter for the instance_failover_groups resource.
    - name: failover_group_name
      value: "{{ failover_group_name }}"
      description: Required parameter for the instance_failover_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the instance_failover_groups resource.
    - name: properties
      description: |
        Resource properties.
      value:
        secondaryType: "{{ secondaryType }}"
        readWriteEndpoint:
          failoverPolicy: "{{ failoverPolicy }}"
          failoverWithDataLossGracePeriodMinutes: {{ failoverWithDataLossGracePeriodMinutes }}
        readOnlyEndpoint:
          failoverPolicy: "{{ failoverPolicy }}"
        replicationRole: "{{ replicationRole }}"
        replicationState: "{{ replicationState }}"
        partnerRegions:
          - location: "{{ location }}"
            replicationRole: "{{ replicationRole }}"
        managedInstancePairs:
          - primaryManagedInstanceId: "{{ primaryManagedInstanceId }}"
            partnerManagedInstanceId: "{{ partnerManagedInstanceId }}"
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

Creates or updates a failover group.

```sql
REPLACE azure.sql.instance_failover_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND location_name = '{{ location_name }}' --required
AND failover_group_name = '{{ failover_group_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a failover group.

```sql
DELETE FROM azure.sql.instance_failover_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND location_name = '{{ location_name }}' --required
AND failover_group_name = '{{ failover_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="failover"
    values={[
        { label: 'failover', value: 'failover' },
        { label: 'force_failover_allow_data_loss', value: 'force_failover_allow_data_loss' }
    ]}
>
<TabItem value="failover">

Fails over from the current primary managed instance to this managed instance.

```sql
EXEC azure.sql.instance_failover_groups.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@failover_group_name='{{ failover_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="force_failover_allow_data_loss">

Fails over from the current primary managed instance to this managed instance. This operation might result in data loss.

```sql
EXEC azure.sql.instance_failover_groups.force_failover_allow_data_loss 
@resource_group_name='{{ resource_group_name }}' --required, 
@location_name='{{ location_name }}' --required, 
@failover_group_name='{{ failover_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
