--- 
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - kubernetesconfiguration
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

Creates, updates, deletes, gets or lists an <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesconfiguration.extensions" /></td></tr>
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
    <td><CopyableCode code="aksAssignedIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity of the Extension resource in an AKS cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="autoUpgradeMinorVersion" /></td>
    <td><code>boolean</code></td>
    <td>Flag to note if this extension participates in auto upgrade of minor version, or not.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationProtectedSettings" /></td>
    <td><code>object</code></td>
    <td>Configuration settings that are sensitive, as name-value pairs for configuring this extension.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationSettings" /></td>
    <td><code>object</code></td>
    <td>Configuration settings, as name-value pairs for configuring this extension.</td>
</tr>
<tr>
    <td><CopyableCode code="currentVersion" /></td>
    <td><code>string</code></td>
    <td>Currently installed version of the extension.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationSettings" /></td>
    <td><code>object</code></td>
    <td>Custom Location settings properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errorInfo" /></td>
    <td><code>object</code></td>
    <td>Error information from the Agent - e.g. errors during installation.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionType" /></td>
    <td><code>string</code></td>
    <td>Type of the Extension, of which this resource is an instance of. It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity of the Extension resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemExtension" /></td>
    <td><code>boolean</code></td>
    <td>Flag to note if this extension is a system extension.</td>
</tr>
<tr>
    <td><CopyableCode code="packageUri" /></td>
    <td><code>string</code></td>
    <td>Uri of the Helm package.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of installation of this extension. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="releaseTrain" /></td>
    <td><code>string</code></td>
    <td>ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>Scope at which the extension is installed.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>Status from this extension.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>User-specified version of the extension for this extension to 'pin'. To use 'version', autoUpgradeMinorVersion must be 'false'.</td>
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
    <td><CopyableCode code="aksAssignedIdentity" /></td>
    <td><code>object</code></td>
    <td>Identity of the Extension resource in an AKS cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="autoUpgradeMinorVersion" /></td>
    <td><code>boolean</code></td>
    <td>Flag to note if this extension participates in auto upgrade of minor version, or not.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationProtectedSettings" /></td>
    <td><code>object</code></td>
    <td>Configuration settings that are sensitive, as name-value pairs for configuring this extension.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationSettings" /></td>
    <td><code>object</code></td>
    <td>Configuration settings, as name-value pairs for configuring this extension.</td>
</tr>
<tr>
    <td><CopyableCode code="currentVersion" /></td>
    <td><code>string</code></td>
    <td>Currently installed version of the extension.</td>
</tr>
<tr>
    <td><CopyableCode code="customLocationSettings" /></td>
    <td><code>object</code></td>
    <td>Custom Location settings properties.</td>
</tr>
<tr>
    <td><CopyableCode code="errorInfo" /></td>
    <td><code>object</code></td>
    <td>Error information from the Agent - e.g. errors during installation.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionType" /></td>
    <td><code>string</code></td>
    <td>Type of the Extension, of which this resource is an instance of. It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity of the Extension resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isSystemExtension" /></td>
    <td><code>boolean</code></td>
    <td>Flag to note if this extension is a system extension.</td>
</tr>
<tr>
    <td><CopyableCode code="packageUri" /></td>
    <td><code>string</code></td>
    <td>Uri of the Helm package.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of installation of this extension. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="releaseTrain" /></td>
    <td><code>string</code></td>
    <td>ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>Scope at which the extension is installed.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>Status from this extension.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>User-specified version of the extension for this extension to 'pin'. To use 'version', autoUpgradeMinorVersion must be 'false'.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets Kubernetes Cluster Extension.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Extensions in the cluster.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Kubernetes Cluster Extension.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch an existing Kubernetes Cluster Extension.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDelete"><code>forceDelete</code></a></td>
    <td>Delete a Kubernetes Cluster Extension. This will cause the Agent to Uninstall the extension from the cluster.</td>
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
    <td>The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters. Required.</td>
</tr>
<tr id="parameter-cluster_rp">
    <td><CopyableCode code="cluster_rp" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.</td>
</tr>
<tr id="parameter-extension_name">
    <td><CopyableCode code="extension_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Extension. Required.</td>
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
<tr id="parameter-forceDelete">
    <td><CopyableCode code="forceDelete" /></td>
    <td><code>boolean</code></td>
    <td>Delete the extension resource in Azure - not the normal asynchronous delete. Default value is None.</td>
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

Gets Kubernetes Cluster Extension.

```sql
SELECT
id,
name,
aksAssignedIdentity,
autoUpgradeMinorVersion,
configurationProtectedSettings,
configurationSettings,
currentVersion,
customLocationSettings,
errorInfo,
extensionType,
identity,
isSystemExtension,
packageUri,
plan,
provisioningState,
releaseTrain,
scope,
statuses,
systemData,
type,
version
FROM azure.kubernetesconfiguration.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND extension_name = '{{ extension_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Extensions in the cluster.

```sql
SELECT
id,
name,
aksAssignedIdentity,
autoUpgradeMinorVersion,
configurationProtectedSettings,
configurationSettings,
currentVersion,
customLocationSettings,
errorInfo,
extensionType,
identity,
isSystemExtension,
packageUri,
plan,
provisioningState,
releaseTrain,
scope,
statuses,
systemData,
type,
version
FROM azure.kubernetesconfiguration.extensions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a new Kubernetes Cluster Extension.

```sql
INSERT INTO azure.kubernetesconfiguration.extensions (
identity,
plan,
properties,
resource_group_name,
cluster_rp,
cluster_resource_name,
cluster_name,
extension_name,
subscription_id
)
SELECT 
'{{ identity }}',
'{{ plan }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_rp }}',
'{{ cluster_resource_name }}',
'{{ cluster_name }}',
'{{ extension_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
plan,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: extensions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the extensions resource.
    - name: cluster_rp
      value: "{{ cluster_rp }}"
      description: Required parameter for the extensions resource.
    - name: cluster_resource_name
      value: "{{ cluster_resource_name }}"
      description: Required parameter for the extensions resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the extensions resource.
    - name: extension_name
      value: "{{ extension_name }}"
      description: Required parameter for the extensions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the extensions resource.
    - name: identity
      description: |
        Identity of the Extension resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: plan
      description: |
        The plan information.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
    - name: properties
      value:
        extensionType: "{{ extensionType }}"
        autoUpgradeMinorVersion: {{ autoUpgradeMinorVersion }}
        releaseTrain: "{{ releaseTrain }}"
        version: "{{ version }}"
        scope:
          cluster:
            releaseNamespace: "{{ releaseNamespace }}"
          namespace:
            targetNamespace: "{{ targetNamespace }}"
        configurationSettings: "{{ configurationSettings }}"
        configurationProtectedSettings: "{{ configurationProtectedSettings }}"
        statuses:
          - code: "{{ code }}"
            displayStatus: "{{ displayStatus }}"
            level: "{{ level }}"
            message: "{{ message }}"
            time: "{{ time }}"
        aksAssignedIdentity:
          principalId: "{{ principalId }}"
          tenantId: "{{ tenantId }}"
          type: "{{ type }}"
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

Patch an existing Kubernetes Cluster Extension.

```sql
UPDATE azure.kubernetesconfiguration.extensions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND extension_name = '{{ extension_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
plan,
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

Delete a Kubernetes Cluster Extension. This will cause the Agent to Uninstall the extension from the cluster.

```sql
DELETE FROM azure.kubernetesconfiguration.extensions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND extension_name = '{{ extension_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDelete = '{{ forceDelete }}'
;
```
</TabItem>
</Tabs>
