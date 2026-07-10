--- 
title: resource_changes
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_changes
  - changeanalysis
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

Creates, updates, deletes, gets or lists a <code>resource_changes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_changes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.changeanalysis.resource_changes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="changeType" /></td>
    <td><code>string</code></td>
    <td>The type of the change. Known values are: "Add", "Remove", and "Update".</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedByList" /></td>
    <td><code>array</code></td>
    <td>The list of identities who might initiated the change. The identity could be user name (email address) or the object ID of the Service Principal.</td>
</tr>
<tr>
    <td><CopyableCode code="propertyChanges" /></td>
    <td><code>array</code></td>
    <td>The list of detailed changes at json property level.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource id that the change is attached to.</td>
</tr>
<tr>
    <td><CopyableCode code="timeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the change is detected.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-$startTime"><code>$startTime</code></a>, <a href="#parameter-$endTime"><code>$endTime</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access. List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access.</td>
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
<tr id="parameter-$endTime">
    <td><CopyableCode code="$endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the end time of the changes request. Required.</td>
</tr>
<tr id="parameter-$startTime">
    <td><CopyableCode code="$startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the start time of the changes request. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access. List the changes of a resource within the specified time range. Customer data will be masked if the user doesn't have access.

```sql
SELECT
id,
name,
changeType,
initiatedByList,
propertyChanges,
resourceId,
timeStamp,
type
FROM azure.changeanalysis.resource_changes
WHERE resource_id = '{{ resource_id }}' -- required
AND $startTime = '{{ $startTime }}' -- required
AND $endTime = '{{ $endTime }}' -- required
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>
