--- 
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - maintenance
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

Creates, updates, deletes, gets or lists a <code>updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="updates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.updates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_parent"
    values={[
        { label: 'list_parent', value: 'list_parent' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_parent">

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
    <td><CopyableCode code="impactDurationInSec" /></td>
    <td><code>integer</code></td>
    <td>Duration of impact in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="impactType" /></td>
    <td><code>string</code></td>
    <td>The impact type. Known values are: "None", "Freeze", "Restart", and "Redeploy". (None, Freeze, Restart, Redeploy)</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceScope" /></td>
    <td><code>string</code></td>
    <td>The impact area. Known values are: "Host", "Resource", "OSImage", "Extension", "InGuestPatch", "SQLDB", and "SQLManagedInstance". (Host, Resource, OSImage, Extension, InGuestPatch, SQLDB, SQLManagedInstance)</td>
</tr>
<tr>
    <td><CopyableCode code="notBefore" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when Azure will start force updates if not self-updated by customer before this time.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resourceId.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Pending", "InProgress", "Completed", "RetryNow", "RetryLater", "NoUpdatesPending", "Cancel", and "Cancelled". (Pending, InProgress, Completed, RetryNow, RetryLater, NoUpdatesPending, Cancel, Cancelled)</td>
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
    <td><CopyableCode code="impactDurationInSec" /></td>
    <td><code>integer</code></td>
    <td>Duration of impact in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="impactType" /></td>
    <td><code>string</code></td>
    <td>The impact type. Known values are: "None", "Freeze", "Restart", and "Redeploy". (None, Freeze, Restart, Redeploy)</td>
</tr>
<tr>
    <td><CopyableCode code="maintenanceScope" /></td>
    <td><code>string</code></td>
    <td>The impact area. Known values are: "Host", "Resource", "OSImage", "Extension", "InGuestPatch", "SQLDB", and "SQLManagedInstance". (Host, Resource, OSImage, Extension, InGuestPatch, SQLDB, SQLManagedInstance)</td>
</tr>
<tr>
    <td><CopyableCode code="notBefore" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when Azure will start force updates if not self-updated by customer before this time.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resourceId.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status. Known values are: "Pending", "InProgress", "Completed", "RetryNow", "RetryLater", "NoUpdatesPending", "Cancel", and "Cancelled". (Pending, InProgress, Completed, RetryNow, RetryLater, NoUpdatesPending, Cancel, Cancelled)</td>
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
    <td><a href="#list_parent"><CopyableCode code="list_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_parent_type"><code>resource_parent_type</code></a>, <a href="#parameter-resource_parent_name"><code>resource_parent_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Updates to resource. Get updates to resources.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Updates to resource. Get updates to resources.</td>
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
<tr id="parameter-provider_name">
    <td><CopyableCode code="provider_name" /></td>
    <td><code>string</code></td>
    <td>Resource provider name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>Resource identifier. Required.</td>
</tr>
<tr id="parameter-resource_parent_name">
    <td><CopyableCode code="resource_parent_name" /></td>
    <td><code>string</code></td>
    <td>Resource parent identifier. Required.</td>
</tr>
<tr id="parameter-resource_parent_type">
    <td><CopyableCode code="resource_parent_type" /></td>
    <td><code>string</code></td>
    <td>Resource parent type. Required.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Resource type. Required.</td>
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
    defaultValue="list_parent"
    values={[
        { label: 'list_parent', value: 'list_parent' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_parent">

Get Updates to resource. Get updates to resources.

```sql
SELECT
impactDurationInSec,
impactType,
maintenanceScope,
notBefore,
resourceId,
status
FROM azure.maintenance.updates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provider_name = '{{ provider_name }}' -- required
AND resource_parent_type = '{{ resource_parent_type }}' -- required
AND resource_parent_name = '{{ resource_parent_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get Updates to resource. Get updates to resources.

```sql
SELECT
impactDurationInSec,
impactType,
maintenanceScope,
notBefore,
resourceId,
status
FROM azure.maintenance.updates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provider_name = '{{ provider_name }}' -- required
AND resource_type = '{{ resource_type }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
