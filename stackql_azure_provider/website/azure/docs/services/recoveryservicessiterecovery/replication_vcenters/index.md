--- 
title: replication_vcenters
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_vcenters
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_vcenters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_vcenters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_vcenters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_fabrics', value: 'list_by_replication_fabrics' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="discoveryStatus" /></td>
    <td><code>string</code></td>
    <td>The VCenter discovery status.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricArmResourceName" /></td>
    <td><code>string</code></td>
    <td>The ARM resource name of the fabric containing this VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>The health errors for this VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureId" /></td>
    <td><code>string</code></td>
    <td>The infrastructure Id of vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="internalId" /></td>
    <td><code>string</code></td>
    <td>VCenter internal ID.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address of the vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartbeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the last heartbeat was received by vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>string</code></td>
    <td>The port number for discovery.</td>
</tr>
<tr>
    <td><CopyableCode code="processServerId" /></td>
    <td><code>string</code></td>
    <td>The process server Id.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsAccountId" /></td>
    <td><code>string</code></td>
    <td>The account Id which has privileges to discover the vCenter.</td>
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
<TabItem value="list_by_replication_fabrics">

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
    <td><CopyableCode code="discoveryStatus" /></td>
    <td><code>string</code></td>
    <td>The VCenter discovery status.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricArmResourceName" /></td>
    <td><code>string</code></td>
    <td>The ARM resource name of the fabric containing this VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>The health errors for this VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureId" /></td>
    <td><code>string</code></td>
    <td>The infrastructure Id of vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="internalId" /></td>
    <td><code>string</code></td>
    <td>VCenter internal ID.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address of the vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartbeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the last heartbeat was received by vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>string</code></td>
    <td>The port number for discovery.</td>
</tr>
<tr>
    <td><CopyableCode code="processServerId" /></td>
    <td><code>string</code></td>
    <td>The process server Id.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsAccountId" /></td>
    <td><code>string</code></td>
    <td>The account Id which has privileges to discover the vCenter.</td>
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
    <td><CopyableCode code="discoveryStatus" /></td>
    <td><code>string</code></td>
    <td>The VCenter discovery status.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricArmResourceName" /></td>
    <td><code>string</code></td>
    <td>The ARM resource name of the fabric containing this VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>The health errors for this VCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureId" /></td>
    <td><code>string</code></td>
    <td>The infrastructure Id of vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="internalId" /></td>
    <td><code>string</code></td>
    <td>VCenter internal ID.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address of the vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartbeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the last heartbeat was received by vCenter.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>string</code></td>
    <td>The port number for discovery.</td>
</tr>
<tr>
    <td><CopyableCode code="processServerId" /></td>
    <td><code>string</code></td>
    <td>The process server Id.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsAccountId" /></td>
    <td><code>string</code></td>
    <td>The account Id which has privileges to discover the vCenter.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a vCenter. Gets the details of a registered vCenter server(Add vCenter server).</td>
</tr>
<tr>
    <td><a href="#list_by_replication_fabrics"><CopyableCode code="list_by_replication_fabrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of vCenter registered under a fabric. Lists the vCenter servers registered in a fabric.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of vCenter registered under the vault. Lists the vCenter servers registered in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add vCenter. The operation to create a vCenter object..</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update vCenter operation. The operation to update a registered vCenter.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-vcenter_name"><code>vcenter_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove vcenter operation. The operation to remove(unregister) a registered vCenter server from the vault.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vcenter_name">
    <td><CopyableCode code="vcenter_name" /></td>
    <td><code>string</code></td>
    <td>vcenter name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_fabrics', value: 'list_by_replication_fabrics' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details of a vCenter. Gets the details of a registered vCenter server(Add vCenter server).

```sql
SELECT
id,
name,
discoveryStatus,
fabricArmResourceName,
friendlyName,
healthErrors,
infrastructureId,
internalId,
ipAddress,
lastHeartbeat,
location,
port,
processServerId,
runAsAccountId,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_vcenters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND vcenter_name = '{{ vcenter_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_fabrics">

Gets the list of vCenter registered under a fabric. Lists the vCenter servers registered in a fabric.

```sql
SELECT
id,
name,
discoveryStatus,
fabricArmResourceName,
friendlyName,
healthErrors,
infrastructureId,
internalId,
ipAddress,
lastHeartbeat,
location,
port,
processServerId,
runAsAccountId,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_vcenters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of vCenter registered under the vault. Lists the vCenter servers registered in the vault.

```sql
SELECT
id,
name,
discoveryStatus,
fabricArmResourceName,
friendlyName,
healthErrors,
infrastructureId,
internalId,
ipAddress,
lastHeartbeat,
location,
port,
processServerId,
runAsAccountId,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_vcenters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Add vCenter. The operation to create a vCenter object..

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_vcenters (
properties,
resource_group_name,
resource_name,
fabric_name,
vcenter_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ vcenter_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_vcenters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_vcenters resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_vcenters resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_vcenters resource.
    - name: vcenter_name
      value: "{{ vcenter_name }}"
      description: Required parameter for the replication_vcenters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_vcenters resource.
    - name: properties
      description: |
        The properties of an add vCenter request.
      value:
        friendlyName: "{{ friendlyName }}"
        ipAddress: "{{ ipAddress }}"
        processServerId: "{{ processServerId }}"
        port: "{{ port }}"
        runAsAccountId: "{{ runAsAccountId }}"
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

Update vCenter operation. The operation to update a registered vCenter.

```sql
UPDATE azure.recoveryservicessiterecovery.replication_vcenters
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND vcenter_name = '{{ vcenter_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Remove vcenter operation. The operation to remove(unregister) a registered vCenter server from the vault.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_vcenters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND vcenter_name = '{{ vcenter_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
