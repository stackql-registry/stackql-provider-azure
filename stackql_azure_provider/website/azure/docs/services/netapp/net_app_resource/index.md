--- 
title: net_app_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - net_app_resource
  - netapp
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

Creates, updates, deletes, gets or lists a <code>net_app_resource</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="net_app_resource" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.netapp.net_app_resource" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'check_file_path_availability', value: 'check_file_path_availability' },
        { label: 'query_network_sibling_set', value: 'query_network_sibling_set' }
    ]}
>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="isAvailable" /></td>
    <td><code>boolean</code></td>
    <td>true indicates name is valid and available. false indicates the name is invalid, unavailable, or both.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>If reason == invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason == AlreadyExists, explain that resource name is already in use, and direct them to select a different name.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Invalid indicates the name provided does not match Azure App Service naming requirements. AlreadyExists indicates that the name is already in use and is therefore unavailable. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_file_path_availability">

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
    <td><CopyableCode code="isAvailable" /></td>
    <td><code>boolean</code></td>
    <td>true indicates name is valid and available. false indicates the name is invalid, unavailable, or both.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>If reason == invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason == AlreadyExists, explain that resource name is already in use, and direct them to select a different name.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Invalid indicates the name provided does not match Azure App Service naming requirements. AlreadyExists indicates that the name is already in use and is therefore unavailable. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="query_network_sibling_set">

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
    <td><CopyableCode code="networkFeatures" /></td>
    <td><code>string</code></td>
    <td>Network features available to the volume, or current state of update. Known values are: "Basic", "Standard", "Basic_Standard", and "Standard_Basic". (Basic, Standard, Basic_Standard, Standard_Basic)</td>
</tr>
<tr>
    <td><CopyableCode code="networkSiblingSetId" /></td>
    <td><code>string</code></td>
    <td>Network Sibling Set ID for a group of volumes sharing networking resources in a subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSiblingSetStateId" /></td>
    <td><code>string</code></td>
    <td>Network sibling set state Id identifying the current state of the sibling set.</td>
</tr>
<tr>
    <td><CopyableCode code="nicInfoList" /></td>
    <td><code>array</code></td>
    <td>List of NIC information.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets the status of the NetworkSiblingSet at the time the operation was called. Known values are: "Succeeded", "Failed", "Canceled", and "Updating". (Succeeded, Failed, Canceled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes. Example /subscriptions/subscriptionId/resourceGroups/resourceGroup/providers/Microsoft.Network/virtualNetworks/testVnet/subnets/&#123;mySubnet&#125;.</td>
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
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check resource name availability. Check if a resource name is available.</td>
</tr>
<tr>
    <td><a href="#check_file_path_availability"><CopyableCode code="check_file_path_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check file path availability. Check if a file path is available.</td>
</tr>
<tr>
    <td><a href="#query_network_sibling_set"><CopyableCode code="query_network_sibling_set" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Describe a network sibling set. Get details of the specified network sibling set.</td>
</tr>
<tr>
    <td><a href="#check_quota_availability"><CopyableCode code="check_quota_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-resourceGroup"><code>resourceGroup</code></a></td>
    <td></td>
    <td>Check quota availability. Check if a quota is available.</td>
</tr>
<tr>
    <td><a href="#query_region_info"><CopyableCode code="query_region_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Describes region specific information. Provides storage to network proximity and logical zone mapping information.</td>
</tr>
<tr>
    <td><a href="#update_network_sibling_set"><CopyableCode code="update_network_sibling_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-networkSiblingSetId"><code>networkSiblingSetId</code></a>, <a href="#parameter-subnetId"><code>subnetId</code></a>, <a href="#parameter-networkSiblingSetStateId"><code>networkSiblingSetStateId</code></a>, <a href="#parameter-networkFeatures"><code>networkFeatures</code></a></td>
    <td></td>
    <td>Update the network features of a network sibling set. Update the network features of the specified network sibling set.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
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
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'check_file_path_availability', value: 'check_file_path_availability' },
        { label: 'query_network_sibling_set', value: 'query_network_sibling_set' }
    ]}
>
<TabItem value="check_name_availability">

Check resource name availability. Check if a resource name is available.

```sql
SELECT
isAvailable,
message,
reason
FROM azure.netapp.net_app_resource
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_file_path_availability">

Check file path availability. Check if a file path is available.

```sql
SELECT
isAvailable,
message,
reason
FROM azure.netapp.net_app_resource
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="query_network_sibling_set">

Describe a network sibling set. Get details of the specified network sibling set.

```sql
SELECT
networkFeatures,
networkSiblingSetId,
networkSiblingSetStateId,
nicInfoList,
provisioningState,
subnetId
FROM azure.netapp.net_app_resource
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_quota_availability"
    values={[
        { label: 'check_quota_availability', value: 'check_quota_availability' },
        { label: 'query_region_info', value: 'query_region_info' },
        { label: 'update_network_sibling_set', value: 'update_network_sibling_set' }
    ]}
>
<TabItem value="check_quota_availability">

Check quota availability. Check if a quota is available.

```sql
EXEC azure.netapp.net_app_resource.check_quota_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}", 
"resourceGroup": "{{ resourceGroup }}"
}'
;
```
</TabItem>
<TabItem value="query_region_info">

Describes region specific information. Provides storage to network proximity and logical zone mapping information.

```sql
EXEC azure.netapp.net_app_resource.query_region_info 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_network_sibling_set">

Update the network features of a network sibling set. Update the network features of the specified network sibling set.

```sql
EXEC azure.netapp.net_app_resource.update_network_sibling_set 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"networkSiblingSetId": "{{ networkSiblingSetId }}", 
"subnetId": "{{ subnetId }}", 
"networkSiblingSetStateId": "{{ networkSiblingSetStateId }}", 
"networkFeatures": "{{ networkFeatures }}"
}'
;
```
</TabItem>
</Tabs>
