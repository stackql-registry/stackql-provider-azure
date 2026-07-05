--- 
title: occurrence_extension
hide_title: false
hide_table_of_contents: false
keywords:
  - occurrence_extension
  - computeschedule
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

Creates, updates, deletes, gets or lists an <code>occurrence_extension</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="occurrence_extension" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.computeschedule.occurrence_extension" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_occurrence_by_vms"
    values={[
        { label: 'list_occurrence_by_vms', value: 'list_occurrence_by_vms' }
    ]}
>
<TabItem value="list_occurrence_by_vms">

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
    <td><CopyableCode code="errorDetails" /></td>
    <td><code>object</code></td>
    <td>Error details for the resource. Only populated if resource is in failed state.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSettings" /></td>
    <td><code>array</code></td>
    <td>The desired notification settings for the specified resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current state of the resource. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The ARM Id of the resource. "subscriptions/&#123;subId&#125;/resourceGroups/&#123;rgName&#125;/providers/Microsoft.Compute/virtualMachines/&#123;vmName&#125;". Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledActionId" /></td>
    <td><code>string</code></td>
    <td>The arm identifier of the scheduled action the occurrence belongs to. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the occurrence is scheduled for the resource. Specified in UTC. Required.</td>
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
    <td><a href="#list_occurrence_by_vms"><CopyableCode code="list_occurrence_by_vms" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>List OccurrenceExtensionResource resources by parent.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_occurrence_by_vms"
    values={[
        { label: 'list_occurrence_by_vms', value: 'list_occurrence_by_vms' }
    ]}
>
<TabItem value="list_occurrence_by_vms">

List OccurrenceExtensionResource resources by parent.

```sql
SELECT
id,
name,
errorDetails,
notificationSettings,
provisioningState,
resourceId,
scheduledActionId,
scheduledTime,
systemData,
type
FROM azure.computeschedule.occurrence_extension
WHERE resource_uri = '{{ resource_uri }}' -- required
;
```
</TabItem>
</Tabs>
