--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - resource_managedapplications
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_managedapplications.applications" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified path of managed application definition Id.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The collection of managed application artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The read-only authorizations property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="billingDetails" /></td>
    <td><code>object</code></td>
    <td>The managed application billing details.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that created the JIT request.</td>
</tr>
<tr>
    <td><CopyableCode code="customerSupport" /></td>
    <td><code>object</code></td>
    <td>The read-only customer support property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="jitAccessPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application Jit access policy.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. Required.</td>
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
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id.</td>
</tr>
<tr>
    <td><CopyableCode code="managementMode" /></td>
    <td><code>string</code></td>
    <td>The managed application management mode. Known values are: "NotSpecified", "Unmanaged", and "Managed".</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application parameters. It can be a JObject or a well formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The managed application provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherTenantId" /></td>
    <td><code>string</code></td>
    <td>The publisher tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="supportUrls" /></td>
    <td><code>object</code></td>
    <td>The read-only support URLs property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that last updated the JIT request.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified path of managed application definition Id.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The collection of managed application artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The read-only authorizations property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="billingDetails" /></td>
    <td><code>object</code></td>
    <td>The managed application billing details.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that created the JIT request.</td>
</tr>
<tr>
    <td><CopyableCode code="customerSupport" /></td>
    <td><code>object</code></td>
    <td>The read-only customer support property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="jitAccessPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application Jit access policy.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. Required.</td>
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
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id.</td>
</tr>
<tr>
    <td><CopyableCode code="managementMode" /></td>
    <td><code>string</code></td>
    <td>The managed application management mode. Known values are: "NotSpecified", "Unmanaged", and "Managed".</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application parameters. It can be a JObject or a well formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The managed application provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherTenantId" /></td>
    <td><code>string</code></td>
    <td>The publisher tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="supportUrls" /></td>
    <td><code>object</code></td>
    <td>The read-only support URLs property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that last updated the JIT request.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified path of managed application definition Id.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The collection of managed application artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The read-only authorizations property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="billingDetails" /></td>
    <td><code>object</code></td>
    <td>The managed application billing details.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that created the JIT request.</td>
</tr>
<tr>
    <td><CopyableCode code="customerSupport" /></td>
    <td><code>object</code></td>
    <td>The read-only customer support property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="jitAccessPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application Jit access policy.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. Required.</td>
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
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id.</td>
</tr>
<tr>
    <td><CopyableCode code="managementMode" /></td>
    <td><code>string</code></td>
    <td>The managed application management mode. Known values are: "NotSpecified", "Unmanaged", and "Managed".</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application parameters. It can be a JObject or a well formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The managed application provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherTenantId" /></td>
    <td><code>string</code></td>
    <td>The publisher tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="supportUrls" /></td>
    <td><code>object</code></td>
    <td>The read-only support URLs property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that last updated the JIT request.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified path of managed application definition Id.</td>
</tr>
<tr>
    <td><CopyableCode code="artifacts" /></td>
    <td><code>array</code></td>
    <td>The collection of managed application artifacts.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizations" /></td>
    <td><code>array</code></td>
    <td>The read-only authorizations property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="billingDetails" /></td>
    <td><code>object</code></td>
    <td>The managed application billing details.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that created the JIT request.</td>
</tr>
<tr>
    <td><CopyableCode code="customerSupport" /></td>
    <td><code>object</code></td>
    <td>The read-only customer support property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="jitAccessPolicy" /></td>
    <td><code>object</code></td>
    <td>The managed application Jit access policy.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. Required.</td>
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
    <td><CopyableCode code="managedResourceGroupId" /></td>
    <td><code>string</code></td>
    <td>The managed resource group Id.</td>
</tr>
<tr>
    <td><CopyableCode code="managementMode" /></td>
    <td><code>string</code></td>
    <td>The managed application management mode. Known values are: "NotSpecified", "Unmanaged", and "Managed".</td>
</tr>
<tr>
    <td><CopyableCode code="outputs" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application outputs.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Name and value pairs that define the managed application parameters. It can be a JObject or a well formed JSON string.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>The plan information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The managed application provisioning state. Known values are: "NotSpecified", "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled", "Failed", "Succeeded", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="publisherTenantId" /></td>
    <td><code>string</code></td>
    <td>The publisher tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="supportUrls" /></td>
    <td><code>object</code></td>
    <td>The read-only support URLs property that is retrieved from the application package.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>object</code></td>
    <td>The client entity that last updated the JIT request.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the managed application.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the applications within a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the applications within a subscription.</td>
</tr>
<tr>
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Gets the managed application.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates a new managed application.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_id"><CopyableCode code="create_or_update_by_id" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates a new managed application.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.</td>
</tr>
<tr>
    <td><a href="#update_by_id"><CopyableCode code="update_by_id" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates a new managed application.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_id"><CopyableCode code="create_or_update_by_id" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates a new managed application.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the managed application.</td>
</tr>
<tr>
    <td><a href="#delete_by_id"><CopyableCode code="delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Deletes the managed application.</td>
</tr>
<tr>
    <td><a href="#refresh_permissions"><CopyableCode code="refresh_permissions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh Permissions for application.</td>
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
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/&#123;guid&#125;/resourceGroups/&#123;resource-group-name&#125;/Microsoft.Solutions/applications/&#123;application-name&#125;. Required.</td>
</tr>
<tr id="parameter-application_name">
    <td><CopyableCode code="application_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed application. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'get_by_id', value: 'get_by_id' }
    ]}
>
<TabItem value="get">

Gets the managed application.

```sql
SELECT
id,
name,
applicationDefinitionId,
artifacts,
authorizations,
billingDetails,
createdBy,
customerSupport,
identity,
jitAccessPolicy,
kind,
location,
managedBy,
managedResourceGroupId,
managementMode,
outputs,
parameters,
plan,
provisioningState,
publisherTenantId,
sku,
supportUrls,
tags,
type,
updatedBy
FROM azure.resource_managedapplications.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all the applications within a resource group.

```sql
SELECT
id,
name,
applicationDefinitionId,
artifacts,
authorizations,
billingDetails,
createdBy,
customerSupport,
identity,
jitAccessPolicy,
kind,
location,
managedBy,
managedResourceGroupId,
managementMode,
outputs,
parameters,
plan,
provisioningState,
publisherTenantId,
sku,
supportUrls,
tags,
type,
updatedBy
FROM azure.resource_managedapplications.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Gets all the applications within a subscription.

```sql
SELECT
id,
name,
applicationDefinitionId,
artifacts,
authorizations,
billingDetails,
createdBy,
customerSupport,
identity,
jitAccessPolicy,
kind,
location,
managedBy,
managedResourceGroupId,
managementMode,
outputs,
parameters,
plan,
provisioningState,
publisherTenantId,
sku,
supportUrls,
tags,
type,
updatedBy
FROM azure.resource_managedapplications.applications
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_id">

Gets the managed application.

```sql
SELECT
id,
name,
applicationDefinitionId,
artifacts,
authorizations,
billingDetails,
createdBy,
customerSupport,
identity,
jitAccessPolicy,
kind,
location,
managedBy,
managedResourceGroupId,
managementMode,
outputs,
parameters,
plan,
provisioningState,
publisherTenantId,
sku,
supportUrls,
tags,
type,
updatedBy
FROM azure.resource_managedapplications.applications
WHERE application_id = '{{ application_id }}' -- required
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

Creates a new managed application.

```sql
INSERT INTO azure.resource_managedapplications.applications (
location,
tags,
managedBy,
sku,
plan,
kind,
identity,
properties,
resource_group_name,
application_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ managedBy }}',
'{{ sku }}',
'{{ plan }}',
'{{ kind }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ application_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_by_id">

Creates a new managed application.

```sql
INSERT INTO azure.resource_managedapplications.applications (
location,
tags,
managedBy,
sku,
plan,
kind,
identity,
properties,
application_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ managedBy }}',
'{{ sku }}',
'{{ plan }}',
'{{ kind }}' /* required */,
'{{ identity }}',
'{{ properties }}',
'{{ application_id }}'
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: applications
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the applications resource.
    - name: application_name
      value: "{{ application_name }}"
      description: Required parameter for the applications resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the applications resource.
    - name: application_id
      value: "{{ application_id }}"
      description: Required parameter for the applications resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
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
    - name: plan
      description: |
        The plan information.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. Required.
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: properties
      value:
        managedResourceGroupId: "{{ managedResourceGroupId }}"
        applicationDefinitionId: "{{ applicationDefinitionId }}"
        parameters: "{{ parameters }}"
        jitAccessPolicy:
          jitAccessEnabled: {{ jitAccessEnabled }}
          jitApprovalMode: "{{ jitApprovalMode }}"
          jitApprovers:
            - id: "{{ id }}"
              type: "{{ type }}"
              displayName: "{{ displayName }}"
          maximumJitAccessDuration: "{{ maximumJitAccessDuration }}"
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

Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.

```sql
UPDATE azure.resource_managedapplications.applications
SET 
location = '{{ location }}',
tags = '{{ tags }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
tags,
type;
```
</TabItem>
<TabItem value="update_by_id">

Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.

```sql
UPDATE azure.resource_managedapplications.applications
SET 
location = '{{ location }}',
tags = '{{ tags }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
application_id = '{{ application_id }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
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

Creates a new managed application.

```sql
REPLACE azure.resource_managedapplications.applications
SET 
location = '{{ location }}',
tags = '{{ tags }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_id">

Creates a new managed application.

```sql
REPLACE azure.resource_managedapplications.applications
SET 
location = '{{ location }}',
tags = '{{ tags }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
plan = '{{ plan }}',
kind = '{{ kind }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
application_id = '{{ application_id }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
identity,
kind,
location,
managedBy,
plan,
properties,
sku,
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

Deletes the managed application.

```sql
DELETE FROM azure.resource_managedapplications.applications
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_id">

Deletes the managed application.

```sql
DELETE FROM azure.resource_managedapplications.applications
WHERE application_id = '{{ application_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh_permissions"
    values={[
        { label: 'refresh_permissions', value: 'refresh_permissions' }
    ]}
>
<TabItem value="refresh_permissions">

Refresh Permissions for application.

```sql
EXEC azure.resource_managedapplications.applications.refresh_permissions 
@resource_group_name='{{ resource_group_name }}' --required, 
@application_name='{{ application_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
