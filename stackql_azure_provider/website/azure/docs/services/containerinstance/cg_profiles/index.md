--- 
title: cg_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - cg_profiles
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

Creates, updates, deletes, gets or lists a <code>cg_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cg_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerinstance.cg_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
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
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="registeredRevisions" /></td>
    <td><code>array</code></td>
    <td>Registered revisions are calculated at request time based off the records in the table logs.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>Container group profile current revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="securityContext" /></td>
    <td><code>object</code></td>
    <td>The container security properties.</td>
</tr>
<tr>
    <td><CopyableCode code="shutdownGracePeriod" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shutdown grace period for containers in a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
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
    <td><CopyableCode code="timeToLive" /></td>
    <td><code>string (date-time)</code></td>
    <td>Post completion time to live for containers of a CG.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useKrypton" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets Krypton use property.</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="registeredRevisions" /></td>
    <td><code>array</code></td>
    <td>Registered revisions are calculated at request time based off the records in the table logs.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>Container group profile current revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="securityContext" /></td>
    <td><code>object</code></td>
    <td>The container security properties.</td>
</tr>
<tr>
    <td><CopyableCode code="shutdownGracePeriod" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shutdown grace period for containers in a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
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
    <td><CopyableCode code="timeToLive" /></td>
    <td><code>string (date-time)</code></td>
    <td>Post completion time to live for containers of a CG.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useKrypton" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets Krypton use property.</td>
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
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List container group profiles in a resource group. Gets a list of all container group profiles under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List container group profiles in a subscription. Gets a list of all container group profiles under a subscription.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_resource_group"
    values={[
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="list_by_resource_group">

List container group profiles in a resource group. Gets a list of all container group profiles under a resource group.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containers,
diagnostics,
encryptionProperties,
extensions,
imageRegistryCredentials,
initContainers,
ipAddress,
location,
osType,
priority,
registeredRevisions,
restartPolicy,
revision,
securityContext,
shutdownGracePeriod,
sku,
systemData,
tags,
timeToLive,
type,
useKrypton,
volumes,
zones
FROM azure.containerinstance.cg_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List container group profiles in a subscription. Gets a list of all container group profiles under a subscription.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containers,
diagnostics,
encryptionProperties,
extensions,
imageRegistryCredentials,
initContainers,
ipAddress,
location,
osType,
priority,
registeredRevisions,
restartPolicy,
revision,
securityContext,
shutdownGracePeriod,
sku,
systemData,
tags,
timeToLive,
type,
useKrypton,
volumes,
zones
FROM azure.containerinstance.cg_profiles
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
