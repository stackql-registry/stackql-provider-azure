--- 
title: global
hide_title: false
hide_table_of_contents: false
keywords:
  - global
  - web
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

Creates, updates, deletes, gets or lists a <code>global</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="global" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.global" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_deleted_web_app"
    values={[
        { label: 'get_deleted_web_app', value: 'get_deleted_web_app' }
    ]}
>
<TabItem value="get_deleted_web_app">

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
    <td><CopyableCode code="deletedSiteId" /></td>
    <td><code>integer</code></td>
    <td>Numeric id for the deleted site.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedSiteName" /></td>
    <td><code>string</code></td>
    <td>Name of the deleted site.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedTimestamp" /></td>
    <td><code>string</code></td>
    <td>Time in UTC when the app was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="geoRegionName" /></td>
    <td><code>string</code></td>
    <td>Geo Region of the deleted site.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>ResourceGroup that contained the deleted site.</td>
</tr>
<tr>
    <td><CopyableCode code="slot" /></td>
    <td><code>string</code></td>
    <td>Slot of the deleted site.</td>
</tr>
<tr>
    <td><CopyableCode code="subscription" /></td>
    <td><code>string</code></td>
    <td>Subscription containing the deleted site.</td>
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
    <td><a href="#get_deleted_web_app"><CopyableCode code="get_deleted_web_app" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deleted_site_id"><code>deleted_site_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get deleted app for a subscription. Description for Get deleted app for a subscription.</td>
</tr>
<tr>
    <td><a href="#get_deleted_web_app_snapshots"><CopyableCode code="get_deleted_web_app_snapshots" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deleted_site_id"><code>deleted_site_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all deleted apps for a subscription. Description for Get all deleted apps for a subscription.</td>
</tr>
<tr>
    <td><a href="#get_subscription_operation_with_async_response"><CopyableCode code="get_subscription_operation_with_async_response" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an operation in a subscription and given region. Description for Gets an operation in a subscription and given region.</td>
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
<tr id="parameter-deleted_site_id">
    <td><CopyableCode code="deleted_site_id" /></td>
    <td><code>string</code></td>
    <td>The numeric ID of the deleted app, e.g. 12345. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
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
    defaultValue="get_deleted_web_app"
    values={[
        { label: 'get_deleted_web_app', value: 'get_deleted_web_app' }
    ]}
>
<TabItem value="get_deleted_web_app">

Get deleted app for a subscription. Description for Get deleted app for a subscription.

```sql
SELECT
id,
name,
deletedSiteId,
deletedSiteName,
deletedTimestamp,
geoRegionName,
kind,
resourceGroup,
slot,
subscription,
systemData,
type
FROM azure.web.global
WHERE deleted_site_id = '{{ deleted_site_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_deleted_web_app_snapshots"
    values={[
        { label: 'get_deleted_web_app_snapshots', value: 'get_deleted_web_app_snapshots' },
        { label: 'get_subscription_operation_with_async_response', value: 'get_subscription_operation_with_async_response' }
    ]}
>
<TabItem value="get_deleted_web_app_snapshots">

Get all deleted apps for a subscription. Description for Get all deleted apps for a subscription.

```sql
EXEC azure.web.global.get_deleted_web_app_snapshots 
@deleted_site_id='{{ deleted_site_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_subscription_operation_with_async_response">

Gets an operation in a subscription and given region. Description for Gets an operation in a subscription and given region.

```sql
EXEC azure.web.global.get_subscription_operation_with_async_response 
@location='{{ location }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
