--- 
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.namespaces" /></td></tr>
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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Namespace resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isZoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>This is an optional property and it allows the user to specify if the namespace resource supports zone-redundancy capability or not. If this property is not specified explicitly by the user, its default value depends on the following conditions: a. For Availability Zones enabled regions - The default property value would be true. b. For non-Availability Zones enabled regions - The default property value would be false. Once specified, this property cannot be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the namespace resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "Deleted", "DeleteFailed", "CreateFailed", and "UpdatedFailed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, Deleted, DeleteFailed, CreateFailed, UpdatedFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Represents available Sku pricing tiers.</td>
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
    <td><CopyableCode code="topicSpacesConfiguration" /></td>
    <td><code>object</code></td>
    <td>Topic spaces configuration information for the namespace resource.</td>
</tr>
<tr>
    <td><CopyableCode code="topicsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Topics configuration information for the namespace resource.</td>
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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Namespace resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isZoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>This is an optional property and it allows the user to specify if the namespace resource supports zone-redundancy capability or not. If this property is not specified explicitly by the user, its default value depends on the following conditions: a. For Availability Zones enabled regions - The default property value would be true. b. For non-Availability Zones enabled regions - The default property value would be false. Once specified, this property cannot be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the namespace resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "Deleted", "DeleteFailed", "CreateFailed", and "UpdatedFailed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, Deleted, DeleteFailed, CreateFailed, UpdatedFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Represents available Sku pricing tiers.</td>
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
    <td><CopyableCode code="topicSpacesConfiguration" /></td>
    <td><code>object</code></td>
    <td>Topic spaces configuration information for the namespace resource.</td>
</tr>
<tr>
    <td><CopyableCode code="topicsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Topics configuration information for the namespace resource.</td>
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
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity information for the Namespace resource.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundIpRules" /></td>
    <td><code>array</code></td>
    <td>This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isZoneRedundant" /></td>
    <td><code>boolean</code></td>
    <td>This is an optional property and it allows the user to specify if the namespace resource supports zone-redundancy capability or not. If this property is not specified explicitly by the user, its default value depends on the following conditions: a. For Availability Zones enabled regions - The default property value would be true. b. For non-Availability Zones enabled regions - The default property value would be false. Once specified, this property cannot be updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="minimumTlsVersionAllowed" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported. Known values are: "1.0", "1.1", and "1.2". (1.0, 1.1, 1.2)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>List of private endpoint connections.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the namespace resource. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", "Failed", "Deleted", "DeleteFailed", "CreateFailed", and "UpdatedFailed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed, Deleted, DeleteFailed, CreateFailed, UpdatedFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring . Known values are: "Enabled", "Disabled", and "SecuredByPerimeter". (Enabled, Disabled, SecuredByPerimeter)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Represents available Sku pricing tiers.</td>
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
    <td><CopyableCode code="topicSpacesConfiguration" /></td>
    <td><code>object</code></td>
    <td>Topic spaces configuration information for the namespace resource.</td>
</tr>
<tr>
    <td><CopyableCode code="topicsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Topics configuration information for the namespace resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a namespace. Get properties of a namespace.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List namespaces under a resource group. List all the namespaces under a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>List namespaces under an Azure subscription. List all the namespaces under an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a namespace. Asynchronously creates or updates a new namespace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a namespace. Asynchronously updates a namespace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a namespace. Asynchronously creates or updates a new namespace with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a namespace. Delete existing namespace.</td>
</tr>
<tr>
    <td><a href="#list_shared_access_keys"><CopyableCode code="list_shared_access_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List keys for a namespace. List the two keys used to publish to a namespace.</td>
</tr>
<tr>
    <td><a href="#regenerate_key"><CopyableCode code="regenerate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyName"><code>keyName</code></a></td>
    <td></td>
    <td>Regenerate key for a namespace. Regenerate a shared access key for a namespace.</td>
</tr>
<tr>
    <td><a href="#validate_custom_domain_ownership"><CopyableCode code="validate_custom_domain_ownership" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validate ownership for all custom domains in a namespace. Performs ownership validation via checking TXT records for all custom domains in a namespace.</td>
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
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the namespace. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. Default value is None.</td>
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

Get a namespace. Get properties of a namespace.

```sql
SELECT
id,
name,
identity,
inboundIpRules,
isZoneRedundant,
location,
minimumTlsVersionAllowed,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
topicSpacesConfiguration,
topicsConfiguration,
type
FROM azure.event_grid.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List namespaces under a resource group. List all the namespaces under a resource group.

```sql
SELECT
id,
name,
identity,
inboundIpRules,
isZoneRedundant,
location,
minimumTlsVersionAllowed,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
topicSpacesConfiguration,
topicsConfiguration,
type
FROM azure.event_grid.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

List namespaces under an Azure subscription. List all the namespaces under an Azure subscription.

```sql
SELECT
id,
name,
identity,
inboundIpRules,
isZoneRedundant,
location,
minimumTlsVersionAllowed,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
sku,
systemData,
tags,
topicSpacesConfiguration,
topicsConfiguration,
type
FROM azure.event_grid.namespaces
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create or update a namespace. Asynchronously creates or updates a new namespace with the specified parameters.

```sql
INSERT INTO azure.event_grid.namespaces (
tags,
location,
properties,
sku,
identity,
resource_group_name,
namespace_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: namespaces
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the namespaces resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the namespaces resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the namespaces resource.
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
        Properties of the Namespace resource.
      value:
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
              privateEndpoint:
                id: "{{ id }}"
              groupIds:
                - "{{ groupIds }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        provisioningState: "{{ provisioningState }}"
        topicsConfiguration:
          hostname: "{{ hostname }}"
          customDomains:
            - fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
              validationState: "{{ validationState }}"
              identity:
                type: "{{ type }}"
                userAssignedIdentity: "{{ userAssignedIdentity }}"
              certificateUrl: "{{ certificateUrl }}"
              expectedTxtRecordName: "{{ expectedTxtRecordName }}"
              expectedTxtRecordValue: "{{ expectedTxtRecordValue }}"
        topicSpacesConfiguration:
          state: "{{ state }}"
          routeTopicResourceId: "{{ routeTopicResourceId }}"
          hostname: "{{ hostname }}"
          routingEnrichments:
            static:
              - key: "{{ key }}"
                valueType: "{{ valueType }}"
            dynamic:
              - key: "{{ key }}"
                value: "{{ value }}"
          clientAuthentication:
            alternativeAuthenticationNameSources:
              - "{{ alternativeAuthenticationNameSources }}"
            customJwtAuthentication:
              tokenIssuer: "{{ tokenIssuer }}"
              issuerCertificates:
                - certificateUrl: "{{ certificateUrl }}"
                  identity:
                    type: "{{ type }}"
                    userAssignedIdentity: "{{ userAssignedIdentity }}"
              encodedIssuerCertificates:
                - kid: "{{ kid }}"
                  encodedCertificate: "{{ encodedCertificate }}"
            webhookAuthentication:
              identity:
                type: "{{ type }}"
                userAssignedIdentity: "{{ userAssignedIdentity }}"
              endpointUrl: "{{ endpointUrl }}"
              endpointBaseUrl: "{{ endpointBaseUrl }}"
              azureActiveDirectoryApplicationIdOrUri: "{{ azureActiveDirectoryApplicationIdOrUri }}"
              azureActiveDirectoryTenantId: "{{ azureActiveDirectoryTenantId }}"
          maximumSessionExpiryInHours: {{ maximumSessionExpiryInHours }}
          maximumClientSessionsPerAuthenticationName: {{ maximumClientSessionsPerAuthenticationName }}
          routingIdentityInfo:
            type: "{{ type }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          customDomains:
            - fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
              validationState: "{{ validationState }}"
              identity:
                type: "{{ type }}"
                userAssignedIdentity: "{{ userAssignedIdentity }}"
              certificateUrl: "{{ certificateUrl }}"
              expectedTxtRecordName: "{{ expectedTxtRecordName }}"
              expectedTxtRecordValue: "{{ expectedTxtRecordValue }}"
        isZoneRedundant: {{ isZoneRedundant }}
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        inboundIpRules:
          - ipMask: "{{ ipMask }}"
            action: "{{ action }}"
        minimumTlsVersionAllowed: "{{ minimumTlsVersionAllowed }}"
    - name: sku
      description: |
        Represents available Sku pricing tiers.
      value:
        name: "{{ name }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Identity information for the Namespace resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
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

Update a namespace. Asynchronously updates a namespace with the specified parameters.

```sql
UPDATE azure.event_grid.namespaces
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Create or update a namespace. Asynchronously creates or updates a new namespace with the specified parameters.

```sql
REPLACE azure.event_grid.namespaces
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Delete a namespace. Delete existing namespace.

```sql
DELETE FROM azure.event_grid.namespaces
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_shared_access_keys"
    values={[
        { label: 'list_shared_access_keys', value: 'list_shared_access_keys' },
        { label: 'regenerate_key', value: 'regenerate_key' },
        { label: 'validate_custom_domain_ownership', value: 'validate_custom_domain_ownership' }
    ]}
>
<TabItem value="list_shared_access_keys">

List keys for a namespace. List the two keys used to publish to a namespace.

```sql
EXEC azure.event_grid.namespaces.list_shared_access_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="regenerate_key">

Regenerate key for a namespace. Regenerate a shared access key for a namespace.

```sql
EXEC azure.event_grid.namespaces.regenerate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyName": "{{ keyName }}"
}'
;
```
</TabItem>
<TabItem value="validate_custom_domain_ownership">

Validate ownership for all custom domains in a namespace. Performs ownership validation via checking TXT records for all custom domains in a namespace.

```sql
EXEC azure.event_grid.namespaces.validate_custom_domain_ownership 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
