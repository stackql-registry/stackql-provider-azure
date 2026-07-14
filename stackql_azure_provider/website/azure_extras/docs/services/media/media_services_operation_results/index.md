--- 
title: media_services_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - media_services_operation_results
  - media
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

Creates, updates, deletes, gets or lists a <code>media_services_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="media_services_operation_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.media.media_services_operation_results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The account encryption properties.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Managed Identity for the Media Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="keyDelivery" /></td>
    <td><code>object</code></td>
    <td>The Key Delivery properties for Media Services account.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mediaServiceId" /></td>
    <td><code>string</code></td>
    <td>The Media Services account ID.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The Private Endpoint Connections created for the Media Service account.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Media Services account. Known values are: "Failed", "InProgress", and "Succeeded".</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Whether or not public network access is allowed for resources under the Media Services account. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccounts" /></td>
    <td><code>array</code></td>
    <td>The storage accounts for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAuthentication" /></td>
    <td><code>string</code></td>
    <td>Known values are: "System" and "ManagedIdentity".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get operation result. Get media service operation result.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>Location name. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Operation Id. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get operation result. Get media service operation result.

```sql
SELECT
id,
name,
encryption,
identity,
keyDelivery,
location,
mediaServiceId,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
storageAccounts,
storageAuthentication,
systemData,
tags,
type
FROM azure_extras.media.media_services_operation_results
WHERE location_name = '{{ location_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
