--- 
title: event
hide_title: false
hide_table_of_contents: false
keywords:
  - event
  - recovery_services_data_replication
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

Creates, updates, deletes, gets or lists an <code>event</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="event" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_data_replication.event" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event correlation Id.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Event model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event description.</td>
</tr>
<tr>
    <td><CopyableCode code="eventName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event name.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event type.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the errors associated with this event.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the event. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event severity.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfOccurrence" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the time at which the event occurred at source.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event correlation Id.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Event model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event description.</td>
</tr>
<tr>
    <td><CopyableCode code="eventName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event name.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event type.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the errors associated with this event.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the event. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the event severity.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeOfOccurrence" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the time at which the event occurred at source.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-event_name"><code>event_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the event.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-odataOptions"><code>odataOptions</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a></td>
    <td>Gets the list of events in the given vault.</td>
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
<tr id="parameter-event_name">
    <td><CopyableCode code="event_name" /></td>
    <td><code>string</code></td>
    <td>The event name. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The vault name. Required.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token. Default value is None.</td>
</tr>
<tr id="parameter-odataOptions">
    <td><CopyableCode code="odataOptions" /></td>
    <td><code>string</code></td>
    <td>OData options. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Page size. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details of the event.

```sql
SELECT
id,
name,
correlationId,
customProperties,
description,
eventName,
eventType,
healthErrors,
provisioningState,
resourceName,
resourceType,
severity,
systemData,
timeOfOccurrence,
type
FROM azure.recovery_services_data_replication.event
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND event_name = '{{ event_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of events in the given vault.

```sql
SELECT
id,
name,
correlationId,
customProperties,
description,
eventName,
eventType,
healthErrors,
provisioningState,
resourceName,
resourceType,
severity,
systemData,
timeOfOccurrence,
type
FROM azure.recovery_services_data_replication.event
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND odataOptions = '{{ odataOptions }}'
AND continuationToken = '{{ continuationToken }}'
AND pageSize = '{{ pageSize }}'
;
```
</TabItem>
</Tabs>
