--- 
title: cassandra_data_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_data_centers
  - cosmosdb
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

Creates, updates, deletes, gets or lists a <code>cassandra_data_centers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cassandra_data_centers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmosdb.cassandra_data_centers" /></td></tr>
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
    <td><CopyableCode code="authenticationMethodLdapProperties" /></td>
    <td><code>object</code></td>
    <td>Ldap authentication method properties. This feature is in preview.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>boolean</code></td>
    <td>If the data center has Availability Zone support, apply it to the Virtual Machine ScaleSet that host the cassandra data center virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageCustomerKeyUri" /></td>
    <td><code>string</code></td>
    <td>Indicates the Key Uri of the customer key to use for encryption of the backup storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="base64EncodedCassandraYamlFragment" /></td>
    <td><code>string</code></td>
    <td>A fragment of a cassandra.yaml configuration file to be included in the cassandra.yaml for all nodes in this data center. The fragment should be Base64 encoded, and only a subset of keys are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCenterLocation" /></td>
    <td><code>string</code></td>
    <td>The region this data center should be created in.</td>
</tr>
<tr>
    <td><CopyableCode code="deallocated" /></td>
    <td><code>boolean</code></td>
    <td>Whether the data center has been deallocated.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetId" /></td>
    <td><code>string</code></td>
    <td>Resource id of a subnet the nodes in this data center should have their network interfaces connected to. The subnet must be in the same region specified in 'dataCenterLocation' and must be able to route to the subnet specified in the cluster's 'delegatedManagementSubnetId' property. This resource id will be of the form '/subscriptions//resourceGroups//providers/Microsoft.Network/virtualNetworks//subnets/'.</td>
</tr>
<tr>
    <td><CopyableCode code="diskCapacity" /></td>
    <td><code>integer</code></td>
    <td>Number of disks attached to each node. Default is 4.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSku" /></td>
    <td><code>string</code></td>
    <td>Disk SKU used for data centers. Default value is P30.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDiskCustomerKeyUri" /></td>
    <td><code>string</code></td>
    <td>Key uri to use for encryption of managed disks. Ensure the system assigned identity of the cluster has been assigned appropriate permissions(key get/wrap/unwrap permissions) on the key.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes the data center should have. This is the desired number. After it is set, it may take some time for the data center to be scaled to match. To monitor the number of nodes and their status, use the fetchNodeStatus method on the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>Ip of the VPN Endpoint for this data center.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionError" /></td>
    <td><code>object</code></td>
    <td>CassandraError.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the resource at the time the operation was called. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="seedNodes" /></td>
    <td><code>array</code></td>
    <td>IP addresses for seed nodes in this data center. This is for reference. Generally you will want to use the seedNodes property on the cluster, which aggregates the seed nodes from all data centers in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine SKU used for data centers. Default value is Standard_DS14_v2.</td>
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
    <td><CopyableCode code="authenticationMethodLdapProperties" /></td>
    <td><code>object</code></td>
    <td>Ldap authentication method properties. This feature is in preview.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityZone" /></td>
    <td><code>boolean</code></td>
    <td>If the data center has Availability Zone support, apply it to the Virtual Machine ScaleSet that host the cassandra data center virtual machines.</td>
</tr>
<tr>
    <td><CopyableCode code="backupStorageCustomerKeyUri" /></td>
    <td><code>string</code></td>
    <td>Indicates the Key Uri of the customer key to use for encryption of the backup storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="base64EncodedCassandraYamlFragment" /></td>
    <td><code>string</code></td>
    <td>A fragment of a cassandra.yaml configuration file to be included in the cassandra.yaml for all nodes in this data center. The fragment should be Base64 encoded, and only a subset of keys are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCenterLocation" /></td>
    <td><code>string</code></td>
    <td>The region this data center should be created in.</td>
</tr>
<tr>
    <td><CopyableCode code="deallocated" /></td>
    <td><code>boolean</code></td>
    <td>Whether the data center has been deallocated.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedSubnetId" /></td>
    <td><code>string</code></td>
    <td>Resource id of a subnet the nodes in this data center should have their network interfaces connected to. The subnet must be in the same region specified in 'dataCenterLocation' and must be able to route to the subnet specified in the cluster's 'delegatedManagementSubnetId' property. This resource id will be of the form '/subscriptions//resourceGroups//providers/Microsoft.Network/virtualNetworks//subnets/'.</td>
</tr>
<tr>
    <td><CopyableCode code="diskCapacity" /></td>
    <td><code>integer</code></td>
    <td>Number of disks attached to each node. Default is 4.</td>
</tr>
<tr>
    <td><CopyableCode code="diskSku" /></td>
    <td><code>string</code></td>
    <td>Disk SKU used for data centers. Default value is P30.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDiskCustomerKeyUri" /></td>
    <td><code>string</code></td>
    <td>Key uri to use for encryption of managed disks. Ensure the system assigned identity of the cluster has been assigned appropriate permissions(key get/wrap/unwrap permissions) on the key.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeCount" /></td>
    <td><code>integer</code></td>
    <td>The number of nodes the data center should have. This is the desired number. After it is set, it may take some time for the data center to be scaled to match. To monitor the number of nodes and their status, use the fetchNodeStatus method on the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointIpAddress" /></td>
    <td><code>string</code></td>
    <td>Ip of the VPN Endpoint for this data center.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionError" /></td>
    <td><code>object</code></td>
    <td>CassandraError.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the resource at the time the operation was called. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Failed", and "Canceled". (Creating, Updating, Deleting, Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="seedNodes" /></td>
    <td><code>array</code></td>
    <td>IP addresses for seed nodes in this data center. This is for reference. Generally you will want to use the seedNodes property on the cluster, which aggregates the seed nodes from all data centers in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Virtual Machine SKU used for data centers. Default value is Standard_DS14_v2.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-data_center_name"><code>data_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of a managed Cassandra data center.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all data centers in a particular managed Cassandra cluster.</td>
</tr>
<tr>
    <td><a href="#create_update"><CopyableCode code="create_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-data_center_name"><code>data_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-data_center_name"><code>data_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update some of the properties of a managed Cassandra data center.</td>
</tr>
<tr>
    <td><a href="#create_update"><CopyableCode code="create_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-data_center_name"><code>data_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-data_center_name"><code>data_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a managed Cassandra data center.</td>
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
    <td>Managed Cassandra cluster name. Required.</td>
</tr>
<tr id="parameter-data_center_name">
    <td><CopyableCode code="data_center_name" /></td>
    <td><code>string</code></td>
    <td>Data center name in a managed Cassandra cluster. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the properties of a managed Cassandra data center.

```sql
SELECT
id,
name,
authenticationMethodLdapProperties,
availabilityZone,
backupStorageCustomerKeyUri,
base64EncodedCassandraYamlFragment,
dataCenterLocation,
deallocated,
delegatedSubnetId,
diskCapacity,
diskSku,
managedDiskCustomerKeyUri,
nodeCount,
privateEndpointIpAddress,
provisionError,
provisioningState,
seedNodes,
sku,
systemData,
type
FROM azure.cosmosdb.cassandra_data_centers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND data_center_name = '{{ data_center_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all data centers in a particular managed Cassandra cluster.

```sql
SELECT
id,
name,
authenticationMethodLdapProperties,
availabilityZone,
backupStorageCustomerKeyUri,
base64EncodedCassandraYamlFragment,
dataCenterLocation,
deallocated,
delegatedSubnetId,
diskCapacity,
diskSku,
managedDiskCustomerKeyUri,
nodeCount,
privateEndpointIpAddress,
provisionError,
provisioningState,
seedNodes,
sku,
systemData,
type
FROM azure.cosmosdb.cassandra_data_centers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_update"
    values={[
        { label: 'create_update', value: 'create_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_update">

Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH.

```sql
INSERT INTO azure.cosmosdb.cassandra_data_centers (
properties,
resource_group_name,
cluster_name,
data_center_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ data_center_name }}',
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
- name: cassandra_data_centers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cassandra_data_centers resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the cassandra_data_centers resource.
    - name: data_center_name
      value: "{{ data_center_name }}"
      description: Required parameter for the cassandra_data_centers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cassandra_data_centers resource.
    - name: properties
      description: |
        Properties of a managed Cassandra data center.
      value:
        provisioningState: "{{ provisioningState }}"
        dataCenterLocation: "{{ dataCenterLocation }}"
        delegatedSubnetId: "{{ delegatedSubnetId }}"
        nodeCount: {{ nodeCount }}
        seedNodes:
          - ipAddress: "{{ ipAddress }}"
        base64EncodedCassandraYamlFragment: "{{ base64EncodedCassandraYamlFragment }}"
        managedDiskCustomerKeyUri: "{{ managedDiskCustomerKeyUri }}"
        backupStorageCustomerKeyUri: "{{ backupStorageCustomerKeyUri }}"
        sku: "{{ sku }}"
        diskSku: "{{ diskSku }}"
        diskCapacity: {{ diskCapacity }}
        availabilityZone: {{ availabilityZone }}
        authenticationMethodLdapProperties:
          serverHostname: "{{ serverHostname }}"
          serverPort: {{ serverPort }}
          serviceUserDistinguishedName: "{{ serviceUserDistinguishedName }}"
          serviceUserPassword: "{{ serviceUserPassword }}"
          searchBaseDistinguishedName: "{{ searchBaseDistinguishedName }}"
          searchFilterTemplate: "{{ searchFilterTemplate }}"
          serverCertificates:
            - pem: "{{ pem }}"
          connectionTimeoutInMs: {{ connectionTimeoutInMs }}
        deallocated: {{ deallocated }}
        provisionError:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          additionalErrorInfo: "{{ additionalErrorInfo }}"
        privateEndpointIpAddress: "{{ privateEndpointIpAddress }}"
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

Update some of the properties of a managed Cassandra data center.

```sql
UPDATE azure.cosmosdb.cassandra_data_centers
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND data_center_name = '{{ data_center_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_update"
    values={[
        { label: 'create_update', value: 'create_update' }
    ]}
>
<TabItem value="create_update">

Create or update a managed Cassandra data center. When updating, overwrite all properties. To update only some properties, use PATCH.

```sql
REPLACE azure.cosmosdb.cassandra_data_centers
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND data_center_name = '{{ data_center_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a managed Cassandra data center.

```sql
DELETE FROM azure.cosmosdb.cassandra_data_centers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND data_center_name = '{{ data_center_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
