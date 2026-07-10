--- 
title: informational_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - informational_operations
  - fileshares
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

Creates, updates, deletes, gets or lists an <code>informational_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="informational_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fileshares.informational_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_provisioning_recommendation"
    values={[
        { label: 'get_provisioning_recommendation', value: 'get_provisioning_recommendation' },
        { label: 'get_usage_data', value: 'get_usage_data' }
    ]}
>
<TabItem value="get_provisioning_recommendation">

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
    <td><CopyableCode code="availableRedundancyOptions" /></td>
    <td><code>array</code></td>
    <td>Redundancy options for the share. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedIOPerSec" /></td>
    <td><code>integer</code></td>
    <td>The recommended value of provisioned IO / sec of the share. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedThroughputMiBPerSec" /></td>
    <td><code>integer</code></td>
    <td>The recommended value of provisioned throughput / sec of the share. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_usage_data">

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
    <td><CopyableCode code="liveShares" /></td>
    <td><code>object</code></td>
    <td>File share usage data for active file shares. Required.</td>
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
    <td><a href="#get_provisioning_recommendation"><CopyableCode code="get_provisioning_recommendation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get file shares provisioning parameters recommendation.</td>
</tr>
<tr>
    <td><a href="#get_usage_data"><CopyableCode code="get_usage_data" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get file shares usage data.</td>
</tr>
<tr>
    <td><a href="#get_limits"><CopyableCode code="get_limits" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get file shares limits.</td>
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
    defaultValue="get_provisioning_recommendation"
    values={[
        { label: 'get_provisioning_recommendation', value: 'get_provisioning_recommendation' },
        { label: 'get_usage_data', value: 'get_usage_data' }
    ]}
>
<TabItem value="get_provisioning_recommendation">

Get file shares provisioning parameters recommendation.

```sql
SELECT
availableRedundancyOptions,
provisionedIOPerSec,
provisionedThroughputMiBPerSec
FROM azure.fileshares.informational_operations
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_usage_data">

Get file shares usage data.

```sql
SELECT
liveShares
FROM azure.fileshares.informational_operations
WHERE location = '{{ location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_limits"
    values={[
        { label: 'get_limits', value: 'get_limits' }
    ]}
>
<TabItem value="get_limits">

Get file shares limits.

```sql
EXEC azure.fileshares.informational_operations.get_limits 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
