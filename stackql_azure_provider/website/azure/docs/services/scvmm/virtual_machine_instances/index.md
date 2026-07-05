--- 
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - scvmm
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scvmm.virtual_machine_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilitySets" /></td>
    <td><code>array</code></td>
    <td>Availability Sets in vm.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>Hardware properties.</td>
</tr>
<tr>
    <td><CopyableCode code="infrastructureProfile" /></td>
    <td><code>object</code></td>
    <td>Gets the infrastructure profile.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Network properties.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>OS properties.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Gets the power state of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>Storage properties.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Gets a virtual machine. Retrieves information about a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.</td>
</tr>
<tr>
    <td><a href="#create_checkpoint"><CopyableCode code="create_checkpoint" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to creates a checkpoint in a virtual machine instance. Creates a checkpoint in virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Updates a virtual machine. The operation to update a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-extendedLocation"><code>extendedLocation</code></a></td>
    <td></td>
    <td>Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a>, <a href="#parameter-deleteFromHost"><code>deleteFromHost</code></a></td>
    <td>Deletes an virtual machine. The operation to delete a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#delete_checkpoint"><CopyableCode code="delete_checkpoint" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to delete a checkpoint in a virtual machine instance. Deletes a checkpoint in virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to restart a virtual machine. The operation to restart a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#restore_checkpoint"><CopyableCode code="restore_checkpoint" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to restores to a checkpoint in a virtual machine instance. Restores to a checkpoint in virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to start a virtual machine. The operation to start a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to stop a virtual machine. The operation to power off (stop) a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements List virtual machine instances. Lists all of the virtual machine instances within the specified parent resource.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-deleteFromHost">
    <td><CopyableCode code="deleteFromHost" /></td>
    <td><code>string</code></td>
    <td>Whether to disable the VM from azure and also delete it from Vmm. Known values are: "true" and "false". Default value is None.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td>Forces the resource to be deleted. Known values are: "true" and "false". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a virtual machine. Retrieves information about a virtual machine instance.

```sql
SELECT
id,
name,
availabilitySets,
extendedLocation,
hardwareProfile,
infrastructureProfile,
networkProfile,
osProfile,
powerState,
provisioningState,
storageProfile,
systemData,
type
FROM azure.scvmm.virtual_machine_instances
WHERE resource_uri = '{{ resource_uri }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_checkpoint', value: 'create_checkpoint' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.

```sql
INSERT INTO azure.scvmm.virtual_machine_instances (
properties,
extendedLocation,
resource_uri
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}' /* required */,
'{{ resource_uri }}'
RETURNING
id,
name,
extendedLocation,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="create_checkpoint">

Implements the operation to creates a checkpoint in a virtual machine instance. Creates a checkpoint in virtual machine instance.

```sql
INSERT INTO azure.scvmm.virtual_machine_instances (
name,
description,
resource_uri
)
SELECT 
'{{ name }}',
'{{ description }}',
'{{ resource_uri }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_machine_instances
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the virtual_machine_instances resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        availabilitySets:
          - id: "{{ id }}"
            name: "{{ name }}"
        osProfile:
          adminPassword: "{{ adminPassword }}"
          computerName: "{{ computerName }}"
          osType: "{{ osType }}"
          osSku: "{{ osSku }}"
          osVersion: "{{ osVersion }}"
        hardwareProfile:
          memoryMB: {{ memoryMB }}
          cpuCount: {{ cpuCount }}
          limitCpuForMigration: "{{ limitCpuForMigration }}"
          dynamicMemoryEnabled: "{{ dynamicMemoryEnabled }}"
          dynamicMemoryMaxMB: {{ dynamicMemoryMaxMB }}
          dynamicMemoryMinMB: {{ dynamicMemoryMinMB }}
          isHighlyAvailable: "{{ isHighlyAvailable }}"
        networkProfile:
          networkInterfaces:
            - name: "{{ name }}"
              displayName: "{{ displayName }}"
              ipv4Addresses: "{{ ipv4Addresses }}"
              ipv6Addresses: "{{ ipv6Addresses }}"
              macAddress: "{{ macAddress }}"
              virtualNetworkId: "{{ virtualNetworkId }}"
              networkName: "{{ networkName }}"
              ipv4AddressType: "{{ ipv4AddressType }}"
              ipv6AddressType: "{{ ipv6AddressType }}"
              macAddressType: "{{ macAddressType }}"
              nicId: "{{ nicId }}"
        storageProfile:
          disks:
            - name: "{{ name }}"
              displayName: "{{ displayName }}"
              diskId: "{{ diskId }}"
              diskSizeGB: {{ diskSizeGB }}
              maxDiskSizeGB: {{ maxDiskSizeGB }}
              bus: {{ bus }}
              lun: {{ lun }}
              busType: "{{ busType }}"
              vhdType: "{{ vhdType }}"
              volumeType: "{{ volumeType }}"
              vhdFormatType: "{{ vhdFormatType }}"
              templateDiskId: "{{ templateDiskId }}"
              storageQoSPolicy:
                name: "{{ name }}"
                id: "{{ id }}"
              createDiffDisk: "{{ createDiffDisk }}"
        infrastructureProfile:
          inventoryItemId: "{{ inventoryItemId }}"
          vmmServerId: "{{ vmmServerId }}"
          cloudId: "{{ cloudId }}"
          templateId: "{{ templateId }}"
          vmName: "{{ vmName }}"
          uuid: "{{ uuid }}"
          lastRestoredVMCheckpoint:
            parentCheckpointID: "{{ parentCheckpointID }}"
            checkpointID: "{{ checkpointID }}"
            name: "{{ name }}"
            description: "{{ description }}"
          checkpoints:
            - parentCheckpointID: "{{ parentCheckpointID }}"
              checkpointID: "{{ checkpointID }}"
              name: "{{ name }}"
              description: "{{ description }}"
          checkpointType: "{{ checkpointType }}"
          generation: {{ generation }}
          biosGuid: "{{ biosGuid }}"
        powerState: "{{ powerState }}"
        provisioningState: "{{ provisioningState }}"
    - name: extendedLocation
      description: |
        Gets or sets the extended location. Required.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
    - name: name
      value: "{{ name }}"
      description: |
        Name of the checkpoint.
    - name: description
      value: "{{ description }}"
      description: |
        Description of the checkpoint.
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

Updates a virtual machine. The operation to update a virtual machine instance.

```sql
UPDATE azure.scvmm.virtual_machine_instances
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
RETURNING
id,
name,
extendedLocation,
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

Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.

```sql
REPLACE azure.scvmm.virtual_machine_instances
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND extendedLocation = '{{ extendedLocation }}' --required
RETURNING
id,
name,
extendedLocation,
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

Deletes an virtual machine. The operation to delete a virtual machine instance.

```sql
DELETE FROM azure.scvmm.virtual_machine_instances
WHERE resource_uri = '{{ resource_uri }}' --required
AND force = '{{ force }}'
AND deleteFromHost = '{{ deleteFromHost }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete_checkpoint"
    values={[
        { label: 'delete_checkpoint', value: 'delete_checkpoint' },
        { label: 'restart', value: 'restart' },
        { label: 'restore_checkpoint', value: 'restore_checkpoint' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="delete_checkpoint">

Implements the operation to delete a checkpoint in a virtual machine instance. Deletes a checkpoint in virtual machine instance.

```sql
EXEC azure.scvmm.virtual_machine_instances.delete_checkpoint 
@resource_uri='{{ resource_uri }}' --required 
@@json=
'{
"id": "{{ id }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Implements the operation to restart a virtual machine. The operation to restart a virtual machine instance.

```sql
EXEC azure.scvmm.virtual_machine_instances.restart 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="restore_checkpoint">

Implements the operation to restores to a checkpoint in a virtual machine instance. Restores to a checkpoint in virtual machine instance.

```sql
EXEC azure.scvmm.virtual_machine_instances.restore_checkpoint 
@resource_uri='{{ resource_uri }}' --required 
@@json=
'{
"id": "{{ id }}"
}'
;
```
</TabItem>
<TabItem value="start">

Implements the operation to start a virtual machine. The operation to start a virtual machine instance.

```sql
EXEC azure.scvmm.virtual_machine_instances.start 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="stop">

Implements the operation to stop a virtual machine. The operation to power off (stop) a virtual machine instance.

```sql
EXEC azure.scvmm.virtual_machine_instances.stop 
@resource_uri='{{ resource_uri }}' --required 
@@json=
'{
"skipShutdown": "{{ skipShutdown }}"
}'
;
```
</TabItem>
<TabItem value="list_raw">

Implements List virtual machine instances. Lists all of the virtual machine instances within the specified parent resource.

```sql
EXEC azure.scvmm.virtual_machine_instances.list_raw 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
</Tabs>
