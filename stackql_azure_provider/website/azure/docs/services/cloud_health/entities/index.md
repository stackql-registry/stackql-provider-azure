--- 
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
  - cloud_health
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

Creates, updates, deletes, gets or lists an <code>entities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_health.entities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_signal_history"
    values={[
        { label: 'get_signal_history', value: 'get_signal_history' },
        { label: 'get', value: 'get' },
        { label: 'list_by_health_model', value: 'list_by_health_model' }
    ]}
>
<TabItem value="get_signal_history">

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
    <td><CopyableCode code="entityName" /></td>
    <td><code>string</code></td>
    <td>Name of the entity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="history" /></td>
    <td><code>array</code></td>
    <td>Signal history data points. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="signalName" /></td>
    <td><code>string</code></td>
    <td>Name of the signal. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="alerts" /></td>
    <td><code>object</code></td>
    <td>Alert configuration for this entity.</td>
</tr>
<tr>
    <td><CopyableCode code="canvasPosition" /></td>
    <td><code>object</code></td>
    <td>Positioning of the entity on the model canvas.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveredBy" /></td>
    <td><code>string</code></td>
    <td>Discovered by which discovery rule. If set, the entity cannot be deleted manually.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthObjective" /></td>
    <td><code>number</code></td>
    <td>Health objective as a percentage of time the entity should be healthy.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Health state of this entity. Known values are: "Healthy", "Degraded", "Unhealthy", "Unknown", and "Deleted". (Healthy, Degraded, Unhealthy, Unknown, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="icon" /></td>
    <td><code>object</code></td>
    <td>Visual icon definition. If not set, a default icon is used.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>string</code></td>
    <td>Impact of the entity in health state propagation. Known values are: "Standard", "Limited", and "Suppressed". (Standard, Limited, Suppressed)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="signalGroups" /></td>
    <td><code>object</code></td>
    <td>Signal groups which are assigned to this entity.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Optional set of tags (key-value pairs).</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_health_model">

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
    <td><CopyableCode code="alerts" /></td>
    <td><code>object</code></td>
    <td>Alert configuration for this entity.</td>
</tr>
<tr>
    <td><CopyableCode code="canvasPosition" /></td>
    <td><code>object</code></td>
    <td>Positioning of the entity on the model canvas.</td>
</tr>
<tr>
    <td><CopyableCode code="discoveredBy" /></td>
    <td><code>string</code></td>
    <td>Discovered by which discovery rule. If set, the entity cannot be deleted manually.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthObjective" /></td>
    <td><code>number</code></td>
    <td>Health objective as a percentage of time the entity should be healthy.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Health state of this entity. Known values are: "Healthy", "Degraded", "Unhealthy", "Unknown", and "Deleted". (Healthy, Degraded, Unhealthy, Unknown, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="icon" /></td>
    <td><code>object</code></td>
    <td>Visual icon definition. If not set, a default icon is used.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>string</code></td>
    <td>Impact of the entity in health state propagation. Known values are: "Standard", "Limited", and "Suppressed". (Standard, Limited, Suppressed)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="signalGroups" /></td>
    <td><code>object</code></td>
    <td>Signal groups which are assigned to this entity.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Optional set of tags (key-value pairs).</td>
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
    <td><a href="#get_signal_history"><CopyableCode code="get_signal_history" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the time series history for a signal on an entity.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Entity.</td>
</tr>
<tr>
    <td><a href="#list_by_health_model"><CopyableCode code="list_by_health_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td>List Entity resources by HealthModel.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Entity.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Entity.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Entity.</td>
</tr>
<tr>
    <td><a href="#get_history"><CopyableCode code="get_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the health state transition history for an entity.</td>
</tr>
<tr>
    <td><a href="#ingest_health_report"><CopyableCode code="ingest_health_report" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-signalName"><code>signalName</code></a>, <a href="#parameter-healthState"><code>healthState</code></a></td>
    <td></td>
    <td>Ingest a health report for a specific signal on an entity (the entity must already exist).</td>
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
<tr id="parameter-entity_name">
    <td><CopyableCode code="entity_name" /></td>
    <td><code>string</code></td>
    <td>Name of the entity. Must be unique within a health model. Required.</td>
</tr>
<tr id="parameter-health_model_name">
    <td><CopyableCode code="health_model_name" /></td>
    <td><code>string</code></td>
    <td>Name of health model resource. Required.</td>
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
<tr id="parameter-timestamp">
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp to use for the operation. When specified, the version of the resource at this point in time is retrieved. If not specified, the latest version is used. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_signal_history"
    values={[
        { label: 'get_signal_history', value: 'get_signal_history' },
        { label: 'get', value: 'get' },
        { label: 'list_by_health_model', value: 'list_by_health_model' }
    ]}
>
<TabItem value="get_signal_history">

Retrieve the time series history for a signal on an entity.

```sql
SELECT
entityName,
history,
signalName
FROM azure.cloud_health.entities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND health_model_name = '{{ health_model_name }}' -- required
AND entity_name = '{{ entity_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a Entity.

```sql
SELECT
id,
name,
alerts,
canvasPosition,
discoveredBy,
displayName,
healthObjective,
healthState,
icon,
impact,
provisioningState,
signalGroups,
systemData,
tags,
type
FROM azure.cloud_health.entities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND health_model_name = '{{ health_model_name }}' -- required
AND entity_name = '{{ entity_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_health_model">

List Entity resources by HealthModel.

```sql
SELECT
id,
name,
alerts,
canvasPosition,
discoveredBy,
displayName,
healthObjective,
healthState,
icon,
impact,
provisioningState,
signalGroups,
systemData,
tags,
type
FROM azure.cloud_health.entities
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND health_model_name = '{{ health_model_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND timestamp = '{{ timestamp }}'
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

Create a Entity.

```sql
INSERT INTO azure.cloud_health.entities (
properties,
resource_group_name,
health_model_name,
entity_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ health_model_name }}',
'{{ entity_name }}',
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
- name: entities
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the entities resource.
    - name: health_model_name
      value: "{{ health_model_name }}"
      description: Required parameter for the entities resource.
    - name: entity_name
      value: "{{ entity_name }}"
      description: Required parameter for the entities resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the entities resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        displayName: "{{ displayName }}"
        canvasPosition:
          x: {{ x }}
          y: {{ y }}
        icon:
          iconName: "{{ iconName }}"
          customData: "{{ customData }}"
        healthObjective: {{ healthObjective }}
        impact: "{{ impact }}"
        tags: "{{ tags }}"
        signalGroups:
          azureResource:
            authenticationSetting: "{{ authenticationSetting }}"
            azureResourceId: "{{ azureResourceId }}"
            azureResourceKind: "{{ azureResourceKind }}"
            signals:
              - signalKind: "{{ signalKind }}"
                name: "{{ name }}"
                signalDefinitionName: "{{ signalDefinitionName }}"
                status:
                  healthState: "{{ healthState }}"
                  value: {{ value }}
                  reportedAt: "{{ reportedAt }}"
                  error: "{{ error }}"
                metricNamespace: "{{ metricNamespace }}"
                metricName: "{{ metricName }}"
                timeGrain: "{{ timeGrain }}"
                aggregationType: "{{ aggregationType }}"
                dimension: "{{ dimension }}"
                dimensionFilter: "{{ dimensionFilter }}"
                displayName: "{{ displayName }}"
                refreshInterval: "{{ refreshInterval }}"
                dataUnit: "{{ dataUnit }}"
                evaluationRules:
                  degradedRule: "{{ degradedRule }}"
                  unhealthyRule: "{{ unhealthyRule }}"
          azureLogAnalytics:
            authenticationSetting: "{{ authenticationSetting }}"
            logAnalyticsWorkspaceResourceId: "{{ logAnalyticsWorkspaceResourceId }}"
            signals:
              - signalKind: "{{ signalKind }}"
                name: "{{ name }}"
                signalDefinitionName: "{{ signalDefinitionName }}"
                status:
                  healthState: "{{ healthState }}"
                  value: {{ value }}
                  reportedAt: "{{ reportedAt }}"
                  error: "{{ error }}"
                queryText: "{{ queryText }}"
                timeGrain: "{{ timeGrain }}"
                valueColumnName: "{{ valueColumnName }}"
                displayName: "{{ displayName }}"
                refreshInterval: "{{ refreshInterval }}"
                dataUnit: "{{ dataUnit }}"
                evaluationRules:
                  degradedRule: "{{ degradedRule }}"
                  unhealthyRule: "{{ unhealthyRule }}"
          azureMonitorWorkspace:
            authenticationSetting: "{{ authenticationSetting }}"
            azureMonitorWorkspaceResourceId: "{{ azureMonitorWorkspaceResourceId }}"
            signals:
              - signalKind: "{{ signalKind }}"
                name: "{{ name }}"
                signalDefinitionName: "{{ signalDefinitionName }}"
                status:
                  healthState: "{{ healthState }}"
                  value: {{ value }}
                  reportedAt: "{{ reportedAt }}"
                  error: "{{ error }}"
                queryText: "{{ queryText }}"
                timeGrain: "{{ timeGrain }}"
                displayName: "{{ displayName }}"
                refreshInterval: "{{ refreshInterval }}"
                dataUnit: "{{ dataUnit }}"
                evaluationRules:
                  degradedRule: "{{ degradedRule }}"
                  unhealthyRule: "{{ unhealthyRule }}"
          dependencies:
            aggregationType: "{{ aggregationType }}"
            degradedThreshold: {{ degradedThreshold }}
            unhealthyThreshold: {{ unhealthyThreshold }}
            unit: "{{ unit }}"
            ignoreUnknown: {{ ignoreUnknown }}
          external:
            signals:
              - signalKind: "{{ signalKind }}"
                name: "{{ name }}"
                signalDefinitionName: "{{ signalDefinitionName }}"
                status:
                  healthState: "{{ healthState }}"
                  value: {{ value }}
                  reportedAt: "{{ reportedAt }}"
                  error: "{{ error }}"
                evaluationRules:
                  degradedRule: "{{ degradedRule }}"
                  unhealthyRule: "{{ unhealthyRule }}"
        discoveredBy: "{{ discoveredBy }}"
        healthState: "{{ healthState }}"
        alerts:
          unhealthy:
            severity: "{{ severity }}"
            description: "{{ description }}"
            actionGroupIds:
              - "{{ actionGroupIds }}"
          degraded:
            severity: "{{ severity }}"
            description: "{{ description }}"
            actionGroupIds:
              - "{{ actionGroupIds }}"
`}</CodeBlock>

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

Create a Entity.

```sql
REPLACE azure.cloud_health.entities
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND health_model_name = '{{ health_model_name }}' --required
AND entity_name = '{{ entity_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Delete a Entity.

```sql
DELETE FROM azure.cloud_health.entities
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND health_model_name = '{{ health_model_name }}' --required
AND entity_name = '{{ entity_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_history"
    values={[
        { label: 'get_history', value: 'get_history' },
        { label: 'ingest_health_report', value: 'ingest_health_report' }
    ]}
>
<TabItem value="get_history">

Retrieve the health state transition history for an entity.

```sql
EXEC azure.cloud_health.entities.get_history 
@resource_group_name='{{ resource_group_name }}' --required, 
@health_model_name='{{ health_model_name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startAt": "{{ startAt }}", 
"endAt": "{{ endAt }}"
}'
;
```
</TabItem>
<TabItem value="ingest_health_report">

Ingest a health report for a specific signal on an entity (the entity must already exist).

```sql
EXEC azure.cloud_health.entities.ingest_health_report 
@resource_group_name='{{ resource_group_name }}' --required, 
@health_model_name='{{ health_model_name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"signalName": "{{ signalName }}", 
"healthState": "{{ healthState }}", 
"value": {{ value }}, 
"evaluationRules": "{{ evaluationRules }}", 
"expiresInMinutes": {{ expiresInMinutes }}, 
"additionalContext": "{{ additionalContext }}"
}'
;
```
</TabItem>
</Tabs>
