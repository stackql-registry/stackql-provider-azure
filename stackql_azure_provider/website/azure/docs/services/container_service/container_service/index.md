--- 
title: container_service
hide_title: false
hide_table_of_contents: false
keywords:
  - container_service
  - container_service
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

Creates, updates, deletes, gets or lists a <code>container_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="container_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.container_service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_node_image_versions"
    values={[
        { label: 'list_node_image_versions', value: 'list_node_image_versions' }
    ]}
>
<TabItem value="list_node_image_versions">

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
    <td><CopyableCode code="fullName" /></td>
    <td><code>string</code></td>
    <td>The OS + SKU + version of the node image. Example: AKSUbuntu-1804gen2containerd-2024.02.02.</td>
</tr>
<tr>
    <td><CopyableCode code="os" /></td>
    <td><code>string</code></td>
    <td>The operating system of the node image. Example: AKSUbuntu.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU or flavor of the node image. Example: 2004gen2containerd.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>major.minor.patch version of the node image version release. Example: 2024.02.02.</td>
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
    <td><a href="#list_node_image_versions"><CopyableCode code="list_node_image_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of supported NodeImage versions in the specified subscription. Only returns the latest version of each node image. For example there may be an AKSUbuntu-1804gen2containerd-2024.01.26, but only AKSUbuntu-1804gen2containerd-2024.02.02 is visible in this list.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
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
    defaultValue="list_node_image_versions"
    values={[
        { label: 'list_node_image_versions', value: 'list_node_image_versions' }
    ]}
>
<TabItem value="list_node_image_versions">

Gets a list of supported NodeImage versions in the specified subscription. Only returns the latest version of each node image. For example there may be an AKSUbuntu-1804gen2containerd-2024.01.26, but only AKSUbuntu-1804gen2containerd-2024.02.02 is visible in this list.

```sql
SELECT
fullName,
os,
sku,
version
FROM azure.container_service.container_service
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
