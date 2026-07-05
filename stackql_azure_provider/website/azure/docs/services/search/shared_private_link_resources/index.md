--- 
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
  - search
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

Creates, updates, deletes, gets or lists a <code>shared_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="shared_private_link_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.shared_private_link_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
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
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The group ID from the provider of resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the shared private link resource. Valid values are Updating, Deleting, Failed, Succeeded or Incomplete. Known values are: "Updating", "Deleting", "Failed", "Succeeded", and "Incomplete". (Updating, Deleting, Failed, Succeeded, Incomplete)</td>
</tr>
<tr>
    <td><CopyableCode code="requestMessage" /></td>
    <td><code>string</code></td>
    <td>The message for requesting approval of the shared private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRegion" /></td>
    <td><code>string</code></td>
    <td>Optional. Can be used to specify the Azure Resource Manager location of the resource for which a shared private link is being created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the shared private link resource. Valid values are Pending, Approved, Rejected or Disconnected. Known values are: "Pending", "Approved", "Rejected", and "Disconnected". (Pending, Approved, Rejected, Disconnected)</td>
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
<TabItem value="list_by_service">

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
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The group ID from the provider of resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkResourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the resource the shared private link resource is for.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the shared private link resource. Valid values are Updating, Deleting, Failed, Succeeded or Incomplete. Known values are: "Updating", "Deleting", "Failed", "Succeeded", and "Incomplete". (Updating, Deleting, Failed, Succeeded, Incomplete)</td>
</tr>
<tr>
    <td><CopyableCode code="requestMessage" /></td>
    <td><code>string</code></td>
    <td>The message for requesting approval of the shared private link resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRegion" /></td>
    <td><code>string</code></td>
    <td>Optional. Can be used to specify the Azure Resource Manager location of the resource for which a shared private link is being created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the shared private link resource. Valid values are Pending, Approved, Rejected or Disconnected. Known values are: "Pending", "Approved", "Rejected", and "Disconnected". (Pending, Approved, Rejected, Disconnected)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the shared private link resource managed by the search service in the given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_service"><CopyableCode code="list_by_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all shared private link resources managed by the given service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiates the creation or update of a shared private link resource managed by the search service in the given resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiates the creation or update of a shared private link resource managed by the search service in the given resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-shared_private_link_resource_name"><code>shared_private_link_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiates the deletion of the shared private link resource from the search service. Returns 202 (Accepted) for asynchronous deletion, 204 (No Content) if the service exists but the shared private link is not found, or 404 (Not Found) if the service is not found. NOTE: The behavior of returning 404 is inconsistent with ARM guidelines. Clients should expect a 204 response in future versions and avoid new dependencies on the 404 response.</td>
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
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure AI Search service associated with the specified resource group. Required.</td>
</tr>
<tr id="parameter-shared_private_link_resource_name">
    <td><CopyableCode code="shared_private_link_resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the shared private link resource managed by the Azure AI Search service within the specified resource group. Required.</td>
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
        { label: 'list_by_service', value: 'list_by_service' }
    ]}
>
<TabItem value="get">

Gets the details of the shared private link resource managed by the search service in the given resource group.

```sql
SELECT
id,
name,
groupId,
privateLinkResourceId,
provisioningState,
requestMessage,
resourceRegion,
status,
systemData,
type
FROM azure.search.shared_private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND search_service_name = '{{ search_service_name }}' -- required
AND shared_private_link_resource_name = '{{ shared_private_link_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_service">

Gets a list of all shared private link resources managed by the given service.

```sql
SELECT
id,
name,
groupId,
privateLinkResourceId,
provisioningState,
requestMessage,
resourceRegion,
status,
systemData,
type
FROM azure.search.shared_private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND search_service_name = '{{ search_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Initiates the creation or update of a shared private link resource managed by the search service in the given resource group.

```sql
INSERT INTO azure.search.shared_private_link_resources (
properties,
resource_group_name,
search_service_name,
shared_private_link_resource_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ search_service_name }}',
'{{ shared_private_link_resource_name }}',
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
- name: shared_private_link_resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the shared_private_link_resources resource.
    - name: search_service_name
      value: "{{ search_service_name }}"
      description: Required parameter for the shared_private_link_resources resource.
    - name: shared_private_link_resource_name
      value: "{{ shared_private_link_resource_name }}"
      description: Required parameter for the shared_private_link_resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the shared_private_link_resources resource.
    - name: properties
      description: |
        Describes the properties of a shared private link resource managed by the Azure AI Search service.
      value:
        privateLinkResourceId: "{{ privateLinkResourceId }}"
        groupId: "{{ groupId }}"
        requestMessage: "{{ requestMessage }}"
        resourceRegion: "{{ resourceRegion }}"
        status: "{{ status }}"
        provisioningState: "{{ provisioningState }}"
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

Initiates the creation or update of a shared private link resource managed by the search service in the given resource group.

```sql
REPLACE azure.search.shared_private_link_resources
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND search_service_name = '{{ search_service_name }}' --required
AND shared_private_link_resource_name = '{{ shared_private_link_resource_name }}' --required
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

Initiates the deletion of the shared private link resource from the search service. Returns 202 (Accepted) for asynchronous deletion, 204 (No Content) if the service exists but the shared private link is not found, or 404 (Not Found) if the service is not found. NOTE: The behavior of returning 404 is inconsistent with ARM guidelines. Clients should expect a 204 response in future versions and avoid new dependencies on the 404 response.

```sql
DELETE FROM azure.search.shared_private_link_resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND search_service_name = '{{ search_service_name }}' --required
AND shared_private_link_resource_name = '{{ shared_private_link_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
