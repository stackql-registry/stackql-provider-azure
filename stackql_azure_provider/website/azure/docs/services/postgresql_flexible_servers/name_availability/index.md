--- 
title: name_availability
hide_title: false
hide_table_of_contents: false
keywords:
  - name_availability
  - postgresql_flexible_servers
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

Creates, updates, deletes, gets or lists a <code>name_availability</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="name_availability" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_flexible_servers.name_availability" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="check_with_location"
    values={[
        { label: 'check_with_location', value: 'check_with_location' },
        { label: 'check_globally', value: 'check_globally' }
    ]}
>
<TabItem value="check_with_location">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name for which validity and availability was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Detailed reason why the given name is not available.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the resource name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason why the given name is not available. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of resource. It can be 'Microsoft.DBforPostgreSQL/flexibleServers' or 'Microsoft.DBforPostgreSQL/flexibleServers/virtualendpoints'.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_globally">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name for which validity and availability was checked.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Detailed reason why the given name is not available.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the resource name is available.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason why the given name is not available. Known values are: "Invalid" and "AlreadyExists". (Invalid, AlreadyExists)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of resource. It can be 'Microsoft.DBforPostgreSQL/flexibleServers' or 'Microsoft.DBforPostgreSQL/flexibleServers/virtualendpoints'.</td>
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
    <td><a href="#check_with_location"><CopyableCode code="check_with_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check the availability of name for resource.</td>
</tr>
<tr>
    <td><a href="#check_globally"><CopyableCode code="check_globally" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the validity and availability of the given name, to assign it to a new server or to use it as the base name of a new pair of virtual endpoints.</td>
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
    <td>The name of the location. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="check_with_location"
    values={[
        { label: 'check_with_location', value: 'check_with_location' },
        { label: 'check_globally', value: 'check_globally' }
    ]}
>
<TabItem value="check_with_location">

Check the availability of name for resource.

```sql
SELECT
name,
message,
nameAvailable,
reason,
type
FROM azure.postgresql_flexible_servers.name_availability
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_globally">

Checks the validity and availability of the given name, to assign it to a new server or to use it as the base name of a new pair of virtual endpoints.

```sql
SELECT
name,
message,
nameAvailable,
reason,
type
FROM azure.postgresql_flexible_servers.name_availability
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
