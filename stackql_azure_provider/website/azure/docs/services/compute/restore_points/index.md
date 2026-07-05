--- 
title: restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_points
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

Creates, updates, deletes, gets or lists a <code>restore_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="restore_points" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.restore_points" /></td></tr>
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
    <td><CopyableCode code="consistencyMode" /></td>
    <td><code>string</code></td>
    <td>ConsistencyMode of the RestorePoint. Can be specified in the input while creating a restore point. For now, only CrashConsistent is accepted as a valid input. Please refer to `https://aka.ms/RestorePoints `_ for more details. Known values are: "CrashConsistent", "FileSystemConsistent", and "ApplicationConsistent". (CrashConsistent, FileSystemConsistent, ApplicationConsistent)</td>
</tr>
<tr>
    <td><CopyableCode code="excludeDisks" /></td>
    <td><code>array</code></td>
    <td>List of disk resource ids that the customer wishes to exclude from the restore point. If no disks are specified, all disks will be included.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The restore point instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="instantAccessDurationMinutes" /></td>
    <td><code>integer</code></td>
    <td>This property determines the time in minutes the snapshot is retained as instant access for restoring Premium SSD v2 or Ultra disk with fast restore performance in this restore point.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the provisioning state of the restore point.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceMetadata" /></td>
    <td><code>object</code></td>
    <td>Gets the details of the VM captured at the time of the restore point creation.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceRestorePoint" /></td>
    <td><code>object</code></td>
    <td>The API entity reference.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeCreated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the creation time of the restore point.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-restore_point_name"><code>restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get the restore point.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-restore_point_name"><code>restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to create the restore point. Updating properties of an existing restore point is not allowed.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-restore_point_collection_name"><code>restore_point_collection_name</code></a>, <a href="#parameter-restore_point_name"><code>restore_point_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete the restore point.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-restore_point_collection_name">
    <td><CopyableCode code="restore_point_collection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the restore point collection. Required.</td>
</tr>
<tr id="parameter-restore_point_name">
    <td><CopyableCode code="restore_point_name" /></td>
    <td><code>string</code></td>
    <td>The name of the restore point. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. 'InstanceView' retrieves information about the run-time state of a restore point. "instanceView" Default value is None.</td>
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

The operation to get the restore point.

```sql
SELECT
id,
name,
consistencyMode,
excludeDisks,
instanceView,
instantAccessDurationMinutes,
provisioningState,
sourceMetadata,
sourceRestorePoint,
systemData,
timeCreated,
type
FROM azure.compute.restore_points
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' -- required
AND restore_point_name = '{{ restore_point_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
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

The operation to create the restore point. Updating properties of an existing restore point is not allowed.

```sql
INSERT INTO azure.compute.restore_points (
properties,
resource_group_name,
restore_point_collection_name,
restore_point_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ restore_point_collection_name }}',
'{{ restore_point_name }}',
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
- name: restore_points
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the restore_points resource.
    - name: restore_point_collection_name
      value: "{{ restore_point_collection_name }}"
      description: Required parameter for the restore_points resource.
    - name: restore_point_name
      value: "{{ restore_point_name }}"
      description: Required parameter for the restore_points resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the restore_points resource.
    - name: properties
      description: |
        The restore point properties.
      value:
        excludeDisks:
          - id: "{{ id }}"
        sourceMetadata:
          hardwareProfile:
            vmSize: "{{ vmSize }}"
            vmSizeProperties:
              vCPUsAvailable: {{ vCPUsAvailable }}
              vCPUsPerCore: {{ vCPUsPerCore }}
          storageProfile:
            osDisk:
              osType: "{{ osType }}"
              encryptionSettings:
                diskEncryptionKey: "{{ diskEncryptionKey }}"
                keyEncryptionKey: "{{ keyEncryptionKey }}"
                enabled: {{ enabled }}
              name: "{{ name }}"
              caching: "{{ caching }}"
              diskSizeGB: {{ diskSizeGB }}
              managedDisk:
                id: "{{ id }}"
                storageAccountType: "{{ storageAccountType }}"
                diskEncryptionSet: "{{ diskEncryptionSet }}"
                securityProfile: "{{ securityProfile }}"
              diskRestorePoint:
                id: "{{ id }}"
                encryption: "{{ encryption }}"
                sourceDiskRestorePoint: "{{ sourceDiskRestorePoint }}"
              writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
            dataDisks:
              - lun: {{ lun }}
                name: "{{ name }}"
                caching: "{{ caching }}"
                diskSizeGB: {{ diskSizeGB }}
                managedDisk:
                  id: "{{ id }}"
                  storageAccountType: "{{ storageAccountType }}"
                  diskEncryptionSet: "{{ diskEncryptionSet }}"
                  securityProfile: "{{ securityProfile }}"
                diskRestorePoint:
                  id: "{{ id }}"
                  encryption: "{{ encryption }}"
                  sourceDiskRestorePoint: "{{ sourceDiskRestorePoint }}"
                writeAcceleratorEnabled: {{ writeAcceleratorEnabled }}
            diskControllerType: "{{ diskControllerType }}"
          osProfile:
            computerName: "{{ computerName }}"
            adminUsername: "{{ adminUsername }}"
            adminPassword: "{{ adminPassword }}"
            customData: "{{ customData }}"
            windowsConfiguration:
              provisionVMAgent: {{ provisionVMAgent }}
              enableAutomaticUpdates: {{ enableAutomaticUpdates }}
              timeZone: "{{ timeZone }}"
              additionalUnattendContent:
                - passName: "{{ passName }}"
                  componentName: "{{ componentName }}"
                  settingName: "{{ settingName }}"
                  content: "{{ content }}"
              patchSettings:
                patchMode: "{{ patchMode }}"
                enableHotpatching: {{ enableHotpatching }}
                assessmentMode: "{{ assessmentMode }}"
                automaticByPlatformSettings: "{{ automaticByPlatformSettings }}"
              winRM:
                listeners: "{{ listeners }}"
              enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
            linuxConfiguration:
              disablePasswordAuthentication: {{ disablePasswordAuthentication }}
              ssh:
                publicKeys: "{{ publicKeys }}"
              provisionVMAgent: {{ provisionVMAgent }}
              patchSettings:
                patchMode: "{{ patchMode }}"
                assessmentMode: "{{ assessmentMode }}"
                automaticByPlatformSettings: "{{ automaticByPlatformSettings }}"
              enableVMAgentPlatformUpdates: {{ enableVMAgentPlatformUpdates }}
            secrets:
              - sourceVault:
                  id: "{{ id }}"
                vaultCertificates: "{{ vaultCertificates }}"
            allowExtensionOperations: {{ allowExtensionOperations }}
            requireGuestProvisionSignal: {{ requireGuestProvisionSignal }}
          diagnosticsProfile:
            bootDiagnostics:
              enabled: {{ enabled }}
              storageUri: "{{ storageUri }}"
          licenseType: "{{ licenseType }}"
          vmId: "{{ vmId }}"
          securityProfile:
            uefiSettings:
              secureBootEnabled: {{ secureBootEnabled }}
              vTpmEnabled: {{ vTpmEnabled }}
            encryptionAtHost: {{ encryptionAtHost }}
            securityType: "{{ securityType }}"
            encryptionIdentity:
              userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
            proxyAgentSettings:
              enabled: {{ enabled }}
              mode: "{{ mode }}"
              keyIncarnationId: {{ keyIncarnationId }}
              wireServer:
                mode: "{{ mode }}"
                inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
              imds:
                mode: "{{ mode }}"
                inVMAccessControlProfileReferenceId: "{{ inVMAccessControlProfileReferenceId }}"
              addProxyAgentExtension: {{ addProxyAgentExtension }}
          location: "{{ location }}"
          userData: "{{ userData }}"
          hyperVGeneration: "{{ hyperVGeneration }}"
        provisioningState: "{{ provisioningState }}"
        consistencyMode: "{{ consistencyMode }}"
        timeCreated: "{{ timeCreated }}"
        sourceRestorePoint:
          id: "{{ id }}"
        instanceView:
          diskRestorePoints:
            - id: "{{ id }}"
              snapshotAccessState: "{{ snapshotAccessState }}"
              replicationStatus:
                status:
                  code: "{{ code }}"
                  level: "{{ level }}"
                  displayStatus: "{{ displayStatus }}"
                  message: "{{ message }}"
                  time: "{{ time }}"
                completionPercent: {{ completionPercent }}
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        instantAccessDurationMinutes: {{ instantAccessDurationMinutes }}
`}</CodeBlock>

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

The operation to delete the restore point.

```sql
DELETE FROM azure.compute.restore_points
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND restore_point_collection_name = '{{ restore_point_collection_name }}' --required
AND restore_point_name = '{{ restore_point_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
