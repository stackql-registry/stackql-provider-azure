--- 
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
  - impactreporting
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

Creates, updates, deletes, gets or lists an <code>insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="insights" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.impactreporting.insights" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="additionalDetails" /></td>
    <td><code>object</code></td>
    <td>additional details of the insight.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>category of the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>Contains title & description for the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the event that has been correlated with this insight. This can be used to aggregate insights for the same event.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time of the event, which has been correlated the impact.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>Identifier that can be used to group similar insights.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>object</code></td>
    <td>details of of the impact for which insight has been generated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="insightUniqueId" /></td>
    <td><code>string</code></td>
    <td>unique id of the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>status of the insight. example resolved, repaired, other.</td>
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
<TabItem value="list_by_subscription">

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
    <td><CopyableCode code="additionalDetails" /></td>
    <td><code>object</code></td>
    <td>additional details of the insight.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>category of the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>Contains title & description for the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eventId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the event that has been correlated with this insight. This can be used to aggregate insights for the same event.</td>
</tr>
<tr>
    <td><CopyableCode code="eventTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time of the event, which has been correlated the impact.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>Identifier that can be used to group similar insights.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>object</code></td>
    <td>details of of the impact for which insight has been generated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="insightUniqueId" /></td>
    <td><code>string</code></td>
    <td>unique id of the insight. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Resource provisioning state. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>status of the insight. example resolved, repaired, other.</td>
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
    <td><a href="#parameter-workload_impact_name"><code>workload_impact_name</code></a>, <a href="#parameter-insight_name"><code>insight_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Insight resources by workloadImpactName and insightName.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workload_impact_name"><code>workload_impact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Insight resources by workloadImpactName.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workload_impact_name"><code>workload_impact_name</code></a>, <a href="#parameter-insight_name"><code>insight_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create Insight resource, This is Admin only operation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workload_impact_name"><code>workload_impact_name</code></a>, <a href="#parameter-insight_name"><code>insight_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete Insight resource, This is Admin only operation.</td>
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
<tr id="parameter-insight_name">
    <td><CopyableCode code="insight_name" /></td>
    <td><code>string</code></td>
    <td>Name of the insight. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workload_impact_name">
    <td><CopyableCode code="workload_impact_name" /></td>
    <td><code>string</code></td>
    <td>workloadImpact resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get Insight resources by workloadImpactName and insightName.

```sql
SELECT
id,
name,
additionalDetails,
category,
content,
eventId,
eventTime,
groupId,
impact,
insightUniqueId,
provisioningState,
status,
systemData,
type
FROM azure.impactreporting.insights
WHERE workload_impact_name = '{{ workload_impact_name }}' -- required
AND insight_name = '{{ insight_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List Insight resources by workloadImpactName.

```sql
SELECT
id,
name,
additionalDetails,
category,
content,
eventId,
eventTime,
groupId,
impact,
insightUniqueId,
provisioningState,
status,
systemData,
type
FROM azure.impactreporting.insights
WHERE workload_impact_name = '{{ workload_impact_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create Insight resource, This is Admin only operation.

```sql
INSERT INTO azure.impactreporting.insights (
properties,
workload_impact_name,
insight_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ workload_impact_name }}',
'{{ insight_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: insights
  props:
    - name: workload_impact_name
      value: "{{ workload_impact_name }}"
      description: Required parameter for the insights resource.
    - name: insight_name
      value: "{{ insight_name }}"
      description: Required parameter for the insights resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the insights resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        category: "{{ category }}"
        status: "{{ status }}"
        eventId: "{{ eventId }}"
        groupId: "{{ groupId }}"
        content:
          title: "{{ title }}"
          description: "{{ description }}"
        eventTime: "{{ eventTime }}"
        insightUniqueId: "{{ insightUniqueId }}"
        impact:
          impactedResourceId: "{{ impactedResourceId }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
          impactId: "{{ impactId }}"
        additionalDetails: "{{ additionalDetails }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete Insight resource, This is Admin only operation.

```sql
DELETE FROM azure.impactreporting.insights
WHERE workload_impact_name = '{{ workload_impact_name }}' --required
AND insight_name = '{{ insight_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
