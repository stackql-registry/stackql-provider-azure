--- 
title: sap_supported_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_supported_skus
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

Creates, updates, deletes, gets or lists a <code>sap_supported_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sap_supported_skus" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.workloads.sap_supported_skus" /></td></tr>
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
    <td><a href="#sap_supported_sku"><CopyableCode code="sap_supported_sku" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-appLocation"><code>appLocation</code></a>, <a href="#parameter-environment"><code>environment</code></a>, <a href="#parameter-sapProduct"><code>sapProduct</code></a>, <a href="#parameter-deploymentType"><code>deploymentType</code></a>, <a href="#parameter-databaseType"><code>databaseType</code></a></td>
    <td></td>
    <td>Get a list of SAP supported SKUs for ASCS, Application and Database tier.</td>
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
    defaultValue="sap_supported_sku"
    values={[
        { label: 'sap_supported_sku', value: 'sap_supported_sku' }
    ]}
>
<TabItem value="sap_supported_sku">

Get a list of SAP supported SKUs for ASCS, Application and Database tier.

```sql
EXEC azure_isv.workloads.sap_supported_skus.sap_supported_sku 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appLocation": "{{ appLocation }}", 
"environment": "{{ environment }}", 
"sapProduct": "{{ sapProduct }}", 
"deploymentType": "{{ deploymentType }}", 
"databaseType": "{{ databaseType }}", 
"highAvailabilityType": "{{ highAvailabilityType }}"
}'
;
```
</TabItem>
</Tabs>
