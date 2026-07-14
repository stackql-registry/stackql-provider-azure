--- 
title: device_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - device_pools
  - azure_stack_hci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>device_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="device_pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.device_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationName" /></td>
    <td><code>string</code></td>
    <td>Custom Location Name for the pool, default: -CL.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationResourceId" /></td>
    <td><code>string</code></td>
    <td>Custom Location Resource Id for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="devices" /></td>
    <td><code>array</code></td>
    <td>List of machines in device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Managed resource group name for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="operationDetails" /></td>
    <td><code>array</code></td>
    <td>operation status details for device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationName" /></td>
    <td><code>string</code></td>
    <td>Custom Location Name for the pool, default: -CL.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationResourceId" /></td>
    <td><code>string</code></td>
    <td>Custom Location Resource Id for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="devices" /></td>
    <td><code>array</code></td>
    <td>List of machines in device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Managed resource group name for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="operationDetails" /></td>
    <td><code>array</code></td>
    <td>operation status details for device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="cloudId" /></td>
    <td><code>string</code></td>
    <td>Unique, immutable resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationName" /></td>
    <td><code>string</code></td>
    <td>Custom Location Name for the pool, default: -CL.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationResourceId" /></td>
    <td><code>string</code></td>
    <td>Custom Location Resource Id for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="devices" /></td>
    <td><code>array</code></td>
    <td>List of machines in device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Managed resource group name for the pool.</td>
</tr>
<tr>
    <td><CopyableCode code="operationDetails" /></td>
    <td><code>array</code></td>
    <td>operation status details for device pool.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of a resource. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a DevicePool.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all device pools in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all device pools in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a DevicePool.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a devicePool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a DevicePool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a DevicePool.</td>
</tr>
<tr>
    <td><a href="#claim_devices"><CopyableCode code="claim_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-devices"><code>devices</code></a></td>
    <td></td>
    <td>Claiming devices of the pool.</td>
</tr>
<tr>
    <td><a href="#release_devices"><CopyableCode code="release_devices" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-device_pool_name"><code>device_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-devices"><code>devices</code></a></td>
    <td></td>
    <td>Releasing devices of the pool.</td>
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
<tr id="parameter-device_pool_name">
    <td><CopyableCode code="device_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the DevicePool. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a DevicePool.

```sql
SELECT
id,
name,
cloudId,
customLocationName,
customLocationResourceId,
devices,
identity,
location,
managedResourceGroup,
operationDetails,
provisioningState,
systemData,
tags,
type
FROM azure_stack.azure_stack_hci.device_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND device_pool_name = '{{ device_pool_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all device pools in a resource group.

```sql
SELECT
id,
name,
cloudId,
customLocationName,
customLocationResourceId,
devices,
identity,
location,
managedResourceGroup,
operationDetails,
provisioningState,
systemData,
tags,
type
FROM azure_stack.azure_stack_hci.device_pools
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List all device pools in a subscription.

```sql
SELECT
id,
name,
cloudId,
customLocationName,
customLocationResourceId,
devices,
identity,
location,
managedResourceGroup,
operationDetails,
provisioningState,
systemData,
tags,
type
FROM azure_stack.azure_stack_hci.device_pools
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create a DevicePool.

```sql
INSERT INTO azure_stack.azure_stack_hci.device_pools (
tags,
location,
properties,
identity,
resource_group_name,
device_pool_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ device_pool_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: device_pools
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the device_pools resource.
    - name: device_pool_name
      value: "{{ device_pool_name }}"
      description: Required parameter for the device_pools resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the device_pools resource.
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
        provisioningState: "{{ provisioningState }}"
        cloudId: "{{ cloudId }}"
        devices:
          - deviceResourceId: "{{ deviceResourceId }}"
            claimedBy: "{{ claimedBy }}"
        customLocationResourceId: "{{ customLocationResourceId }}"
        customLocationName: "{{ customLocationName }}"
        managedResourceGroup: "{{ managedResourceGroup }}"
        operationDetails:
          - name: "{{ name }}"
            id: "{{ id }}"
            type: "{{ type }}"
            resourceId: "{{ resourceId }}"
            description: "{{ description }}"
            status: "{{ status }}"
            error:
              code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details:
                - code: "{{ code }}"
                  message: "{{ message }}"
                  target: "{{ target }}"
                  details: "{{ details }}"
                  additionalInfo: "{{ additionalInfo }}"
              additionalInfo:
                - type: "{{ type }}"
                  info: "{{ info }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Update a devicePool.

```sql
UPDATE azure_stack.azure_stack_hci.device_pools
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND device_pool_name = '{{ device_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Create a DevicePool.

```sql
REPLACE azure_stack.azure_stack_hci.device_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND device_pool_name = '{{ device_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Delete a DevicePool.

```sql
DELETE FROM azure_stack.azure_stack_hci.device_pools
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND device_pool_name = '{{ device_pool_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="claim_devices"
    values={[
        { label: 'claim_devices', value: 'claim_devices' },
        { label: 'release_devices', value: 'release_devices' }
    ]}
>
<TabItem value="claim_devices">

Claiming devices of the pool.

```sql
EXEC azure_stack.azure_stack_hci.device_pools.claim_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_pool_name='{{ device_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"devices": "{{ devices }}", 
"claimedBy": "{{ claimedBy }}"
}'
;
```
</TabItem>
<TabItem value="release_devices">

Releasing devices of the pool.

```sql
EXEC azure_stack.azure_stack_hci.device_pools.release_devices 
@resource_group_name='{{ resource_group_name }}' --required, 
@device_pool_name='{{ device_pool_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"devices": "{{ devices }}"
}'
;
```
</TabItem>
</Tabs>
