--- 
title: sap_availability_zone_details
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_availability_zone_details
  - workloads
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

Creates, updates, deletes, gets or lists a <code>sap_availability_zone_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sap_availability_zone_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.workloads.sap_availability_zone_details" /></td></tr>
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
    <td><a href="#sap_availability_zone_details"><CopyableCode code="sap_availability_zone_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-appLocation"><code>appLocation</code></a>, <a href="#parameter-sapProduct"><code>sapProduct</code></a>, <a href="#parameter-databaseType"><code>databaseType</code></a></td>
    <td></td>
    <td>Get the recommended SAP Availability Zone Pair Details for your region.</td>
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
    <td>The name of Azure region. Required.</td>
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
    defaultValue="sap_availability_zone_details"
    values={[
        { label: 'sap_availability_zone_details', value: 'sap_availability_zone_details' }
    ]}
>
<TabItem value="sap_availability_zone_details">

Get the recommended SAP Availability Zone Pair Details for your region.

```sql
EXEC azure_isv.workloads.sap_availability_zone_details.sap_availability_zone_details 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appLocation": "{{ appLocation }}", 
"sapProduct": "{{ sapProduct }}", 
"databaseType": "{{ databaseType }}"
}'
;
```
</TabItem>
</Tabs>
