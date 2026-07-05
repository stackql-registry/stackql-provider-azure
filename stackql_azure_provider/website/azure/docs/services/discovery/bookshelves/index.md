--- 
title: bookshelves
hide_title: false
hide_table_of_contents: false
keywords:
  - bookshelves
  - discovery
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

Creates, updates, deletes, gets or lists a <code>bookshelves</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bookshelves" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.discovery.bookshelves" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="bookshelfUri" /></td>
    <td><code>string</code></td>
    <td>The bookshelf data plane API URI.</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeys" /></td>
    <td><code>string</code></td>
    <td>Whether or not to use a customer managed key when encrypting data at rest. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>The key to use for encrypting data at rest when customer managed keys are enabled. Required if Customer Managed Keys is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsClusterId" /></td>
    <td><code>string</code></td>
    <td>The Log Analytics Cluster to use for debug logs. This is required when Customer Managed Keys are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed-On-Behalf-Of configuration properties. This configuration exists for the resources where a resource provider manages those resources on behalf of the resource owner.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group for resources managed on behalf of customer.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointSubnetId" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint Subnet ID for private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for this resource. For security reasons, it is recommended to disable it whenever possible. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="searchSubnetId" /></td>
    <td><code>string</code></td>
    <td>Search Subnet ID for search resources.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadIdentities" /></td>
    <td><code>object</code></td>
    <td>User assigned identity IDs to be used by knowledgebase workloads. The key value must be the resource ID of the identity resource.</td>
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
    <td><CopyableCode code="bookshelfUri" /></td>
    <td><code>string</code></td>
    <td>The bookshelf data plane API URI.</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeys" /></td>
    <td><code>string</code></td>
    <td>Whether or not to use a customer managed key when encrypting data at rest. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>The key to use for encrypting data at rest when customer managed keys are enabled. Required if Customer Managed Keys is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsClusterId" /></td>
    <td><code>string</code></td>
    <td>The Log Analytics Cluster to use for debug logs. This is required when Customer Managed Keys are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed-On-Behalf-Of configuration properties. This configuration exists for the resources where a resource provider manages those resources on behalf of the resource owner.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group for resources managed on behalf of customer.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointSubnetId" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint Subnet ID for private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for this resource. For security reasons, it is recommended to disable it whenever possible. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="searchSubnetId" /></td>
    <td><code>string</code></td>
    <td>Search Subnet ID for search resources.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadIdentities" /></td>
    <td><code>object</code></td>
    <td>User assigned identity IDs to be used by knowledgebase workloads. The key value must be the resource ID of the identity resource.</td>
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
    <td><CopyableCode code="bookshelfUri" /></td>
    <td><code>string</code></td>
    <td>The bookshelf data plane API URI.</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeys" /></td>
    <td><code>string</code></td>
    <td>Whether or not to use a customer managed key when encrypting data at rest. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultProperties" /></td>
    <td><code>object</code></td>
    <td>The key to use for encrypting data at rest when customer managed keys are enabled. Required if Customer Managed Keys is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logAnalyticsClusterId" /></td>
    <td><code>string</code></td>
    <td>The Log Analytics Cluster to use for debug logs. This is required when Customer Managed Keys are enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="managedOnBehalfOfConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed-On-Behalf-Of configuration properties. This configuration exists for the resources where a resource provider manages those resources on behalf of the resource owner.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroup" /></td>
    <td><code>string</code></td>
    <td>The resource group for resources managed on behalf of customer.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointSubnetId" /></td>
    <td><code>string</code></td>
    <td>Private Endpoint Subnet ID for private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for this resource. For security reasons, it is recommended to disable it whenever possible. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="searchSubnetId" /></td>
    <td><code>string</code></td>
    <td>Search Subnet ID for search resources.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="workloadIdentities" /></td>
    <td><code>object</code></td>
    <td>User assigned identity IDs to be used by knowledgebase workloads. The key value must be the resource ID of the identity resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bookshelf_name"><code>bookshelf_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Bookshelf.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Bookshelf resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Bookshelf resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bookshelf_name"><code>bookshelf_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a Bookshelf.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bookshelf_name"><code>bookshelf_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Update a Bookshelf.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bookshelf_name"><code>bookshelf_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a Bookshelf.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-bookshelf_name"><code>bookshelf_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Bookshelf.</td>
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
<tr id="parameter-bookshelf_name">
    <td><CopyableCode code="bookshelf_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Bookshelf. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a Bookshelf.

```sql
SELECT
id,
name,
bookshelfUri,
customerManagedKeys,
keyVaultProperties,
location,
logAnalyticsClusterId,
managedOnBehalfOfConfiguration,
managedResourceGroup,
privateEndpointConnections,
privateEndpointSubnetId,
provisioningState,
publicNetworkAccess,
searchSubnetId,
systemData,
tags,
type,
workloadIdentities
FROM azure.discovery.bookshelves
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND bookshelf_name = '{{ bookshelf_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List Bookshelf resources by resource group.

```sql
SELECT
id,
name,
bookshelfUri,
customerManagedKeys,
keyVaultProperties,
location,
logAnalyticsClusterId,
managedOnBehalfOfConfiguration,
managedResourceGroup,
privateEndpointConnections,
privateEndpointSubnetId,
provisioningState,
publicNetworkAccess,
searchSubnetId,
systemData,
tags,
type,
workloadIdentities
FROM azure.discovery.bookshelves
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List Bookshelf resources by subscription ID.

```sql
SELECT
id,
name,
bookshelfUri,
customerManagedKeys,
keyVaultProperties,
location,
logAnalyticsClusterId,
managedOnBehalfOfConfiguration,
managedResourceGroup,
privateEndpointConnections,
privateEndpointSubnetId,
provisioningState,
publicNetworkAccess,
searchSubnetId,
systemData,
tags,
type,
workloadIdentities
FROM azure.discovery.bookshelves
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

Create a Bookshelf.

```sql
INSERT INTO azure.discovery.bookshelves (
tags,
location,
properties,
resource_group_name,
bookshelf_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ bookshelf_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bookshelves
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the bookshelves resource.
    - name: bookshelf_name
      value: "{{ bookshelf_name }}"
      description: Required parameter for the bookshelves resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the bookshelves resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        workloadIdentities: "{{ workloadIdentities }}"
        customerManagedKeys: "{{ customerManagedKeys }}"
        keyVaultProperties:
          keyVaultUri: "{{ keyVaultUri }}"
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
          identityClientId: "{{ identityClientId }}"
        logAnalyticsClusterId: "{{ logAnalyticsClusterId }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              groupIds:
                - "{{ groupIds }}"
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        privateEndpointSubnetId: "{{ privateEndpointSubnetId }}"
        searchSubnetId: "{{ searchSubnetId }}"
        managedResourceGroup: "{{ managedResourceGroup }}"
        managedOnBehalfOfConfiguration:
          moboBrokerResources:
            - id: "{{ id }}"
        bookshelfUri: "{{ bookshelfUri }}"
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

Update a Bookshelf.

```sql
UPDATE azure.discovery.bookshelves
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bookshelf_name = '{{ bookshelf_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
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

Create a Bookshelf.

```sql
REPLACE azure.discovery.bookshelves
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND bookshelf_name = '{{ bookshelf_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Delete a Bookshelf.

```sql
DELETE FROM azure.discovery.bookshelves
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND bookshelf_name = '{{ bookshelf_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
