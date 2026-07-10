--- 
title: cluster_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_configurations
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

Creates, updates, deletes, gets or lists a <code>cluster_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.cluster_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_cluster_configuration"
    values={[
        { label: 'get_cluster_configuration', value: 'get_cluster_configuration' }
    ]}
>
<TabItem value="get_cluster_configuration">

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
    <td><CopyableCode code="ClusterConfiguration" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#get_cluster_configuration"><CopyableCode code="get_cluster_configuration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ConfigurationApiVersion"><code>ConfigurationApiVersion</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Get the Service Fabric standalone cluster configuration. The cluster configuration contains properties of the cluster that include different node types on the cluster, security configurations, fault, and upgrade domain topologies, etc.</td>
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
<tr id="parameter-ConfigurationApiVersion">
    <td><CopyableCode code="ConfigurationApiVersion" /></td>
    <td><code>string</code></td>
    <td>The API version of the Standalone cluster json configuration.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_cluster_configuration"
    values={[
        { label: 'get_cluster_configuration', value: 'get_cluster_configuration' }
    ]}
>
<TabItem value="get_cluster_configuration">

Get the Service Fabric standalone cluster configuration. The cluster configuration contains properties of the cluster that include different node types on the cluster, security configurations, fault, and upgrade domain topologies, etc.

```sql
SELECT
ClusterConfiguration
FROM azure.servicefabric_dataplane.cluster_configurations
WHERE ConfigurationApiVersion = '{{ ConfigurationApiVersion }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
