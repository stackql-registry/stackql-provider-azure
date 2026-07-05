--- 
title: network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - network_connections
  - devcenter
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

Creates, updates, deletes, gets or lists a <code>network_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.network_connections" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="domainJoinType" /></td>
    <td><code>string</code></td>
    <td>AAD Join type. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>Active Directory domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainPassword" /></td>
    <td><code>string</code></td>
    <td>The password for the account used to join domain.</td>
</tr>
<tr>
    <td><CopyableCode code="domainUsername" /></td>
    <td><code>string</code></td>
    <td>The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the network connection. Health checks are run on creation, update, and periodically to validate the network connection. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkingResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>The name for resource group where NICs will be placed.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationUnit" /></td>
    <td><code>string</code></td>
    <td>Active Directory domain Organization Unit (OU).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The subnet to attach Virtual Machines to.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="domainJoinType" /></td>
    <td><code>string</code></td>
    <td>AAD Join type. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>Active Directory domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainPassword" /></td>
    <td><code>string</code></td>
    <td>The password for the account used to join domain.</td>
</tr>
<tr>
    <td><CopyableCode code="domainUsername" /></td>
    <td><code>string</code></td>
    <td>The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the network connection. Health checks are run on creation, update, and periodically to validate the network connection. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkingResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>The name for resource group where NICs will be placed.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationUnit" /></td>
    <td><code>string</code></td>
    <td>Active Directory domain Organization Unit (OU).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The subnet to attach Virtual Machines to.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;". # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="domainJoinType" /></td>
    <td><code>string</code></td>
    <td>AAD Join type. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="domainName" /></td>
    <td><code>string</code></td>
    <td>Active Directory domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainPassword" /></td>
    <td><code>string</code></td>
    <td>The password for the account used to join domain.</td>
</tr>
<tr>
    <td><CopyableCode code="domainUsername" /></td>
    <td><code>string</code></td>
    <td>The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Overall health status of the network connection. Health checks are run on creation, update, and periodically to validate the network connection. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="networkingResourceGroupName" /></td>
    <td><code>string</code></td>
    <td>The name for resource group where NICs will be placed.</td>
</tr>
<tr>
    <td><CopyableCode code="organizationUnit" /></td>
    <td><code>string</code></td>
    <td>Active Directory domain Organization Unit (OU).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The subnet to attach Virtual Machines to.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a network connection resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists network connections in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists network connections in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Network Connections resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Partially updates a Network Connection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a Network Connections resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Network Connections resource.</td>
</tr>
<tr>
    <td><a href="#list_health_details"><CopyableCode code="list_health_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists health check status details.</td>
</tr>
<tr>
    <td><a href="#list_outbound_network_dependencies_endpoints"><CopyableCode code="list_outbound_network_dependencies_endpoints" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the endpoints that agents may call as part of Dev Box service administration. These FQDNs should be allowed for outbound access in order for the Dev Box service to function.</td>
</tr>
<tr>
    <td><a href="#get_health_details"><CopyableCode code="get_health_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets health check status details.</td>
</tr>
<tr>
    <td><a href="#run_health_checks"><CopyableCode code="run_health_checks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_connection_name"><code>network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Triggers a new health check run. The execution and health check result can be tracked via the network Connection health check details.</td>
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
<tr id="parameter-network_connection_name">
    <td><CopyableCode code="network_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Network Connection that can be applied to a Pool. Required.</td>
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
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
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

Gets a network connection resource.

```sql
SELECT
id,
name,
domainJoinType,
domainName,
domainPassword,
domainUsername,
healthCheckStatus,
location,
networkingResourceGroupName,
organizationUnit,
provisioningState,
subnetId,
systemData,
tags,
type
FROM azure.devcenter.network_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_connection_name = '{{ network_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists network connections in a resource group.

```sql
SELECT
id,
name,
domainJoinType,
domainName,
domainPassword,
domainUsername,
healthCheckStatus,
location,
networkingResourceGroupName,
organizationUnit,
provisioningState,
subnetId,
systemData,
tags,
type
FROM azure.devcenter.network_connections
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists network connections in a subscription.

```sql
SELECT
id,
name,
domainJoinType,
domainName,
domainPassword,
domainUsername,
healthCheckStatus,
location,
networkingResourceGroupName,
organizationUnit,
provisioningState,
subnetId,
systemData,
tags,
type
FROM azure.devcenter.network_connections
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
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

Creates or updates a Network Connections resource.

```sql
INSERT INTO azure.devcenter.network_connections (
tags,
location,
properties,
resource_group_name,
network_connection_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_connection_name }}',
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
- name: network_connections
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_connections resource.
    - name: network_connection_name
      value: "{{ network_connection_name }}"
      description: Required parameter for the network_connections resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_connections resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        subnetId: "{{ subnetId }}"
        domainName: "{{ domainName }}"
        organizationUnit: "{{ organizationUnit }}"
        domainUsername: "{{ domainUsername }}"
        domainPassword: "{{ domainPassword }}"
        networkingResourceGroupName: "{{ networkingResourceGroupName }}"
        domainJoinType: "{{ domainJoinType }}"
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

Partially updates a Network Connection.

```sql
UPDATE azure.devcenter.network_connections
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_connection_name = '{{ network_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Creates or updates a Network Connections resource.

```sql
REPLACE azure.devcenter.network_connections
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_connection_name = '{{ network_connection_name }}' --required
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

Deletes a Network Connections resource.

```sql
DELETE FROM azure.devcenter.network_connections
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_connection_name = '{{ network_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_health_details"
    values={[
        { label: 'list_health_details', value: 'list_health_details' },
        { label: 'list_outbound_network_dependencies_endpoints', value: 'list_outbound_network_dependencies_endpoints' },
        { label: 'get_health_details', value: 'get_health_details' },
        { label: 'run_health_checks', value: 'run_health_checks' }
    ]}
>
<TabItem value="list_health_details">

Lists health check status details.

```sql
EXEC azure.devcenter.network_connections.list_health_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_connection_name='{{ network_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="list_outbound_network_dependencies_endpoints">

Lists the endpoints that agents may call as part of Dev Box service administration. These FQDNs should be allowed for outbound access in order for the Dev Box service to function.

```sql
EXEC azure.devcenter.network_connections.list_outbound_network_dependencies_endpoints 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_connection_name='{{ network_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$top='{{ $top }}'
;
```
</TabItem>
<TabItem value="get_health_details">

Gets health check status details.

```sql
EXEC azure.devcenter.network_connections.get_health_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_connection_name='{{ network_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_health_checks">

Triggers a new health check run. The execution and health check result can be tracked via the network Connection health check details.

```sql
EXEC azure.devcenter.network_connections.run_health_checks 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_connection_name='{{ network_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
