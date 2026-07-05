--- 
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - authorization
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

Creates, updates, deletes, gets or lists an <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alerts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="alertConfiguration" /></td>
    <td><code>object</code></td>
    <td>The alert configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="alertDefinition" /></td>
    <td><code>object</code></td>
    <td>The alert definition.</td>
</tr>
<tr>
    <td><CopyableCode code="alertIncidents" /></td>
    <td><code>array</code></td>
    <td>The alert incidents.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentCount" /></td>
    <td><code>integer</code></td>
    <td>The number of generated incidents of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>False by default; true if the alert is active.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the alert configuration was updated or new incidents were generated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastScannedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the alert was last scanned.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The alert scope.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_scope">

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
    <td><CopyableCode code="alertConfiguration" /></td>
    <td><code>object</code></td>
    <td>The alert configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="alertDefinition" /></td>
    <td><code>object</code></td>
    <td>The alert definition.</td>
</tr>
<tr>
    <td><CopyableCode code="alertIncidents" /></td>
    <td><code>array</code></td>
    <td>The alert incidents.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentCount" /></td>
    <td><code>integer</code></td>
    <td>The number of generated incidents of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>False by default; true if the alert is active.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the alert configuration was updated or new incidents were generated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastScannedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the alert was last scanned.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The alert scope.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Get the specified alert.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Gets alerts for a resource scope.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Update an alert.</td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Refresh an alert.</td>
</tr>
<tr>
    <td><a href="#refresh_all"><CopyableCode code="refresh_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Refresh all alerts for a resource scope.</td>
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
<tr id="parameter-alert_id">
    <td><CopyableCode code="alert_id" /></td>
    <td><code>string</code></td>
    <td>The name of the alert to get. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
    ]}
>
<TabItem value="get">

Get the specified alert.

```sql
SELECT
id,
name,
alertConfiguration,
alertDefinition,
alertIncidents,
incidentCount,
isActive,
lastModifiedDateTime,
lastScannedDateTime,
scope,
systemData,
type
FROM azure.authorization.alerts
WHERE scope = '{{ scope }}' -- required
AND alert_id = '{{ alert_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_scope">

Gets alerts for a resource scope.

```sql
SELECT
id,
name,
alertConfiguration,
alertDefinition,
alertIncidents,
incidentCount,
isActive,
lastModifiedDateTime,
lastScannedDateTime,
scope,
systemData,
type
FROM azure.authorization.alerts
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an alert.

```sql
UPDATE azure.authorization.alerts
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND alert_id = '{{ alert_id }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh"
    values={[
        { label: 'refresh', value: 'refresh' },
        { label: 'refresh_all', value: 'refresh_all' }
    ]}
>
<TabItem value="refresh">

Refresh an alert.

```sql
EXEC azure.authorization.alerts.refresh 
@scope='{{ scope }}' --required, 
@alert_id='{{ alert_id }}' --required
;
```
</TabItem>
<TabItem value="refresh_all">

Refresh all alerts for a resource scope.

```sql
EXEC azure.authorization.alerts.refresh_all 
@scope='{{ scope }}' --required
;
```
</TabItem>
</Tabs>
