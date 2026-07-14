--- 
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - kubernetes_configuration
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

Creates, updates, deletes, gets or lists an <code>operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operation_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.operation_status" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified ID for the async operation.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the async operation.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>If present, details of the operation error.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Additional information, if available.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Operation status. Required.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-extension_name"><code>extension_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Async Operation status.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the kubernetes cluster. Required.</td>
</tr>
<tr id="parameter-cluster_resource_name">
    <td><CopyableCode code="cluster_resource_name" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters, appliances. Required.</td>
</tr>
<tr id="parameter-cluster_rp">
    <td><CopyableCode code="cluster_rp" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.</td>
</tr>
<tr id="parameter-extension_name">
    <td><CopyableCode code="extension_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Extension. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get Async Operation status.

```sql
SELECT
id,
name,
error,
properties,
status
FROM azure.kubernetes_configuration.operation_status
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND extension_name = '{{ extension_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
