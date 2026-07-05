--- 
title: consumer_source_data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_source_data_sets
  - datashare
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

Creates, updates, deletes, gets or lists a <code>consumer_source_data_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="consumer_source_data_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.datashare.consumer_source_data_sets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_share_subscription"
    values={[
        { label: 'list_by_share_subscription', value: 'list_by_share_subscription' }
    ]}
>
<TabItem value="list_by_share_subscription">

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
    <td>The resource id of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetId" /></td>
    <td><code>string</code></td>
    <td>DataSet Id.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetLocation" /></td>
    <td><code>string</code></td>
    <td>Location of the data set.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetName" /></td>
    <td><code>string</code></td>
    <td>DataSet name.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetPath" /></td>
    <td><code>string</code></td>
    <td>DataSet path.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSetType" /></td>
    <td><code>string</code></td>
    <td>Type of data set. Known values are: "Blob", "Container", "BlobFolder", "AdlsGen2FileSystem", "AdlsGen2Folder", "AdlsGen2File", "AdlsGen1Folder", "AdlsGen1File", "KustoCluster", "KustoDatabase", "SqlDBTable", "SqlDWTable", and "SynapseWorkspaceSqlPoolTable".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>System Data of the Azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the azure resource.</td>
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
    <td><a href="#list_by_share_subscription"><CopyableCode code="list_by_share_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-share_subscription_name"><code>share_subscription_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Get source dataSets of a shareSubscription. Get source dataSets of a shareSubscription.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the share account. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-share_subscription_name">
    <td><CopyableCode code="share_subscription_name" /></td>
    <td><code>string</code></td>
    <td>The name of the shareSubscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_share_subscription"
    values={[
        { label: 'list_by_share_subscription', value: 'list_by_share_subscription' }
    ]}
>
<TabItem value="list_by_share_subscription">

Get source dataSets of a shareSubscription. Get source dataSets of a shareSubscription.

```sql
SELECT
id,
name,
dataSetId,
dataSetLocation,
dataSetName,
dataSetPath,
dataSetType,
systemData,
type
FROM azure.datashare.consumer_source_data_sets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND share_subscription_name = '{{ share_subscription_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
