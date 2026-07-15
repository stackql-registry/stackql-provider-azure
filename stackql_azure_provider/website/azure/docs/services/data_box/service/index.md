--- 
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - data_box
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

Creates, updates, deletes, gets or lists a <code>service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box.service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_available_skus_by_resource_group"
    values={[
        { label: 'list_available_skus_by_resource_group', value: 'list_available_skus_by_resource_group' }
    ]}
>
<TabItem value="list_available_skus_by_resource_group">

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
    <td><CopyableCode code="apiVersions" /></td>
    <td><code>array</code></td>
    <td>Api versions that support this Sku.</td>
</tr>
<tr>
    <td><CopyableCode code="capacity" /></td>
    <td><code>object</code></td>
    <td>Capacity of the Sku.</td>
</tr>
<tr>
    <td><CopyableCode code="costs" /></td>
    <td><code>array</code></td>
    <td>Cost of the Sku.</td>
</tr>
<tr>
    <td><CopyableCode code="countriesWithinCommerceBoundary" /></td>
    <td><code>array</code></td>
    <td>List of all the Countries in the SKU specific commerce boundary.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLocationToServiceLocationMap" /></td>
    <td><code>array</code></td>
    <td>The map of data location to service location.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledReason" /></td>
    <td><code>string</code></td>
    <td>Reason why the Sku is disabled. Known values are: "None", "Country", "Region", "Feature", "OfferType", and "NoSubscriptionInfo".</td>
</tr>
<tr>
    <td><CopyableCode code="disabledReasonMessage" /></td>
    <td><code>string</code></td>
    <td>Message for why the Sku is disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The sku is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredFeature" /></td>
    <td><code>string</code></td>
    <td>Required feature to access the sku.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Sku.</td>
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
    <td><a href="#list_available_skus_by_resource_group"><CopyableCode code="list_available_skus_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This method provides the list of available skus for the given subscription, resource group and location.</td>
</tr>
<tr>
    <td><a href="#validate_address"><CopyableCode code="validate_address" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-validationType"><code>validationType</code></a>, <a href="#parameter-shippingAddress"><code>shippingAddress</code></a>, <a href="#parameter-deviceType"><code>deviceType</code></a></td>
    <td></td>
    <td>[DEPRECATED NOTICE: This operation will soon be removed]. This method validates the customer shipping address and provide alternate addresses if any.</td>
</tr>
<tr>
    <td><a href="#validate_inputs_by_resource_group"><CopyableCode code="validate_inputs_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-validationCategory"><code>validationCategory</code></a>, <a href="#parameter-individualRequestDetails"><code>individualRequestDetails</code></a></td>
    <td></td>
    <td>This method does all necessary pre-job creation validation under resource group.</td>
</tr>
<tr>
    <td><a href="#validate_inputs"><CopyableCode code="validate_inputs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-validationCategory"><code>validationCategory</code></a>, <a href="#parameter-individualRequestDetails"><code>individualRequestDetails</code></a></td>
    <td></td>
    <td>This method does all necessary pre-job creation validation under subscription.</td>
</tr>
<tr>
    <td><a href="#region_configuration"><CopyableCode code="region_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This API provides configuration details specific to given region/location at Subscription level.</td>
</tr>
<tr>
    <td><a href="#region_configuration_by_resource_group"><CopyableCode code="region_configuration_by_resource_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This API provides configuration details specific to given region/location at Resource group level.</td>
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
    <td>The location of the resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The Resource Group Name. Required.</td>
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
    defaultValue="list_available_skus_by_resource_group"
    values={[
        { label: 'list_available_skus_by_resource_group', value: 'list_available_skus_by_resource_group' }
    ]}
>
<TabItem value="list_available_skus_by_resource_group">

This method provides the list of available skus for the given subscription, resource group and location.

```sql
SELECT
apiVersions,
capacity,
costs,
countriesWithinCommerceBoundary,
dataLocationToServiceLocationMap,
disabledReason,
disabledReasonMessage,
enabled,
requiredFeature,
sku
FROM azure.data_box.service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_address"
    values={[
        { label: 'validate_address', value: 'validate_address' },
        { label: 'validate_inputs_by_resource_group', value: 'validate_inputs_by_resource_group' },
        { label: 'validate_inputs', value: 'validate_inputs' },
        { label: 'region_configuration', value: 'region_configuration' },
        { label: 'region_configuration_by_resource_group', value: 'region_configuration_by_resource_group' }
    ]}
>
<TabItem value="validate_address">

[DEPRECATED NOTICE: This operation will soon be removed]. This method validates the customer shipping address and provide alternate addresses if any.

```sql
EXEC azure.data_box.service.validate_address 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validationType": "{{ validationType }}", 
"shippingAddress": "{{ shippingAddress }}", 
"deviceType": "{{ deviceType }}", 
"transportPreferences": "{{ transportPreferences }}", 
"model": "{{ model }}"
}'
;
```
</TabItem>
<TabItem value="validate_inputs_by_resource_group">

This method does all necessary pre-job creation validation under resource group.

```sql
EXEC azure.data_box.service.validate_inputs_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validationCategory": "{{ validationCategory }}", 
"individualRequestDetails": "{{ individualRequestDetails }}"
}'
;
```
</TabItem>
<TabItem value="validate_inputs">

This method does all necessary pre-job creation validation under subscription.

```sql
EXEC azure.data_box.service.validate_inputs 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"validationCategory": "{{ validationCategory }}", 
"individualRequestDetails": "{{ individualRequestDetails }}"
}'
;
```
</TabItem>
<TabItem value="region_configuration">

This API provides configuration details specific to given region/location at Subscription level.

```sql
EXEC azure.data_box.service.region_configuration 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"scheduleAvailabilityRequest": "{{ scheduleAvailabilityRequest }}", 
"transportAvailabilityRequest": "{{ transportAvailabilityRequest }}", 
"datacenterAddressRequest": "{{ datacenterAddressRequest }}", 
"deviceCapabilityRequest": "{{ deviceCapabilityRequest }}"
}'
;
```
</TabItem>
<TabItem value="region_configuration_by_resource_group">

This API provides configuration details specific to given region/location at Resource group level.

```sql
EXEC azure.data_box.service.region_configuration_by_resource_group 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"scheduleAvailabilityRequest": "{{ scheduleAvailabilityRequest }}", 
"transportAvailabilityRequest": "{{ transportAvailabilityRequest }}", 
"datacenterAddressRequest": "{{ datacenterAddressRequest }}", 
"deviceCapabilityRequest": "{{ deviceCapabilityRequest }}"
}'
;
```
</TabItem>
</Tabs>
