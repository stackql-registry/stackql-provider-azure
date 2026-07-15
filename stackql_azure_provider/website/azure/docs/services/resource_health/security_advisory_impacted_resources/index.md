--- 
title: security_advisory_impacted_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - security_advisory_impacted_resources
  - resource_health
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

Creates, updates, deletes, gets or lists a <code>security_advisory_impacted_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_advisory_impacted_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_health.security_advisory_impacted_resources" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_subscription_id_and_event_id"
    values={[
        { label: 'list_by_subscription_id_and_event_id', value: 'list_by_subscription_id_and_event_id' },
        { label: 'list_by_tenant_id_and_event_id', value: 'list_by_tenant_id_and_event_id' }
    ]}
>
<TabItem value="list_by_subscription_id_and_event_id">

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
    <td><CopyableCode code="info" /></td>
    <td><code>array</code></td>
    <td>Additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRegion" /></td>
    <td><code>string</code></td>
    <td>Impacted resource region name.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Identity for resource within Microsoft cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type within Microsoft cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_tenant_id_and_event_id">

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
    <td><CopyableCode code="info" /></td>
    <td><code>array</code></td>
    <td>Additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetRegion" /></td>
    <td><code>string</code></td>
    <td>Impacted resource region name.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceId" /></td>
    <td><code>string</code></td>
    <td>Identity for resource within Microsoft cloud.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>Resource type within Microsoft cloud.</td>
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
    <td><a href="#list_by_subscription_id_and_event_id"><CopyableCode code="list_by_subscription_id_and_event_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists impacted resources in the subscription by an event (Security Advisory).</td>
</tr>
<tr>
    <td><a href="#list_by_tenant_id_and_event_id"><CopyableCode code="list_by_tenant_id_and_event_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists impacted resources in the tenant by an event (Security Advisory).</td>
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
<tr id="parameter-event_tracking_id">
    <td><CopyableCode code="event_tracking_id" /></td>
    <td><code>string</code></td>
    <td>Event Id which uniquely identifies ServiceHealth event. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. For more information please see `https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN `_. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_subscription_id_and_event_id"
    values={[
        { label: 'list_by_subscription_id_and_event_id', value: 'list_by_subscription_id_and_event_id' },
        { label: 'list_by_tenant_id_and_event_id', value: 'list_by_tenant_id_and_event_id' }
    ]}
>
<TabItem value="list_by_subscription_id_and_event_id">

Lists impacted resources in the subscription by an event (Security Advisory).

```sql
SELECT
id,
name,
info,
systemData,
targetRegion,
targetResourceId,
targetResourceType,
type
FROM azure.resource_health.security_advisory_impacted_resources
WHERE event_tracking_id = '{{ event_tracking_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_tenant_id_and_event_id">

Lists impacted resources in the tenant by an event (Security Advisory).

```sql
SELECT
id,
name,
info,
systemData,
targetRegion,
targetResourceId,
targetResourceType,
type
FROM azure.resource_health.security_advisory_impacted_resources
WHERE event_tracking_id = '{{ event_tracking_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
