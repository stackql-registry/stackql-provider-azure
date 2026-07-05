--- 
title: check_dns_name_availabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - check_dns_name_availabilities
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

Creates, updates, deletes, gets or lists a <code>check_dns_name_availabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="check_dns_name_availabilities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.check_dns_name_availabilities" /></td></tr>
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
    <td><a href="#check_dns_name_availability"><CopyableCode code="check_dns_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-domainNameLabel"><code>domainNameLabel</code></a></td>
    <td></td>
    <td>Checks whether a domain name in the cloudapp.azure.com zone is available for use.</td>
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
<tr id="parameter-domainNameLabel">
    <td><CopyableCode code="domainNameLabel" /></td>
    <td><code>string</code></td>
    <td>The domain name to be verified. It must conform to the following regular expression: ^[a-z][a-z0-9-]&#123;1,61&#125;[a-z0-9]$. Required.</td>
</tr>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="check_dns_name_availability"
    values={[
        { label: 'check_dns_name_availability', value: 'check_dns_name_availability' }
    ]}
>
<TabItem value="check_dns_name_availability">

Checks whether a domain name in the cloudapp.azure.com zone is available for use.

```sql
EXEC azure.network.check_dns_name_availabilities.check_dns_name_availability 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@domainNameLabel='{{ domainNameLabel }}' --required
;
```
</TabItem>
</Tabs>
