--- 
title: iscsi_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_targets
  - storage_pool
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>iscsi_targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iscsi_targets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storage_pool.iscsi_targets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_disk_pool', value: 'list_by_disk_pool' }
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aclMode" /></td>
    <td><code>string</code></td>
    <td>Mode for Target connectivity. Required. Known values are: "Dynamic" and "Static".</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>List of private IPv4 addresses to connect to the iSCSI Target.</td>
</tr>
<tr>
    <td><CopyableCode code="luns" /></td>
    <td><code>array</code></td>
    <td>List of LUNs to be exposed through iSCSI Target.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Azure resource id. Indicates if this resource is managed by another Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByExtended" /></td>
    <td><code>array</code></td>
    <td>List of Azure resource ids that manage this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port used by iSCSI Target portal group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Required. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="sessions" /></td>
    <td><code>array</code></td>
    <td>List of identifiers for active sessions on the iSCSI target.</td>
</tr>
<tr>
    <td><CopyableCode code="staticAcls" /></td>
    <td><code>array</code></td>
    <td>Access Control List (ACL) for an iSCSI Target; defines LUN masking policy.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operational status of the iSCSI Target. Required. Known values are: "Invalid", "Unknown", "Healthy", "Unhealthy", "Updating", "Running", "Stopped", and "Stopped (deallocated)".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Resource metadata required by ARM RPC.</td>
</tr>
<tr>
    <td><CopyableCode code="targetIqn" /></td>
    <td><code>string</code></td>
    <td>iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_disk_pool">

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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aclMode" /></td>
    <td><code>string</code></td>
    <td>Mode for Target connectivity. Required. Known values are: "Dynamic" and "Static".</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>List of private IPv4 addresses to connect to the iSCSI Target.</td>
</tr>
<tr>
    <td><CopyableCode code="luns" /></td>
    <td><code>array</code></td>
    <td>List of LUNs to be exposed through iSCSI Target.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>Azure resource id. Indicates if this resource is managed by another Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="managedByExtended" /></td>
    <td><code>array</code></td>
    <td>List of Azure resource ids that manage this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port used by iSCSI Target portal group.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the operation on the resource. Required. Known values are: "Invalid", "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Updating", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="sessions" /></td>
    <td><code>array</code></td>
    <td>List of identifiers for active sessions on the iSCSI target.</td>
</tr>
<tr>
    <td><CopyableCode code="staticAcls" /></td>
    <td><code>array</code></td>
    <td>Access Control List (ACL) for an iSCSI Target; defines LUN masking policy.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operational status of the iSCSI Target. Required. Known values are: "Invalid", "Unknown", "Healthy", "Unhealthy", "Updating", "Running", "Stopped", and "Stopped (deallocated)".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Resource metadata required by ARM RPC.</td>
</tr>
<tr>
    <td><CopyableCode code="targetIqn" /></td>
    <td><code>string</code></td>
    <td>iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_pool_name"><code>disk_pool_name</code></a>, <a href="#parameter-iscsi_target_name"><code>iscsi_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an iSCSI Target.</td>
</tr>
<tr>
    <td><a href="#list_by_disk_pool"><CopyableCode code="list_by_disk_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_pool_name"><code>disk_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get iSCSI Targets in a Disk pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_pool_name"><code>disk_pool_name</code></a>, <a href="#parameter-iscsi_target_name"><code>iscsi_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or Update an iSCSI Target.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_pool_name"><code>disk_pool_name</code></a>, <a href="#parameter-iscsi_target_name"><code>iscsi_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an iSCSI Target.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_pool_name"><code>disk_pool_name</code></a>, <a href="#parameter-iscsi_target_name"><code>iscsi_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or Update an iSCSI Target.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-disk_pool_name"><code>disk_pool_name</code></a>, <a href="#parameter-iscsi_target_name"><code>iscsi_target_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an iSCSI Target.</td>
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
<tr id="parameter-disk_pool_name">
    <td><CopyableCode code="disk_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Disk Pool. Required.</td>
</tr>
<tr id="parameter-iscsi_target_name">
    <td><CopyableCode code="iscsi_target_name" /></td>
    <td><code>string</code></td>
    <td>The name of the iSCSI Target. Required.</td>
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
        { label: 'list_by_disk_pool', value: 'list_by_disk_pool' }
    ]}
>
<TabItem value="get">

Get an iSCSI Target.

```sql
SELECT
id,
name,
aclMode,
endpoints,
luns,
managedBy,
managedByExtended,
port,
provisioningState,
sessions,
staticAcls,
status,
systemData,
targetIqn,
type
FROM azure_extras.storage_pool.iscsi_targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND disk_pool_name = '{{ disk_pool_name }}' -- required
AND iscsi_target_name = '{{ iscsi_target_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_disk_pool">

Get iSCSI Targets in a Disk pool.

```sql
SELECT
id,
name,
aclMode,
endpoints,
luns,
managedBy,
managedByExtended,
port,
provisioningState,
sessions,
staticAcls,
status,
systemData,
targetIqn,
type
FROM azure_extras.storage_pool.iscsi_targets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND disk_pool_name = '{{ disk_pool_name }}' -- required
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

Create or Update an iSCSI Target.

```sql
INSERT INTO azure_extras.storage_pool.iscsi_targets (
managedBy,
managedByExtended,
properties,
resource_group_name,
disk_pool_name,
iscsi_target_name,
subscription_id
)
SELECT 
'{{ managedBy }}',
'{{ managedByExtended }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ disk_pool_name }}',
'{{ iscsi_target_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
managedBy,
managedByExtended,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: iscsi_targets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the iscsi_targets resource.
    - name: disk_pool_name
      value: "{{ disk_pool_name }}"
      description: Required parameter for the iscsi_targets resource.
    - name: iscsi_target_name
      value: "{{ iscsi_target_name }}"
      description: Required parameter for the iscsi_targets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the iscsi_targets resource.
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        Azure resource id. Indicates if this resource is managed by another Azure resource.
    - name: managedByExtended
      value:
        - "{{ managedByExtended }}"
      description: |
        List of Azure resource ids that manage this resource.
    - name: properties
      value:
        aclMode: "{{ aclMode }}"
        targetIqn: "{{ targetIqn }}"
        staticAcls:
          - initiatorIqn: "{{ initiatorIqn }}"
            mappedLuns: "{{ mappedLuns }}"
        luns:
          - name: "{{ name }}"
            managedDiskAzureResourceId: "{{ managedDiskAzureResourceId }}"
            lun: {{ lun }}
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

Update an iSCSI Target.

```sql
UPDATE azure_extras.storage_pool.iscsi_targets
SET 
managedBy = '{{ managedBy }}',
managedByExtended = '{{ managedByExtended }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND disk_pool_name = '{{ disk_pool_name }}' --required
AND iscsi_target_name = '{{ iscsi_target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
managedBy,
managedByExtended,
properties,
systemData,
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

Create or Update an iSCSI Target.

```sql
REPLACE azure_extras.storage_pool.iscsi_targets
SET 
managedBy = '{{ managedBy }}',
managedByExtended = '{{ managedByExtended }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND disk_pool_name = '{{ disk_pool_name }}' --required
AND iscsi_target_name = '{{ iscsi_target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
managedBy,
managedByExtended,
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

Delete an iSCSI Target.

```sql
DELETE FROM azure_extras.storage_pool.iscsi_targets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND disk_pool_name = '{{ disk_pool_name }}' --required
AND iscsi_target_name = '{{ iscsi_target_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
