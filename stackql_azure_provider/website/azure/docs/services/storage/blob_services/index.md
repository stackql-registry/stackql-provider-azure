--- 
title: blob_services
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_services
  - storage
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

Creates, updates, deletes, gets or lists a <code>blob_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="blob_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.blob_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="automaticSnapshotPolicyEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated in favor of isVersioningEnabled property.</td>
</tr>
<tr>
    <td><CopyableCode code="changeFeed" /></td>
    <td><code>object</code></td>
    <td>The blob service properties for change feed events.</td>
</tr>
<tr>
    <td><CopyableCode code="containerDeleteRetentionPolicy" /></td>
    <td><code>object</code></td>
    <td>The blob service properties for container soft delete.</td>
</tr>
<tr>
    <td><CopyableCode code="cors" /></td>
    <td><code>object</code></td>
    <td>Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultServiceVersion" /></td>
    <td><code>string</code></td>
    <td>DefaultServiceVersion indicates the default version to use for requests to the Blob service if an incoming request’s version is not specified. Possible values include version 2008-10-27 and all more recent versions.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteRetentionPolicy" /></td>
    <td><code>object</code></td>
    <td>The blob service properties for blob soft delete.</td>
</tr>
<tr>
    <td><CopyableCode code="isVersioningEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Versioning is enabled if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="lastAccessTimeTrackingPolicy" /></td>
    <td><code>object</code></td>
    <td>The blob service property to configure last access time based tracking policy.</td>
</tr>
<tr>
    <td><CopyableCode code="restorePolicy" /></td>
    <td><code>object</code></td>
    <td>The blob service properties for blob restore policy.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku name and tier.</td>
</tr>
<tr>
    <td><CopyableCode code="staticWebsite" /></td>
    <td><code>object</code></td>
    <td>The static website properties for blob storage.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List blob services of storage account. It returns a collection of one object named default.</td>
</tr>
<tr>
    <td><a href="#set_service_properties"><CopyableCode code="set_service_properties" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.</td>
</tr>
<tr>
    <td><a href="#get_service_properties"><CopyableCode code="get_service_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. Required.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List blob services of storage account. It returns a collection of one object named default.

```sql
SELECT
id,
name,
automaticSnapshotPolicyEnabled,
changeFeed,
containerDeleteRetentionPolicy,
cors,
defaultServiceVersion,
deleteRetentionPolicy,
isVersioningEnabled,
lastAccessTimeTrackingPolicy,
restorePolicy,
sku,
staticWebsite,
systemData,
type
FROM azure.storage.blob_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_service_properties"
    values={[
        { label: 'set_service_properties', value: 'set_service_properties' }
    ]}
>
<TabItem value="set_service_properties">

Sets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

```sql
REPLACE azure.storage.blob_services
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
systemData,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_service_properties"
    values={[
        { label: 'get_service_properties', value: 'get_service_properties' }
    ]}
>
<TabItem value="get_service_properties">

Gets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

```sql
EXEC azure.storage.blob_services.get_service_properties 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
