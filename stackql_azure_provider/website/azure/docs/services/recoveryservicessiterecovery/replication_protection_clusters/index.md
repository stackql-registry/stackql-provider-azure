--- 
title: replication_protection_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_clusters
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_protection_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_protection_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_protection_clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_operation_results"
    values={[
        { label: 'get_operation_results', value: 'get_operation_results' },
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_operation_results">

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
    <td><CopyableCode code="activeLocation" /></td>
    <td><code>string</code></td>
    <td>The Current active location of the Protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentClusterId" /></td>
    <td><code>string</code></td>
    <td>The Agent cluster Id.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="areAllClusterNodesRegistered" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether all nodes of the cluster are registered or not.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterFqdn" /></td>
    <td><code>string</code></td>
    <td>The cluster FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNodeFqdns" /></td>
    <td><code>array</code></td>
    <td>The List of cluster Node FQDNs.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProtectedItemIds" /></td>
    <td><code>array</code></td>
    <td>The List of Protected Item Id's.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterRegisteredNodes" /></td>
    <td><code>array</code></td>
    <td>The registered node details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The Policy Id.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricProvider" /></td>
    <td><code>string</code></td>
    <td>The fabric provider of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of primary protection container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionClusterType" /></td>
    <td><code>string</code></td>
    <td>The type of protection cluster type.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>The protection status.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStateDescription" /></td>
    <td><code>string</code></td>
    <td>The protection state description.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The Replication cluster provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryContainerId" /></td>
    <td><code>string</code></td>
    <td>The recovery container Id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricId" /></td>
    <td><code>string</code></td>
    <td>The Arm Id of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of recovery container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedDiskProperties" /></td>
    <td><code>object</code></td>
    <td>The shared disk properties.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverState" /></td>
    <td><code>string</code></td>
    <td>The Test failover state.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverStateDescription" /></td>
    <td><code>string</code></td>
    <td>The Test failover state description.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="activeLocation" /></td>
    <td><code>string</code></td>
    <td>The Current active location of the Protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentClusterId" /></td>
    <td><code>string</code></td>
    <td>The Agent cluster Id.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="areAllClusterNodesRegistered" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether all nodes of the cluster are registered or not.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterFqdn" /></td>
    <td><code>string</code></td>
    <td>The cluster FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNodeFqdns" /></td>
    <td><code>array</code></td>
    <td>The List of cluster Node FQDNs.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProtectedItemIds" /></td>
    <td><code>array</code></td>
    <td>The List of Protected Item Id's.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterRegisteredNodes" /></td>
    <td><code>array</code></td>
    <td>The registered node details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The Policy Id.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricProvider" /></td>
    <td><code>string</code></td>
    <td>The fabric provider of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of primary protection container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionClusterType" /></td>
    <td><code>string</code></td>
    <td>The type of protection cluster type.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>The protection status.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStateDescription" /></td>
    <td><code>string</code></td>
    <td>The protection state description.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The Replication cluster provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryContainerId" /></td>
    <td><code>string</code></td>
    <td>The recovery container Id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricId" /></td>
    <td><code>string</code></td>
    <td>The Arm Id of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of recovery container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedDiskProperties" /></td>
    <td><code>object</code></td>
    <td>The shared disk properties.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverState" /></td>
    <td><code>string</code></td>
    <td>The Test failover state.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverStateDescription" /></td>
    <td><code>string</code></td>
    <td>The Test failover state description.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_replication_protection_containers">

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
    <td><CopyableCode code="activeLocation" /></td>
    <td><code>string</code></td>
    <td>The Current active location of the Protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentClusterId" /></td>
    <td><code>string</code></td>
    <td>The Agent cluster Id.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="areAllClusterNodesRegistered" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether all nodes of the cluster are registered or not.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterFqdn" /></td>
    <td><code>string</code></td>
    <td>The cluster FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNodeFqdns" /></td>
    <td><code>array</code></td>
    <td>The List of cluster Node FQDNs.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProtectedItemIds" /></td>
    <td><code>array</code></td>
    <td>The List of Protected Item Id's.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterRegisteredNodes" /></td>
    <td><code>array</code></td>
    <td>The registered node details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The Policy Id.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricProvider" /></td>
    <td><code>string</code></td>
    <td>The fabric provider of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of primary protection container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionClusterType" /></td>
    <td><code>string</code></td>
    <td>The type of protection cluster type.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>The protection status.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStateDescription" /></td>
    <td><code>string</code></td>
    <td>The protection state description.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The Replication cluster provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryContainerId" /></td>
    <td><code>string</code></td>
    <td>The recovery container Id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricId" /></td>
    <td><code>string</code></td>
    <td>The Arm Id of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of recovery container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedDiskProperties" /></td>
    <td><code>object</code></td>
    <td>The shared disk properties.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverState" /></td>
    <td><code>string</code></td>
    <td>The Test failover state.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverStateDescription" /></td>
    <td><code>string</code></td>
    <td>The Test failover state description.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="activeLocation" /></td>
    <td><code>string</code></td>
    <td>The Current active location of the Protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="agentClusterId" /></td>
    <td><code>string</code></td>
    <td>The Agent cluster Id.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protection cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="areAllClusterNodesRegistered" /></td>
    <td><code>boolean</code></td>
    <td>A value indicating whether all nodes of the cluster are registered or not.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterFqdn" /></td>
    <td><code>string</code></td>
    <td>The cluster FQDN.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterNodeFqdns" /></td>
    <td><code>array</code></td>
    <td>The List of cluster Node FQDNs.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProtectedItemIds" /></td>
    <td><code>array</code></td>
    <td>The List of Protected Item Id's.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterRegisteredNodes" /></td>
    <td><code>array</code></td>
    <td>The registered node details.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The Policy Id.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryFabricProvider" /></td>
    <td><code>string</code></td>
    <td>The fabric provider of the primary fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of primary protection container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionClusterType" /></td>
    <td><code>string</code></td>
    <td>The type of protection cluster type.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>The protection status.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStateDescription" /></td>
    <td><code>string</code></td>
    <td>The protection state description.</td>
</tr>
<tr>
    <td><CopyableCode code="providerSpecificDetails" /></td>
    <td><code>object</code></td>
    <td>The Replication cluster provider custom settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryContainerId" /></td>
    <td><code>string</code></td>
    <td>The recovery container Id.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryFabricId" /></td>
    <td><code>string</code></td>
    <td>The Arm Id of recovery fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="recoveryProtectionContainerFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of recovery container friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="sharedDiskProperties" /></td>
    <td><code>object</code></td>
    <td>The shared disk properties.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverState" /></td>
    <td><code>string</code></td>
    <td>The Test failover state.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverStateDescription" /></td>
    <td><code>string</code></td>
    <td>The Test failover state description.</td>
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
    <td><a href="#get_operation_results"><CopyableCode code="get_operation_results" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Tracks the Replication protection cluster async operation. Track the results of an asynchronous operation on the replication protection cluster.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a Replication protection cluster. Gets the details of an ASR replication protection cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_protection_containers"><CopyableCode code="list_by_replication_protection_containers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of Replication protection clusters in fabric, container. Gets the list of ASR replication protected clusters in the protection container.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipToken"><code>skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the list of Replication protection clusters in vault. Gets the list of ASR replication protected clusters in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Replication protection Cluster. The operation to create an ASR replication protection cluster item.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Purge the replication protection cluster. The operation to purge the replication protection cluster. This operation will force delete the replication protection cluster. Use the remove operation on replication protection cluster to perform a clean disable replication protection cluster.</td>
</tr>
<tr>
    <td><a href="#apply_recovery_point"><CopyableCode code="apply_recovery_point" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute the change recovery point operation for cluster. Operation to apply a new cluster recovery point on the Protection cluster.</td>
</tr>
<tr>
    <td><a href="#failover_commit"><CopyableCode code="failover_commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute commit failover for cluster. Operation to initiate commit failover of the replication protection cluster.</td>
</tr>
<tr>
    <td><a href="#repair_replication"><CopyableCode code="repair_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resynchronize or repair replication of protection cluster. The operation to repair replication protection cluster.</td>
</tr>
<tr>
    <td><a href="#test_failover"><CopyableCode code="test_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute test failover for cluster. Operation to initiate a failover of the replication protection cluster.</td>
</tr>
<tr>
    <td><a href="#test_failover_cleanup"><CopyableCode code="test_failover_cleanup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute test failover cleanup for cluster. Operation to clean up the test failover of a replication protected cluster.</td>
</tr>
<tr>
    <td><a href="#unplanned_failover"><CopyableCode code="unplanned_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replication_protection_cluster_name"><code>replication_protection_cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute unplanned cluster failover. Operation to initiate a failover of the replication protection cluster.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>job id to track. Required.</td>
</tr>
<tr id="parameter-protection_container_name">
    <td><CopyableCode code="protection_container_name" /></td>
    <td><code>string</code></td>
    <td>Protection container name. Required.</td>
</tr>
<tr id="parameter-replication_protection_cluster_name">
    <td><CopyableCode code="replication_protection_cluster_name" /></td>
    <td><code>string</code></td>
    <td>Replication protection cluster name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery services vault. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>The pagination token. Possible values: "FabricId" or "FabricId_CloudId" or null. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_operation_results"
    values={[
        { label: 'get_operation_results', value: 'get_operation_results' },
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_operation_results">

Tracks the Replication protection cluster async operation. Track the results of an asynchronous operation on the replication protection cluster.

```sql
SELECT
id,
name,
activeLocation,
agentClusterId,
allowedOperations,
areAllClusterNodesRegistered,
clusterFqdn,
clusterNodeFqdns,
clusterProtectedItemIds,
clusterRegisteredNodes,
currentScenario,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectionClusterType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
provisioningState,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
replicationHealth,
sharedDiskProperties,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protection_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND replication_protection_cluster_name = '{{ replication_protection_cluster_name }}' -- required
AND job_id = '{{ job_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the details of a Replication protection cluster. Gets the details of an ASR replication protection cluster.

```sql
SELECT
id,
name,
activeLocation,
agentClusterId,
allowedOperations,
areAllClusterNodesRegistered,
clusterFqdn,
clusterNodeFqdns,
clusterProtectedItemIds,
clusterRegisteredNodes,
currentScenario,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectionClusterType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
provisioningState,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
replicationHealth,
sharedDiskProperties,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protection_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND replication_protection_cluster_name = '{{ replication_protection_cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_protection_containers">

Gets the list of Replication protection clusters in fabric, container. Gets the list of ASR replication protected clusters in the protection container.

```sql
SELECT
id,
name,
activeLocation,
agentClusterId,
allowedOperations,
areAllClusterNodesRegistered,
clusterFqdn,
clusterNodeFqdns,
clusterProtectedItemIds,
clusterRegisteredNodes,
currentScenario,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectionClusterType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
provisioningState,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
replicationHealth,
sharedDiskProperties,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protection_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of Replication protection clusters in vault. Gets the list of ASR replication protected clusters in the vault.

```sql
SELECT
id,
name,
activeLocation,
agentClusterId,
allowedOperations,
areAllClusterNodesRegistered,
clusterFqdn,
clusterNodeFqdns,
clusterProtectedItemIds,
clusterRegisteredNodes,
currentScenario,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectionClusterType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
provisioningState,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
replicationHealth,
sharedDiskProperties,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protection_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND skipToken = '{{ skipToken }}'
AND $filter = '{{ $filter }}'
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

Create Replication protection Cluster. The operation to create an ASR replication protection cluster item.

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_protection_clusters (
properties,
resource_group_name,
resource_name,
fabric_name,
protection_container_name,
replication_protection_cluster_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ protection_container_name }}',
'{{ replication_protection_cluster_name }}',
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
- name: replication_protection_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_protection_clusters resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_protection_clusters resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_protection_clusters resource.
    - name: protection_container_name
      value: "{{ protection_container_name }}"
      description: Required parameter for the replication_protection_clusters resource.
    - name: replication_protection_cluster_name
      value: "{{ replication_protection_cluster_name }}"
      description: Required parameter for the replication_protection_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_protection_clusters resource.
    - name: properties
      description: |
        The custom data.
      value:
        protectionClusterType: "{{ protectionClusterType }}"
        primaryFabricFriendlyName: "{{ primaryFabricFriendlyName }}"
        primaryFabricProvider: "{{ primaryFabricProvider }}"
        recoveryFabricFriendlyName: "{{ recoveryFabricFriendlyName }}"
        recoveryFabricId: "{{ recoveryFabricId }}"
        primaryProtectionContainerFriendlyName: "{{ primaryProtectionContainerFriendlyName }}"
        recoveryProtectionContainerFriendlyName: "{{ recoveryProtectionContainerFriendlyName }}"
        protectionState: "{{ protectionState }}"
        protectionStateDescription: "{{ protectionStateDescription }}"
        activeLocation: "{{ activeLocation }}"
        testFailoverState: "{{ testFailoverState }}"
        testFailoverStateDescription: "{{ testFailoverStateDescription }}"
        allowedOperations:
          - "{{ allowedOperations }}"
        replicationHealth: "{{ replicationHealth }}"
        healthErrors:
          - innerHealthErrors: "{{ innerHealthErrors }}"
            errorSource: "{{ errorSource }}"
            errorType: "{{ errorType }}"
            errorLevel: "{{ errorLevel }}"
            errorCategory: "{{ errorCategory }}"
            errorCode: "{{ errorCode }}"
            summaryMessage: "{{ summaryMessage }}"
            errorMessage: "{{ errorMessage }}"
            possibleCauses: "{{ possibleCauses }}"
            recommendedAction: "{{ recommendedAction }}"
            creationTimeUtc: "{{ creationTimeUtc }}"
            recoveryProviderErrorMessage: "{{ recoveryProviderErrorMessage }}"
            entityId: "{{ entityId }}"
            errorId: "{{ errorId }}"
            customerResolvability: "{{ customerResolvability }}"
        lastSuccessfulFailoverTime: "{{ lastSuccessfulFailoverTime }}"
        lastSuccessfulTestFailoverTime: "{{ lastSuccessfulTestFailoverTime }}"
        policyFriendlyName: "{{ policyFriendlyName }}"
        currentScenario:
          scenarioName: "{{ scenarioName }}"
          jobId: "{{ jobId }}"
          startTime: "{{ startTime }}"
        recoveryContainerId: "{{ recoveryContainerId }}"
        agentClusterId: "{{ agentClusterId }}"
        clusterFqdn: "{{ clusterFqdn }}"
        clusterNodeFqdns:
          - "{{ clusterNodeFqdns }}"
        clusterProtectedItemIds:
          - "{{ clusterProtectedItemIds }}"
        provisioningState: "{{ provisioningState }}"
        areAllClusterNodesRegistered: {{ areAllClusterNodesRegistered }}
        clusterRegisteredNodes:
          - clusterNodeFqdn: "{{ clusterNodeFqdn }}"
            machineId: "{{ machineId }}"
            biosId: "{{ biosId }}"
            isSharedDiskVirtualNode: {{ isSharedDiskVirtualNode }}
        providerSpecificDetails:
          instanceType: "{{ instanceType }}"
        sharedDiskProperties:
          protectionState: "{{ protectionState }}"
          testFailoverState: "{{ testFailoverState }}"
          activeLocation: "{{ activeLocation }}"
          allowedOperations:
            - "{{ allowedOperations }}"
          replicationHealth: "{{ replicationHealth }}"
          healthErrors:
            - innerHealthErrors: "{{ innerHealthErrors }}"
              errorSource: "{{ errorSource }}"
              errorType: "{{ errorType }}"
              errorLevel: "{{ errorLevel }}"
              errorCategory: "{{ errorCategory }}"
              errorCode: "{{ errorCode }}"
              summaryMessage: "{{ summaryMessage }}"
              errorMessage: "{{ errorMessage }}"
              possibleCauses: "{{ possibleCauses }}"
              recommendedAction: "{{ recommendedAction }}"
              creationTimeUtc: "{{ creationTimeUtc }}"
              recoveryProviderErrorMessage: "{{ recoveryProviderErrorMessage }}"
              entityId: "{{ entityId }}"
              errorId: "{{ errorId }}"
              customerResolvability: "{{ customerResolvability }}"
          currentScenario:
            scenarioName: "{{ scenarioName }}"
            jobId: "{{ jobId }}"
            startTime: "{{ startTime }}"
          sharedDiskProviderSpecificDetails:
            instanceType: "{{ instanceType }}"
        policyId: "{{ policyId }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="purge"
    values={[
        { label: 'purge', value: 'purge' }
    ]}
>
<TabItem value="purge">

Purge the replication protection cluster. The operation to purge the replication protection cluster. This operation will force delete the replication protection cluster. Use the remove operation on replication protection cluster to perform a clean disable replication protection cluster.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_protection_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND replication_protection_cluster_name = '{{ replication_protection_cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="apply_recovery_point"
    values={[
        { label: 'apply_recovery_point', value: 'apply_recovery_point' },
        { label: 'failover_commit', value: 'failover_commit' },
        { label: 'repair_replication', value: 'repair_replication' },
        { label: 'test_failover', value: 'test_failover' },
        { label: 'test_failover_cleanup', value: 'test_failover_cleanup' },
        { label: 'unplanned_failover', value: 'unplanned_failover' }
    ]}
>
<TabItem value="apply_recovery_point">

Execute the change recovery point operation for cluster. Operation to apply a new cluster recovery point on the Protection cluster.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_clusters.apply_recovery_point 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replication_protection_cluster_name='{{ replication_protection_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="failover_commit">

Execute commit failover for cluster. Operation to initiate commit failover of the replication protection cluster.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_clusters.failover_commit 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replication_protection_cluster_name='{{ replication_protection_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="repair_replication">

Resynchronize or repair replication of protection cluster. The operation to repair replication protection cluster.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_clusters.repair_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replication_protection_cluster_name='{{ replication_protection_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="test_failover">

Execute test failover for cluster. Operation to initiate a failover of the replication protection cluster.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_clusters.test_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replication_protection_cluster_name='{{ replication_protection_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="test_failover_cleanup">

Execute test failover cleanup for cluster. Operation to clean up the test failover of a replication protected cluster.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_clusters.test_failover_cleanup 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replication_protection_cluster_name='{{ replication_protection_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="unplanned_failover">

Execute unplanned cluster failover. Operation to initiate a failover of the replication protection cluster.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protection_clusters.unplanned_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replication_protection_cluster_name='{{ replication_protection_cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
