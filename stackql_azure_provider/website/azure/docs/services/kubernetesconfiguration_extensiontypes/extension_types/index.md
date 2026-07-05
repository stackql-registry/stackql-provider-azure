--- 
title: extension_types
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_types
  - kubernetesconfiguration_extensiontypes
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

Creates, updates, deletes, gets or lists an <code>extension_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extension_types" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesconfiguration_extensiontypes.extension_types" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the extension type.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagedIdentityRequired" /></td>
    <td><code>boolean</code></td>
    <td>Should an identity for this cluster resource be created.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemExtension" /></td>
    <td><code>boolean</code></td>
    <td>Is this Extension Type a system extension.</td>
</tr>
<tr>
    <td><CopyableCode code="planInfo" /></td>
    <td><code>object</code></td>
    <td>Plan information only for the Marketplace Extension Type.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Name of the publisher for the Extension Type.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedClusterTypes" /></td>
    <td><code>array</code></td>
    <td>Cluster Types supported for this Extension Type.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedScopes" /></td>
    <td><code>object</code></td>
    <td>Supported Kubernetes Scopes for this Extension Type.</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the extension type.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagedIdentityRequired" /></td>
    <td><code>boolean</code></td>
    <td>Should an identity for this cluster resource be created.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemExtension" /></td>
    <td><code>boolean</code></td>
    <td>Is this Extension Type a system extension.</td>
</tr>
<tr>
    <td><CopyableCode code="planInfo" /></td>
    <td><code>object</code></td>
    <td>Plan information only for the Marketplace Extension Type.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Name of the publisher for the Extension Type.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedClusterTypes" /></td>
    <td><code>array</code></td>
    <td>Cluster Types supported for this Extension Type.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedScopes" /></td>
    <td><code>object</code></td>
    <td>Supported Kubernetes Scopes for this Extension Type.</td>
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
<TabItem value="get_version">

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
    <td><CopyableCode code="supportedClusterTypes" /></td>
    <td><code>array</code></td>
    <td>A list of supported cluster types for this version of the Extension Type.</td>
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
    <td><CopyableCode code="unsupportedKubernetesVersions" /></td>
    <td><code>object</code></td>
    <td>The list of supported Kubernetes cluster versions for this extension type.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version number for the extension type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_versions">

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
    <td><CopyableCode code="supportedClusterTypes" /></td>
    <td><code>array</code></td>
    <td>A list of supported cluster types for this version of the Extension Type.</td>
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
    <td><CopyableCode code="unsupportedKubernetesVersions" /></td>
    <td><code>object</code></td>
    <td>The list of supported Kubernetes cluster versions for this extension type.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version number for the extension type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_type_name"><code>extension_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an Extension Type installable to the cluster based region and type for the cluster.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-publisherId"><code>publisherId</code></a>, <a href="#parameter-offerId"><code>offerId</code></a>, <a href="#parameter-planId"><code>planId</code></a>, <a href="#parameter-releaseTrain"><code>releaseTrain</code></a></td>
    <td>List installable Extension Types for the cluster based region and type for the cluster.</td>
</tr>
<tr>
    <td><a href="#get_version"><CopyableCode code="get_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extension_type_name"><code>extension_type_name</code></a>, <a href="#parameter-version_number"><code>version_number</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of a version for an extension type and location.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extension_type_name"><code>extension_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-releaseTrain"><code>releaseTrain</code></a>, <a href="#parameter-clusterType"><code>clusterType</code></a>, <a href="#parameter-majorVersion"><code>majorVersion</code></a>, <a href="#parameter-showLatest"><code>showLatest</code></a></td>
    <td>List the versions for an extension type and location.</td>
</tr>
<tr>
    <td><a href="#location_get"><CopyableCode code="location_get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-extension_type_name"><code>extension_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an extension type for the location.</td>
</tr>
<tr>
    <td><a href="#location_list"><CopyableCode code="location_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-publisherId"><code>publisherId</code></a>, <a href="#parameter-offerId"><code>offerId</code></a>, <a href="#parameter-planId"><code>planId</code></a>, <a href="#parameter-releaseTrain"><code>releaseTrain</code></a>, <a href="#parameter-clusterType"><code>clusterType</code></a></td>
    <td>List all Extension Types for the location.</td>
</tr>
<tr>
    <td><a href="#cluster_get_version"><CopyableCode code="cluster_get_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_type_name"><code>extension_type_name</code></a>, <a href="#parameter-version_number"><code>version_number</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of a version for an Extension Type installable to the cluster.</td>
</tr>
<tr>
    <td><a href="#cluster_list_versions"><CopyableCode code="cluster_list_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_type_name"><code>extension_type_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-releaseTrain"><code>releaseTrain</code></a>, <a href="#parameter-majorVersion"><code>majorVersion</code></a>, <a href="#parameter-showLatest"><code>showLatest</code></a></td>
    <td>List the version for an Extension Type installable to the cluster.</td>
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
    <td>The name of the kubernetes cluster. Required.</td>
</tr>
<tr id="parameter-cluster_resource_name">
    <td><CopyableCode code="cluster_resource_name" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters, appliances. Required.</td>
</tr>
<tr id="parameter-cluster_rp">
    <td><CopyableCode code="cluster_rp" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.</td>
</tr>
<tr id="parameter-extension_type_name">
    <td><CopyableCode code="extension_type_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Extension Type. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
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
<tr id="parameter-version_number">
    <td><CopyableCode code="version_number" /></td>
    <td><code>string</code></td>
    <td>Version number of the Extension Type. Required.</td>
</tr>
<tr id="parameter-clusterType">
    <td><CopyableCode code="clusterType" /></td>
    <td><code>string</code></td>
    <td>Filter results by the cluster type for extension types. Default value is None.</td>
</tr>
<tr id="parameter-majorVersion">
    <td><CopyableCode code="majorVersion" /></td>
    <td><code>string</code></td>
    <td>Filter results by the major version of an extension type. Default value is None.</td>
</tr>
<tr id="parameter-offerId">
    <td><CopyableCode code="offerId" /></td>
    <td><code>string</code></td>
    <td>Filter results by Offer or Product ID of a marketplace extension type. Default value is None.</td>
</tr>
<tr id="parameter-planId">
    <td><CopyableCode code="planId" /></td>
    <td><code>string</code></td>
    <td>Filter results by Plan ID of a marketplace extension type. Default value is None.</td>
</tr>
<tr id="parameter-publisherId">
    <td><CopyableCode code="publisherId" /></td>
    <td><code>string</code></td>
    <td>Filter results by Publisher ID of a marketplace extension type. Default value is None.</td>
</tr>
<tr id="parameter-releaseTrain">
    <td><CopyableCode code="releaseTrain" /></td>
    <td><code>string</code></td>
    <td>Filter results by release train (default value is stable). Default value is None.</td>
</tr>
<tr id="parameter-showLatest">
    <td><CopyableCode code="showLatest" /></td>
    <td><code>boolean</code></td>
    <td>Filter results by only the latest version (based on other query parameters). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_version', value: 'get_version' },
        { label: 'list_versions', value: 'list_versions' }
    ]}
>
<TabItem value="get">

Get an Extension Type installable to the cluster based region and type for the cluster.

```sql
SELECT
id,
name,
description,
isManagedIdentityRequired,
isSystemExtension,
planInfo,
publisher,
supportedClusterTypes,
supportedScopes,
systemData,
type
FROM azure.kubernetesconfiguration_extensiontypes.extension_types
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND extension_type_name = '{{ extension_type_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List installable Extension Types for the cluster based region and type for the cluster.

```sql
SELECT
id,
name,
description,
isManagedIdentityRequired,
isSystemExtension,
planInfo,
publisher,
supportedClusterTypes,
supportedScopes,
systemData,
type
FROM azure.kubernetesconfiguration_extensiontypes.extension_types
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND publisherId = '{{ publisherId }}'
AND offerId = '{{ offerId }}'
AND planId = '{{ planId }}'
AND releaseTrain = '{{ releaseTrain }}'
;
```
</TabItem>
<TabItem value="get_version">

Get details of a version for an extension type and location.

```sql
SELECT
id,
name,
supportedClusterTypes,
systemData,
type,
unsupportedKubernetesVersions,
version
FROM azure.kubernetesconfiguration_extensiontypes.extension_types
WHERE location = '{{ location }}' -- required
AND extension_type_name = '{{ extension_type_name }}' -- required
AND version_number = '{{ version_number }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_versions">

List the versions for an extension type and location.

```sql
SELECT
id,
name,
supportedClusterTypes,
systemData,
type,
unsupportedKubernetesVersions,
version
FROM azure.kubernetesconfiguration_extensiontypes.extension_types
WHERE location = '{{ location }}' -- required
AND extension_type_name = '{{ extension_type_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND releaseTrain = '{{ releaseTrain }}'
AND clusterType = '{{ clusterType }}'
AND majorVersion = '{{ majorVersion }}'
AND showLatest = '{{ showLatest }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="location_get"
    values={[
        { label: 'location_get', value: 'location_get' },
        { label: 'location_list', value: 'location_list' },
        { label: 'cluster_get_version', value: 'cluster_get_version' },
        { label: 'cluster_list_versions', value: 'cluster_list_versions' }
    ]}
>
<TabItem value="location_get">

Get an extension type for the location.

```sql
EXEC azure.kubernetesconfiguration_extensiontypes.extension_types.location_get 
@location='{{ location }}' --required, 
@extension_type_name='{{ extension_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="location_list">

List all Extension Types for the location.

```sql
EXEC azure.kubernetesconfiguration_extensiontypes.extension_types.location_list 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@publisherId='{{ publisherId }}', 
@offerId='{{ offerId }}', 
@planId='{{ planId }}', 
@releaseTrain='{{ releaseTrain }}', 
@clusterType='{{ clusterType }}'
;
```
</TabItem>
<TabItem value="cluster_get_version">

Get details of a version for an Extension Type installable to the cluster.

```sql
EXEC azure.kubernetesconfiguration_extensiontypes.extension_types.cluster_get_version 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_rp='{{ cluster_rp }}' --required, 
@cluster_resource_name='{{ cluster_resource_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@extension_type_name='{{ extension_type_name }}' --required, 
@version_number='{{ version_number }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cluster_list_versions">

List the version for an Extension Type installable to the cluster.

```sql
EXEC azure.kubernetesconfiguration_extensiontypes.extension_types.cluster_list_versions 
@resource_group_name='{{ resource_group_name }}' --required, 
@cluster_rp='{{ cluster_rp }}' --required, 
@cluster_resource_name='{{ cluster_resource_name }}' --required, 
@cluster_name='{{ cluster_name }}' --required, 
@extension_type_name='{{ extension_type_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@releaseTrain='{{ releaseTrain }}', 
@majorVersion='{{ majorVersion }}', 
@showLatest={{ showLatest }}
;
```
</TabItem>
</Tabs>
