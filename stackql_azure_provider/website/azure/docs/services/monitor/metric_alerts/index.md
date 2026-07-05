--- 
title: metric_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts
  - monitor
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

Creates, updates, deletes, gets or lists a <code>metric_alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metric_alerts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metric_alerts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="actionProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of an action properties.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="autoMitigate" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the alert should be auto resolved or not. The default is true.</td>
</tr>
<tr>
    <td><CopyableCode code="criteria" /></td>
    <td><code>object</code></td>
    <td>Defines the specific alert criteria information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of an alert payload.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the metric alert that will be included in the alert email.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the metric alert is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationFrequency" /></td>
    <td><code>string</code></td>
    <td>How often the metric alert is evaluated represented in ISO 8601 duration format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isMigrated" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether this alert rule is migrated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the rule was updated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resolveConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration for how the alert is resolved. Applicable for PromQLCriteria.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of resource id's that this metric alert is scoped to. You cannot change the scope of a metric rule based on logs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>integer</code></td>
    <td>Alert severity &#123;0, 1, 2, 3, 4&#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceRegion" /></td>
    <td><code>string</code></td>
    <td>The region of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>The resource type of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="windowSize" /></td>
    <td><code>string</code></td>
    <td>The period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="actionProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of an action properties.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="autoMitigate" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the alert should be auto resolved or not. The default is true.</td>
</tr>
<tr>
    <td><CopyableCode code="criteria" /></td>
    <td><code>object</code></td>
    <td>Defines the specific alert criteria information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of an alert payload.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the metric alert that will be included in the alert email.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the metric alert is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationFrequency" /></td>
    <td><code>string</code></td>
    <td>How often the metric alert is evaluated represented in ISO 8601 duration format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isMigrated" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether this alert rule is migrated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the rule was updated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resolveConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration for how the alert is resolved. Applicable for PromQLCriteria.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of resource id's that this metric alert is scoped to. You cannot change the scope of a metric rule based on logs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>integer</code></td>
    <td>Alert severity &#123;0, 1, 2, 3, 4&#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceRegion" /></td>
    <td><code>string</code></td>
    <td>The region of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>The resource type of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="windowSize" /></td>
    <td><code>string</code></td>
    <td>The period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold.</td>
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
    <td><CopyableCode code="actionProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of an action properties.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="autoMitigate" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the alert should be auto resolved or not. The default is true.</td>
</tr>
<tr>
    <td><CopyableCode code="criteria" /></td>
    <td><code>object</code></td>
    <td>Defines the specific alert criteria information. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>The properties of an alert payload.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the metric alert that will be included in the alert email.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>The flag that indicates whether the metric alert is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationFrequency" /></td>
    <td><code>string</code></td>
    <td>How often the metric alert is evaluated represented in ISO 8601 duration format. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="isMigrated" /></td>
    <td><code>boolean</code></td>
    <td>The value indicating whether this alert rule is migrated.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the rule was updated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="resolveConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration for how the alert is resolved. Applicable for PromQLCriteria.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of resource id's that this metric alert is scoped to. You cannot change the scope of a metric rule based on logs. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>integer</code></td>
    <td>Alert severity &#123;0, 1, 2, 3, 4&#125;. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceRegion" /></td>
    <td><code>string</code></td>
    <td>The region of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>The resource type of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="windowSize" /></td>
    <td><code>string</code></td>
    <td>The period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve an alert rule definition.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve alert rule definitions in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve alert rule definitions in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an metric alert definition.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an metric alert definition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create or update an metric alert definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an alert rule definition.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the rule. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieve an alert rule definition.

```sql
SELECT
id,
name,
actionProperties,
actions,
autoMitigate,
criteria,
customProperties,
description,
enabled,
evaluationFrequency,
identity,
isMigrated,
lastUpdatedTime,
location,
resolveConfiguration,
scopes,
severity,
systemData,
tags,
targetResourceRegion,
targetResourceType,
type,
windowSize
FROM azure.monitor.metric_alerts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieve alert rule definitions in a resource group.

```sql
SELECT
id,
name,
actionProperties,
actions,
autoMitigate,
criteria,
customProperties,
description,
enabled,
evaluationFrequency,
identity,
isMigrated,
lastUpdatedTime,
location,
resolveConfiguration,
scopes,
severity,
systemData,
tags,
targetResourceRegion,
targetResourceType,
type,
windowSize
FROM azure.monitor.metric_alerts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieve alert rule definitions in a subscription.

```sql
SELECT
id,
name,
actionProperties,
actions,
autoMitigate,
criteria,
customProperties,
description,
enabled,
evaluationFrequency,
identity,
isMigrated,
lastUpdatedTime,
location,
resolveConfiguration,
scopes,
severity,
systemData,
tags,
targetResourceRegion,
targetResourceType,
type,
windowSize
FROM azure.monitor.metric_alerts
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an metric alert definition.

```sql
INSERT INTO azure.monitor.metric_alerts (
tags,
location,
properties,
identity,
resource_group_name,
rule_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: metric_alerts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the metric_alerts resource.
    - name: rule_name
      value: "{{ rule_name }}"
      description: Required parameter for the metric_alerts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the metric_alerts resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The alert rule properties of the resource. Required.
      value:
        description: "{{ description }}"
        severity: {{ severity }}
        enabled: {{ enabled }}
        scopes:
          - "{{ scopes }}"
        evaluationFrequency: "{{ evaluationFrequency }}"
        windowSize: "{{ windowSize }}"
        targetResourceType: "{{ targetResourceType }}"
        targetResourceRegion: "{{ targetResourceRegion }}"
        criteria:
          odata:
            type: "{{ type }}"
        autoMitigate: {{ autoMitigate }}
        resolveConfiguration:
          autoResolved: {{ autoResolved }}
          timeToResolve: "{{ timeToResolve }}"
        actions:
          - actionGroupId: "{{ actionGroupId }}"
            webHookProperties: "{{ webHookProperties }}"
        lastUpdatedTime: "{{ lastUpdatedTime }}"
        isMigrated: {{ isMigrated }}
        customProperties: "{{ customProperties }}"
        actionProperties: "{{ actionProperties }}"
    - name: identity
      description: |
        The identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

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

Update an metric alert definition.

```sql
UPDATE azure.monitor.metric_alerts
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Create or update an metric alert definition.

```sql
REPLACE azure.monitor.metric_alerts
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
tags,
type;
```
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

Delete an alert rule definition.

```sql
DELETE FROM azure.monitor.metric_alerts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND rule_name = '{{ rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
