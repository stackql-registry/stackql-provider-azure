--- 
title: provisioned_cluster_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_cluster_instances
  - hybrid_container_service
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

Creates, updates, deletes, gets or lists a <code>provisioned_cluster_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provisioned_cluster_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_container_service.provisioned_cluster_instances" /></td></tr>
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
    <td><CopyableCode code="agentPoolProfiles" /></td>
    <td><code>array</code></td>
    <td>The agent pool properties for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScalerProfile" /></td>
    <td><code>object</code></td>
    <td>Parameters to be applied to the cluster-autoscaler when auto scaling is enabled for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudProviderProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for the underlying cloud infrastructure provider for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVMAccessProfile" /></td>
    <td><code>object</code></td>
    <td>The SSH restricted access profile for the VMs in the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="controlPlane" /></td>
    <td><code>object</code></td>
    <td>The profile for control plane of the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended location pointing to the underlying infrastructure.</td>
</tr>
<tr>
    <td><CopyableCode code="kubernetesVersion" /></td>
    <td><code>string</code></td>
    <td>The version of Kubernetes in use by the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProfile" /></td>
    <td><code>object</code></td>
    <td>The license profile of the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="linuxProfile" /></td>
    <td><code>object</code></td>
    <td>The profile for Linux VMs in the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The network configuration profile for the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the latest long running operation for the provisioned cluster. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Creating", "Deleting", "Updating", "Upgrading", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The observed status of the provisioned cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage configuration profile for the provisioned cluster.</td>
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
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Gets the provisioned cluster instance. Gets the provisioned cluster instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Creates or updates the provisioned cluster instance. Creates or updates the provisioned cluster instance.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Creates or updates the provisioned cluster instance. Creates or updates the provisioned cluster instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Deletes the provisioned cluster instance. Deletes the provisioned cluster instance.</td>
</tr>
<tr>
    <td><a href="#list_user_kubeconfig"><CopyableCode code="list_user_kubeconfig" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Lists the user credentials of the provisioned cluster (can only be used within private network). Lists the user credentials of the provisioned cluster (can only be used within private network).</td>
</tr>
<tr>
    <td><a href="#list_admin_kubeconfig"><CopyableCode code="list_admin_kubeconfig" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Lists the admin credentials of the provisioned cluster (can only be used within private network). Lists the admin credentials of the provisioned cluster (can only be used within private network).</td>
</tr>
<tr>
    <td><a href="#get_upgrade_profile"><CopyableCode code="get_upgrade_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Gets the upgrade profile of a provisioned cluster. Gets the upgrade profile of a provisioned cluster.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-connected_cluster_resource_uri"><code>connected_cluster_resource_uri</code></a></td>
    <td></td>
    <td>Lists the ProvisionedClusterInstance resource associated with the ConnectedCluster. Lists the ProvisionedClusterInstance resource associated with the ConnectedCluster.</td>
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
<tr id="parameter-connected_cluster_resource_uri">
    <td><CopyableCode code="connected_cluster_resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource Manager identifier of the connected cluster resource. Required.</td>
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

Gets the provisioned cluster instance. Gets the provisioned cluster instance.

```sql
SELECT
id,
name,
agentPoolProfiles,
autoScalerProfile,
cloudProviderProfile,
clusterVMAccessProfile,
controlPlane,
extendedLocation,
kubernetesVersion,
licenseProfile,
linuxProfile,
networkProfile,
provisioningState,
status,
storageProfile,
systemData,
type
FROM azure.hybrid_container_service.provisioned_cluster_instances
WHERE connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' -- required
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

Creates or updates the provisioned cluster instance. Creates or updates the provisioned cluster instance.

```sql
INSERT INTO azure.hybrid_container_service.provisioned_cluster_instances (
properties,
extendedLocation,
connected_cluster_resource_uri
)
SELECT 
'{{ properties }}',
'{{ extendedLocation }}',
'{{ connected_cluster_resource_uri }}'
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
- name: provisioned_cluster_instances
  props:
    - name: connected_cluster_resource_uri
      value: "{{ connected_cluster_resource_uri }}"
      description: Required parameter for the provisioned_cluster_instances resource.
    - name: properties
      description: |
        Properties of the provisioned cluster.
      value:
        linuxProfile:
          ssh:
            publicKeys:
              - keyData: "{{ keyData }}"
        controlPlane:
          count: {{ count }}
          vmSize: "{{ vmSize }}"
          controlPlaneEndpoint:
            hostIP: "{{ hostIP }}"
        kubernetesVersion: "{{ kubernetesVersion }}"
        networkProfile:
          loadBalancerProfile:
            count: {{ count }}
          networkPolicy: "{{ networkPolicy }}"
          podCidr: "{{ podCidr }}"
        storageProfile:
          smbCsiDriver:
            enabled: {{ enabled }}
          nfsCsiDriver:
            enabled: {{ enabled }}
        clusterVMAccessProfile:
          authorizedIPRanges: "{{ authorizedIPRanges }}"
        agentPoolProfiles:
          - osType: "{{ osType }}"
            osSKU: "{{ osSKU }}"
            nodeLabels: "{{ nodeLabels }}"
            nodeTaints: "{{ nodeTaints }}"
            maxCount: {{ maxCount }}
            minCount: {{ minCount }}
            enableAutoScaling: {{ enableAutoScaling }}
            maxPods: {{ maxPods }}
            count: {{ count }}
            vmSize: "{{ vmSize }}"
            kubernetesVersion: "{{ kubernetesVersion }}"
            name: "{{ name }}"
        cloudProviderProfile:
          infraNetworkProfile:
            vnetSubnetIds:
              - "{{ vnetSubnetIds }}"
        provisioningState: "{{ provisioningState }}"
        status:
          controlPlaneStatus:
            - name: "{{ name }}"
              phase: "{{ phase }}"
              ready: {{ ready }}
              errorMessage: "{{ errorMessage }}"
          currentState: "{{ currentState }}"
          errorMessage: "{{ errorMessage }}"
        licenseProfile:
          azureHybridBenefit: "{{ azureHybridBenefit }}"
        autoScalerProfile:
          balance-similar-node-groups: "{{ balance-similar-node-groups }}"
          expander: "{{ expander }}"
          max-empty-bulk-delete: "{{ max-empty-bulk-delete }}"
          max-graceful-termination-sec: "{{ max-graceful-termination-sec }}"
          max-node-provision-time: "{{ max-node-provision-time }}"
          max-total-unready-percentage: "{{ max-total-unready-percentage }}"
          new-pod-scale-up-delay: "{{ new-pod-scale-up-delay }}"
          ok-total-unready-count: "{{ ok-total-unready-count }}"
          scan-interval: "{{ scan-interval }}"
          scale-down-delay-after-add: "{{ scale-down-delay-after-add }}"
          scale-down-delay-after-delete: "{{ scale-down-delay-after-delete }}"
          scale-down-delay-after-failure: "{{ scale-down-delay-after-failure }}"
          scale-down-unneeded-time: "{{ scale-down-unneeded-time }}"
          scale-down-unready-time: "{{ scale-down-unready-time }}"
          scale-down-utilization-threshold: "{{ scale-down-utilization-threshold }}"
          skip-nodes-with-local-storage: "{{ skip-nodes-with-local-storage }}"
          skip-nodes-with-system-pods: "{{ skip-nodes-with-system-pods }}"
    - name: extendedLocation
      description: |
        Extended location pointing to the underlying infrastructure.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
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

Creates or updates the provisioned cluster instance. Creates or updates the provisioned cluster instance.

```sql
REPLACE azure.hybrid_container_service.provisioned_cluster_instances
SET 
properties = '{{ properties }}',
extendedLocation = '{{ extendedLocation }}'
WHERE 
connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' --required
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

Deletes the provisioned cluster instance. Deletes the provisioned cluster instance.

```sql
DELETE FROM azure.hybrid_container_service.provisioned_cluster_instances
WHERE connected_cluster_resource_uri = '{{ connected_cluster_resource_uri }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_user_kubeconfig"
    values={[
        { label: 'list_user_kubeconfig', value: 'list_user_kubeconfig' },
        { label: 'list_admin_kubeconfig', value: 'list_admin_kubeconfig' },
        { label: 'get_upgrade_profile', value: 'get_upgrade_profile' },
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_user_kubeconfig">

Lists the user credentials of the provisioned cluster (can only be used within private network). Lists the user credentials of the provisioned cluster (can only be used within private network).

```sql
EXEC azure.hybrid_container_service.provisioned_cluster_instances.list_user_kubeconfig 
@connected_cluster_resource_uri='{{ connected_cluster_resource_uri }}' --required
;
```
</TabItem>
<TabItem value="list_admin_kubeconfig">

Lists the admin credentials of the provisioned cluster (can only be used within private network). Lists the admin credentials of the provisioned cluster (can only be used within private network).

```sql
EXEC azure.hybrid_container_service.provisioned_cluster_instances.list_admin_kubeconfig 
@connected_cluster_resource_uri='{{ connected_cluster_resource_uri }}' --required
;
```
</TabItem>
<TabItem value="get_upgrade_profile">

Gets the upgrade profile of a provisioned cluster. Gets the upgrade profile of a provisioned cluster.

```sql
EXEC azure.hybrid_container_service.provisioned_cluster_instances.get_upgrade_profile 
@connected_cluster_resource_uri='{{ connected_cluster_resource_uri }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Lists the ProvisionedClusterInstance resource associated with the ConnectedCluster. Lists the ProvisionedClusterInstance resource associated with the ConnectedCluster.

```sql
EXEC azure.hybrid_container_service.provisioned_cluster_instances.list_raw 
@connected_cluster_resource_uri='{{ connected_cluster_resource_uri }}' --required
;
```
</TabItem>
</Tabs>
