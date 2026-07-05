--- 
title: virtual_machine_images
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_images
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_images" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_with_properties', value: 'list_with_properties' },
        { label: 'list', value: 'list' },
        { label: 'list_skus', value: 'list_skus' },
        { label: 'list_by_edge_zone', value: 'list_by_edge_zone' },
        { label: 'list_offers', value: 'list_offers' },
        { label: 'list_publishers', value: 'list_publishers' }
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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="architecture" /></td>
    <td><code>string</code></td>
    <td>Specifies the Architecture Type. Known values are: "x64" and "Arm64". (x64, Arm64)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticOSUpgradeProperties" /></td>
    <td><code>object</code></td>
    <td>Describes automatic OS upgrade properties on the image.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskImages" /></td>
    <td><code>array</code></td>
    <td>The list of data disk images information.</td>
</tr>
<tr>
    <td><CopyableCode code="disallowed" /></td>
    <td><code>object</code></td>
    <td>Specifies disallowed configuration for the VirtualMachine created from the image.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>:vartype features: list[~azure.mgmt.compute.models.VirtualMachineImageFeature]</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>Specifies the HyperVGeneration Type. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="imageDeprecationStatus" /></td>
    <td><code>object</code></td>
    <td>Describes image deprecation status properties on the image.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskImage" /></td>
    <td><code>object</code></td>
    <td>Contains the os disk image information.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Used for establishing the purchase context of any 3rd Party artifact through MarketPlace.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_with_properties">

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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="architecture" /></td>
    <td><code>string</code></td>
    <td>Specifies the Architecture Type. Known values are: "x64" and "Arm64". (x64, Arm64)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticOSUpgradeProperties" /></td>
    <td><code>object</code></td>
    <td>Describes automatic OS upgrade properties on the image.</td>
</tr>
<tr>
    <td><CopyableCode code="dataDiskImages" /></td>
    <td><code>array</code></td>
    <td>The list of data disk images information.</td>
</tr>
<tr>
    <td><CopyableCode code="disallowed" /></td>
    <td><code>object</code></td>
    <td>Specifies disallowed configuration for the VirtualMachine created from the image.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>:vartype features: list[~azure.mgmt.compute.models.VirtualMachineImageFeature]</td>
</tr>
<tr>
    <td><CopyableCode code="hyperVGeneration" /></td>
    <td><code>string</code></td>
    <td>Specifies the HyperVGeneration Type. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="imageDeprecationStatus" /></td>
    <td><code>object</code></td>
    <td>Describes image deprecation status properties on the image.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osDiskImage" /></td>
    <td><code>object</code></td>
    <td>Contains the os disk image information.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Used for establishing the purchase context of any 3rd Party artifact through MarketPlace.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_skus">

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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_edge_zone">

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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_offers">

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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_publishers">

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
    <td>The name of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>The extended location of the Virtual Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The supported Azure location of the resource. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Specifies the tags that are assigned to the virtual machine. For more information about using tags, see `Using tags to organize your Azure resources `_.</td>
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
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-offer"><code>offer</code></a>, <a href="#parameter-skus"><code>skus</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a virtual machine image.</td>
</tr>
<tr>
    <td><a href="#list_with_properties"><CopyableCode code="list_with_properties" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-offer"><code>offer</code></a>, <a href="#parameter-skus"><code>skus</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>list_with_properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-offer"><code>offer</code></a>, <a href="#parameter-skus"><code>skus</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU.</td>
</tr>
<tr>
    <td><a href="#list_skus"><CopyableCode code="list_skus" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-offer"><code>offer</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.</td>
</tr>
<tr>
    <td><a href="#list_by_edge_zone"><CopyableCode code="list_by_edge_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-edge_zone"><code>edge_zone</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all virtual machine image versions for the specified edge zone.</td>
</tr>
<tr>
    <td><a href="#list_offers"><CopyableCode code="list_offers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of virtual machine image offers for the specified location and publisher.</td>
</tr>
<tr>
    <td><a href="#list_publishers"><CopyableCode code="list_publishers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of virtual machine image publishers for the specified Azure location.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. Required.</td>
</tr>
<tr id="parameter-edge_zone">
    <td><CopyableCode code="edge_zone" /></td>
    <td><code>string</code></td>
    <td>The name of the edge zone. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-offer">
    <td><CopyableCode code="offer" /></td>
    <td><code>string</code></td>
    <td>A valid image publisher offer. Required.</td>
</tr>
<tr id="parameter-publisher_name">
    <td><CopyableCode code="publisher_name" /></td>
    <td><code>string</code></td>
    <td>A valid image publisher. Required.</td>
</tr>
<tr id="parameter-skus">
    <td><CopyableCode code="skus" /></td>
    <td><code>string</code></td>
    <td>A valid image SKU. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>A valid image SKU version. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_with_properties', value: 'list_with_properties' },
        { label: 'list', value: 'list' },
        { label: 'list_skus', value: 'list_skus' },
        { label: 'list_by_edge_zone', value: 'list_by_edge_zone' },
        { label: 'list_offers', value: 'list_offers' },
        { label: 'list_publishers', value: 'list_publishers' }
    ]}
>
<TabItem value="get">

Gets a virtual machine image.

```sql
SELECT
id,
name,
architecture,
automaticOSUpgradeProperties,
dataDiskImages,
disallowed,
extendedLocation,
features,
hyperVGeneration,
imageDeprecationStatus,
location,
osDiskImage,
plan,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND offer = '{{ offer }}' -- required
AND skus = '{{ skus }}' -- required
AND version = '{{ version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_with_properties">

list_with_properties.

```sql
SELECT
id,
name,
architecture,
automaticOSUpgradeProperties,
dataDiskImages,
disallowed,
extendedLocation,
features,
hyperVGeneration,
imageDeprecationStatus,
location,
osDiskImage,
plan,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND offer = '{{ offer }}' -- required
AND skus = '{{ skus }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}' -- required
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU.

```sql
SELECT
id,
name,
extendedLocation,
location,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND offer = '{{ offer }}' -- required
AND skus = '{{ skus }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
<TabItem value="list_skus">

Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.

```sql
SELECT
id,
name,
extendedLocation,
location,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND offer = '{{ offer }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_edge_zone">

Gets a list of all virtual machine image versions for the specified edge zone.

```sql
SELECT
id,
name,
extendedLocation,
location,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND edge_zone = '{{ edge_zone }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_offers">

Gets a list of virtual machine image offers for the specified location and publisher.

```sql
SELECT
id,
name,
extendedLocation,
location,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_publishers">

Gets a list of virtual machine image publishers for the specified Azure location.

```sql
SELECT
id,
name,
extendedLocation,
location,
tags
FROM azure.compute.virtual_machine_images
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
