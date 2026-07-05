--- 
title: exposure_control
hide_title: false
hide_table_of_contents: false
keywords:
  - exposure_control
  - datafactory
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

Creates, updates, deletes, gets or lists an <code>exposure_control</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exposure_control" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datafactory.exposure_control" /></td></tr>
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
    <td><a href="#get_feature_value_by_factory"><CopyableCode code="get_feature_value_by_factory" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get exposure control feature for specific factory.</td>
</tr>
<tr>
    <td><a href="#get_feature_value"><CopyableCode code="get_feature_value" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_id"><code>location_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get exposure control feature for specific location.</td>
</tr>
<tr>
    <td><a href="#query_feature_values_by_factory"><CopyableCode code="query_feature_values_by_factory" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-factory_name"><code>factory_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-exposureControlRequests"><code>exposureControlRequests</code></a></td>
    <td></td>
    <td>Get list of exposure control features for specific factory.</td>
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
<tr id="parameter-factory_name">
    <td><CopyableCode code="factory_name" /></td>
    <td><code>string</code></td>
    <td>The factory name. Required.</td>
</tr>
<tr id="parameter-location_id">
    <td><CopyableCode code="location_id" /></td>
    <td><code>string</code></td>
    <td>The location identifier. Required.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="get_feature_value_by_factory"
    values={[
        { label: 'get_feature_value_by_factory', value: 'get_feature_value_by_factory' },
        { label: 'get_feature_value', value: 'get_feature_value' },
        { label: 'query_feature_values_by_factory', value: 'query_feature_values_by_factory' }
    ]}
>
<TabItem value="get_feature_value_by_factory">

Get exposure control feature for specific factory.

```sql
EXEC azure.datafactory.exposure_control.get_feature_value_by_factory 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"featureName": "{{ featureName }}", 
"featureType": "{{ featureType }}"
}'
;
```
</TabItem>
<TabItem value="get_feature_value">

Get exposure control feature for specific location.

```sql
EXEC azure.datafactory.exposure_control.get_feature_value 
@location_id='{{ location_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"featureName": "{{ featureName }}", 
"featureType": "{{ featureType }}"
}'
;
```
</TabItem>
<TabItem value="query_feature_values_by_factory">

Get list of exposure control features for specific factory.

```sql
EXEC azure.datafactory.exposure_control.query_feature_values_by_factory 
@resource_group_name='{{ resource_group_name }}' --required, 
@factory_name='{{ factory_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"exposureControlRequests": "{{ exposureControlRequests }}"
}'
;
```
</TabItem>
</Tabs>
