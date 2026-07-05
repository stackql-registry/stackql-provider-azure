--- 
title: service_tag_information
hide_title: false
hide_table_of_contents: false
keywords:
  - service_tag_information
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

Creates, updates, deletes, gets or lists a <code>service_tag_information</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_tag_information" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_tag_information" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>The ID of service tag.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of service tag.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>The list of IP address prefixes.</td>
</tr>
<tr>
    <td><CopyableCode code="changeNumber" /></td>
    <td><code>string</code></td>
    <td>The iteration number of service tag.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region of service tag.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTagChangeNumber" /></td>
    <td><code>string</code></td>
    <td>The iteration number of service tag object for region.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the service tag.</td>
</tr>
<tr>
    <td><CopyableCode code="systemService" /></td>
    <td><code>string</code></td>
    <td>The name of system service.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-noAddressPrefixes"><code>noAddressPrefixes</code></a>, <a href="#parameter-tagName"><code>tagName</code></a></td>
    <td>Gets a list of service tag information resources with pagination.</td>
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
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-noAddressPrefixes">
    <td><CopyableCode code="noAddressPrefixes" /></td>
    <td><code>boolean</code></td>
    <td>Do not return address prefixes for the tag(s). Default value is None.</td>
</tr>
<tr id="parameter-tagName">
    <td><CopyableCode code="tagName" /></td>
    <td><code>string</code></td>
    <td>Return tag information for a particular tag. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets a list of service tag information resources with pagination.

```sql
SELECT
id,
name,
addressPrefixes,
changeNumber,
region,
serviceTagChangeNumber,
state,
systemService
FROM azure.network.service_tag_information
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND noAddressPrefixes = '{{ noAddressPrefixes }}'
AND tagName = '{{ tagName }}'
;
```
</TabItem>
</Tabs>
