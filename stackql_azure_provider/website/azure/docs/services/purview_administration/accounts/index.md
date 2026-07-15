--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - purview_administration
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_administration.accounts" /></td></tr>
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
    <td><a href="#get_account_properties"><CopyableCode code="get_account_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an account.</td>
</tr>
<tr>
    <td><a href="#get_access_keys"><CopyableCode code="get_access_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List the authorization keys associated with this account.</td>
</tr>
<tr>
    <td><a href="#regenerate_access_key"><CopyableCode code="regenerate_access_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Regenerate the authorization keys associated with this data catalog.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_account_properties"
    values={[
        { label: 'get_account_properties', value: 'get_account_properties' },
        { label: 'get_access_keys', value: 'get_access_keys' },
        { label: 'regenerate_access_key', value: 'regenerate_access_key' }
    ]}
>
<TabItem value="get_account_properties">

Get an account.

```sql
EXEC azure.purview_administration.accounts.get_account_properties 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_access_keys">

List the authorization keys associated with this account.

```sql
EXEC azure.purview_administration.accounts.get_access_keys 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="regenerate_access_key">

Regenerate the authorization keys associated with this data catalog.

```sql
EXEC azure.purview_administration.accounts.regenerate_access_key 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
