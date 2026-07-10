--- 
title: express_route_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_gateways
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

Creates, updates, deletes, gets or lists an <code>express_route_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="express_route_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_gateways" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_failover_single_test_details"
    values={[
        { label: 'get_failover_single_test_details', value: 'get_failover_single_test_details' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_failover_single_test_details">

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
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string</code></td>
    <td>Time when the test was completed.</td>
</tr>
<tr>
    <td><CopyableCode code="failoverConnectionDetails" /></td>
    <td><code>array</code></td>
    <td>List of all the failover connections for this peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="nonRedundantRoutes" /></td>
    <td><code>array</code></td>
    <td>List of al the routes that were received only from this peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>Peering location of the test.</td>
</tr>
<tr>
    <td><CopyableCode code="redundantRoutes" /></td>
    <td><code>array</code></td>
    <td>List of routes received from this peering as well as some other peering location.</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string</code></td>
    <td>Time when the test was started.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the test. Known values are: "NotStarted", "Starting", "Running", "StartFailed", "Stopping", "Completed", "StopFailed", "Invalid", and "Expired". (NotStarted, Starting, Running, StartFailed, Stopping, Completed, StopFailed, Invalid, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="wasSimulationSuccessful" /></td>
    <td><code>boolean</code></td>
    <td>Whether the failover simulation was successful or not.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="allowNonVirtualWanTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configures this gateway to accept traffic from non Virtual WAN networks.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configuration for auto scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>List of ExpressRoute connections to the ExpressRoute gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>The Virtual Hub where the ExpressRoute gateway is or will be deployed. Required.</td>
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
    <td><CopyableCode code="allowNonVirtualWanTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configures this gateway to accept traffic from non Virtual WAN networks.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configuration for auto scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>List of ExpressRoute connections to the ExpressRoute gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>The Virtual Hub where the ExpressRoute gateway is or will be deployed. Required.</td>
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
    <td><CopyableCode code="allowNonVirtualWanTraffic" /></td>
    <td><code>boolean</code></td>
    <td>Configures this gateway to accept traffic from non Virtual WAN networks.</td>
</tr>
<tr>
    <td><CopyableCode code="autoScaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Configuration for auto scaling.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="expressRouteConnections" /></td>
    <td><code>array</code></td>
    <td>List of ExpressRoute connections to the ExpressRoute gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the express route gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
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
    <td><CopyableCode code="virtualHub" /></td>
    <td><code>object</code></td>
    <td>The Virtual Hub where the ExpressRoute gateway is or will be deployed. Required.</td>
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
    <td><a href="#get_failover_single_test_details"><CopyableCode code="get_failover_single_test_details" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-peeringLocation"><code>peeringLocation</code></a>, <a href="#parameter-failoverTestId"><code>failoverTestId</code></a></td>
    <td></td>
    <td>Retrieves the details of a particular failover test performed on the ExpressRoute gateway based on the test Guid.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetches the details of a ExpressRoute gateway in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists ExpressRoute gateways in a given resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists ExpressRoute gateways under a given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a ExpressRoute gateway in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates express route gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a ExpressRoute gateway in a specified resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources.</td>
</tr>
<tr>
    <td><a href="#get_failover_all_tests_details"><CopyableCode code="get_failover_all_tests_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-fetchLatest"><code>fetchLatest</code></a></td>
    <td>Retrieves the details of all the failover tests performed on the ExpressRoute gateway for different peering locations.</td>
</tr>
<tr>
    <td><a href="#get_routes_information"><CopyableCode code="get_routes_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-attemptRefresh"><code>attemptRefresh</code></a></td>
    <td>Retrieves the route sets information for the ExpressRoute gateway.</td>
</tr>
<tr>
    <td><a href="#get_resiliency_information"><CopyableCode code="get_resiliency_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-attemptRefresh"><code>attemptRefresh</code></a></td>
    <td>Retrieves the resiliency information for the ExpressRoute gateway.</td>
</tr>
<tr>
    <td><a href="#start_site_failover_test"><CopyableCode code="start_site_failover_test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-peeringLocation"><code>peeringLocation</code></a></td>
    <td></td>
    <td>Starts failover simulation on the ExpressRoute gateway for the specified peering location.</td>
</tr>
<tr>
    <td><a href="#stop_site_failover_test"><CopyableCode code="stop_site_failover_test" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-express_route_gateway_name"><code>express_route_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops failover simulation on the ExpressRoute gateway for the specified peering location.</td>
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
<tr id="parameter-express_route_gateway_name">
    <td><CopyableCode code="express_route_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ExpressRoute gateway. Required.</td>
</tr>
<tr id="parameter-failoverTestId">
    <td><CopyableCode code="failoverTestId" /></td>
    <td><code>string</code></td>
    <td>The unique Guid value which identifies the test. Required.</td>
</tr>
<tr id="parameter-peeringLocation">
    <td><CopyableCode code="peeringLocation" /></td>
    <td><code>string</code></td>
    <td>Peering location of the test. Required.</td>
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
<tr id="parameter-attemptRefresh">
    <td><CopyableCode code="attemptRefresh" /></td>
    <td><code>boolean</code></td>
    <td>Whether to attempt a refresh of the resiliency information. Default value is None.</td>
</tr>
<tr id="parameter-fetchLatest">
    <td><CopyableCode code="fetchLatest" /></td>
    <td><code>boolean</code></td>
    <td>Fetch only the latest tests for each peering location. Default value is None.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of failover test. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_failover_single_test_details"
    values={[
        { label: 'get_failover_single_test_details', value: 'get_failover_single_test_details' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get_failover_single_test_details">

Retrieves the details of a particular failover test performed on the ExpressRoute gateway based on the test Guid.

```sql
SELECT
endTimeUtc,
failoverConnectionDetails,
nonRedundantRoutes,
peeringLocation,
redundantRoutes,
startTimeUtc,
status,
wasSimulationSuccessful
FROM azure.network.express_route_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND peeringLocation = '{{ peeringLocation }}' -- required
AND failoverTestId = '{{ failoverTestId }}' -- required
;
```
</TabItem>
<TabItem value="get">

Fetches the details of a ExpressRoute gateway in a resource group.

```sql
SELECT
id,
name,
allowNonVirtualWanTraffic,
autoScaleConfiguration,
etag,
expressRouteConnections,
location,
provisioningState,
tags,
type,
virtualHub
FROM azure.network.express_route_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists ExpressRoute gateways in a given resource group.

```sql
SELECT
id,
name,
allowNonVirtualWanTraffic,
autoScaleConfiguration,
etag,
expressRouteConnections,
location,
provisioningState,
tags,
type,
virtualHub
FROM azure.network.express_route_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists ExpressRoute gateways under a given subscription.

```sql
SELECT
id,
name,
allowNonVirtualWanTraffic,
autoScaleConfiguration,
etag,
expressRouteConnections,
location,
provisioningState,
tags,
type,
virtualHub
FROM azure.network.express_route_gateways
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a ExpressRoute gateway in a specified resource group.

```sql
INSERT INTO azure.network.express_route_gateways (
id,
location,
tags,
properties,
resource_group_name,
express_route_gateway_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ express_route_gateway_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: express_route_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the express_route_gateways resource.
    - name: express_route_gateway_name
      value: "{{ express_route_gateway_name }}"
      description: Required parameter for the express_route_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the express_route_gateways resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the express route gateway.
      value:
        autoScaleConfiguration:
          bounds:
            min: {{ min }}
            max: {{ max }}
        expressRouteConnections:
          - id: "{{ id }}"
            properties:
              provisioningState: "{{ provisioningState }}"
              expressRouteCircuitPeering:
                id: "{{ id }}"
              authorizationKey: "{{ authorizationKey }}"
              routingWeight: {{ routingWeight }}
              enableInternetSecurity: {{ enableInternetSecurity }}
              expressRouteGatewayBypass: {{ expressRouteGatewayBypass }}
              enablePrivateLinkFastPath: {{ enablePrivateLinkFastPath }}
              routingConfiguration:
                associatedRouteTable:
                  id: "{{ id }}"
                propagatedRouteTables:
                  labels: "{{ labels }}"
                  ids: "{{ ids }}"
                vnetRoutes:
                  staticRoutesConfig: "{{ staticRoutesConfig }}"
                  staticRoutes: "{{ staticRoutes }}"
                  bgpConnections: "{{ bgpConnections }}"
                inboundRouteMap:
                  id: "{{ id }}"
                outboundRouteMap:
                  id: "{{ id }}"
            name: "{{ name }}"
        provisioningState: "{{ provisioningState }}"
        virtualHub:
          id: "{{ id }}"
        allowNonVirtualWanTraffic: {{ allowNonVirtualWanTraffic }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates express route gateway tags.

```sql
UPDATE azure.network.express_route_gateways
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Creates or updates a ExpressRoute gateway in a specified resource group.

```sql
REPLACE azure.network.express_route_gateways
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources.

```sql
DELETE FROM azure.network.express_route_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND express_route_gateway_name = '{{ express_route_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_failover_all_tests_details"
    values={[
        { label: 'get_failover_all_tests_details', value: 'get_failover_all_tests_details' },
        { label: 'get_routes_information', value: 'get_routes_information' },
        { label: 'get_resiliency_information', value: 'get_resiliency_information' },
        { label: 'start_site_failover_test', value: 'start_site_failover_test' },
        { label: 'stop_site_failover_test', value: 'stop_site_failover_test' }
    ]}
>
<TabItem value="get_failover_all_tests_details">

Retrieves the details of all the failover tests performed on the ExpressRoute gateway for different peering locations.

```sql
EXEC azure.network.express_route_gateways.get_failover_all_tests_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@express_route_gateway_name='{{ express_route_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@type='{{ type }}', 
@fetchLatest={{ fetchLatest }}
;
```
</TabItem>
<TabItem value="get_routes_information">

Retrieves the route sets information for the ExpressRoute gateway.

```sql
EXEC azure.network.express_route_gateways.get_routes_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@express_route_gateway_name='{{ express_route_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@attemptRefresh={{ attemptRefresh }}
;
```
</TabItem>
<TabItem value="get_resiliency_information">

Retrieves the resiliency information for the ExpressRoute gateway.

```sql
EXEC azure.network.express_route_gateways.get_resiliency_information 
@resource_group_name='{{ resource_group_name }}' --required, 
@express_route_gateway_name='{{ express_route_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@attemptRefresh={{ attemptRefresh }}
;
```
</TabItem>
<TabItem value="start_site_failover_test">

Starts failover simulation on the ExpressRoute gateway for the specified peering location.

```sql
EXEC azure.network.express_route_gateways.start_site_failover_test 
@resource_group_name='{{ resource_group_name }}' --required, 
@express_route_gateway_name='{{ express_route_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@peeringLocation='{{ peeringLocation }}' --required
;
```
</TabItem>
<TabItem value="stop_site_failover_test">

Stops failover simulation on the ExpressRoute gateway for the specified peering location.

```sql
EXEC azure.network.express_route_gateways.stop_site_failover_test 
@resource_group_name='{{ resource_group_name }}' --required, 
@express_route_gateway_name='{{ express_route_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"peeringLocation": "{{ peeringLocation }}", 
"wasSimulationSuccessful": {{ wasSimulationSuccessful }}, 
"details": "{{ details }}"
}'
;
```
</TabItem>
</Tabs>
