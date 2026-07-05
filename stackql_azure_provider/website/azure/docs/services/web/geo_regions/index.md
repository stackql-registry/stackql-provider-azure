--- 
title: geo_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - geo_regions
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

Creates, updates, deletes, gets or lists a <code>geo_regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="geo_regions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.geo_regions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_geo_regions"
    values={[
        { label: 'list_geo_regions', value: 'list_geo_regions' }
    ]}
>
<TabItem value="list_geo_regions">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Region description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for region.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="orgDomain" /></td>
    <td><code>string</code></td>
    <td>Display name for region.</td>
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
    <td><a href="#list_geo_regions"><CopyableCode code="list_geo_regions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-linuxWorkersEnabled"><code>linuxWorkersEnabled</code></a>, <a href="#parameter-xenonWorkersEnabled"><code>xenonWorkersEnabled</code></a>, <a href="#parameter-linuxDynamicWorkersEnabled"><code>linuxDynamicWorkersEnabled</code></a>, <a href="#parameter-customModeWorkersEnabled"><code>customModeWorkersEnabled</code></a></td>
    <td>Get a list of available geographical regions. Description for Get a list of available geographical regions.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-customModeWorkersEnabled">
    <td><CopyableCode code="customModeWorkersEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specify true if you want to filter to only regions that support App Service Plans with IsCustomMode set to true. Default value is None.</td>
</tr>
<tr id="parameter-linuxDynamicWorkersEnabled">
    <td><CopyableCode code="linuxDynamicWorkersEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specify true if you want to filter to only regions that support Linux Consumption Workers. Default value is None.</td>
</tr>
<tr id="parameter-linuxWorkersEnabled">
    <td><CopyableCode code="linuxWorkersEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specify true if you want to filter to only regions that support Linux workers. Default value is None.</td>
</tr>
<tr id="parameter-sku">
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Name of SKU used to filter the regions. Known values are: "Free", "Shared", "Basic", "Standard", "Premium", "Dynamic", "Isolated", "IsolatedV2", "PremiumV2", "PremiumV3", "PremiumContainer", "ElasticPremium", "ElasticIsolated", and "FlexConsumption". Default value is None.</td>
</tr>
<tr id="parameter-xenonWorkersEnabled">
    <td><CopyableCode code="xenonWorkersEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specify true if you want to filter to only regions that support Xenon workers. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_geo_regions"
    values={[
        { label: 'list_geo_regions', value: 'list_geo_regions' }
    ]}
>
<TabItem value="list_geo_regions">

Get a list of available geographical regions. Description for Get a list of available geographical regions.

```sql
SELECT
id,
name,
description,
displayName,
kind,
orgDomain,
type
FROM azure.web.geo_regions
WHERE subscription_id = '{{ subscription_id }}' -- required
AND sku = '{{ sku }}'
AND linuxWorkersEnabled = '{{ linuxWorkersEnabled }}'
AND xenonWorkersEnabled = '{{ xenonWorkersEnabled }}'
AND linuxDynamicWorkersEnabled = '{{ linuxDynamicWorkersEnabled }}'
AND customModeWorkersEnabled = '{{ customModeWorkersEnabled }}'
;
```
</TabItem>
</Tabs>
