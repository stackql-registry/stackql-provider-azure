--- 
title: data_products
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products
  - network_analytics
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>data_products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_products" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.network_analytics.data_products" /></td></tr>
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
    <td><CopyableCode code="availableMinorVersions" /></td>
    <td><code>array</code></td>
    <td>List of available minor versions of the data product resource.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionEndpoints" /></td>
    <td><code>object</code></td>
    <td>Resource links which exposed to the customer to query the data.</td>
</tr>
<tr>
    <td><CopyableCode code="currentMinorVersion" /></td>
    <td><code>string</code></td>
    <td>Current configured minor version of the data product resource.</td>
</tr>
<tr>
    <td><CopyableCode code="customerEncryptionKey" /></td>
    <td><code>object</code></td>
    <td>Customer managed encryption key details for data product.</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeyEncryptionEnabled" /></td>
    <td><code>string</code></td>
    <td>Flag to enable customer managed key encryption for data product. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="documentation" /></td>
    <td><code>string</code></td>
    <td>Documentation link for the data product based on definition file.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultUrl" /></td>
    <td><code>string</code></td>
    <td>Key vault url.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="majorVersion" /></td>
    <td><code>string</code></td>
    <td>Major version of data product. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkacls" /></td>
    <td><code>object</code></td>
    <td>Network rule set for data product.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>List of name or email associated with data product resource deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinksEnabled" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable private link for data product resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name of data product. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Latest provisioning state of data product. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable public access of data product resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Data product publisher name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="purviewAccount" /></td>
    <td><code>string</code></td>
    <td>Purview account url for data product to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="purviewCollection" /></td>
    <td><code>string</code></td>
    <td>Purview collection url for data product to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancy" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable redundancy for data product. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the data product resource.</td>
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
    <td><CopyableCode code="availableMinorVersions" /></td>
    <td><code>array</code></td>
    <td>List of available minor versions of the data product resource.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionEndpoints" /></td>
    <td><code>object</code></td>
    <td>Resource links which exposed to the customer to query the data.</td>
</tr>
<tr>
    <td><CopyableCode code="currentMinorVersion" /></td>
    <td><code>string</code></td>
    <td>Current configured minor version of the data product resource.</td>
</tr>
<tr>
    <td><CopyableCode code="customerEncryptionKey" /></td>
    <td><code>object</code></td>
    <td>Customer managed encryption key details for data product.</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeyEncryptionEnabled" /></td>
    <td><code>string</code></td>
    <td>Flag to enable customer managed key encryption for data product. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="documentation" /></td>
    <td><code>string</code></td>
    <td>Documentation link for the data product based on definition file.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultUrl" /></td>
    <td><code>string</code></td>
    <td>Key vault url.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="majorVersion" /></td>
    <td><code>string</code></td>
    <td>Major version of data product. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkacls" /></td>
    <td><code>object</code></td>
    <td>Network rule set for data product.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>List of name or email associated with data product resource deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinksEnabled" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable private link for data product resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name of data product. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Latest provisioning state of data product. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable public access of data product resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Data product publisher name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="purviewAccount" /></td>
    <td><code>string</code></td>
    <td>Purview account url for data product to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="purviewCollection" /></td>
    <td><code>string</code></td>
    <td>Purview collection url for data product to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancy" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable redundancy for data product. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the data product resource.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="availableMinorVersions" /></td>
    <td><code>array</code></td>
    <td>List of available minor versions of the data product resource.</td>
</tr>
<tr>
    <td><CopyableCode code="consumptionEndpoints" /></td>
    <td><code>object</code></td>
    <td>Resource links which exposed to the customer to query the data.</td>
</tr>
<tr>
    <td><CopyableCode code="currentMinorVersion" /></td>
    <td><code>string</code></td>
    <td>Current configured minor version of the data product resource.</td>
</tr>
<tr>
    <td><CopyableCode code="customerEncryptionKey" /></td>
    <td><code>object</code></td>
    <td>Customer managed encryption key details for data product.</td>
</tr>
<tr>
    <td><CopyableCode code="customerManagedKeyEncryptionEnabled" /></td>
    <td><code>string</code></td>
    <td>Flag to enable customer managed key encryption for data product. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="documentation" /></td>
    <td><code>string</code></td>
    <td>Documentation link for the data product based on definition file.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultUrl" /></td>
    <td><code>string</code></td>
    <td>Key vault url.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="majorVersion" /></td>
    <td><code>string</code></td>
    <td>Major version of data product. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedResourceGroupConfiguration" /></td>
    <td><code>object</code></td>
    <td>Managed resource group configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="networkacls" /></td>
    <td><code>object</code></td>
    <td>Network rule set for data product.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>List of name or email associated with data product resource deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinksEnabled" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable private link for data product resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name of data product. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Latest provisioning state of data product. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable public access of data product resource. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>Data product publisher name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="purviewAccount" /></td>
    <td><code>string</code></td>
    <td>Purview account url for data product to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="purviewCollection" /></td>
    <td><code>string</code></td>
    <td>Purview collection url for data product to connect to.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancy" /></td>
    <td><code>string</code></td>
    <td>Flag to enable or disable redundancy for data product. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the data product resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve data product resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List data products by resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List data products by subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create data product resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update data product resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete data product resource.</td>
</tr>
<tr>
    <td><a href="#list_roles_assignments"><CopyableCode code="list_roles_assignments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List user roles associated with the data product.</td>
</tr>
<tr>
    <td><a href="#add_user_role"><CopyableCode code="add_user_role" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-roleId"><code>roleId</code></a>, <a href="#parameter-principalId"><code>principalId</code></a>, <a href="#parameter-userName"><code>userName</code></a>, <a href="#parameter-dataTypeScope"><code>dataTypeScope</code></a>, <a href="#parameter-principalType"><code>principalType</code></a>, <a href="#parameter-role"><code>role</code></a></td>
    <td></td>
    <td>Assign role to the data product.</td>
</tr>
<tr>
    <td><a href="#generate_storage_account_sas_token"><CopyableCode code="generate_storage_account_sas_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-startTimeStamp"><code>startTimeStamp</code></a>, <a href="#parameter-expiryTimeStamp"><code>expiryTimeStamp</code></a>, <a href="#parameter-ipAddress"><code>ipAddress</code></a></td>
    <td></td>
    <td>Generate sas token for storage account.</td>
</tr>
<tr>
    <td><a href="#remove_user_role"><CopyableCode code="remove_user_role" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-roleId"><code>roleId</code></a>, <a href="#parameter-principalId"><code>principalId</code></a>, <a href="#parameter-userName"><code>userName</code></a>, <a href="#parameter-dataTypeScope"><code>dataTypeScope</code></a>, <a href="#parameter-principalType"><code>principalType</code></a>, <a href="#parameter-role"><code>role</code></a>, <a href="#parameter-roleAssignmentId"><code>roleAssignmentId</code></a></td>
    <td></td>
    <td>Remove role from the data product.</td>
</tr>
<tr>
    <td><a href="#rotate_key"><CopyableCode code="rotate_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_product_name"><code>data_product_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-keyVaultUrl"><code>keyVaultUrl</code></a></td>
    <td></td>
    <td>Initiate key rotation on Data Product.</td>
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
<tr id="parameter-data_product_name">
    <td><CopyableCode code="data_product_name" /></td>
    <td><code>string</code></td>
    <td>The data product resource name. Required.</td>
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

Retrieve data product resource.

```sql
SELECT
id,
name,
availableMinorVersions,
consumptionEndpoints,
currentMinorVersion,
customerEncryptionKey,
customerManagedKeyEncryptionEnabled,
documentation,
identity,
keyVaultUrl,
location,
majorVersion,
managedResourceGroupConfiguration,
networkacls,
owners,
privateLinksEnabled,
product,
provisioningState,
publicNetworkAccess,
publisher,
purviewAccount,
purviewCollection,
redundancy,
resourceGuid,
systemData,
tags,
type
FROM azure_extras.network_analytics.data_products
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_product_name = '{{ data_product_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List data products by resource group.

```sql
SELECT
id,
name,
availableMinorVersions,
consumptionEndpoints,
currentMinorVersion,
customerEncryptionKey,
customerManagedKeyEncryptionEnabled,
documentation,
identity,
keyVaultUrl,
location,
majorVersion,
managedResourceGroupConfiguration,
networkacls,
owners,
privateLinksEnabled,
product,
provisioningState,
publicNetworkAccess,
publisher,
purviewAccount,
purviewCollection,
redundancy,
resourceGuid,
systemData,
tags,
type
FROM azure_extras.network_analytics.data_products
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List data products by subscription.

```sql
SELECT
id,
name,
availableMinorVersions,
consumptionEndpoints,
currentMinorVersion,
customerEncryptionKey,
customerManagedKeyEncryptionEnabled,
documentation,
identity,
keyVaultUrl,
location,
majorVersion,
managedResourceGroupConfiguration,
networkacls,
owners,
privateLinksEnabled,
product,
provisioningState,
publicNetworkAccess,
publisher,
purviewAccount,
purviewCollection,
redundancy,
resourceGuid,
systemData,
tags,
type
FROM azure_extras.network_analytics.data_products
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create data product resource.

```sql
INSERT INTO azure_extras.network_analytics.data_products (
tags,
location,
properties,
identity,
resource_group_name,
data_product_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ data_product_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: data_products
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_products resource.
    - name: data_product_name
      value: "{{ data_product_name }}"
      description: Required parameter for the data_products resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_products resource.
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
        resourceGuid: "{{ resourceGuid }}"
        provisioningState: "{{ provisioningState }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        majorVersion: "{{ majorVersion }}"
        owners:
          - "{{ owners }}"
        redundancy: "{{ redundancy }}"
        purviewAccount: "{{ purviewAccount }}"
        purviewCollection: "{{ purviewCollection }}"
        privateLinksEnabled: "{{ privateLinksEnabled }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        customerManagedKeyEncryptionEnabled: "{{ customerManagedKeyEncryptionEnabled }}"
        customerEncryptionKey:
          keyVaultUri: "{{ keyVaultUri }}"
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
        networkacls:
          virtualNetworkRule:
            - id: "{{ id }}"
              action: "{{ action }}"
              state: "{{ state }}"
          ipRules:
            - value: "{{ value }}"
              action: "{{ action }}"
          allowedQueryIpRangeList:
            - "{{ allowedQueryIpRangeList }}"
          defaultAction: "{{ defaultAction }}"
        managedResourceGroupConfiguration:
          name: "{{ name }}"
          location: "{{ location }}"
        availableMinorVersions:
          - "{{ availableMinorVersions }}"
        currentMinorVersion: "{{ currentMinorVersion }}"
        documentation: "{{ documentation }}"
        consumptionEndpoints:
          ingestionUrl: "{{ ingestionUrl }}"
          ingestionResourceId: "{{ ingestionResourceId }}"
          fileAccessUrl: "{{ fileAccessUrl }}"
          fileAccessResourceId: "{{ fileAccessResourceId }}"
          queryUrl: "{{ queryUrl }}"
          queryResourceId: "{{ queryResourceId }}"
        keyVaultUrl: "{{ keyVaultUrl }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
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

Update data product resource.

```sql
UPDATE azure_extras.network_analytics.data_products
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND data_product_name = '{{ data_product_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Delete data product resource.

```sql
DELETE FROM azure_extras.network_analytics.data_products
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND data_product_name = '{{ data_product_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_roles_assignments"
    values={[
        { label: 'list_roles_assignments', value: 'list_roles_assignments' },
        { label: 'add_user_role', value: 'add_user_role' },
        { label: 'generate_storage_account_sas_token', value: 'generate_storage_account_sas_token' },
        { label: 'remove_user_role', value: 'remove_user_role' },
        { label: 'rotate_key', value: 'rotate_key' }
    ]}
>
<TabItem value="list_roles_assignments">

List user roles associated with the data product.

```sql
EXEC azure_extras.network_analytics.data_products.list_roles_assignments 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="add_user_role">

Assign role to the data product.

```sql
EXEC azure_extras.network_analytics.data_products.add_user_role 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"roleId": "{{ roleId }}", 
"principalId": "{{ principalId }}", 
"userName": "{{ userName }}", 
"dataTypeScope": "{{ dataTypeScope }}", 
"principalType": "{{ principalType }}", 
"role": "{{ role }}"
}'
;
```
</TabItem>
<TabItem value="generate_storage_account_sas_token">

Generate sas token for storage account.

```sql
EXEC azure_extras.network_analytics.data_products.generate_storage_account_sas_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startTimeStamp": "{{ startTimeStamp }}", 
"expiryTimeStamp": "{{ expiryTimeStamp }}", 
"ipAddress": "{{ ipAddress }}"
}'
;
```
</TabItem>
<TabItem value="remove_user_role">

Remove role from the data product.

```sql
EXEC azure_extras.network_analytics.data_products.remove_user_role 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"roleId": "{{ roleId }}", 
"principalId": "{{ principalId }}", 
"userName": "{{ userName }}", 
"dataTypeScope": "{{ dataTypeScope }}", 
"principalType": "{{ principalType }}", 
"role": "{{ role }}", 
"roleAssignmentId": "{{ roleAssignmentId }}"
}'
;
```
</TabItem>
<TabItem value="rotate_key">

Initiate key rotation on Data Product.

```sql
EXEC azure_extras.network_analytics.data_products.rotate_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@data_product_name='{{ data_product_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyVaultUrl": "{{ keyVaultUrl }}"
}'
;
```
</TabItem>
</Tabs>
