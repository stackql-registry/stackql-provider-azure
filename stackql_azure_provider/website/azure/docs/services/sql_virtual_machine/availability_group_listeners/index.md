--- 
title: availability_group_listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_group_listeners
  - sql_virtual_machine
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

Creates, updates, deletes, gets or lists an <code>availability_group_listeners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="availability_group_listeners" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_virtual_machine.availability_group_listeners" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_group', value: 'list_by_group' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Availability Group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>Name of the availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="createDefaultAvailabilityGroupIfNotExist" /></td>
    <td><code>boolean</code></td>
    <td>Create a default availability group if it does not exist.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of load balancer configurations for an availability group listener.</td>
</tr>
<tr>
    <td><CopyableCode code="multiSubnetIpConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of multi subnet IP configurations for an AG listener.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Listener port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_group">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Availability Group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityGroupName" /></td>
    <td><code>string</code></td>
    <td>Name of the availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="createDefaultAvailabilityGroupIfNotExist" /></td>
    <td><code>boolean</code></td>
    <td>Create a default availability group if it does not exist.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of load balancer configurations for an availability group listener.</td>
</tr>
<tr>
    <td><CopyableCode code="multiSubnetIpConfigurations" /></td>
    <td><code>array</code></td>
    <td>List of multi subnet IP configurations for an AG listener.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>Listener port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-availability_group_listener_name"><code>availability_group_listener_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets an availability group listener.</td>
</tr>
<tr>
    <td><a href="#list_by_group"><CopyableCode code="list_by_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all availability group listeners in a SQL virtual machine group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-availability_group_listener_name"><code>availability_group_listener_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an availability group listener.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-availability_group_listener_name"><code>availability_group_listener_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an availability group listener.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-availability_group_listener_name"><code>availability_group_listener_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an availability group listener.</td>
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
<tr id="parameter-availability_group_listener_name">
    <td><CopyableCode code="availability_group_listener_name" /></td>
    <td><code>string</code></td>
    <td>Name of the availability group listener. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-sql_virtual_machine_group_name">
    <td><CopyableCode code="sql_virtual_machine_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SQL virtual machine group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The child resources to include in the response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_group', value: 'list_by_group' }
    ]}
>
<TabItem value="get">

Gets an availability group listener.

```sql
SELECT
id,
name,
availabilityGroupConfiguration,
availabilityGroupName,
createDefaultAvailabilityGroupIfNotExist,
loadBalancerConfigurations,
multiSubnetIpConfigurations,
port,
provisioningState,
systemData,
type
FROM azure.sql_virtual_machine.availability_group_listeners
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' -- required
AND availability_group_listener_name = '{{ availability_group_listener_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_group">

Lists all availability group listeners in a SQL virtual machine group.

```sql
SELECT
id,
name,
availabilityGroupConfiguration,
availabilityGroupName,
createDefaultAvailabilityGroupIfNotExist,
loadBalancerConfigurations,
multiSubnetIpConfigurations,
port,
provisioningState,
systemData,
type
FROM azure.sql_virtual_machine.availability_group_listeners
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' -- required
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

Creates or updates an availability group listener.

```sql
INSERT INTO azure.sql_virtual_machine.availability_group_listeners (
properties,
resource_group_name,
sql_virtual_machine_group_name,
availability_group_listener_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sql_virtual_machine_group_name }}',
'{{ availability_group_listener_name }}',
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
- name: availability_group_listeners
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the availability_group_listeners resource.
    - name: sql_virtual_machine_group_name
      value: "{{ sql_virtual_machine_group_name }}"
      description: Required parameter for the availability_group_listeners resource.
    - name: availability_group_listener_name
      value: "{{ availability_group_listener_name }}"
      description: Required parameter for the availability_group_listeners resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the availability_group_listeners resource.
    - name: properties
      value:
        availabilityGroupName: "{{ availabilityGroupName }}"
        loadBalancerConfigurations:
          - privateIpAddress:
              ipAddress: "{{ ipAddress }}"
              subnetResourceId: "{{ subnetResourceId }}"
            publicIpAddressResourceId: "{{ publicIpAddressResourceId }}"
            loadBalancerResourceId: "{{ loadBalancerResourceId }}"
            probePort: {{ probePort }}
            sqlVirtualMachineInstances: "{{ sqlVirtualMachineInstances }}"
        multiSubnetIpConfigurations:
          - privateIpAddress:
              ipAddress: "{{ ipAddress }}"
              subnetResourceId: "{{ subnetResourceId }}"
            sqlVirtualMachineInstance: "{{ sqlVirtualMachineInstance }}"
        createDefaultAvailabilityGroupIfNotExist: {{ createDefaultAvailabilityGroupIfNotExist }}
        port: {{ port }}
        availabilityGroupConfiguration:
          replicas:
            - sqlVirtualMachineInstanceId: "{{ sqlVirtualMachineInstanceId }}"
              role: "{{ role }}"
              commit: "{{ commit }}"
              failover: "{{ failover }}"
              readableSecondary: "{{ readableSecondary }}"
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

Creates or updates an availability group listener.

```sql
REPLACE azure.sql_virtual_machine.availability_group_listeners
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' --required
AND availability_group_listener_name = '{{ availability_group_listener_name }}' --required
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

Deletes an availability group listener.

```sql
DELETE FROM azure.sql_virtual_machine.availability_group_listeners
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' --required
AND availability_group_listener_name = '{{ availability_group_listener_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
