--- 
title: resource_set_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_set_rules
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

Creates, updates, deletes, gets or lists a <code>resource_set_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_set_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview_administration.resource_set_rules" /></td></tr>
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
    <td><a href="#list_resource_set_rules"><CopyableCode code="list_resource_set_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a resource set config service model.</td>
</tr>
<tr>
    <td><a href="#get_resource_set_rule"><CopyableCode code="get_resource_set_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a resource set config service model.</td>
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
    defaultValue="list_resource_set_rules"
    values={[
        { label: 'list_resource_set_rules', value: 'list_resource_set_rules' },
        { label: 'get_resource_set_rule', value: 'get_resource_set_rule' }
    ]}
>
<TabItem value="list_resource_set_rules">

Get a resource set config service model.

```sql
EXEC azure.purview_administration.resource_set_rules.list_resource_set_rules 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="get_resource_set_rule">

Get a resource set config service model.

```sql
EXEC azure.purview_administration.resource_set_rules.get_resource_set_rule 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
