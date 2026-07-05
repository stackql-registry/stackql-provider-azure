--- 
title: attached_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_networks
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

Creates, updates, deletes, gets or lists an <code>attached_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="attached_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devcenter.attached_networks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_dev_center"
    values={[
        { label: 'get_by_dev_center', value: 'get_by_dev_center' },
        { label: 'get_by_project', value: 'get_by_project' },
        { label: 'list_by_project', value: 'list_by_project' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' }
    ]}
>
<TabItem value="get_by_dev_center">

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
    <td>AAD Join type of the network. This is populated based on the referenced Network Connection. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Health check status values. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the NetworkConnection you want to attach.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionLocation" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the NetworkConnection resource specified in 'networkConnectionResourceId' property lives.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
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
<TabItem value="get_by_project">

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
    <td>AAD Join type of the network. This is populated based on the referenced Network Connection. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Health check status values. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the NetworkConnection you want to attach.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionLocation" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the NetworkConnection resource specified in 'networkConnectionResourceId' property lives.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
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
<TabItem value="list_by_project">

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
    <td>AAD Join type of the network. This is populated based on the referenced Network Connection. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Health check status values. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the NetworkConnection you want to attach.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionLocation" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the NetworkConnection resource specified in 'networkConnectionResourceId' property lives.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
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
<TabItem value="list_by_dev_center">

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
    <td>AAD Join type of the network. This is populated based on the referenced Network Connection. Known values are: "HybridAzureADJoin" and "AzureADJoin".</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckStatus" /></td>
    <td><code>string</code></td>
    <td>Health check status values. Known values are: "Unknown", "Pending", "Running", "Passed", "Warning", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the NetworkConnection you want to attach.</td>
</tr>
<tr>
    <td><CopyableCode code="networkConnectionLocation" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the NetworkConnection resource specified in 'networkConnectionResourceId' property lives.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Known values are: "NotSpecified", "Accepted", "Running", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "Succeeded", "Failed", "Canceled", "MovingResources", "TransientFailure", "RolloutInProgress", and "StorageProvisioningFailed".</td>
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
    <td><a href="#get_by_dev_center"><CopyableCode code="get_by_dev_center" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-attached_network_connection_name"><code>attached_network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an attached NetworkConnection.</td>
</tr>
<tr>
    <td><a href="#get_by_project"><CopyableCode code="get_by_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-attached_network_connection_name"><code>attached_network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an attached NetworkConnection.</td>
</tr>
<tr>
    <td><a href="#list_by_project"><CopyableCode code="list_by_project" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the attached NetworkConnections for a Project.</td>
</tr>
<tr>
    <td><a href="#list_by_dev_center"><CopyableCode code="list_by_dev_center" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists the attached NetworkConnections for a DevCenter.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-attached_network_connection_name"><code>attached_network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an attached NetworkConnection.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-attached_network_connection_name"><code>attached_network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an attached NetworkConnection.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-dev_center_name"><code>dev_center_name</code></a>, <a href="#parameter-attached_network_connection_name"><code>attached_network_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Un-attach a NetworkConnection.</td>
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
<tr id="parameter-attached_network_connection_name">
    <td><CopyableCode code="attached_network_connection_name" /></td>
    <td><code>string</code></td>
    <td>The name of the attached NetworkConnection. Required.</td>
</tr>
<tr id="parameter-dev_center_name">
    <td><CopyableCode code="dev_center_name" /></td>
    <td><code>string</code></td>
    <td>The name of the devcenter. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The name of the project. Required.</td>
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
    defaultValue="get_by_dev_center"
    values={[
        { label: 'get_by_dev_center', value: 'get_by_dev_center' },
        { label: 'get_by_project', value: 'get_by_project' },
        { label: 'list_by_project', value: 'list_by_project' },
        { label: 'list_by_dev_center', value: 'list_by_dev_center' }
    ]}
>
<TabItem value="get_by_dev_center">

Gets an attached NetworkConnection.

```sql
SELECT
id,
name,
domainJoinType,
healthCheckStatus,
networkConnectionId,
networkConnectionLocation,
provisioningState,
systemData,
type
FROM azure.devcenter.attached_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND attached_network_connection_name = '{{ attached_network_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_project">

Gets an attached NetworkConnection.

```sql
SELECT
id,
name,
domainJoinType,
healthCheckStatus,
networkConnectionId,
networkConnectionLocation,
provisioningState,
systemData,
type
FROM azure.devcenter.attached_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND attached_network_connection_name = '{{ attached_network_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_project">

Lists the attached NetworkConnections for a Project.

```sql
SELECT
id,
name,
domainJoinType,
healthCheckStatus,
networkConnectionId,
networkConnectionLocation,
provisioningState,
systemData,
type
FROM azure.devcenter.attached_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_dev_center">

Lists the attached NetworkConnections for a DevCenter.

```sql
SELECT
id,
name,
domainJoinType,
healthCheckStatus,
networkConnectionId,
networkConnectionLocation,
provisioningState,
systemData,
type
FROM azure.devcenter.attached_networks
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND dev_center_name = '{{ dev_center_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates an attached NetworkConnection.

```sql
INSERT INTO azure.devcenter.attached_networks (
properties,
resource_group_name,
dev_center_name,
attached_network_connection_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ dev_center_name }}',
'{{ attached_network_connection_name }}',
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
- name: attached_networks
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the attached_networks resource.
    - name: dev_center_name
      value: "{{ dev_center_name }}"
      description: Required parameter for the attached_networks resource.
    - name: attached_network_connection_name
      value: "{{ attached_network_connection_name }}"
      description: Required parameter for the attached_networks resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the attached_networks resource.
    - name: properties
      value:
        networkConnectionId: "{{ networkConnectionId }}"
`}</CodeBlock>

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

Creates or updates an attached NetworkConnection.

```sql
REPLACE azure.devcenter.attached_networks
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND attached_network_connection_name = '{{ attached_network_connection_name }}' --required
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

Un-attach a NetworkConnection.

```sql
DELETE FROM azure.devcenter.attached_networks
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND dev_center_name = '{{ dev_center_name }}' --required
AND attached_network_connection_name = '{{ attached_network_connection_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
