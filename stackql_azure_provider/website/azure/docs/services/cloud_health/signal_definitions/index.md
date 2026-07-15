--- 
title: signal_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_definitions
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

Creates, updates, deletes, gets or lists a <code>signal_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="signal_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_health.signal_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_health_model', value: 'list_by_health_model' }
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
    <td><CopyableCode code="dataUnit" /></td>
    <td><code>string</code></td>
    <td>Unit of the signal result (e.g. Bytes, MilliSeconds, Percent, Count)).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationRules" /></td>
    <td><code>object</code></td>
    <td>Evaluation rules for the signal definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshInterval" /></td>
    <td><code>string</code></td>
    <td>Interval in which the signal is being evaluated. Defaults to PT1M (1 minute). Known values are: "PT1M", "PT5M", "PT10M", "PT30M", "PT1H", and "PT2H". (PT1M, PT5M, PT10M, PT30M, PT1H, PT2H)</td>
</tr>
<tr>
    <td><CopyableCode code="signalKind" /></td>
    <td><code>string</code></td>
    <td>Kind of the signal definition. Required. Known values are: "AzureResourceMetric", "LogAnalyticsQuery", "PrometheusMetricsQuery", and "External".</td>
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
    <td><CopyableCode code="dataUnit" /></td>
    <td><code>string</code></td>
    <td>Unit of the signal result (e.g. Bytes, MilliSeconds, Percent, Count)).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationRules" /></td>
    <td><code>object</code></td>
    <td>Evaluation rules for the signal definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Creating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshInterval" /></td>
    <td><code>string</code></td>
    <td>Interval in which the signal is being evaluated. Defaults to PT1M (1 minute). Known values are: "PT1M", "PT5M", "PT10M", "PT30M", "PT1H", and "PT2H". (PT1M, PT5M, PT10M, PT30M, PT1H, PT2H)</td>
</tr>
<tr>
    <td><CopyableCode code="signalKind" /></td>
    <td><code>string</code></td>
    <td>Kind of the signal definition. Required. Known values are: "AzureResourceMetric", "LogAnalyticsQuery", "PrometheusMetricsQuery", and "External".</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-signal_definition_name"><code>signal_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a SignalDefinition.</td>
</tr>
<tr>
    <td><a href="#list_by_health_model"><CopyableCode code="list_by_health_model" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td>List SignalDefinition resources by HealthModel.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-signal_definition_name"><code>signal_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a SignalDefinition.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-signal_definition_name"><code>signal_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a SignalDefinition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-health_model_name"><code>health_model_name</code></a>, <a href="#parameter-signal_definition_name"><code>signal_definition_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a SignalDefinition.</td>
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
<tr id="parameter-signal_definition_name">
    <td><CopyableCode code="signal_definition_name" /></td>
    <td><code>string</code></td>
    <td>Name of the signal definition. Must be unique within a health model. Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_health_model', value: 'list_by_health_model' }
    ]}
>
<TabItem value="get">

Get a SignalDefinition.

```sql
SELECT
id,
name,
dataUnit,
displayName,
evaluationRules,
provisioningState,
refreshInterval,
signalKind,
systemData,
tags,
type
FROM azure.cloud_health.signal_definitions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND health_model_name = '{{ health_model_name }}' -- required
AND signal_definition_name = '{{ signal_definition_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_health_model">

List SignalDefinition resources by HealthModel.

```sql
SELECT
id,
name,
dataUnit,
displayName,
evaluationRules,
provisioningState,
refreshInterval,
signalKind,
systemData,
tags,
type
FROM azure.cloud_health.signal_definitions
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

Create a SignalDefinition.

```sql
INSERT INTO azure.cloud_health.signal_definitions (
properties,
resource_group_name,
health_model_name,
signal_definition_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ health_model_name }}',
'{{ signal_definition_name }}',
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
- name: signal_definitions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the signal_definitions resource.
    - name: health_model_name
      value: "{{ health_model_name }}"
      description: Required parameter for the signal_definitions resource.
    - name: signal_definition_name
      value: "{{ signal_definition_name }}"
      description: Required parameter for the signal_definitions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the signal_definitions resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        displayName: "{{ displayName }}"
        signalKind: "{{ signalKind }}"
        refreshInterval: "{{ refreshInterval }}"
        tags: "{{ tags }}"
        dataUnit: "{{ dataUnit }}"
        evaluationRules:
          degradedRule:
            operator: "{{ operator }}"
            threshold: {{ threshold }}
          unhealthyRule:
            operator: "{{ operator }}"
            threshold: {{ threshold }}
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

Create a SignalDefinition.

```sql
REPLACE azure.cloud_health.signal_definitions
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND health_model_name = '{{ health_model_name }}' --required
AND signal_definition_name = '{{ signal_definition_name }}' --required
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

Delete a SignalDefinition.

```sql
DELETE FROM azure.cloud_health.signal_definitions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND health_model_name = '{{ health_model_name }}' --required
AND signal_definition_name = '{{ signal_definition_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
