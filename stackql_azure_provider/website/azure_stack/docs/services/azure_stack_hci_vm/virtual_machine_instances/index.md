--- 
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - azure_stack_hci_vm
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci_vm.virtual_machine_instances" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createFromLocal" /></td>
    <td><code>boolean</code></td>
    <td>Boolean indicating whether this is an existing local virtual machine or if one should be created.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extendedLocation of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="guestAgentInstallStatus" /></td>
    <td><code>object</code></td>
    <td>Guest agent install status.</td>
</tr>
<tr>
    <td><CopyableCode code="hardwareProfile" /></td>
    <td><code>object</code></td>
    <td>HardwareProfile - Specifies the hardware settings for the virtual machine instance.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNodeIpAddress" /></td>
    <td><code>string</code></td>
    <td>Name of the host node that the VM is on.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNodeName" /></td>
    <td><code>string</code></td>
    <td>Name of the host node that the VM is on.</td>
</tr>
<tr>
    <td><CopyableCode code="httpProxyConfig" /></td>
    <td><code>object</code></td>
    <td>HTTP Proxy configuration for the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVVmId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the Hyper-V VM resource.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>NetworkProfile - describes the network configuration the virtual machine instance.</td>
</tr>
<tr>
    <td><CopyableCode code="osProfile" /></td>
    <td><code>object</code></td>
    <td>OsProfile - describes the configuration of the operating system and sets login data.</td>
</tr>
<tr>
    <td><CopyableCode code="placementProfile" /></td>
    <td><code>object</code></td>
    <td>PlacementProfile - Specifies the placement related settings for the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the virtual machine instance. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUid" /></td>
    <td><code>string</code></td>
    <td>Unique identifier defined by ARC to identify the guest of the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>SecurityProfile - Specifies the security settings for the virtual machine instance.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed state of virtual machine instances.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>StorageProfile - contains information about the disks and storage information for the virtual machine instance.</td>
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
<tr>
    <td><CopyableCode code="vmId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the vm resource.</td>
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
    <td>Gets a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to update a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to delete a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to start a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to stop a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to restart a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to pause a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#save"><CopyableCode code="save" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>The operation to save a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Lists all of the virtual machine instances within the specified parent resource.</td>
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

Gets a virtual machine instance.

```sql
SELECT
id,
name,
createFromLocal,
extendedLocation,
guestAgentInstallStatus,
hardwareProfile,
hostNodeIpAddress,
hostNodeName,
httpProxyConfig,
hyperVVmId,
identity,
instanceView,
networkProfile,
osProfile,
placementProfile,
provisioningState,
resourceUid,
securityProfile,
status,
storageProfile,
systemData,
type,
vmId
FROM azure_stack.azure_stack_hci_vm.virtual_machine_instances
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
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.

```sql
INSERT INTO azure_stack.azure_stack_hci_vm.virtual_machine_instances (
properties,
extendedLocation,
identity,
resource_uri
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ identity }}',
'{{ resource_uri }}'
RETURNING
id,
name,
extendedLocation,
identity,
properties,
systemData,
type
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
        hardwareProfile:
          vmSize: "{{ vmSize }}"
          processors: {{ processors }}
          memoryMB: {{ memoryMB }}
          dynamicMemoryConfig:
            maximumMemoryMB: {{ maximumMemoryMB }}
            minimumMemoryMB: {{ minimumMemoryMB }}
            targetMemoryBuffer: {{ targetMemoryBuffer }}
          virtualMachineGPUs:
            - assignmentType: "{{ assignmentType }}"
              partitionSizeMB: {{ partitionSizeMB }}
              gpuName: "{{ gpuName }}"
        placementProfile:
          zone: "{{ zone }}"
          strictPlacementPolicy: {{ strictPlacementPolicy }}
        networkProfile:
          networkInterfaces:
            - id: "{{ id }}"
        osProfile:
          adminPassword: "{{ adminPassword }}"
          adminUsername: "{{ adminUsername }}"
          computerName: "{{ computerName }}"
          linuxConfiguration:
            disablePasswordAuthentication: {{ disablePasswordAuthentication }}
            ssh:
              publicKeys:
                - path: "{{ path }}"
                  keyData: "{{ keyData }}"
            provisionVMAgent: {{ provisionVMAgent }}
            provisionVMConfigAgent: {{ provisionVMConfigAgent }}
          windowsConfiguration:
            enableAutomaticUpdates: {{ enableAutomaticUpdates }}
            ssh:
              publicKeys:
                - path: "{{ path }}"
                  keyData: "{{ keyData }}"
            timeZone: "{{ timeZone }}"
            provisionVMAgent: {{ provisionVMAgent }}
            provisionVMConfigAgent: {{ provisionVMConfigAgent }}
        securityProfile:
          enableTPM: {{ enableTPM }}
          uefiSettings:
            secureBootEnabled: {{ secureBootEnabled }}
          securityType: "{{ securityType }}"
        storageProfile:
          dataDisks:
            - id: "{{ id }}"
          imageReference:
            id: "{{ id }}"
          osDisk:
            id: "{{ id }}"
            osType: "{{ osType }}"
            managedDisk:
              securityProfile:
                securityEncryptionType: "{{ securityEncryptionType }}"
          vmConfigStoragePathId: "{{ vmConfigStoragePathId }}"
        httpProxyConfig:
          httpProxy: "{{ httpProxy }}"
          httpsProxy: "{{ httpsProxy }}"
          noProxy:
            - "{{ noProxy }}"
          trustedCa: "{{ trustedCa }}"
        createFromLocal: {{ createFromLocal }}
        provisioningState: "{{ provisioningState }}"
        instanceView:
          vmAgent:
            vmConfigAgentVersion: "{{ vmConfigAgentVersion }}"
            statuses:
              - code: "{{ code }}"
                level: "{{ level }}"
                displayStatus: "{{ displayStatus }}"
                message: "{{ message }}"
                time: "{{ time }}"
        status:
          errorCode: "{{ errorCode }}"
          errorMessage: "{{ errorMessage }}"
          powerState: "{{ powerState }}"
          provisioningStatus:
            operationId: "{{ operationId }}"
            status: "{{ status }}"
        guestAgentInstallStatus:
          vmUuid: "{{ vmUuid }}"
          status: "{{ status }}"
          lastStatusChange: "{{ lastStatusChange }}"
          agentVersion: "{{ agentVersion }}"
          errorDetails:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
        vmId: "{{ vmId }}"
        resourceUid: "{{ resourceUid }}"
        hyperVVmId: "{{ hyperVVmId }}"
        hostNodeName: "{{ hostNodeName }}"
        hostNodeIpAddress: "{{ hostNodeIpAddress }}"
    - name: extendedLocation
      description: |
        The extendedLocation of the resource.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
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

The operation to update a virtual machine instance.

```sql
UPDATE azure_stack.azure_stack_hci_vm.virtual_machine_instances
SET 
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
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

The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.

```sql
REPLACE azure_stack.azure_stack_hci_vm.virtual_machine_instances
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
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

The operation to delete a virtual machine instance.

```sql
DELETE FROM azure_stack.azure_stack_hci_vm.virtual_machine_instances
WHERE resource_uri = '{{ resource_uri }}' --required
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
        { label: 'restart', value: 'restart' },
        { label: 'pause', value: 'pause' },
        { label: 'save', value: 'save' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="start">

The operation to start a virtual machine instance.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_machine_instances.start 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="stop">

The operation to stop a virtual machine instance.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_machine_instances.stop 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="restart">

The operation to restart a virtual machine instance.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_machine_instances.restart 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="pause">

The operation to pause a virtual machine instance.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_machine_instances.pause 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="save">

The operation to save a virtual machine instance.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_machine_instances.save 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Lists all of the virtual machine instances within the specified parent resource.

```sql
EXEC azure_stack.azure_stack_hci_vm.virtual_machine_instances.list_raw 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
</Tabs>
