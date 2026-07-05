--- 
title: verify_hosting_environment_vnets
hide_title: false
hide_table_of_contents: false
keywords:
  - verify_hosting_environment_vnets
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

Creates, updates, deletes, gets or lists a <code>verify_hosting_environment_vnets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="verify_hosting_environment_vnets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.verify_hosting_environment_vnets" /></td></tr>
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
    <td><a href="#verify_hosting_environment_vnet"><CopyableCode code="verify_hosting_environment_vnet" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules. Description for Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="verify_hosting_environment_vnet"
    values={[
        { label: 'verify_hosting_environment_vnet', value: 'verify_hosting_environment_vnet' }
    ]}
>
<TabItem value="verify_hosting_environment_vnet">

Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules. Description for Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

```sql
EXEC azure.web.verify_hosting_environment_vnets.verify_hosting_environment_vnet 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
