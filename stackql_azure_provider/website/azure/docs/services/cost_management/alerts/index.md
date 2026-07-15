--- 
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - cost_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.alerts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_external', value: 'list_external' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="closeTime" /></td>
    <td><code>string</code></td>
    <td>dateTime in which alert was closed.</td>
</tr>
<tr>
    <td><CopyableCode code="costEntityId" /></td>
    <td><code>string</code></td>
    <td>related budget.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string</code></td>
    <td>dateTime in which alert was created.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>defines the type of alert.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Alert description.</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>object</code></td>
    <td>Alert details.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="modificationTime" /></td>
    <td><code>string</code></td>
    <td>dateTime in which alert was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of alert. Known values are: "Preset" and "User". (Preset, User)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>alert status. Known values are: "None", "Active", "Overridden", "Resolved", and "Dismissed". (None, Active, Overridden, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="statusModificationTime" /></td>
    <td><code>string</code></td>
    <td>dateTime in which the alert status was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="statusModificationUserName" /></td>
    <td><code>string</code></td>
    <td>User who last modified the alert.</td>
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
<TabItem value="list_external">

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
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>URL to get the next set of alerts results if there are any.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>List of alerts.</td>
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
    <td><CopyableCode code="nextLink" /></td>
    <td><code>string</code></td>
    <td>URL to get the next set of alerts results if there are any.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>List of alerts.</td>
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
    <td>Gets the alert for the scope by alert ID.</td>
</tr>
<tr>
    <td><a href="#list_external"><CopyableCode code="list_external" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-external_cloud_provider_type"><code>external_cloud_provider_type</code></a>, <a href="#parameter-external_cloud_provider_id"><code>external_cloud_provider_id</code></a></td>
    <td></td>
    <td>Lists the Alerts for external cloud provider type defined.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Lists the alerts for scope defined.</td>
</tr>
<tr>
    <td><a href="#dismiss"><CopyableCode code="dismiss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Dismisses the specified alert.</td>
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
    <td>Alert ID. Required.</td>
</tr>
<tr id="parameter-external_cloud_provider_id">
    <td><CopyableCode code="external_cloud_provider_id" /></td>
    <td><code>string</code></td>
    <td>This can be '&#123;externalSubscriptionId&#125;' for linked account or '&#123;externalBillingAccountId&#125;' for consolidated account used with dimension/query operations. Required.</td>
</tr>
<tr id="parameter-external_cloud_provider_type">
    <td><CopyableCode code="external_cloud_provider_type" /></td>
    <td><code>string</code></td>
    <td>The external cloud provider type associated with dimension/query operations. This includes 'externalSubscriptions' for linked account and 'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions" and "externalBillingAccounts". Required.</td>
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
        { label: 'list_external', value: 'list_external' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the alert for the scope by alert ID.

```sql
SELECT
id,
name,
closeTime,
costEntityId,
creationTime,
definition,
description,
details,
eTag,
modificationTime,
source,
status,
statusModificationTime,
statusModificationUserName,
systemData,
type
FROM azure.cost_management.alerts
WHERE scope = '{{ scope }}' -- required
AND alert_id = '{{ alert_id }}' -- required
;
```
</TabItem>
<TabItem value="list_external">

Lists the Alerts for external cloud provider type defined.

```sql
SELECT
nextLink,
value
FROM azure.cost_management.alerts
WHERE external_cloud_provider_type = '{{ external_cloud_provider_type }}' -- required
AND external_cloud_provider_id = '{{ external_cloud_provider_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the alerts for scope defined.

```sql
SELECT
nextLink,
value
FROM azure.cost_management.alerts
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="dismiss"
    values={[
        { label: 'dismiss', value: 'dismiss' }
    ]}
>
<TabItem value="dismiss">

Dismisses the specified alert.

```sql
EXEC azure.cost_management.alerts.dismiss 
@scope='{{ scope }}' --required, 
@alert_id='{{ alert_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
