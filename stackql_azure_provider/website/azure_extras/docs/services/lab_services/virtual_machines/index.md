--- 
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - lab_services
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

Creates, updates, deletes, gets or lists a <code>virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.lab_services.virtual_machines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_lab', value: 'list_by_lab' }
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
    <td><CopyableCode code="claimedByUserId" /></td>
    <td><code>string</code></td>
    <td>The lab user ID (not the PUID!) of who claimed the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProfile" /></td>
    <td><code>object</code></td>
    <td>Profile for information about connecting to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the virtual machine. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the virtual machine. Known values are: "Stopped", "Starting", "Running", "Stopping", "ResettingPassword", "Reimaging", and "Redeploying".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System data of the Lab virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmType" /></td>
    <td><code>string</code></td>
    <td>The type of this VM resource. Known values are: "User" and "Template".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_lab">

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
    <td><CopyableCode code="claimedByUserId" /></td>
    <td><code>string</code></td>
    <td>The lab user ID (not the PUID!) of who claimed the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionProfile" /></td>
    <td><code>object</code></td>
    <td>Profile for information about connecting to the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current provisioning state of the virtual machine. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Locked".</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the virtual machine. Known values are: "Stopped", "Starting", "Running", "Stopping", "ResettingPassword", "Reimaging", and "Redeploying".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System data of the Lab virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmType" /></td>
    <td><code>string</code></td>
    <td>The type of this VM resource. Known values are: "User" and "Template".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a lab virtual machine. Returns the properties for a lab virtual machine.</td>
</tr>
<tr>
    <td><a href="#list_by_lab"><CopyableCode code="list_by_lab" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all virtual machines for a lab. Returns a list of all virtual machines for a lab.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a lab virtual machine. Action to start a lab virtual machine.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop a lab virtual machine. Action to stop a lab virtual machine.</td>
</tr>
<tr>
    <td><a href="#reimage"><CopyableCode code="reimage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Re-image a lab virtual machine. Re-image a lab virtual machine. The virtual machine will be deleted and recreated using the latest published snapshot of the reference environment of the lab.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity. Action to redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity.</td>
</tr>
<tr>
    <td><a href="#reset_password"><CopyableCode code="reset_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-virtual_machine_name"><code>virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-username"><code>username</code></a>, <a href="#parameter-password"><code>password</code></a></td>
    <td></td>
    <td>Reset a lab virtual machine password. Resets a lab virtual machine password.</td>
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
<tr id="parameter-lab_name">
    <td><CopyableCode code="lab_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs. Required.</td>
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
<tr id="parameter-virtual_machine_name">
    <td><CopyableCode code="virtual_machine_name" /></td>
    <td><code>string</code></td>
    <td>The ID of the virtual machine that uniquely identifies it within the containing lab. Used in resource URIs. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_lab', value: 'list_by_lab' }
    ]}
>
<TabItem value="get">

Get a lab virtual machine. Returns the properties for a lab virtual machine.

```sql
SELECT
id,
name,
claimedByUserId,
connectionProfile,
provisioningState,
state,
systemData,
type,
vmType
FROM azure_extras.lab_services.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND virtual_machine_name = '{{ virtual_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_lab">

Get all virtual machines for a lab. Returns a list of all virtual machines for a lab.

```sql
SELECT
id,
name,
claimedByUserId,
connectionProfile,
provisioningState,
state,
systemData,
type,
vmType
FROM azure_extras.lab_services.virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'reimage', value: 'reimage' },
        { label: 'redeploy', value: 'redeploy' },
        { label: 'reset_password', value: 'reset_password' }
    ]}
>
<TabItem value="start">

Start a lab virtual machine. Action to start a lab virtual machine.

```sql
EXEC azure_extras.lab_services.virtual_machines.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop a lab virtual machine. Action to stop a lab virtual machine.

```sql
EXEC azure_extras.lab_services.virtual_machines.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reimage">

Re-image a lab virtual machine. Re-image a lab virtual machine. The virtual machine will be deleted and recreated using the latest published snapshot of the reference environment of the lab.

```sql
EXEC azure_extras.lab_services.virtual_machines.reimage 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="redeploy">

Redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity. Action to redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity.

```sql
EXEC azure_extras.lab_services.virtual_machines.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_password">

Reset a lab virtual machine password. Resets a lab virtual machine password.

```sql
EXEC azure_extras.lab_services.virtual_machines.reset_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@lab_name='{{ lab_name }}' --required, 
@virtual_machine_name='{{ virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"username": "{{ username }}", 
"password": "{{ password }}"
}'
;
```
</TabItem>
</Tabs>
