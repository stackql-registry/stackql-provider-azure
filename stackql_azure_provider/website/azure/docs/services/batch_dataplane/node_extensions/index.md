--- 
title: node_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - node_extensions
  - batch_dataplane
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

Creates, updates, deletes, gets or lists a <code>node_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="node_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.node_extensions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_extension"
    values={[
        { label: 'get_node_extension', value: 'get_node_extension' },
        { label: 'list_node_extensions', value: 'list_node_extensions' }
    ]}
>
<TabItem value="get_node_extension">

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
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The vm extension instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual machine extension.</td>
</tr>
<tr>
    <td><CopyableCode code="vmExtension" /></td>
    <td><code>object</code></td>
    <td>The configuration for virtual machine extensions.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_node_extensions">

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
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The vm extension instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the virtual machine extension.</td>
</tr>
<tr>
    <td><CopyableCode code="vmExtension" /></td>
    <td><code>object</code></td>
    <td>The configuration for virtual machine extensions.</td>
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
    <td><a href="#get_node_extension"><CopyableCode code="get_node_extension" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Gets information about the specified Compute Node Extension. Gets information about the specified Compute Node Extension.</td>
</tr>
<tr>
    <td><a href="#list_node_extensions"><CopyableCode code="list_node_extensions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-node_id"><code>node_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$select"><code>$select</code></a></td>
    <td>Lists the Compute Nodes Extensions in the specified Pool. Lists the Compute Nodes Extensions in the specified Pool.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-extension_name">
    <td><CopyableCode code="extension_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Compute Node Extension that you want to get information about. Required.</td>
</tr>
<tr id="parameter-node_id">
    <td><CopyableCode code="node_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Compute Node that you want to list extensions. Required.</td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Pool that contains Compute Node. Required.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>An OData $select clause. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. A maximum of 1000 applications can be returned. Default value is None.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_node_extension"
    values={[
        { label: 'get_node_extension', value: 'get_node_extension' },
        { label: 'list_node_extensions', value: 'list_node_extensions' }
    ]}
>
<TabItem value="get_node_extension">

Gets information about the specified Compute Node Extension. Gets information about the specified Compute Node Extension.

```sql
SELECT
instanceView,
provisioningState,
vmExtension
FROM azure.batch_dataplane.node_extensions
WHERE pool_id = '{{ pool_id }}' -- required
AND node_id = '{{ node_id }}' -- required
AND extension_name = '{{ extension_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND $select = '{{ $select }}'
;
```
</TabItem>
<TabItem value="list_node_extensions">

Lists the Compute Nodes Extensions in the specified Pool. Lists the Compute Nodes Extensions in the specified Pool.

```sql
SELECT
instanceView,
provisioningState,
vmExtension
FROM azure.batch_dataplane.node_extensions
WHERE pool_id = '{{ pool_id }}' -- required
AND node_id = '{{ node_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $select = '{{ $select }}'
;
```
</TabItem>
</Tabs>
