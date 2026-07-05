--- 
title: supercomputers
hide_title: false
hide_table_of_contents: false
keywords:
  - supercomputers
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

Creates, updates, deletes, gets or lists a <code>supercomputers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="supercomputers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.discovery.supercomputers" /></td></tr>
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
    <td><CopyableCode code="customerManagedKeys" /></td>
    <td><code>string</code></td>
    <td>Whether or not to use a customer managed key when encrypting data at rest. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetId" /></td>
    <td><code>string</code></td>
    <td>Disk Encryption Set ID to use for Customer Managed Keys encryption. Required if Customer Managed Keys is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="identities" /></td>
    <td><code>object</code></td>
    <td>Dictionary of identity properties. Required.</td>
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
    <td><CopyableCode code="managementSubnetId" /></td>
    <td><code>string</code></td>
    <td>System Subnet ID associated with AKS apiserver. Must be delegated to Microsoft.ContainerService/managedClusters. It should have connectivity to the system subnet and nodepool subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundType" /></td>
    <td><code>string</code></td>
    <td>Network egress type provisioned for the supercomputer workloads. Defaults to LoadBalancer if not specified. If None is specified, the customer is responsible for providing outbound connectivity for Supercomputer functionality. Known values are: "LoadBalancer" and "None". (LoadBalancer, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>System Subnet ID associated with managed NodePool for system resources. It should have connectivity to the child NodePool subnets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSku" /></td>
    <td><code>string</code></td>
    <td>The SKU to use for the system node pool. Known values are: "Standard_D4s_v6", "Standard_D4s_v5", and "Standard_D4s_v4". (Standard_D4s_v6, Standard_D4s_v5, Standard_D4s_v4)</td>
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
    <td><CopyableCode code="customerManagedKeys" /></td>
    <td><code>string</code></td>
    <td>Whether or not to use a customer managed key when encrypting data at rest. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetId" /></td>
    <td><code>string</code></td>
    <td>Disk Encryption Set ID to use for Customer Managed Keys encryption. Required if Customer Managed Keys is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="identities" /></td>
    <td><code>object</code></td>
    <td>Dictionary of identity properties. Required.</td>
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
    <td><CopyableCode code="managementSubnetId" /></td>
    <td><code>string</code></td>
    <td>System Subnet ID associated with AKS apiserver. Must be delegated to Microsoft.ContainerService/managedClusters. It should have connectivity to the system subnet and nodepool subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundType" /></td>
    <td><code>string</code></td>
    <td>Network egress type provisioned for the supercomputer workloads. Defaults to LoadBalancer if not specified. If None is specified, the customer is responsible for providing outbound connectivity for Supercomputer functionality. Known values are: "LoadBalancer" and "None". (LoadBalancer, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>System Subnet ID associated with managed NodePool for system resources. It should have connectivity to the child NodePool subnets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSku" /></td>
    <td><code>string</code></td>
    <td>The SKU to use for the system node pool. Known values are: "Standard_D4s_v6", "Standard_D4s_v5", and "Standard_D4s_v4". (Standard_D4s_v6, Standard_D4s_v5, Standard_D4s_v4)</td>
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
    <td><CopyableCode code="customerManagedKeys" /></td>
    <td><code>string</code></td>
    <td>Whether or not to use a customer managed key when encrypting data at rest. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="diskEncryptionSetId" /></td>
    <td><code>string</code></td>
    <td>Disk Encryption Set ID to use for Customer Managed Keys encryption. Required if Customer Managed Keys is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="identities" /></td>
    <td><code>object</code></td>
    <td>Dictionary of identity properties. Required.</td>
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
    <td><CopyableCode code="managementSubnetId" /></td>
    <td><code>string</code></td>
    <td>System Subnet ID associated with AKS apiserver. Must be delegated to Microsoft.ContainerService/managedClusters. It should have connectivity to the system subnet and nodepool subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundType" /></td>
    <td><code>string</code></td>
    <td>Network egress type provisioned for the supercomputer workloads. Defaults to LoadBalancer if not specified. If None is specified, the customer is responsible for providing outbound connectivity for Supercomputer functionality. Known values are: "LoadBalancer" and "None". (LoadBalancer, None)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Accepted, Provisioning, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>System Subnet ID associated with managed NodePool for system resources. It should have connectivity to the child NodePool subnets. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSku" /></td>
    <td><code>string</code></td>
    <td>The SKU to use for the system node pool. Known values are: "Standard_D4s_v6", "Standard_D4s_v5", and "Standard_D4s_v4". (Standard_D4s_v6, Standard_D4s_v5, Standard_D4s_v4)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Supercomputer.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Supercomputer resources by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Supercomputer resources by subscription ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a Supercomputer.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Update a Supercomputer.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a Supercomputer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-supercomputer_name"><code>supercomputer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Supercomputer.</td>
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
<tr id="parameter-supercomputer_name">
    <td><CopyableCode code="supercomputer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Supercomputer. Required.</td>
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

Get a Supercomputer.

```sql
SELECT
id,
name,
customerManagedKeys,
diskEncryptionSetId,
identities,
location,
logAnalyticsClusterId,
managedOnBehalfOfConfiguration,
managedResourceGroup,
managementSubnetId,
outboundType,
provisioningState,
subnetId,
systemData,
systemSku,
tags,
type
FROM azure.discovery.supercomputers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND supercomputer_name = '{{ supercomputer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List Supercomputer resources by resource group.

```sql
SELECT
id,
name,
customerManagedKeys,
diskEncryptionSetId,
identities,
location,
logAnalyticsClusterId,
managedOnBehalfOfConfiguration,
managedResourceGroup,
managementSubnetId,
outboundType,
provisioningState,
subnetId,
systemData,
systemSku,
tags,
type
FROM azure.discovery.supercomputers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List Supercomputer resources by subscription ID.

```sql
SELECT
id,
name,
customerManagedKeys,
diskEncryptionSetId,
identities,
location,
logAnalyticsClusterId,
managedOnBehalfOfConfiguration,
managedResourceGroup,
managementSubnetId,
outboundType,
provisioningState,
subnetId,
systemData,
systemSku,
tags,
type
FROM azure.discovery.supercomputers
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

Create a Supercomputer.

```sql
INSERT INTO azure.discovery.supercomputers (
tags,
location,
properties,
resource_group_name,
supercomputer_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ supercomputer_name }}',
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
- name: supercomputers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the supercomputers resource.
    - name: supercomputer_name
      value: "{{ supercomputer_name }}"
      description: Required parameter for the supercomputers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the supercomputers resource.
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
        subnetId: "{{ subnetId }}"
        managementSubnetId: "{{ managementSubnetId }}"
        outboundType: "{{ outboundType }}"
        systemSku: "{{ systemSku }}"
        identities:
          clusterIdentity:
            id: "{{ id }}"
            principalId: "{{ principalId }}"
            clientId: "{{ clientId }}"
          kubeletIdentity:
            id: "{{ id }}"
            principalId: "{{ principalId }}"
            clientId: "{{ clientId }}"
          workloadIdentities: "{{ workloadIdentities }}"
        customerManagedKeys: "{{ customerManagedKeys }}"
        diskEncryptionSetId: "{{ diskEncryptionSetId }}"
        logAnalyticsClusterId: "{{ logAnalyticsClusterId }}"
        managedResourceGroup: "{{ managedResourceGroup }}"
        managedOnBehalfOfConfiguration:
          moboBrokerResources:
            - id: "{{ id }}"
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

Update a Supercomputer.

```sql
UPDATE azure.discovery.supercomputers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND supercomputer_name = '{{ supercomputer_name }}' --required
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

Create a Supercomputer.

```sql
REPLACE azure.discovery.supercomputers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND supercomputer_name = '{{ supercomputer_name }}' --required
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

Delete a Supercomputer.

```sql
DELETE FROM azure.discovery.supercomputers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND supercomputer_name = '{{ supercomputer_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
