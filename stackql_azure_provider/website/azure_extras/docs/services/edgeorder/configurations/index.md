--- 
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - edgeorder
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edgeorder.configurations" /></td></tr>
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
    <td><a href="#list_configurations"><CopyableCode code="list_configurations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-configurationFilters"><code>configurationFilters</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>This method provides the list of configurations for the given product family, product line and product under subscription.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>$skipToken is supported on list of configurations, which provides the next page in the list of configurations. Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="list_configurations"
    values={[
        { label: 'list_configurations', value: 'list_configurations' }
    ]}
>
<TabItem value="list_configurations">

This method provides the list of configurations for the given product family, product line and product under subscription.

```sql
EXEC azure_extras.edgeorder.configurations.list_configurations 
@subscription_id='{{ subscription_id }}' --required, 
@$skipToken='{{ $skipToken }}' 
@@json=
'{
"configurationFilters": "{{ configurationFilters }}", 
"customerSubscriptionDetails": "{{ customerSubscriptionDetails }}"
}'
;
```
</TabItem>
</Tabs>
