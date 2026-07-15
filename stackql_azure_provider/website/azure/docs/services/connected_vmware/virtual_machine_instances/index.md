--- 
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - connected_vmware
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.connected_vmware.virtual_machine_instances" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the extended location.</td>
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
    <td><CopyableCode code="placementProfile" /></td>
    <td><code>object</code></td>
    <td>Placement properties.</td>
</tr>
<tr>
    <td><CopyableCode code="powerState" /></td>
    <td><code>string</code></td>
    <td>Gets the power state of the virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", "Accepted", and "Created".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceUid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets a unique identifier for the vm resource.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>Gets the security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>The resource status information.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td><a href="#parameter-deleteFromHost"><code>deleteFromHost</code></a>, <a href="#parameter-force"><code>force</code></a></td>
    <td>Deletes an virtual machine. The operation to delete a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to stop a virtual machine. The operation to power off (stop) a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to start a virtual machine. The operation to start a virtual machine instance.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements the operation to restart a virtual machine. The operation to restart a virtual machine instance.</td>
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
    <td>The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended. Required.</td>
</tr>
<tr id="parameter-deleteFromHost">
    <td><CopyableCode code="deleteFromHost" /></td>
    <td><code>boolean</code></td>
    <td>Whether to delete the VM from the vCenter. Default value is None.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>Whether force delete was specified. Default value is None.</td>
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
extendedLocation,
hardwareProfile,
infrastructureProfile,
networkProfile,
osProfile,
placementProfile,
powerState,
provisioningState,
resourceUid,
securityProfile,
statuses,
storageProfile,
systemData,
type
FROM azure.connected_vmware.virtual_machine_instances
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

Implements virtual machine PUT method. The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation.

```sql
INSERT INTO azure.connected_vmware.virtual_machine_instances (
extendedLocation,
properties,
resource_uri
)
SELECT 
'{{ extendedLocation }}',
'{{ properties }}',
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
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: virtual_machine_instances
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the virtual_machine_instances resource.
    - name: extendedLocation
      description: |
        Gets or sets the extended location.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
    - name: properties
      value:
        placementProfile:
          resourcePoolId: "{{ resourcePoolId }}"
          clusterId: "{{ clusterId }}"
          hostId: "{{ hostId }}"
          datastoreId: "{{ datastoreId }}"
        osProfile:
          computerName: "{{ computerName }}"
          adminUsername: "{{ adminUsername }}"
          adminPassword: "{{ adminPassword }}"
          guestId: "{{ guestId }}"
          osType: "{{ osType }}"
          osSku: "{{ osSku }}"
          toolsRunningStatus: "{{ toolsRunningStatus }}"
          toolsVersionStatus: "{{ toolsVersionStatus }}"
          toolsVersion: "{{ toolsVersion }}"
        hardwareProfile:
          memorySizeMB: {{ memorySizeMB }}
          numCPUs: {{ numCPUs }}
          numCoresPerSocket: {{ numCoresPerSocket }}
          cpuHotAddEnabled: {{ cpuHotAddEnabled }}
          cpuHotRemoveEnabled: {{ cpuHotRemoveEnabled }}
          memoryHotAddEnabled: {{ memoryHotAddEnabled }}
        networkProfile:
          networkInterfaces:
            - name: "{{ name }}"
              label: "{{ label }}"
              ipAddresses: "{{ ipAddresses }}"
              macAddress: "{{ macAddress }}"
              networkId: "{{ networkId }}"
              nicType: "{{ nicType }}"
              powerOnBoot: "{{ powerOnBoot }}"
              networkMoRefId: "{{ networkMoRefId }}"
              networkMoName: "{{ networkMoName }}"
              deviceKey: {{ deviceKey }}
              ipSettings:
                allocationMethod: "{{ allocationMethod }}"
                dnsServers:
                  - "{{ dnsServers }}"
                gateway:
                  - "{{ gateway }}"
                ipAddress: "{{ ipAddress }}"
                subnetMask: "{{ subnetMask }}"
                primaryWinsServer: "{{ primaryWinsServer }}"
                secondaryWinsServer: "{{ secondaryWinsServer }}"
                ipAddressInfo:
                  - allocationMethod: "{{ allocationMethod }}"
                    ipAddress: "{{ ipAddress }}"
                    subnetMask: "{{ subnetMask }}"
        storageProfile:
          disks:
            - name: "{{ name }}"
              label: "{{ label }}"
              diskObjectId: "{{ diskObjectId }}"
              diskSizeGB: {{ diskSizeGB }}
              deviceKey: {{ deviceKey }}
              diskMode: "{{ diskMode }}"
              controllerKey: {{ controllerKey }}
              unitNumber: {{ unitNumber }}
              deviceName: "{{ deviceName }}"
              diskType: "{{ diskType }}"
          scsiControllers:
            - type: "{{ type }}"
              controllerKey: {{ controllerKey }}
              busNumber: {{ busNumber }}
              scsiCtlrUnitNumber: {{ scsiCtlrUnitNumber }}
              sharing: "{{ sharing }}"
        securityProfile:
          uefiSettings:
            secureBootEnabled: {{ secureBootEnabled }}
        infrastructureProfile:
          templateId: "{{ templateId }}"
          vCenterId: "{{ vCenterId }}"
          moRefId: "{{ moRefId }}"
          inventoryItemId: "{{ inventoryItemId }}"
          moName: "{{ moName }}"
          folderPath: "{{ folderPath }}"
          instanceUuid: "{{ instanceUuid }}"
          smbiosUuid: "{{ smbiosUuid }}"
          firmwareType: "{{ firmwareType }}"
          customResourceName: "{{ customResourceName }}"
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
UPDATE azure.connected_vmware.virtual_machine_instances
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
REPLACE azure.connected_vmware.virtual_machine_instances
SET 
extendedLocation = '{{ extendedLocation }}',
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
DELETE FROM azure.connected_vmware.virtual_machine_instances
WHERE resource_uri = '{{ resource_uri }}' --required
AND deleteFromHost = '{{ deleteFromHost }}'
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' },
        { label: 'start', value: 'start' },
        { label: 'restart', value: 'restart' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="stop">

Implements the operation to stop a virtual machine. The operation to power off (stop) a virtual machine instance.

```sql
EXEC azure.connected_vmware.virtual_machine_instances.stop 
@resource_uri='{{ resource_uri }}' --required 
@@json=
'{
"skipShutdown": {{ skipShutdown }}
}'
;
```
</TabItem>
<TabItem value="start">

Implements the operation to start a virtual machine. The operation to start a virtual machine instance.

```sql
EXEC azure.connected_vmware.virtual_machine_instances.start 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="restart">

Implements the operation to restart a virtual machine. The operation to restart a virtual machine instance.

```sql
EXEC azure.connected_vmware.virtual_machine_instances.restart 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Implements List virtual machine instances. Lists all of the virtual machine instances within the specified parent resource.

```sql
EXEC azure.connected_vmware.virtual_machine_instances.list_raw 
@resource_uri='{{ resource_uri }}' --required
;
```
</TabItem>
</Tabs>
