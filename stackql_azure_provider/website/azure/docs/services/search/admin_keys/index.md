--- 
title: admin_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_keys
  - search
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

Creates, updates, deletes, gets or lists an <code>admin_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="admin_keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.admin_keys" /></td></tr>
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
    <td><a href="#regenerate"><CopyableCode code="regenerate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-key_kind"><code>key_kind</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Regenerates either the primary or secondary admin API key. You can only regenerate one key at a time.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-search_service_name"><code>search_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the primary and secondary admin API keys for the specified Azure AI Search service.</td>
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
<tr id="parameter-key_kind">
    <td><CopyableCode code="key_kind" /></td>
    <td><code>string</code></td>
    <td>Specifies which key to regenerate. Valid values include 'primary' and 'secondary'. Known values are: "primary" and "secondary". Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-search_service_name">
    <td><CopyableCode code="search_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure AI Search service associated with the specified resource group. Required.</td>
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
    defaultValue="regenerate"
    values={[
        { label: 'regenerate', value: 'regenerate' },
        { label: 'get_raw', value: 'get_raw' }
    ]}
>
<TabItem value="regenerate">

Regenerates either the primary or secondary admin API key. You can only regenerate one key at a time.

```sql
EXEC azure.search.admin_keys.regenerate 
@resource_group_name='{{ resource_group_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required, 
@key_kind='{{ key_kind }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_raw">

Gets the primary and secondary admin API keys for the specified Azure AI Search service.

```sql
EXEC azure.search.admin_keys.get_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@search_service_name='{{ search_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
