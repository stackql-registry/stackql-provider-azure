--- 
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - trafficmanager
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

Creates, updates, deletes, gets or lists an <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.trafficmanager.endpoints" /></td></tr>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/trafficManagerProfiles/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="alwaysServe" /></td>
    <td><code>string</code></td>
    <td>If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="customHeaders" /></td>
    <td><code>array</code></td>
    <td>List of custom headers.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointLocation" /></td>
    <td><code>string</code></td>
    <td>Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointMonitorStatus" /></td>
    <td><code>string</code></td>
    <td>The monitoring status of the endpoint. Known values are: "CheckingEndpoint", "Online", "Degraded", "Disabled", "Inactive", "Stopped", and "Unmonitored". (CheckingEndpoint, Online, Degraded, Disabled, Inactive, Stopped, Unmonitored)</td>
</tr>
<tr>
    <td><CopyableCode code="endpointStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="geoMapping" /></td>
    <td><code>array</code></td>
    <td>The list of countries/regions mapped to this endpoint when using the 'Geographic' traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values.</td>
</tr>
<tr>
    <td><CopyableCode code="minChildEndpoints" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.</td>
</tr>
<tr>
    <td><CopyableCode code="minChildEndpointsIPv4" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.</td>
</tr>
<tr>
    <td><CopyableCode code="minChildEndpointsIPv6" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of this endpoint when using the 'Priority' traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter. If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value.</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the 'Subnet' traffic routing method. An empty list will match all ranges not covered by other endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.</td>
</tr>
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>The weight of this endpoint when using the 'Weighted' traffic routing method. Possible values are from 1 to 1000.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_type"><code>endpoint_type</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Traffic Manager endpoint.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_type"><code>endpoint_type</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Traffic Manager endpoint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_type"><code>endpoint_type</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Traffic Manager endpoint.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_type"><code>endpoint_type</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Traffic Manager endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_type"><code>endpoint_type</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Traffic Manager endpoint.</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Traffic Manager endpoint. Required.</td>
</tr>
<tr id="parameter-endpoint_type">
    <td><CopyableCode code="endpoint_type" /></td>
    <td><code>string</code></td>
    <td>The type of the Traffic Manager endpoint. Known values are: "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Traffic Manager profile. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a Traffic Manager endpoint.

```sql
SELECT
id,
name,
alwaysServe,
customHeaders,
endpointLocation,
endpointMonitorStatus,
endpointStatus,
geoMapping,
minChildEndpoints,
minChildEndpointsIPv4,
minChildEndpointsIPv6,
priority,
subnets,
target,
targetResourceId,
type,
weight
FROM azure.trafficmanager.endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_type = '{{ endpoint_type }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create or update a Traffic Manager endpoint.

```sql
INSERT INTO azure.trafficmanager.endpoints (
id,
name,
type,
properties,
resource_group_name,
profile_name,
endpoint_type,
endpoint_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ type }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ endpoint_type }}',
'{{ endpoint_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: endpoints
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the endpoints resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint_type
      value: "{{ endpoint_type }}"
      description: Required parameter for the endpoints resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the endpoints resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the endpoints resource.
    - name: id
      value: "{{ id }}"
      description: |
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource.
    - name: type
      value: "{{ type }}"
      description: |
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
    - name: properties
      description: |
        The properties of the Traffic Manager endpoint.
      value:
        targetResourceId: "{{ targetResourceId }}"
        target: "{{ target }}"
        endpointStatus: "{{ endpointStatus }}"
        weight: {{ weight }}
        priority: {{ priority }}
        endpointLocation: "{{ endpointLocation }}"
        endpointMonitorStatus: "{{ endpointMonitorStatus }}"
        minChildEndpoints: {{ minChildEndpoints }}
        minChildEndpointsIPv4: {{ minChildEndpointsIPv4 }}
        minChildEndpointsIPv6: {{ minChildEndpointsIPv6 }}
        geoMapping:
          - "{{ geoMapping }}"
        subnets:
          - first: "{{ first }}"
            last: "{{ last }}"
            scope: {{ scope }}
        customHeaders:
          - name: "{{ name }}"
            value: "{{ value }}"
        alwaysServe: "{{ alwaysServe }}"
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

Update a Traffic Manager endpoint.

```sql
UPDATE azure.trafficmanager.endpoints
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_type = '{{ endpoint_type }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Create or update a Traffic Manager endpoint.

```sql
REPLACE azure.trafficmanager.endpoints
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_type = '{{ endpoint_type }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Deletes a Traffic Manager endpoint.

```sql
DELETE FROM azure.trafficmanager.endpoints
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_type = '{{ endpoint_type }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
