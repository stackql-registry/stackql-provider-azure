--- 
title: distributed_availability_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - distributed_availability_groups
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

Creates, updates, deletes, gets or lists a <code>distributed_availability_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="distributed_availability_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.distributed_availability_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_instance', value: 'list_by_instance' }
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
    <td><CopyableCode code="databases" /></td>
    <td><code>array</code></td>
    <td>Databases in the distributed availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="distributedAvailabilityGroupId" /></td>
    <td><code>string</code></td>
    <td>ID of the distributed availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="distributedAvailabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>Name of the distributed availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverMode" /></td>
    <td><code>string</code></td>
    <td>The link failover mode - can be Manual if intended to be used for two-way failover with a supported SQL Server, or None for one-way failover to Azure. Known values are: "None" and "Manual". (None, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="instanceAvailabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>Managed instance side availability group name.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceLinkRole" /></td>
    <td><code>string</code></td>
    <td>Managed instance side link role. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerAvailabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>SQL server side availability group name.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerEndpoint" /></td>
    <td><code>string</code></td>
    <td>SQL server side endpoint - IP or DNS resolvable name.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLinkRole" /></td>
    <td><code>string</code></td>
    <td>SQL server side link role. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode of the link. Known values are: "Async" and "Sync". (Async, Sync)</td>
</tr>
<tr>
    <td><CopyableCode code="seedingMode" /></td>
    <td><code>string</code></td>
    <td>Database seeding mode – can be Automatic (default), or Manual for supported scenarios. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
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
<TabItem value="list_by_instance">

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
    <td><CopyableCode code="databases" /></td>
    <td><code>array</code></td>
    <td>Databases in the distributed availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="distributedAvailabilityGroupId" /></td>
    <td><code>string</code></td>
    <td>ID of the distributed availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="distributedAvailabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>Name of the distributed availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverMode" /></td>
    <td><code>string</code></td>
    <td>The link failover mode - can be Manual if intended to be used for two-way failover with a supported SQL Server, or None for one-way failover to Azure. Known values are: "None" and "Manual". (None, Manual)</td>
</tr>
<tr>
    <td><CopyableCode code="instanceAvailabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>Managed instance side availability group name.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceLinkRole" /></td>
    <td><code>string</code></td>
    <td>Managed instance side link role. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
</tr>
<tr>
    <td><CopyableCode code="partnerAvailabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>SQL server side availability group name.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerEndpoint" /></td>
    <td><code>string</code></td>
    <td>SQL server side endpoint - IP or DNS resolvable name.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerLinkRole" /></td>
    <td><code>string</code></td>
    <td>SQL server side link role. Known values are: "Primary" and "Secondary". (Primary, Secondary)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationMode" /></td>
    <td><code>string</code></td>
    <td>Replication mode of the link. Known values are: "Async" and "Sync". (Async, Sync)</td>
</tr>
<tr>
    <td><CopyableCode code="seedingMode" /></td>
    <td><code>string</code></td>
    <td>Database seeding mode – can be Automatic (default), or Manual for supported scenarios. Known values are: "Automatic" and "Manual". (Automatic, Manual)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a distributed availability group info.</td>
</tr>
<tr>
    <td><a href="#list_by_instance"><CopyableCode code="list_by_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of a distributed availability groups in instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a distributed availability group between Sql On-Prem and Sql Managed Instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a distributed availability group replication mode.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a distributed availability group between Sql On-Prem and Sql Managed Instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Drops a distributed availability group between Sql On-Prem and Sql Managed Instance.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-failoverType"><code>failoverType</code></a></td>
    <td></td>
    <td>Performs requested failover type in this distributed availability group.</td>
</tr>
<tr>
    <td><a href="#set_role"><CopyableCode code="set_role" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-distributed_availability_group_name"><code>distributed_availability_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-instanceRole"><code>instanceRole</code></a>, <a href="#parameter-roleChangeType"><code>roleChangeType</code></a></td>
    <td></td>
    <td>Sets the role for managed instance in a distributed availability group.</td>
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
<tr id="parameter-distributed_availability_group_name">
    <td><CopyableCode code="distributed_availability_group_name" /></td>
    <td><code>string</code></td>
    <td>The distributed availability group name. Required.</td>
</tr>
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
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
        { label: 'list_by_instance', value: 'list_by_instance' }
    ]}
>
<TabItem value="get">

Gets a distributed availability group info.

```sql
SELECT
id,
name,
databases,
distributedAvailabilityGroupId,
distributedAvailabilityGroupName,
failoverMode,
instanceAvailabilityGroupName,
instanceLinkRole,
partnerAvailabilityGroupName,
partnerEndpoint,
partnerLinkRole,
replicationMode,
seedingMode,
systemData,
type
FROM azure.sql.distributed_availability_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND distributed_availability_group_name = '{{ distributed_availability_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_instance">

Gets a list of a distributed availability groups in instance.

```sql
SELECT
id,
name,
databases,
distributedAvailabilityGroupId,
distributedAvailabilityGroupName,
failoverMode,
instanceAvailabilityGroupName,
instanceLinkRole,
partnerAvailabilityGroupName,
partnerEndpoint,
partnerLinkRole,
replicationMode,
seedingMode,
systemData,
type
FROM azure.sql.distributed_availability_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
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

Creates a distributed availability group between Sql On-Prem and Sql Managed Instance.

```sql
INSERT INTO azure.sql.distributed_availability_groups (
properties,
resource_group_name,
managed_instance_name,
distributed_availability_group_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ managed_instance_name }}',
'{{ distributed_availability_group_name }}',
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
- name: distributed_availability_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the distributed_availability_groups resource.
    - name: managed_instance_name
      value: "{{ managed_instance_name }}"
      description: Required parameter for the distributed_availability_groups resource.
    - name: distributed_availability_group_name
      value: "{{ distributed_availability_group_name }}"
      description: Required parameter for the distributed_availability_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the distributed_availability_groups resource.
    - name: properties
      description: |
        Resource properties.
      value:
        distributedAvailabilityGroupName: "{{ distributedAvailabilityGroupName }}"
        distributedAvailabilityGroupId: "{{ distributedAvailabilityGroupId }}"
        replicationMode: "{{ replicationMode }}"
        partnerLinkRole: "{{ partnerLinkRole }}"
        partnerAvailabilityGroupName: "{{ partnerAvailabilityGroupName }}"
        partnerEndpoint: "{{ partnerEndpoint }}"
        instanceLinkRole: "{{ instanceLinkRole }}"
        instanceAvailabilityGroupName: "{{ instanceAvailabilityGroupName }}"
        failoverMode: "{{ failoverMode }}"
        seedingMode: "{{ seedingMode }}"
        databases:
          - databaseName: "{{ databaseName }}"
            instanceReplicaId: "{{ instanceReplicaId }}"
            partnerReplicaId: "{{ partnerReplicaId }}"
            replicaState: "{{ replicaState }}"
            seedingProgress: "{{ seedingProgress }}"
            synchronizationHealth: "{{ synchronizationHealth }}"
            connectedState: "{{ connectedState }}"
            lastReceivedLsn: "{{ lastReceivedLsn }}"
            lastReceivedTime: "{{ lastReceivedTime }}"
            lastSentLsn: "{{ lastSentLsn }}"
            lastSentTime: "{{ lastSentTime }}"
            lastCommitLsn: "{{ lastCommitLsn }}"
            lastCommitTime: "{{ lastCommitTime }}"
            lastHardenedLsn: "{{ lastHardenedLsn }}"
            lastHardenedTime: "{{ lastHardenedTime }}"
            lastBackupLsn: "{{ lastBackupLsn }}"
            lastBackupTime: "{{ lastBackupTime }}"
            mostRecentLinkError: "{{ mostRecentLinkError }}"
            partnerAuthCertValidity:
              certificateName: "{{ certificateName }}"
              expiryDate: "{{ expiryDate }}"
            instanceSendReplicationLagSeconds: {{ instanceSendReplicationLagSeconds }}
            instanceRedoReplicationLagSeconds: {{ instanceRedoReplicationLagSeconds }}
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

Updates a distributed availability group replication mode.

```sql
UPDATE azure.sql.distributed_availability_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND distributed_availability_group_name = '{{ distributed_availability_group_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates a distributed availability group between Sql On-Prem and Sql Managed Instance.

```sql
REPLACE azure.sql.distributed_availability_groups
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND distributed_availability_group_name = '{{ distributed_availability_group_name }}' --required
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

Drops a distributed availability group between Sql On-Prem and Sql Managed Instance.

```sql
DELETE FROM azure.sql.distributed_availability_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND distributed_availability_group_name = '{{ distributed_availability_group_name }}' --required
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
        { label: 'set_role', value: 'set_role' }
    ]}
>
<TabItem value="failover">

Performs requested failover type in this distributed availability group.

```sql
EXEC azure.sql.distributed_availability_groups.failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@distributed_availability_group_name='{{ distributed_availability_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"failoverType": "{{ failoverType }}"
}'
;
```
</TabItem>
<TabItem value="set_role">

Sets the role for managed instance in a distributed availability group.

```sql
EXEC azure.sql.distributed_availability_groups.set_role 
@resource_group_name='{{ resource_group_name }}' --required, 
@managed_instance_name='{{ managed_instance_name }}' --required, 
@distributed_availability_group_name='{{ distributed_availability_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"instanceRole": "{{ instanceRole }}", 
"roleChangeType": "{{ roleChangeType }}"
}'
;
```
</TabItem>
</Tabs>
