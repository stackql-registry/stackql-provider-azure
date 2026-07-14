--- 
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
  - container_service
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

Creates, updates, deletes, gets or lists a <code>machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.machines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="billing" /></td>
    <td><code>object</code></td>
    <td>The properties having to do with machine billing.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Unique read-only string used to implement optimistic concurrency. The eTag value will change when the resource is updated. Specify an if-match or if-none-match header with the eTag value for a subsequent request to enable optimistic concurrency per the normal eTag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>The eviction policy for machine. This cannot be specified unless the priority is 'Spot'. If not specified, the default is 'Delete'. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="hardware" /></td>
    <td><code>object</code></td>
    <td>The hardware and GPU settings of the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetes" /></td>
    <td><code>object</code></td>
    <td>The Kubernetes configurations used by the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="localDNSProfile" /></td>
    <td><code>object</code></td>
    <td>Configures the per-node local DNS, with VnetDNS and KubeDNS overrides. LocalDNS helps improve performance and reliability of DNS resolution in an AKS cluster. For more details see aka.ms/aks/localdns.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Machine only allows 'System' and 'User' mode. Known values are: "System", "User", "Gateway", "ManagedSystem", and "Machines". (System, User, Gateway, ManagedSystem, Machines)</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>network properties of the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of node image.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystem" /></td>
    <td><code>object</code></td>
    <td>The operating system and disk used by the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority for the machine. If not specified, the default is 'Regular'. Known values are: "Spot" and "Regular". (Spot, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource id of the machine. It can be used to GET underlying VM Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="security" /></td>
    <td><code>object</code></td>
    <td>The security settings of the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags to be persisted on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The Availability zone in which machine is located.</td>
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
    <td><CopyableCode code="billing" /></td>
    <td><code>object</code></td>
    <td>The properties having to do with machine billing.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>Unique read-only string used to implement optimistic concurrency. The eTag value will change when the resource is updated. Specify an if-match or if-none-match header with the eTag value for a subsequent request to enable optimistic concurrency per the normal eTag convention.</td>
</tr>
<tr>
    <td><CopyableCode code="evictionPolicy" /></td>
    <td><code>string</code></td>
    <td>The eviction policy for machine. This cannot be specified unless the priority is 'Spot'. If not specified, the default is 'Delete'. Known values are: "Delete" and "Deallocate". (Delete, Deallocate)</td>
</tr>
<tr>
    <td><CopyableCode code="hardware" /></td>
    <td><code>object</code></td>
    <td>The hardware and GPU settings of the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetes" /></td>
    <td><code>object</code></td>
    <td>The Kubernetes configurations used by the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="localDNSProfile" /></td>
    <td><code>object</code></td>
    <td>Configures the per-node local DNS, with VnetDNS and KubeDNS overrides. LocalDNS helps improve performance and reliability of DNS resolution in an AKS cluster. For more details see aka.ms/aks/localdns.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Machine only allows 'System' and 'User' mode. Known values are: "System", "User", "Gateway", "ManagedSystem", and "Machines". (System, User, Gateway, ManagedSystem, Machines)</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>network properties of the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeImageVersion" /></td>
    <td><code>string</code></td>
    <td>The version of node image.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystem" /></td>
    <td><code>object</code></td>
    <td>The operating system and disk used by the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority for the machine. If not specified, the default is 'Regular'. Known values are: "Spot" and "Regular". (Spot, Regular)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current deployment or provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Azure resource id of the machine. It can be used to GET underlying VM Instance.</td>
</tr>
<tr>
    <td><CopyableCode code="security" /></td>
    <td><code>object</code></td>
    <td>The security settings of the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Contains read-only information about the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags to be persisted on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The Availability zone in which machine is located.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a specific machine in the specified agent pool.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of machines in the specified agent pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a machine in the specified agent pool.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-agent_pool_name"><code>agent_pool_name</code></a>, <a href="#parameter-machine_name"><code>machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a machine in the specified agent pool.</td>
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
<tr id="parameter-agent_pool_name">
    <td><CopyableCode code="agent_pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent pool. Required.</td>
</tr>
<tr id="parameter-machine_name">
    <td><CopyableCode code="machine_name" /></td>
    <td><code>string</code></td>
    <td>Host name of the machine. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed cluster resource. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a specific machine in the specified agent pool.

```sql
SELECT
id,
name,
billing,
eTag,
evictionPolicy,
hardware,
kubernetes,
localDNSProfile,
mode,
network,
nodeImageVersion,
operatingSystem,
priority,
provisioningState,
resourceId,
security,
status,
systemData,
tags,
type,
zones
FROM azure.container_service.machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND agent_pool_name = '{{ agent_pool_name }}' -- required
AND machine_name = '{{ machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of machines in the specified agent pool.

```sql
SELECT
id,
name,
billing,
eTag,
evictionPolicy,
hardware,
kubernetes,
localDNSProfile,
mode,
network,
nodeImageVersion,
operatingSystem,
priority,
provisioningState,
resourceId,
security,
status,
systemData,
tags,
type,
zones
FROM azure.container_service.machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND agent_pool_name = '{{ agent_pool_name }}' -- required
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

Creates or updates a machine in the specified agent pool.

```sql
INSERT INTO azure.container_service.machines (
properties,
zones,
resource_group_name,
resource_name,
agent_pool_name,
machine_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ agent_pool_name }}',
'{{ machine_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the machines resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the machines resource.
    - name: agent_pool_name
      value: "{{ agent_pool_name }}"
      description: Required parameter for the machines resource.
    - name: machine_name
      value: "{{ machine_name }}"
      description: Required parameter for the machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the machines resource.
    - name: properties
      description: |
        The properties of the machine.
      value:
        network:
          ipAddresses:
            - family: "{{ family }}"
              ip: "{{ ip }}"
          vnetSubnetID: "{{ vnetSubnetID }}"
          podSubnetID: "{{ podSubnetID }}"
          enableNodePublicIP: {{ enableNodePublicIP }}
          nodePublicIPPrefixID: "{{ nodePublicIPPrefixID }}"
          nodePublicIPTags:
            - ipTagType: "{{ ipTagType }}"
              tag: "{{ tag }}"
        resourceId: "{{ resourceId }}"
        hardware:
          vmSize: "{{ vmSize }}"
          gpuInstanceProfile: "{{ gpuInstanceProfile }}"
          gpuProfile:
            driver: "{{ driver }}"
            driverType: "{{ driverType }}"
            nvidia:
              managementMode: "{{ managementMode }}"
              migStrategy: "{{ migStrategy }}"
          ultraSsdEnabled: {{ ultraSsdEnabled }}
        operatingSystem:
          osType: "{{ osType }}"
          osSKU: "{{ osSKU }}"
          osDiskSizeGB: {{ osDiskSizeGB }}
          osDiskType: "{{ osDiskType }}"
          enableFIPS: {{ enableFIPS }}
          linuxProfile:
            linuxOSConfig:
              sysctls:
                netCoreSomaxconn: {{ netCoreSomaxconn }}
                netCoreNetdevMaxBacklog: {{ netCoreNetdevMaxBacklog }}
                netCoreRmemDefault: {{ netCoreRmemDefault }}
                netCoreRmemMax: {{ netCoreRmemMax }}
                netCoreWmemDefault: {{ netCoreWmemDefault }}
                netCoreWmemMax: {{ netCoreWmemMax }}
                netCoreOptmemMax: {{ netCoreOptmemMax }}
                netIpv4TcpMaxSynBacklog: {{ netIpv4TcpMaxSynBacklog }}
                netIpv4TcpMaxTwBuckets: {{ netIpv4TcpMaxTwBuckets }}
                netIpv4TcpFinTimeout: {{ netIpv4TcpFinTimeout }}
                netIpv4TcpKeepaliveTime: {{ netIpv4TcpKeepaliveTime }}
                netIpv4TcpKeepaliveProbes: {{ netIpv4TcpKeepaliveProbes }}
                netIpv4TcpkeepaliveIntvl: {{ netIpv4TcpkeepaliveIntvl }}
                netIpv4TcpTwReuse: {{ netIpv4TcpTwReuse }}
                netIpv4IpLocalPortRange: "{{ netIpv4IpLocalPortRange }}"
                netIpv4NeighDefaultGcThresh1: {{ netIpv4NeighDefaultGcThresh1 }}
                netIpv4NeighDefaultGcThresh2: {{ netIpv4NeighDefaultGcThresh2 }}
                netIpv4NeighDefaultGcThresh3: {{ netIpv4NeighDefaultGcThresh3 }}
                netNetfilterNfConntrackMax: {{ netNetfilterNfConntrackMax }}
                netNetfilterNfConntrackBuckets: {{ netNetfilterNfConntrackBuckets }}
                fsInotifyMaxUserWatches: {{ fsInotifyMaxUserWatches }}
                fsFileMax: {{ fsFileMax }}
                fsAioMaxNr: {{ fsAioMaxNr }}
                fsNrOpen: {{ fsNrOpen }}
                kernelThreadsMax: {{ kernelThreadsMax }}
                vmMaxMapCount: {{ vmMaxMapCount }}
                vmSwappiness: {{ vmSwappiness }}
                vmVfsCachePressure: {{ vmVfsCachePressure }}
              transparentHugePageEnabled: "{{ transparentHugePageEnabled }}"
              transparentHugePageDefrag: "{{ transparentHugePageDefrag }}"
              swapFileSizeMB: {{ swapFileSizeMB }}
            messageOfTheDay: "{{ messageOfTheDay }}"
          windowsProfile:
            disableOutboundNat: {{ disableOutboundNat }}
        kubernetes:
          nodeLabels: "{{ nodeLabels }}"
          orchestratorVersion: "{{ orchestratorVersion }}"
          currentOrchestratorVersion: "{{ currentOrchestratorVersion }}"
          kubeletDiskType: "{{ kubeletDiskType }}"
          kubeletConfig:
            cpuManagerPolicy: "{{ cpuManagerPolicy }}"
            cpuCfsQuota: {{ cpuCfsQuota }}
            cpuCfsQuotaPeriod: "{{ cpuCfsQuotaPeriod }}"
            imageGcHighThreshold: {{ imageGcHighThreshold }}
            imageGcLowThreshold: {{ imageGcLowThreshold }}
            topologyManagerPolicy: "{{ topologyManagerPolicy }}"
            allowedUnsafeSysctls:
              - "{{ allowedUnsafeSysctls }}"
            failSwapOn: {{ failSwapOn }}
            containerLogMaxSizeMB: {{ containerLogMaxSizeMB }}
            containerLogMaxFiles: {{ containerLogMaxFiles }}
            podMaxPids: {{ podMaxPids }}
            seccompDefault: "{{ seccompDefault }}"
            kubeReserved:
              cpuMillicores: {{ cpuMillicores }}
              memoryMB: {{ memoryMB }}
            hardEvictionThreshold:
              memoryAvailable: "{{ memoryAvailable }}"
              nodeFsAvailable: "{{ nodeFsAvailable }}"
              nodeFsInodesFree: "{{ nodeFsInodesFree }}"
          nodeInitializationTaints:
            - "{{ nodeInitializationTaints }}"
          nodeTaints:
            - "{{ nodeTaints }}"
          maxPods: {{ maxPods }}
          nodeName: "{{ nodeName }}"
          workloadRuntime: "{{ workloadRuntime }}"
          artifactStreamingProfile:
            enabled: {{ enabled }}
        mode: "{{ mode }}"
        security:
          enableVTPM: {{ enableVTPM }}
          enableSecureBoot: {{ enableSecureBoot }}
          sshAccess: "{{ sshAccess }}"
          enableEncryptionAtHost: {{ enableEncryptionAtHost }}
        priority: "{{ priority }}"
        evictionPolicy: "{{ evictionPolicy }}"
        billing:
          spotMaxPrice: {{ spotMaxPrice }}
        nodeImageVersion: "{{ nodeImageVersion }}"
        provisioningState: "{{ provisioningState }}"
        tags: "{{ tags }}"
        eTag: "{{ eTag }}"
        status:
          provisioningError:
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
          creationTimestamp: "{{ creationTimestamp }}"
          driftAction: "{{ driftAction }}"
          driftReason: "{{ driftReason }}"
          vmState: "{{ vmState }}"
        localDNSProfile:
          mode: "{{ mode }}"
          state: "{{ state }}"
          vnetDNSOverrides: "{{ vnetDNSOverrides }}"
          kubeDNSOverrides: "{{ kubeDNSOverrides }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The Availability zone in which machine is located.
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

Creates or updates a machine in the specified agent pool.

```sql
REPLACE azure.container_service.machines
SET 
properties = '{{ properties }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND agent_pool_name = '{{ agent_pool_name }}' --required
AND machine_name = '{{ machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type,
zones;
```
</TabItem>
</Tabs>
