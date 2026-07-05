--- 
title: name_availability
hide_title: false
hide_table_of_contents: false
keywords:
  - name_availability
  - postgresqlflexibleservers
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresqlflexibleservers.name_availability" /></td></tr>
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
    <td><a href="#check_globally"><CopyableCode code="check_globally" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the validity and availability of the given name, to assign it to a new server or to use it as the base name of a new pair of virtual endpoints.</td>
</tr>
<tr>
    <td><a href="#check_with_location"><CopyableCode code="check_with_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check the availability of name for resource.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="check_globally"
    values={[
        { label: 'check_globally', value: 'check_globally' },
        { label: 'check_with_location', value: 'check_with_location' }
    ]}
>
<TabItem value="check_globally">

Checks the validity and availability of the given name, to assign it to a new server or to use it as the base name of a new pair of virtual endpoints.

```sql
EXEC azure.postgresqlflexibleservers.name_availability.check_globally 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
<TabItem value="check_with_location">

Check the availability of name for resource.

```sql
EXEC azure.postgresqlflexibleservers.name_availability.check_with_location 
@location_name='{{ location_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
