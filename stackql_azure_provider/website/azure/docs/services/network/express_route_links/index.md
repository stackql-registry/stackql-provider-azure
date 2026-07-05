--- 
title: express_route_links
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_links
  - network
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

Creates, updates, deletes, gets or lists an <code>express_route_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_links" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_links" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td>Name of child port resource that is unique among child port resources of the parent.</td>
</tr>
<tr>
    <td><CopyableCode code="adminState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the physical port. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="coloLocation" /></td>
    <td><code>string</code></td>
    <td>Cololocation for ExpressRoute Hybrid Direct.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorType" /></td>
    <td><code>string</code></td>
    <td>Physical fiber port type. Known values are: "LC" and "SC". (LC, SC)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceName" /></td>
    <td><code>string</code></td>
    <td>Name of Azure router interface.</td>
</tr>
<tr>
    <td><CopyableCode code="macSecConfig" /></td>
    <td><code>object</code></td>
    <td>MacSec configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="patchPanelId" /></td>
    <td><code>string</code></td>
    <td>Mapping between physical port to patch panel port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route link resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>Mapping of physical patch panel to rack.</td>
</tr>
<tr>
    <td><CopyableCode code="routerName" /></td>
    <td><code>string</code></td>
    <td>Name of Azure router associated with physical port.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of child port resource that is unique among child port resources of the parent.</td>
</tr>
<tr>
    <td><CopyableCode code="adminState" /></td>
    <td><code>string</code></td>
    <td>Administrative state of the physical port. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="coloLocation" /></td>
    <td><code>string</code></td>
    <td>Cololocation for ExpressRoute Hybrid Direct.</td>
</tr>
<tr>
    <td><CopyableCode code="connectorType" /></td>
    <td><code>string</code></td>
    <td>Physical fiber port type. Known values are: "LC" and "SC". (LC, SC)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="interfaceName" /></td>
    <td><code>string</code></td>
    <td>Name of Azure router interface.</td>
</tr>
<tr>
    <td><CopyableCode code="macSecConfig" /></td>
    <td><code>object</code></td>
    <td>MacSec configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="patchPanelId" /></td>
    <td><code>string</code></td>
    <td>Mapping between physical port to patch panel port.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route link resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="rackId" /></td>
    <td><code>string</code></td>
    <td>Mapping of physical patch panel to rack.</td>
</tr>
<tr>
    <td><CopyableCode code="routerName" /></td>
    <td><code>string</code></td>
    <td>Name of Azure router associated with physical port.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_port_name"><code>express_route_port_name</code></a>, <a href="#parameter-link_name"><code>link_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the specified ExpressRouteLink resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_port_name"><code>express_route_port_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource.</td>
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
<tr id="parameter-express_route_port_name">
    <td><CopyableCode code="express_route_port_name" /></td>
    <td><code>string</code></td>
    <td>The name of ExpressRoutePort. Required.</td>
</tr>
<tr id="parameter-link_name">
    <td><CopyableCode code="link_name" /></td>
    <td><code>string</code></td>
    <td>The name of the express route link. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the specified ExpressRouteLink resource.

```sql
SELECT
id,
name,
adminState,
coloLocation,
connectorType,
etag,
interfaceName,
macSecConfig,
patchPanelId,
provisioningState,
rackId,
routerName
FROM azure.network.express_route_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND express_route_port_name = '{{ express_route_port_name }}' -- required
AND link_name = '{{ link_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource.

```sql
SELECT
id,
name,
adminState,
coloLocation,
connectorType,
etag,
interfaceName,
macSecConfig,
patchPanelId,
provisioningState,
rackId,
routerName
FROM azure.network.express_route_links
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND express_route_port_name = '{{ express_route_port_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
