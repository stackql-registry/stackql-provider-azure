--- 
title: managed_cluster_version
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_cluster_version
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>managed_cluster_version</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_cluster_version" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.managed_cluster_version" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_environment"
    values={[
        { label: 'get_by_environment', value: 'get_by_environment' },
        { label: 'get', value: 'get' },
        { label: 'list_by_environment', value: 'list_by_environment' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_environment">

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
    <td>The identification of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Cluster operating system, the default will be Windows. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiry of support of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The result resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The identification of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Cluster operating system, the default will be Windows. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiry of support of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The result resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_environment">

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
    <td>The identification of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Cluster operating system, the default will be Windows. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiry of support of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The result resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>The identification of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the result.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterCodeVersion" /></td>
    <td><code>string</code></td>
    <td>The Service Fabric runtime version of the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>Cluster operating system, the default will be Windows. "Windows" (Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="supportExpiryUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of expiry of support of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The result resource type.</td>
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
    <td><a href="#get_by_environment"><CopyableCode code="get_by_environment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-environment"><code>environment</code></a>, <a href="#parameter-cluster_version"><code>cluster_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a Service Fabric cluster code version available for the specified environment. Gets information about an available Service Fabric cluster code version by environment.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-cluster_version"><code>cluster_version</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a Service Fabric managed cluster code version available in the specified location. Gets information about an available Service Fabric managed cluster code version.</td>
</tr>
<tr>
    <td><a href="#list_by_environment"><CopyableCode code="list_by_environment" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-environment"><code>environment</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of Service Fabric cluster code versions available for the specified environment. Gets all available code versions for Service Fabric cluster resources by environment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of Service Fabric cluster code versions available for the specified location. Gets all available code versions for Service Fabric cluster resources by location.</td>
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
<tr id="parameter-cluster_version">
    <td><CopyableCode code="cluster_version" /></td>
    <td><code>string</code></td>
    <td>The cluster code version. Required.</td>
</tr>
<tr id="parameter-environment">
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>The operating system of the cluster. "Windows" Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location for the cluster code versions. This is different from cluster location. Required.</td>
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
    defaultValue="get_by_environment"
    values={[
        { label: 'get_by_environment', value: 'get_by_environment' },
        { label: 'get', value: 'get' },
        { label: 'list_by_environment', value: 'list_by_environment' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_environment">

Gets information about a Service Fabric cluster code version available for the specified environment. Gets information about an available Service Fabric cluster code version by environment.

```sql
SELECT
id,
name,
clusterCodeVersion,
osType,
supportExpiryUtc,
type
FROM azure.service_fabric_managed_clusters.managed_cluster_version
WHERE location = '{{ location }}' -- required
AND environment = '{{ environment }}' -- required
AND cluster_version = '{{ cluster_version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets information about a Service Fabric managed cluster code version available in the specified location. Gets information about an available Service Fabric managed cluster code version.

```sql
SELECT
id,
name,
clusterCodeVersion,
osType,
supportExpiryUtc,
type
FROM azure.service_fabric_managed_clusters.managed_cluster_version
WHERE location = '{{ location }}' -- required
AND cluster_version = '{{ cluster_version }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_environment">

Gets the list of Service Fabric cluster code versions available for the specified environment. Gets all available code versions for Service Fabric cluster resources by environment.

```sql
SELECT
id,
name,
clusterCodeVersion,
osType,
supportExpiryUtc,
type
FROM azure.service_fabric_managed_clusters.managed_cluster_version
WHERE location = '{{ location }}' -- required
AND environment = '{{ environment }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of Service Fabric cluster code versions available for the specified location. Gets all available code versions for Service Fabric cluster resources by location.

```sql
SELECT
id,
name,
clusterCodeVersion,
osType,
supportExpiryUtc,
type
FROM azure.service_fabric_managed_clusters.managed_cluster_version
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
