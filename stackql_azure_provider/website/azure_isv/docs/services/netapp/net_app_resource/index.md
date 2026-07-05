--- 
title: net_app_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - net_app_resource
  - netapp
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.net_app_resource" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-resourceGroup"><code>resourceGroup</code></a></td>
    <td></td>
    <td>Check resource name availability. Check if a resource name is available.</td>
</tr>
<tr>
    <td><a href="#check_file_path_availability"><CopyableCode code="check_file_path_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subnetId"><code>subnetId</code></a></td>
    <td></td>
    <td>Check file path availability. Check if a file path is available.</td>
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
    <td><a href="#query_network_sibling_set"><CopyableCode code="query_network_sibling_set" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-networkSiblingSetId"><code>networkSiblingSetId</code></a>, <a href="#parameter-subnetId"><code>subnetId</code></a></td>
    <td></td>
    <td>Describe a network sibling set. Get details of the specified network sibling set.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'check_file_path_availability', value: 'check_file_path_availability' },
        { label: 'check_quota_availability', value: 'check_quota_availability' },
        { label: 'query_region_info', value: 'query_region_info' },
        { label: 'query_network_sibling_set', value: 'query_network_sibling_set' },
        { label: 'update_network_sibling_set', value: 'update_network_sibling_set' }
    ]}
>
<TabItem value="check_name_availability">

Check resource name availability. Check if a resource name is available.

```sql
EXEC azure_isv.netapp.net_app_resource.check_name_availability 
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
<TabItem value="check_file_path_availability">

Check file path availability. Check if a file path is available.

```sql
EXEC azure_isv.netapp.net_app_resource.check_file_path_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"subnetId": "{{ subnetId }}", 
"availabilityZone": "{{ availabilityZone }}"
}'
;
```
</TabItem>
<TabItem value="check_quota_availability">

Check quota availability. Check if a quota is available.

```sql
EXEC azure_isv.netapp.net_app_resource.check_quota_availability 
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
EXEC azure_isv.netapp.net_app_resource.query_region_info 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="query_network_sibling_set">

Describe a network sibling set. Get details of the specified network sibling set.

```sql
EXEC azure_isv.netapp.net_app_resource.query_network_sibling_set 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"networkSiblingSetId": "{{ networkSiblingSetId }}", 
"subnetId": "{{ subnetId }}"
}'
;
```
</TabItem>
<TabItem value="update_network_sibling_set">

Update the network features of a network sibling set. Update the network features of the specified network sibling set.

```sql
EXEC azure_isv.netapp.net_app_resource.update_network_sibling_set 
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
