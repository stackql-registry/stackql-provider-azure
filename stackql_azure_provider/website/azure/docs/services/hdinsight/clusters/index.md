--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

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
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error message associated with the cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The async operation state. Known values are: "InProgress", "Succeeded", and "Failed". (InProgress, Succeeded, Failed)</td>
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
    <td><CopyableCode code="clusterDefinition" /></td>
    <td><code>object</code></td>
    <td>The cluster definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterHdpVersion" /></td>
    <td><code>string</code></td>
    <td>The hdp version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The cluster id.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterState" /></td>
    <td><code>string</code></td>
    <td>The state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="computeIsolationProperties" /></td>
    <td><code>object</code></td>
    <td>The compute isolation properties.</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>The compute profile.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of connectivity endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string</code></td>
    <td>The date on which the cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The disk encryption properties.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionInTransitProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption-in-transit properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedServicesConfig" /></td>
    <td><code>object</code></td>
    <td>The excluded services config.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaRestProperties" /></td>
    <td><code>object</code></td>
    <td>The cluster kafka rest proxy configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minSupportedTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimal supported tls version.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProperties" /></td>
    <td><code>object</code></td>
    <td>The network properties.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of operating system. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>The private link configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "InProgress", "Failed", "Succeeded", "Canceled", and "Deleting". (InProgress, Failed, Succeeded, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaInfo" /></td>
    <td><code>object</code></td>
    <td>The quota information.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage profile.</td>
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
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>The cluster tier. Known values are: "Standard" and "Premium". (Standard, Premium)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="clusterDefinition" /></td>
    <td><code>object</code></td>
    <td>The cluster definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterHdpVersion" /></td>
    <td><code>string</code></td>
    <td>The hdp version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The cluster id.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterState" /></td>
    <td><code>string</code></td>
    <td>The state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="computeIsolationProperties" /></td>
    <td><code>object</code></td>
    <td>The compute isolation properties.</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>The compute profile.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of connectivity endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string</code></td>
    <td>The date on which the cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The disk encryption properties.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionInTransitProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption-in-transit properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedServicesConfig" /></td>
    <td><code>object</code></td>
    <td>The excluded services config.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaRestProperties" /></td>
    <td><code>object</code></td>
    <td>The cluster kafka rest proxy configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minSupportedTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimal supported tls version.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProperties" /></td>
    <td><code>object</code></td>
    <td>The network properties.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of operating system. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>The private link configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "InProgress", "Failed", "Succeeded", "Canceled", and "Deleting". (InProgress, Failed, Succeeded, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaInfo" /></td>
    <td><code>object</code></td>
    <td>The quota information.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage profile.</td>
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
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>The cluster tier. Known values are: "Standard" and "Premium". (Standard, Premium)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="clusterDefinition" /></td>
    <td><code>object</code></td>
    <td>The cluster definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterHdpVersion" /></td>
    <td><code>string</code></td>
    <td>The hdp version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterId" /></td>
    <td><code>string</code></td>
    <td>The cluster id.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterState" /></td>
    <td><code>string</code></td>
    <td>The state of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="computeIsolationProperties" /></td>
    <td><code>object</code></td>
    <td>The compute isolation properties.</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>The compute profile.</td>
</tr>
<tr>
    <td><CopyableCode code="connectivityEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of connectivity endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string</code></td>
    <td>The date on which the cluster was created.</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The disk encryption properties.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionInTransitProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption-in-transit properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedServicesConfig" /></td>
    <td><code>object</code></td>
    <td>The excluded services config.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the cluster, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="kafkaRestProperties" /></td>
    <td><code>object</code></td>
    <td>The cluster kafka rest proxy configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minSupportedTlsVersion" /></td>
    <td><code>string</code></td>
    <td>The minimal supported tls version.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProperties" /></td>
    <td><code>object</code></td>
    <td>The network properties.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of operating system. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>The private link configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "InProgress", "Failed", "Succeeded", "Canceled", and "Deleting". (InProgress, Failed, Succeeded, Canceled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="quotaInfo" /></td>
    <td><code>object</code></td>
    <td>The quota information.</td>
</tr>
<tr>
    <td><CopyableCode code="securityProfile" /></td>
    <td><code>object</code></td>
    <td>The security profile.</td>
</tr>
<tr>
    <td><CopyableCode code="storageProfile" /></td>
    <td><code>object</code></td>
    <td>The storage profile.</td>
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
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>The cluster tier. Known values are: "Standard" and "Premium". (Standard, Premium)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#get_azure_async_operation_status"><CopyableCode code="get_azure_async_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The the async operation status.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the HDInsight clusters in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the HDInsight clusters under the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new HDInsight cluster with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch HDInsight cluster with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#get_gateway_settings"><CopyableCode code="get_gateway_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the gateway settings for the specified cluster.</td>
</tr>
<tr>
    <td><a href="#resize"><CopyableCode code="resize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-role_name"><code>role_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resizes the specified HDInsight cluster to the specified size.</td>
</tr>
<tr>
    <td><a href="#update_auto_scale_configuration"><CopyableCode code="update_auto_scale_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-role_name"><code>role_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Autoscale Configuration for HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#rotate_disk_encryption_key"><CopyableCode code="rotate_disk_encryption_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Rotate disk encryption key of the specified HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#update_gateway_settings"><CopyableCode code="update_gateway_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Configures the gateway settings on the specified cluster.</td>
</tr>
<tr>
    <td><a href="#update_identity_certificate"><CopyableCode code="update_identity_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the cluster identity certificate.</td>
</tr>
<tr>
    <td><a href="#execute_script_actions"><CopyableCode code="execute_script_actions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-persistOnSuccess"><code>persistOnSuccess</code></a></td>
    <td></td>
    <td>Executes script actions on the specified HDInsight cluster.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The long running operation id. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-role_name">
    <td><CopyableCode code="role_name" /></td>
    <td><code>string</code></td>
    <td>The constant value for the roleName. "workernode" Required.</td>
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
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

The the async operation status.

```sql
SELECT
error,
status
FROM azure.hdinsight.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the specified cluster.

```sql
SELECT
id,
name,
clusterDefinition,
clusterHdpVersion,
clusterId,
clusterState,
clusterVersion,
computeIsolationProperties,
computeProfile,
connectivityEndpoints,
createdDate,
diskEncryptionProperties,
encryptionInTransitProperties,
errors,
etag,
excludedServicesConfig,
identity,
kafkaRestProperties,
location,
minSupportedTlsVersion,
networkProperties,
osType,
privateEndpointConnections,
privateLinkConfigurations,
provisioningState,
quotaInfo,
securityProfile,
storageProfile,
systemData,
tags,
tier,
type,
zones
FROM azure.hdinsight.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the HDInsight clusters in a resource group.

```sql
SELECT
id,
name,
clusterDefinition,
clusterHdpVersion,
clusterId,
clusterState,
clusterVersion,
computeIsolationProperties,
computeProfile,
connectivityEndpoints,
createdDate,
diskEncryptionProperties,
encryptionInTransitProperties,
errors,
etag,
excludedServicesConfig,
identity,
kafkaRestProperties,
location,
minSupportedTlsVersion,
networkProperties,
osType,
privateEndpointConnections,
privateLinkConfigurations,
provisioningState,
quotaInfo,
securityProfile,
storageProfile,
systemData,
tags,
tier,
type,
zones
FROM azure.hdinsight.clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the HDInsight clusters under the subscription.

```sql
SELECT
id,
name,
clusterDefinition,
clusterHdpVersion,
clusterId,
clusterState,
clusterVersion,
computeIsolationProperties,
computeProfile,
connectivityEndpoints,
createdDate,
diskEncryptionProperties,
encryptionInTransitProperties,
errors,
etag,
excludedServicesConfig,
identity,
kafkaRestProperties,
location,
minSupportedTlsVersion,
networkProperties,
osType,
privateEndpointConnections,
privateLinkConfigurations,
provisioningState,
quotaInfo,
securityProfile,
storageProfile,
systemData,
tags,
tier,
type,
zones
FROM azure.hdinsight.clusters
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates a new HDInsight cluster with the specified parameters.

```sql
INSERT INTO azure.hdinsight.clusters (
location,
tags,
zones,
properties,
identity,
resource_group_name,
cluster_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ zones }}',
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the clusters resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the clusters resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the cluster.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
    - name: properties
      description: |
        The cluster create parameters.
      value:
        clusterVersion: "{{ clusterVersion }}"
        osType: "{{ osType }}"
        tier: "{{ tier }}"
        clusterDefinition:
          blueprint: "{{ blueprint }}"
          kind: "{{ kind }}"
          componentVersion: "{{ componentVersion }}"
          configurations: "{{ configurations }}"
        kafkaRestProperties:
          clientGroupInfo:
            groupName: "{{ groupName }}"
            groupId: "{{ groupId }}"
          configurationOverride: "{{ configurationOverride }}"
        securityProfile:
          directoryType: "{{ directoryType }}"
          domain: "{{ domain }}"
          organizationalUnitDN: "{{ organizationalUnitDN }}"
          ldapsUrls:
            - "{{ ldapsUrls }}"
          domainUsername: "{{ domainUsername }}"
          domainUserPassword: "{{ domainUserPassword }}"
          clusterUsersGroupDNs:
            - "{{ clusterUsersGroupDNs }}"
          aaddsResourceId: "{{ aaddsResourceId }}"
          msiResourceId: "{{ msiResourceId }}"
        computeProfile:
          roles:
            - name: "{{ name }}"
              minInstanceCount: {{ minInstanceCount }}
              targetInstanceCount: {{ targetInstanceCount }}
              VMGroupName: "{{ VMGroupName }}"
              autoscale:
                capacity:
                  minInstanceCount: {{ minInstanceCount }}
                  maxInstanceCount: {{ maxInstanceCount }}
                recurrence:
                  timeZone: "{{ timeZone }}"
                  schedule: "{{ schedule }}"
              hardwareProfile:
                vmSize: "{{ vmSize }}"
              osProfile:
                linuxOperatingSystemProfile:
                  username: "{{ username }}"
                  password: "{{ password }}"
                  sshProfile: "{{ sshProfile }}"
              virtualNetworkProfile:
                id: "{{ id }}"
                subnet: "{{ subnet }}"
              dataDisksGroups: "{{ dataDisksGroups }}"
              scriptActions: "{{ scriptActions }}"
              encryptDataDisks: {{ encryptDataDisks }}
        storageProfile:
          storageaccounts:
            - name: "{{ name }}"
              isDefault: {{ isDefault }}
              container: "{{ container }}"
              fileSystem: "{{ fileSystem }}"
              key: "{{ key }}"
              resourceId: "{{ resourceId }}"
              msiResourceId: "{{ msiResourceId }}"
              saskey: "{{ saskey }}"
              fileshare: "{{ fileshare }}"
              enableSecureChannel: {{ enableSecureChannel }}
        diskEncryptionProperties:
          vaultUri: "{{ vaultUri }}"
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
          encryptionAlgorithm: "{{ encryptionAlgorithm }}"
          msiResourceId: "{{ msiResourceId }}"
          encryptionAtHost: {{ encryptionAtHost }}
        encryptionInTransitProperties:
          isEncryptionInTransitEnabled: {{ isEncryptionInTransitEnabled }}
        minSupportedTlsVersion: "{{ minSupportedTlsVersion }}"
        networkProperties:
          outboundDependenciesManagedType: "{{ outboundDependenciesManagedType }}"
          resourceProviderConnection: "{{ resourceProviderConnection }}"
          privateLink: "{{ privateLink }}"
          publicIpTag:
            ipTagType: "{{ ipTagType }}"
            tag: "{{ tag }}"
        computeIsolationProperties:
          enableComputeIsolation: {{ enableComputeIsolation }}
          hostSku: "{{ hostSku }}"
        privateLinkConfigurations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              groupId: "{{ groupId }}"
              provisioningState: "{{ provisioningState }}"
              ipConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    provisioningState: "{{ provisioningState }}"
                    primary: {{ primary }}
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    subnet: "{{ subnet }}"
    - name: identity
      description: |
        The identity of the cluster, if configured.
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

Patch HDInsight cluster with the specified parameters.

```sql
UPDATE azure.hdinsight.clusters
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Deletes the specified HDInsight cluster.

```sql
DELETE FROM azure.hdinsight.clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_gateway_settings"
    values={[
        { label: 'get_gateway_settings', value: 'get_gateway_settings' },
        { label: 'resize', value: 'resize' },
        { label: 'update_auto_scale_configuration', value: 'update_auto_scale_configuration' },
        { label: 'rotate_disk_encryption_key', value: 'rotate_disk_encryption_key' },
        { label: 'update_gateway_settings', value: 'update_gateway_settings' },
        { label: 'update_identity_certificate', value: 'update_identity_certificate' },
        { label: 'execute_script_actions', value: 'execute_script_actions' }
    ]}
>
<TabItem value="get_gateway_settings">

Gets the gateway settings for the specified cluster.

```sql
EXEC azure.hdinsight.clusters.get_gateway_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resize">

Resizes the specified HDInsight cluster to the specified size.

```sql
EXEC azure.hdinsight.clusters.resize 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@role_name='{{ role_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetInstanceCount": {{ targetInstanceCount }}
}'
;
```
</TabItem>
<TabItem value="update_auto_scale_configuration">

Updates the Autoscale Configuration for HDInsight cluster.

```sql
EXEC azure.hdinsight.clusters.update_auto_scale_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@role_name='{{ role_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"autoscale": "{{ autoscale }}"
}'
;
```
</TabItem>
<TabItem value="rotate_disk_encryption_key">

Rotate disk encryption key of the specified HDInsight cluster.

```sql
EXEC azure.hdinsight.clusters.rotate_disk_encryption_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"vaultUri": "{{ vaultUri }}", 
"keyName": "{{ keyName }}", 
"keyVersion": "{{ keyVersion }}"
}'
;
```
</TabItem>
<TabItem value="update_gateway_settings">

Configures the gateway settings on the specified cluster.

```sql
EXEC azure.hdinsight.clusters.update_gateway_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"restAuthCredential": "{{ restAuthCredential }}", 
"restAuthEntraUsers": "{{ restAuthEntraUsers }}"
}'
;
```
</TabItem>
<TabItem value="update_identity_certificate">

Updates the cluster identity certificate.

```sql
EXEC azure.hdinsight.clusters.update_identity_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"applicationId": "{{ applicationId }}", 
"certificate": "{{ certificate }}", 
"certificatePassword": "{{ certificatePassword }}"
}'
;
```
</TabItem>
<TabItem value="execute_script_actions">

Executes script actions on the specified HDInsight cluster.

```sql
EXEC azure.hdinsight.clusters.execute_script_actions 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"scriptActions": "{{ scriptActions }}", 
"persistOnSuccess": {{ persistOnSuccess }}
}'
;
```
</TabItem>
</Tabs>
