--- 
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - resource
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'get_by_id', value: 'get_by_id' }
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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Resource extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ID of the resource that manages this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The resource-specific properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The changed time of the resource. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The created time of the resource. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Resource extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ID of the resource that manages this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The resource-specific properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The changed time of the resource. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The created time of the resource. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Resource extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ID of the resource that manages this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The resource-specific properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. This is only present if requested via the $expand query parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
<TabItem value="get_by_id">

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
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Resource extended location.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>ID of the resource that manages this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>The resource-specific properties for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the resources for a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Get all the resources in a subscription.</td>
</tr>
<tr>
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Gets a resource by ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_id"><CopyableCode code="create_or_update_by_id" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Create a resource by ID.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a resource.</td>
</tr>
<tr>
    <td><a href="#update_by_id"><CopyableCode code="update_by_id" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Update a resource by ID.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_id"><CopyableCode code="create_or_update_by_id" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Create a resource by ID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a resource.</td>
</tr>
<tr>
    <td><a href="#delete_by_id"><CopyableCode code="delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Deletes a resource by ID.</td>
</tr>
<tr>
    <td><a href="#check_existence"><CopyableCode code="check_existence" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_provider_namespace"><code>resource_provider_namespace</code></a>, <a href="#parameter-parent_resource_path"><code>parent_resource_path</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks whether a resource exists.</td>
</tr>
<tr>
    <td><a href="#check_existence_by_id"><CopyableCode code="check_existence_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Checks by ID whether a resource exists. This API currently works only for a limited set of Resource providers. In the event that a Resource provider does not implement this API, ARM will respond with a 405. The alternative then is to use the GET API to check for the existence of the resource.</td>
</tr>
<tr>
    <td><a href="#move_resources"><CopyableCode code="move_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-source_resource_group_name"><code>source_resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Moves resources from one resource group to another resource group. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes.</td>
</tr>
<tr>
    <td><a href="#validate_move_resources"><CopyableCode code="validate_move_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-source_resource_group_name"><code>source_resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Validates whether resources can be moved from one resource group to another resource group. This operation checks whether the specified resources can be moved to the target. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation.</td>
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
<tr id="parameter-parent_resource_path">
    <td><CopyableCode code="parent_resource_path" /></td>
    <td><code>string</code></td>
    <td>The parent resource identity. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group containing the resource to get. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource to check whether it exists. Required.</td>
</tr>
<tr id="parameter-resource_provider_namespace">
    <td><CopyableCode code="resource_provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The resource provider of the resource to check. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The resource type. Required.</td>
</tr>
<tr id="parameter-source_resource_group_name">
    <td><CopyableCode code="source_resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group to get. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of additional properties to be included in the response. Valid values include `createdTime`, `changedTime` and `provisioningState`. For example, `$expand=createdTime,changedTime`. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation.Filter comparison operators include `eq` (equals) and `ne` (not equals) and may be used with the following properties: `location`, `resourceType`, `name`, `resourceGroup`, `identity`, `identity/principalId`, `plan`, `plan/publisher`, `plan/product`, `plan/name`, `plan/version`, and `plan/promotionCode`.For example, to filter by a resource type, use `$filter=resourceType eq 'Microsoft.Network/virtualNetworks'``substringof(value, property)` can be used to filter for substrings of the following currently-supported properties: `name` and `resourceGroup`For example, to get all resources with 'demo' anywhere in the resource name, use `$filter=substringof('demo', name)`Multiple substring operations can also be combined using `and`/`or` operators.Note that any truncated number of results queried via `$top` may also not be compatible when using a filter.Resources can be filtered by tag names and values. For example, to filter for a tag name and value, use `$filter=tagName eq 'tag1' and tagValue eq 'Value1'`. Note that when resources are filtered by tag name and value, the original tags for each resource will not be returned in the results. Any list of additional properties queried via `$expand` may also not be compatible when filtering by tag names/values. For tag names only, resources can be filtered by prefix using the following syntax: `$filter=startswith(tagName, 'depart')`. This query will return all resources with a tag name prefixed by the phrase `depart` (i.e.`department`, `departureDate`, `departureTime`, etc.)Note that some properties can be combined when filtering resources, which include the following: `substringof() and/or resourceType`, `plan and plan/publisher and plan/name`, and `identity and identity/principalId`. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of recommendations per page if a paged version of this API is being used. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' },
        { label: 'get_by_id', value: 'get_by_id' }
    ]}
>
<TabItem value="get">

Gets a resource.

```sql
SELECT
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type
FROM azure.resource.resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' -- required
AND parent_resource_path = '{{ parent_resource_path }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all the resources for a resource group.

```sql
SELECT
id,
name,
changedTime,
createdTime,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.resource.resources
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list">

Get all the resources in a subscription.

```sql
SELECT
id,
name,
changedTime,
createdTime,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
provisioningState,
sku,
systemData,
tags,
type
FROM azure.resource.resources
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_by_id">

Gets a resource by ID.

```sql
SELECT
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type
FROM azure.resource.resources
WHERE resource_id = '{{ resource_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_by_id', value: 'create_or_update_by_id' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates a resource.

```sql
INSERT INTO azure.resource.resources (
properties,
plan,
kind,
managedBy,
sku,
identity,
location,
extendedLocation,
tags,
resource_group_name,
resource_provider_namespace,
parent_resource_path,
resource_type,
resource_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ plan }}',
'{{ kind }}',
'{{ managedBy }}',
'{{ sku }}',
'{{ identity }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ resource_provider_namespace }}',
'{{ parent_resource_path }}',
'{{ resource_type }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_by_id">

Create a resource by ID.

```sql
INSERT INTO azure.resource.resources (
properties,
plan,
kind,
managedBy,
sku,
identity,
location,
extendedLocation,
tags,
resource_id
)
SELECT 
'{{ properties }}',
'{{ plan }}',
'{{ kind }}',
'{{ managedBy }}',
'{{ sku }}',
'{{ identity }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ resource_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
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
- name: resources
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the resources resource.
    - name: resource_provider_namespace
      value: "{{ resource_provider_namespace }}"
      description: Required parameter for the resources resource.
    - name: parent_resource_path
      value: "{{ parent_resource_path }}"
      description: Required parameter for the resources resource.
    - name: resource_type
      value: "{{ resource_type }}"
      description: Required parameter for the resources resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the resources resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the resources resource.
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the resources resource.
    - name: properties
      value: "{{ properties }}"
      description: |
        The resource-specific properties for this resource.
    - name: plan
      description: |
        The plan of the resource.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the resource.
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        ID of the resource that manages this resource.
    - name: sku
      description: |
        The SKU of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        model: "{{ model }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: extendedLocation
      description: |
        Resource extended location.
      value:
        type: "{{ type }}"
        name: "{{ name }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'update_by_id', value: 'update_by_id' }
    ]}
>
<TabItem value="update">

Updates a resource.

```sql
UPDATE azure.resource.resources
SET 
properties = '{{ properties }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
extendedLocation = '{{ extendedLocation }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' --required
AND parent_resource_path = '{{ parent_resource_path }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="update_by_id">

Update a resource by ID.

```sql
UPDATE azure.resource.resources
SET 
properties = '{{ properties }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
extendedLocation = '{{ extendedLocation }}',
tags = '{{ tags }}'
WHERE 
resource_id = '{{ resource_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
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
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_by_id', value: 'create_or_update_by_id' }
    ]}
>
<TabItem value="create_or_update">

Creates a resource.

```sql
REPLACE azure.resource.resources
SET 
properties = '{{ properties }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
extendedLocation = '{{ extendedLocation }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' --required
AND parent_resource_path = '{{ parent_resource_path }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_id">

Create a resource by ID.

```sql
REPLACE azure.resource.resources
SET 
properties = '{{ properties }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
location = '{{ location }}',
extendedLocation = '{{ extendedLocation }}',
tags = '{{ tags }}'
WHERE 
resource_id = '{{ resource_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
location,
managedBy,
plan,
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
        { label: 'delete', value: 'delete' },
        { label: 'delete_by_id', value: 'delete_by_id' }
    ]}
>
<TabItem value="delete">

Deletes a resource.

```sql
DELETE FROM azure.resource.resources
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_provider_namespace = '{{ resource_provider_namespace }}' --required
AND parent_resource_path = '{{ parent_resource_path }}' --required
AND resource_type = '{{ resource_type }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_id">

Deletes a resource by ID.

```sql
DELETE FROM azure.resource.resources
WHERE resource_id = '{{ resource_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_existence"
    values={[
        { label: 'check_existence', value: 'check_existence' },
        { label: 'check_existence_by_id', value: 'check_existence_by_id' },
        { label: 'move_resources', value: 'move_resources' },
        { label: 'validate_move_resources', value: 'validate_move_resources' }
    ]}
>
<TabItem value="check_existence">

Checks whether a resource exists.

```sql
EXEC azure.resource.resources.check_existence 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_provider_namespace='{{ resource_provider_namespace }}' --required, 
@parent_resource_path='{{ parent_resource_path }}' --required, 
@resource_type='{{ resource_type }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_existence_by_id">

Checks by ID whether a resource exists. This API currently works only for a limited set of Resource providers. In the event that a Resource provider does not implement this API, ARM will respond with a 405. The alternative then is to use the GET API to check for the existence of the resource.

```sql
EXEC azure.resource.resources.check_existence_by_id 
@resource_id='{{ resource_id }}' --required
;
```
</TabItem>
<TabItem value="move_resources">

Moves resources from one resource group to another resource group. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes.

```sql
EXEC azure.resource.resources.move_resources 
@source_resource_group_name='{{ source_resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resources": "{{ resources }}", 
"targetResourceGroup": "{{ targetResourceGroup }}"
}'
;
```
</TabItem>
<TabItem value="validate_move_resources">

Validates whether resources can be moved from one resource group to another resource group. This operation checks whether the specified resources can be moved to the target. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation.

```sql
EXEC azure.resource.resources.validate_move_resources 
@source_resource_group_name='{{ source_resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"resources": "{{ resources }}", 
"targetResourceGroup": "{{ targetResourceGroup }}"
}'
;
```
</TabItem>
</Tabs>
