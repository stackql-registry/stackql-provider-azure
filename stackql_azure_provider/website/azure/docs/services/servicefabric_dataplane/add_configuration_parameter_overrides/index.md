--- 
title: add_configuration_parameter_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - add_configuration_parameter_overrides
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists an <code>add_configuration_parameter_overrides</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="add_configuration_parameter_overrides" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.add_configuration_parameter_overrides" /></td></tr>
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
    <td><a href="#add_configuration_parameter_overrides"><CopyableCode code="add_configuration_parameter_overrides" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-SectionName"><code>SectionName</code></a>, <a href="#parameter-ParameterName"><code>ParameterName</code></a>, <a href="#parameter-ParameterValue"><code>ParameterValue</code></a></td>
    <td><a href="#parameter-Force"><code>Force</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Adds the list of configuration overrides on the specified node. This api allows adding all existing configuration overrides on the specified node.</td>
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
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
    <td><code>string</code></td>
    <td>The name of the node.</td>
</tr>
<tr id="parameter-Force">
    <td><CopyableCode code="Force" /></td>
    <td><code>boolean</code></td>
    <td>Force adding configuration overrides on specified nodes.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="add_configuration_parameter_overrides"
    values={[
        { label: 'add_configuration_parameter_overrides', value: 'add_configuration_parameter_overrides' }
    ]}
>
<TabItem value="add_configuration_parameter_overrides">

Adds the list of configuration overrides on the specified node. This api allows adding all existing configuration overrides on the specified node.

```sql
EXEC azure.servicefabric_dataplane.add_configuration_parameter_overrides.add_configuration_parameter_overrides 
@node_name='{{ node_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@Force={{ Force }}, 
@timeout='{{ timeout }}' 
@@json=
'{
"SectionName": "{{ SectionName }}", 
"ParameterName": "{{ ParameterName }}", 
"ParameterValue": "{{ ParameterValue }}", 
"Timeout": "{{ Timeout }}", 
"PersistAcrossUpgrade": {{ PersistAcrossUpgrade }}
}'
;
```
</TabItem>
</Tabs>
