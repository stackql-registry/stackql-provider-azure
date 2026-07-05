--- 
title: replication_protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protected_items
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

Creates, updates, deletes, gets or lists a <code>replication_protected_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_protected_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_protected_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
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
    <td><CopyableCode code="activeLocation" /></td>
    <td><code>string</code></td>
    <td>The Current active location of the PE.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="eventCorrelationId" /></td>
    <td><code>string</code></td>
    <td>The correlation Id for events associated with this protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated failover health for the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverRecoveryPointId" /></td>
    <td><code>string</code></td>
    <td>The recovery point ARM Id to which the Vm was failed over.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The ID of Policy governing this PE.</td>
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
    <td><CopyableCode code="protectableItemId" /></td>
    <td><code>string</code></td>
    <td>The protected item ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemType" /></td>
    <td><code>string</code></td>
    <td>The type of protected item type.</td>
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
    <td>The Replication provider custom settings.</td>
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
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="switchProviderState" /></td>
    <td><code>string</code></td>
    <td>The switch provider state.</td>
</tr>
<tr>
    <td><CopyableCode code="switchProviderStateDescription" /></td>
    <td><code>string</code></td>
    <td>The switch provider state description.</td>
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
    <td>The Current active location of the PE.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="eventCorrelationId" /></td>
    <td><code>string</code></td>
    <td>The correlation Id for events associated with this protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated failover health for the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverRecoveryPointId" /></td>
    <td><code>string</code></td>
    <td>The recovery point ARM Id to which the Vm was failed over.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The ID of Policy governing this PE.</td>
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
    <td><CopyableCode code="protectableItemId" /></td>
    <td><code>string</code></td>
    <td>The protected item ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemType" /></td>
    <td><code>string</code></td>
    <td>The type of protected item type.</td>
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
    <td>The Replication provider custom settings.</td>
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
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="switchProviderState" /></td>
    <td><code>string</code></td>
    <td>The switch provider state.</td>
</tr>
<tr>
    <td><CopyableCode code="switchProviderStateDescription" /></td>
    <td><code>string</code></td>
    <td>The switch provider state description.</td>
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
    <td>The Current active location of the PE.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedOperations" /></td>
    <td><code>array</code></td>
    <td>The allowed operations on the Replication protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="currentScenario" /></td>
    <td><code>object</code></td>
    <td>The current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="eventCorrelationId" /></td>
    <td><code>string</code></td>
    <td>The correlation Id for events associated with this protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated failover health for the VM.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverRecoveryPointId" /></td>
    <td><code>string</code></td>
    <td>The recovery point ARM Id to which the Vm was failed over.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>The name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>List of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Last successful failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="policyFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The name of Policy governing this PE.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The ID of Policy governing this PE.</td>
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
    <td><CopyableCode code="protectableItemId" /></td>
    <td><code>string</code></td>
    <td>The protected item ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemType" /></td>
    <td><code>string</code></td>
    <td>The type of protected item type.</td>
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
    <td>The Replication provider custom settings.</td>
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
    <td><CopyableCode code="recoveryServicesProviderId" /></td>
    <td><code>string</code></td>
    <td>The recovery provider ARM Id.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>The consolidated protection health for the VM taking any issues with SRS as well as all the replication units associated with the VM's replication group into account. This is a string representation of the ProtectionHealth enumeration.</td>
</tr>
<tr>
    <td><CopyableCode code="switchProviderState" /></td>
    <td><code>string</code></td>
    <td>The switch provider state.</td>
</tr>
<tr>
    <td><CopyableCode code="switchProviderStateDescription" /></td>
    <td><code>string</code></td>
    <td>The switch provider state description.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a Replication protected item. Gets the details of an ASR replication protected item.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_protection_containers"><CopyableCode code="list_by_replication_protection_containers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of Replication protected items. Gets the list of ASR replication protected items in the protection container.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-skipToken"><code>skipToken</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the list of replication protected items. Gets the list of ASR replication protected items in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enables protection. The operation to create an ASR replication protected item (Enable replication).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the replication protected item settings. The operation to update the recovery settings of an ASR replication protected item.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables protection. The operation to disable replication on a replication protected item. This will also remove the item.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Purges protection. The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item.</td>
</tr>
<tr>
    <td><a href="#add_disks"><CopyableCode code="add_disks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add disk(s) for protection. Operation to add disks(s) to the replication protected item.</td>
</tr>
<tr>
    <td><a href="#apply_recovery_point"><CopyableCode code="apply_recovery_point" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Change or apply recovery point. The operation to change the recovery point of a failed over replication protected item.</td>
</tr>
<tr>
    <td><a href="#failover_cancel"><CopyableCode code="failover_cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute cancel failover. Operation to cancel the failover of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#failover_commit"><CopyableCode code="failover_commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute commit failover. Operation to commit the failover of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#planned_failover"><CopyableCode code="planned_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute planned failover. Operation to initiate a planned failover of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#remove_disks"><CopyableCode code="remove_disks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes disk(s). Operation to remove disk(s) from the replication protected item.</td>
</tr>
<tr>
    <td><a href="#repair_replication"><CopyableCode code="repair_replication" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resynchronize or repair replication. The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization.</td>
</tr>
<tr>
    <td><a href="#reprotect"><CopyableCode code="reprotect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute Reverse Replication\Reprotect. Operation to reprotect or reverse replicate a failed over replication protected item.</td>
</tr>
<tr>
    <td><a href="#resolve_health_errors"><CopyableCode code="resolve_health_errors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resolve health errors. Operation to resolve health issues of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#switch_provider"><CopyableCode code="switch_provider" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Execute switch provider. Operation to initiate a switch provider of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#test_failover"><CopyableCode code="test_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute test failover. Operation to perform a test failover of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#test_failover_cleanup"><CopyableCode code="test_failover_cleanup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute test failover cleanup. Operation to clean up the test failover of a replication protected item.</td>
</tr>
<tr>
    <td><a href="#unplanned_failover"><CopyableCode code="unplanned_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Execute unplanned failover. Operation to initiate a failover of the replication protected item.</td>
</tr>
<tr>
    <td><a href="#update_appliance"><CopyableCode code="update_appliance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Updates appliance for replication protected Item. The operation to update appliance of an ASR replication protected item.</td>
</tr>
<tr>
    <td><a href="#update_mobility_service"><CopyableCode code="update_mobility_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the mobility service on a protected item. The operation to update(push update) the installed mobility service software on a replication protected item to the latest available version.</td>
</tr>
<tr>
    <td><a href="#reinstall_mobility_service"><CopyableCode code="reinstall_mobility_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-protection_container_name"><code>protection_container_name</code></a>, <a href="#parameter-replicated_protected_item_name"><code>replicated_protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reinstall the mobility service on a protected item. The operation to reinstall the installed mobility service software on a replication protected item to the latest available version.</td>
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
<tr id="parameter-protection_container_name">
    <td><CopyableCode code="protection_container_name" /></td>
    <td><code>string</code></td>
    <td>Protection container name. Required.</td>
</tr>
<tr id="parameter-replicated_protected_item_name">
    <td><CopyableCode code="replicated_protected_item_name" /></td>
    <td><code>string</code></td>
    <td>The name of the protected item on which the agent is to be updated. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_protection_containers', value: 'list_by_replication_protection_containers' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details of a Replication protected item. Gets the details of an ASR replication protected item.

```sql
SELECT
id,
name,
activeLocation,
allowedOperations,
currentScenario,
eventCorrelationId,
failoverHealth,
failoverRecoveryPointId,
friendlyName,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
location,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectableItemId,
protectedItemType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
recoveryServicesProviderId,
replicationHealth,
switchProviderState,
switchProviderStateDescription,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protected_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND replicated_protected_item_name = '{{ replicated_protected_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_protection_containers">

Gets the list of Replication protected items. Gets the list of ASR replication protected items in the protection container.

```sql
SELECT
id,
name,
activeLocation,
allowedOperations,
currentScenario,
eventCorrelationId,
failoverHealth,
failoverRecoveryPointId,
friendlyName,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
location,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectableItemId,
protectedItemType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
recoveryServicesProviderId,
replicationHealth,
switchProviderState,
switchProviderStateDescription,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protected_items
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND protection_container_name = '{{ protection_container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of replication protected items. Gets the list of ASR replication protected items in the vault.

```sql
SELECT
id,
name,
activeLocation,
allowedOperations,
currentScenario,
eventCorrelationId,
failoverHealth,
failoverRecoveryPointId,
friendlyName,
healthErrors,
lastSuccessfulFailoverTime,
lastSuccessfulTestFailoverTime,
location,
policyFriendlyName,
policyId,
primaryFabricFriendlyName,
primaryFabricProvider,
primaryProtectionContainerFriendlyName,
protectableItemId,
protectedItemType,
protectionState,
protectionStateDescription,
providerSpecificDetails,
recoveryContainerId,
recoveryFabricFriendlyName,
recoveryFabricId,
recoveryProtectionContainerFriendlyName,
recoveryServicesProviderId,
replicationHealth,
switchProviderState,
switchProviderStateDescription,
systemData,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicessiterecovery.replication_protected_items
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

Enables protection. The operation to create an ASR replication protected item (Enable replication).

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_protected_items (
properties,
resource_group_name,
resource_name,
fabric_name,
protection_container_name,
replicated_protected_item_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ protection_container_name }}',
'{{ replicated_protected_item_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_protected_items
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_protected_items resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_protected_items resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_protected_items resource.
    - name: protection_container_name
      value: "{{ protection_container_name }}"
      description: Required parameter for the replication_protected_items resource.
    - name: replicated_protected_item_name
      value: "{{ replicated_protected_item_name }}"
      description: Required parameter for the replication_protected_items resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_protected_items resource.
    - name: properties
      description: |
        Enable protection input properties.
      value:
        policyId: "{{ policyId }}"
        protectableItemId: "{{ protectableItemId }}"
        providerSpecificDetails:
          instanceType: "{{ instanceType }}"
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

Updates the replication protected item settings. The operation to update the recovery settings of an ASR replication protected item.

```sql
UPDATE azure.recoveryservicessiterecovery.replication_protected_items
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND replicated_protected_item_name = '{{ replicated_protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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
        { label: 'delete', value: 'delete' },
        { label: 'purge', value: 'purge' }
    ]}
>
<TabItem value="delete">

Disables protection. The operation to disable replication on a replication protected item. This will also remove the item.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_protected_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND replicated_protected_item_name = '{{ replicated_protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="purge">

Purges protection. The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_protected_items
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND protection_container_name = '{{ protection_container_name }}' --required
AND replicated_protected_item_name = '{{ replicated_protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_disks"
    values={[
        { label: 'add_disks', value: 'add_disks' },
        { label: 'apply_recovery_point', value: 'apply_recovery_point' },
        { label: 'failover_cancel', value: 'failover_cancel' },
        { label: 'failover_commit', value: 'failover_commit' },
        { label: 'planned_failover', value: 'planned_failover' },
        { label: 'remove_disks', value: 'remove_disks' },
        { label: 'repair_replication', value: 'repair_replication' },
        { label: 'reprotect', value: 'reprotect' },
        { label: 'resolve_health_errors', value: 'resolve_health_errors' },
        { label: 'switch_provider', value: 'switch_provider' },
        { label: 'test_failover', value: 'test_failover' },
        { label: 'test_failover_cleanup', value: 'test_failover_cleanup' },
        { label: 'unplanned_failover', value: 'unplanned_failover' },
        { label: 'update_appliance', value: 'update_appliance' },
        { label: 'update_mobility_service', value: 'update_mobility_service' },
        { label: 'reinstall_mobility_service', value: 'reinstall_mobility_service' }
    ]}
>
<TabItem value="add_disks">

Add disk(s) for protection. Operation to add disks(s) to the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.add_disks 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="apply_recovery_point">

Change or apply recovery point. The operation to change the recovery point of a failed over replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.apply_recovery_point 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="failover_cancel">

Execute cancel failover. Operation to cancel the failover of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.failover_cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="failover_commit">

Execute commit failover. Operation to commit the failover of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.failover_commit 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="planned_failover">

Execute planned failover. Operation to initiate a planned failover of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.planned_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="remove_disks">

Removes disk(s). Operation to remove disk(s) from the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.remove_disks 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="repair_replication">

Resynchronize or repair replication. The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.repair_replication 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reprotect">

Execute Reverse Replication\Reprotect. Operation to reprotect or reverse replicate a failed over replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.reprotect 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="resolve_health_errors">

Resolve health errors. Operation to resolve health issues of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.resolve_health_errors 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="switch_provider">

Execute switch provider. Operation to initiate a switch provider of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.switch_provider 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="test_failover">

Execute test failover. Operation to perform a test failover of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.test_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="test_failover_cleanup">

Execute test failover cleanup. Operation to clean up the test failover of a replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.test_failover_cleanup 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="unplanned_failover">

Execute unplanned failover. Operation to initiate a failover of the replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.unplanned_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_appliance">

Updates appliance for replication protected Item. The operation to update appliance of an ASR replication protected item.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.update_appliance 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_mobility_service">

Update the mobility service on a protected item. The operation to update(push update) the installed mobility service software on a replication protected item to the latest available version.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.update_mobility_service 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="reinstall_mobility_service">

Reinstall the mobility service on a protected item. The operation to reinstall the installed mobility service software on a replication protected item to the latest available version.

```sql
EXEC azure.recoveryservicessiterecovery.replication_protected_items.reinstall_mobility_service 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@protection_container_name='{{ protection_container_name }}' --required, 
@replicated_protected_item_name='{{ replicated_protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
