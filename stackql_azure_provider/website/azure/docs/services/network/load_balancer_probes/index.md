--- 
title: load_balancer_probes
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_probes
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

Creates, updates, deletes, gets or lists a <code>load_balancer_probes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancer_probes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_probes" /></td></tr>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="intervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than half the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default value is 15, the minimum value is 5.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>The load balancer rules that use this probe.</td>
</tr>
<tr>
    <td><CopyableCode code="noHealthyBackendsBehavior" /></td>
    <td><code>string</code></td>
    <td>Determines how new connections are handled by the load balancer when all backend instances are probed down. Known values are: "AllProbedDown" and "AllProbedUp". (AllProbedDown, AllProbedUp)</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfProbes" /></td>
    <td><code>integer</code></td>
    <td>The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port for communicating the probe. Possible values range from 1 to 65535, inclusive. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="probeThreshold" /></td>
    <td><code>integer</code></td>
    <td>The number of consecutive successful or failed probes in order to allow or deny traffic from being delivered to this endpoint. After failing the number of consecutive probes equal to this value, the endpoint will be taken out of rotation and require the same number of successful consecutive probes to be placed back in rotation.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI is required for the probe to be successful. Required. Known values are: "Http", "Tcp", and "Https". (Http, Tcp, Https)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the probe resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="requestPath" /></td>
    <td><code>string</code></td>
    <td>The URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. There is no default value.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="intervalInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The interval, in seconds, for how frequently to probe the endpoint for health status. Typically, the interval is slightly less than half the allocated timeout period (in seconds) which allows two full probes before taking the instance out of rotation. The default value is 15, the minimum value is 5.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancingRules" /></td>
    <td><code>array</code></td>
    <td>The load balancer rules that use this probe.</td>
</tr>
<tr>
    <td><CopyableCode code="noHealthyBackendsBehavior" /></td>
    <td><code>string</code></td>
    <td>Determines how new connections are handled by the load balancer when all backend instances are probed down. Known values are: "AllProbedDown" and "AllProbedUp". (AllProbedDown, AllProbedUp)</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfProbes" /></td>
    <td><code>integer</code></td>
    <td>The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint. This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port for communicating the probe. Possible values range from 1 to 65535, inclusive. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="probeThreshold" /></td>
    <td><code>integer</code></td>
    <td>The number of consecutive successful or failed probes in order to allow or deny traffic from being delivered to this endpoint. After failing the number of consecutive probes equal to this value, the endpoint will be taken out of rotation and require the same number of successful consecutive probes to be placed back in rotation.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI is required for the probe to be successful. Required. Known values are: "Http", "Tcp", and "Https". (Http, Tcp, Https)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the probe resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="requestPath" /></td>
    <td><code>string</code></td>
    <td>The URI used for requesting health status from the VM. Path is required if a protocol is set to http. Otherwise, it is not allowed. There is no default value.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-probe_name"><code>probe_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets load balancer probe.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-load_balancer_name"><code>load_balancer_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the load balancer probes.</td>
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
<tr id="parameter-load_balancer_name">
    <td><CopyableCode code="load_balancer_name" /></td>
    <td><code>string</code></td>
    <td>The name of the load balancer. Required.</td>
</tr>
<tr id="parameter-probe_name">
    <td><CopyableCode code="probe_name" /></td>
    <td><code>string</code></td>
    <td>The name of the probe. Required.</td>
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

Gets load balancer probe.

```sql
SELECT
id,
name,
etag,
intervalInSeconds,
loadBalancingRules,
noHealthyBackendsBehavior,
numberOfProbes,
port,
probeThreshold,
protocol,
provisioningState,
requestPath,
type
FROM azure.network.load_balancer_probes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND probe_name = '{{ probe_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all the load balancer probes.

```sql
SELECT
id,
name,
etag,
intervalInSeconds,
loadBalancingRules,
noHealthyBackendsBehavior,
numberOfProbes,
port,
probeThreshold,
protocol,
provisioningState,
requestPath,
type
FROM azure.network.load_balancer_probes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND load_balancer_name = '{{ load_balancer_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
