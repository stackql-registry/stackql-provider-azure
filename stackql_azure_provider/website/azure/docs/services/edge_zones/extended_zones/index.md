--- 
title: extended_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_zones
  - edge_zones
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

Creates, updates, deletes, gets or lists an <code>extended_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extended_zones" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.edge_zones.extended_zones" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="geography" /></td>
    <td><code>string</code></td>
    <td>Geography of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="geographyGroup" /></td>
    <td><code>string</code></td>
    <td>The Geography Group of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="homeLocation" /></td>
    <td><code>string</code></td>
    <td>The Home Location of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>string</code></td>
    <td>The Latitude of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>string</code></td>
    <td>The Longitude of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the last operation performed by the subscription on the Edge Zone resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="regionCategory" /></td>
    <td><code>string</code></td>
    <td>Category of region for the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="regionType" /></td>
    <td><code>string</code></td>
    <td>Type of region for the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="regionalDisplayName" /></td>
    <td><code>string</code></td>
    <td>Regional display name of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationState" /></td>
    <td><code>string</code></td>
    <td>Indicates the Azure Extended Zone registration’s approval status. Known values are: "NotRegistered", "PendingRegister", "Registered", and "PendingUnregister". (NotRegistered, PendingRegister, Registered, PendingUnregister)</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="geography" /></td>
    <td><code>string</code></td>
    <td>Geography of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="geographyGroup" /></td>
    <td><code>string</code></td>
    <td>The Geography Group of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="homeLocation" /></td>
    <td><code>string</code></td>
    <td>The Home Location of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>string</code></td>
    <td>The Latitude of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>string</code></td>
    <td>The Longitude of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the last operation performed by the subscription on the Edge Zone resource. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="regionCategory" /></td>
    <td><code>string</code></td>
    <td>Category of region for the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="regionType" /></td>
    <td><code>string</code></td>
    <td>Type of region for the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="regionalDisplayName" /></td>
    <td><code>string</code></td>
    <td>Regional display name of the Azure Extended Zone. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationState" /></td>
    <td><code>string</code></td>
    <td>Indicates the Azure Extended Zone registration’s approval status. Known values are: "NotRegistered", "PendingRegister", "Registered", and "PendingUnregister". (NotRegistered, PendingRegister, Registered, PendingUnregister)</td>
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
    <td><a href="#parameter-extended_zone_name"><code>extended_zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Azure Extended Zone for a subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Azure Extended Zones available to a subscription.</td>
</tr>
<tr>
    <td><a href="#register"><CopyableCode code="register" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-extended_zone_name"><code>extended_zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Registers a subscription for an Extended Zone.</td>
</tr>
<tr>
    <td><a href="#unregister"><CopyableCode code="unregister" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-extended_zone_name"><code>extended_zone_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Unregisters a subscription for an Extended Zone.</td>
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
<tr id="parameter-extended_zone_name">
    <td><CopyableCode code="extended_zone_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ExtendedZone. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets an Azure Extended Zone for a subscription.

```sql
SELECT
id,
name,
displayName,
geography,
geographyGroup,
homeLocation,
latitude,
longitude,
provisioningState,
regionCategory,
regionType,
regionalDisplayName,
registrationState,
systemData,
type
FROM azure.edge_zones.extended_zones
WHERE extended_zone_name = '{{ extended_zone_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists the Azure Extended Zones available to a subscription.

```sql
SELECT
id,
name,
displayName,
geography,
geographyGroup,
homeLocation,
latitude,
longitude,
provisioningState,
regionCategory,
regionType,
regionalDisplayName,
registrationState,
systemData,
type
FROM azure.edge_zones.extended_zones
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="register"
    values={[
        { label: 'register', value: 'register' },
        { label: 'unregister', value: 'unregister' }
    ]}
>
<TabItem value="register">

Registers a subscription for an Extended Zone.

```sql
EXEC azure.edge_zones.extended_zones.register 
@extended_zone_name='{{ extended_zone_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="unregister">

Unregisters a subscription for an Extended Zone.

```sql
EXEC azure.edge_zones.extended_zones.unregister 
@extended_zone_name='{{ extended_zone_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
