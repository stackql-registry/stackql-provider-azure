--- 
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
  - compute
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

Creates, updates, deletes, gets or lists an <code>availability_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="availability_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.availability_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count.</td>
</tr>
<tr>
    <td><CopyableCode code="platformUpdateDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Update Domain count.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the availability set.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the availability set, only name is required to be set. See AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for virtual machines with managed disks and 'Classic' for virtual machines with unmanaged disks. Default value is 'Classic'.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
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
    <td><CopyableCode code="virtualMachineScaleSetMigrationInfo" /></td>
    <td><code>object</code></td>
    <td>Describes the migration properties on the Availability Set.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the availability set.</td>
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count.</td>
</tr>
<tr>
    <td><CopyableCode code="platformUpdateDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Update Domain count.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the availability set.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the availability set, only name is required to be set. See AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for virtual machines with managed disks and 'Classic' for virtual machines with unmanaged disks. Default value is 'Classic'.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
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
    <td><CopyableCode code="virtualMachineScaleSetMigrationInfo" /></td>
    <td><code>object</code></td>
    <td>Describes the migration properties on the Availability Set.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the availability set.</td>
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
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="platformFaultDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Fault Domain count.</td>
</tr>
<tr>
    <td><CopyableCode code="platformUpdateDomainCount" /></td>
    <td><code>integer</code></td>
    <td>Update Domain count.</td>
</tr>
<tr>
    <td><CopyableCode code="proximityPlacementGroup" /></td>
    <td><code>object</code></td>
    <td>SubResource.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledEventsPolicy" /></td>
    <td><code>object</code></td>
    <td>Specifies Redeploy, Reboot and ScheduledEventsAdditionalPublishingTargets Scheduled Event related configurations for the availability set.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the availability set, only name is required to be set. See AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for virtual machines with managed disks and 'Classic' for virtual machines with unmanaged disks. Default value is 'Classic'.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
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
    <td><CopyableCode code="virtualMachineScaleSetMigrationInfo" /></td>
    <td><code>object</code></td>
    <td>Describes the migration properties on the Availability Set.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachines" /></td>
    <td><code>array</code></td>
    <td>A list of references to all virtual machines in the availability set.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves information about an availability set.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all availability sets in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all availability sets in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an availability set.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an availability set.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update an availability set.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an availability set.</td>
</tr>
<tr>
    <td><a href="#list_available_sizes"><CopyableCode code="list_available_sizes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set.</td>
</tr>
<tr>
    <td><a href="#start_migration_to_virtual_machine_scale_set"><CopyableCode code="start_migration_to_virtual_machine_scale_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-virtualMachineScaleSetFlexible"><code>virtualMachineScaleSetFlexible</code></a></td>
    <td></td>
    <td>Start migration operation on an Availability Set to move its Virtual Machines to a Virtual Machine Scale Set. This should be followed by a migrate operation on each Virtual Machine that triggers a downtime on the Virtual Machine.</td>
</tr>
<tr>
    <td><a href="#cancel_migration_to_virtual_machine_scale_set"><CopyableCode code="cancel_migration_to_virtual_machine_scale_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancel the migration operation on an Availability Set.</td>
</tr>
<tr>
    <td><a href="#validate_migration_to_virtual_machine_scale_set"><CopyableCode code="validate_migration_to_virtual_machine_scale_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-virtualMachineScaleSetFlexible"><code>virtualMachineScaleSetFlexible</code></a></td>
    <td></td>
    <td>Validates that the Virtual Machines in the Availability Set can be migrated to the provided Virtual Machine Scale Set.</td>
</tr>
<tr>
    <td><a href="#convert_to_virtual_machine_scale_set"><CopyableCode code="convert_to_virtual_machine_scale_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-availability_set_name"><code>availability_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Flexible Virtual Machine Scale Set and migrate all the Virtual Machines in the Availability Set. This does not trigger a downtime on the Virtual Machines.</td>
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
<tr id="parameter-availability_set_name">
    <td><CopyableCode code="availability_set_name" /></td>
    <td><code>string</code></td>
    <td>The name of the availability set. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply to the operation. Allowed values are 'instanceView'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieves information about an availability set.

```sql
SELECT
id,
name,
location,
platformFaultDomainCount,
platformUpdateDomainCount,
proximityPlacementGroup,
scheduledEventsPolicy,
sku,
statuses,
systemData,
tags,
type,
virtualMachineScaleSetMigrationInfo,
virtualMachines
FROM azure.compute.availability_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND availability_set_name = '{{ availability_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all availability sets in a resource group.

```sql
SELECT
id,
name,
location,
platformFaultDomainCount,
platformUpdateDomainCount,
proximityPlacementGroup,
scheduledEventsPolicy,
sku,
statuses,
systemData,
tags,
type,
virtualMachineScaleSetMigrationInfo,
virtualMachines
FROM azure.compute.availability_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all availability sets in a subscription.

```sql
SELECT
id,
name,
location,
platformFaultDomainCount,
platformUpdateDomainCount,
proximityPlacementGroup,
scheduledEventsPolicy,
sku,
statuses,
systemData,
tags,
type,
virtualMachineScaleSetMigrationInfo,
virtualMachines
FROM azure.compute.availability_sets
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

Create or update an availability set.

```sql
INSERT INTO azure.compute.availability_sets (
tags,
location,
properties,
sku,
resource_group_name,
availability_set_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ availability_set_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: availability_sets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the availability_sets resource.
    - name: availability_set_name
      value: "{{ availability_set_name }}"
      description: Required parameter for the availability_sets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the availability_sets resource.
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
        The instance view of a resource.
      value:
        platformUpdateDomainCount: {{ platformUpdateDomainCount }}
        platformFaultDomainCount: {{ platformFaultDomainCount }}
        virtualMachines:
          - id: "{{ id }}"
        proximityPlacementGroup:
          id: "{{ id }}"
        statuses:
          - code: "{{ code }}"
            level: "{{ level }}"
            displayStatus: "{{ displayStatus }}"
            message: "{{ message }}"
            time: "{{ time }}"
        scheduledEventsPolicy:
          userInitiatedRedeploy:
            automaticallyApprove: {{ automaticallyApprove }}
          userInitiatedReboot:
            automaticallyApprove: {{ automaticallyApprove }}
          scheduledEventsAdditionalPublishingTargets:
            eventGridAndResourceGraph:
              enable: {{ enable }}
              scheduledEventsApiVersion: "{{ scheduledEventsApiVersion }}"
          allInstancesDown:
            automaticallyApprove: {{ automaticallyApprove }}
        virtualMachineScaleSetMigrationInfo:
          defaultVirtualMachineScaleSetInfo:
            constrainedMaximumCapacity: {{ constrainedMaximumCapacity }}
            defaultVirtualMachineScaleSet:
              id: "{{ id }}"
          migrateToVirtualMachineScaleSet:
            id: "{{ id }}"
    - name: sku
      description: |
        Sku of the availability set, only name is required to be set. See AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for virtual machines with managed disks and 'Classic' for virtual machines with unmanaged disks. Default value is 'Classic'.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Update an availability set.

```sql
UPDATE azure.compute.availability_sets
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND availability_set_name = '{{ availability_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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

Create or update an availability set.

```sql
REPLACE azure.compute.availability_sets
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND availability_set_name = '{{ availability_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
sku,
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

Delete an availability set.

```sql
DELETE FROM azure.compute.availability_sets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND availability_set_name = '{{ availability_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_available_sizes"
    values={[
        { label: 'list_available_sizes', value: 'list_available_sizes' },
        { label: 'start_migration_to_virtual_machine_scale_set', value: 'start_migration_to_virtual_machine_scale_set' },
        { label: 'cancel_migration_to_virtual_machine_scale_set', value: 'cancel_migration_to_virtual_machine_scale_set' },
        { label: 'validate_migration_to_virtual_machine_scale_set', value: 'validate_migration_to_virtual_machine_scale_set' },
        { label: 'convert_to_virtual_machine_scale_set', value: 'convert_to_virtual_machine_scale_set' }
    ]}
>
<TabItem value="list_available_sizes">

Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set.

```sql
EXEC azure.compute.availability_sets.list_available_sizes 
@resource_group_name='{{ resource_group_name }}' --required, 
@availability_set_name='{{ availability_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_migration_to_virtual_machine_scale_set">

Start migration operation on an Availability Set to move its Virtual Machines to a Virtual Machine Scale Set. This should be followed by a migrate operation on each Virtual Machine that triggers a downtime on the Virtual Machine.

```sql
EXEC azure.compute.availability_sets.start_migration_to_virtual_machine_scale_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@availability_set_name='{{ availability_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"virtualMachineScaleSetFlexible": "{{ virtualMachineScaleSetFlexible }}"
}'
;
```
</TabItem>
<TabItem value="cancel_migration_to_virtual_machine_scale_set">

Cancel the migration operation on an Availability Set.

```sql
EXEC azure.compute.availability_sets.cancel_migration_to_virtual_machine_scale_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@availability_set_name='{{ availability_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_migration_to_virtual_machine_scale_set">

Validates that the Virtual Machines in the Availability Set can be migrated to the provided Virtual Machine Scale Set.

```sql
EXEC azure.compute.availability_sets.validate_migration_to_virtual_machine_scale_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@availability_set_name='{{ availability_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"virtualMachineScaleSetFlexible": "{{ virtualMachineScaleSetFlexible }}"
}'
;
```
</TabItem>
<TabItem value="convert_to_virtual_machine_scale_set">

Create a new Flexible Virtual Machine Scale Set and migrate all the Virtual Machines in the Availability Set. This does not trigger a downtime on the Virtual Machines.

```sql
EXEC azure.compute.availability_sets.convert_to_virtual_machine_scale_set 
@resource_group_name='{{ resource_group_name }}' --required, 
@availability_set_name='{{ availability_set_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"virtualMachineScaleSetName": "{{ virtualMachineScaleSetName }}"
}'
;
```
</TabItem>
</Tabs>
