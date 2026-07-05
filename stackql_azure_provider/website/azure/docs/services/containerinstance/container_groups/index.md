--- 
title: container_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - container_groups
  - containerinstance
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

Creates, updates, deletes, gets or lists a <code>container_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerinstance.container_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="confidentialComputeProperties" /></td>
    <td><code>object</code></td>
    <td>The properties for confidential container group.</td>
</tr>
<tr>
    <td><CopyableCode code="containerGroupProfile" /></td>
    <td><code>object</code></td>
    <td>The reference container group profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers within the container group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>The diagnostic information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfig" /></td>
    <td><code>object</code></td>
    <td>The DNS config information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>extensions used by virtual kubelet.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the container group, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="identityAcls" /></td>
    <td><code>object</code></td>
    <td>The access control levels of the identities.</td>
</tr>
<tr>
    <td><CopyableCode code="imageRegistryCredentials" /></td>
    <td><code>array</code></td>
    <td>The image registry credentials by which the container group is created from.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The instance view of the container group. Only valid in response.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="isCreatedFromStandbyPool" /></td>
    <td><code>boolean</code></td>
    <td>The flag to determine whether the container group is created from standby pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the container group. This only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="secretReferences" /></td>
    <td><code>array</code></td>
    <td>The secret references that will be referenced within the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
</tr>
<tr>
    <td><CopyableCode code="standbyPoolProfile" /></td>
    <td><code>object</code></td>
    <td>The reference standby pool profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetIds" /></td>
    <td><code>array</code></td>
    <td>The subnet resource IDs for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The list of volumes that can be mounted by containers in this container group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="confidentialComputeProperties" /></td>
    <td><code>object</code></td>
    <td>The properties for confidential container group.</td>
</tr>
<tr>
    <td><CopyableCode code="containerGroupProfile" /></td>
    <td><code>object</code></td>
    <td>The reference container group profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers within the container group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>The diagnostic information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfig" /></td>
    <td><code>object</code></td>
    <td>The DNS config information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>extensions used by virtual kubelet.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the container group, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="identityAcls" /></td>
    <td><code>object</code></td>
    <td>The access control levels of the identities.</td>
</tr>
<tr>
    <td><CopyableCode code="imageRegistryCredentials" /></td>
    <td><code>array</code></td>
    <td>The image registry credentials by which the container group is created from.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The instance view of the container group. Only valid in response.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="isCreatedFromStandbyPool" /></td>
    <td><code>boolean</code></td>
    <td>The flag to determine whether the container group is created from standby pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the container group. This only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="secretReferences" /></td>
    <td><code>array</code></td>
    <td>The secret references that will be referenced within the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
</tr>
<tr>
    <td><CopyableCode code="standbyPoolProfile" /></td>
    <td><code>object</code></td>
    <td>The reference standby pool profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetIds" /></td>
    <td><code>array</code></td>
    <td>The subnet resource IDs for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The list of volumes that can be mounted by containers in this container group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="confidentialComputeProperties" /></td>
    <td><code>object</code></td>
    <td>The properties for confidential container group.</td>
</tr>
<tr>
    <td><CopyableCode code="containerGroupProfile" /></td>
    <td><code>object</code></td>
    <td>The reference container group profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers within the container group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>The diagnostic information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfig" /></td>
    <td><code>object</code></td>
    <td>The DNS config information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>extensions used by virtual kubelet.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the container group, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="identityAcls" /></td>
    <td><code>object</code></td>
    <td>The access control levels of the identities.</td>
</tr>
<tr>
    <td><CopyableCode code="imageRegistryCredentials" /></td>
    <td><code>array</code></td>
    <td>The image registry credentials by which the container group is created from.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The instance view of the container group. Only valid in response.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="isCreatedFromStandbyPool" /></td>
    <td><code>boolean</code></td>
    <td>The flag to determine whether the container group is created from standby pool.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the container group. This only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="secretReferences" /></td>
    <td><code>array</code></td>
    <td>The secret references that will be referenced within the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
</tr>
<tr>
    <td><CopyableCode code="standbyPoolProfile" /></td>
    <td><code>object</code></td>
    <td>The reference standby pool profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetIds" /></td>
    <td><code>array</code></td>
    <td>The subnet resource IDs for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The list of volumes that can be mounted by containers in this container group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of the specified container group. Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of container groups in the specified subscription and resource group. Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of container groups in the specified subscription. Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update container groups. Create or update container groups with specified configurations.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update container groups. Updates container group tags with specified values.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update container groups. Create or update container groups with specified configurations.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the specified container group. Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes.</td>
</tr>
<tr>
    <td><a href="#get_outbound_network_dependencies_endpoints"><CopyableCode code="get_outbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all network dependencies for container group. Gets all the network dependencies for this container group to allow complete control of network setting and configuration. For container groups, this will always be an empty list.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restarts all containers in a container group. Restarts all containers in a container group in place. If container image has updates, new image will be downloaded.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops all containers in a container group. Stops all containers in a container group. Compute resources will be deallocated and billing will stop.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_name"><code>container_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts all containers in a container group. Starts all containers in a container group. Compute resources will be allocated and billing will start.</td>
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
<tr id="parameter-container_group_name">
    <td><CopyableCode code="container_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the container group. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the properties of the specified container group. Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containerGroupProfile,
containers,
diagnostics,
dnsConfig,
encryptionProperties,
extensions,
identity,
identityAcls,
imageRegistryCredentials,
initContainers,
instanceView,
ipAddress,
isCreatedFromStandbyPool,
location,
osType,
priority,
provisioningState,
restartPolicy,
secretReferences,
sku,
standbyPoolProfile,
subnetIds,
systemData,
tags,
type,
volumes,
zones
FROM azure.containerinstance.container_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_group_name = '{{ container_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get a list of container groups in the specified subscription and resource group. Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containerGroupProfile,
containers,
diagnostics,
dnsConfig,
encryptionProperties,
extensions,
identity,
identityAcls,
imageRegistryCredentials,
initContainers,
instanceView,
ipAddress,
isCreatedFromStandbyPool,
location,
osType,
priority,
provisioningState,
restartPolicy,
secretReferences,
sku,
standbyPoolProfile,
subnetIds,
systemData,
tags,
type,
volumes,
zones
FROM azure.containerinstance.container_groups
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of container groups in the specified subscription. Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containerGroupProfile,
containers,
diagnostics,
dnsConfig,
encryptionProperties,
extensions,
identity,
identityAcls,
imageRegistryCredentials,
initContainers,
instanceView,
ipAddress,
isCreatedFromStandbyPool,
location,
osType,
priority,
provisioningState,
restartPolicy,
secretReferences,
sku,
standbyPoolProfile,
subnetIds,
systemData,
tags,
type,
volumes,
zones
FROM azure.containerinstance.container_groups
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

Create or update container groups. Create or update container groups with specified configurations.

```sql
INSERT INTO azure.containerinstance.container_groups (
location,
tags,
zones,
identity,
properties,
resource_group_name,
container_group_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ zones }}',
'{{ identity }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ container_group_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: container_groups
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the container_groups resource.
    - name: container_group_name
      value: "{{ container_group_name }}"
      description: Required parameter for the container_groups resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the container_groups resource.
    - name: location
      value: "{{ location }}"
      description: |
        The resource location of the container group.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: identity
      description: |
        The identity of the container group, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      description: |
        The container group properties. Required.
      value:
        provisioningState: "{{ provisioningState }}"
        secretReferences:
          - name: "{{ name }}"
            identity: "{{ identity }}"
            secretReferenceUri: "{{ secretReferenceUri }}"
        containers:
          - name: "{{ name }}"
            properties:
              image: "{{ image }}"
              command:
                - "{{ command }}"
              ports:
                - protocol: "{{ protocol }}"
                  port: {{ port }}
              environmentVariables:
                - name: "{{ name }}"
                  value: "{{ value }}"
                  secureValue: "{{ secureValue }}"
                  secureValueReference: "{{ secureValueReference }}"
              instanceView:
                restartCount: {{ restartCount }}
                currentState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                previousState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                events:
                  - count: {{ count }}
                    firstTimestamp: "{{ firstTimestamp }}"
                    lastTimestamp: "{{ lastTimestamp }}"
                    name: "{{ name }}"
                    message: "{{ message }}"
                    type: "{{ type }}"
              resources:
                requests:
                  memoryInGB: {{ memoryInGB }}
                  cpu: {{ cpu }}
                  gpu: "{{ gpu }}"
                limits:
                  memoryInGB: {{ memoryInGB }}
                  cpu: {{ cpu }}
                  gpu: "{{ gpu }}"
              volumeMounts:
                - name: "{{ name }}"
                  mountPath: "{{ mountPath }}"
                  readOnly: {{ readOnly }}
              livenessProbe:
                exec:
                  command: "{{ command }}"
                httpGet:
                  path: "{{ path }}"
                  port: {{ port }}
                  scheme: "{{ scheme }}"
                  httpHeaders: "{{ httpHeaders }}"
                initialDelaySeconds: {{ initialDelaySeconds }}
                periodSeconds: {{ periodSeconds }}
                failureThreshold: {{ failureThreshold }}
                successThreshold: {{ successThreshold }}
                timeoutSeconds: {{ timeoutSeconds }}
              readinessProbe:
                exec:
                  command: "{{ command }}"
                httpGet:
                  path: "{{ path }}"
                  port: {{ port }}
                  scheme: "{{ scheme }}"
                  httpHeaders: "{{ httpHeaders }}"
                initialDelaySeconds: {{ initialDelaySeconds }}
                periodSeconds: {{ periodSeconds }}
                failureThreshold: {{ failureThreshold }}
                successThreshold: {{ successThreshold }}
                timeoutSeconds: {{ timeoutSeconds }}
              securityContext:
                privileged: {{ privileged }}
                allowPrivilegeEscalation: {{ allowPrivilegeEscalation }}
                capabilities:
                  add: "{{ add }}"
                  drop: "{{ drop }}"
                runAsGroup: {{ runAsGroup }}
                runAsUser: {{ runAsUser }}
                seccompProfile: "{{ seccompProfile }}"
              configMap:
                keyValuePairs: "{{ keyValuePairs }}"
        imageRegistryCredentials:
          - server: "{{ server }}"
            username: "{{ username }}"
            password: "{{ password }}"
            passwordReference: "{{ passwordReference }}"
            identity: "{{ identity }}"
            identityUrl: "{{ identityUrl }}"
        restartPolicy: "{{ restartPolicy }}"
        ipAddress:
          ports:
            - protocol: "{{ protocol }}"
              port: {{ port }}
          type: "{{ type }}"
          ip: "{{ ip }}"
          dnsNameLabel: "{{ dnsNameLabel }}"
          autoGeneratedDomainNameLabelScope: "{{ autoGeneratedDomainNameLabelScope }}"
          fqdn: "{{ fqdn }}"
        osType: "{{ osType }}"
        volumes:
          - name: "{{ name }}"
            azureFile:
              shareName: "{{ shareName }}"
              readOnly: {{ readOnly }}
              storageAccountName: "{{ storageAccountName }}"
              storageAccountKey: "{{ storageAccountKey }}"
              storageAccountKeyReference: "{{ storageAccountKeyReference }}"
            emptyDir: "{{ emptyDir }}"
            secret: "{{ secret }}"
            secretReference: "{{ secretReference }}"
            gitRepo:
              directory: "{{ directory }}"
              repository: "{{ repository }}"
              revision: "{{ revision }}"
        instanceView:
          events:
            - count: {{ count }}
              firstTimestamp: "{{ firstTimestamp }}"
              lastTimestamp: "{{ lastTimestamp }}"
              name: "{{ name }}"
              message: "{{ message }}"
              type: "{{ type }}"
          state: "{{ state }}"
        diagnostics:
          logAnalytics:
            workspaceId: "{{ workspaceId }}"
            workspaceKey: "{{ workspaceKey }}"
            logType: "{{ logType }}"
            metadata: "{{ metadata }}"
            workspaceResourceId: "{{ workspaceResourceId }}"
        subnetIds:
          - id: "{{ id }}"
            name: "{{ name }}"
        dnsConfig:
          nameServers:
            - "{{ nameServers }}"
          searchDomains: "{{ searchDomains }}"
          options: "{{ options }}"
        sku: "{{ sku }}"
        encryptionProperties:
          vaultBaseUrl: "{{ vaultBaseUrl }}"
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
          identity: "{{ identity }}"
        initContainers:
          - name: "{{ name }}"
            properties:
              image: "{{ image }}"
              command:
                - "{{ command }}"
              environmentVariables:
                - name: "{{ name }}"
                  value: "{{ value }}"
                  secureValue: "{{ secureValue }}"
                  secureValueReference: "{{ secureValueReference }}"
              instanceView:
                restartCount: {{ restartCount }}
                currentState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                previousState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                events:
                  - count: {{ count }}
                    firstTimestamp: "{{ firstTimestamp }}"
                    lastTimestamp: "{{ lastTimestamp }}"
                    name: "{{ name }}"
                    message: "{{ message }}"
                    type: "{{ type }}"
              volumeMounts:
                - name: "{{ name }}"
                  mountPath: "{{ mountPath }}"
                  readOnly: {{ readOnly }}
              securityContext:
                privileged: {{ privileged }}
                allowPrivilegeEscalation: {{ allowPrivilegeEscalation }}
                capabilities:
                  add: "{{ add }}"
                  drop: "{{ drop }}"
                runAsGroup: {{ runAsGroup }}
                runAsUser: {{ runAsUser }}
                seccompProfile: "{{ seccompProfile }}"
        extensions:
          - name: "{{ name }}"
            properties:
              extensionType: "{{ extensionType }}"
              version: "{{ version }}"
              settings: "{{ settings }}"
              protectedSettings: "{{ protectedSettings }}"
        confidentialComputeProperties:
          ccePolicy: "{{ ccePolicy }}"
        priority: "{{ priority }}"
        identityAcls:
          defaultAccess: "{{ defaultAccess }}"
          acls:
            - access: "{{ access }}"
              identity: "{{ identity }}"
        containerGroupProfile:
          id: "{{ id }}"
          revision: {{ revision }}
        standbyPoolProfile:
          id: "{{ id }}"
          failContainerGroupCreateOnReuseFailure: {{ failContainerGroupCreateOnReuseFailure }}
        isCreatedFromStandbyPool: {{ isCreatedFromStandbyPool }}
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

Update container groups. Updates container group tags with specified values.

```sql
UPDATE azure.containerinstance.container_groups
SET 
location = '{{ location }}',
tags = '{{ tags }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_group_name = '{{ container_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type,
zones;
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

Create or update container groups. Create or update container groups with specified configurations.

```sql
REPLACE azure.containerinstance.container_groups
SET 
location = '{{ location }}',
tags = '{{ tags }}',
zones = '{{ zones }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_group_name = '{{ container_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type,
zones;
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

Delete the specified container group. Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes.

```sql
DELETE FROM azure.containerinstance.container_groups
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND container_group_name = '{{ container_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_outbound_network_dependencies_endpoints"
    values={[
        { label: 'get_outbound_network_dependencies_endpoints', value: 'get_outbound_network_dependencies_endpoints' },
        { label: 'restart', value: 'restart' },
        { label: 'stop', value: 'stop' },
        { label: 'start', value: 'start' }
    ]}
>
<TabItem value="get_outbound_network_dependencies_endpoints">

Get all network dependencies for container group. Gets all the network dependencies for this container group to allow complete control of network setting and configuration. For container groups, this will always be an empty list.

```sql
EXEC azure.containerinstance.container_groups.get_outbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_name='{{ container_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restarts all containers in a container group. Restarts all containers in a container group in place. If container image has updates, new image will be downloaded.

```sql
EXEC azure.containerinstance.container_groups.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_name='{{ container_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops all containers in a container group. Stops all containers in a container group. Compute resources will be deallocated and billing will stop.

```sql
EXEC azure.containerinstance.container_groups.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_name='{{ container_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts all containers in a container group. Starts all containers in a container group. Compute resources will be allocated and billing will start.

```sql
EXEC azure.containerinstance.container_groups.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_name='{{ container_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
