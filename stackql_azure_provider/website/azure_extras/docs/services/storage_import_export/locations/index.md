--- 
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - storage_import_export
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storage_import_export.locations" /></td></tr>
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
    <td>Specifies the resource identifier of the location.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the location. Use List Locations to get all supported locations.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalShippingInformation" /></td>
    <td><code>string</code></td>
    <td>Additional shipping information for customer, specific to datacenter to which customer should send their disks.</td>
</tr>
<tr>
    <td><CopyableCode code="alternateLocations" /></td>
    <td><code>array</code></td>
    <td>A list of location IDs that should be used to ship shipping drives to for jobs created against the current location. If the current location is active, it will be part of the list. If it is temporarily closed due to maintenance, this list may contain other locations.</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>The city name to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="countryOrRegion" /></td>
    <td><code>string</code></td>
    <td>The country or region to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="phone" /></td>
    <td><code>string</code></td>
    <td>The phone number for the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>The postal code to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="recipientName" /></td>
    <td><code>string</code></td>
    <td>The recipient name to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="stateOrProvince" /></td>
    <td><code>string</code></td>
    <td>The state or province to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress1" /></td>
    <td><code>string</code></td>
    <td>The first line of the street address to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress2" /></td>
    <td><code>string</code></td>
    <td>The second line of the street address to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCarriers" /></td>
    <td><code>array</code></td>
    <td>A list of carriers that are supported at this location.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the location.</td>
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
    <td>Specifies the resource identifier of the location.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the location. Use List Locations to get all supported locations.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalShippingInformation" /></td>
    <td><code>string</code></td>
    <td>Additional shipping information for customer, specific to datacenter to which customer should send their disks.</td>
</tr>
<tr>
    <td><CopyableCode code="alternateLocations" /></td>
    <td><code>array</code></td>
    <td>A list of location IDs that should be used to ship shipping drives to for jobs created against the current location. If the current location is active, it will be part of the list. If it is temporarily closed due to maintenance, this list may contain other locations.</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>The city name to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="countryOrRegion" /></td>
    <td><code>string</code></td>
    <td>The country or region to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="phone" /></td>
    <td><code>string</code></td>
    <td>The phone number for the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>The postal code to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="recipientName" /></td>
    <td><code>string</code></td>
    <td>The recipient name to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="stateOrProvince" /></td>
    <td><code>string</code></td>
    <td>The state or province to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress1" /></td>
    <td><code>string</code></td>
    <td>The first line of the street address to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress2" /></td>
    <td><code>string</code></td>
    <td>The second line of the street address to use when shipping the drives to the Azure data center.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedCarriers" /></td>
    <td><code>array</code></td>
    <td>A list of carriers that are supported at this location.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of the location.</td>
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
    <td><a href="#parameter-location_name"><code>location_name</code></a></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a></td>
    <td>Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The name of the location. For example, West US or westus. Required.</td>
</tr>
<tr id="parameter-Accept-Language">
    <td><CopyableCode code="Accept-Language" /></td>
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

Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region.

```sql
SELECT
id,
name,
additionalShippingInformation,
alternateLocations,
city,
countryOrRegion,
phone,
postalCode,
recipientName,
stateOrProvince,
streetAddress1,
streetAddress2,
supportedCarriers,
type
FROM azure_extras.storage_import_export.locations
WHERE location_name = '{{ location_name }}' -- required
AND Accept-Language = '{{ Accept-Language }}'
;
```
</TabItem>
<TabItem value="list">

Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region.

```sql
SELECT
id,
name,
additionalShippingInformation,
alternateLocations,
city,
countryOrRegion,
phone,
postalCode,
recipientName,
stateOrProvince,
streetAddress1,
streetAddress2,
supportedCarriers,
type
FROM azure_extras.storage_import_export.locations
WHERE Accept-Language = '{{ Accept-Language }}'
;
```
</TabItem>
</Tabs>
